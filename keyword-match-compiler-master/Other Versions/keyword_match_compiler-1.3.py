'''
Double Keyword Match Scraper
Version: 1.4
Created by Antonios J. Bokas on September 20, 2021
Based on a script by Zilhaz Jajal from https://zilhaz.com/python-script-for-web-scraping/
'''

''' IMPORT STANDARD LIBRARIES '''

import csv, re, requests, time
from datetime import date

''' IMPORT 3RD PARTY LIBRARIES '''

from bs4 import BeautifulSoup
from pathlib import Path

''' DEFINE PSEUDO CONSTANTS ''' # None

''' LOCAL FUNCTIONS ''' # None

''' LOCAL CLASSES ''' # None

''' MAIN ENTRY POINT '''

print('Double Keyword Match Scraper 1.4', '\nAntonios J. Bokas') # prints the name and author of the script.
print('\nThis script extracts all content from a specified website archived in the Wayback Machine' \
	  '\nat http://web.archive.org/. First, it extracts content that contains a primary keyword,'
	  '\nthen it filters that content using to a modifying keyword.') # describes the script to the user.

# The following prompts the user for a web address:

while True:

	while True:
		
		new_url = (input('\nStep 1. Enter a URL path (e.g., https://yahoo.com): '))
		print('Checking if ' + new_url + ' is in the Wayback Machine...')

		try:
			
			website_archive = requests.get('web.archive.org/web/*/' + new_url)
			website_archive.raise_for_status()
			break
			
		except Exception:
			print('Invalid URL. Please try again.')
		
	print('URL verified.')
	time.sleep(0.5)
	
	print('\nStep 2. Search Criteria')
	
	'''
	start_year = input('\nEnter a year to search in YYYY format: ')
	'''
	
	search_month = input('\nEnter a month to search in MM format: ')
	month_dict = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', \
				  '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}	
	archive_month = month_dict.get(search_month, 0)
	time.sleep(0.5)

	print('\nStep 3. Keywords')

	primary_keyword = input('\nWhat is the primary keyword?: ')
	modifying_keyword = input('What is the modifying keyword?: ')
	alt_primary = primary_keyword.lower()
	alt_modifying = modifying_keyword.lower()

	# The following scrapes the web page for HTML content:
	
	main_website_archive = BeautifulSoup(website_archive.text, 'html.parser') # main archive page of website.
	archive_month_captures = []
	headline_matches = []
	
	for parent_tag in main_website_archive.find("div", str(archive_month)):
		
		for each_link in parent_tag.findAll('a'):
			
			archive_month_captures.append(link.get('href'))		
	
	for each_url in archive_month_captures:
		
		requests.get(each_url)
		each_url.raise_for_status()
		parsed_page = BeautifulSoup(each_url.text, 'html.parser') # initiates the parse.
		headline_return_1 = parsed_page.findAll(string=re.compile(primary_keyword)) # scrapes headlines.
		headline_return_2 = parsed_page.findAll(string=re.compile(alt_primary)) # scrapes headlines.
		headline_returns = headline_return_1 + headline_return_2
		double_keyword_match = [x for x in headline_returns if modifying_keyword in x]
		double_keyword_matches.append(double_keyword_match)
	
	time.sleep(0.5)	

	# The following prompts the user for new file name for later use:
	
	new_file_name = input('\nStep 4. Enter a new file name: ')
	
	# The following writes the scraped content to a CSV file:
	
	new_csv_file = Path(str(new_file_name) + str('-') + str(archive_month) + str('.csv'))
	new_file_location = Path(str(Path.home()), 'Desktop', str(new_csv_file))
	
	try:
		
		open(new_file_location, 'w')
		
		with open(new_file_location, 'a') as csv_file:
			
			file_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
			file_writer.writerow(['Keyword Hits'])
			
			for column_1 in headline_matches:

				file_writer.writerow([column_1.get_text().strip()])
	
	except Exception as err:
		
		print('\nError:', str(err))	
	
	time.sleep(0.5)
	
	# The following notifies the user of the new file name and location.
	
	print('\nStep 5. Results')
	
	print('\nNumber of double keyword matches: ', len(double_keyword_matches))
	print('Content exported to file: ', str(new_csv_file))
	print('File location: ', str(Path(new_file_location.anchor, new_file_location.parent)))
	continue_or_quit = input('\nEnter (Y) to scrape another website or press Enter to quit. ')
	
	if continue_or_quit == 'Y':
		
		continue
	
	else:
		
		break