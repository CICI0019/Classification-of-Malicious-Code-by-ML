import pefile
import os, string, shutil, re
import sys
import csv

path = sys.argv[1]
pf = pefile.PE(path)
imports = []

##Check how many bit is contains in the file
if hex(pf.FILE_HEADER.Machine) == '0x14c':
    print("This is a 32-bit binary")
else:
    print("This is a 64-bit binary")

print("\n")

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
imports.append([entry.dll.decode('utf-8'),function.name.decode('utf-8'),section.Name.decode(),section.Misc_VirtualSize,section.SizeOfRawData,str(pf.DOS_HEADER.e_magic),str(pf.DOS_HEADER.e_cblp),str(pf.DOS_HEADER.e_cp),str(pf.DOS_HEADER.e_crlc),str(pf.DOS_HEADER.e_cparhdr),str(pf.DOS_HEADER.e_minalloc),str(pf.DOS_HEADER.e_maxalloc),str(pf.DOS_HEADER.e_ss),str(pf.DOS_HEADER.e_sp),str(pf.DOS_HEADER.e_csum),str(pf.DOS_HEADER.e_ip),str(pf.DOS_HEADER.e_cs),str(pf.DOS_HEADER.e_lfarlc),str(pf.DOS_HEADER.e_ovno),str(pf.DOS_HEADER.e_oemid),str(pf.DOS_HEADER.e_oeminfo),str(pf.DOS_HEADER.e_lfanew),str(pf.NT_HEADERS.Signature),str(pf.FILE_HEADER.Machine),str(pf.FILE_HEADER.NumberOfSections),str(pf.FILE_HEADER.TimeDateStamp),str(pf.FILE_HEADER.PointerToSymbolTable),str(pf.FILE_HEADER.NumberOfSymbols),str(pf.OPTIONAL_HEADER.Magic),str(pf.OPTIONAL_HEADER.DllCharacteristics),str(pf.OPTIONAL_HEADER.ImageBase),str(pf.OPTIONAL_HEADER.SectionAlignment),str(pf.OPTIONAL_HEADER.FileAlignment),str(pf.OPTIONAL_HEADER.SizeOfImage)])

with open('output.csv', 'a+',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['DLL Name', 'Import Name', 'File Name', 'Misc Size', 'Data Size', 'e_magic','e_cblp','e_cp','e_crlc','e_cparhdr','e_minalloc','e_maxalloc','e_ss','e_sp','e_csum','e_ip','e_cs','e_lfarlc','e_ovno','e_oemid','e_oeminfo','e_lfanew','Signature','Machine','NumberOfSection','TimeDateStamp','PointerToSymbols','NumberOfSymbols','Magic','Characteristics','ImageBase','SectionAlignment','FileAlignment','SizeOfImage'])
    for row in imports:
       writer.writerow(row)

print("\n")
