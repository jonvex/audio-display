import I2C_LCD_driver
import time
import atexit





class lcd:
    def __init__(self):
        #init lcd and turn off backlight
        this.__lcd = I2C_LCD_driver.lcd()
        this.__lcd.backlight(0)

        #load custom characters
        customCC = [      

            #music note
            [ 0b00001,
	          0b00011,
	          0b00101,
	          0b01001,
	          0b01001,
	          0b01011,
	          0b11011,
	          0b11000],
        ]
        this.__lcd.lcd_load_custom_chars(customCC)

        
        


