docker run --name ubuntu22_vnc --entrypoint bash -dit --gpus device=1 \
    -p 5902:5901 \
	-v ~/:/multy_sunny \
    -v /media/sde1/multy/workspace:/workspace \
	ubuntu22_vnc