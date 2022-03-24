'''
Created on Sep 13, 2019

@author:toni
'''
import time


def duration(_):
    '''Call a function, measure its execution time and return the time value.
    '''
    start = time.time()
    _
    end = time.time()
    print('\nTime required:', (end-start))


def main():
    duration(sum([3, 5, 2]))


if __name__ == "__main__":
    main()
