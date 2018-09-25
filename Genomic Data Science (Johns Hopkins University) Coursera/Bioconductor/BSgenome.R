library(BSgenome)
available.genomes()
installed.genomes()
biocLite("BSgenome.Scerevisiae.UCSC.sacCer2")

library('BSgenome.Scerevisiae.UCSC.sacCer2')
Scerevisiae
seqnames(Scerevisiae)
seqlengths(Scerevisiae)
Scerevisiae$chrI
letterFrequency(Scerevisiae$chrI, "GC")
letterFrequency(Scerevisiae$chrI, "GC", as.prob=TRUE)
param = new("BSParams", X=Scerevisiae, FUN = letterFrequency)
bsapply(param, "GC")
sum(unlist(bsapply(param,"GC"))) / sum(seqlengths(Scerevisiae))
unlist(bsapply(param, "GC", as.prob = TRUE))
