'''
Created on Apr 11, 2014
@author: David Xu
'''
import os, re, sys
print sys.argv[1:]
argc=len(sys.argv)
# argc=2
types=[r"\w+\.((ic)|(st)|(op)|(pa)|(su))\d+\w*",r"\w+.pyc$", \
       r"scope.log\w*",r"\w+~$",r"logFile"] # aux files
types2=[r"\w+\.((sw)|(tr)|(ac)|(mt))\d+\w*"] # results files
# types=types+types2  # include result files
def tocheckexist(fname):
  for ftype in types:
    g=re.search(ftype, fname)
    if g is not None:
      #print "found ",g.group(0), "  ", ftype, "  ", fname
      return ftype
  return None

def walkclean(curr_dir='./'):
  counter=0
  print "Current path: %s"%(os.path.abspath(curr_dir))
  for dirpath,_,files in os.walk(curr_dir):
    for f in files:
      checkresult=tocheckexist(f)
      if checkresult is not None:
        counter=counter+1
        cur_path=os.path.join(dirpath,f)
        if (argc==2):
          os.remove(cur_path)
        else:
          print "%20s"%(f), "  \t  ", checkresult        
  return counter

dir_to_clean='./'
nfind=walkclean(dir_to_clean)
if (argc==2):
  print "%d files removed from\n%s"%(nfind,os.path.abspath(dir_to_clean))
else:
  print "%d files found from\n%s"%(nfind,os.path.abspath(dir_to_clean))
