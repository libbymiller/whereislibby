# whereislibby

A very simple web based desk label using [SHA2017's badge](https://wiki.sha2017.org/w/Projects:Badge).

It's based on [weather](https://badge.sha2017.org/files/549).

I can't put it in the [hatchery](https://badge.sha2017.org) - which would make installation easier - 
because it uses an internal system with a private url, which just gives you a json file of the form:

    {"description":"WFH"}

updated at midnight every day.

I've made this update every hour because sometimes I change my mind about where I am / will be.

Once you run it (from launcher) it continues to run while powered, but it forgets when the badge is 
powered down.

# Setup

I built it on Mac OS X using [these instructions](https://github.com/SHA2017-badge/Firmware).

    brew install libsdl2
    brew install hg
    hg clone https://hg.libsdl.org/SDL SDL
    cd SDL
    configure
    make
    sudo make install

    # emulator, though it doesn't seem to work unless the app doesn't depend on wifi etc libraries specifci to the hardware (e.g. games)
    brew install mbedtls
    make -C micropython/unix 

    # shell thingy
    sudo easy_install pip
    sudo pip install adafruit-ampy

# Installing on the badge

    # Stop it deep sleeping
    # Wake up the badge using a button, then
    screen /dev/tty.SLAB_USBtoUART 115200
    import shell

within 5 seconds.

Then get out of screen to free up the port

    ctrl-A ctrl-\ y 

Install the app in the lib directory

    sudo ampy -p /dev/tty.SLAB_USBtoUART run whereislibby/whereislibby.py
    sudo ampy -p /dev/tty.SLAB_USBtoUART put whereislibby lib/whereislibby

# Links

* [micropython](https://wiki.sha2017.org/w/Projects:Badge/MicroPython)
* [micropython fonts](https://wiki.sha2017.org/w/Projects:Badge/MicroPython#Fonts)
* [ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/run-code) [ampy github](https://github.com/adafruit/ampy)
* [badge firmware instructions](https://github.com/SHA2017-badge/Firmware)
* [badge docs](https://wiki.sha2017.org/w/Projects:Badge/Documentation)
* [badge safe mode](https://wiki.sha2017.org/w/Projects:Badge/Documentation#Safe_mode)
* [micropython reference](https://micropython.org/resources/docs/en/latest/wipy/wipy/tutorial/repl.html)
