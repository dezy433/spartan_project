from flask import Flask,request,jsonify

flask_object = Flask(__name__)

@flask_object.route('/')
def home_page():
    welcome = "Welcome to the Devops Server\n"
    tutorial = ("\nAPI is an interface that allows your application to interact with an external service using a simple set of commands.\n You do not need to know the internal logic of the service, just send a simple command and the service will return the necessary data.")
    description = (welcome+"\n"+tutorial)
    return description
if __name__ == "__main__":


    flask_object.run()