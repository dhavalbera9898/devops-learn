from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://dhavalberaethics:EgT8c4mB0Pit8jjS@cluster0.zcjx88y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.mydatabase
collection = db.mycollection

@app.route('/api')
def api():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        try:
            collection.insert_one({'name': name, 'email': email})
            return redirect(url_for('success'))
        except Exception as e:
            return render_template('form.html', error=str(e))
    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
	app.run(debug=True)