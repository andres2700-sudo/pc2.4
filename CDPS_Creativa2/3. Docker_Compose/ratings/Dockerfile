FROM node:12.18.1-slim

EXPOSE 9080
WORKDIR /opt/microservices/
COPY ./package.json .
COPY ./ratings.js .
ENV SERVICE_VERSION=v1
RUN npm install

CMD ["node", "ratings.js", "9080"]
