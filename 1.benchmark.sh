#!/bin/bash
benchmark=$1
# graphtype=$2
# echo $benchmark
root="/Users/zhijiaoliu/Documents/Github/graphchi-cpp/"
dir="/Users/zhijiaoliu/Documents/NetworkData/wiki-Talk"
cd $dir
# for f in *.txt
# do 
# echo "Processing $f file.."
# echo $(pwd)
# done

out="-$benchmark.800.0.stdout"
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