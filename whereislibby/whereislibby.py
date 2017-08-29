import ugfx, gc, wifi, badge, deepsleep
from time import *
import urequests as requests
import esp

def whereislibby():

    ugfx.init()

    # run at boot, but not after deep sleep - https://wiki.sha2017.org/w/Projects:Badge/MicroPython#import_esp
    esp.rtcmem_write_string("whereislibby", 2)

    # Make sure WiFi is connected
    wifi.init()

    ugfx.clear(ugfx.WHITE);
    ugfx.string(10,10,"Waiting for wifi.....","Roboto_Regular12", 0)
    ugfx.flush()

    # Wait for WiFi connection
    while not wifi.sta_if.isconnected():
        sleep(0.1)
        pass


    # loading screen
    ugfx.clear(ugfx.WHITE);
    ugfx.string(10,10,"Getting where libby is ...","Roboto_Regular12", 0)
    ugfx.flush()

    # fetching data
    url = "https://example.com/where.json"
    r = requests.get(url)
    gc.collect()
    data = r.json()
    r.close()

    ugfx.clear();
    ugfx.string(5, 5, "Where is libby?", "PermanentMarker22", 0)

    ds = data["description"]

    ugfx.string(0, 70, str(ds), "PermanentMarker36", 0)

    ugfx.flush(ugfx.LUT_FULL);

    badge.eink_busy_wait()
    deepsleep.start_sleeping(3600000) # 60 mins
#   deepsleep.start_sleeping(600000) # 10 mins
#   deepsleep.start_sleeping(60000) # 1 min


whereislibby()
