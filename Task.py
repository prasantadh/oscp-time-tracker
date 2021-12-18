from time import time
class Task:
    def __init__(self, title, platform, status, description='', tags=''):
        self.title = title
        self.platform = platform
        self.status = status
        self.description = description
        import re
        tags = re.sub(' +', ' ', tags)
        self.tags = tags.strip().split(' ')
        self.work = [ ]

    '''return hours spent on this task'''
    def hourson():
        print('return hours spend on this task')

