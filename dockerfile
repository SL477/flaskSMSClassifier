# First stage
FROM python:3.8 as builder
COPY requirements.txt .

# Install dependancies
RUN pip install --user -r requirements.txt

# Second stage
FROM python:3.8-slim
WORKDIR /app

COPY --from=builder /root/.local root/.local
COPY . .

# Update PATH
ENV PATH=/root/.local:$PATH

# Build the model
CMD [ "python3", "-u", "./modelmaker.py" ]

# Run the app
CMD [ "python3", "-u", "./app.py" ]