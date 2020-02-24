FROM ubuntu:18.04

WORKDIR /usr/src/app

ENV LANG="C.UTF-8" LC_ALL="C.UTF-8" PATH="/opt/venv/bin:$PATH" PIP_NO_CACHE_DIR="false"

RUN apt-get update -qq && apt-get install -qq -y --no-install-recommends \
    python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python3 -m venv /opt/venv && \
    python3 -m pip install pip==19.3.1 pip-tools==4.2.0

RUN python3 -m piptools sync

COPY . .

ENTRYPOINT ["/usr/src/app/bin/planex"]
CMD ["-h"]
