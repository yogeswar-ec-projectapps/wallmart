hello welcome to DevOps

echo "Please enter file name:

read filename

if [ -r $filename ]
then
echo "$filename have read permission"
elif [ -w $filename ]
then
echo "$filename have write permissin"
elif [ -e $filename ]
then
echo "$file have execution permission"
else
echo "please enter file present in shell directory"
fi

