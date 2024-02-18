from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=["POST"])
def generate():
    # Process form data if needed
    prompt = request.form.get("inputString")
    image_src = ""

    # Redirect to index1 route
    return redirect(url_for('index1'))

@app.route('/index1')
def index1():
    return render_template('index1.html')

# Add a new route to handle the return from index1.html to index.html
@app.route('/index', methods=["POST"])
def return_to_index():
    # Here you can perform any necessary processing
    return redirect(url_for('index'))  # Redirect back to index.html

if __name__ == '__main__':
    app.run(debug=True)