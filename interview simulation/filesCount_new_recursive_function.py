import os


def dirCount(ProjDir,dict):
	subs = os.listdir(ProjDir)
	total = 0
	for item in subs:
		if os.path.isdir(os.path.join(ProjDir, item)):
			total += dirCount(os.path.join(ProjDir, item),dict)
		else:
			total += 1

	dict[ProjDir] = total
	

	return total

def filesCount(ProjDir):
	result = {}
	dirCount(ProjDir,result)
	for key in sorted(result.keys()):
		print(key,result[key])





filesCount(os.getcwd())
# print(result)

