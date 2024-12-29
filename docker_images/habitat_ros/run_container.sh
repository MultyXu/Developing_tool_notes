docker run --name habitat_ros_0 --entrypoint bash -dit --gpus device=0 \
    -p 5904:5901 \
	-v ~/:/multy_sunny \
    -v /media/sde1/multy/workspace:/workspace_sde \
    -v /media/sda1/multy:/workspace_sda \
    -v /home/tribhi/work/habicrowd:/tribhi_habicrowd \
	habitat_ros