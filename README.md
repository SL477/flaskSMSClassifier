# flaskSMSClassifier
 Flask SMS Classifier

# Setup
Install python packages from requirements.txt
pip install requirements.txt

Get data from:
https://cdn.freecodecamp.org/project-data/sms/train-data.tsv
https://cdn.freecodecamp.org/project-data/sms/valid-data.tsv

Put the files into the folder data. Then run setup.py

# Docker
Build with:
docker build -t flasksmsclassifier .

Run with:
docker run -dp 5000:5000 flasksmsclassifier