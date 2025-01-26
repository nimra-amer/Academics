#Q1

#ls : lists all the files in the directory
#cd : takes you into the directory specified by you
#pwd: Displays the path of current working directory
#mkdir: makes an empty directory
#rmdir: remove an empty directory
#rm: removes directories or files
#cp : copies files or directories from one location to another
#mv : moves or renames files/directories
#touch : creates an empty file 

#Q3
#pinged the networks : 127.0.0.1 , google.com , twitter.com , instagram.com , and youtube.com for 5 iterations. The minimum latency rate was of 127.0.0.1 in all the itertions as compared to the other 4.

#Q4
import sys
import struct

byte = sys.byteorder
print("Byte Ordering : " , byte)

hex = 0x3412
pack_little = list(struct.pack('<H', hex))   #H = unsigned short , h - signed short 
pack_big =list(struct.pack('>H' ,hex))
print("Little Endian\n")
print("Data in Packed Form :" , pack_little)
print("0x{0:X} in Un-Packed Form".format(hex))
for byte in pack_little:
    print("{:02X}".format(byte), end=" ")
print('\n')


print("Big Endian\n")
print("Data in Packed Form :" , pack_big)
print("0x{0:X} in Un-Packed Form".format(hex))
for byte in pack_big:
    print("{:02X}".format(byte), end=" ")
print('\n')

