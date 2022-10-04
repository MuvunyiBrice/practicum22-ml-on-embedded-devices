# practicum22-ml-on-embedded-devices
This is the development environment of the Fall22 CMUA practicum project

## Installing Docker (Windows 11)
 
### Prerequisite:
 You need to have virtualization enabled before installing docker desktop [how to enable virtualization](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v).
1. Navigate to [Install Docker Desktop on Windows | Docker Documentation](https://docs.docker.com/desktop/install/windows-install/) and download "Docker Desktop for Windows.”
2. Double-click Docker Desktop Installer.exe to run the installer.
3. When prompted, ensure the Use WSL 2 instead of Hyper-V option on the Configuration page is selected or not, depending on your choice of backend.
4.  Follow the instructions on the installation wizard to authorize the installer and proceed with the installation.
5.  When the installation is successful, click Close to complete the installation process.
6.  This setup assumes you are installing as an admin user, but if it’s not the case, you must add the user to the docker-users group. Run Computer Management as an administrator and navigate to Local Users and Groups > Groups > docker-users. Right-click to add the user to the group. Log out and log back in for the changes to take effect.
Docker automatically starts after installation. The whale in the status bar indicates a running (and accessible via terminal) Docker instance.
You can open any Windows command tool (PowerShell or CMD) on your PC and run:

`$docker run hello-world`

Although the windows command line can run all docker commands, for this documentation, we will be using the Windows Subsystem for Linux (WSL) that equips our windows OS with a Linux kernel on which we can run Linux commands. [Install WSL | Microsoft Learn](https://learn.microsoft.com/en-us/windows/wsl/install).
 
 

## Creating an Ubuntu Docker image and installing a C compiler and the Arduino IDE
### Prerequisites:
Install [Windows X server](https://sourceforge.net/projects/vcxsrv/) (leave everything on default) to allow native Linux GUI applications to be run from the command line (this is only necessary if you’re using a Windows OS).
Create a Dockerfile with a text editor of your choice
`$nano Dockerfile`

Add the commands obtained from [tombenke/darduino](https://github.com/tombenke/darduino/blob/master/Dockerfile)'s Dockerfile. 

Changes made:
1. Install Ubuntu 20 instead of Ubuntu 16
2. Install `openjdk-8-jre` instead of `openjdk-9-jre` as `openjdk-9-jre` was raising errors
3. Install `gcc` and `gcc-multilib` to compile C code

Build an image from the Dockerfile in the current directory and tag the image

`$docker build -t image_name:tag` .

Create and run a writable container

`$docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v "$(pwd)"/shared_space_host:/home/developer/shared_space_docker image_name:tag`

The -v tag is used to bind mount a volume, in this case we’re mounting the display and a directory where the host and container can share files.

Inside the docker container, start Arduino:

`$arduino`

Incase you close your container and want to access it again, run:

`$docker start container-name`

to start your container, and:

`$docker attach container-name`

to access it.

**Comments:** Installing docker itself and creating and accessing a container wasn't a challenge, the difficulty came about running GUI apps from the container.
