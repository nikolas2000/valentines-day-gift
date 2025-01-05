# I created a function that prints a heart using only symbols and spaces. Just for fun!
# 5/1/2024.

import time
symbol ="*" #-,+,*,e.t.c.

def sendHeart():
    width = input() #19 for example
    validation = int(width)%2!=0 and int(width)>=7 and int(width)<=45
    if(validation == False):
        print("Please give a correct odd number (>=7 & <=45)")
        sendHeart()
    else:
        heart(int(width))
        
def heart(width):
    upBody(width)
    downBody(width)

def upBody(length):
    leftSpaces=3
    midSpaces=5
    maxleftStars = (length-2)//2 #-2 because we the full symbol line is included in the down body
    decreaseLeftSpaces=4
    while (leftSpaces>0):
        leftStars = maxleftStars - decreaseLeftSpaces
        print(" " * leftSpaces + symbol * leftStars + " " * midSpaces + symbol * leftStars)
        time.sleep(0.5) #put a delay for 0.5 second just for the simple "animation"
        leftSpaces-=1
        midSpaces-=2
        decreaseLeftSpaces-=2
def downBody(length):
    stars=length
    leftSpaces=0
    while stars>0:
        print(" " * leftSpaces + symbol * stars)
        time.sleep(0.5) #put a delay for 0.5 second just for the  simple "animation"
        stars-=2
        leftSpaces+=1

print("Send love giving a correct odd number (>=7 & <=45)")
sendHeart()