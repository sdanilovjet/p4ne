from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        IPv4Network.__init__(self,(random.randint(0x0b000000, 0xdf000000), random.randint(8, 24)), strict=False)

    def key_value(self):
        return

l = []
for x in range(0,50):
    l.append(IPv4RandomNetwork())

for x in l:
    print(x)
