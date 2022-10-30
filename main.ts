input.onButtonPressed(Button.A, function () {
    if (to_change == units) {
        units += -1
        to_change = units
    } else if (to_change == tens) {
        tens += -1
        to_change = tens
    } else if (to_change == hundreds) {
        hundreds += -1
        to_change = hundreds
    } else if (to_change == thousands) {
        thousands += -1
        to_change = thousands
    } else {
    	
    }
})
input.onButtonPressed(Button.B, function () {
    if (to_change == units) {
        units += 1
        to_change = units
    } else if (to_change == tens) {
        tens += 1
        to_change = tens
    } else if (to_change == hundreds) {
        hundreds += 1
        to_change = hundreds
    } else if (to_change == thousands) {
        thousands += 1
        to_change = thousands
    } else {
    	
    }
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("" + (money))
    basic.pause(1000)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    which += 1
    if (which == 1) {
        basic.showString("ones")
    }
    if (which == 2) {
        basic.showString("tens")
    }
    if (which == 3) {
        basic.showString("hundreds")
    }
    if (which == 4) {
        basic.showString("thousands")
    }
    if (which > 4) {
        basic.showString("ones")
    }
})
let money = 0
let thousands = 0
let tens = 0
let units = 0
let to_change = 0
let which = 0
let hundreds = 0
hundreds = 5
which = 1
basic.forever(function () {
    money = thousands * 1000 + hundreds * 100 + (tens * 10 + units)
})
basic.forever(function () {
    if (which == 1) {
        to_change = units
    }
    if (which == 2) {
        to_change = tens
    }
    if (which == 3) {
        to_change = hundreds
    }
    if (which == 4) {
        to_change = thousands
    }
    if (which > 4) {
        which = 1
        to_change = units
    }
})
