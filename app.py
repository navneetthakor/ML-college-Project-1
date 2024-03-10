from flask import Flask, render_template, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


"""
training model with our data
"""
import numpy as np
from sklearn.linear_model import LinearRegression


X_train = np.array([182,178,150,130,160])
Y_train = np.array([75,72,62,40,67])

# Creating a linear regression model
model = LinearRegression()

# Training the model
model.fit(X_train.reshape(-1, 1), Y_train)
# y_pred = model.predict(np.array([180]).reshape(1, -1))


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