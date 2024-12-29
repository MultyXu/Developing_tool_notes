docker run --name ubuntu20_gl_cuda11.4 --entrypoint bash -dit --gpus device=1 \
    -p 5903:5901 \
	-v ~/:/multy_sunny \
    -v /media/sde1/multy/workspace:/workspace_sde \
    -v /media/sda1/multy:/workspace_sda \
	ubuntu20_gl_cuda11.4