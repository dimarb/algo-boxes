FROM  python:3.11.0

RUN   adduser   --group  --shell /bin/sh --disabled-password apis

COPY ./src/ /home/api/

WORKDIR /home/api/

RUN pip install -r requirements.txt


ENV export FLASK_APP=app.py

EXPOSE 3000

ENV FLASK_DEBUG=1

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=3000"]