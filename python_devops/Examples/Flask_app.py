# Install flask package and import the Flask class
from flask import Flask

# Common step for all Flask-based Python apps: create a Flask app instance
app = Flask(__name__)   # __name__ must NOT have spaces

# Decorator used to invoke a specific route before the actual function triggers
@app.route('/')
def Radha():
    return 'Hello, God bless you!'

# Run the Flask app on particular URL
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  
  
    
# Default port for flask app is 5000
# if you wnat to customize the flask port
# app.run(0.0.0.0, port = 3000)   

