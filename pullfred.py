#!/usr/bin/python3
################################################################################
## Script: pullfred.py
## Author: Joe Saia
## Notes: Pulls a series from FRED and saves it
## Input: Takes name of series to pull from FRED
################################################################################
import sys
def download_fred(series, api_key, = file_type='xml', obs_start='', obs_end='', units='', freq='', agg_method='', noisey=True):
# Pulls a series from Fred and save it
# Required inputs
# series: Series name
# api_key: API key to access FRED. See FRED website to get one for easy and free
# optional outputs
# noisey: If True then print all characteristics of series request. Default = True
# See https://research.stlouisfed.org/docs/api/fred/series_observations.html#Parameters for other parameters
    import urllib.request

    base_url = "https://api.stlouisfed.org/fred/series/observations?"

    params = dict([
        ('api_key', api_key),
        ('file_type', file_type),
        ('observation_start', obs_start),
        ('observation_end', obs_start),
        ('units', units),
        ('frequency',freq),
        ('aggregation_method', agg_method)
    ])

    savefile = series + "." + params['file_type']

    print("Downloading Fred Data to " + savefile)
    url = base_url + "series_id=" + series
    for key in params:
        if params[key] != '':
            if noisey:
                print(key + ": " + params[key])
            url = url + "&" + key + "=" + params[key]
    print("The URL is: \n" + url)
    urllib.request.urlretrieve(url,savefile)
################################################################################
## Call script
download_fred(sys.argv[1])
