FROM python:3.7.7-slim

EXPOSE 9080
WORKDIR ~/
COPY . .
RUN pip3 install -r ./creativa_2/bookinfo/src/productpage/requirements.txt
ENV GROUP_NUMBER 36

CMD ["python3", "./productpage_monolith.py", "9080"]

