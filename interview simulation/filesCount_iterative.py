import os



def Count(ProjDir):
	# output = {}
	# print("current:" ,ProjDir)
	total = 0
	for root, dirs, files in os.walk(ProjDir):
		total += len(files)
	return total

	


def filesCount(ProjDir):
	output = {}
	for r,d,f in os.walk(ProjDir):
		# output[r] = Count(r)
		print(r,Count(r))





# filesCount('/Users/lucienleung/Documents/Videos/pic')

filesCount(os.getcwd())