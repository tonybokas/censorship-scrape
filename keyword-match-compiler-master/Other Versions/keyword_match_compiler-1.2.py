'''
Simple Keyword Scraper
Version: 1.3
Created by Antonios J. Bokas on September 20, 2021
Based on a script by Zilhaz Jajal from https://zilhaz.com/python-script-for-web-scraping/
'''

''' IMPORT STANDARD LIBRARIES '''

import csv, re, requests, time, urllib
from urllib import request

''' IMPORT 3RD PARTY LIBRARIES '''

from bs4 import BeautifulSoup
from pathlib import Path

''' DEFINE PSEUDO CONSTANTS ''' # None

''' LOCAL FUNCTIONS ''' # None

''' LOCAL CLASSES ''' # None

''' MAIN ENTRY POINT '''

print('Simple Keyword Scraper 1.3', '\nAntonios J. Bokas') # prints the name and author of the script.

print('\nThis script will extract all content from a website that contains a specific primary_keyword.') # describes the script to the user.

# The following prompts the user for a web address:

while True:

	while True:
		new_url = (input('\nStep 1. Enter a URL path: '))
	
		try:
			website = urllib.request.Request(new_url)
			content = urllib.request.urlopen(website)

			break
			
		except Exception:
			
			print('\nInvalid URL. Please try again.')
		
	print('\nURL verified.')
	
	time.sleep(0.5)
	
	# The following prompts the user for new file name for later use:
	
	new_file_name = (input('\nStep 2. Enter a new file name: '))
	time.sleep(0.5)
	
	primary_keyword = input('\nStep 3. Enter a primary keyword: ')
	alt_primary = primary_keyword.lower()
	
	# The following scrapes the web page for HTML content:
	
	parsed_website = BeautifulSoup(content.text, 'html.parser') # initiates the parse.
	headline_return_1 = parsed_website.find_all(string=re.compile(primary_keyword)) # scrapes headlines.
	#headline_return_2 = parsed_website.find_all(string=re.compile(alt_primary)) # scrapes headlines.
	#headline_returns = headline_return_1 + headline_return_2
	
	# The following writes the scraped content to a CSV file:
	
	new_csv_file = Path(str(new_file_name) + str('.csv'))
	new_file_location = Path(str(Path.home()), 'Desktop', str(new_csv_file))
	
	try:
	
		open(new_file_location, 'w')
		
		with open(new_file_location, 'a') as csv_file:
			file_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
			file_writer.writerow(['Keyword Hits'])
			
			for column_1 in headline_return_1:
				file_writer.writerow([column_1.get_text().strip()])
	
	except Exception as err:
		
		print('\nError:', str(err))	
	
	time.sleep(0.5)
	
	# The following notifies the user of the new file name and location.
	
	print('\nStep 5. Scrape complete.')
	
	print('\nNumber of primary_keyword hits: ', len(headline_returns))
	
	print('Content exported to file: ', str(new_csv_file))
	
	print('File location: ', str(Path(new_file_location.anchor, new_file_location.parent)))
	
	continue_or_quit = input('\nEnter (Y) to scrape another website or press Enter to quit. ')
	
	if continue_or_quit == 'Y':
		
		continue
	
	else:
		
		break