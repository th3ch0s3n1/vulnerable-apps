FROM php:8.3-cli
WORKDIR /app
COPY app/ /app
EXPOSE 8080
CMD ["php", "-S", "0.0.0.0:5000", "-t", "/app"]
