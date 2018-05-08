# -*- coding: utf-8 -*-
"""
Created on Sat May  5 22:40:12 2018

@author: lilly
"""

#function to calculate number on one certain square 
def on_square(square):
    
    while True:
        try:
            square = int(input('Please select a square. '))
                
            #possible error #1
        
            if 65 < square or square < 0:
                print()
                print('Sorry, this square does not exist. '
                      'A chessboard has 64 squares.')
                continue                
            
            #calculate amount of grains for valid selection
            elif 1 <= square <= 64: 
              
                amount_grains = 2 ** (square - 1)
                print()
                return(amount_grains)
                                
        #possible error #2     
        except ValueError: 
            print()
            print("That's not a number!")
            continue
           

#function to calculate number of grains on a square
#and all the following ones
def total_after(square):
    
    while True: 
        try:
            square = int(input('Please select a square. '))
            
            #possible error #1
            
            if square < 1 or square > 64:
                
                print()
                print('Sorry, this square does not exist. '
                      'A chessboard has 64 squares.')
                continue
            
            #calculate result for valid selection 
            
            elif 1 <= square <= 64:
                
                while True: 
                    #list for continous counting 
                    amount_grains = 0 
                
                    while True: 
                                       
                        if square <= 64: 
                            amount_square = 2 ** (square - 1)
                            amount_grains = amount_grains + amount_square
                            square = square + 1 
                            continue 
                        
                    elif square > 64: 
                        break
                
                print()
                return(amount_grains)
        
            #possible error #2
                                    
        except ValueError: 
            print()
            print("That's not a number!")
            continue
         
#apply functions in main       
if __name__ == '__main__':
    
    print('____The servant that could have gotten a shitton of gold but '
          'asked for grains instead____')
    print(" ~ Description I'm too lazy to write ~ ")
    print()
    print('To calculate the amount of grains on '
          'a certain square press 1.')
    print('To calculate the amount of grains on a '
          'square and all the following ones combined press 2.')
    
    #select which function to use/what to calculate    
    while True: 
        try:
            selection = int(input())
        
            if selection == 1:
                print('There are', on_square(selection), 
                      'grains on that square. ')
                break
            
            elif selection == 2:
                print('There are', total_after(selection), 
                      'grains on that square and all the squares afterwards.')
                break
        
            #possible error #1
            else:
                print()
                print('Please choose option 1 or 2.')
                continue
            
        #possible error #2
        except ValueError:
            print()
            print('Please choose option 1 or 2.')
            continue




