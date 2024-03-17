# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/me")
def home():

    name = "Me" 
    age = "14" 

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/dad")
def home2():

    name = "Dad" 
    age = "48" 

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mom")
def home3():

    name = "Mom"
    age = "40" 

    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def home4():

    name = "Friend" 
    age = "14"

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
