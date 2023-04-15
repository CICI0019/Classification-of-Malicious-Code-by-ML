import pefile
import os, string, shutil, re
import sys
import csv

path = sys.argv[1]
pf = pefile.PE(path)
imports = []

print("----------------------------------\n")
print("|Comprehensive analysis of Pefile|\n")
print("----------------------------------\n")

##print("Section\t\tBase_Address\t\tMax_Size\t\tData_Size")
for section in pf.sections:
          ##print(section.Name, "\t\t", hex(section.VirtualAddress),"\t\t", hex(section.Misc_VirtualSize), "\t\t", section.SizeOfRawData)
            print(section)

print("\n")
print("--------------------------------------------------\n")
print("| Export the API functions from the file program |\n")
print("--------------------------------------------------\n")

for entry in pf.DIRECTORY_ENTRY_IMPORT:
    print(entry.dll)
    for function in entry.imports:
        print("\t", function.name)
imports.append([entry.dll.decode('utf-8'),function.name.decode('utf-8')])

with open('output.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['DLL Name', 'Import Name'])
    for row in imports:
        writer.writerow(row)

print("\n")