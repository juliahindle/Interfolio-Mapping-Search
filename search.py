import re
import csv

# "constant" vars
IN_FORMATS = ['wos', 'asjc', 'sm journal', 'anzsrc', 'cip', 'dc']
OUT_FORMATS = ['dc', 'cip']
SEARCH_FORMATS = ['id', 'name']

# classes
class GenericObj:
	def __init__(self, local_id, local_name, DC_id):
		self.local_id = local_id
		self.local_name = local_name
		self.DC_id = DC_id


class Ref:
	def __init__(self, DC_id, Flvl_name, Slvl_name, Tlvl_name):
		self.DC_id = DC_id
		self.Flvl_name= Flvl_name
		self.Slvl_name = Slvl_name
		self.Tlvl_name = Tlvl_name

	def print_ref(self):
		print("Mapped ID" + self.DC_id)
		print("low level name: " + self.Flvl_name)
		print("mid level name: " + self.Slvl_name)
		print("high level name: " + self.Tlvl_name)

# general function defs
def clean_string(words):
	return re.sub(r'\W+', ' ', words.lower())

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

# set file paths
in_file_path = clean_string(out_format) + '_mapping/' + clean_string(in_format) + '.csv'
ref_file_path =  clean_string(out_format) + '_mapping/REFERENCE.csv'


# open and scan csv files
in_list = []
ref_list = []

with open (in_file_path, 'r') as file:
	in_reader = csv.reader(file)

	next(in_reader)
	next(in_reader)

	for line in in_reader:
		in_list.append(GenericObj(line[0], line[1], line[4]))
		print(line[1])


with open (ref_file_path, 'r') as file:
	ref_reader = csv.reader(file)

	next(ref_reader)

	for line in ref_reader:
		ref_list.append(Ref(line[0], line[1], line[3], line[5]))


# get search format
print('Search options: ID, Name')
search_format = raw_input('Search by: ')
while (clean_string(search_format) not in SEARCH_FORMATS):
	print('Invalid search format. Please choose from list')
	out_format = raw_input('Search by: ')

# get search key
if search_format == 'ID':
	key = clean_id(raw_input('Search for: '))
else:
	key = clean_string(raw_input('Search for: ')) 

in_count = 0
if search_format == 'ID':
	while key != in_list[in_count].local_id:	
		in_count +=1
		if in_count >= len(in_list): 
			print('Input not found')
			exit(1)
else:
	while key != in_list[in_count].local_name:	
		in_count +=1
		if in_count >= len(in_list):
			print('Input not found')
			exit(1)


# do search then call print function
temp_id = in_list[in_count].DC_id

ref_count = 0
while(temp_id !=ref_list[ref_count].DC_id):
	ref_count +=1

Ref.print_ref(ref_list[ref_count])