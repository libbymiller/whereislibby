# whereislibby

A very simple web based desk label based on https://wiki.sha2017.org/w/Projects:Badge

It's based on [weather](https://badge.sha2017.org/files/549)

I can't put it in the [hatchery](https://badge.sha2017.org) because it uses an internal system with a 
private url, which just gives you a json file of the form:

    {"description":"WFH"}

updated at midnight every day.

I've made this update every hour because sometimes I change my mind about where I am / will be.

Once you run it (from launcher) it continues to run while powered.

# Setup

I built it on Mac OS X using [these instructions](https://github.com/SHA2017-badge/Firmware).

    brew install libsdl2
    brew install hg
    hg clone https://hg.libsdl.org/SDL SDL
    cd SDL
    configure
    make
    sudo make install
    brew install mbedtls

    # emulator, though it doesn't seem to work unless it deoesn't depend on wifi etc libraries
    make -C micropython/unix 

    sudo easy_install pip
    sudo pip install adafruit-ampy

# Installing on the badge

    screen /dev/tty.SLAB_USBtoUART 115200

click the screen and type

    import shell

within 5 seconds

then get out of screen to free up the port

    ctrl-A ctrl-\ y 

install in the lib directory

    sudo ampy -p /dev/tty.SLAB_USBtoUART run whereislibby/whereislibby.py
    sudo ampy -p /dev/tty.SLAB_USBtoUART put whereislibby lib/whereislibby

