from flask import Flask, request,Markup,render_template,flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_home():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    if 'State' in request.args:
        State=(request.args['State'])
        return render_template('home.html', options=get_state_options(counties), funFact=funFact(State))
    return render_template('home.html', options=get_state_options(counties))
def get_state_options(counties):
    myList=[]
    for county in counties:
        if not county["State"] in myList:
            myList.append(county["State"] )
    options=""
    for State in myList:
        options += Markup("<option value=\"" + State + "\">" + State + "</option>")
    return options
  
def funFact(State):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    first= counties [0]["County"]
    for county in counties:
        if county["County"]< first and county["State"]== State:
            first= county["County"]
    last= counties [0]["County"]
    for county in counties:
        if county["County"]> last and  county["State"]== State:
            last= county["County"]
    return first + " "+last
    
if __name__=="__main__":
    app.run(debug=True)
    

  
     
   
  
    
