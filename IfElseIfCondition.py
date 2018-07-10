# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 16:07:51 2018

@author: ost01
"""
option == 1
while option != 0:
    print ("MENU")
    option = input()
    print ("please make a selection")
    print ("1. count")
    print ("0. quit")
    if option == 1:
        while option != 0:
            print ("1. count up")
            print ("2. count down")
            print ("0. go back")
            if option == 1:
                print ("please enter a number")
                for x in range(1, x, 1):
                    print (x)
                elif option == 2:
                    print ("please enter a number")
                    for x in range(x, 1, 1):
                elif option == 0:
                    break
                else:
                    print ("invalid command")
    elif option == 0:
        break