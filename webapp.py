frome flask import Flask, request,Markup,render_template,flash, Markup
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
   for State in counties:
    if county["State"] in myList:
     myList=county["State"] 
    for State in myList:
     options += Markup("<option value=\"" + State + "\">" + State + "</option>")
return options
  
def funFact(State):
    first= counties [0]["County"]
     for counties in State:
          if county["County"]< first:
               first= county["County"]
     return first
 
     
   
  
    
