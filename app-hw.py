from flask import Flask,jsonify,request

app = Flask(__name__)

contacts = [
    {
        "id":1,
        "Contact":"9705116262",
        "Name":"Prasanna",
        "done":False
    },

    {
        "id":2,
        "Contact":"987654321",
        "Name":"Sujitha",
        "done":False
    },
]

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please Provide The Data"
        },400)
    contact = {
        "id":contacts[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"Contact added successfully"
    })
if(__name__ == "__main__"):
    app.run(debug = True)