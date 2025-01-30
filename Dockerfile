# Pobierz oficjalny obraz Pythona 3.11.7
FROM python:3.11.7

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki do kontenera
COPY requirements.txt .
COPY script.py .

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Tworzy katalog na wyjściowe pliki (jeśli ktoś nie poda własnego voluma)
RUN mkdir -p /output

# Uruchom skrypt
CMD ["python", "script.py"]
