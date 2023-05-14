"""For Gunicorn

Created on Thu Sep  9 17:01:11 2021

@author: link477"""

from .server import app
application = app

if __name__ == '__main__':
    app.run()
