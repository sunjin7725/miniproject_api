FROM continuumio/anaconda3:2020.02-alpine

RUN apk update && apk upgrade
RUN apk -e search git && apk search git && apk add git

RUN mkdir -p /app
RUN git clone https://github.com/sunjin7725/miniproject_api \
    /app/miniproject_api

CMD ["python", "/app/miniproject_api/app.py"]