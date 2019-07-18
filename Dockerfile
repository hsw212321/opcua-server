FROM python:2.7.16

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com --no-cache-dir -r requirements.txt

COPY ua-server.py ./

CMD [ "python", "./ua-server.py" ]