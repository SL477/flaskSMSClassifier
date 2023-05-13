# flaskSMSClassifier

Flask SMS Classifier
![Screenshot](https://link477.com/assets/images/SMSClassifier.jpg)

## Setup

Install python packages from requirements.txt

```bash
pip install requirements.txt
```

Get data from:

- [Train Data](https://cdn.freecodecamp.org/project-data/sms/train-data.tsv)
- [Validation Data](https://cdn.freecodecamp.org/project-data/sms/valid-data.tsv)

Put the files into the folder data. Then run setup.py

## Run with

```bash
gunicorn -w 1 app.wsgi
```

or

```bash
bash run.sh
```

## Docker

Build with:

```bash
docker build -t flasksmsclassifier .
```

Run with:

```bash
docker run -dp 5000:5000 flasksmsclassifier
```
