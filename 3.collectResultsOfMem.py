import io, os, sys, json

benchmark = "pagerank"
# print os.path.join(os.getcwd(),benchmark)
list_dirs = os.walk(os.path.join(os.getcwd(),"memory"))
for root, dirs, files in list_dirs: 
	# print files
	for f in files:
		a, b = os.path.splitext(f)
		# print a, b
		if benchmark in a and "stdout" in b:
			with open(os.path.join(root,f), "r") as inF:
				# print a
				for line in inF:
					# if "execute_sharding" in line:
					# 	# print line.strip()
					# 	print line.strip().split("		")[-1].split("	 ")[0].split(" ")[0]
					if "runtime" in line and "total" not in line and "degree" not in line:
						# print line.strip()
						print a,"	",line.strip().split("		")[-1].split(" ")[0]
						print line.strip().split("		")[-1].split(" ")[0]