import math
import sys
from os import rename

import requests

print(sys.version)

test = "Test"

r = requests.get("https://coreyms.com")
print(r.status_code)


# python autoformat:
# install formater, keyboard shortcut
# Shift + ALT + f

# sort imports; CTRL + SHIFT + P

name = input("Your Name?")
print("\nHello, ", name)


