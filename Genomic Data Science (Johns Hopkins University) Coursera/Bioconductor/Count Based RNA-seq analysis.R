#Count Based NRA-seq analysis
biocLite(c("DESeq2", "edgeR"))
#count_based models built on the negative binomial distribution, edgeR, DESeq, DESeq2
#The Data
library(airway)
data(airway)
airway

assay(airway, "counts")[1:3,1:3]
airway$dex
airway$dex <- relevel(airway$dex, "untrt")
airway$dex

#information about which gene model was used for each gene:
granges(airway)

#edgeR
library(edgeR)
dge <- DGEList(counts = assay(airway, "counts"),
               group = airway$dex)
dge$samples <- merge(dge$samples,
                     as.data.frame(colData(airway)),
                     by = 0)
dge$genes <- data.frame(name = names(rowRanges(airway)),
                        stringsAsFactors = FALSE)
dge <- calcNormFactors(dge)
design <- model.matrix(~dge$samples$group)
dge <- estimateGLMCommonDisp(dge, design)
dge <- estimateGLMTagwiseDisp(dge, design)
fit <- glmFit(dge, design)
lrt <- glmLRT(fit, coef = 2)
topTags(lrt)

#DESeq2
install.packages('stringi')
library(DESeq2)
dds <- DESeqDataSet(airway, design = ~dex)
dds <- DESeq(dds)
res <- results(dds)
res <- res[order(res$padj),]
res

#R version 3.2.1
#edgeR_3.10.2
#DESeq2_1.8.1