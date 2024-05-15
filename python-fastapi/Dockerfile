FROM python:3.11

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chmod +x start-server.sh

RUN python -m nuitka --follow-imports main.py

EXPOSE 8040

# To be overridden at startup
ENV NUITKA="0"
ENV WORKERS="1"

CMD ["./start-server.sh"]
