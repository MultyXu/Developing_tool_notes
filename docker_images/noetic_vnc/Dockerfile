FROM ros:noetic

# Install basic tools
RUN apt update && apt install -y \
    x11vnc xvfb openbox xterm wget sudo \
    ros-noetic-rviz ros-noetic-desktop-full \
    net-tools curl && \
    apt clean

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

CMD ["bash", "/home/docker/start.sh"]