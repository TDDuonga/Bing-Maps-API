from flask import Flask,request, render_template
from flask_cors import CORS
import convertJSON as cj
import astar as algo
import json
import math
from flask import jsonify  # Importing jsonify for JSON response

app = Flask(__name__)
CORS(app)


@app.route('/calculate', methods=['GET'])
def home():
    # if
    raw_input = request.args.get('pntdata').split(',')
    inputSourceLoc = (float(raw_input[0]), float(raw_input[1])) 
    inputDestLoc = (float(raw_input[2]), float(raw_input[3]))
    
    mappedSourceLoc = cj.getKNN(inputSourceLoc)
    mappedDestLoc = cj.getKNN(inputDestLoc)
    
    path = algo.aStar(mappedSourceLoc, mappedDestLoc)
    finalPath, cost = cj.getResponsePathDict(path, mappedSourceLoc, mappedDestLoc)
    
    print("Chi phí của đường đi (km): " + str(cost))
    
    # Creating a dictionary to hold both finalPath and cost
    response_data = {
        "finalPath": finalPath,
        "cost": cost
    }
    
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')