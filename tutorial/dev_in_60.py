#! /usr/bin/env python

# open the file to add data
with open('dev_in_60_sample.txt', 'a') as f:
    
    # write a line to the file
    f.write('Hello World!\n')

# open the file to read to contents
with open('dev_in_60_sample.txt', 'r') as f:

    # iterate over the file lines
    for line in f:
        print line
