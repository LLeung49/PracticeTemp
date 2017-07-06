import os

result = {}

def filesCount(ProjDir):
	output = []
	subs = os.listdir(ProjDir)
	total = 0
	for item in subs:
		if os.path.isdir(os.path.join(ProjDir, item)):
			total += filesCount(os.path.join(ProjDir, item))
		else:
			total += 1
	# output = output + [ProjDir, total]
	# print(ProjDir, total)
	result[ProjDir] = total
	

	return total




filesCount(os.getcwd())
# print(result)

for key in sorted(result.keys()):
	print(key,result[key])