docker run --name multy_latentbki_1 --entrypoint bash -dit --gpus device=1 \
	-v ~/:/multy_sunny \
    -v /media/sde1/multy/workspace:/workspace \
    -v /media/sda1/multy:/workspace_sda \
    -v /media/sde1/kitti:/KITTI \
	ubuntu20_cuda11.6.1