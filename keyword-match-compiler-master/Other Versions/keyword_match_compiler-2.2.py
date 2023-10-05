'''
Keyword Match Compiler
Version: 2.2
By Antonios J. Bokas
Last Update: October 7, 2021
'''

''' IMPORT STANDARD LIBRARIES '''

import datetime, os, re, sys, time
from pathlib import Path

''' IMPORT THIRD PARTY LIBRARIES '''

from bs4 import BeautifulSoup

''' MAIN ENTRY POINT '''

print('Keyword Match Compiler', '\nby Antonios J. Bokas')

print('\nThis script parses all HTML files in a given directory for two or four keyword compilations.' \
	  '\nA keyword compilation contains two key words or phrases that are determined by the user.' \
	  '\nA text field in the HTML that contains both keywords in a compilation is counted in the match totals.' \
	  '\nAll results are then summarized and written to a TXT file for further analysis.')

print('\nSTEP 1. USER INPUTS')

project_name = input('\nEnter a name for your project: ')
directory = input('Enter a directory that contains HTML files (e.g., C:/Users/___/Documents): ')
while os.path.isdir(directory) == False: # verifies that the directory exists.
	del directory
	directory = input('Incorrect directory path. Please try again: ')
txt_file = Path(str(project_name) + '_parse' + str('.txt')) # creates a TXT file.
txt_file_path = Path(directory, str(txt_file)) # creates the absolute path of the TXT file.
minimum_file_size = input('Enter a file-size threshold in bytes (e.g., 100000): ')
chunk_size = int(input('Enter a chunk size (in bytes):  '))
time.sleep(0.5)

print('\nSTEP 2. KEY WORDS AND PHRASES')

print('\nKeyword Compilation 1')
keyword_1a = input('\nEnter the first key word or phrase: ')
while keyword_1a == '':
	keyword_1a = input('\nYou must enter at least one word or phrase: ')
keyword_1b = input('Enter a second key word or phrase: ')

print('\nKeyword Compilation 2')
keyword_2a = input('\nEnter the first key word or phrase: ')
while keyword_2a == '':
	keyword_2a = input('\nYou must enter at least one key word or phrase: ')
keyword_2b = input('Enter a second key word or phrase: ')

more_inputs = input('\nDo you want to create two more compilations? Enter (Y) for yes or (N) for no: ')

if more_inputs == 'Y':

	print('\nKeyword Compilation 3')
	keyword_3a = input('\nEnter the first key word or phrase: ')
	while keyword_3a == '':
		keyword_3a = input('\nYou must enter at least one key word or phrase: ')
	keyword_3b = input('Enter a second key word or phrase: ')
	
	print('\nKeyword Compilation 4')
	keyword_4a = input('\nEnter the first key word or phrase: ')
	while keyword_4a == '':
		keyword_4a = input('\nYou must enter at least one key word or phrase: ')	
	keyword_4b = input('Enter a second key word or phrase: ')

# BEGIN PRINT TO TEXT FILE

stdoutOrigin = sys.stdout # changes the print function output.
sys.stdout = open(txt_file_path, "w") # makes the print function output to the TXT file.

print('PARSE RESULTS FOR DIRECTORY ', directory)

print('\nMethod: "Keyword Match Compiler" Python script by Antonios J. Bokas')
time_now = datetime.datetime.now()
print('\nExecuted:', time_now.strftime('%H:%M:%S, %A, %B %d, %Y'))

print('\n----------------------------------------------------------------------')
print('SECTION 1. KEYWORD COMPILATIONS')

print('\nKeyword Compilation 1')
print('\nFirst keyword: ', keyword_1a)
print('Second keyword: ', keyword_1b)

print('\nKeyword Compilation 2')
print('\nFirst keyword: ', keyword_2a)
print('Second keyword: ', keyword_2b)

if more_inputs == 'Y':

	print('\nKeyword Compilation 3')
	print('\nFirst keyword: ', keyword_3a)
	print('Second keyword: ', keyword_3b)

	print('\nKeyword Compilation 4')
	print('\nFirst keyword: ', keyword_4a)
	print('Second keyword: ', keyword_4b)

print('\n----------------------------------------------------------------------')
print('SECTION 2. COMPLIATION MATCHES')

compilation_1_matches = []
compilation_2_matches = []
compilation_3_matches = []
compilation_4_matches = []
parse_count = 0

for file_name in os.listdir(directory): # determines which directory will be processed.
	if file_name.endswith('.html'): # determines that only HTML files will be processed.
		if os.path.getsize(Path(directory, file_name)) > int(minimum_file_size):
			
			print('\n>>> HTML FILE: ', file_name)	
				
			try:
			
				archived_page = open(str(Path(directory, file_name)), encoding='utf-8') # opens the first HTML file in the directory.
				archived_page_html = BeautifulSoup(archived_page, 'html.parser') # accesses the HTML code with bs4 BeautifulSoup.
				
				# The following cycle parses the HTML file for Keyword Compilation 1:
				
				print('\nKeyword Compilation 1')
				keyword_1a_matches = archived_page_html.find_all(text=re.compile(keyword_1a)) # returns the context of each instance of the keyword.
				
				for each_keyword_1a_match in keyword_1a_matches:
					if keyword_1b in each_keyword_1a_match:
						if len(each_keyword_1a_match) < 151:
							compilation_1_matches.append(each_keyword_1a_match)
							print('"' + each_keyword_1a_match + '"')
	
				# The following cycle parses the HTML file for Keyword Compilation 2:
				
				print('\nKeyword Compilation 2')
				keyword_2a_matches = archived_page_html.find_all(text=re.compile(keyword_2a)) # returns the context of each instance of the keyword.
				
				for each_keyword_2a_match in keyword_2a_matches:
					if keyword_2b in each_keyword_2a_match:
						if len(each_keyword_2a_match) < 151:
							compilation_2_matches.append(each_keyword_2a_match)
							print('"' + each_keyword_2a_match + '"')
							
				# The following cycle parses the HTML file for Keyword Compilation 3:
				
				if more_inputs == 'Y':
							
					print('\nKeyword Compilation 3')
					keyword_3a_matches = archived_page_html.find_all(text=re.compile(keyword_3a)) # returns the context of each instance of the keyword.
					
					for each_keyword_3a_match in keyword_3a_matches:
						if keyword_3b in each_keyword_3a_match:
							if len(each_keyword_3a_match) < 151:
								compilation_3_matches.append(each_keyword_3a_match)
								print('"' + each_keyword_3a_match + '"')
								
					# The following cycle parses the HTML file for Keyword Compilation 4:
								
					print('\nKeyword Compilation 4')
					keyword_4a_matches = archived_page_html.find_all(text=re.compile(keyword_4a)) # returns the context of each instance of the keyword.
					
					for each_keyword_4a_match in keyword_4a_matches:
						if keyword_4b in each_keyword_4a_match:
							if len(each_keyword_4a_match) < 151:
								compilation_4_matches.append(each_keyword_4a_match)
								print('"' + each_keyword_4a_match + '"')
				
				parse_count = parse_count + 1 # tracks the number of HTML files parsed.
			
			except Exception as error_1:
				
				print('\nParsing error: ', str(error_1))			

print('\n----------------------------------------------------------------------')
print('SECTION 3. SUMMARY')

print('\nNumber of HTML files parsed: ', parse_count)
print('Number of Keyword Compilation 1 matches for batch: ', len(compilation_1_matches))
print('Number of Keyword Compilation 2 matches for batch: ', len(compilation_2_matches))

if more_inputs == 'Y':
	
	print('Number of Keyword Compilation 3 matches for batch: ', len(compilation_3_matches))
	print('Number of Keyword Compilation 4 matches for batch: ', len(compilation_4_matches))
	print('Total matches for batch: ', len(compilation_1_matches) + len(compilation_2_matches) + len(compilation_3_matches) + len(compilation_4_matches))
	
else:
	
	print('Total number of matches for batch: ', len(compilation_1_matches) + len(compilation_2_matches))
	
print('\nEND OF RESULTS')

# END PRINT TO TEXT FILE

sys.stdout.close() # closes the TXT file.
sys.stdout = stdoutOrigin # returns the print function output to the script display.
time.sleep(0.5)

print('\nSTEP 3. FILE INFORMATION')

print('\nContent exported to file: ', str(txt_file))
file_size = os.path.getsize(txt_file_path)
print('File size : ', str('{:,}'.format(file_size)), ' bytes')
print('File location: ', str(Path(txt_file_path.anchor, txt_file_path.parent)))
quit_script = input('\nEnd of script. Press Enter to quit.')