import re

def clean_id(s):
	clean_num = re.sub(r'^0', '', s)
	clean_num = re.sub(r'\.0+$', '', clean_num)
	clean_num = re.sub(r'\.0+$', '', clean_num)
	return clean_num

inp = raw_input('Search for: ') 
print(clean_id(inp))