#4 Data Formats
# Sample Dataset FJ817486 JX069768 JX469983
from Bio import SeqIO, Entrez
Entrez.email = 'yaochung41@gmail.com'
handle = Entrez.efetch(db='nucleotide', id=["FJ817486", "JX069768", "JX469983"], 
                       rettype='fasta')

records = SeqIO.parse(handle,'fasta')  #we get the list of SeqIO objects in FASTA format

print min(records, key=lambda s: len(s.seq)).format('fasta')
