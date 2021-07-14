FROM python:latest

WORKDIR /root

ADD . /root

ENV DISCORD_BOT_TOKEN=PASTE_YOUR_DISCORD_KEY 

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]
