FROM  ubuntu:22.04

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    git jq vim  python3 python3-pip libvips

RUN apt-get install --reinstall -y ca-certificates


COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /app

WORKDIR /app

ENTRYPOINT ["/bin/bash"]
