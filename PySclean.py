'''
Created on Apr 11, 2014
@author: David Xu
'''
import os, re, sys

print sys.argv[1:]
argc=len(sys.argv)
types=[r"\w{1,}\.((ic)|(st)|(op)|(pa))[0-9]{1,}\w{0,}",r"\w{1,}.pyc", r"scope.log\w{0,}"]

def tocheckexist(fname):
  for ftype in types:
    g=re.search(ftype, fname)
    if g is not None:
      #print "file found ",g.group(0), "    ", ftype, "    ", fname
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

nfind=walkclean()
if (argc==2):
  print "%d files removed"%(nfind)
else:
  print "%d files found but not removed"%(nfind)
