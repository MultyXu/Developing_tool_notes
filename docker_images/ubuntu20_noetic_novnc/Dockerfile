# Pull base image.
# FROM dsalvat1/cudagl:12.3.1-runtime-ubuntu22.04
FROM nvidia/cudagl:11.4.1-runtime-ubuntu20.04

# set environment variables
ENV USER=root
ENV DISPLAY=:1

# set build time arguments
ARG DEBIAN_FRONTEND=noninteractive

# Expose VNC and noVNC port
EXPOSE 5901 
EXPOSE 6081 

# Install minimum requirements
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential \
    sudo

# solve locale issue 
RUN ln -fs /usr/share/zoneinfo/America/Detroit /etc/localtime 
RUN apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8

# instal libraries and tools
RUN apt-get install -y --no-install-recommends \
    curl git unzip vim nano xauth x11-apps openssh-server ffmpeg cmake \ 
    valgrind \
    apt-utils \
    mesa-utils \
    tmux \
    wget \
    curl \
    gdb \
    clang \
    x11-xserver-utils \
    lsb-release \
    zsh \
    pkg-config 

# python related packages
RUN apt-get install -y --no-install-recommends \
    python3-dev \
    python3-pip \
    python3-tk \
    python3-matplotlib 

# install libraries and tools
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     sudo \
#     dialog \
#     apt-utils \
#     git \
#     mercurial \
#     pkg-config \
#     mesa-utils \
#     libxau-dev \
#     libxdmcp-dev \
#     libxcb1-dev \
#     libxext-dev \
#     libx11-dev \ 
#     git \
#     tmux \
#     wget \
#     curl \
#     cmake \
#     vim \ 
#     build-essential \
#     unzip \
#     autoconf \
#     autogen \
#     automake \
#     libtool \
#     zlib1g-dev \
#     libopenblas-dev \
#     libflann-dev \
#     libboost-all-dev \
#     libsuitesparse-dev \
#     libtbb-dev \
#     libusb-1.0-0-dev \
#     libgtest-dev \
#     pkg-config \
#     cmake-curses-gui \
#     gdb \
#     clang \
#     emacs \
#     libpcap-dev \
#     gnupg2 \
#     x11-xserver-utils \
#     lsb-release \
#     tilix \
#     zsh \
#     python3-dev \
#     python3-pip \
#     python3-tk \
#     python3-matplotlib \
#     valgrind \
#     kcachegrind

# Install TensorRT (only if the nvidia cuda is configured correctly on host machine, otherwise, follow https://docs.nvidia.com/deeplearning/tensorrt/latest/installing-tensorrt/overview.html)
# RUN apt-get install tensorrt -y
# RUN apt install libnvinfer-dev libnvonnxparsers-dev libnvinfer-plugin-dev
RUN echo 'keyboard-configuration keyboard-configuration/layoutcode select us' | debconf-set-selections && \
    echo 'keyboard-configuration keyboard-configuration/modelcode select pc105' | debconf-set-selections && \
    apt-get update && \
    apt-get install -y keyboard-configuration

# Install basic vnc tools
RUN apt update && apt install -y \
    x11vnc xvfb openbox xterm \
    net-tools && \
    apt clean
    
# install lightweight desktop environment
# RUN sudo apt-get install xfce4 xfce4-goodies -y

# install TigerVNC server
RUN sudo apt-get install tigervnc-standalone-server tigervnc-common -y

# --- Install ROS Noetic ---
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
RUN sudo apt-get update
RUN sudo apt-get install ros-noetic-desktop -y
RUN sudo apt-get install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential -y

# Install noVNC
WORKDIR /opt
RUN wget https://github.com/novnc/noVNC/archive/refs/tags/v1.6.0.zip
RUN unzip v1.6.0.zip && \
    mv noVNC-1.6.0 novnc && \
    rm v1.6.0.zip

# setup vnc to run openbox and xterm
WORKDIR /root
COPY xstartup /root/.vnc/xstartup
RUN chmod +x /root/.vnc/xstartup
COPY start_vnc.sh /root/start_vnc.sh
RUN chmod +x /root/start_vnc.sh