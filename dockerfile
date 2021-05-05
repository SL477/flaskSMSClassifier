FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt

COPY . .

# Build the model
CMD [ "python3", "-u", "modelmaker.py" ]

# Run the app
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]