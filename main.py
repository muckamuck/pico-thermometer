import time
from machine import Pin
from machine import I2C
from ssd1306 import SSD1306_I2C

width = 128
height = 64
segment_length = 20
left_margin = 28
spacing = 8


def init_display():
    try:
        i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)
        addr = i2c.scan()[0]
        display = SSD1306_I2C(width, height, i2c, addr)
        return display
    except Exception:
        pass

    return None


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


def seg_0(display, offset):
    x = left_margin + offset
    display.hline(x, 16, segment_length, 1)
    display.hline(x, 17, segment_length, 1)


def seg_1(display, offset):
    x = left_margin + offset
    display.vline(x, 17, segment_length, 1)
    display.vline(x+1, 17, segment_length, 1)


def seg_2(display, offset):
    x = left_margin + segment_length + offset
    display.vline(x, 17, segment_length, 1)
    display.vline(x+1, 17, segment_length, 1)


def seg_3(display, offset):
    x = left_margin + offset
    display.hline(x, segment_length + 16, segment_length, 1)
    display.hline(x, segment_length + 17, segment_length, 1)


def seg_4(display, offset):
    x = left_margin + offset
    display.vline(x, segment_length + 17, segment_length, 1)
    display.vline(x+1, segment_length + 17, segment_length, 1)


def seg_5(display, offset):
    x = left_margin + segment_length + offset
    display.vline(x, segment_length + 17, segment_length, 1)
    display.vline(x+1, segment_length + 17, segment_length, 1)


def seg_6(display, offset):
    x = left_margin + offset
    display.hline(x, 2 * segment_length + 16, segment_length, 1)
    display.hline(x, 2 * segment_length + 17, segment_length, 1)


def calculate_offset(power):
    if power == 0:
        offset = segment_length + spacing
    elif power == 1:
        offset = 0
    else:
        offset = 0

    return offset


def write_0(display, power):
    offset = calculate_offset(power)
    seg_0(display, offset)
    seg_1(display, offset)
    seg_2(display, offset)
    seg_4(display, offset)
    seg_5(display, offset)
    seg_6(display, offset)


def write_1(display, power):
    offset = calculate_offset(power)
    seg_2(display, offset)
    seg_5(display, offset)


def write_2(display, power):
    offset = calculate_offset(power)
    seg_0(display, offset)
    seg_2(display, offset)
    seg_3(display, offset)
    seg_4(display, offset)
    seg_6(display, offset)


def write_3(display, power):
    offset = calculate_offset(power)
    seg_0(display, offset)
    seg_2(display, offset)
    seg_3(display, offset)
    seg_5(display, offset)
    seg_6(display, offset)


def write_4(display, power):
    offset = calculate_offset(power)
    seg_1(display, offset)
    seg_2(display, offset)
    seg_3(display, offset)
    seg_5(display, offset)


def write_5(display, power):
    offset = calculate_offset(power)
    seg_0(display, offset)
    seg_1(display, offset)
    seg_3(display, offset)
    seg_5(display, offset)
    seg_6(display, offset)


def write_6(display, power):
    offset = calculate_offset(power)
    seg_0(display, offset)
    seg_1(display, offset)
    seg_3(display, offset)
    seg_4(display, offset)
    seg_5(display, offset)
    seg_6(display, offset)


def write_7(display, power):
    offset = calculate_offset(power)
    seg_0(display, offset)
    seg_2(display, offset)
    seg_5(display, offset)


def write_8(display, power):
    offset = calculate_offset(power)
    seg_0(display, offset)
    seg_1(display, offset)
    seg_2(display, offset)
    seg_3(display, offset)
    seg_4(display, offset)
    seg_5(display, offset)
    seg_6(display, offset)


def write_9(display, power):
    offset = calculate_offset(power)
    seg_0(display, offset)
    seg_1(display, offset)
    seg_2(display, offset)
    seg_3(display, offset)
    seg_5(display, offset)


def write_number(display, n):
    f = [
        write_0,
        write_1,
        write_2,
        write_3,
        write_4,
        write_5,
        write_6,
        write_7,
        write_8,
        write_9
    ]
    display.fill(0)
    if n >= 0 or n < 100:
        x = int(n / 10)
        if x > 0:
            f[x](display, 1)
        x = n % 10
        f[x](display, 0)

    display.show()


if __name__ == '__main__':
    display = init_display()
    for n in range(100):
        write_number(display, n)
        time.sleep(.2)
