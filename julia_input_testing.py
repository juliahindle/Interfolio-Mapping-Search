import re

# "constant" vars
IN_FORMATS = ['wos', 'asjc', 'sm journal', 'anzsrc', 'cip', 'dc']
OUT_FORMATS = ['dc', 'cip']
SEARCH_FORMATS = ['id', 'name']

# general function defs
def clean_string(str):
	return re.sub(r'\W+', ' ', str.lower())

def clean_id(num):
	return num

# get input format
print('Input format options: WOS, ASJC, SM Journal, ANZSRC, CIP, DC')
in_format = raw_input('Input: ')
while (clean_string(in_format) not in IN_FORMATS):
	print('Invalid input format. Please choose from list')
	in_format = raw_input('Input: ')

# get output format
print('Output format options: DC, CIP')
out_format = raw_input('Output: ')
while (clean_string(out_format) not in OUT_FORMATS):
	print('Invalid output format. Please choose from list')
	out_format = raw_input('Output: ')

# get search format
print('Search options: ID, Name')
search_format = raw_input('Search by: ')
while (clean_string(search_format) not in SEARCH_FORMATS):
	print('Invalid search format. Please choose from list')
	out_format = raw_input('Search by: ')

# get search key
if search_format == ID:
	key = clean_id(raw_input('Search for: '))
else
	key = clean_string(raw_input('Search for: '))









# if provided file name as arg, output to it. Else output to terminal