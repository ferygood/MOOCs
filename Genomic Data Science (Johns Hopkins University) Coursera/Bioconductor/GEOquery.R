#GEOquery
biocLite(c("GEOquery"))
library(GEOquery)
eList <- getGEO("GSE11675")
class(eList)
length(eList)
names(eList)
eData <- eList[[1]]
eData

names(pData(eData))
eList2 <- getGEOSuppFiles("GSE11675")
eList2

tarArchive <- rownames(eList2)[1]
tarArchive

#R version 3.2.1
# GEOquery_2.34.0