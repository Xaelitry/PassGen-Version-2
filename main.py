import validator
import generator
import os
import time

# Console Name
os.system('title Xaelitry\'s Secure Password Generator')

# Variable Storage
helloText = '''
###############################
##                           ##
##   Welcome to Xaelitry's   ##
## Secure Password Generator ##
##                           ##
###############################
'''
menu = '''
[1] Generate password
[2] Generate password without selected characters \n    (for login portals that only accept some symbols)
'''

print(helloText)

if __name__ == '__main__':
    while True:
        print(menu)

        # Menu Selection
        mS = input('\nSelect which option you would like to perform [1/2]: ')
        if mS == "1":
            generator.generate()
        elif mS == "2":
            validator.validate()
            validator.generate()

        # Check for continue / close
        cont = input('Do you want to continue? [Y/N] ')
        yes = ['y', 'Y', 'yes', 'Yes', 'YES']
        no = ['n', 'N', 'no', 'No', 'NO']
        if cont in yes:
            print('Moving onto next job.')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif cont in no:
            print('Closing application.')
            time.sleep(3)
            exit()
        else:
            print('An error occurred, input was not recognized.')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
