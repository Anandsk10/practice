FROM python:3.9
WORKDIR /
#Copy from "host" to "container"
COPY . /
#Run this command in the container
RUN apt-get update
RUN pip3 install -r requirements.txt
EXPOSE 5002
CMD ["python3","app.py"]
