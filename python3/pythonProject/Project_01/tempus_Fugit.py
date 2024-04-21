import os
import urllib.request
from flask import Flask, flash, request, redirect, render_template
from ftplib import FTP
import subprocess

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = {'txt', 'rtf'}

app = Flask(__name__)
app.secret_key = "mofosecret"
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    cmd = 'fortune -o'
    result = subprocess.check_output(cmd, shell=True)
    return "<h1>400 - Sorry. I didn't find what you where looking for.</h1> <h2>Maybe this will cheer you up:</h2><h3>" + result.decode(
        "utf-8") + "</h3>"


@app.errorhandler(500)
def internal_error(error):
    return "<h1>500?! - What are you trying to do here?!</h1>"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload')
def upload_form():
    try:
        return render_template('my-form.html')
    except Exception as e:
        return render_template("500.html", error=str(e))


def allowed_file(filename):
    check = filename.rsplit('.', 1)[1].lower()
    check = check[:3] in ALLOWED_EXTENSIONS
    return check


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file.filename and allowed_file(file.filename):
            filename = file.filename

            file.save(os.path.join(UPLOAD_FOLDER, filename))
            cmd = "cat " + UPLOAD_FOLDER + "/" + filename
            result = subprocess.check_output(cmd, shell=True)
            flash(result.decode("utf-8"))
            flash('File successfully uploaded')

            try:
                ftp = FTP('ftp.mofo.pwn')
                ftp.login('someuser', 'b232a4da4c104798be4613ab76d26efda1a04606')
                with open(UPLOAD_FOLDER + "/" + filename, 'rb') as f:
                    ftp.storlines('STOR %s' % filename, f)
                    ftp.quit()
            except:
                flash("Cannot connect to FTP-server")
            return redirect('/upload')

        else:
            flash('Allowed file types are txt and rtf')
            return redirect(request.url)


if __name__ == "__main__":
    app.run()