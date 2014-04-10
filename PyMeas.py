import time, os, linecache, warnings, os, fnmatch, re

def get_info(filename,sep_mark=''):
	"""
	get_info(filename,sep_mark='')
	Get the information needed to process the measurement results
	sep_mark is defaul to be whitespace, potential ',' needed
	all line number are 0 biased
	return (tot_lines,line_info0, line_info1, num_last_blk_line)
	tot_lines: total number of lines in the file
	line_info0, line_info1: first line and last line of varible names
	num_last_blk_line: entry # in the last line of a block	
	"""
	line_info0,line_info1=-1,-1,
	fh=open(filename,'r')
	tot_lines=sum(1 for _ in fh)
	fh.seek(0)
	line_ct=0-1  # 0 for actual line number, -1 for 0 biased line number
	for line in fh:
		line_ct+=1
		if line.find(".TITLE '**")==0:
			line_info0=line_ct+1
		else:
			if line.find("alter#")!=-1:
				line_info1=line_ct
				if not sep_mark:
					split_line=line.strip('\n').split()
				else:
					split_line=line.strip('\n').split(sep_mark) 
				split_line=[i for i in split_line if i != '']
				num_last_blk_line=len(split_line)
				break
	fh.close()
	blk_lines=line_info1-line_info0+1
	# print line_info0, line_info1, num_last_blk_line,tot_blk_entry
	return (tot_lines,line_info0, line_info1, num_last_blk_line)

def mea_file_unwrap(filename,sep_mark="  "):
	"""
	mea_file_unwrap(filename='Global2.mt0',sep_mark="  ")
	return (num_blk,len(blk_line))
	
	unwrap measurement files into a matrix
	failed entries will be substituted by a number
	sep_mark: change this to ',' for csv like format
	num_blk: number of blocks ( for MC simulation ) 
	len(blk_line): number of measurement n each block
	"""
	if not os.path.isfile(filename):
		print "%s not exist\n"%(filename)
		return 
	tot_lines,line_info0, line_info1,=get_info(filename)
	f=linecache.getlines(filename)
	outfilename='./'+filename.replace('.','_')+'.txt'
	fhout=open(outfilename,'w')
	num_blk=(tot_lines-line_info1-1)/(line_info1-line_info0+1)
	num_blk_line=line_info1-line_info0+1
	for blkct in xrange(num_blk):
		blk_line=[]
		for blk_line_ct in xrange(num_blk_line):
			current_line_pt=line_info1+1+num_blk_line*blkct+blk_line_ct
			current_line=f[current_line_pt].replace("failed", "-1.11")
			current_line_list=current_line.split()
			blk_line=blk_line+current_line_list
		fhout.write(sep_mark.join(blk_line)+"\n")
	fhout.close()
	print "%s: num_blk %d;\t Num_entry %d;\t Blk_line %d"\
	%(filename,num_blk,len(blk_line),num_blk_line)
	return (num_blk,len(blk_line))

def tocheckexist(fname,types=None):
	"""
	tocheckexist(fname,types=None)
	chekc whether a file name string match a set of regexp patterns
	return None if not match
	otherwise return the first matched regexp type
	"""
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
	"""
	get_file_list(types=None,osdir='./')
	get a list of file names in osdir directory that matche the file type
	"""
	flist=os.listdir(osdir)
	print flist, "\n\n"
	outlist=[]
	for f in flist:
		if tocheckexist(f,types) is not None:
			outlist=outlist+[f]
	return outlist
		
	
name_list=get_file_list()
# name_list=['comparetr.txt']
for fname in name_list:	
	blk_process(fname)
help(get_info)
