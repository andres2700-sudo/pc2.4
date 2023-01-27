FROM python:3.7.7-slim

EXPOSE 9080
WORKDIR ../creativa_2/bookinfo/src/productpage
COPY . .
RUN pip3 install -r ./requirements.txt
ENV GROUP_NUMBER 36

CMD ["python3", "./productpage_monolith.py", "9080"]

