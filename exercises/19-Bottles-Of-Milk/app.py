"""Ninety-Nine Bottles of Milk on the Wall
 By Al Sweigart al@inventwithpython.com
 Print the full lyrics to one of the longest songs ever! Press
 Ctrl-C to stop.
 This code is available at https://nostarch.com/big-book-small-python-programming
 Tags: tiny, beginner, scrolling"""
 


bottles = 99  # This is the starting number of bottles.
PAUSE = 2  # (!) Try changing this to 0 to see the full song at once.
 
try:
     while bottles > 1:  # Keep looping and display the lyrics.
         print(bottles, 'bottles of milk on the wall,')

         print(bottles, 'bottles of milk,')

         print('Take one down, pass it around,')
 
         bottles = bottles - 1  # Decrease the number of bottles by one.
         print(bottles, 'bottles of milk on the wall!')

         print()  # Print a newline.
 
     # Display the last stanza:
     print('1 bottle of milk on the wall,')

     print('1 bottle of milk,')

     print('Take it down, pass it around,')

     print('No more bottles of milk on the wall!')