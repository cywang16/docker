import flask
import os
import pandas as pd
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def fix_csv(filename):
    classdata = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    del classdata['textBox35']
    del classdata['textBox5']
    del classdata['textBox37']
    del classdata['textBox38']
    cols = classdata.columns.tolist()
    cols = cols[-3:-2] + cols[:-3] + cols[-2:]
    cols = cols[0:7] + cols[-2:-1] + cols[7:-2] + cols[-1:]
    classdataFixed = classdata[cols]
    classdataFixed.columns = ['Class Code',
                              'Room',
                              'Min',
                              'Max',
                              'Pending',
                              'Enrolled',
                              'Waitlisted',
                              'Open',
                              'Start Date',
                              'End Date',
                              'Start Time',
                              'End Time',
                              'Days',
                              'Adjudicator',
                              'Status']
    filenamefixed = '{}_fixed.csv'.format(os.path.splitext(filename)[0])
    classdataFixed.to_csv(os.path.join(app.config['UPLOAD_FOLDER'], filenamefixed), index = False)
    return filenamefixed

'''
Followed http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
and https://stackoverflow.com/questions/25001729/python-how-to-upload-file-to-webservice-using-flask-module
'''
@app.route('/uploadtest', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filefixed = fix_csv(filename)
            return redirect(url_for('uploaded_file',
                                    filename=filefixed))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, mimetype = 'text/csv')
@app.route("/flask")
def hello():
    return "Hello World!<br><h3>flask version: {}</h3>".format(flask.__version__)

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
