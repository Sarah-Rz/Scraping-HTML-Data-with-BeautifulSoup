# This is a Python program, using urllib to read the HTML from the data files below (http://py4e-data.dr-chuck.net/comments_1862740.html),
# and parse the data, extracting numbers and compute the sum of the numbers in the file.


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
tags = soup('span')
for tag in tags:
    num = tag.contents[0]
    count = float(num) + count
print(count)
