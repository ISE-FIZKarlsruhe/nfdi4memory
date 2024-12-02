FROM ghcr.io/epoz/shmarql:latest

COPY docs /src/docs
COPY mkdocs.yml /src/mkdocs.yml

RUN mkdocs build