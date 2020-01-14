FROM taoliu/gunicorn3

WORKDIR /cooperation
ADD requirements.txt .
RUN pip3 install -r requirements.txt


EXPOSE 8000

VOLUME /everything

ENV MONGO_URL=mongodb://mongo
ENV REDIS=redis://redis
ENV REDIS_DB=0
ENV ADDR=/everything/cooperation.sock
ENV PREFIX=''
ENV SESSION=http://session
ENV LANG="en_US"
ENV DEBUG=0

ADD . /cooperation
CMD gunicorn service:app --bind 0.0.0.0:8000 --worker-class sanic.worker.GunicornWorker
