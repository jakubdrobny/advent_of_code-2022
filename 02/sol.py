ls=[]
dic={'A':1,'B':2,'C':3}
with open(inputFilename, 'r') as f:
	ls = f.readlines()
from itertools import permutations
mx=0
#for p in permutations('XYZ'):
for ttt in range(1):
	#pl=list(p)
	pl=['X','Y','Z']
	cur=0
	for l in ls:
		print(l)
		p1,p2=dic[l[0]], pl.index(l[2])+1
		cur+=p2
		if p1==p2:
			cur+=3
		else:
			p1+=1
			if p1==4:p1=1
			elif p1==p2:
				cur+=6
		print(cur)
	mx=max(mx,cur)
print(mx)