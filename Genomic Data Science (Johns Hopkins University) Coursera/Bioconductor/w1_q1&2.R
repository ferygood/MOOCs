#Bioconductor for Genomic Data Science W1 Quiz
source("http://www.bioconductor.org/biocLite.R")
biocLite(c("GenomicRanges", "rtracklayer","AnnotationHub"))

library(GenomicRanges)
library(rtracklayer)
library(AnnotationHub)

#create an Annotation object
ah <- AnnotationHub()

#exam data on CpG Islands in the human genome (hg19)
CpG_islands <- query(ah, c("CpG Islands", "hg19"))
CpG_data <- CpG_islands[["AH5086"]]
CpG_data


#summary info about CpG island dataset
summary(width(CpG_data))
seqinfo(CpG_data)
seqlevels(CpG_data)
gaps(CpG_data)

#reduce data size
CpG_reduce <- reduce(CpG_data)

#count number of CpG islands in autochromosome
autosome <- c(paste("chr", 1:22, sep=''))
split_data_by_chr <- split(CpG_reduce, seqnames(CpG_reduce))
autosome_cpg_data <- split_data_by_chr[autosome]
seqlevels(autosome_cpg_data)
autosome_cpg_data

#CpG Islands on autosome
unlist(autosome_cpg_data)

#CpG Islands on chr4
autosome_cpg_data[4]

#Q3
ah_H3K4me <- query(ah, c("H3K4me3", "E003"))
ah_H3K4me_data <- ah_H3K4me[["AH29884"]]
seqinfo(ah_H3K4me_data)
seqlevels(ah_H3K4me_data)
#subset autosome data
ah_H3K4me_autosome_data <- subset(ah_H3K4me_data, seqnames %in% autosome)
# count base pairs
sum(width(unlist(ah_H3K4me_autosome_data)))