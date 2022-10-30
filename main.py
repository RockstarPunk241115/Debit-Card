def on_button_pressed_a():
    global units, to_change, tens, hundreds, thousands
    if to_change == units:
        units += -1
        to_change = units
    elif to_change == tens:
        tens += -1
        to_change = tens
    elif to_change == hundreds:
        hundreds += -1
        to_change = hundreds
    elif to_change == thousands:
        thousands += -1
        to_change = thousands
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global units, to_change, tens, hundreds, thousands
    if to_change == units:
        units += 1
        to_change = units
    elif to_change == tens:
        tens += 1
        to_change = tens
    elif to_change == hundreds:
        hundreds += 1
        to_change = hundreds
    elif to_change == thousands:
        thousands += 1
        to_change = thousands
    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global which
    which += 1
    if which == 1:
        basic.show_string("ones")
    if which == 2:
        basic.show_string("tens")
    if which == 3:
        basic.show_string("hundreds")
    if which == 4:
        basic.show_string("thousands")
    if which > 4:
        basic.show_string("ones")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

money = 0
thousands = 0
tens = 0
units = 0
to_change = 0
which = 0
hundreds = 0
hundreds = 5
which = 1

def on_forever():
    global money
    money = thousands * 1000 + hundreds * 100 + (tens * 10 + units)
    basic.show_string("" + str((money)))
    basic.pause(5000)
basic.forever(on_forever)

def on_forever2():
    global to_change, which
    if which == 1:
        to_change = units
    if which == 2:
        to_change = tens
    if which == 3:
        to_change = hundreds
    if which == 4:
        to_change = thousands
    if which > 4:
        which = 1
        to_change = units
basic.forever(on_forever2)
