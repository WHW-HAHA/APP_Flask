'''
portal
'''
from flask import Flask


app = Flask(__name__) # with a name
app.config.from_object('config') # path of the module

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug= app.config['DEBUG'], port = 81)
