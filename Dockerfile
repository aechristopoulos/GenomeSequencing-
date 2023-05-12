FROM ubuntu:22.04

# Install base utilities
RUN apt-get update 
RUN apt-get install -y wget 
RUN apt-get clean

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

Workdir /app 

COPY . . 

RUN python -m pip install biopython matplotlib



CMD ["/bin/sh"]