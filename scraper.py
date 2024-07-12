import re
from urllib.request import urlopen
from package.data import url, element, split_list
from package.functions import cleaner


# detects the web encoding used, then reads and converts the webpage into bytes and decodes
page = urlopen(url)
encoding = page.headers.get_content_charset() 
html_bytes = page.read()
html = html_bytes.decode(encoding)

# finding the elements that starts from the specified element from the decoded html then filter objects into a str to be used as list
index = html.find(element[0]) 
start_index = index + len(element[0]) 
end_index = html.find(element[1]) 
title = str(html[start_index:end_index])

output_list = str(re.findall('<div class="BNeawe s3v9rd AP7Wnd">.*</div>', title))

# cleans the output
end_result = cleaner(output_list,split_list)
