def on_button_pressed_a():
    for index in range(3):
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
        basic.show_number(3 - index)
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    basic.show_string("GO!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
