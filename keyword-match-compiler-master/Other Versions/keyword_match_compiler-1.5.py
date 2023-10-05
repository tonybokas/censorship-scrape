'''
Key Word and Phrase Counter
Version: 1.5
Created by Antonios J. Bokas on September 29, 2021
Special thanks to Zilhaz Jajal at https://zilhaz.com/python-script-for-web-scraping/
'''

''' IMPORT STANDARD LIBRARIES '''

import csv, os, re, time
from pathlib import Path

''' IMPORT 3RD PARTY LIBRARIES '''

from bs4 import BeautifulSoup

''' MAIN ENTRY POINT '''

print('Key Word and Phrase Counter', '\nAntonios J. Bokas') # prints the name and author of the script.

print('\nThis script parses all HTML files in a given directory for content that contains a primary keyword.' \
	  '\nIf the content with the primary keyword also contains a modifying keyword, it is added to a list.' \
	  '\nThe script then writes the list to a TXT file for further use.') # describes the script to the user.

# The following asks the user to input search criteria:

print('\nStep 1. User Inputs')

directory = input('\nEnter a directory that contains HTML files: ')
primary_keyword = input('Enter a primary keyword: ')
'''
modifying_keyword = input('Enter a modifying keyword: ')

alt_primary = primary_keyword.lower()
alt_modifying = modifying_keyword.lower()
'''
time.sleep(0.5)

# The following scrapes the web page for HTML content:

print('\nStep 2. Parse HTML Files')

html_file_list = []
keyword_matches = []
parse_count = 0

try:
	
	for file_name in os.listdir(directory):
	
		if file_name.endswith('.html'):
		
			archived_page = open(str(Path(directory, file_name)), encoding='utf-8')
			archived_page_html = BeautifulSoup(archived_page, 'html.parser') # main archive page of website.
			headline_return_1 = archived_page_html.find_all(text=re.compile(primary_keyword)) # scrapes headlines.
			keyword_matches.append(headline_return_1)
			print(headline_return_1)
			parse_count = parse_count + 1
		
		else:
	
			continue		

except Exception as error:
	
	print('\nParsing error: ', str(error))

print('\nScrape complete.')

time.sleep(0.5)

# The following displays preliminary scrape results:

print('\nStep 3. Results')

print('\nNumber of HTML files parsed: ', parse_count)
print('Number of full keyword matches: ', len(keyword_matches))

time.sleep(0.5)	

# The following writes the scraped content to a CSV file:

if parse_count >= 1:

	print('\nStep 4. Create a Data Table')
	
	file_name = input('\nEnter a new file name: ')
	
	txt_file = Path(str(file_name) + str('.txt'))
	txt_file_path = Path(directory, str(txt_file))
	
	with open(txt_file_path, 'w') as notes:
		
		for entry in keyword_matches:
			
			notes.write('test')
			
		
	# The following notifies the user of the new html_file name and location.
		
	print('\nContent exported to TXT file: ', str(txt_file))
	print('File location: ', str(Path(txt_file_path.anchor, txt_file_path.parent)))
	
	quit_script = input('\nEnd of script. Press Enter to quit.')
	
else:
	
	quit_script = input('\nEnd of script. Press Enter to quit.')