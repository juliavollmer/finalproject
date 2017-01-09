from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_post():
    return render_template('layout.html')

@app.route('/upload', methods=['GET'])
def upload_get():
    return render_template('layout.html')

@app.route('/')
def index():
    return redirect(url_for('upload_get'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == "__main__":
    app.run()
