#The oligo package
biocLite(c("oligo", "GEOquery"))
library(oligo)
library(GEOquery)
#oligo package handles Affymetrix and Nimblegen microarrays, especially gene expression, exon expression and SNP arrays

#Getting the data
getGEOSuppFiles("GSE38792")
list.files("GSE38792")
untar("GSE38792/GSE38792_RAW.tar", exdir = "GSE38792/CEL")
list.files("GSE38792/CEL")

#construct a vector of filenames and feed it to read.celfiles()
celfiles <- list.files("GSE38792/CEL", full=TRUE)
rawData <- read.celfiles(celfiles)
rawData
getClass("GeneFeatureSet")
exprs(rawData)[1:4,1:3]
max(exprs(rawData))

filename <- sampleNames(rawData)
pData(rawData)$filename <- filename
sampleNames <- sub(".*_", "", filename)
sampleNames <- sub(".CEL.gz$", "", sampleNames)
sampleNames(rawData) <- sampleNames
pData(rawData)$group <- ifelse(grepl("^OSA", sampleNames(rawData)),
                               "OSA", "Control")
pData(rawData)

#Normalization
boxplot(rawData)

normData <- rma(rawData)
normData
boxplot(normData)

#R version 3.2.1
#GEOquery_2.34.0
#oligoClasses_1.30.0