FROM python:3.8

WORKDIR /app
COPY src .
ENV FLASK_APP=main.py

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "flask"]
CMD [ "run" ]