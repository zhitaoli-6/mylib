#encoding=utf-8
import sys
from const import KEY, KEYFORM, LOCAL_PATH as path

reload(sys)
sys.setdefaultencoding('utf-8')

def run():
    with open(path, 'r') as f:
        for line in f:
            cells = line.strip().split(']')
            print cells[0][1:],
            cmd = raw_input().strip()
            print cells[1]
            if(cmd == 'q'):
                break
            

if __name__ == '__main__':
    run()

