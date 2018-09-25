#GenomicFeatures
source("http://www.bioconductor.org/biocLite.R")
biocLite(c("GenomicFeatures", "TxDb.Hsapiens.UCSC.hg19.knownGene"))
install.packages('stringi')
install.packages('TxDb.Hsapiens.UCSC.hg19.knownGene')
library(GenomicFeatures)
library(TxDb.Hsapiens.UCSC.hg19.knownGene)

txdb <- TxDb.Hsapiens.UCSC.hg19.knownGene
txdb

#Gene, exons and transcripts
gr <- GRanges(seqnames = "chr1", strand = "+", ranges = IRanges(start = 11874, end = 14409))
subsetByOverlaps(genes(txdb), gr)
subsetByOverlaps(genes(txdb), gr, ignore.strand = TRUE)
subsetByOverlaps(transcripts(txdb), gr)
subsetByOverlaps(exons(txdb), gr)
subsetByOverlaps(exonsBy(txdb, by = "tx"), gr)
subsetByOverlaps(cds(txdb), gr)
subsetByOverlaps(cdsBy(txdb, by = "tx"), gr)
subset(transcriptLengths(txdb, with.cds_len = TRUE), gene_id == "100287102")

# R version 3.2.1 (2015-06-18)
# other attached packages:
# [1] XVector_0.8.0                          
# [2] TxDb.Hsapiens.UCSC.hg19.knownGene_3.1.2
# [3] GenomicFeatures_1.20.2                 
# [4] AnnotationDbi_1.30.1                   
# [5] Biobase_2.28.0                         
#[6] GenomicRanges_1.20.5                   
# [7] GenomeInfoDb_1.4.2                     
# [8] IRanges_2.2.7                          
#[9] S4Vectors_0.6.3                        
#[10] BiocGenerics_0.14.0                    
#[11] BiocStyle_1.6.0                        
#[12] rmarkdown_0.7                          
## loaded via a namespace (and not attached):
##  [1] knitr_1.11              magrittr_1.5           
##  [3] GenomicAlignments_1.4.1 zlibbioc_1.14.0        
##  [5] BiocParallel_1.2.20     stringr_1.0.0          
##  [7] tools_3.2.1             DBI_0.3.1              
##  [9] lambda.r_1.1.7          futile.logger_1.4.1    
## [11] htmltools_0.2.6         yaml_2.1.13            
## [13] digest_0.6.8            rtracklayer_1.28.8     
## [15] formatR_1.2             futile.options_1.0.0   
## [17] bitops_1.0-6            RCurl_1.95-4.7         
## [19] biomaRt_2.24.0          evaluate_0.7.2         
## [21] RSQLite_1.0.0           stringi_0.5-5          
## [23] Rsamtools_1.20.4        Biostrings_2.36.3      
## [25] XML_3.98-1.3