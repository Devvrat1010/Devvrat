# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:51:48 2020

@author: Devvrat
"""

print("odd = 1\neven = 2")
a=int(input("select odd or even : "))
print (a)
if a%2==0 :
    print("you chose even")
elif a%2 ==1:
    print("you chose odd")
x=int(input("choose a number from 1 to 6 : "))
import random
b=random.randint(0,6)
print("computer played",b)
c=x+b
print(c)
p=0
computer=0
if c%2==0 and a%2==0:
    print("you won the toss")
    print("choose \n 1-bat\n2-ball ")
    x=int(input("choose to bat or ball first"))
    if x==1:
        print("you chose to bat first\nscore run by typing any number from 1 to 6")
        for i in range(24):
            
            a=int(input("score run"))
            b=random.randint(0,6)
            p=p+a
            print("run")
            print("computer bowled",b) 
            
            if a==8:
                break
            if b==a:
                print("computer bowled you")
                print("now it computer's turn to bat")
                print("type a number from 0 to 6 to throw a delivery to computer")
        
                for i in range(24):
                    b=random.randint(0,6)
                    computer=0
                    a=int(input("bowl a ball"))
                    print("computer played",b)
                    computer+=b
                    print("computer scored a total of ",computer,"runs")
                    if a==b:
                        print("Game Over")
                        break
                break    
    elif x==2:
            print("you chose to ball first\n\ntype a number from 0 to 6 to throw a delivery to computer")
            while True:
                b=random.randint(0,6)
                a=int(input("type a delivery"))
                print("computer played",b)
                if b==a:
                    print("you bowled computer\n\nnow its your turn to bat\n\nscore run by typing any number from 1 to 6 ")
                    #print("now its your turn to bat\n\nscore run by typing any number from 1 to 6")
                    while True:
                        a=int(input("score run"))
                        b=random.randint(0,6)
                        print("computer bowled",b)
                        if b==a :
                            print("computer bowled you\n\nGame Over ")
                            #print("Game Over")
                            break
                    break    

                    



elif c%2==0 and a%2==1:
    print("you lost the toss\n\ncomputer won the toss ")
    b=random.randint(1,2)
    if b==1:
        print("computer chose to bat first\n\ntype a number from 0 to 6 to throw a delivery to computer")
        while True:  
            a=int(input("bowl a ball"))
            b=random.randint(0,6)
            print("computer played",b)
            if a==b:
                print("you bowled computer\n\n Now its your turn to bat\n\nscore run by typing any number from 1 to 6")
                while True:
                       a=int(input("score run"))
                       b=random.randint(0,6)
                       print("computer bowled",b)
                       if b==a :
                            print("computer bowled you\n\nGame Over ")
                            #print("Game Over")
                            break
                break 
    else:
        print ("computer chose to ball first\n\nscore run by typing any number from 1 to 6")
        while True:  
            a=int(input("Score a run : "))
            b=random.randint(0,6)
            
            print("computer bowled",b)
            if a==b:
                print("computer bowled you \n\n Now it your turn to ball\n\ntype a number from 0 to 6 to throw a delivery to computer")
                while True:
                       a=int(input("bowl a ball"))
                       b=random.randint(0,6)
                       print("computer played",b)
                       if b==a :
                            print("you bowled computer\n\nGame Over ")
                            #print("Game Over")
                            break
                break 
    
            


elif c%2==1 and a%2==1:
    print ("you won the toss")
    print("choose \n 1-bat\n2-ball ")
    x=int(input("choose to bat or ball first"))
    if x==1:
        print("you chose to bat first\nscore run by typing any number from 1 to 6")
        while True:
            a=int(input("score run"))
            b=random.randint(0,6)
            print("computer bowled",b) 
            if b==a:
                print("computer bowled you")
                print("now it computer's turn to bat")
                print("type a number from 0 to 6 to throw a delivery to computer")
        
                while True:
                    b=random.randint(0,6)
                    a=int(input("bowl a ball"))
                    print("computer played",b)
                    if a==b:
                        print("Game Over")
                        break
                break    
    elif x==2:
            print("you chose to ball first\n\ntype a number from 0 to 6 to throw a delivery to computer")
            while True:
                b=random.randint(0,6)
                a=int(input("type a delivery"))
                print("computer played",b)
                if b==a:
                    print("you bowled computer\n\nnow its your turn to bat\n\nscore run by typing any number from 1 to 6 ")
                    #print("now its your turn to bat\n\nscore run by typing any number from 1 to 6")
                    while True:
                        a=int(input("score run"))
                        b=random.randint(0,6)
                        print("computer bowled",b)
                        if b==a :
                            print("computer bowled you\n\nGame Over ")
                            #print("Game Over")
                            break
                    break  




elif c%2==1 and a%2==0:
    print("you lost the toss\n\ncomputer won the toss ")
    b=random.randint(1,2)
    if b==1:
        print("computer chose to bat first\n\ntype a number from 0 to 6 to throw a delivery to computer")
        while True:  
            a=int(input("bowl a ball"))
            b=random.randint(0,6)
            print("computer played",b)
            if a==b:
                print("you bowled computer\n\n Now its your turn to bat\n\nscore run by typing any number from 1 to 6")
                while True:
                       a=int(input("score run"))
                       b=random.randint(0,6)
                       print("computer bowled",b)
                       if b==a :
                            print("computer bowled you\n\nGame Over ")
                            #print("Game Over")
                            break
                break 
    else:
        print ("computer chose to ball first\n\nscore run by typing any number from 1 to 6")
        while True:  
            a=int(input("Score a run : "))
            b=random.randint(0,6)
            
            print("computer bowled",b)
            if a==b:
                print("computer bowled you \n\n Now it your turn to ball\n\ntype a number from 0 to 6 to throw a delivery to computer")
                while True:
                       a=int(input("bowl a ball"))
                       b=random.randint(0,6)
                       print("computer played",b)
                       if b==a :
                            print("you bowled computer\n\nGame Over ")
                            #print("Game Over")
                            break
                break 
    

