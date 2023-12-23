#!/bin/python
from gpiozero import Button, RGBLED
import time
import datetime
from signal import pause

import board
import busio
import adafruit_ssd1306

from PIL import Image, ImageDraw, ImageFont

## sCREEN SETUP


i2c = busio.I2C(board.SCL, board.SDA)

oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c)

oled.fill(0)
oled.show()

## reed setup & file


filename = datetime.datetime.now()
filename = "/home/bike/" + filename.strftime("%Y-%m-%d %H_%M")


#reed switch goes between gpio 12 and gnd
reed = Button(12, bounce_time=0.001)



#function to print text
def printText(oled, text):
        
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("FreeSans.ttf", size=14)

    (font_width, font_height) = font.getsize(text)
    draw.text(
        (oled.width//2 - font_width//2, oled.height//2-font_height//2),
        text,
        font=font,
        fill=255
        )
    oled.image(image)
    oled.show()

printText(oled, "Ready to start")

def press():
    f = open(filename, "a")
    f.write(str(time.time())+"\n")
    printText(oled, "Running!")
#    time.sleep(10)
 #   printText(oled, "Paused")
    
reed.when_pressed = press

pause()
