#Introduction to Protein Databases
#A central repository for protein data is UniProt
#UProtKB: 1. Swiss-Prot 2. TrEMBL
#http://www.uniprot.org/uniprot/uniprot_id and obtain data uniprot_id.txt

from Bio import ExPASy
from Bio import SwissProt
#.get_sprot_raw will find a target protein by its ID
handle = ExPASy.get_sprot_raw('B5ZC00')  #you can give several IDs separated by commas
record = SwissProt.read(handle)

#dir() check the list of attributes for the obtained Swiss-Prot record
print dir(record)
print
#To see the list if references to the other databases, we can check the .cross_references attribute of our record
print record.cross_references[0]
print

#Sample Dataset
pro_handle = ExPASy.get_sprot_raw('Q5SLP9')
pro_record = SwissProt.read(pro_handle)
pro_ref = pro_record.cross_references

GO_list = []
GO_process_list = []
for i in pro_ref:
    if 'GO' in i:
        GO_list.append(i)
        
for j in GO_list:
    for k in j:
        if k[0]== 'P':
            GO_process_list.append(k[2:])
for item in GO_process_list:
    print item
    
#Download Dataset
pro_handle = ExPASy.get_sprot_raw('P79987')
pro_record = SwissProt.read(pro_handle)
pro_ref = pro_record.cross_references

GO_list = []
GO_process_list = []
for i in pro_ref:
    if 'GO' in i:
        GO_list.append(i)
        
for j in GO_list:
    for k in j:
        if k[0]== 'P':                     #'P' for process
            GO_process_list.append(k[2:])  # [2:] all the description after letter P
for item in GO_process_list:
    print item
