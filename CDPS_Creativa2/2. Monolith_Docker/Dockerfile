FROM python:3.12.0a4-buster

EXPOSE 9080
WORKDIR /home/ltr_trave/creativa_2/bookinfo/src/productpage
COPY . .
RUN pip3 install -r ./requirements.txt
ENV GROUP_NUMBER 36

CMD ["python3", "./productpage_monolith.py", "9080"]

