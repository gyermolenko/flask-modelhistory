from decimal import Decimal
from functools import partial

from flask import Blueprint
from flask import render_template, redirect, url_for, request
from sqlalchemy import event
from sqlalchemy.orm.attributes import get_history
from flask.ext.login import current_user

from app import app
from app import db
from .models import HistoryModel


class History(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # BP registration is needed only to find history template path
        history_blueprint = Blueprint('history_blueprint', __name__, template_folder='templates')
        app.register_blueprint(history_blueprint, url_prefix="/history")


    def track_changes(self, model, alias='empty', fields=None, decorator=None):
        app.add_url_rule('/%s/<int:obj_id>/history' % alias, 'show_history_%s' % alias, decorator(self.show_history))
        event.listen(model, 'after_insert', partial(self.tracker, db_alias=alias, fields=fields, is_new=True))
        event.listen(model, 'after_update', partial(self.tracker, db_alias=alias, fields=fields, is_new=False))


    def show_history(self, obj_id):
        obj_type = request.path.split('/')[1]
        if obj_id and obj_type:
            history = db.session.query(HistoryModel) \
                                .filter(HistoryModel.object_type == obj_type) \
                                .filter(HistoryModel.object_id == obj_id) \
                                .order_by(HistoryModel.date)
            return render_template('history.html', history=history)

        return redirect(url_for('home'))


    def tracker(self, mapper, connection, target, db_alias='some_object', fields=None, is_new=False):
        if is_new:
            fields_with_changes = fields
        else:
            fields_with_changes = []
            for field in fields:
                if get_history(target, field).deleted:
                    fields_with_changes.append(field)

        updates = {}
        for field in fields_with_changes:
            new_value = getattr(target, field)
            if type(new_value) is Decimal:
                updates[field] = str(new_value)
            else:
                updates[field] = new_value

        if updates:
            db_table = HistoryModel.__table__
            object_type = db_alias

            connection.execute(
                db_table.insert(),
                dict(
                    user_id=current_user.id,
                    object_type=object_type,
                    object_id=target.id,
                    data=updates,
                )
            )

