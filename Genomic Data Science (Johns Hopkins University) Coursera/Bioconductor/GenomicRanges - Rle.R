#GenomicRanges - Rle
source("http://www.bioconductor.org/biocLite.R")
biocLite(c("GenomicRanges"))
library(GenomicRanges)

#a file format which is often used to represent coverage data is Wig or the modern version BigWig
#Rle (run-length-encoded)
rl <- Rle(c(1,1,1,1,2,2,3,3,2,2))
rl
runLength(rl)
runValue(rl)
as.numeric(rl)

ir <- IRanges(start = c(2,6), width = 2)
ir
aggregate(rl, ir, FUN = mean)

ir <- IRanges(start = 1:10, width = 3)
rl <- coverage(ir)
rl

#select high coverage regions by the slice() function
slice(rl,2)

#Views and Rles
vi <- Views(rl, start=c(3,7), width=3)
vi
mean(vi)

#Rles and GRanges
gr <- GRanges(seqnames = "chr1", ranges = IRanges(start = 1:10, width = 3))
rl <- coverage(gr)
rl

grView <- GRanges("chr1", ranges = IRanges(start = 2, end = 7))
vi <- Views(rl, grView)
vi <- Views(rl, as(grView, "RangesList"))
vi
vi[[1]]

