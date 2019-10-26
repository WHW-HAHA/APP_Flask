'''
portal: Only trigger the server and app
'''

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug= app.config['DEBUG'])
