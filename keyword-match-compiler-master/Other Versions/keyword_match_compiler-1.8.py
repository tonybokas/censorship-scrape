'''
Keyword Match Compiler
Version: 1.6
By Antonios J. Bokas
Last Update: September 30, 2021
'''

''' IMPORT STANDARD LIBRARIES '''

import datetime, os, re, sys, time
from pathlib import Path

''' IMPORT THIRD PARTY LIBRARIES '''

from bs4 import BeautifulSoup

''' MAIN ENTRY POINT '''

print('Keyword Match Compiler', '\nby Antonios J. Bokas')

print('\nThis script parses all HTML files in a given directory for six user-identified key words or phrases. ' \
	  '\nAll results are then summarized and written to a TXT file for further analysis.')

print('\nSTEP 1. USER INPUTS')

project_name = input('\nEnter a name for your project: ')
directory = input('Enter a directory that contains HTML files (e.g., C:/Users/___/Documents): ')

while os.path.isdir(directory) == False: # verifies that the directory exists.
	
	del directory
	directory = input('Incorrect directory path. Please try again: ')

txt_file = Path(str(project_name) + '_parse' + str('.txt')) # creates a TXT file.
txt_file_path = Path(directory, str(txt_file)) # creates the absolute path of the TXT file.

time.sleep(0.5)

print('\nSTEP 2. KEY WORDS AND PHRASES')

keyword_1 = input('\nEnter the first key word or phrase: ')
keyword_2 = input('Enter the second key word or phrase: ')
keyword_3 = input('Enter the third key word or phrase: ')
keyword_4 = input('Enter the fourth key word or phrase: ')
keyword_5 = input('Enter the fifth key word or phrase: ')
keyword_6 = input('Enter the sixth key word or phrase: ')

# BEGIN PRINT TO TEXT FILE

stdoutOrigin = sys.stdout # changes the print function output.
sys.stdout = open(txt_file_path, "w") # makes the print function output to the TXT file.

print('PARSE RESULTS FOR DIRECTORY ', directory)

time_now = datetime.datetime.now()

print('\nExecuted:', time_now.strftime('%H:%M:%S, %A, %B %d, %Y'))
print('\nMethod: "Keyword Match Compiler" Python script by Antonios J. Bokas')

print('\n----------------------------------------------------------------------')
print('SECTION 1. KEY WORD OR PHRASE MATCHES')

keyword_1_match_list = []
keyword_2_match_list = []
keyword_3_match_list = []
keyword_4_match_list = []
keyword_5_match_list = []
keyword_6_match_list = []
parse_count = 0

try:
	
	for file_name in os.listdir(directory): # determines which directory will be processed.
	
		if file_name.endswith('.html'): # determines that only HTML files will be processed.
			
			print('\n>>> HTML FILE: ', file_name)
		
			archived_page = open(str(Path(directory, file_name)), encoding='utf-8') # opens the first HTML file in the directory.
			archived_page_html = BeautifulSoup(archived_page, 'html.parser') # accesses the HTML code with bs4 BeautifulSoup.
			
			# The following cycle parses the HTML file for six different keywords:
			
			keyword_1_matches = archived_page_html.find_all(text=re.compile(keyword_1)) # returns the context of each instance of the keyword.
			keyword_1_match_list = keyword_1_match_list + keyword_1_matches # compiles each context in a list.
			
			print('\nKeyword: ', keyword_1, '\n')
			
			if len(keyword_1_matches) > 0:
			
				for item in keyword_1_matches:
					
					print(item) # prints the context list.
					
			else:
				
				print('(None)')
			
			keyword_2_matches = archived_page_html.find_all(text=re.compile(keyword_2))
			keyword_2_match_list = keyword_2_match_list + keyword_2_matches
			
			print('\nKeyword: ', keyword_2, '\n')
			
			if len(keyword_2_matches) > 0:
			
				for item in keyword_2_matches:
			
					print(item)
					
			else:		
		
				print('(None)')			
		
			keyword_3_matches = archived_page_html.find_all(text=re.compile(keyword_3))
			keyword_3_match_list = keyword_3_match_list + keyword_3_matches
			
			print('\nKeyword: ', keyword_3, '\n')
			
			if len(keyword_3_matches) > 0:
			
				for item in keyword_3_matches:
			
					print(item)
			
			else:		
		
				print('(None)')				
				
			keyword_4_matches = archived_page_html.find_all(text=re.compile(keyword_4))
			keyword_4_match_list = keyword_4_match_list + keyword_4_matches
			
			print('\nKeyword: ', keyword_4, '\n')
			
			if len(keyword_4_matches) > 0:
			
				for item in keyword_4_matches:
					
					print(item)
			
			else:		
		
				print('(None)')					
			
			keyword_5_matches = archived_page_html.find_all(text=re.compile(keyword_5))
			keyword_5_match_list = keyword_5_match_list + keyword_5_matches
			
			print('\nKeyword: ', keyword_5, '\n')
			
			if len(keyword_5_matches) > 0:
			
				for item in keyword_5_matches:
			
					print(item)	
					
			else:		
		
				print('(None)')						
			
			keyword_6_matches = archived_page_html.find_all(text=re.compile(keyword_6))
			keyword_6_match_list = keyword_6_match_list + keyword_6_matches
			
			print('\nKeyword: ', keyword_6, '\n')
			
			if len(keyword_6_matches) > 0:
			
				for item in keyword_6_matches:
			
					print(item)
				
			else:		
		
				print('(None)')				
			
			parse_count = parse_count + 1 # tracks the number of HTML files parsed.
		
		else:
	
			continue		

except Exception as error_1:
	
	print('\nParsing error: ', str(error_1))

print('\n----------------------------------------------------------------------')
print('SECTION 2. SUMMARY')

print('\nNumber of HTML files parsed: ', parse_count)
print('Number of (', keyword_1, ') matches: ', len(keyword_1_match_list))
print('Number of (', keyword_2, ') matches: ', len(keyword_2_match_list))
print('Number of (', keyword_3, ') matches: ', len(keyword_3_match_list))
print('Number of (', keyword_4, ') matches: ', len(keyword_4_match_list))
print('Number of (', keyword_5, ') matches: ', len(keyword_5_match_list))
print('Number of (', keyword_6, ') matches: ', len(keyword_6_match_list))
print('\nEND OF RESULTS')

# END PRINT TO TEXT FILE

sys.stdout.close() # closes the TXT file.
sys.stdout = stdoutOrigin # returns the print function output to the script display.

time.sleep(0.5)

print('\nSTEP 3. FILE INFORMATION')

print('\nContent exported to file: ', str(txt_file))
print('File location: ', str(Path(txt_file_path.anchor, txt_file_path.parent)))

quit_script = input('\nEnd of script. Press Enter to quit.')