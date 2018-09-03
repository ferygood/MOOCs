#3 GenBank Introduction
#Programming shortcut
from Bio import Entrez

Entrez.email = 'yaochung41@gmail.com'
handle = Entrez.esearch(db='nucleotide',term='"Zea mays"[Organism] AND rbcL[Gene]')
record = Entrez.read(handle)
print record['Count']


#Sample Dataset
genus, start, end = 'Anthoxanthum','2003/7/25','2005/12/27'
term = '"%s"[Organism] AND ("%s"[PDAT] : "%s"[PDAT])' % (genus, start, end)
handle = Entrez.esearch(db="nucleotide", term=term)
print Entrez.read(handle)['Count']


#open downloadfile
genus, start, end = 'Ameiurus','2003/05/07','2008/05/07'
term = '"%s"[Organism] AND ("%s"[PDAT] : "%s"[PDAT])' % (genus, start, end)
handle = Entrez.esearch(db="nucleotide", term=term)
print Entrez.read(handle)['Count']
