'''
Created on Sep 22, 2011

@author: David

Usage:
1 Please inlcude this file and comparetr.txt in the save directory
2 >> python readmeasure.py
'''



# This function converts a list into a string with approperiate strings
def line2str(cur_line):
    out_line=""
    for l in range(0,len(cur_line)):
        out_line=out_line+str(cur_line[l])+"  \t"
    return out_line+""

# parameter settings and file operations
inputfilename='comparetr.txt'
outputfilename=inputfilename.split('.')[0]+'_data.'+inputfilename.split('.')[1]
starting_line_num=6  # Need to mannually input the starting line of data
step_line_num=3      # How many lines are there in each sweeping

infile=open(inputfilename,'r')
infile=infile.readlines()
outfile=open(outputfilename,'w')

# Initializations
current_line_num=starting_line_num    # Pointing to hte startling line
total_data_num=0                      # Counter for total number of blocks 
ct_blk_step=0                         # Counter in each block
current_line=[]

# Iterate through all lines towards the end of file
while (current_line_num != len(infile)):
    
    current_line.extend(infile[current_line_num-1].split()) # read lines and extend current block line
    current_line_num=current_line_num+1  
    ct_blk_step=ct_blk_step+1
    if ct_blk_step == step_line_num:
        total_data_num=total_data_num+1
        ct_blk_step=0
        current_line.insert(0, total_data_num)
        tmpstr=line2str(current_line)
        print tmpstr  # print out parsed line
        outfile.write(tmpstr+"\n")
        num_entry=len(current_line)
        current_line=[]

print "\nTotal data number is", total_data_num
print "There are ",num_entry, " in each line.\n"
outfile.close()

