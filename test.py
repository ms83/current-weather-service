import json
import urllib2
import unittest

WEB_SERVICE_URL = 'http://0.0.0.0:8080/api/v1/city/{}'

class TestStringMethods(unittest.TestCase):
    def test_json_corrent(self):
        response = urllib2.urlopen(WEB_SERVICE_URL.format('Palma')).read()
        weather = json.loads(response)

        for att in ('coord', 'weather', 'base', 'main', 'visibility', 'wind', 
                    'clouds', 'dt', 'sys', 'id', 'name', 'cod'):
            self.assertTrue(att in weather)

        for att in ('temp', 'pressure', 'humidity', 'temp_min', 'temp_max'):
            self.assertTrue(att in weather['main'])

        self.assertTrue(weather['name'] == 'Palma')
        self.assertTrue(weather['sys']['country'] == 'ES')

    def test_name_with_spaces(self):
        response = urllib2.urlopen(WEB_SERVICE_URL.format('Palma%20de%20Mallorca')).read()
        weather = json.loads(response)
        self.assertTrue(weather['name'] == 'Palma de Mallorca')


if __name__ == '__main__':
    unittest.main()
