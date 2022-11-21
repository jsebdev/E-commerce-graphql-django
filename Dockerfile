# base image  
FROM python:3.8-bullseye

# set work directory
WORKDIR /usr/src/app
# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
ENV HomeDir=/home/app  

# set work directory  
RUN mkdir -p $HomeDir  
WORKDIR $HomeDir  

# install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $HomeDir  

# port where the Django app runs  
EXPOSE 8000

# start server  
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "backend.wsgi:application"]