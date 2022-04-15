"""
If we want to scrape a Website:
1.Use the API
2.HTML Scraping using some tool like bs4

Install the Requirements
1.pip install requests
2.pip install bs4
3.pip install html5lib
"""
import requests
from bs4 import BeautifulSoup

# url = "https://codewithharry.com"
url = "https://timesofindia.indiatimes.com/"

# Step1 Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

# Step2 Parse the HTML
soup = BeautifulSoup(htmlContent,"html.parser")
#print(soup.prettify())

# Step3 HTML Tree Traversal
# Commonly used types of objects:
# 1.Tag
# 2. Navigable String
# 3. BeautifulSoup
# 4.Comment

title = soup.title  # Getting the title of the page
# print(type(soup))  # BeautifulSoap
# print(title)  # Tag
# print(title.string)  # It will give the string, # Navigable String

# Taking all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)


# To Get only 1st element

#print(soup.find('p'))
#print(soup.find('p')['class'])

# to find all the element with class lead
# print(soup.find_all('p',class_="lead"))

# Get the Text from the element/tags

#print(soup.find('p').get_text())
#print(soup.get_text())


# Taking all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# print(anchors)
# Get all links in anchors

# for link in anchors:
#     if(link != '#'):
#      link = "https://codewithharry.com"+link.get('href')
#      all_links.add(link)
#      print(all_links)

# 4. Comment
# markup = "<p> <!-----This is comment ---> </p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p.string)

# Contents

# .contents - in this a tag's children are available as a list
# .children - In this tag's children are available in generator , it is faster than contents

navbarSupportContent = soup.find(id="app")
#print(navbarSupportContent)


# for item in navbarSupportContent.strings:
#    print(item)

# For parent
#print(navbarSupportContent.parent)

# for item in navbarSupportContent.parents:
   # print(item.name)

"""
Next Sibling : it will give the nxt tag from the specified tag
Previous Sibling : it will give you previous tag from the specified tag

"""

# print(navbarSupportContent.nextSibling.nextSibling)
# print(navbarSupportContent.previousSibling)

# soup.select('#CSS Selector')

