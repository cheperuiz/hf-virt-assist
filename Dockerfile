FROM  python:3.8
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && echo America/Los_Angeles > /etc/timezone

COPY assets/ /
RUN useradd --create-home hf

RUN apt-get update \
    && apt-get install -y \
    ipython \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
