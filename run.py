#!/usr/bin/python3
import os
import sys

'''
r1filename="testcase_R1.fastq"
r2filename="testcase_R2.fastq"
'''
r1filename="2834-MM-1_S1_L001_R1_001.fastq"
r2filename="2834-MM-1_S1_L001_R2_001.fastq"

fd1 = open(r1filename, 'r')
fd2 = open(r2filename, 'r')

counts = {}

seen = {}

fnamelist = []

filenumber = 0 

destinationFileIdList = []

nestedList = []

tmp = fd1.readline()

# for i in range(0,10000000000000000000000000000):
for i in range(0,100000000000000000000000000000):
	#if i % 10000000 == 0:
		#sys.stderr.write(str(i/10000000)+'\n')

	tmp = fd1.readline().rstrip()

	if tmp == "":
		break

	#print(tmp[0:10])

	if tmp[0:10] in seen.keys():
		destinationFileIdList.append(seen[tmp[0:10]])
		counts[tmp[0:10]] += 1

	else:
		seen[tmp[0:10]]=filenumber
		fnamelist.append(tmp[0:10])
		counts[tmp[0:10]] = 1
		destinationFileIdList.append(filenumber)
		nestedList.append([])
		nestedList[-1]=filenumber
		filenumber+=1

	fd1.readline()
	fd1.readline()
	fd1.readline()

# skip this version in production

fileDescriptors = []

for thing in seen.keys():
	# fileDescriptors.append(-1)
	os.mkdir('./outputFastqs/'+thing)

	# if counts[thing] > 69363:
	# fileDescriptors[seen[thing]] = open('./outputFastqs/'+thing+'/'+thing+".fastq", "w")

	# print(counts[thing])

trash = open("/dev/null", 'w')
	
# for basename in fnamelist:


#these changes will cause it to run very slow but it will at least get the job done.
for i in range(0, 10000000000000000000000000):
	#if fileDescriptors[destinationFileIdList[i]]:

	if counts[fnamelist[nestedList[i]]] > 10000:


		fd = open('./outputFastqs/'+fnamelist[nestedList[i]]+'/'+fnamelist[nestedList[i]], "a+")
		#else:
		#	fd = trash

		tmp = fd2.readline()

		if tmp == "":
			break

		fd.write(tmp)
		fd.write(fd2.readline())
		fd.write(fd2.readline())
		fd.write(fd2.readline())

		fd.close()



