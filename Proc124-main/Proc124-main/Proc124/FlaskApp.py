from flask import Flask,jsonify,request
app = Flask(__name__)

contacts=[
    {
        'id':1,
        'contact':u'347-233-8119',
        'name':u'Raju',
        'done':False
    },
    {
        'id':2,
        'contact':u'347-233-8120',
        'name':u'Rose',
        'done':False
    },
    {
        'id':3,
        'contact':u'347-233-8121',
        'name':u'Monu',
        'done':False
    },
    {
        'id':4,
        'contact':u'347-233-8122',
        'name':u'Aniket',
        'done':False
    }
]


@app.route("/add-data",methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message": "Please provide the data"
        },400)

    contact = {
            'id':contacts[-1]['id']+1,
            'name':request.json['name'],
            'contact':request.json.get('contact',""),
            'done':False
        }

    contacts.append(contact)
    return jsonify({
        "status" : "success",
        "message": "contact number added successfully"
    })

@app.route("/get-data")
def get_contacts():
    return jsonify({
        "data":contacts
    })


if(__name__ == "__main__"):
    app.run(debug=True)