from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient("mongodb://localhost:27017/")
db = client["todoDB"]
collection = db["todos"]


@app.route('/submittodoitem', methods=['POST'])
def submit_todo():

    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")

    collection.insert_one({

        "itemName": itemName,
        "itemDescription": itemDescription

    })

    return "Item saved successfully"


if __name__ == "__main__":

    app.run(debug=True)
