FROM python:3.9

WORKDIR /phonebook

RUN pip3 freeze > requirements.txt

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["bash"]