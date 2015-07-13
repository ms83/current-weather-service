"""
Web service that serves current weather in JSON format.
- uses http://openweathermap.org/wiki/API/2.1/JSON_API
- cache request and responses for configured timeout

Example:
curl http://0.0.0.0:8080/api/v1/city/Palma

TODO:
    Currently webserver is just a proxy of openweathermap API and response 
    schema should be designed in case we will have to change API/provider.
"""

import web
import time
import urllib
import urllib2

API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}'
CACHE_TIMEOUT_SEC = 5*60
        
urls = (
    '/api/v1/city/(.*)', 'city'
)
app = web.application(urls, globals())

class city:        
    CACHE = {}
    def GET(self, name):
        now = time.time()
        # Cache responses to not flood API end point.
        # CACHE['Palma'] = (response, timestamp)
        if name in self.CACHE:
            cached_response, ts = self.CACHE[name]
            if now - ts < CACHE_TIMEOUT_SEC:
                return cached_response
             
        response = urllib2.urlopen(API_URL.format(urllib.quote(name))).read()
        self.CACHE[name] = (response, now)
        # Forward response as it is.
        # FIXME (look at pydoc on top of file)
        return response

if __name__ == "__main__":
    app.run()
