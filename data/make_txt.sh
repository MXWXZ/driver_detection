cd imgs
cd train
for i in `ls -d */`
do
    cd $i
    for j in `ls`
    do
        echo "`pwd`/$j ${i:0-2:1}" >> ../../../train.txt
    done
    cd ..
done
cd ..
cd val
for i in `ls -d */`
do
    cd $i
    for j in `ls`
    do
        echo "`pwd`/$j ${i:0-2:1}" >> ../../../val.txt
    done
    cd ..
done