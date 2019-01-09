# FoodScraps

FoodScraps is a webscraping tool designed at the CanDEV Data Challenge (2018) for the Canadian Food Inspection Agency (CFIA). Foodscraps is a solution for the CFIA to explore publicly accessible data about agriculture and agri-food businesses within Canada or exporting to Canada. The scraped data is used to develop a scoring system to know which companies to flag for inspection for a potential uncompliance of CFIA regulations. The developed strategy uses **Python (Selenium Webdriver)** for webscraping the data and coming up with a score for each company. The scores are then displayed on an interactive webpage using the **Google Maps API** and **Firebase Realtime Database**.

## Table Of Contents


- [Getting Started](#getting-started)
  * [Webscraping Instructions](#webscraping-instructions)

## Getting Started 

clone the repository

```
git clone https://github.com/EricHaggar/FoodScraps.git
```

change to the project directory

```
cd FoodScraps
```

### Webscraping Instructions

Navigate to the scripts directory

```
cd scripts
```

If Python is not installed on your machine, install it before proceeding

```
https://www.python.org/downloads/
```

If it is installed, ensure the Python version being used is 3.7.0 or higher

```
python --version
```
Then install all dependencies for webscraping and Firebase using pip

```
pip install selenium
```
```
pip install chromedriver
```
```
pip install google
```
```
pip install pyrebase
```

Create a free Firebase account and create a realtime database

```
https://firebase.google.com/
```

Navigate to `master.py` and replace with your Firebase database information

```
config = {

    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": ""
}
```

The scripts are ready to be run in the background!

```
python master.py
```

  > _More to be added..._




