import csv

class generic_obj:
	def __init__(self, local_id, local_name, DC_id):
		self.local_id = local_id
		self.local_name = local_name
		self.DC_id = DC_id


class DC:
	def __init__(self, DC_id, Flvl_name, Slvl_name, Tlvl_name):
		self.DC_id = DC_id
		self.Flvl_name= Flvl_name
		self.Slvl_name = Slvl_name
		self.Tlvl_name = Tlvl_name

	def print_DC(self):
		print("The DCid of this object is " + self.DC_id)
		print("The first level DC classification of this object is " + self.Flvl_name)
		print("The second level DC classification of this object is " + self.Slvl_name)
		print("The third level DC classification of this object is " + self.Tlvl_name)


with open ('dc_mapping/cip.csv', 'r') as file:
	CIP_reader = csv.reader(file)

	next(CIP_reader)
	next(CIP_reader)
	
	
	CIPlist = []

	for line in CIP_reader:
		CIPlist.append(generic_obj(line[0], line[1], line[4]))


with open ('dc_mapping/REFERENCE.csv', 'r') as file:
	DC_reader = csv.reader(file)

	next(DC_reader)

	DClist = []

	for line in DC_reader:
		DClist.append(DC(line[0], line[1], line[3], line[5]))


inpt = raw_input("Please enter the CIP string that you would like to query ")

Gcount = 0

while(inpt != CIPlist[Gcount].local_name):	
	Gcount +=1

temp_id = CIPlist[Gcount].DC_id

DCcount = 0
while(temp_id !=DClist[DCcount].DC_id):
	DCcount +=1

DC.print_DC(DClist[DCcount])


# Gcount = 0
# while(inpt != CIPlist[Gcount].local_id):	
# 	Gcount +=1

# temp_id = CIPlist[Gcount].DC_id

# DCcount = 0
# while(temp_id !=DClist[DCcount].DC_id):
# 	DCcount +=1


# DC.print_DC(DClist[DCcount])



#DC.print_DC(DClist[6])
#print( "")
#generic_obj.print_object(CIPlist[0])

