FROM ruby:2.7.1-slim

EXPOSE 9080
WORKDIR /opt/microservices/
COPY ./details.rb .
ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

CMD ["ruby", "./details.rb", "9080"]

