# Pull base image.
FROM nvidia/cuda:11.7.1-runtime-ubuntu22.04

ENV USER=root

# Install minimum requirements
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y curl git unzip vim nano tmux wget xauth x11-apps openssh-server lsb-release cmake

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

RUN apt-get update && apt-get install -y --no-install-recommends \
# For Habitat Sim
software-properties-common \
wget \
git-lfs \
gconf-service \
libatk1.0-0 \
libatk-bridge2.0-0 \
libc6 \
libcairo2 \
libcups2 \
libdbus-1-3 \
libexpat1 \
libfontconfig1 \
libgcc1 \
libgconf-2-4 \
libgdk-pixbuf2.0-0 \
libglib2.0-0 \
libgtk-3-0 \
libnspr4 \
libpango-1.0-0 \
libstdc++6 \
libx11-6 \
libx11-xcb1 \
libxcb1 \
libxcomposite1 \
libxcursor1 \
libxdamage1 \
libxext6 \
libxfixes3 \
libxrender1 \
libxss1 \
libxtst6 \
ca-certificates \
fonts-liberation \
libappindicator1 \
libnss3 \
lsb-release \
xdg-utils \
# For Building Habitat-Sim locally
libegl1-mesa \
libgegl-0.4-0 \
libnvidia-egl-wayland1 \
libnvidia-egl-wayland-dev \
libjpeg-dev \
libglm-dev \
libgl1-mesa-glx \
libgl1-mesa-dev \
libegl1-mesa-dev \
mesa-utils \
xorg-dev \
freeglut3-dev \
build-essential \
&& apt-get -y autoremove \
&& apt-get clean autoclean \
&& rm -rf /var/lib/apt/lists/*

# Setup Git LFS
RUN git lfs install

# Install miniconda 
RUN mkdir -p /root/miniconda3
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh
RUN bash /tmp/miniconda.sh -b -u -p /root/miniconda3
RUN /root/miniconda3/bin/conda init && \
    /root/miniconda3/bin/conda config --set auto_activate_base false && \
    /root/miniconda3/condabin/conda create -y -n habitat python=3.9 cmake=3.14.0

# Install python package dependencies, if additional packages are needed, add them to the RUN command below
SHELL ["/root/miniconda3/condabin/conda", "run", "-n", "habitat", "/bin/bash", "-c"]

# install conda ros
RUN conda config --env --add channels conda-forge && \
    conda config --env --add channels robostack-staging
RUN conda install ros-noetic-desktop && \
    conda install compilers cmake pkg-config make ninja colcon-common-extensions catkin_tools rosdep

# might need to install pytorch and cuda-toolkit

# Clone Habitat Sim Repository and build a local version
RUN git clone --branch v0.3.0 https://github.com/facebookresearch/habitat-sim.git

RUN cd habitat-sim && \
    pip install -r requirements.txt && \
    python setup.py install --bullet && \
    pip install -e .

WORKDIR /root

# install habitat lab
RUN git clone --branch dev https://github.com/UMich-CURLY/habitat-lab.git

RUN cd habitat-lab && \
    pip install -e habitat-lab/ && \
    pip install -e habitat-baseline

# install ros-habitat-interface
WORKDIR /home
RUN mkdir catkin_ws && cd catkin_ws && mkdir src && cd src
RUN cd /catkin_ws/src && git clone --branch v0.3 https://github.com/UMich-CURLY/habitat_ros_interface.git
RUN cd /catkin_ws && catkin_make


ENTRYPOINT /bin/bash