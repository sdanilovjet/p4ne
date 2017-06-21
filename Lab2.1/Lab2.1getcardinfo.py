import requests
import argparse
import pprint
import sys

parser = argparse.ArgumentParser()

parser.add_argument("number_card", nargs="*")

args = parser.parse_args()

print(args)

#r = requests.get('https://lookup.binlist.net/[0-9]{8}')

#dir(r)
