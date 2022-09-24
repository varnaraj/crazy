import speedtest
wifi  = speedtest()
print("Wifi Download Speed is ", wifi.download())
print("Wifi Upload Speed is ", wifi.upload())

#couldn't work