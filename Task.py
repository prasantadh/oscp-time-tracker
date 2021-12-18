from time import time
class Task:
    def __init__(self, title, platform, status):
        self.title = title
        self.platform = platform
        self.status = status
        self.work = [
                (int(time()), int(time()+10000))
                ]

    '''return hours spent on this task'''
    def hourson():
        print('return hours spend on this task')

