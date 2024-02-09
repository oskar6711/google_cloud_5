import os
from flask import Flask

from flask import Flask,render_template,request
 
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')
 
@app.route('/dane/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"Formularz nie został wypełniony."
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))