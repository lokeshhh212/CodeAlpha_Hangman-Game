import random
words=["tower","chair","lenght","helmet","laptop"]
attempts=6
word=random.choice(words)
s=["_"]*len(word)
letter=[]

while attempts>0 and "_" in s:
    print(" ".join(s))
    print("Attempts :",attempts)
    l=input("Guess the letter:").lower()
    if l in letter:
        print("You already entered this letter")
        continue
    letter.append(l)
    if l in word:
        print("Correct Guess")
        for i in range(len(word)):
            if word[i]==l:
                s[i]=l
    else:
        print("Wrong Guess")
        attempts-=1
        
if "_" not in s:
    print("Congratulation you gussed the word!")
else:
    print("Game Over!")
    print("The Correct Word Was:",word)
            
        
        
    
