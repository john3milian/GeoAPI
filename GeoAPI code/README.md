
# GeoAPI

A python API which takes in address and return coordiates or location of the
 given address using Google's GeocodeAPI.

# Installation

The API has been made using the following libraries:

- Flask 
- requests 
- request 
- Api from flask_restful
- Resource from flask_restful
- xml.etree.ElementTree


 Flask - Creates a server on the machine it is running on. For this
 app it will be running on local host server of the machine in which
 it is installed in.

 requests - will send the information to the server from a point or event
 whenever the request is made. This will be done securely so that no leakage
 of data occurs. For this the built in method 'POST' is used

 request - will parse out what data was sent alongside the post request, 
 which cannnot be seen in the url but it is present there and has reached 
 the server successfully.

 Api - It provides our Flask 'app' or server to have an api functionality such 
 as creating restful api(s)

-Resource - Resource creates resources for the api; such as post functions.
It is on the server side

-xml.etree.ElementTree - Used to convert python strings to an XML tree and
 document.

 If a module is not present,
  -  pip install (any missing libraries)
  - or just go to the folder, type 'cmd' in address
    bar of the folder & press enter (this will open the directory directly in command prompt)
    and inside cmd console, type  >> pip install -r requirements.txt

# Usage

 The project has two files GeoAPI.py and test.py.
 
 GeoAPI.py will be the server side. It will handle POST requests
 and return location data in string format

 &

 test.py will be the client side. It will send the address provided
 by the user and in return will show the response send by the host

- Step1: Run the server 
  - open command prompt and locate the file directory which will
    look like: >>C:\Users\HP\Desktop\GeoAPI code JOHN EMILIAN MINJ>
  - inside the file directory, write >>python GeoAPI.py (make sure you
    have python installed; and writing python before file is important)
  - The server would start and you should be able to see:
  
      * Serving Flask app "GeoAPI"
      * Environment: production
      WARNING: This is a development server. Do not use it in a production deployment.
      Use a production WSGI server instead.
      * Debug mode: off
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

- Step2: Run the client
  - open another command prompt and locate the file directory as mentioned above
    in Step1.
  - inside file directory, write >>python test.py
  - It will ask to enter address and file format type.
    After entering it will give results in either a .txt file or a .xml
    file in the relative file path i.e. the folder where both the
    python files GeoAPI.py and test.py are present.

# Support

I have not created many exception cases, so restart the server and client
to fix any problem.

Otherwise contact or post at https://github.com/john3milian

# Roadmap

The current version of program works but it can be improved further.
I will be adding some exception cases to avoid server crashes.

# Sources

- The stackoverflow.com forums
- docs.python requests documentation
- docs.python xml.etree.ElementTree documentation

  
 
