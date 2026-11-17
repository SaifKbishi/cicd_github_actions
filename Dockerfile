#use an oficial Python image
FROM python:3.9-slim

#set the working directory in the container
WORKDIR /app

#copy app files
COPY . .

#install dependencies
RUN pip install Flask

#run the application
CMD ["python","app.py"]
