# Cinderella-Crawler
Information
===========
This script crawls http://cinderella.pro for card information from a user and neatly parses and prints said information. It will fetch high-tiered cards from your account and display the top ~48 cards if possible. Output includes card name, card type, skill, and highest attribute.

Requirements
============
Python 3.X (3.6 Recommended) | [Download Here](https://www.python.org/downloads/)<br>
GeckoDriver.exe (Firefox's webdriver, included in the repository for you) | [Latest Here](https://github.com/mozilla/geckodriver/releases)<br>
Selenium Module for Python 3.X (```pip install selenium```) | [More Information Here](http://selenium-python.readthedocs.io/installation.html)<br>

How to Use
==========
1. Download or Clone the Git Repository and Install all necessary requirements
2. Replace the ```'PUT YOUR PROFILE URL HERE'``` in the script with your http://cinderella.pro profile URL
3. Run the script using ```python cinderella.py```
4. Let the script run and the output will be placed into a file called ```cinderella.txt```
5. That's it!

Example Output
==============
```
SSR Morikubo Nono "Forest Story" | Cool | For every 9 seconds, there is a 35% chance that Great and Perfect notes will receive a 17% score bonus in the next 5 seconds. | Highest: Vocal (4935)<br>
SSR Honda Mio "Wonder Entertainer" | Passion | For every 9 seconds, there is a 35% chance that you will gain an extra 18% combo bonus in the next 5 seconds. | Highest: Dance (5830)
SSR Yorita Yoshino "Watasumi's Guidance" | Passion | For every 9 seconds, there is a 35% chance that Great and Perfect notes will receive a 17% score bonus in the next 5 seconds. | Highest: Visual (5552)
```

Disclaimer
==========
If the website changes, this script will most likely break. I might try to keep it updated, but due to it's infrequent use it is highly unlikely. Please do not have multiple scripts running at once, as this script is very request heavy and may have you blocked or banned from http://cinderella.pro if they feel as if you are malicious traffic.
