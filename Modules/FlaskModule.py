from flask import render_template
from flask import Flask, Response
import threading

class EndpointAction(object):
    
    def __init__(self, action):
        self.action = action

    def __call__(self, *args):
        # Perform the action
        answer = self.action()
        # Create the answer (bundle it in a correctly formatted HTTP answer)
        self.response = Response(answer, status=200, headers={})
        # Send it
        return self.response

class FlaskModule():
    def __init__(self,name):
        self.flaskapp = Flask(name)
        self.flaskapp.config['TEMPLATES_AUTO_RELOAD'] = True
        self.flaskapp.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
        self.flaskapp.debug = False
        self.flaskapp.use_reloader=False
        self.flask_thread = None

    def run(self,BootError):
        if not BootError:
            self.add_all_endpoints()
        else:
            self.add_error_endpoint()
            
        self.flask_thread = threading.Thread(target=self.flaskapp.run,kwargs={"host":"0.0.0.0","port":5000})
        self.flask_thread.daemon = True
        self.flask_thread.start()

    def add_error_endpoint(self):
        self.flaskapp.register_error_handler(404,self.page_not_found)

    def add_all_endpoints(self):
        # Add root endpoint
        self.add_endpoint(endpoint="/", endpoint_name="/", handler=self.InitFlask)
        self.add_endpoint(endpoint="/test", endpoint_name="/test", handler=self.Test)

        # Add action endpoints
        #self.add_endpoint(endpoint="/add_X", endpoint_name="/add_X", handler=self.add_X)
        # you can add more ... 
        self.flaskapp.register_error_handler(404,self.page_not_found)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.flaskapp.add_url_rule(endpoint, endpoint_name, EndpointAction(handler)) 
        # You can also add options here : "... , methods=['POST'], ... "

# ==================== ------ API Calls ------- ====================
    def InitFlask(self):
        # Dummy action
        return render_template('home.html')
        # Test it with curl 127.0.0.1:5000

    def Test(self):
        return render_template('test.html')

    def page_not_found(self,Error):
        # Dummy action
        return "Oops Something Went Wrong!"
        # Test it with curl 127.0.0.1:5000/add_X

# app = Flask(__name__)
# print("Flask Started.")

# @app.route("/")
# def home():
#     return render_template('home.html')

# @app.route("/page_2")
# def page_2():
#     return render_template('page_2.html')

# app.run(host="0.0.0.0",port=5000)