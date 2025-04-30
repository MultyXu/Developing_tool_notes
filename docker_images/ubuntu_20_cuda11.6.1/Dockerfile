# Pull base image.
FROM nvidia/cuda:11.6.1-runtime-ubuntu20.04

RUN ln -fs /usr/share/zoneinfo/America/Detroit /etc/localtime

# Install minimum requirements
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential

RUN apt-get install -y curl git unzip vim nano tmux wget xauth x11-apps openssh-server ffmpeg lsb-release cmake


# NOTE: Conda is installed in a separate folder other than under root to save space, and to reuse environment, if possible
# activate conda by 
# source /workspace/miniconda3/bin/activate
# conda init --all

# Clean environment
RUN apt-get update && apt-get upgrade && apt-get clean all

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

# Define default command.
CMD ["bash"]
