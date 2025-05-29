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

# Create a user to avoid root GUI issues
RUN useradd -m -s /bin/bash docker && \
    echo "docker:docker" | chpasswd && \
    adduser docker sudo

USER docker
WORKDIR /home/docker

# Expose VNC port
EXPOSE 5900

# Create startup script
RUN echo '#!/bin/bash\n\
Xvfb :0 -screen 0 1280x800x24 &\n\
sleep 2\n\
export DISPLAY=:0\n\
openbox &\n\
x11vnc -forever -usepw -create' > /home/docker/start.sh && \
chmod +x /home/docker/start.sh

RUN mkdir ~/.vnc && x11vnc -storepasswd password ~/.vnc/passwd


# ------------- old method -------------#

# # Install XFCE, VNC server, dbus-x11, and xfonts-base
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     xfce4 \
#     xfce4-goodies \
#     tightvncserver \
#     dbus-x11 \
#     xfonts-base \
#     && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# # Setup VNC server
# RUN mkdir /root/.vnc \
#     && echo "password" | vncpasswd -f > /root/.vnc/passwd \
#     && chmod 600 /root/.vnc/passwd

# # Create an .Xauthority file
# RUN touch /root/.Xauthority

# # Set display resolution (change as needed)
# ENV RESOLUTION=1920x1080

# # Expose VNC port
# EXPOSE 5901

# # NOTE: Conda is installed in a separate folder other than under root to save space, and to reuse environment, if possible
# # activate conda by 
# # source /workspace/miniconda3/bin/activate
# # conda init --all

# # Clean environment
# RUN apt-get update && apt-get upgrade && apt-get clean all

# # Set environment variables.
# ENV HOME /root

# # Define working directory.
# WORKDIR /root

# # Copy a script to start the VNC server
# COPY start-vnc.sh start-vnc.sh
# RUN chmod +x start-vnc.sh

# # Define default command.
# # CMD ["bash"]

# # docker run -it --name multy_gs_0 --gpus device=0 --shm-size 16G -v /media/sde1/multy/workspace:/workspace -v /media/sdd1/multy:/sdd1 -v /home/multy:/sunny_multy multy/ubuntu_22.04_cuda11.7.1_gs bash 