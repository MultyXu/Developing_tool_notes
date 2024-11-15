# Pull base image.
FROM nvidia/cuda:11.7.1-runtime-ubuntu22.04

# Install minimum requirements
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y curl git unzip vim nano tmux wget xauth x11-apps openssh-server ffmpeg lsb-release cmake

# packages needed by GS interactive viewer, providing time zone if asked
RUN ln -fs /usr/share/zoneinfo/America/Detroit /etc/localtime && apt install -y libglew-dev libassimp-dev libboost-all-dev libgtk-3-dev libopencv-dev libglfw3-dev libavdevice-dev libavcodec-dev libeigen3-dev libxxf86vm-dev libembree-dev

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

# docker run -it --name multy_gs_0 --gpus device=0 --shm-size 16G -v /media/sde1/multy/workspace:/workspace -v /media/sdd1/multy:/sdd1 -v /home/multy:/sunny_multy multy/ubuntu_22.04_cuda11.7.1_gs bash 