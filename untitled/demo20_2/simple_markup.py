import sys, re
from demo20_2.util import *

print('<html><head><title>这是第二次测试</title><body>')
title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print("<h1>")
        print(block)
        print("</h1>")
        title = False
    else:
        print("<p>")
        print(block)
        print("</p>")
    print("</body></html>")