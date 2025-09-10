cuteBot.move_time(cuteBot.Direction.FORWARD, 100, 2)
cuteBot.move_time(cuteBot.Direction.BACKWARD, 100, 2)
cuteBot.stopcar()
basic.show_string("Hello!")
basic.show_leds("""
    . # . # .
    # # # # #
    # # # # #
    . # # # .
    . . # . .
    """)

def on_forever():
    pass
basic.forever(on_forever)
