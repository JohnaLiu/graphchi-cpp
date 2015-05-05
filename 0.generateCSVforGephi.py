import io, os, sys, json

OUTPUT = {"nodes":[],"links":[]}
nodes = []

# f=sys.argv[1]
f="/Users/zhijiaoliu/Documents/NetworkData/soc-sign-epinions/soc-sign-epinions.txt"
c=0
with open("test.csv","w") as outF:
	outF.write("Source,Target\n")
	with open(f,"r") as inF:
		for line in inF:
			if not "#" in line:
				[s,t] = line.split("	")[:2]
				s = s.strip()
				t = t.strip()
				# link={}
				# link["source"]=int(s)
				# link["target"]=int(t)
				# link["value"]=1
				# OUTPUT["links"].append(link)
				# if s not in nodes:
				# 	nodes.append(s)
				# 	node = {}
				# 	node["name"]=s
				# 	node["group"]=1
				# 	OUTPUT["nodes"].append(node)
				# if t not in nodes:
				# 	nodes.append(t)
				# 	node = {}
				# 	node["name"]=t
				# 	node["group"]=1
				# 	OUTPUT["nodes"].append(node)
				# if int(s) < 2000 and int(t) <2000: 
				outF.write(s+","+t+"\n")
				if c%100000==0:
					print c
				c+=1

# with open("out.json","w") as outF:
# 	json.dump(OUTPUT, outF)