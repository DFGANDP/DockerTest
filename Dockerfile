FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY script.py ./

RUN mkdir -p /app/output

# ENTRYPOINT pozwala na przekazywanie argumentów (appid)
ENTRYPOINT ["python", "script.py"]
