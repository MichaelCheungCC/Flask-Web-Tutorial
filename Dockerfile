FROM python:3.9.16

# set the working directory
WORKDIR /app

# copy the application files and the requirements file
COPY . .

# install the dependencies
RUN pip install -r requirements.txt

# expose the necessary port
EXPOSE 5001

# Start the application
CMD ["python", "main.py"]