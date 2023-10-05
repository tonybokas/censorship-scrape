'''
Wayback Machine Scraper
Version: 1.0
By Antonios J. Bokas
Last Update: September 30, 2021
'''

''' IMPORT STANDARD LIBRARIES '''

import codecs
import datetime
import os
import sys
import time
from pathlib import Path

''' IMPORT THIRD PARTY LIBRARIES '''

from selenium import webdriver

''' MAIN ENTRY POINT '''

print('Wayback Machine Scraper\nby Antonios J. Bokas')

print('\nThis script scrapes web pages that are archived in the Wayback Machine.'
      '\nFirst, you must enter a URL, save folder location, and date range. '
      '\nThe script then scrapes one version of the archived page for each day in the date range. '
      '\nFinally, the script saves a scrape summary to a TXT file for future reference.')

print('\nSTEP 1. USER INPUTS')

wayback_machine_url = 'http://web.archive.org/web/'

target_website = (input('\nEnter a web page you want to scrape, (e.g., https://___.com): '))
project_name = input('Enter a name for your project: ')
extant_folder = input('Enter a save directory (e.g., C:/Users/___/Downloads): ')

while os.path.isdir(extant_folder) == False:  # verifies that the save directory exists.

	del extant_folder
	extant_folder = input('Incorrect directory path. Please try again: ')

os.makedirs(Path(extant_folder, project_name + '_scrape'), exist_ok=True)  # creates a new folder for the project.
directory = str(Path(extant_folder, project_name + '_scrape'))  # creates the absolute path of the new folder.

start_day_string = input('Enter the start date of your scrape (e.g., YYYY-MM-DD): ')
end_day_string = input('Enter the end date of your scrape (e.g., YYYY-MM-DD): ')
time_of_day = int(input('Enter a prefered time to scrape for every date (e.g., HHMMSS): '))

start_day = datetime.date.fromisoformat(start_day_string)
end_day = datetime.date.fromisoformat(end_day_string)
results_limit = end_day - start_day  # establishes the date range.

file_name = project_name
txt_file = Path(str(file_name) + '-scrape_activity_log' + str('.txt'))  # creates a TXT file.
txt_file_path = Path(directory, str(txt_file))  # creates the absolute path of the TXT file.
time.sleep(0.5)

print('\nSTEP 2. SCRAPE')

print('\nScrape in progress.')

# BEGIN PRINT TO TEXT FILE

stdoutOrigin = sys.stdout  # changes the print function output.
sys.stdout = open(txt_file_path, "w")  # makes the print function output to the TXT file.

print('SCRAPE SUMMARY FOR ', target_website, ' FROM WAYBACK MACHINE')
print('\nMethod: "Wayback Machine Scraper" Python script by Antonios J. Bokas')

time_now = datetime.datetime.now()
print('\nExecuted:', time_now.strftime('%H:%M:%S, %A, %B %d, %Y'))

print('\n----------------------------------------------------------------------')
print('SECTION 1. PARAMETERS')

print('\nStart date: ', start_day_string)
print('End date: ', end_day_string)
print('Range: ', results_limit.days + 1, ' days')

print('\n----------------------------------------------------------------------')
print('SECTION 2. ACTIVITY LOG')

search_day = start_day  # makes the first day of the date range the start point of the scrape.
additional_day = datetime.timedelta(days=1)  # equals one day in the correct format.

failed_downloads = 0
file_count = 1  # is added to the name of each HTML file.
day_count = 0  # is used to track progress through the date range.

while day_count <= results_limit.days:

	working_day = search_day.strftime('%Y%m%d')  # adds the year, month, and day to the URL.
	current_url = wayback_machine_url + working_day + str(time_of_day) + '/' + target_website  # is the Wayback Machine URL formula.

	try:

		web_broswer = webdriver.Firefox()  # launches the selenium webdriver.
		web_broswer.implicitly_wait(0.5)
		web_broswer.get(current_url)

	except Exception as error_1:

		print('\nError: ', str(error_1))

	try:

		print('\nAccessing archive for date: ', search_day)
		print('Scraping page: ', str(web_broswer.current_url))
		html_file_path = os.path.abspath(str(Path(directory, project_name + '-day_' + str(file_count) + '.html')))  # creates the absolute path of the HTML file.
		open_html_file = codecs.open(html_file_path, "w", "utf−8")
		html_code = web_broswer.page_source
		open_html_file.write(html_code)
		open_html_file.close()
		web_broswer.quit()
		file_count = file_count + 1

	except Exception as error_2:

		print('\nError:', str(error_2))

	day_count = day_count + 1
	search_day = search_day + additional_day  # determines the next day and page that will be scraped.

print('\n----------------------------------------------------------------------')
print('SECTION 3. RESULTS')

print('\nNumber of pages scraped: ', str(file_count - 1))
print('\nEND OF SUMMARY')

# END PRINT TO TEXT FILE

sys.stdout.close()  # closes the TXT file.
sys.stdout = stdoutOrigin  # returns the print function output to the script display.

print('Scrape complete.')
time.sleep(0.5)

print('\nSTEP 3. RESULTS')

print('\nNumber of pages scraped: ', str(file_count - 1))

if file_count >= 1:

	print('Pages saved to directory: ', str(directory))  # only displays if one or more pages were successfully scraped.

quit_script = input('\nEnd of script. Press Enter to quit.')