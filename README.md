# Weather-Scrapping
Welcome to our web scraping project! In this project, we will be using Python to extract data from from the websites using api calls.

## API KEY
To use the OpenWeather API, you will need to sign up for a free API key at https://home.openweathermap.org/users/sign_up. Once you have your API key, you can use it to make requests to the OpenWeather API.

Here is an example of how to use your API key to make a request to the OpenWeather API using Python:
```
import requests

# Replace YOUR_API_KEY with your actual API key
api_key = "YOUR_API_KEY"

# Make a request to the OpenWeather API for the weather in London
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London&appid=" + api_key)

# Print the response from the API
print(response.text)
```
You can also use your API key to make requests to other endpoints of the OpenWeather API, such as the forecast endpoint or the historical data endpoint. You can find more information about the different endpoints and how to use them in the OpenWeather API documentation at https://openweathermap.org/api.

## Prerequisites
Before you begin, you will need to have the following software installed on your machine:

- Python 3
- pip (Python package manager)  

You will also need to install the following Python packages:

- requests  

This library allows you to give HTTP request to request data from the server.
To install these packages, open a terminal window and enter the following command:  
```
pip install requests
```

## Tips

- Some websites may block web scrapers. You can use the User-Agent header to identify yourself as a web browser, rather than a scraper. For example:  

 ```
 headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
 html = requests.get(url, headers=headers).text
 ```
- Be respectful of the website that you are scraping. Do not send too many requests in a short period of time as your ip address may get banned from that website.

