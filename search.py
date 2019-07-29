import re
import csv
from fuzzywuzzy import fuzz

# "constant" vars
IN_FORMATS = ['wos', 'asjc', 'smjournal', 'anzsrc', 'cerif', 'cip', 'dc']
OUT_FORMATS = ['dc', 'cip']
SEARCH_FORMATS = ['id', 'name']

# classes
class GenericObj:
	def __init__(self, local_id, local_name, ref_id):
		self.local_id = local_id
		self.local_name = local_name
		self.ref_id = ref_id


class Ref:
	def __init__(self, ref_id, Flvl_name, Slvl_name, Tlvl_name):
		self.ref_id = ref_id
		self.Flvl_name= Flvl_name
		self.Slvl_name = Slvl_name
		self.Tlvl_name = Tlvl_name

	def print_ref(self): 
		print('\n\n{')
		print('\t"mapped_id": "' + self.ref_id + '",')
		print('\t"low_level_name": "' + self.Flvl_name + '",')
		print('\t"mid_level_name": "' + self.Slvl_name + '",')
		print('\t"high_level_name": "' + self.Tlvl_name + '"')
		print('}')

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


# open and scan csv files
in_list = []
ref_list = []

with open (in_file_path, 'r') as file:
	in_reader = csv.reader(file)

	next(in_reader)

	for line in in_reader:
		in_list.append(GenericObj(clean_id(line[0]), clean_string(line[1]), line[4]))


with open (ref_file_path, 'r') as file:
	ref_reader = csv.reader(file)

	next(ref_reader)

	for line in ref_reader:
		ref_list.append(Ref(line[0], line[1], line[3], line[5]))


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
in_count = 0
if search_format == 'id':
	while key != in_list[in_count].local_id:	
		in_count += 1
		
		if in_count >= len(in_list): 
			print('ID not found')
			exit(1)
else:
	max_ratio = 0
	while key != in_list[in_count].local_name:
		''''''
		current_ratio = fuzz.ratio(key, in_list[in_count].local_name)
		
		if current_ratio > max_ratio:
			max_ratio = current_ratio
			temp = in_list[in_count].local_name
		''''''
		in_count += 1
		
		if in_count >= len(in_list):
			print('Name not found. Did you mean ' + '\033[94m' + temp + '\033[0m' + '?')
			exit(1)

temp_id = in_list[in_count].ref_id
clean_temp_id = clean_id(temp_id)



ref_count = 0
while clean_temp_id != clean_id(ref_list[ref_count].ref_id):
	ref_count += 1

	if ref_count >= len(ref_list): 
			print('Reference not found')
			exit(1)

# output
Ref.print_ref(ref_list[ref_count])






'''
need to stop user from bad inputs (i.e. cip -> cip, ID when format doesn't have IDs)
deal with cleaning apostrophes
allow user to continue doing searches?




DICT OPTION:

////////////For input search//////////////
"inputted ID": "mapped ID"				ex: "1007": "3.04.01"
"inputted name": "mapped ID"			ex: "Architecture": "3.04.01"

///////For mapped reference search////////
"mapped ID": ["low level name", "mid level name", "high level name"]	
			ex: "2.04.15": ["Sculpture", "Art and Design", "Arts and Humanities"]

Pro: easy search (ex: dict.get("3.04.01"))

Concerns: fuzzy match, even just with clean_string function, seems difficult with dict.get()
		  do we even need to store data in data structure vs. comparing in moment and holding onto data we need

'''








