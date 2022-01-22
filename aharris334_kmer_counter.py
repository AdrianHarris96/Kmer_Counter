#! /usr/bin/env python3

import sys

filename = sys.argv[2]
k = int(sys.argv[1])
#Order: <aharris334_kmer_counter.py> <kmer-length> <fasta_file>

seqString = ""
file_handle = open(filename, "r")
for line in file_handle:
  if ">" in line:
    pass
  else:
    line = line.strip()
    seqString += line
#Skips line with ">"
#Strip whitespace from the line and add to this growing string  - Loading into working memory will not be ideal for larger fasta files

count = 0
kmerDict = {}
for x in range(count, int(len(seqString))):
  if k+count <= len(seqString) and len(seqString[count:k+count]) == k:
    key = seqString[count:k+count]
    if key in kmerDict.keys():
      kmerDict[key] += 1
    else:
      kmerDict[key] = 1
  count += 1
#Progressively move through the long string (by incrementing count) until reaching the end. 
#Initial "if" checks that we have not reached the end of the string. If we have, the loop stops.
#If the key is there, increment with each find of it. Otherwise, give it a value of 1. 

for key in sorted(kmerDict):
  print(key, kmerDict[key], sep="\t")
#Simply prints the key, value pair, separated by tabs