import time
import psutil as psutil
from time import mktime
from datetime import datetime


def program_run_length(program):
    for process in psutil.process_iter():
        if process.name() == program:
            start_time = datetime.fromtimestamp(mktime(time.localtime(process.create_time())))
            run_length = (datetime.now() - start_time)
            minutes = int(run_length.seconds / 60)
            if minutes > 60:
                hours = int(minutes / 60)
            else:
                hours = 0
            if program == 'Microsoft Word':
                print(f'You have been writing for {minutes} minutes')
            else:
                print(f'{program} has been running for {hours} hours, {minutes} minutes')
            return run_length

