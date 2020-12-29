FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /shop
COPY . ./
RUN pip install -r requirements.txt
ENTRYPOINT ["sh","./docker-entrypoint.sh"]