FROM python:2.7-wheezy
EXPOSE 4568
WORKDIR /usr/src/app
RUN ln -sf /usr/src/app/flask.sh /flask
CMD /flask

COPY requirements*.txt /tmp/

RUN pip install -r /tmp/requirements.txt -i https://pi.builds.2ndsiteinc.com/dev/releases
COPY . /usr/src/app


RUN cd /usr/src/app && pip install  -e . 

# dev things

RUN apt-get update && apt-get -y install vim
RUN pip install -r /tmp/requirements-dev.txt -i https://pi.builds.2ndsiteinc.com/dev/releases


