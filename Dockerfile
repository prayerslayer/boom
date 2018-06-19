FROM python:3.6.5-alpine3.7

RUN apk update
RUN apk add --no-cache git docker
RUN mkdir /app && git clone https://github.com/StepicOrg/epicbox.git /app/epicbox
RUN pip install -e /app/epicbox

