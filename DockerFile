FROM python:3.13-slim

# Répertoire de travail
WORKDIR /app

# Copie uniquement les fichiers nécessaires
COPY requirements.txt ./
COPY script.py ./

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exécution du script toutes les minutes
CMD ["sh", "-c", "while true; do python /app/script.py; sleep 60; done"]