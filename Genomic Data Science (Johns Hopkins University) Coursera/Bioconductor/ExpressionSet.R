#ExpressionSet
source("http://www.bioconductor.org/biocLite.R")
biocLite(c("Biobase", "ALL", "hgu95av2.db"))

library(ALL)
data(ALL)
ALL
experimentData(ALL)

exprs(ALL)[1:4,1:4]
head(sampleNames(ALL))
head(featureNames(ALL))
head(pData(ALL))
head(pData(ALL)$sex)
head(ALL$sex)

#subsetting
ALL[,1:5]
ALL[1:10,]
ALL[1:10,1:5]
ALL[, c(3,2,1)]
ALL$sex[c(1,2,3)]
ALL[,c(3,2,1)]$sex

#featureData and annotation
featureData(ALL)
ids <- featureNames(ALL)[1:5]
ids
library(hgu95av2.db)
as.list(hgu95av2ENTREZID[ids])

#Note: phenoData and pData
pD <- phenoData(ALL)
varLabels(pD)
varLabels(pD)[2] <- "Age at diagnosis"
pD
colnames(pD)[1:3]
varLabels(pD)[1:3]
