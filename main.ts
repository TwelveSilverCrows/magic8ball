input.onGesture(Gesture.Shake, function () {
    x = randint(1, 3)
    if (x == 1) {
        basic.showString("Yes")
        basic.showIcon(IconNames.Happy)
    } else if (x == 2) {
        basic.showString("No")
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showString("Try again later...")
        basic.showIcon(IconNames.Confused)
    }
})
let x = 0
basic.showString("Ask me and shake")
