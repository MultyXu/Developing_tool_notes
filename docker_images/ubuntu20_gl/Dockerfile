# Pull base image.
FROM nvidia/cudagl:11.4.1-runtime-ubuntu20.04

ENV USER=root

# provide time, some apt install package needs that
RUN ln -fs /usr/share/zoneinfo/America/Detroit /etc/localtime

# Install minimum requirements
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y curl git unzip vim nano tmux wget xauth x11-apps lsb-release cmake

# needed for build habitat-sim

# Install XFCE, VNC server, dbus-x11, and xfonts-base
RUN apt-get update && apt-get install -y --no-install-recommends \
    xfce4 \
    xfce4-goodies \
    tightvncserver \
    dbus-x11 \
    xfonts-base \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Setup VNC server
RUN mkdir /root/.vnc \
    && echo "password" | vncpasswd -f > /root/.vnc/passwd \
    && chmod 600 /root/.vnc/passwd

# Create an .Xauthority file
RUN touch /root/.Xauthority

# Set display resolution (change as needed)
ENV RESOLUTION=1920x1080

# Expose VNC port
EXPOSE 5901

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

# Copy a script to start the VNC server
COPY start-vnc.sh start-vnc.sh
RUN chmod +x start-vnc.sh

# Define default command.
# CMD ["bash"]

# docker run -it --name multy_gs_0 --gpus device=0 --shm-size 16G -v /media/sde1/multy/workspace:/workspace -v /media/sdd1/multy:/sdd1 -v /home/multy:/sunny_multy multy/ubuntu_22.04_cuda11.7.1_gs bash 