source("http://www.bioconductor.org/biocLite.R")
biocLite(c("GenomicRanges", "airway"))

library(airway)
data(airway)
airway
colData(airway)
airway$cell
exptData(airway)
colnames(airway)
head(rownames(airway))
airway
assayNames(airway)
assays(airway)
head(assay(airway, "counts"))
length(rowRanges(airway))
dim(airway)
rowRanges(airway)
length(rowRanges(airway))
start

gr <- GRanges(seqnames = "1", ranges = IRanges(start = 1, end = 10^7))
subsetByOverlaps(airway, gr)
