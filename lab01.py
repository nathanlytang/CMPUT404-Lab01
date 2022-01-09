import requests

# virtualenv Pt4. Print requests package version
print(requests.__version__)

# curl Pt5. Get the Google homepage
req = requests.get('https://www.google.com')
print(req.status_code)

# curl Pt10. Modify your Python script so that it downloads itself from GitHub and prints out its own source code from GitHub
req = requests.get('https://raw.githubusercontent.com/nathanlytang/CMPUT404-Lab01/master/lab01.py')
print(req.text)
