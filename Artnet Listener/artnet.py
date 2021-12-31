import PythonArtNet


UDP_IP = "127.0.0.1"
UDP_PORT = 6454

udp_listener = PythonArtNet.listener(UDP_IP, UDP_PORT)
universe = 1
dmx_channel = []



try:
    while True:
        data, addr = udp_listener.getData()
        if udp_listener.getCurrentUniverse(data) == universe:
            dmx_channel = udp_listener.parseDMXChannel(data)
            print(dmx_channel[0])
        
            
except KeyboardInterrupt:
    print("KeyBoard Interrupt")