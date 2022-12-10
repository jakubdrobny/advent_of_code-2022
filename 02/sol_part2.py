sc=0
dic={'AX':3,'BX':1,'CX':2,'AY':4,'BY':5,'CY':6,'AZ':8,'BZ':9,'CZ':7}
with open(inputFilename, 'r') as f:
	for l in f.readlines():
		sc+=dic[l[0]+l[2]]
print(sc)