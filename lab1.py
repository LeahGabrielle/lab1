import requests

#print requests.__version__

response = requests.get('https://github.com/LeahGabrielle/lab1/raw/master/lab1.py')
print (response.text)
