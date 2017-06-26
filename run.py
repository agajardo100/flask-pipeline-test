import os

from app import create_app

"""
This is the application's entry point. 
Run this file to start the Flask server and launch application.
"""

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()