from flask import Flask, render_template, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        height = request.args.get('height')
        height = int(height)
        ans = ((height*0.39) + 3)
        return str(ans)
    return "5"

if __name__ == "__main__":
    app.run(debug=True)