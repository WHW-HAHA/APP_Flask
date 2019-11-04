'''
portal: Only trigger the server and app
'''

from app import create_app

app = create_app()

@app.route('/')
def hello_world():
    pass

if __name__ == '__main__':
    app.run(debug= app.config['DEBUG'])
