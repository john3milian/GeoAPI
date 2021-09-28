# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 09:49:36 2021

@author: HP
"""

import requests

print("")                                                                      #User Interface just for demo purposes-
print("Enter Address that you want to know the location of:")                  #-Directly change address and format below-
address_input = input(str)                                                     #-for automation.:)
print("")
print("Either Type json for JSON format file or Type xml for XML format file:")
format_input = input(str)
print("")
print("Got it!")


DATA = {"address" : address_input,                                             # Change address here
        "output_format" : format_input}                                        # Change output format here

BASE = "http://127.0.0.1:5000/"
url = requests.post(BASE + "getAddressDetails", DATA)


#url.raise_for_status()
if DATA["output_format"] == "json":
                                             
    response_json = str(url.json())  
    print(response_json)
    location_json_file = open('JSON_location.txt', 'w')                        # file JSON_location.txt
    location_json_file.seek(0)
    location_json_file.truncate()
    location_json_file.write(response_json)
    location_json_file.close()
    print("\nfile saved as JSON_location.txt in the relative path\n")
    
    
elif DATA["output_format"] == "xml": 

    xml_output = url.text                                                      # xml Response from server
    xml_output = xml_output.replace('"','')
    print(xml_output)
    #print(type(xml_output))
    
    location_xml_file = open('XML_location.xml', 'w')                          #file XML_location.xml
    location_xml_file.seek(0)                    
    location_xml_file.truncate()
    location_xml_file.write(xml_output)
    location_xml_file.close()
    print("\nfile saved as XML_location.xml in the relative path\n")

else:
    print("invalid output format. Try json or xml\n")


#print(response_post.json())
#input('Press ENTER to exit')

