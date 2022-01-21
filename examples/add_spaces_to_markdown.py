#!/usr/bin/python3

# should be read as arguments from the command line
input = './inputFile.md'
output = './outputFile.md'

print(f"Reading from {input} ...")
with open(input) as ifile:
    content = ifile.readlines()

print(f"Processing content ...")
#
# for each line in the content, strip the existing newline character, 
#   add two spaces, add a newline character back, and add the new 
#   content to an array to be written to the new file
#
output_list = []  # will hold modified content to be written
for line in content:
    output_list.append(line.rstrip() + '  ' + '\n')

print(f"Writing modified content to {output} ...")
with open(output, 'w') as ofile:
    ofile.writelines(output_list)

print(f"Complete!")
