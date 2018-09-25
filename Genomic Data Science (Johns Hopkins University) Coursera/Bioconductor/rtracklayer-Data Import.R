#rtracklayer - Data Import
source("http://www.bioconductor.org/biocLite.R")
biocLite(c("rtracklayer", "AnnotationHub", "Rsamtools"))
library(rtracklayer)
library(AnnotationHub)
#Rsamtools is not available for R version 3.5.1
install.packages('Rsamtools')
library(Rsamtools)

#Extensive example
ahub <- AnnotationHub()
table(ahub$rdataclass)
ahub.gr <- subset(ahub, rdataclass == "GRanges" & species == "Homo sapiens")
gr <- ahub.gr[[1]]
gr
seqinfo(gr)
ahub.bw <- subset(ahub, rdataclass == "BigWigFile" & species == "Homo sapiens")
ahub.bw
bw <- ahub.bw[[1]]
bw
gr1 <- gr[1:3]
out.gr <- import(bw, which = gr1)
out.gr
out.rle <- import(bw, which = gr1, as = "Rle")
out.rle

gr.chr22 <- GRanges(seqnames = "chr22",
                    ranges = IRanges(start = 1, end = seqlengths(gr)["chr22"]))
out.chr22 <- import(bw, which = gr.chr22, as = "Rle")
out.chr22[["chr22"]]

#LiftOver
ahub.chain <- subset(ahub, rdataclass == "ChainFile" & species == "Homo sapiens")
query(ahub.chain, c("hg18", "hg19"))
chain <- ahub.chain[ahub.chain$title == "hg19ToHg18.over.chain.gz"]
chain <- chain[[1]]
gr.hg18 <- liftOver(gr, chain)
gr.hg18
table(elementLengths(gr.hg18))

#Importing directly from UCSC, Tabix indexing
library(Rsamtools)
from <- system.file("extdata", "ex1.sam", package="Rsamtools",
                    mustWork=TRUE)
from

to <- tempfile()
zipped <- bgzip(from, to)
idx <- indexTabix(zipped, "sam")

#R version 3.2.1
#Rsamtools_1.20.4
#AnnotationHub_2.0.3
#rtracklayer_1.28.8