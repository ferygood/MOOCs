'''
Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output
MAMAPRTEINSTRING
'''

from Bio.Seq import Seq
from Bio.Alphabet import generic_rna
messenger_rna = Seq('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA',generic_rna)
protein = messenger_rna.translate()

print protein

#open with file
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna
rna_seq = open(r'').read()
m_rna = Seq(rna_seq,generic_rna)
pro = m_rna.translate()

print pro
