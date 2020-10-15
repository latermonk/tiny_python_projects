#! /usr/bin/env python3


import argparse
import pathlib


def main():
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('name', help='Name to greet')
    #
    #
    args = parser.parse_args()
    #
    # print(pathlib.Path(__file__).parent.absolute())
    #
    print('Hello, World!   ' + args.name)



def test():
    print(pathlib.Path(__file__).parent.absolute())

if __name__ == '__main__':
    test()
