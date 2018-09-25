biocLite(c("limma", "leukemiasEset"))
library(limma)
library(leukemiasEset)

#limma = linear models for microarray data, is a very popular package for analyzing microarray and RNA-seq data
data(leukemiasEset)
leukemiasEset
table(leukemiasEset$LeukemiaType)
ourData <- leukemiasEset[, leukemiasEset$LeukemiaType %in% c("ALL", "NoL")]
ourData$LeukemiaType <- factor(ourData$LeukemiaType)

#linear model
design <- model.matrix(~ourData$LeukemiaType)
fit <- lmFit(ourData, design)
fit <- eBayes(fit)
topTable(fit)

ourData$LeukemiaType
topTable(fit, n = 1)
genename <- rownames(topTable(fit, n=1))
typeMean <- tapply(exprs(ourData)[genename,], ourData$LeukemiaType, mean)
typeMean
typeMean["NoL"] - typeMean["ALL"]

#More on the design
design <- model.matrix(~ ourData$LeukemiaType)
head(design)
design2 <- model.matrix(~ ourData$LeukemiaType - 1)
head(design2)
colnames(design2) <- c("ALL", "NoL")
fit2 <- lmFit(ourData, design2)
contrast.matrix <- makeContrasts("ALL-NoL", levels = design2)
contrast.matrix

fit2C <- contrasts.fit(fit2, contrast.matrix)
fit2C <- eBayes(fit2C)
topTable(fit2C)

#R version 3.2.1 
#limma_3.24.15
#leukemiasEset_1.4.0
