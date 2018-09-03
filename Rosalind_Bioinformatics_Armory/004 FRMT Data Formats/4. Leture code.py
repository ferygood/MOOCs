#4 Data Formats lecture
#Bio.Entrez.efetch(db, rettype), db database, rettype takes the data format to be returned
#Programming shortcut
from Bio import Entrez
Entrez.email = 'yaochung41@gmail.com'
handle = Entrez.efetch(db='nucleotide', id=["FJ817486", "JX069768", "JX469983"], 
                       rettype='fasta')
records = handle.read()
print records
print 

#To work with FASTA format, we use Bio.SeqIO
#Bio.SeqIO.parse() takes a handle and format name as parameters and returns entries as SeqRecords.
from Bio import SeqIO
from Bio import Entrez
Entrez.email = 'yaochung41@gmail.com'
handle = Entrez.efetch(db='nucleotide', id=["FJ817486", "JX069768", "JX469983"], 
                       rettype='fasta')
records = list(SeqIO.parse(handle,'fasta'))  #we get the list of SeqIO objects in FASTA format
print records
print records[0].id
print len(records[-1].seq)
