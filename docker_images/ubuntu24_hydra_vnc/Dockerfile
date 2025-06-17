# Pull base image.
FROM tsapu/cudagl:12.6.3-devel-ubuntu24.04

ENV USER=root

RUN ln -fs /usr/share/zoneinfo/America/Detroit /etc/localtime 

# Install minimum requirements
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y curl git unzip vim nano tmux wget xauth x11-apps openssh-server ffmpeg lsb-release cmake

# install libraries and tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    dialog \
    apt-utils \
    git \
    mercurial \
    pkg-config \
    mesa-utils \
    libxau-dev \
    libxdmcp-dev \
    libxcb1-dev \
    libxext-dev \
    libx11-dev \ 
    git \
    tmux \
    wget \
    curl \
    cmake \
    vim \ 
    build-essential \
    unzip \
    autoconf \
    autogen \
    automake \
    libtool \
    zlib1g-dev \
    libopenblas-dev \
    libflann-dev \
    libboost-all-dev \
    libsuitesparse-dev \
    libtbb-dev \
    libusb-1.0-0-dev \
    libgtest-dev \
    pkg-config \
    cmake-curses-gui \
    gdb \
    clang \
    emacs \
    libpcap-dev \
    gnupg2 \
    x11-xserver-utils \
    lsb-release \
    tilix \
    zsh \
    python3-dev \
    python3-pip \
    python3-tk \
    python3-matplotlib \
    valgrind \
    kcachegrind

# solve locale issue 
RUN locale-gen en_US.UTF-8

# Install TensroRT (only if the nvidia cuda is configured correctly on host machine, otherwise, follow https://docs.nvidia.com/deeplearning/tensorrt/latest/installing-tensorrt/overview.html)
RUN apt-get install tensorrt -y
# RUN apt install libnvinfer-dev libnvonnxparsers-dev libnvinfer-plugin-dev

# Install basic tools
RUN apt update && apt install -y \
    x11vnc xvfb openbox xterm wget sudo \
    net-tools curl && \
    apt clean

# --- Install ROS2
RUN sudo apt-get install software-properties-common -y \
    && sudo add-apt-repository universe -y \
    && sudo apt-get update && sudo apt-get install curl -y \
    && sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# RUN sudo apt-get update --fix-missing \
#     && sudo apt-get remove libbrotli1 -y
RUN sudo apt update && sudo apt install ros-dev-tools -y
RUN sudo apt-get install -y ros-jazzy-desktop

# install lightweight desktop environment
RUN sudo apt install xfce4 xfce4-goodies -y
RUN sudo apt install tigervnc-standalone-server tigervnc-common -y

# Expose VNC and noVNC port
EXPOSE 5901
EXPOSE 6080

WORKDIR /root
# Install noVNC
RUN wget https://github.com/novnc/noVNC/archive/refs/tags/v1.6.0.zip
RUN unzip v1.6.0.zip && \
    rm v1.6.0.zip

# setup vnc to run openbox and xterm
COPY xstartup /root/.vnc/xstartup
RUN chmod +x /root/.vnc/xstartup

# Create a user to avoid root GUI issues
# RUN useradd -m -s /bin/bash docker && \
#     echo "docker:docker" | chpasswd && \
#     adduser docker sudo

# USER docker
# WORKDIR /home/docker


# Create startup script
# RUN echo '#!/bin/bash\n\
# Xvfb :0 -screen 0 1280x800x24 &\n\
# sleep 2\n\
# export DISPLAY=:0\n\
# openbox &\n\
# x11vnc -forever -usepw -create' > /home/docker/start.sh && \
# chmod +x /home/docker/start.sh

# RUN mkdir ~/.vnc && x11vnc -storepasswd password ~/.vnc/passwd