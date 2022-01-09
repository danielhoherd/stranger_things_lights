# Stranger Things Lights

This repo holds software for a project that is described in [a blog post about recreating a famous scene from Stranger Things](https://www.tomshardware.com/how-to/stranger-things-lights-raspberry-pi). This project makes use of the following technologies:

- raspberry pi OS
- the linux terminal (bash)
- git
- python3
- flask
- docker
- docker-compose
- ip version 4 networking
- ws8211 programmable LEDs (neopixel)

This list may look daunting to newcomers, but don't worry, it's not as scary as it may look, and might just be an exciting introduction to technologies you can use far and wide!

## Installation

This project involves assembling some hardware, and configuring and running some software. The blog post describing it can be found here: <https://www.tomshardware.com/how-to/stranger-things-lights-raspberry-pi>

### Hardware Prerequisites

Complete all the hardware steps shown in [the original blog post](https://www.tomshardware.com/how-to/stranger-things-lights-raspberry-pi). If you're unsure that you have the hardware connected right, the software does twinkle all the lights when it starts up, so once you're fairly confident that you've got the hardware done right, go ahead and move on to the software part.

### Software Prerequisites

1. Raspberry Pi running raspios bullseye or newer. Here's [a link to the 64 bit version of raspios](https://downloads.raspberrypi.org/raspios_arm64/images/) for pi3b and pi4, and [instructions on how to install raspios](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system).
2. Optionally disable the desktop and enable ssh if you're going to be connecting remotely. These can be done in `raspi-config` 1 S5 B1, and 3 I2.
3. Docker installed on the raspberry pi. Instructions to do this are found in the [docker/docker-install github repository](https://github.com/docker/docker-install).
4. Make sure your user has docker group access via `sudo usermod -aG docker "$USER"`.
5. Reboot, then make sure docker is running and your user has the needed access by running `docker info`.

### Project installation

1. Clone the repo via `git clone https://github.com/danielhoherd/stranger_things_lights` and then `cd stranger_things_lights`
2. Run `make run`. This step will download ~1GB of docker images and build two docker containers, then launch them via docker-compose. It will likely take more than a few minutes. You'll know you're done if the lights twinkle.

## Using

1. Find the LAN ip address of your raspberry pi. There are many ways to find this. One is `ip route get 4.2.2.1 | awk '{print $7}'`. Another is `curl -s -w '%{local_ip}\n' github.com`.
2. Navigate to `http://<pi_ip_address>:5000/` and test it out by inputting a sequence of letters like `zyxwvutsrqponmlkjihgfedcba`.
3. If everything is working, you can play with the arrangement of letters on the strand by editing `worker/app.py` and changing the mapping of letters to the numbered LED addresses. Any time you change this, you will have to press `ctrl-c` in the terminal where you ran `make run` and then run `make run` again.

## TODO

- Improve this experience of mapping the letters to numbers. Try to make it so the server doesn't have to restart, because that takes a long time and requires juggling terminals.
- Figure out why non-alpha characters are not working.
- Find a way to synchronize prefs across both components. EG: `char_limit` has to be edited in both places, and if we could reduce that to one place that would be better.
