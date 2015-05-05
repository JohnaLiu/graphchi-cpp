import io, os, sys

f=sys.argv[1]
name=f.split("/")[-1]
# print name
count=0
count_lines=0
with open("adjlist_"+name,"w") as outF:
	with open(f,"r") as inF:
		for line in inF:
			line=line.split("	")
			n=len(line[1:])
			out=line[0]
			for i in range(1,len(line)):
				if i==1:
					out+=" "+str(n)
				out+=" "+line[i]
			outF.write(out)
			count+=n
			count_lines+=1
print "#nodes:",count_lines,"#edges:",count
