import time
from machine import Pin
from machine import I2C
from ssd1306 import SSD1306_I2C

width = 128
height = 64


def init_display():
    try:
        i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)
        addr = i2c.scan()[0]
        display = SSD1306_I2C(width, height, i2c, addr)
        return display
    except Exception:
        pass
    
    return None
    
def write_some_text(display):
    display.fill(0)
    display.text('Byte me!', 5, 5)
    display.text('123456789012345', 5, 16)
    display.text('...............', 5, 26)
    display.text('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 5, 36)
    display.show()


def draw_some_pixels(display):
    x = 0
    y = 0

    for _ in range(64):
        display.fill(0)

        display.pixel((x % width), (y % height), 1)
        display.pixel((x % width) + 2, (y % height) + 1, 1)
        display.pixel((x % width) + 4, (y % height) + 2, 1)
        display.pixel((x % width) + 6, (y % height) + 3, 1)
        display.pixel((x % width) + 8, (y % height) + 4, 1)
        display.show()
        x += 2
        y += 1
        time.sleep(.05)
    
    
def draw_ssd1306_demo(display):
    display.fill(0)
    offset = 16
    display.fill_rect(0, offset+0, 32, 32, 1)
    display.fill_rect(2, offset+2, 28, 28, 0)
    display.vline(9, offset+8, 22, 1)
    display.vline(16, offset+2, 22, 1)
    display.vline(23, offset+8, 22, 1)
    display.fill_rect(26, offset+24, 2, 4, 1)
    display.text('MicroPython', 40, offset+0, 1)
    display.text('SSD1306', 40, offset+12, 1)
    display.text('OLED 128x64', 40, offset+24, 1)
    display.show()



if __name__ == '__main__':
    delay = 3
    display = init_display()
    while True:
        write_some_text(display)
        time.sleep(delay)
        draw_some_pixels(display)
        # time.sleep(delay)
        draw_ssd1306_demo(display)
        time.sleep(delay)
