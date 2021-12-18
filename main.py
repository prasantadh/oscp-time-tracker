from os import name, system
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def banner():

    message  = "welcome! how dy du?\n"
    message += "[ current task ]\n"
    message += " - read the current task and print it out here\n"
    message += " - type p to pause or r to resume\n\n"
    message += "[ paused tasks ]\n"
    message += " - read the paused tasks and print them out here\n\n"
    message += "[ action options ]\n"
    message += "\t1. start a new task"

    clear()
    print(message)

import json
def main():
    banner()

if __name__=='__main__':
    main()
