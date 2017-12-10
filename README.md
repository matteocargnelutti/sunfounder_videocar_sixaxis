# sunfounder_videocar_sixaxis
A quick Python Script to control the Sunfounder Smart Video Car with a PS3 Controller.

This script uses Python 2, as the whole SunFounder script is built around this version of Python.

## Prerequisites
You first need to pair your SIXAXIS with your Pi.

This guide helped me quite a lot : https://www.piborg.org/blog/rpi-ps3-help

You'll also need to install **pygame** if not already installed.

`sudo apt-get install python-pygame`

## Setup and launch
Just copy `server/sixaxis_server.py` into the `server` path.

**If your Pi is connected to a monitor :**

Pair your controller, and then launch `python sixaxis_server.py`.

**Otherwise :**

Run ./startcar.sh, which will export display : a work around to prevent **pygame** from crashing *(as it would normally need a display to work ... yeah I know, not ideal)*.

You may want to make this script launch at startup, so the car doesn't require an external computer to start : for that purpose, I would recommend to use **supervisor** to make this script run and restart automatically.