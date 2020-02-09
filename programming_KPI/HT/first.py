# -*- coding: utf-8 -*-

"""
Редактор Spyder

Это временный скриптовый файл.
"""
import math as m
import sys

def wanna_more ():
    answer = input('''If u wanna to start again press Y
            If u wanna to stop the programm press N ...   ''')
    if answer == 'Y':
        main()
    if answer == 'N':
        sys.exit(0)



def number_equal ():
    a = int(input('Enter the first number'))
    b = int(input('Enter the first number'))
    c = int(input('Enter the first number'))
    
    if a > b and a > b:
        return a
    if b > a and b > c:
        return b
    if c > a and c > a:
        return c
    if a == b == c:
        print ('all numbers is equal')
        return (a)
def triangle_geron ():
    a = float(input('Enter the First side of triangle: '))
    b = float(input('Enter the Second side of triangle: '))
    c = float(input('Enter the Third side of triangle: '))
    p = (a + b + c)/2
    S = m.sqrt(p*(p-a)*(p-b)*(p-c))
    print ('The area of triangle is :  ', S)
    return S
def mass_converter():
    print('Input mass in grams: ', end='')
    a = int(input())
    a = a / 1000
    print ('Mass kg is: ' , a )
    a = a / 1000
    print ('Mass tonn is: ' , a)
def bw_converter():
    print('''Its a byte-weight converter! Select ur type:
        1. B
        2. Kb
        3. MB
        4. GB:
            ...''')
    answer = int(input('Type your number here: '))
    weight = int(input('Input ur memory size: '))
    if answer == 1:
        print(weight , ' Bytes')
        weight = weight / 1024
        print(weight , ' KiloBytes')
        weight = weight / 1024
        print(weight , ' MegaBytes')
        weight = weight / 1024
        print(weight , ' GB')
    if answer == 2:
        print(int(weight*1024), ' Bytes' )
        print(weight , ' KiloBytes')
        weight = weight / 1024
        print(weight , ' MegaBytes')
        weight = weight / 1024
        print(weight , ' GB')
    if answer == 3:
        print(int(weight*1024*1024) , ' Bytes')
        print(int(weight*1024), ' KiloBytes' )
        print(int(weight) , ' MegaBytes')
        weight = weight / 1024
        print(weight , ' GB')
    if answer == 4:
        print(int(weight*1024*1024*1024) , ' Bytes')
        print(int(weight*1024*1024), ' KiloBytes' )
        print(int(weight*1024) , ' MegaBytes')
        print(weight , ' GB') 

    
def main():    
    print('''What u wanna do?
      1. Number comparison
      2. Find triangle area
      3. Mass converter
      4. Memory size converter''', end =(''))
    answer = input()
    if answer == '1':
        number_equal()
        wanna_more()
    elif answer == '2':
        triangle_geron()
        wanna_more()
    elif answer == '3':
        mass_converter()
        wanna_more()
    elif answer == '4':
        bw_converter()
        wanna_more()
main()

