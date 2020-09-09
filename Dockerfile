FROM continuumio/miniconda3:latest

LABEL maintainer="Jeffrey van Santen <jeffreyavansanten@gmail.com>"

WORKDIR /app/
RUN conda update -n base conda
COPY environment.yml /app/
ENV PYTHONVENV "atomorder"
RUN conda env create -f environment.yml

COPY . /app/

EXPOSE 8000

CMD ["./start.sh"]