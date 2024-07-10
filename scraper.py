import urllib
import re
from urllib.request import urlopen

# Following FIFO

url = 'https://www.google.com/search?q=top+search+keywords'
page = urlopen(url) # opens the url

# detects the web encoding used
encoding = page.headers.get_content_charset() 

# reads and converts the webpage into bytes and decodes
html_bytes = page.read() 
html = html_bytes.decode(encoding)

# finding the elements that starts from the <table> container
c = '<table>'
c2 = '</table>' 

# finds the element index and output to a list
index = html.find(c) 
start_index = index + len(c) 
end_index = html.find(c2) 
title = html[start_index:end_index] 

title = str(title)

# outputs a list with everything on one index
f = re.findall('<div class="BNeawe s3v9rd AP7Wnd">.*</div>', title)

f = str(f)

# splitting objects and sorting into a list
split_list = ['<div class="BNeawe s3v9rd AP7Wnd">','</div>','<div class="BNeawe s3v9rd AP7Wnd">']

n = []

for i in split_list:
    n = f.split(i)

for i in n:
    if i == '':
        n.remove(i)

value = []

for i in n:
    if ' ' in i or ',' in i:
        i = i.split('</div>')
        i.pop(1)
        i.pop(1)
        value += i

print (value)
