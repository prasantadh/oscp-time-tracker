from os import name, system
from Task import Task

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def create_task():
    print('title: ', end='')
    title = input()
    print('platform: ', end='')
    platform = input()
    print('description: ', end='')
    description = input()
    print('tags (space-separated): ', end='')
    tags = input()
    status = 'created'
    task = Task(title, platform, status, description, tags)
    return task

def banner():
    message  = "welcome! how dy du?\n"
    message += "[ current task ]\n"
    message += " - read the current task and print it out here\n"
    message += " - type p to pause or r to resume\n\n"
    message += "[ paused tasks ]\n"
    message += " - read the paused tasks and print them out here\n\n"
    message += "[ action options ]\n"
    message += "\t1. resume a task\n"
    message += "\t2. create a new task"

import json
def main():
    with open('oscp.json', 'r') as f:
        try:
            data = json.loads(f.read())
        except:
            data = {}
    clear()
    banner()
    print('make a choice: ', end='')
    choice = input()
    if choice == '1':
        task = create_task()
        if 'tasks' in data.keys():
            data['tasks'].append(task.__dict__)
        else:
            data['tasks'] = [task.__dict__]
    elif choice == 'p':
        task = pause_task()
    elif choice == 'r':
        task = resume_task()
    with open('oscp.json', 'w') as f:
        f.write(json.dumps(data))

if __name__=='__main__':
    main()
