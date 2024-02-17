from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=["POST"])
def generate():
    prompt = request.form.get("inputString")
    image_src = ""

    context = {"image_src" : image_src, "prompt" : prompt}

    return render_template("index.html", **context)

