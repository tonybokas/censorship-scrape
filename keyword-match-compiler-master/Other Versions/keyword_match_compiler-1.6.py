'''
Key Word and Phrase Counter
Version: 1.5
Created by Antonios J. Bokas on September 29, 2021
Special thanks to Zilhaz Jajal at https://zilhaz.com/python-script-for-web-scraping/
'''

''' IMPORT STANDARD LIBRARIES '''

import csv, datetime, os, re, sys
from pathlib import Path

''' IMPORT 3RD PARTY LIBRARIES '''

from bs4 import BeautifulSoup

''' MAIN ENTRY POINT '''

print('Key Word and Phrase Counter', '\nby Antonios J. Bokas') # prints the name and author of the script.

print('\nDescription: This script parses all HTML files in a given directory for three user-identified key words and phrases. ' \
	  'All results are summarized and then written to a TXT file for further analysis.')

print('\n1. User Inputs')

file_name = input('\nEnter a new file name: ')
txt_file = Path(str(file_name) + str('.txt'))
directory = input('Enter a directory that contains HTML files: ')
txt_file_path = Path(directory, str(txt_file))

print('\n2. Key Words and Phrases')

print('\nKeywords')
keyword_1 = input('Enter a first keyword: ')
keyword_2 = input('Enter a second keyword: ')
keyword_3 = input('Enter a third keyword: ')
print('\nKey Phrases')
key_phrase_1 = input('Enter a first key phrase: ')
key_phrase_2 = input('Enter a second key phrase: ')
key_phrase_3 = input('Enter a third key phrase: ')

# BEGIN PRINT TO TEXT FILE

stdoutOrigin = sys.stdout
sys.stdout = open(txt_file_path, "w")

print('"Key Word and Phrase Counter"')

print('\nPython script by Antonios J. Bokas')

print('\nDescription: This script parses all HTML files in a given directory for three user-identified key words and phrases. ' \
	  'All results are summarized and then written to a TXT file for further analysis.')

time_now = datetime.datetime.now()

print('\nParse executed at', time_now.strftime('%H:%M:%S on %A, %B %d, %Y'))

print('\nSECTION 1. PARSED HTML FILES')

keyword_1_match_list = []
keyword_2_match_list = []
keyword_3_match_list  = []
key_phrase_1_match_list = []
key_phrase_2_match_list = []
key_phrase_3_match_list = [] 
parse_count = 0

try:
	
	for file_name in os.listdir(directory):
	
		if file_name.endswith('.html'):
			
			print('\nHTML File: ', file_name)
		
			archived_page = open(str(Path(directory, file_name)), encoding='utf-8')
			archived_page_html = BeautifulSoup(archived_page, 'html.parser') # main archive page of website.
			
			keyword_1_matches = archived_page_html.find_all(text=re.compile(keyword_1))
			keyword_1_match_list = keyword_1_match_list + keyword_1_matches
			
			print('\nKeyword: ', keyword_1)
			
			for item in keyword_1_match_list:
				
				print(item)
			
			keyword_2_matches = archived_page_html.find_all(text=re.compile(keyword_2))
			keyword_2_match_list = keyword_2_match_list + keyword_2_matches
			
			print('\nKeyword: ', keyword_2)
			
			for item in keyword_2_match_list:
		
				print(item)			
			
			keyword_3_matches = archived_page_html.find_all(text=re.compile(keyword_3))
			keyword_3_match_list = keyword_3_match_list + keyword_3_matches
			
			print('\nKeyword: ', keyword_3)
			
			for item in keyword_3_match_list:
		
				print(item)			
			
			key_phrase_1_matches = archived_page_html.find_all(text=re.compile(key_phrase_1))
			key_phrase_1_match_list = key_phrase_1_match_list + key_phrase_1_matches
			
			print('\nKey Phrase: ', key_phrase_1)
			
			for item in key_phrase_1_match_list:
		
				print(item)			
			
			key_phrase_2_matches = archived_page_html.find_all(text=re.compile(key_phrase_2))
			key_phrase_2_match_list = key_phrase_2_match_list + key_phrase_2_matches
			
			print('\nKey Phrase: ', key_phrase_2)
			
			for item in key_phrase_2_match_list:
		
				print(item)			
			
			key_phrase_3_matches = archived_page_html.find_all(text=re.compile(key_phrase_3))
			key_phrase_3_match_list = key_phrase_3_match_list + key_phrase_3_matches
			
			print('\nKey Phrase: ', key_phrase_3)
			
			for item in key_phrase_3_match_list:
		
				print(item)			
			
			parse_count = parse_count + 1
		
		else:
	
			continue		

except Exception as error:
	
	print('\nParsing error: ', str(error))

# The following displays preliminary scrape results:

print('\nSECTION 2. SUMMARY')
print('\nNumber of HTML files parsed: ', parse_count)
print('Number of ', keyword_1, ' matches: ', len(keyword_1_match_list))
print('Number of ', keyword_2, ' matches: ', len(keyword_2_match_list))
print('Number of ', keyword_3, ' matches: ', len(keyword_3_match_list))
print('Number of ', key_phrase_1, ' matches: ', len(key_phrase_1_match_list))
print('Number of ', key_phrase_2, ' matches: ', len(key_phrase_2_match_list))
print('Number of ', key_phrase_3, ' matches: ', len(key_phrase_3_match_list))

print('\nEND OF RESULTS')

# END PRINT TO TEXT FILE

sys.stdout.close()
sys.stdout = stdoutOrigin

print('\n3. File Information')
print('\nContent exported to file: ', str(txt_file))
print('File location: ', str(Path(txt_file_path.anchor, txt_file_path.parent)))
quit_script = input('\nEnd of script. Press Enter to quit.')