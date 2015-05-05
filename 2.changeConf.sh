#!/bin/bash
benchmark=$1

# echo $benchmark
root="/Users/zhijiaoliu/Documents/Github/graphchi-cpp/"
dir="/Users/zhijiaoliu/Documents/NetworkData/"
cd $dir
# for f in *.txt
# do 
# echo "Processing $f file.."
# echo $(pwd)
# done
MEMd=("400" "800" "1600" "3200")
CACHEd=("0" "200" "400" "800" "1600")

for mem in "${MEMd[@]}"
do
for cache in "${CACHEd[@]}"
do
`python /Users/zhijiaoliu/Documents/Github/graphchi-cpp/modifyConf.py $mem $cache`

out="-$benchmark.$mem.$cache.stdout"
FILES=$dir*
for f in $(find $FILES -type f)
do
	if [ ${f: -4} == ".txt" ]
		then
		cd $root
		# echo $(pwd)
		filename="${f%.*}"
		echo "`bin/example_apps/$benchmark file $f`" > $filename$out
		# echo '`$root$benchmark file $f` "$graphtype"' -o $filename$out
	fi
  # take action on each file. $f store current file name
  # cat $f
done

done

done