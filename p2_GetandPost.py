import requests
r = requests.get('https://api.github.com/events')
r.status_code
r.headers['content-type']
# r.text
r.encoding
# r.json()

import requests
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r.json()

