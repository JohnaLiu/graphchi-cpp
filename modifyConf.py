import io, os, sys
from tempfile import mkstemp
from shutil import move
from os import remove, close

file_path ="/Users/zhijiaoliu/Documents/Github/graphchi-cpp/conf/graphchi.cnf"
# print f

mem=sys.argv[1]
cache=sys.argv[2]

fh, abs_path = mkstemp()
with open(abs_path,'w') as new_file:
    with open(file_path, "r") as old_file:
        for line in old_file:
        	if "membudget_mb" in line and "#" not in line:
        		line = line.split("=")[0]
        		line+="= "+mem+"\n"
        	if "cachesize_mb" in line and "#" not in line:
        		line = line.split("=")[0]
        		line+="= "+cache+"\n"
        	new_file.write(line)
close(fh)
#Remove original file
remove(file_path)
#Move new file
move(abs_path, file_path)