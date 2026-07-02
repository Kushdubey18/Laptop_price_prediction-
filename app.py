from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("model/rb.lb")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contacts.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/predict', methods=['POST'])
def predict():

    company = int(request.form['company'])
    typename = int(request.form['typename'])
    inches = int(request.form['inches'])
    ram = int(request.form['ram'])
    memory = int(request.form['memory'])
    opsys = int(request.form['opsys'])

    data = [[company, typename, inches, ram, memory, opsys]]

    pred = model.predict(data)

    prediction = round(float(pred[0]), 2)

    return render_template(
        'project.html',
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)