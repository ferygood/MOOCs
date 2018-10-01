#Exploratory analysis
install.packages(c("devtools", "gplots"))
install.packages("remotes")
source("http://www.bioconductor.org/biocLite.R")
biocLite(c("Biobase","org.Hs.eg.db", "AnnotationDbi"))
biocLite("alyssafrazee/RSkittleBrewer")

library(gplots)
library(devtools)
library(Biobase)

library(org.Hs.eg.db)
library(AnnotationDbi)

#make the plot pretty
library(RSkittleBrewer)
trop = RSkittleBrewer("tropical")
palette(trop)
par(pch=19)

#Load some data
con = url("http://bowtie-bio.sourceforge.net/recount/ExpressionSets/bodymap_eset.RData")
load(file=con)
close(con)
bm = bodymap.eset
pdata = pData(bm)
edata = exprs(bm)
fdata = fData(bm)
ls()

#Tables for factor/character variables
table(pdata$gender)
table(pdata$gender, pdata$race)

#Looking for missing values
#First check a summary of the distribution to look for scale, this is also one way to check for NA values
summary(edata)
#use option useNA to include NA's in table
table(pdata$age, useNA='ifany')
#is.na checks for NA values
table(is.na(pdata$age))
#Check genomic data for NAs
sum(is.na(edata))
#make the distribution of NA's by genes
gene_na = rowSums(is.na(edata))
table(gene_na)
#make the distribution of NA's by samples
sample_na = rowSums(is.na(edata))
table(sample_na)

#Make sure dimensions match up
dim(fdata)
dim(pdata)
dim(edata)

#Look at overall distributions
boxplot(log2(edata+1), col=2, range=0)

#look at this sample by sample with histograms
par(mfrow=c(1,2))
hist(log2(edata[,1]+1),col=2)
hist(log2(edata[,2]+1),col=2)

#density plot
plot(density(log2(edata[,1]+1)), col=2)
lines(density(log2(edata[,2]+1)),col=3)

#compare distributions of measurements with qq-plot
qqplot(log2(edata[,1]+1), log2(edata[,2]+1),col=3)

#M-A plot
mm = log2(edata[,1]+1) - log2(edata[,2]+1)
aa = log2(edata[,1]+1) + log2(edata[,2]+1)
plot(aa,mm,col=2)

#remoce rows that are mostly zero and notice any differneces in the distributions across samples
edata = as.data.frame(edata)
filt_edata = filter(edata, rowMeans(edata)>1)
boxplot(as.matrix(log2(filt_edata+1)), col=2)


#check for obvious data mixups
aeid = as.character(fdata[,1])
chr = AnnotationDbi::select(org.Hs.eg.db, keys=aeid, keytype='ENSEMBL', columns='CHR')
dim(chr)
dim(edata)
# Take non-duplicated chromosomes
chr = chr[!duplicated(chr[,1]),]
#Confirm that the annotation still is in the right order
all(chr[,1] == rownames(edata))
#Select the chromosome Y samples
edatay = dplyr::filter(edata, chr$CHR=="Y")
# Males have Y chromosome expression as expected
boxplot(colSums(edatay)~pdata$gender)
points(colSums(edatay)~jitter(as.numeric(pdata$gender)), col=as.numeric(pdata$gender), pch=19)

#Heatmaps
ematrix = as.matrix(edata)[rowMeans(edata) > 10000,]
heatmap(ematrix)
#change a more visible color
colramp = colorRampPalette(c(3,"white",2))(9)
heatmap(ematrix,col=colramp)
#Turn off automatic clustering 
heatmap(ematrix, col=colramp, Rowv = NA, Colv=NA)
heatmap.2(ematrix, col=colramp, Rowv=NA, Colv=NA, dendrogram='none', scale='row', trace='none')

session_info()
# Session info --------------------------------------------------------------------------
#   setting  value                           
# version  R version 3.5.1 (2018-07-02)    
# system   x86_64, mingw32                 
# ui       RStudio (1.1.453)               
# language (EN)                            
# collate  Chinese (Traditional)_Taiwan.950
# tz       Asia/Taipei                     
# date     2018-10-01                      
# 
# Packages ------------------------------------------------------------------------------
#   package              * version   date       source        
# affyio                 1.50.0    2018-05-01 Bioconductor  
# AnnotationDbi          1.42.1    2018-05-08 Bioconductor  
# assertthat             0.2.0     2017-04-11 CRAN (R 3.5.1)
# base                 * 3.5.1     2018-07-02 local         
# bindr                  0.1.1     2018-03-13 CRAN (R 3.5.1)
# bindrcpp               0.2.2     2018-03-29 CRAN (R 3.5.1)
# Biobase              * 2.40.0    2018-05-01 Bioconductor  
# BiocGenerics         * 0.26.0    2018-05-01 Bioconductor  
# BiocInstaller          1.30.0    2018-05-01 Bioconductor  
# BiocParallel         * 1.14.2    2018-07-09 Bioconductor  
# Biostrings           * 2.48.0    2018-05-01 Bioconductor  
# bit                    1.1-14    2018-05-29 CRAN (R 3.5.0)
# bit64                  0.9-7     2017-05-08 CRAN (R 3.5.0)
# bitops                 1.0-6     2013-08-17 CRAN (R 3.5.0)
# blob                   1.1.1     2018-03-25 CRAN (R 3.5.1)
# BSgenome             * 1.48.0    2018-05-01 Bioconductor  
# codetools              0.2-15    2016-10-05 CRAN (R 3.5.1)
# compiler               3.5.1     2018-07-02 local         
# crayon                 1.3.4     2017-09-16 CRAN (R 3.5.1)
# datasets             * 3.5.1     2018-07-02 local         
# DBI                    1.0.0     2018-05-02 CRAN (R 3.5.1)
# DelayedArray         * 0.6.6     2018-09-11 Bioconductor  
# devtools             * 1.13.6    2018-06-27 CRAN (R 3.5.1)
# digest                 0.6.17    2018-09-12 CRAN (R 3.5.1)
# dplyr                  0.7.6     2018-06-29 CRAN (R 3.5.1)
# ff                     2.2-14    2018-05-15 CRAN (R 3.5.1)
# foreach              * 1.4.4     2017-12-12 CRAN (R 3.5.1)
# GenomeInfoDb         * 1.16.0    2018-05-01 Bioconductor  
# GenomeInfoDbData       1.1.0     2018-07-17 Bioconductor  
# GenomicAlignments      1.16.0    2018-05-01 Bioconductor  
# GenomicRanges        * 1.32.6    2018-07-20 Bioconductor  
# glue                   1.3.0     2018-07-17 CRAN (R 3.5.1)
# graphics             * 3.5.1     2018-07-02 local         
# grDevices            * 3.5.1     2018-07-02 local         
# grid                   3.5.1     2018-07-02 local         
# hwriter                1.3.2     2014-09-10 CRAN (R 3.5.0)
# IRanges              * 2.14.11   2018-08-24 Bioconductor  
# iterators            * 1.0.10    2018-07-13 CRAN (R 3.5.1)
# lattice                0.20-35   2017-03-25 CRAN (R 3.5.1)
# latticeExtra           0.6-28    2016-02-09 CRAN (R 3.5.1)
# limma                * 3.36.5    2018-09-20 Bioconductor  
# locfit               * 1.5-9.1   2013-04-20 CRAN (R 3.5.1)
# magrittr               1.5       2014-11-22 CRAN (R 3.5.1)
# Matrix                 1.2-14    2018-04-13 CRAN (R 3.5.1)
# matrixStats          * 0.54.0    2018-07-23 CRAN (R 3.5.1)
# memoise                1.1.0     2017-04-21 CRAN (R 3.5.1)
# methods              * 3.5.1     2018-07-02 local         
# oligoClasses         * 1.42.0    2018-05-01 Bioconductor  
# parallel             * 3.5.1     2018-07-02 local         
# pillar                 1.3.0     2018-07-14 CRAN (R 3.5.1)
# pkgconfig              2.0.2     2018-08-16 CRAN (R 3.5.1)
# purrr                  0.2.5     2018-05-29 CRAN (R 3.5.1)
# R6                     2.2.2     2017-06-17 CRAN (R 3.5.1)
# RColorBrewer           1.1-2     2014-12-07 CRAN (R 3.5.0)
# Rcpp                   0.12.18   2018-07-23 CRAN (R 3.5.1)
# RCurl                  1.95-4.11 2018-07-15 CRAN (R 3.5.1)
# registry               0.5       2017-12-03 CRAN (R 3.5.0)
# rlang                  0.2.2     2018-08-16 CRAN (R 3.5.1)
# Rsamtools              1.32.3    2018-08-22 Bioconductor  
# RSQLite                2.1.1     2018-05-06 CRAN (R 3.5.1)
# rstudioapi             0.7       2017-09-07 CRAN (R 3.5.1)
# rtracklayer          * 1.40.6    2018-08-31 Bioconductor  
# S4Vectors            * 0.18.3    2018-06-08 Bioconductor  
# ShortRead              1.38.0    2018-05-01 Bioconductor  
# stats                * 3.5.1     2018-07-02 local         
# stats4               * 3.5.1     2018-07-02 local         
# SummarizedExperiment * 1.10.1    2018-05-11 Bioconductor  
# tibble                 1.4.2     2018-01-22 CRAN (R 3.5.1)
# tidyselect             0.2.4     2018-02-26 CRAN (R 3.5.1)
# tools                  3.5.1     2018-07-02 local         
# utils                * 3.5.1     2018-07-02 local         
# withr                  2.1.2     2018-03-15 CRAN (R 3.5.1)
# XML                    3.98-1.16 2018-08-19 CRAN (R 3.5.1)
# XVector              * 0.20.0    2018-05-01 Bioconductor  
# yaml                   2.2.0     2018-07-25 CRAN (R 3.5.1)
# zlibbioc               1.26.0    2018-05-01 Bioconductor