# pip install requests
# (or pip3 install requests)

import requests


# Generic way of saving a web file
def save(filename, rsp):
    with open(filename, 'wb') as file:
        for bytes in rsp.iter_content(10000):
            file.write(bytes)



resp = requests.get('https://en.wikipedia.org/wiki/Main_Page')
# print(resp.status_code)
resp.raise_for_status()   # raise an exception IF I don't get my page

# print('GOOD')

print(resp.text)

resp = requests.get('https://en.wikipedia.org/wiki/Main_Page#/media/File:European_Storm_Petrel_From_The_Crossley_ID_Guide_Eastern_Birds.jpg')
resp.raise_for_status()

# print(resp.text)   NO IT'S BINARY
save('petrel.jpg', resp)
