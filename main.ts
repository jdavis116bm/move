let distance = cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters)
cuteBot.moveTime(cuteBot.Direction.forward, 50, 2)
while (distance < 10) {
    cuteBot.stopcar()
    cuteBot.colorLight(cuteBot.RGBLights.ALL, 0xff0000)
}
