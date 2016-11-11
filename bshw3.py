# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import re
import requests
from bs4 import BeautifulSoup

print ("Name: Madison Huffman")
print ("UM ID: 34109303")
print("\n")

# Making request with Beautiful Soup
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
umsi_soup = BeautifulSoup(r.text, "html.parser")



# Open new html document
f = open('bshw3.html','w')
html_txt = umsi_soup.prettify()

# Replace all instances of students with AMAZING student
amazing_txt = html_txt.replace("student", "AMAZING student")
capital_txt = amazing_txt.replace("Student", "AMAZING Student")

# Add the logos back
add_logos = capital_txt.replace("logo2.png", "https://github.com/cvanlent/SI206/blob/master/HW3-StudentCopy/media/logo.png?raw=true")

# Add my picture (for your comedic relief... lol)
add_mypic = add_logos.replace("https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg", "https://www.dropbox.com/s/o9a2xhjpav1h3tq/IMG_7088.jpg?dl=1")

# Close file
f.write(add_mypic)
f.close()

print ("Done!")


