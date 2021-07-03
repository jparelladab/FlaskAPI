FROM python
WORKDIR /api
COPY ./api/requirements.txt .
RUN apt update
RUN apt-get install -y mariadb-server python-mysqldb
RUN service mysql start
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt mysqlclient
COPY ./api/start.sh /start.sh
RUN chmod +x /start.sh
CMD ["sh", "start.sh"]
