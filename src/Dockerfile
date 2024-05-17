FROM ubuntu

WORKDIR /MyServer

COPY . /MyServer

RUN apt-get update && apt install -y python3 python3-pip python3-venv

RUN python3 -m venv /MyServer/venv
ENV PATH="/MyServer/venv/bin:$PATH"
RUN pip install -r requirements.txt

CMD ["python3", "manage.py"]