# 1) choose base container
# generally use the most recent tag

# data science notebook
# https://hub.docker.com/repository/docker/ucsdets/datascience-notebook/tags
#ARG BASE_CONTAINER=ucsdets/datascience-notebook:2020.2-stable

# scipy/machine learning (tensorflow)
# https://hub.docker.com/repository/docker/ucsdets/scipy-ml-notebook/tags
ARG BASE_CONTAINER=ucsdets/scipy-ml-notebook:2020.2-stable

FROM $BASE_CONTAINER

LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

# 2) change to root to install packages
USER root

RUN apt-get install -y htop \
aria2 \
nmap \
traceroute
# libopencv-dev python-opencv
# apt-get update
# apt-get install -y libsm6 libxext6 libxrender-dev
# pip install opencv-python
# RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev libglib2.0-0
# RUN pip install opencv-python


# 3) install packages
RUN pip install --no-cache-dir networkx scipy python-louvain geopandas babypandas opencv-python
RUN pip3 install opencv-python torch torchvision

# Install the COCO API
RUN git clone https://github.com/cocodataset/cocoapi.git /cocoapi
WORKDIR /cocoapi/PythonAPI
RUN make install

# FROM jjanzic/docker-python3-opencv
# COPY . /app
# WORKDIR /app

# RUN pip3 install -r requirements.txt
# ENTRYPOINT ["python3"]
# CMD ["app.py"]

# 4) change back to notebook user
#COPY /run_jupyter.sh /
RUN echo 'jupyter notebook "$@"' > /run_jupyter.sh 
RUN chmod 755 /run_jupyter.sh 
# USER $NB_UID

# Override command to disable running jupyter notebook at launch
# CMD ["/bin/bash"]