FROM python:2.7
MAINTAINER haongovan7@gamil.com

RUN mkdir -p /app/webapp

WORKDIR /app/webapp

COPY . /app/webapp/

RUN --mount=type=cache,mode=0755,target=/root/.cache/pip pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]