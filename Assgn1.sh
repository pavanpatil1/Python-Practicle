
echo "Create a directory: "
read dname  
mkdir $dname
cd $dname

i='y'
while [ $i = 'y' ]
do

echo "1.Create File"
echo "2.Search File"
echo "3.Delete File"
echo "4.Rename File"
echo "5.View Directory"
echo "6.Exit"
echo "Enter your choice"
read choice

case $choice in
1)
echo "Enter File Name: "
read fname
if [ -f $fname ]
then
echo "fie already exists"

else
touch $fname
echo "file successfully created"
fi;;

2)
echo "Enter file name: "
read fname
if [ -f $fname ]
then
echo "File Found"
else
echo "File does not exists"
fi;;

3)
echo "Enter file name:"
read fname
if [ -f $fname ]
then
rm $fname
else
echo "File does not exists"
fi;;

4)
echo "Enter old file name: "
read old_fname
echo "Enter new file name: "
read new_fname
if [ -f $fname ]
then
mv $old_fname $new_fname
else
echo "File does not exixts"
fi;;

5)
echo "Files in directory" $dname
ls;;

6)
i='n';;
esac
done

OUTPUT:

student@student:~/Desktop$ chmod +x Assgn1.sh
student@student:~/Desktop$ ./Assgn1.sh
Create a directory: 
OS
1.Create File
2.Search File
3.Delete File
4.Rename File
5.View Directory
6.Exit
Enter your choice
1
Enter File Name: 
Process
file successfully created
1.Create File
2.Search File
3.Delete File
4.Rename File
5.View Directory
6.Exit
Enter your choice
1
Enter File Name: 
Thread
file successfully created
1.Create File
2.Search File
3.Delete File
4.Rename File
5.View Directory
6.Exit
Enter your choice
5
Files in directory OS
Process  Thread
1.Create File
2.Search File
3.Delete File
4.Rename File
5.View Directory
6.Exit
Enter your choice
2
Enter file name: 
Thread
File Found
1.Create File
2.Search File
3.Delete File
4.Rename File
5.View Directory
6.Exit
Enter your choice
4
Enter old file name: 
Process
Enter new file name: 
Pr
1.Create File
2.Search File
3.Delete File
4.Rename File
5.View Directory
6.Exit
Enter your choice
3
Enter file name:
Thread
1.Create File
2.Search File
3.Delete File
4.Rename File
5.View Directory
6.Exit
Enter your choice
5
Files in directory OS
Pr
1.Create File
2.Search File
3.Delete File
4.Rename File
5.View Directory
6.Exit
Enter your choice


