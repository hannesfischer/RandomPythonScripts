from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time as t
import random

trailing = 3

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.pwm_lsb_nanoseconds = 200
options.gpio_slowdown = 2
options.brightness = 100
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

canvas = matrix.CreateFrameCanvas()

def calculate_array(start, len, dir, pitch):
    array = []
    for x in range(len):
        if dir == 0:
            array.append(start-(x*pitch))
        if dir == 1:
            array.append(start+(x*pitch))
    return array




try:
    while True:
        yval = random.randint(10, 20)
        xval = 0
        xtop = random.randint(40, 55)
        while xval < xtop:
            matrix.SetPixel(xval, yval, 255, 255, 255)
            xval += 1
            t.sleep(0.01)
            try:
                matrix.SetPixel(xval-trailing, yval, 0, 0, 0)
            except:
               pass
        for x in range(xtop - trailing, xtop):
            matrix.SetPixel(x, yval, 0, 0, 0)
        
        burst_count = random.randint(6, 10)
        for x in range(burst_count):
            burst_len = random.randint(4, 10)
            dirx = random.randint(0, 1)
            diry = random.randint(0, 1)
            xpitch = random.randint(1, 3)
            ypitch = random.randint(1, 2)
            burstx = calculate_array(xtop, burst_len, dirx, xpitch)
            bursty = calculate_array(yval, burst_len, diry, ypitch)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            for y in range(burst_len):
                matrix.SetPixel(burstx[y], bursty[y], r, g, b)

        t.sleep(2)
        canvas.Clear()
        matrix.SwapOnVSync(canvas)


except KeyboardInterrupt:
    print("Exiting ...")