FROM pandoc/latex:latest

# Installiere Noto Color Emoji für farbige Emojis im PDF
RUN apt-get update && \
    apt-get install -y fonts-noto-color-emoji

# Setze das Arbeitsverzeichnis (optional)
WORKDIR /data