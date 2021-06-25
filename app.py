from flask import Flask, render_template

#using template import render template library,



# define  app using the flask import
app = Flask(__name__)


# route home directiory / default is home directory 
# end point returns string hello world python strong just returning from endpoint
# calling the render template that was importated
@app.route('/')
def hell_world():
    #
    title = "Dont Test Me"
    # variable of state to vist equaling a list of differnt string values "string"
    
    states_to_visit =[
        "Texas",
        "Oregon",
        "New York"
        "Florida"
    ]
    # make a seprate dir so render template will work.
    # passing state  to visit to state to visit connecting to the list
    # now i am able to loop over data which is in index.html
    return render_template('index.html', title=title, states_to_visit=states_to_visit)


# built in web server to run flask appliction

# export FLASK_APP=app.py 