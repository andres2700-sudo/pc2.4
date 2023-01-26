FROM python:3.7.7-slim

EXPOSE 9080
WORKDIR /productpage
COPY . .
RUN pip3 install -r ./requirements.txt

CMD ["python3", "./productpage.py", "9080"]

