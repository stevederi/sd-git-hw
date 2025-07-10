# Use the official Python 3.8 slim image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /sd-flask

# Copy the necessary files and directories into the container
COPY templates/ static/ app.py requirements.txt /sd-flask/
COPY templates/ /sd-flask/templates/
COPY static/ /sd-flask/static/
COPY app.py  /sd-flask/

# Upgrade pip and install Python dependencies
RUN pip3 install -i https://pypi.org/simple --trusted-host pypi.org/simple python-pypi-mirror
RUN pip3 install flask
RUN pip3 install pymongo
RUN pip3 install gunicorn

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application using Gunicorn
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-w", "4"]