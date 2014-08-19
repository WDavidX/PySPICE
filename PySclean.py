'''
Created on Apr 11, 2014
@author: David Xu
To check all files to be deleted use "python PySclean.py"
To delete all files "python PySclean.py 1"
'''
import os, re, sys
print sys.argv[1:]
argc=len(sys.argv)
types=[r"\w+\.((ic)|(st)|(op)|(pa)|(su))\d+\w*",r"\w+.pyc$", r"\w+.lis$",\
       r"\w+.printtr\w*$",r"scope.log\w*",r"\w+~$",r"logFile",r"\w*.log$",\
       r"libManager\w*",r"\w+.raw$",r"log$"] # aux files
type2,type3=[],[]
types2=[r"\w+\.((sw)|(tr)|(ac)|(mt))\d+\w*"] # results files
types3=[r"sxcmd.log\w*",r"\w*.ibs",r"\w+.((scs)|(ami)|(partial)|(ibs)|(srf)|(look)|(info)|(tran)|(old))$",\
        r"\w+.((plt)|(save0)|(stev0)|(stet0)|(printSte0)|(mste0))$"]
types=types+types2+types3  # include result files

def removeEmptyFolders(path):
  if not os.path.isdir(path):  return
  # remove empty subfolders
  files = os.listdir(path)
  if len(files):
    for f in files:
      fullpath = os.path.join(path, f)
      if os.path.isdir(fullpath):  removeEmptyFolders(fullpath)
  # if folder empty, delete it
  files = os.listdir(path)
  if len(files) == 0:
    print "Removing empty folder:", path
    os.rmdir(path)

# print types
def tocheckexist(fname):
  for ftype in types:
    g=re.search(ftype, fname)
    if g is not None:
      # print "found ",g.group(0), "  ", ftype, "  ", fname
      return ftype
  return None

def walkclean(curr_dir='./'):
  counter=0
  print "Current path: %s"%(os.path.abspath(curr_dir))
  for dirpath,_,files in os.walk(curr_dir):
    #print dirpath, files 
    for f in files:
      #print os.path.join(dirpath,f)
      checkresult=tocheckexist(f)
      if checkresult is not None:
        counter=counter+1
        cur_path=os.path.join(dirpath,f)
        if (argc==2):
          print "%40s"%(f), "     ", checkresult 
          os.remove(cur_path)
        else:
          print "%40s"%(f), "     ", checkresult
  if (argc==2):removeEmptyFolders(curr_dir)
  return counter

dir_to_clean='./'
nfind=walkclean(dir_to_clean)

if (argc==2):
  print "%d files removed from\n%s"%(nfind,os.path.abspath(dir_to_clean))
else:
  print "%d files found from\n%s"%(nfind,os.path.abspath(dir_to_clean))
