source("http://www.bioconductor.org/biocLite.R")
biocLite(c("GenomicRanges"))
library(GenomicRanges)

gr1 <- GRanges(seqnames = "chr1", ranges = IRanges(start = 1:4, width = 3))
gr2 <- GRanges(seqnames = "chr2", ranges = IRanges(start = 1:4, width = 3))
gL <- GRangesList(gr1 = gr1, gr2 = gr2)
gL
start(gL)
seqnames(gL)
elementMetadata(gL)
#elementLengths(gL) could not work
shift(gL,10)
findOverlaps(gL,gr2)

#there are many other types of XXList, including: RleList, IRangesList, IntegerList, CharacterList, LogicalList
