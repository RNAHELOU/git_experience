from sense_emu import SenseHat

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
print(temp)