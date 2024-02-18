from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():

    return redirect(url_for('ballot'))

@app.route('/ballot')
def ballot():
    return render_template('ballot.html')

# Add a new route to handle the return from index1.html to index.html
@app.route('/index', methods=["POST"])
def return_to_index():
    # Here you can perform any necessary processing
    return redirect(url_for('index'))  # Redirect back to index.html

if __name__ == '__main__':
    app.run(debug=True)