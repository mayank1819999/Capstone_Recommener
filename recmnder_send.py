# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:40:59 2020

@author: MAYANK
"""


from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# define empty list
places = []

# open file and read the content in a list
with open('your_file.txt', 'r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        current_place = line[:-1]

        # add item to the list
        l=list( current_place.split("-"))
        places.append(l[:-1])

lst="olive oil" 
rem=""

print(rem)


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    baskt=[ data.split(',')]
    baskt=baskt[0]
    for i in places:
            if lst in i:
                for j in i:
                    if j not in baskt:
                        rem=j
                        return jsonify({"recomnd":rem})
    print(baskt)
       
    return jsonify({"recomnd":rem})
    
if __name__ == "__main__":
    app.run(debug=False)
