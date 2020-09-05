import json
import os
from urllib.parse import quote

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

# Azure Maps API Key
API_KEY = os.getenv("API_KEY")


def get_coords(placename: str):
    """Takes a place name and queries the Azure Maps database for the
    latitude and longitude coordinates.

    Args:
        placename (str): Location name. Ideally "City, State, Country"
        or similar.

    Returns:
        str: As formatted below, latitude and longitude.
    """
    QUERY = quote(placename)
    URL = f"https://atlas.microsoft.com/search/address/json?subscription-key={API_KEY}&api-version=1.0&query={QUERY}&limit=1"
    r = json.loads(requests.get(URL).text)
    lat = r["results"][0]["position"]["lat"]
    lon = r["results"][0]["position"]["lon"]
    return f"Latitude: {lat} Longitude:{lon}"


def get_bulk_coords(csv: str):
    """Assuming that the input is a .csv file formatted in a way that
    there are three or four geographic subdivisions organized from a
    greater to a smaller, A > B > C > D, this function takes a .csv
    file and returns latitude and longitude for each location/line,
    saved in the same .csv file in additional columns.

    It is important to note here that, since this function uses Azure
    Maps API to do so, the pricing tier will determine the number of
    queries that can be performed.

    Standard Tier 0 accts cannot make more than 50 queries per minute

    Args:
        csv (str): .csv filename

    Returns:
        [type]: [description]
    """
    file = pd.read_csv(csv)
    # clean file
    # for each line:
    # QUERY = quote(line)
    # URL = f"https://atlas.microsoft.com/search/address/json?subscription-key={API_KEY}&api-version=1.0&query={QUERY}&limit=1"
    # run block below,
    # add column lat
    # add column lon
    # return exported .csv file
