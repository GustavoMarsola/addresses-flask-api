# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory inside the container
WORKDIR $SERVICE_HOME

# Copy the requirements file into the container
COPY requirements.txt $SERVICE_HOME

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
ENTRYPOINT ["python", "main.py"]

