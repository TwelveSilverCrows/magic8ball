def on_gesture_shake():
    global x
    x = randint(1, 3)
    if x == 1:
        basic.show_string("Yes")
        basic.show_icon(IconNames.HAPPY)
    elif x == 2:
        basic.show_string("No")
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_string("Try again later...")
        basic.show_icon(IconNames.CONFUSED)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

x = 0
basic.show_string("Ask me and shake")