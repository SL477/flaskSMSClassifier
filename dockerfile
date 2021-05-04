# First stage
#FROM python:3.8 as builder
#COPY requirements.txt .

# Install dependancies
#RUN pip3 install --user -r requirements.txt

# Second stage
#FROM python:3.8-slim
#WORKDIR /app

FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt

COPY . .

#COPY --from=builder /root/.local root/.local
#COPY . .

# Update PATH
#ENV PATH=/root/.local:$PATH

# Build the model
CMD [ "python3", "-u", "modelmaker.py" ]

# Run the app
#CMD [ "python3", "-u", "./app.py" ]
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]