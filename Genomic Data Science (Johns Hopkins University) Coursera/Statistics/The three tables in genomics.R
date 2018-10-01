install.packages("devtools")
source("http://www.bioconductor.org/biocLite.R")
biocLite(c("Biobase"))

# Load the data from the web
con = url("http://bowtie-bio.sourceforge.net/recount/ExpressionSets/bodymap_eset.RData")
load(file=con)
close(con)

# An expression set, this kind of object in R contains the three tables
bm = bodymap.eset
bm
#52580 features, 19 samples

# Table 1: the gemoics data
# These are usually high dimensional measurements. In this case it is RNA-seq data. Row-gene, column-sample
exp_data = exprs(bm)
dim(exp_data)
head(exp_data, n=5)

# Table 2: the phenotype data
# This is the 'meta data' or 'phenotype data' that is what you typically associate the genomic data with.
# Column - variable, row - sample
pheno_data = pData(bm)
dim(pheno_data)
# 19 samples, 6 variable
head(pheno_data)

# Table 3: the feature data
# Information about genes or other genomics features. Column - variable, row - gene features
feature_data = fData(bm)
dim(feature_data)
#52580 gene features  1  column
fData(bm)[1:10,,1]

devtools::session_info()
# Session info -------------------------------------------------------------------------------------------
#   setting  value                           
# version  R version 3.5.1 (2018-07-02)    
# system   x86_64, mingw32                 
# ui       RStudio (1.1.453)               
# language (EN)                            
# collate  Chinese (Traditional)_Taiwan.950
# tz       Asia/Taipei                     
# date     2018-10-01                      
# 
# Packages -----------------------------------------------------------------------------------------------
#   package                * version   date       source        
# acepack                  1.4.1     2016-10-29 CRAN (R 3.5.1)
# affyio                   1.50.0    2018-05-01 Bioconductor  
# AnnotationDbi          * 1.42.1    2018-05-08 Bioconductor  
# AnnotationHub          * 2.12.1    2018-09-05 Bioconductor  
# assertthat               0.2.0     2017-04-11 CRAN (R 3.5.1)
# backports                1.1.2     2017-12-13 CRAN (R 3.5.0)
# base                   * 3.5.1     2018-07-02 local         
# base64enc                0.1-3     2015-07-28 CRAN (R 3.5.0)
# bindr                    0.1.1     2018-03-13 CRAN (R 3.5.1)
# bindrcpp                 0.2.2     2018-03-29 CRAN (R 3.5.1)
# Biobase                * 2.40.0    2018-05-01 Bioconductor  
# BiocGenerics           * 0.26.0    2018-05-01 Bioconductor  
# BiocInstaller            1.30.0    2018-05-01 Bioconductor  
# BiocParallel           * 1.14.2    2018-07-09 Bioconductor  
# Biostrings             * 2.48.0    2018-05-01 Bioconductor  
# bit                      1.1-14    2018-05-29 CRAN (R 3.5.0)
# bit64                    0.9-7     2017-05-08 CRAN (R 3.5.0)
# bitops                   1.0-6     2013-08-17 CRAN (R 3.5.0)
# blob                     1.1.1     2018-03-25 CRAN (R 3.5.1)
# BSgenome               * 1.48.0    2018-05-01 Bioconductor  
# checkmate                1.8.5     2017-10-24 CRAN (R 3.5.1)
# cluster                  2.0.7-1   2018-04-13 CRAN (R 3.5.1)
# codetools                0.2-15    2016-10-05 CRAN (R 3.5.1)
# colorspace               1.3-2     2016-12-14 CRAN (R 3.5.1)
# compiler                 3.5.1     2018-07-02 local         
# crayon                   1.3.4     2017-09-16 CRAN (R 3.5.1)
# datasets               * 3.5.1     2018-07-02 local         
# DBI                      1.0.0     2018-05-02 CRAN (R 3.5.1)
# DelayedArray           * 0.6.6     2018-09-11 Bioconductor  
# devtools                 1.13.6    2018-06-27 CRAN (R 3.5.1)
# digest                   0.6.17    2018-09-12 CRAN (R 3.5.1)
# dplyr                    0.7.6     2018-06-29 CRAN (R 3.5.1)
# edgeR                  * 3.22.4    2018-09-23 Bioconductor  
# ff                       2.2-14    2018-05-15 CRAN (R 3.5.1)
# foreach                * 1.4.4     2017-12-12 CRAN (R 3.5.1)
# foreign                  0.8-71    2018-07-20 CRAN (R 3.5.1)
# Formula                  1.2-3     2018-05-03 CRAN (R 3.5.0)
# GenomeInfoDb           * 1.16.0    2018-05-01 Bioconductor  
# GenomeInfoDbData         1.1.0     2018-07-17 Bioconductor  
# GenomicAlignments        1.16.0    2018-05-01 Bioconductor  
# GenomicRanges          * 1.32.6    2018-07-20 Bioconductor  
# ggplot2                  3.0.0     2018-07-03 CRAN (R 3.5.1)
# glue                     1.3.0     2018-07-17 CRAN (R 3.5.1)
# graphics               * 3.5.1     2018-07-02 local         
# grDevices              * 3.5.1     2018-07-02 local         
# grid                     3.5.1     2018-07-02 local         
# gridExtra                2.3       2017-09-09 CRAN (R 3.5.1)
# gtable                   0.2.0     2016-02-26 CRAN (R 3.5.1)
# hms                      0.4.2     2018-03-10 CRAN (R 3.5.1)
# htmltools                0.3.6     2017-04-28 CRAN (R 3.5.1)
# htmlwidgets              1.3       2018-09-30 CRAN (R 3.5.1)
# httpuv                   1.4.5     2018-07-19 CRAN (R 3.5.1)
# httr                     1.3.1     2017-08-20 CRAN (R 3.5.1)
# hwriter                  1.3.2     2014-09-10 CRAN (R 3.5.0)
# interactiveDisplayBase   1.18.0    2018-05-01 Bioconductor  
# IRanges                * 2.14.11   2018-08-24 Bioconductor  
# iterators              * 1.0.10    2018-07-13 CRAN (R 3.5.1)
# knitr                    1.20      2018-02-20 CRAN (R 3.5.1)
# later                    0.7.5     2018-09-18 CRAN (R 3.5.1)
# lattice                  0.20-35   2017-03-25 CRAN (R 3.5.1)
# latticeExtra             0.6-28    2016-02-09 CRAN (R 3.5.1)
# lazyeval                 0.2.1     2017-10-29 CRAN (R 3.5.1)
# limma                  * 3.36.5    2018-09-20 Bioconductor  
# locfit                 * 1.5-9.1   2013-04-20 CRAN (R 3.5.1)
# magrittr                 1.5       2014-11-22 CRAN (R 3.5.1)
# Matrix                   1.2-14    2018-04-13 CRAN (R 3.5.1)
# matrixStats            * 0.54.0    2018-07-23 CRAN (R 3.5.1)
# memoise                  1.1.0     2017-04-21 CRAN (R 3.5.1)
# methods                * 3.5.1     2018-07-02 local         
# mime                     0.5       2016-07-07 CRAN (R 3.5.0)
# munsell                  0.5.0     2018-06-12 CRAN (R 3.5.1)
# nnet                     7.3-12    2016-02-02 CRAN (R 3.5.1)
# oligoClasses           * 1.42.0    2018-05-01 Bioconductor  
# parallel               * 3.5.1     2018-07-02 local         
# pillar                   1.3.0     2018-07-14 CRAN (R 3.5.1)
# pkgconfig                2.0.2     2018-08-16 CRAN (R 3.5.1)
# plyr                     1.8.4     2016-06-08 CRAN (R 3.5.1)
# prettyunits              1.0.2     2015-07-13 CRAN (R 3.5.1)
# progress                 1.2.0     2018-06-14 CRAN (R 3.5.1)
# promises                 1.0.1     2018-04-13 CRAN (R 3.5.1)
# purrr                    0.2.5     2018-05-29 CRAN (R 3.5.1)
# R6                       2.2.2     2017-06-17 CRAN (R 3.5.1)
# RColorBrewer             1.1-2     2014-12-07 CRAN (R 3.5.0)
# Rcpp                     0.12.18   2018-07-23 CRAN (R 3.5.1)
# RCurl                    1.95-4.11 2018-07-15 CRAN (R 3.5.1)
# registry                 0.5       2017-12-03 CRAN (R 3.5.0)
# rlang                    0.2.2     2018-08-16 CRAN (R 3.5.1)
# rpart                    4.1-13    2018-02-23 CRAN (R 3.5.1)
# Rsamtools                1.32.3    2018-08-22 Bioconductor  
# RSQLite                  2.1.1     2018-05-06 CRAN (R 3.5.1)
# rstudioapi               0.7       2017-09-07 CRAN (R 3.5.1)
# rtracklayer            * 1.40.6    2018-08-31 Bioconductor  
# S4Vectors              * 0.18.3    2018-06-08 Bioconductor  
# scales                   1.0.0     2018-08-09 CRAN (R 3.5.1)
# shiny                    1.1.0     2018-05-17 CRAN (R 3.5.1)
# ShortRead                1.38.0    2018-05-01 Bioconductor  
# splines                  3.5.1     2018-07-02 local         
# stats                  * 3.5.1     2018-07-02 local         
# stats4                 * 3.5.1     2018-07-02 local         
# SummarizedExperiment   * 1.10.1    2018-05-11 Bioconductor  
# survival                 2.42-6    2018-07-13 CRAN (R 3.5.1)
# tibble                   1.4.2     2018-01-22 CRAN (R 3.5.1)
# tidyselect               0.2.4     2018-02-26 CRAN (R 3.5.1)
# tools                    3.5.1     2018-07-02 local         
# utils                  * 3.5.1     2018-07-02 local         
# withr                    2.1.2     2018-03-15 CRAN (R 3.5.1)
# XML                      3.98-1.16 2018-08-19 CRAN (R 3.5.1)
# xtable                   1.8-3     2018-08-29 CRAN (R 3.5.1)
# XVector                * 0.20.0    2018-05-01 Bioconductor  
# yaml                     2.2.0     2018-07-25 CRAN (R 3.5.1)
# zlibbioc                 1.26.0    2018-05-01 Bioconductor  
# > 