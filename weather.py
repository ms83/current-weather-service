# -*- coding: utf-8 -*-
"""
Command line program that requests WEB_SERVICE_URL for current weather.
"""

import json
import urllib
import urllib2
import argparse
import logging

WEB_SERVICE_URL = 'http://0.0.0.0:8080/api/v1/city/{}'

logger = logging.getLogger('weather')
#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

parser = argparse.ArgumentParser()
parser.add_argument("--city", help="display a weather for given city")
args = parser.parse_args()

if args.city:
    url = WEB_SERVICE_URL.format(urllib.quote(args.city))
    logger.debug("Fetching {}".format(url))
    response = urllib2.urlopen(url).read()
    logger.debug("Received `{}`".format(response))
    logger.debug("Loading received data into json")
    weather = json.loads(response)
    logger.debug("Parsing temperature")

    try:
        temp_kelvin = weather['main']['temp']
        temp_celcius = int(temp_kelvin)-272.15
    except ValueError, e:
        logger.error("Error parsing temperature: {}".format(e))
    else:
        print "Current weather in '{}':".format(args.city)
        print '\tTemperature: {} °C'.format(temp_celcius)

