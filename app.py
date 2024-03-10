from flask import Flask, render_template, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


"""
training model with our data
"""
import numpy as np
from sklearn.linear_model import LinearRegression
import csv

X_train = np.array([])
Y_train = np.array([])

with open('data.csv', 'r') as csvFile:
    csv_reader = csv.reader(csvFile)
    for row in csv_reader:
        X_train = np.concatenate((X_train, [float(row[0])])) 
        Y_train = np.concatenate((Y_train, [float(row[1])])) 


# Creating a linear regression model
model = LinearRegression()

# Training the model
model.fit(X_train.reshape(-1, 1), Y_train)


"""
our routes 
"""

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        height = request.args.get('height')
        height = int(height)
        ans = model.predict(np.array([height]).reshape(1,-1))
        # ans = ((height*0.39) + 3)
        return str(ans)
    return "5"

if __name__ == "__main__":
    app.run(debug=True)