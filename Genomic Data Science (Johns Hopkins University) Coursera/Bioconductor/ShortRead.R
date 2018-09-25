#ShortRead
biocLite(c("ShortRead"))
library(ShortRead)

#ShortRead package contains functionality for reading and examing raw sequence reads (typically in FASTQ format)
#Reading FASTQ files
fastqDir <- system.file("extdata", "E-MTAB-1147", package = "ShortRead")
fastqPath <- list.files(fastqDir, pattern = ".fastq.gz$", full = TRUE)[1]
reads <- readFastq(fastqPath)
reads

fqFile <- FastqFile(fastqPath)
fqFile
reads <- readFastq(fqFile)
sread(reads)[1:2]
quality(reads)[1:2]
id(reads)[1:2]

#A word on quality scores
as(quality(reads), "matrix")[1:2,1:10]

#R version 3.2.1
#ShortRead_1.26.0
#Rsamtools_1.20.4
