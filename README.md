# AISIA AnamolyDetection Webservice

## Tools
VScode Extension: vscode-icons, python, markdown preview enhanced

## Installation
### Virtual environment
Ubuntu:  
python3 -m venv venv
venv/bin/activate  
or  
source venv/bin/activate

Window: 
py -3 -m venv venv  
venv\Scripts\activate

### Dependencies installation
(venv) $ pip install flask  
(venv) $ pip install flask-sqlalchemy  
(venv) $ pip install opencv-python  
(venv) $ pip install flask-cors

## Database
(venv) $ flask db migrate

Note that: Sqlite used by default or you can set Database path in environment variable before migrating

## Run
Ubuntu:  
export FLASK_APP=main.py  
export FLASK_DEBUG=0  
flask run

Window: 
set FLASK_APP=main.py  
set FLASK_DEBUG=0  
flask run