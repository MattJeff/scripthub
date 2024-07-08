FROM python:3.9-slim

# Mettre à jour le système et installer les dépendances nécessaires
RUN apt-get update && apt-get install -y build-essential

# Créer un répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposer le port
EXPOSE 5000

# Commande de démarrage
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
