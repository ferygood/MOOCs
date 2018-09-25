#biomaRt
source("http://www.bioconductor.org/biocLite.R")
biocLite(c("biomaRt"))
#Databases supporting the Biomart interface includes Ensembl (from EBI), HapMap and UniProt
library(biomaRt)
install.packages('stringi')
head(listMarts())
mart <- useMart("ensembl")
mart
head(listDatasets(mart))
ensembl <- useDataset("hsapiens_gene_ensembl", mart)
ensembl

#building a query
values <- c("202763_at", "209310_s_at", "207500_at")
getBM(attributes = c("ensembl_gene_id", "affy_hg_u133_plus_2"), 
      filters = "affy_hg_u133_plus_2", values = values, mart = ensembl)

attributes <- listAttributes(ensembl)
head(attributes)
nrow(attributes)

#R version 3.2.1
#biomaRt_2.24.0
