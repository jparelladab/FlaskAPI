FROM python
WORKDIR /api
COPY ./api/requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]