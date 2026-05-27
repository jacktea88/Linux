for n in `ls`
do
	if `test -d $n`; then
		echo $n
	fi
done

