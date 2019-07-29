import re
import csv
from fuzzywuzzy import fuzz

# "constant" vars
IN_FORMATS = ['wos', 'asjc', 'smjournal', 'anzsrc', 'cerif', 'cip', 'dc']
OUT_FORMATS = ['dc', 'cip']
SEARCH_FORMATS = ['id', 'name']

# general function defs
def clean_string(s):
	cleaned = re.sub(r'\W+', ' ', s.lower())	# remove special characters
	cleaned = re.sub(r'^\s+', '', cleaned)		# remove leading spaces
	cleaned = re.sub(r'\s+$', '', cleaned)		# remove trailing spaces
	return cleaned

def clean_id(s):
	cleaned = re.sub(r'^0', '', s)				#remove leading 0
	cleaned = re.sub(r'\.0+$', '', cleaned)		#remove trailing .00
	cleaned = re.sub(r'\.0+$', '', cleaned)		#remove trailing .00
	return cleaned

def print_ref(line):
	print('\n\n{')
	print('\t"mapped_id": "' + line[0] + '",')
	print('\t"low_level_name": "' + line[1] + '",')
	print('\t"mid_level_name": "' + line[3] + '",')
	print('\t"high_level_name": "' + line[5] + '"')
	print('}')

# get input format
print('Input format options: WOS, ASJC, SMjournal, ANZSRC, CERIF, CIP, DC')
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

# set file paths
in_file_path = clean_string(out_format) + '_mapping/' + clean_string(in_format) + '.csv'
ref_file_path =  clean_string(out_format) + '_mapping/REFERENCE.csv'


# get search format
print('Search options: ID, Name')
search_format = clean_string(raw_input('Search by: '))
while (clean_string(search_format) not in SEARCH_FORMATS):
	print('Invalid search format. Please choose from list')
	search_format = clean_string(raw_input('Search by: '))

# get search key
if search_format == 'id':
	key = clean_id(raw_input('Search for: '))
else:
	key = clean_string(raw_input('Search for: ')) 

# search for input
in_file =  open (in_file_path, 'r')
in_reader = csv.reader(in_file)
next(in_reader)

found_id = ''

# ID
if search_format == 'id':
	for line in in_reader:
			if key == clean_id(line[0]):
				found_id = clean_id(line[4])
	
	if found_id == '':
		print('ID not found')
		exit(1)
# Name
else:
	max_ratio = 0
	closest_match = ''
	closest_match_id = ''

	for line in in_reader:
		if key == clean_string(line[1]):
			found_id = clean_id(line[4])
		else:
			current_ratio = fuzz.ratio(key, clean_string(line[1]))
			if current_ratio > max_ratio:
				max_ratio = current_ratio
				closest_match = line[1]
				closest_match_id = clean_id(line[4])
	
	if found_id == '':
		print('Name not found. Did you mean \033[94m' + closest_match + '\033[0m?')
		answer = raw_input('Y/N: ')
		if clean_string(answer) in ['n', 'no']: 
			exit(1)
		found_id = closest_match_id
		

# search for and print mapping in reference
out_file =  open(ref_file_path, 'r')
ref_reader = csv.reader(out_file)

next(ref_reader)

for line in ref_reader:
	if found_id == clean_id(line[0]):
		print_ref(line)
		exit(0)

print('Reference not found')
exit(1)




