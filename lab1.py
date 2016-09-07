import requests

#print requests.__version__

response = requests.post('http://ccid-eddieantonio.rhcloud.com/olexson')
print response.status_code