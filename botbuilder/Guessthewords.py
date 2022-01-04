#GuessTheWords
import random
name = input('Whats your name?')
print('Hello, I see you want to read your future')
print('Good Luck!,',name)
print('(reading your future...)') 
words = ['You become rich','You become spoiled and go to hell','You go to heaven','You go in jail for robbing a bank','You become the president of the U.S.A']
sentence = random.choice(words)
print(sentence)




