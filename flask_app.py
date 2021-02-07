# imports
from flask import Flask,jsonify, request

# intiating flask
app = Flask(__name__)

# contact list
contact_list = [
    {
        'id': 1,
        'name': u'Hari',
        'contact': u'7878787878', 
        'done': False
    },
    {
        'id': 2,
        'name': u'Aditya',
        'contact': u'9787878787', 
        'done': False
    }
]

# app route and adding contact
@app.route("/add", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    contact_list.append(contact)
    return jsonify({
        "status":"success",
        "message": "Successfully added Contact."
    })
    
# app route and getting contacts
@app.route("/get")
def get_task():
    return jsonify({
        "data" : contact_list
    }) 

# running the app
if (__name__ == "__main__"):
    app.run(debug=True)
