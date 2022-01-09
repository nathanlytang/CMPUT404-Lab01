import requests

# Print requests package version
print(requests.__version__)

# Get the Google homepage
req = requests.get('https://www.google.com')
print(req.status_code)