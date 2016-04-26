# needed for cloud 9
import os


#-----------------------
from flask import Flask
app = Flask(__name__)

#route
@app.route('/')
def hello_world():
    return 'hello world!'
    

# test sos
# being called from terminal
#.run creates a waiting server
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port)
    
    
    
    