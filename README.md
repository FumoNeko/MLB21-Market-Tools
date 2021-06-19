# MLB21-Market-Tools
There are 2 main Tools in this package. Both of them use python, you can install python here: https://www.python.org/downloads/
You CANNOT use this tool without installing Python.
# Autobuyer
mlbautobuyer.py uses the Selenium Library, goes to the mlb market website and repeatedly enters buy orders to easily scalp cards of players quickselling.
## Autobuyer Windows Installation:
1. Open CMD and type <kbd>py -m pip install selenium</kbd>
2. You can now run the tool. Double click mlbautobuyer.py or <kbd>cd</kbd> to the path in cmd, then run it with <kbd>py mlbautobuyer.py</kbd>
## Usage:
1. Go to the MLB page of the card you want to buy repeatedly and Copy the URL. An example would be https://mlb21.theshow.com/items/f719b9d74bf9856c0206738aadd1d21a
2. Run the tool, then answer the prompted questions. The tool will then run automatically. Solve a captcha if asked to and the tool will continue to work.
# Sniper
Sniper is a tool designed to give you information about price fluctuation of cards by querying MLB's JSON API. Sniper is currently not finished, but is in a state to query the API.
