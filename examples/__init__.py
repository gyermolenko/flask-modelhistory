from flask import Flask
from flask.ext.login import login_required
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


from model_history import History

history = History(app)
tracked_fields = ['status', 'digits']
history.track_changes(MyModel, alias='mymodel', fields=tracked_fields, decorator=login_required)

