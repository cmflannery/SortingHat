#!/usr/bin/env python
import random
import subprocess as sp
import os
from common.ascii_art import AsciiImage, AsciiText
import time
import sys
import string


class sortingHat():
    def __init__(self, *arg):
        if arg:
            self.debug = arg[0]
        else:
            self.debug = False
        print('debug state:', self.debug)
        self.isPM = False
        self.quoteSpecified = False
        self.set_Constants()
        self.get_name()
        self.check_name()
        self.sort()
        self.show_result()

    def set_Constants(self):
        self.houses = ['Slytherin', 'Gryffindor', 'Hufflepuff', 'Ravenclaw']
        self.specialNames = {
            'harry potter': 'Gryffindor',
            'hermione granger': 'Gryffindor',
            'ron weasley': 'Gryffindor',
            'draco malfoy': 'Slytherin',
            'lord voldemort': 'Slytherin',
            'albus dumbledore': 'Gryffindor',
            'cameron flannery': 'Gryffindor',
            'michael phalen': 'Gryffindor',
            'alex lim': 'Hufflepuff',
            'parker brown': 'Ravenclaw',
            'brandon nyugen': 'Slytherin',
        }
        self.nameSpecifiedQuotes = {
            'harry potter': 0,
            'ron weasley': 1,
        }
        self.quotes = ['Hmm, difficult. VERY difficult. Plenty of courage, I see. Not a bad mind, either. There\'s talent, oh yes. And a thirst to prove yourself. But where to put you?',
                       'Ah! I know just what to do with you...',
                       'I\'ll have alook inside your mind and tell where you belong!',
                       'Curious, very curious...']

    def get_name(self):
        while True:
            if self.debug:
                break
            self.rawName = input('Enter your first and last name (ex: \'Nikola Tesla\'): ')
            if self.isEmpty(self.rawName):
                print('Error: Please enter your name.')
                continue
            else:
                break

        self.rawName = self.rawName.lower()
        self.asciiName = float(''.join(str(ord(c)) for c in self.rawName)) - 10**40

    def sort(self):
        random.seed(self.asciiName)
        if not(self.isPM):
            self.houseChoice = random.randrange(0, 4, 1)
            self.sortedHouse = self.houses[self.houseChoice]
        if not(self.debug):
            time.sleep(0.5)
            if self.quoteSpecified:
                self.get_quote(self.nameSpecifiedQuotes[self.rawName])
            else:
                self.get_quote()
            time.sleep(1.5)


    def show_result(self):
        houseText = AsciiText(self.sortedHouse.upper()+'!')
        houseText.display_text()
        print('\n')

    def print_crest(self):
        """print house crest *** NOT CURRENTLY USED*** """
        # prints ascii art of rocket stored in /resources/openrocketengine
        path = os.path.dirname(__file__)
        fname = os.path.join(path, 'assets', self.sortedHouse+'.jpg')

        logo_image = AsciiImage(fname)
        logo_image.display_image()

    def check_name(self):
        """check_name checks to see if the entered name is a principal member.
        If yes, house is predetermined with dictionary"""

        try:
            self.sortedHouse = self.specialNames[self.rawName]
            self.isPM = True
        except KeyError:
            self.isPM = False  # bool: is principal member of club
        try:
            self.nameSpecifiedQuotes[self.rawName]
            self.quoteSpecified = True
        except KeyError:
            self.quoteSpecified = False  # bool: is principal member of club

    def get_quote(self, *arg):
        if arg:
            i = arg[0]
        else:
            i = random.randrange(0, len(self.quotes), 1)
        self.delay_print(i)

    def delay_print(self, i):
        delayTime = 0.05
        for c in self.quotes[i]:
            if self.is_punct_char(c):
                delayTime = 0.15
            else:
                delayTime = 0.05
            sys.stdout.write('%s' % c)
            sys.stdout.flush()
            time.sleep(delayTime)

    def is_punct_char(self, c):
        '''check if char is punctuation char'''
        if c in string.punctuation:
            return 1
        else:
            return 0

    def isEmpty(self, text):
        if text:
            return False
        else:
            return True


if __name__ == '__main__':
    try:
        sp.call('clear')
    except OSError:
        sp.call('cls', shell=True)

    try:
        RPLsorting = sortingHat()
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt: Exiting')
