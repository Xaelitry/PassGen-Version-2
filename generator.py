import random
import os
from time import sleep
from pathlib import Path

# Variable Storage
file = Path('Output.txt')
fname = 'Output.txt'

# Function to generate the password
def randompass(length: int):
    return ''.join([random.choice('!@#$%^&*_+-=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for x in range(int(length))])

# Function to check user input for password generation
def generate():
    s = input('What is the password for? ')
    m = input('Enter email attached to account: ')
    l = input('Set length for password: ')

    if l.isdigit():
        p = randompass(int(l))
        v = ''
        v = v.join(s.title()+':\nEmail: '+m+'\nPassword: '+p)
        if file.is_file():
            with open(fname, 'a') as f:
                print('Generated password for '+s.title()+'\nPassword: '+p+'\n\nPassword has also been written to file in '+fname+'.\n\n')
                # File Reading
                lc = 0
                fr = open(fname, 'r')
                for line in fr.readlines():
                    if line == 0: lc = 0
                    elif line != 0: lc +=1
                fr.close()
                if lc != 0:
                    f.write('\n\n'+v)
                    f.close()
                else:
                    f.write(v)
                    f.close()
                
        else:
            with open(fname, 'w+') as f:
                f.write(v)
                f.close()
                print('Generated password for '+s.title()+'\nPassword: '+p+'\n\nPassword has also been written to file in '+fname+'.\n\n')
        
    else:
        print('Input for length was not a number, try again.')
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
