from gpiozero import Button, LED

button = Button(14)
led = LED(17)


print("Press the button to toggle the LED.")


while True:
    if button.is_pressed:
        led.on()
        print("on!")
    else:
        led.off()
        print("off!")
