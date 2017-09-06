#encoding=utf-8
import os, sys, json, logging, time
import urllib2
from const import KEY, KEYFORM, LOCAL_PATH as path


reload(sys)
sys.setdefaultencoding('utf-8')

def save(s):
    with open(path, 'a') as f:
        f.write(s)
    


def run():
    stop_cmd = set(['q', 'exit'])
    while True:
        #word = sys.argv[1]
        print '-----------'
        word = raw_input().strip()
        if(not word):
            continue
        if word in stop_cmd:
            return
        #print 'query: %s' % word
        query = 'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=%s&version=1.1&q=%s' % (KEYFORM, KEY, 'json', word)
        res = urllib2.urlopen(query).read()
        
        if res:
            res = json.loads(res)
            if 'basic' not in res:
                print 'not found'
                continue
            if 'basic' in res and 'phonetic' in res['basic']:
                print 'phoetic: %s' % res['basic']['phonetic']
            if 'explains' not in res['basic']:
                continue
            print 'explanation:'
            for item in res['basic']['explains']:
                print item
            try:
                cache_str = '[%s] %s [%s]\n' % (word, res['basic']['phonetic'], ' '.join(res['basic']['explains']))
                save(cache_str)
            except Exception:
                pass
            


if __name__ == '__main__':
    run()
