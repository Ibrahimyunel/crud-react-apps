from flask_package import app

@app.route('/name/<string:myname>')
def name(myname):
    return 'my name is {}'.format(myname)