#14. Translating RNA into Protein
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna
rna_seq = open(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_prot.txt','r').read()
m_rna = Seq(rna_seq,generic_rna)
protein = m_rna.translate()

print protein
