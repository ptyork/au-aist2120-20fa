# pip install requests
# (or pip3 install requests)

import requests


# Generic way of saving a web file
def save(filename, rsp):
    with open(filename, 'wb') as file:
        for bytes in rsp.iter_content(10000):
            file.write(bytes)


resp = requests.get('https://en.wikipedia.org/wiki/Main_Page')
# print(resp.status_code) # 200 == GOOD
resp.raise_for_status()   # raise an exception IF I don't get my page

# print('GOOD')

# NOTE: Commenting this out in the "FIXED" version because it's annoying...
# print(resp.text)

# resp = requests.get('https://en.wikipedia.org/wiki/Main_Page#/media/File:European_Storm_Petrel_From_The_Crossley_ID_Guide_Eastern_Birds.jpg')
# NOTE: So this code wasn't broken. APPARENTLY wikipedia creates a "fake" JPG
#       URL when you click on the image itself. So my original URL wasn't
#       really downloading the JPG. Instead it was downloading the original 
#       HTML page. THIS is the actual URL of the image itself. GRRRRRRR.
resp = requests.get('https://upload.wikimedia.org/wikipedia/commons/c/c1/European_Storm_Petrel_From_The_Crossley_ID_Guide_Eastern_Birds.jpg')
resp.raise_for_status()

# print(resp.text)   NO IT'S BINARY
save('petrel.jpg', resp)
