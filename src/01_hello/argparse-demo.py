#! /usr/bin/env  python

# argparse demo
import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Name to greet')
parser.add_argument('age', age='how old are you')


args = parser.parse_args()

print(args.name)
print(args.age)




