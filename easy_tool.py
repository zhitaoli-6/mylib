#encoding=utf-8
import time

class EasyTool(object):
    '''
    EasyTool provides some class methods that are often used when coding
    '''
    @staticmethod
    def write_file(path, mode, text):
        with open(path, mode) as f:
            f.write(text)


    @staticmethod
    def format_time(st_time, f = '%Y-%m-%d %H:%M:%S'):
        return time.strftime(f, st_time)
