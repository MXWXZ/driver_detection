cd imgs
mkdir val
cd train
for i in `ls -d */`
do
    mkdir ../val/$i
    cd $i
    number=`echo "scale=0; $(ls -l|grep "^-"| wc -l) / 5" |bc`
    for j in `ls|head -n $number`
    do
        mv $j ../../val/$i
    done
    cd ..
done
