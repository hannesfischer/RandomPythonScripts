from smbus import SMBus

class IOBoard:
    def __init__(self, addr, bus=1):
        self.address = addr
        self.busno = bus

    def begin(self):
        self.bus = SMBus(self.busno)
        #set PORTA as output
        self.bus.write_byte_data(self.address, 0x00, 0x00)
    
    def read_inputs(self):
        self.inputs = self.bus.read_byte_data(self.address, 0x13)
        return self.inputs
    
    def write_outputs(self, data):
        try:
            self.bus.write_byte_data(self.address, 0x12, data)
            return True
        except:
            return False
    
    def write_led(self, ledno, value):
        if ledno < 1 or ledno > 8:
            raise ValueError("LED Number out of range! Allowed 1 <-> 8")
        else:
            ledno = ledno - 1
            self.leds = self.bus.read_byte_data(self.address, 0x12)
            if value == True:
                self.leds |= (1 << ledno)
            elif value == False:
                self.leds &= ~(1 << ledno)
            else:
                raise ValueError("value not a boolean (\"True\" | \"False\")")
            self.bus.write_byte_data(self.address, 0x12, self.leds)
    
    def get_button(self, button):
        if button < 1 or button > 8:
            raise ValueError("Button Number out of range! Allowed 1 <-> 8")
        else:
            self.inputs = self.bus.read_byte_data(self.address, 0x13)
            bytestring = str(bin(self.inputs))[2:]
            bytestring = bytestring.zfill(8)[::-1]
            return bytestring[button - 1]