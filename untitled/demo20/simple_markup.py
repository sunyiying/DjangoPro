import sys,re;
#from util import *;
from util import *;
#import util.*;


print('<html><head><title>...</title><body>');
title=True;
#f=open("D:\\RDCenter\\WorkBench\\untitled\\demo20\\test_input.txt");
for block in blocks(sys.stdin):
    block=re.sub(r'\*(.+?)\*',r',<em>\1</em>',block);
    if title:
        print('<h1>');
        print(block);
        print('</h1>');
        title=False;
    else:
        print('<p>');
        print(block);
        print('</p>');
    print('</body></html>');