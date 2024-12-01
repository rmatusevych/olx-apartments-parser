# Olx Apartments parser

## Main Idea

Simple project to parse data from OLX website and get top 10 newest apartments in Lviv based on criteria that you specify and then return URLs to these apartments as a JSON console output.

Run this command to install the dependencies: poetry install

Activate the virtual environment: poetry shell

Install playwright in the virtual environment: playwright install

To start the project, just run the command: python3 main.py --from_price 10000 --to_price 15000
