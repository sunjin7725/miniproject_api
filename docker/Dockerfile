FROM continuumio/anaconda3:2020.02-alpine

USER root
EXPOSE 3000
ENV PATH=/opt/conda/bin:$PATH

RUN apk update && apk upgrade
RUN apk -e search git && apk search git && apk add git

RUN conda create -y -n bigdata python==3.7.6 && conda init bash && conda activate bigdata
RUN mkdir -p /app
RUN git clone https://github.com/sunjin7725/miniproject_api \
    /app/miniproject_api

WORKDIR /app/miniproject_api
RUN pip install -r requirements.txt
CMD ["python", "app.py"]