#!/bin/bash
export DISPLAY=:1
export VNC_PORT=5901
export NOVNC_PORT=6081

# set vnc password
echo "password" | vncpasswd -f > ~/.vnc/passwd
chmod 600 ~/.vnc/passwd

# start VNC server
vncserver -kill $DISPLAY
rm -rf /tmp/.X1-lock
rm -rf /tmp/.X11-unix/X1
vncserver $DISPLAY -depth 16 -geometry 1280x800
# Wait for VNC server to start
sleep 1

# Start noVNC
cd /opt/novnc
./utils/novnc_proxy --listen :$NOVNC_PORT --vnc :$VNC_PORT 

