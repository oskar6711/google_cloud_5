import os
from flask import Flask

from flask import Flask,render_template,request
 
app = Flask(__name__)

def track_event(category, action, label=None, value=0):
    data = {
        'v': '1',  # API Version.
        'tid': "G-5QDQ6CGL4J",  # Tracking ID / Property ID.
        # Anonymous Client Identifier. Ideally, this should be a UUID that
        # is associated with particular user, device, or browser instance.
        'cid': '555',
        't': 'event',  # Event hit type.
        'ec': category,  # Event category.
        'ea': action,  # Event action.
        'el': label,  # Event label.
        'ev': value,  # Event value, must be an integer
    }

    response = requests.post(
        'http://www.google-analytics.com/collect', data=data)

    # If the request fails, this will raise a RequestException. Depending
    # on your application's needs, this may be a non-error and can be caught
    # by the caller.
    response.raise_for_status()
 
@app.route('/')
def form():
    track_event(
        category='Example',
        action='test action')
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