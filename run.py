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

	if "N" in tmp[0:10]: 
		print("skipping")
		continue

	if tmp[0:10] in seen.keys():
		destinationFileIdList.append(seen[tmp[0:10]])
		counts[tmp[0:10]] += 1
		outputFile = "./outputFastqs/" + tmp[0:10] + ".fastq"

	else:
		outputFile = "./outputFastqs/" + tmp[0:10] + ".fastq"
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

	
	fd3 = open(outputFile, "a+")

	fd3.write(fd2.readline())
	fd3.write(fd2.readline())
	fd3.write(fd2.readline())
	fd3.write(fd2.readline())

	fd3.close()



#these changes will cause it to run very slow but it will at least get the job done.
#for i in range(0, 10000000000000000000000000):

#	if counts[fnamelist[nestedList[i]]] > 10000:
 
#		os.mkdir('./outputFastqs/'+fnamelist[nestedList[i])
#		fd = open('./outputFastqs/'+fnamelist[nestedList[i]]+'/'+fnamelist[nestedList[i]], "a+")
#		#else:
#		#	fd = trash

#		tmp = fd2.readline()

#		if tmp == "":
#			break

#		fd.write(tmp)
#		fd.write(fd2.readline())
#		fd.write(fd2.readline())
#		fd.write(fd2.readline())

#		fd.close()


