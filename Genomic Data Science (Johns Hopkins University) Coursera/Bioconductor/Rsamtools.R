biocLite("Rsamtools")
library(Rsamtools)
# The Rsamtools packages contains functionality for reading and examing aligned reads in the BAM format

#Setup a BAMfile object:
bamPath <- system.file("extdata", "ex1.bam", package="Rsamtools")
bamFile <- BamFile(bamPath)
bamFile

#Access high-level information
seqinfo(bamFile)

aln <- scanBam(bamFile)
length(aln)
class(aln)
aln <- aln[[1]]
names(aln)
lapply(aln, function(xx) xx[1])

#Reading in parts of the file
yieldSize(bamFile) <- 1
open(bamFile)
scanBam(bamFile)[[1]]$seq
#Cleanup
close(bamFile)
yieldSize(bamFile) <- NA

gr <- GRanges(seqnames = "seq2",
              ranges = IRanges(start = c(100, 1000), end = c(1500,2000)))
params <- ScanBamParam(which = gr, what = scanBamWhat())
aln <- scanBam(bamFile, param = params)
names(aln)
head(aln[[1]]$pos)

#BAM summary
quickBamFlagSummary(bamFile)

#Other functionality from Rsamtools
#BamViews
bamView <- BamViews(bamPath)
aln <- scanBam(bamView)
names(aln)

bamRanges(bamView) <- gr
aln <- scanBam(bamView)
names(aln)

names(aln[[1]])

# R version 3.2.1
# Rsamtools_1.20.4