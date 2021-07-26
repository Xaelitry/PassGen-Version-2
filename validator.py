import random
import os
import time
from pathlib import Path

file = Path('Output.txt')
fname = 'Output.txt'
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def validate():
    val = input('Enter valid characters here\nex: !@#%+=: ')
    global chars
    chars = chars + val
    return chars

def randompass(length):
    return "".join([random.choice(chars) for x in range(int(length))])

def generate():
    p = input('What is the password for? ')
    mail = input('Enter email attached to account: ')
    lenV = input('Set length for password: ')

    if lenV.isdigit():
        pw = randompass(int(lenV))

        v = ""
        v = v.join(p.title()+":\nEmail: "+mail+"\nPassword: "+pw)
            
        if file.is_file():
            with open(fname, 'a') as f:
                f.write("\n\n"+v)
                f.close()
                print('\nGenerated password for '+p.title()+'\nPassword: '+pw+'\n\nPassword has also been written to file in '+fname+'.\n\n')
        else:
            with open(fname, 'w+') as f:
                f.write(v)
                f.close()
                print('\nGenerated password for '+p.title()+'\nPassword: '+pw+'\n\nPassword has also been written to file in '+fname+'.\n\n')

    else:
        print("Input for length was not a number, try again.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
