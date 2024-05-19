FROM python:3.11

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chmod +x start-server.sh


EXPOSE 8000

# To be overridden at startup
ENV WORKERS="1"
ENV POSTGRES="0"

CMD ["./start-server.sh"]
