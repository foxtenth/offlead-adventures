



from flask import Flask, render_template

app = Flask(__name__)

# Route to the Landing page
@app.route('/')
def home():
    return render_template('start.html')

# Route to the Pet Taxi
@app.route('/pet-taxi')
def pet_taxi():
    return render_template('pet_taxi.html')

if __name__ == '__main__':
    app.run(debug=True)