FROM continuumio/anaconda3:2020.02-alpine

USER root
EXPOSE 3000
ENV PATH=/opt/conda/bin:$PATH

RUN apk update && apk upgrade
RUN apk -e search git && apk search git && apk add git
RUN apk -e search git-lfs && apk search git-lfs && apk add git-lfs
RUN git-lfs install

RUN conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cpuonly -c pytorch

RUN mkdir -p /app
RUN git clone https://github.com/sunjin7725/miniproject_api \
    /app/miniproject_api

RUN mkdir -p /app/miniproject_api/data/model/kogpt2-base-v2
RUN git clone https://huggingface.co/skt/kogpt2-base-v2 \
    /app/miniproject_api/data/model/kogpt2-base-v2

WORKDIR /app/miniproject_api
RUN pip install -r requirements.txt
CMD ["python", "app/app.py"]