FROM alpine

RUN apk update && apk upgrade
RUN apk -e search git && apk search git && apk add git
RUN mkdir -p /opt/conda
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/sh ~/anaconda.sh -b -u -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN mkdir -p /app
RUN git clone https://github.com/sunjin7725/miniproject_api \
    /app/miniproject_api

CMD ["python", "/app/miniproject_api/app.py"]