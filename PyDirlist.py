import time, os, linecache, warnings, os, fnmatch, re


def tocheckexist(fname,types=None):
	if types is None:
		types=(r"\w{1,}\.mt[0-9]+$")
	types=(types,)
	for ftype in types:
		g=re.search(ftype, fname)
		if g is not None:
			# print "file found ",g.group(0), "    ", ftype, "    ", fname
			return ftype
	return None

def get_file_list(types=None,osdir='./'):
	flist=os.listdir(osdir)
	print flist, "\n\n"
	outlist=[]
	for f in flist:
		if tocheckexist(f,types) is not None:
			outlist=outlist+[f]
	return outlist
	
	

print get_file_list()