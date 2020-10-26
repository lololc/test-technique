FROM continuumio/miniconda3:4.8.2

COPY requirements.txt /requirements.txt
RUN /opt/conda/bin/conda install --yes --file requirements.txt && conda clean -afy

RUN mkdir /datapipeline
COPY src /datapipeline/src

WORKDIR /datapipeline/src

ENTRYPOINT ["python","main.py"]