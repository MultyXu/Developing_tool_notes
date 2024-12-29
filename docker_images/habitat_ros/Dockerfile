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

# needed for build habitat-sim locally
RUN apt-get install -y --no-install-recommends \
    libjpeg-dev libglm-dev libgl1-mesa-glx libegl1-mesa-dev mesa-utils xorg-dev freeglut3-dev

# install git lfs
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && apt-get install git-lfs

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

########################### install conda ######################################
RUN mkdir -p ~/miniconda3 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh && \
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 && \
    rm ~/miniconda3/miniconda.sh
RUN /root/miniconda3/bin/conda init && \
    /root/miniconda3/bin/conda config --set auto_activate_base false && \
    /root/miniconda3/condabin/conda create -y -n habitat python=3.9 cmake=3.14.0 && \
    /root/miniconda3/condabin/conda create -y -n ros_env python=3.11

############################### install conda ros ##############################
SHELL ["/root/miniconda3/condabin/conda", "run", "-n", "ros_env", "/bin/bash", "-c"]

RUN conda config --env --add channels conda-forge && \
    conda config --env --add channels robostack-staging

RUN conda install -y ros-noetic-desktop 
RUN conda install -y ros-noetic-map-server ros-noetic-move-base ros-noetic-amcl
RUN conda install -y compilers cmake pkg-config make ninja colcon-common-extensions catkin_tools rosdep

############################# setup hatitat interface ##########################
SHELL ["/root/miniconda3/condabin/conda", "run", "-n", "ros_env", "/bin/bash", "-c"]

WORKDIR /root

RUN mkdir -p catkin_ws && mkdir -p src && \
    git clone -b v0.3 https://github.com/UMich-CURLY/habitat_ros_interface.git

# RUN cd ~/catkin_ws && catkin_make #TODO: need manual make maybe

############################ Build habitat from source #########################
SHELL ["/root/miniconda3/condabin/conda", "run", "-n", "habitat", "/bin/bash", "-c"]

WORKDIR /root

RUN git clone -b v0.3.0 https://github.com/facebookresearch/habitat-sim.git && git clone -b dev https://github.com/UMich-CURLY/habitat-lab.git

RUN cd ~/habitat-sim && \
    pip install -r requirements.txt && \
    python setup.py install --bullet --headless

RUN cd ~/habitat-lab && \
    pip install -e habitat-lab && \
    pip install -e habitat-baselines

RUN pip install IPython pygame==2.0.1 pybullet==3.0.4

# resolve dependencies issues
RUN pip install numpy==1.23.5 moviepy==1.0.1

############################## set up vnc ######################################
SHELL ["/bin/bash", "-c"]

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

# Define working directory.
WORKDIR /root

# Copy a script to start the VNC server
COPY start-vnc.sh start-vnc.sh
RUN chmod +x start-vnc.sh

ENTRYPOINT /bin/bash