#! /usr/bin/env python3.8

import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number
    half_num = number / 2

    def find_root(number, half_num):

        root = (half_num + number / half_num) / 2
        square = root*root
        if round(square) == number:
            return root
        elif round(square) > number:
            return find_root(number, root)
        else:
            grater = root + 1
            if round(grater*grater) > number:
                return root

    
    root = find_root(number, half_num)

    return math.floor(root)



print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (394 == sqrt(155777)) else "Fail")
print ("Pass" if  (28_103 == sqrt(789_789_789)) else "Fail")
