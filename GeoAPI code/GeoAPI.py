# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 09:19:40 2021

@author: johnemilian
"""
from flask import Flask, request
import requests
from flask_restful import Api, Resource
import xml.etree.ElementTree as ET

BASE = "https://maps.googleapis.com/maps/api/geocode/"
API_KEY = ""    #PUT YOU GOOGLE GEOAPI CODE HERE

app = Flask(__name__)                                                          # creates server app
api = Api(app)

class GeoLocation(Resource):                                                   # This class handles all API processes,- 
                                                                               # -requests, and return required response
    
    def post(self):                                                            # API is set for POST requests 
        post_request = {"output_format": request.form["output_format"],
                        "address": request.form["address"]}
        params = {"address" : post_request["address"],
                  "key" : API_KEY
                  }
        
        response = requests.post(BASE + post_request["output_format"] +"?", params= params)
        
        if post_request["output_format"] == 'json':                            # Parsing for JSON data
            response = response.json()                                          
            geometry = (response['results'][0]['geometry'])
            results = {"coordinates" : geometry['location'],
                       "address" : post_request["address"]
                       }
            
            return results                                                     # Sends back JSON data
        
        else: 
            response = response.content                                        # Parsing for XML data
            response_xml = ET.fromstring(response)
            lat_response = response_xml.findall("./result/geometry/location/lat")
            #print(lat_response[0].text)
            lat_response = lat_response[0].text                               # data for XML tree
            #print(lat_response_)
            lng_response = response_xml.findall("./result/geometry/location/lng")
            lng_response = lng_response[0].text                                # data for XML tree
            
            lat = ET.Element('lat')                                            # All XML Elements        
            lat.text = lat_response
            #print("lat ok")
            
            lng = ET.Element('lng')     
            lng.text = lng_response
            #print("lng ok")
            
            address = ET.Element('address')
            address.text = params['address']
            #print("address ok")

            coordinates = ET.Element('coordinates')
            coordinates.append(lat)
            coordinates.append(lng)
            #print("coordinates ok")
            
            root = ET.Element('root')
            root.append(address)
            root.append(coordinates)                                           # root is final XMLtree
            tree_ = ET.tostring(root, encoding="unicode")                      #'tree_' and 'root' have to be type string
            #print(tree_)
            #print(type(tree_))
            #print("OK")
            return tree_                                                       
            
            
api.add_resource(GeoLocation, "/getAddressDetails")                            # '/getAddressDetails' is the unique-
                                                                               #  -url identifier for the API

if __name__ == "__main__":                                                     # Initialises server and updates if there-
    app.run(debug=False)                                                        # changes in the code(only if debug=True)
