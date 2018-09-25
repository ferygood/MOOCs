#Biostrings - Matching
source("http://www.bioconductor.org/biocLite.R")
biocLite(c("Biostrings", "BSgenome", "BSgenome.Scerevisiae.UCSC.sacCer2", "AnnotationHub"))
library(Biostrings)
library(BSgenome)
library(BSgenome.Scerevisiae.UCSC.sacCer2)

#matchPattern, vmatchPattern, matchPDict, vmatchPDict
dnaseq <- DNAString("ACGTACGT")
matchPattern(dnaseq, Scerevisiae$chrI)
countPattern(dnaseq, Scerevisiae$chrI)
vmatchPattern(dnaseq, Scerevisiae)
head(vcountPattern(dnaseq, Scerevisiae))
dnaseq == reverseComplement(dnaseq)

#matchPWM, pairwiseAlignment, trimLRpattern