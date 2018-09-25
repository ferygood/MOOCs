#BSgenome - Views
source("http://www.bioconductor.org/biocLite.R")
biocLite(c("BSgenome","BSgenome.Scerevisiae.UCSC.sacCer2", "AnnotationHub"))
library(BSgenome)
library(BSgenome.Scerevisiae.UCSC.sacCer2)
library(AnnotationHub)

dnaseq <- DNAString("ACGTACGT")
vi <- matchPattern(dnaseq, Scerevisiae$chrI)
vi
#get the IRanges component by ranges
ranges(vi)

Scerevisiae$chrI[start(vi):end(vi)]
alphabetFrequency(vi)
#get the sequence 10 bases next to the original match
shift(vi,10)

gr <- vmatchPattern(dnaseq, Scerevisiae)
vi2 <- Views(Scerevisiae, gr)
ahub <- AnnotationHub()
qh <- query(ahub, c("sacCer2", "genes"))
qh

genes <- qh[[which(qh$title == "SGD Genes")]]
genes

#Compute the GC content
prom <- promoters(genes)
head(prom, n=3)
#clean it up
prom <- trim(prom)
promViews <- Views(Scerevisiae, prom)
gcProm <- letterFrequency(promViews, "GC", as.prob = TRUE)
head(gcProm)

params <- new("BSParams", X=Scerevisiae, FUN = letterFrequency, simplify = TRUE)
gccontent <- bsapply(params, letters="GC")
gcPercentage <- sum(gccontent) / sum(seqlengths(Scerevisiae))
gcPercentage

plot(density(gcProm))
abline(v = gcPercentage, col='red')
