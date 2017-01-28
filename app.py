from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from werkzeug import secure_filename
import os

app = Flask(__name__)

# # This is the path to the upload directory
# app.config['UPLOAD_FOLDER'] = 'uploads/'
# # These are the extension that we are accepting to be uploaded
# app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
#
# # For a given file, return whether it's an allowed type or not
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

UPLOAD_FOLDER = './tempaudio'
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      artpiece = request.form['artpiece']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return 'file uploaded successfully'
  else:
      return render_template('upload.html')


@app.route('/')
def index():
    return redirect(url_for('upload_file'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == "__main__":
    app.run()
