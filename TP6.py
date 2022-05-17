def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def Demarrer_la_pompe():
    pass

def on_button_pressed_b():
    basic.show_number(randint(0, 100))
    if input.temperature() < 60:
        basic.show_string("Watering the plant")
    elif input.temperature() > 70:
        basic.show_string("Stopped watering the plant")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    for index in range(5):
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
        basic.pause(100)
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # # # # #
                        . . # . .
                        . . # . .
        """)
    basic.clear_screen()
    if 0 < 120:
        basic.show_string("Stopped watering")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    if input.light_level() > 120:
        pass
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    if input.temperature() <= 18:
        basic.show_string("Watering the plant")
basic.forever(on_forever)
