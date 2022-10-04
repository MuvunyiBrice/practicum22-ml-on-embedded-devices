docker run \
	-it \
	--rm \
	--network=host \
	-e DISPLAY=$DISPLAY \
	-v /tmp/.X11-unix:/tmp/.X11-unix
	-v $HOME/Arduino:/home/developer/Arduino \
	arduino:final \
	arduino
