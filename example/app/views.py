from app import app

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/test")
def testview():
    return "Hello World!"


