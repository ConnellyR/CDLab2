frome flask import Flask, request,Markup,render_template,flash, Markup
import os
import json

 app = Flask(__name__)

 @app.route("/")
 def render_home():
  with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('home.html')
get_state_options(counties)
myList[]
   for State in counties
    if county["State"] in myList[]:
     myList[]=county["State"] 
    for State in myList[]:
     options += Markup("<option value=\"" + State + "\">" + State + "</option>")
     
  
   
    
