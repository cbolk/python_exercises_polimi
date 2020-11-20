INFO_FILE_NAME = "info.txt"
N_OF_SAMPLES_KEY = "Number of samples"

FILE_PREFIX = "S_"
FILE_SUFFIX = ".gdm"

def readFileLines(fileName):
	try:
		f = open(fileName)
		lines = f.read().splitlines()
		return lines
	except:
		return []


def readInfoFile():
	result = 0
	lines = readFileLines(INFO_FILE_NAME)
	#scan for N_OF_SAMPLES_KEY:
	for l in lines:
		(key, value) = l.split('\t')
		if key ==  N_OF_SAMPLES_KEY:
			result = int(value)
			break

	return result

def buildFileName(index):
	s = FILE_PREFIX + '{:0>5}'.format(index)+FILE_SUFFIX
	return s


def processLine(l):
	print(l)
	parts = l.split('\t')
	print(len(parts))

def processFile(fname):
	print(fname)
	lines = readFileLines(fname)
	lineCount = len(lines)
	if lineCount > 0:
		for l in lines:
			processLine(l)
	else:
		print("cannot open "  + fname)

def process(nofFiles):
	for i in range(0,nOfFiles):
		fname = buildFileName(i)
		processFile(fname)

nOfFiles = readInfoFile()
if nOfFiles>0:
	print(nOfFiles ," to be processed")
	process(nOfFiles)
else:
	print(INFO_FILE_NAME + " is missing")