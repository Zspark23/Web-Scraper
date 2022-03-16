import requests
from bs4 import BeautifulSoup
from datetime import datetime

def getSunsetTime(soup):
    sunInfo = soup.find(class_="tide-header-summary")
    sunInfo = sunInfo.text.split("sunset")[1].strip()
    return datetime.strptime(sunInfo, "is at  %I:%M%p.").time()

def getSunriseTime(soup):
    sunInfo = soup.find(class_="tide-header-summary")
    sunInfo = sunInfo.text.split("Sunrise")[1].split("and")[0].strip()
    return datetime.strptime(sunInfo, "is at  %I:%M%p").time()

def halfMoonBayTideInfo():
    URL = "https://www.tide-forecast.com/locations/Half-Moon-Bay-California/tides/latest"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    sunset = getSunsetTime(soup)
    sunrise = getSunriseTime(soup)
    tide_table = soup.find(class_="tide-day-tides")

    print("Half Moon Bay Low Tide Information: ")
    for x in tide_table.find_all("tr"):
        for y in x.find_all("td"):
            if ":" in y.text:
                try:
                    tideTime = datetime.strptime(y.text.strip(), "%I:%M %p(%a %d %B)").time()
                except ValueError:
                    tideTime = datetime.strptime(y.text.strip(), "%H:%M %p(%a %d %B)").time()
                if tideTime > sunrise and tideTime < sunset and "Low Tide" in x.text:
                    print(x.text)
    print("\n")

def huntingtonBeachTideInfo():
    URL = "https://www.tide-forecast.com/locations/Huntington-Beach/tides/latest"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    sunset = getSunsetTime(soup)
    sunrise = getSunriseTime(soup)
    tide_table = soup.find(class_="tide-day-tides")

    print("Huntington Beach Low Tide Information: ")
    for x in tide_table.find_all("tr"):
        for y in x.find_all("td"):
            if ":" in y.text:
                try:
                    tideTime = datetime.strptime(y.text.strip(), "%I:%M %p(%a %d %B)").time()
                except ValueError:
                    tideTime = datetime.strptime(y.text.strip(), "%H:%M %p(%a %d %B)").time()
                if tideTime > sunrise and tideTime < sunset and "Low Tide" in x.text:
                    print(x.text)
    print("\n")

def providenceTideInfo():
    URL = "https://www.tide-forecast.com/locations/Providence-Rhode-Island/tides/latest"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    sunset = getSunsetTime(soup)
    sunrise = getSunriseTime(soup)
    tide_table = soup.find(class_="tide-day-tides")

    print("Providence Low Tide Information: ")
    for x in tide_table.find_all("tr"):
        for y in x.find_all("td"):
            if ":" in y.text:
                try:
                    tideTime = datetime.strptime(y.text.strip(), "%I:%M %p(%a %d %B)").time()
                except ValueError:
                    tideTime = datetime.strptime(y.text.strip(), "%H:%M %p(%a %d %B)").time()
                if tideTime > sunrise and tideTime < sunset and "Low Tide" in x.text:
                    print(x.text)
    print("\n")


def wrightsvilleBeachTideInfo():
    URL = "https://www.tide-forecast.com/locations/Wrightsville-Beach-North-Carolina/tides/latest"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    sunset = getSunsetTime(soup)
    sunrise = getSunriseTime(soup)
    tide_table = soup.find(class_="tide-day-tides")

    print("Wrightsville Beach Low Tide Information: ")
    for x in tide_table.find_all("tr"):
        for y in x.find_all("td"):
            if ":" in y.text:
                try:
                    tideTime = datetime.strptime(y.text.strip(), "%I:%M %p(%a %d %B)").time()
                except ValueError:
                    tideTime = datetime.strptime(y.text.strip(), "%H:%M %p(%a %d %B)").time()
                if tideTime > sunrise and tideTime < sunset and "Low Tide" in x.text:
                    print(x.text)
    print("\n")


def main():
    halfMoonBayTideInfo()
    huntingtonBeachTideInfo()
    providenceTideInfo()
    wrightsvilleBeachTideInfo()

main()
