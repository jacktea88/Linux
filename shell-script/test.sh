echo  myname  is  $USER
echo  what  is  your  name?
read  name
echo  Hi,  $name,  how  do  you  do?
if [ $name == "mary" ]; then
echo hello,$name~~
elif [ $name == "kevin" ]; then
echo yo,$name,where is my bike?
else
echo who are you !!
fi

