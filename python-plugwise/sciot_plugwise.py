from plugwise.api import *
from pprint import pprint

port = "/dev/ttyUSB0"
mac = "000D6F000567125A"
stick = Stick(port)
circle = Circle(mac, stick)


port2 = "/dev/ttyUSB0"
mac2 = "000D6F0002C0E832"
stick2 = Stick(port2)
circle2 = Circle(mac2, stick2)


print("Current electricity Consumption: '{0}'".format(circle.get_power_usage()))

if 'TURNLIGHTON' in open('../FF-v2.3/output.txt').read():
    circle.switch_on()
    print("Light is On")

if 'TURNLIGHTOFF' in open('../FF-v2.3/output.txt').read():
    circle.switch_off()
    print("Light is Off")


if 'TURNFANON' in open('../FF-v2.3/output.txt').read():
    circle2.switch_on()
    print("Fan is On")


if 'TURNFANOFF' in open('../FF-v2.3/output.txt').read():
    circle2.switch_off()
    print("Fan Off")


if circle.get_info()['relay_state'] == 1:
	print("OK")
else:
	print("NOT OK")

print(circle.get_info())

