import os
from werkzeug.utils import secure_filename

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def upload_file(request_files, location):
    if 'file' not in request_files:
        return False
    file = request_files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return False
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(location, filename))
        return True
    return False
