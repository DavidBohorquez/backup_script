FROM ubuntu:latest

WORKDIR /home/myuser/app

COPY . .

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /home/myuser/app/venv

RUN /home/myuser/app/venv/bin/pip install --no-cache-dir -r requirements.txt

ENV PATH="/home/myuser/app/venv/bin:$PATH"

CMD ["pytest", "-v"]