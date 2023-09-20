import re
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <!--<span>House of Metazord</span>-->
        <body>
        <center><img src="https://i.ibb.co/DQzNLqR/Metazord-Logo.png" alt="Metazord-Logo" border="0" width="300" height="252"></cemter>

        
        <style>
        
            body {background-color: #ffffff;}
            input[type=text] {width: 300px; padding: 12px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;}
            input[type=submit] {width: 100px; background-color: #f79204; color: white; padding: 14px 20px; margin: 8px 0; border: none; border-radius: 4px; cursor: pointer; font-color: black;}
            input[type=submit]:hover {background-color: #45a049;}

            @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');

            span {
            font-family: 'Bebas Neue', cursive;
            font-size: 3em;
            position: absolute;
            top: 8%;
            left: 48%;
            transform: translate(-50%,-50%);
            background-image: linear-gradient(gold, gold);
            background-size: 100% 10px;
            background-repeat: no-repeat;
            background-position: 100% 0%;
            transition: background-size .7s, background-position .5s ease-in-out;
            }

            span:hover {
            background-size: 100% 100%;
            background-position: 0% 100%;
            transition: background-position .7s, background-size .5s ease-in-out;
            }
            .button {
            color: #ecf0f1;
            font-size: 17px;
            background-color: #e67e22;
            border: 1px solid #f39c12;
            border-radius: 5px;
            padding: 10px;
            box-shadow: 0px 6px 0px #d35400;
            transition: all .1s;
            }

            .button:active {
            box-shadow: 0px 2px 0px #d35400;
            position: relative;
            top: 2px;
            }
        </style>
        <center>
        <!--<button>Hello World<button>-->
        <a href="/welcome"><button class="button">Welcome to Metazord</button></a>
        
        </center>
        </body>
        </html>
        
    '''

@app.route('/welcome')
def welcome():
    return ''' 
    <h1> DevOps</h1>
    <h1> Robotic Process Automation</h1>
    <h1> Blockchain</h1>
    <h1> ArVr</h1>
    '''

if __name__ == "__main__":
    app.run(debug=True)
