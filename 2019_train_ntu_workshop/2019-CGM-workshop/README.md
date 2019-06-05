# 2019 CGM Advanced Statistic Analysis Workshop: RNA-seq data analysis

Center of Genomic and Pecision Medicine, National Taiwan University

Taipei, Taiwan

04/06/2019 (Tuesday, 13:30-14:50)  

## Outline
- RNA-seq data analysis [[Slides]](https://www.dropbox.com/sh/coiceg5hus3hd2i/AAC05Z8QTOfyWJOGsIOiQl3Ha?dl=0)
- Webtools for network analysis (gene-level & protein-level)
- Webtool for pathway analysis (DAVID)

## Let's Get started

### Login using the username assigned to you
```
ssh stu#@train2019.cgm.ntu.edu.tw (# = desk number; e.g.53)
stu#@train2019.cgm.ntu.edu.tw's password:train
[stu#@localhost ~]$
```

### Environment and home directory
Basic linux command
- **You should be in your home directory `~/` after login**
- **Type `pwd` and obtain the current path**
- **Change directory to ywh `cd ywh/` and `ls` to list the contents in the folder**

## RNA-seq data analysis

### Let's look at the folder structure


```bash
/home/stu#/ywh/
├── align
│   ├── ERR188428_chrX.bam
│   ├── ERR188428_chrX.sam
│   └── ERR188428_chrX_summarymetric.txt
├── de
│   ├── boxplot.jpg
│   ├── chrX_gene_results.csv
│   ├── chrX_transcript_results.csv
│   ├── FPKM_summary.csv
│   └── FPKM_summary_table.csv
└── quan
    ├── ERR188428
    │   ├── e2t.ctab
    │   ├── e_data.ctab
    │   ├── ERR188428_chrX.gtf
    │   ├── i2t.ctab
    │   ├── i_data.ctab
    │   └── t_data.ctab
    ├── ERR188428_chrX.gtf
    ├── mergelist.txt
    └── stringtie_merged.gtf
```

### Analytic Pipeline

#### Warm-up

```bash
[stu#@localhost ~]$ pwd
/home/train2019/stu#/
[stu#@localhost ~]$ ls
cc  qy  train2019_cc.sh  train2019_qy.sh  train2019_ywh.sh  ywh
[stu#@localhost ~]$ . train2019_ywh.sh
(train2019_rna) [stu#@localhost ~]$ cd ywh/
(train2019_rna) [stu#@localhost ywh]$ mkdir align quan de
```

#### Step 1: Spliced alignment using HISAT2

```bash
(train2019_rna) [stu#@localhost ywh]$ hisat2 --dta -x /home/train2019/ywh/RNA-seq/ref/chrX_tran -1 /home/train2019/ywh/RNA-seq/raw/ERR188428_chrX_1.fastq.gz -2 /home/train2019/ywh/RNA-seq/raw/ERR188428_chrX_2.fastq.gz -S align/ERR188428_chrX.sam 2> align/ERR188428_chrX_summarymetric.txt
(train2019_rna) [stu#@localhost ywh]$ cat align/ERR188428_chrX_summarymetric.txt
```

#### Step 2: Conversion to sorted BAM files using SAMtools

```bash
(train2019_rna) [stu#@localhost ywh]$ samtools sort -@ 1 -o align/ERR188428_chrX.bam align/ERR188428_chrX.sam
```

#### Step 3: Transcript assembly and quantification using StringTie
##### Step3-1: assemble transcripts for each sample

```bash
(train2019_rna) [stu#@localhost ywh]$ stringtie -G /home/train2019/ywh/RNA-seq/ref/chrX.gtf -o quan/ERR188428_chrX.gtf -l ERR188428_chrX align/ERR188428_chrX.bam
```

##### step3-2: merge transcripts for all samples

```bash
(train2019_rna) [stu#@localhost ywh]$ find /home/train2019/ywh/RNA-seq/quan/*.gtf > quan/mergelist.txt
(train2019_rna) [stu#@localhost ywh]$ stringtie --merge -G /home/train2019/ywh/RNA-seq/ref/chrX.gtf -o quan/stringtie_merged.gtf quan/mergelist.txt
```

##### step3-3: re-estimate the abundance

```bash
(train2019_rna) [stu#@localhost ywh]$ stringtie -e -B -G quan/stringtie_merged.gtf -o quan/ERR188428/ERR188428_chrX.gtf align/ERR188428_chrX.bam
(train2019_rna) [stu#@localhost ywh]$ head -n 5 quan/ERR188428/ERR188428_chrX.gtf
```

### step4: differential expression analysis

```bash
(train2019_rna) [stu#@localhost ywh]$ Rscript /home/train2019/ywh/RNA-seq/DEanalysis_new.R
```

### Rscript: DEanalysis_new.R

```R
library(ballgown)
library(genefilter)
library(dplyr)
library(devtools)

pheno_data <- read.csv("/home/train2019/ywh/RNA-seq/chrX_phenodata.csv")
bg_chrX <- ballgown(dataDir = "/home/train2019/ywh/RNA-seq/de", samplePattern = "ERR", pData=pheno_data)
bg_chrX_fit <- subset(bg_chrX,"rowVars(texpr(bg_chrX)) >1",genomesubset=TRUE)
results_genes <- stattest(bg_chrX_fit, feature="gene",covariate="sex", getFC=TRUE, meas="FPKM")
results_transcripts <- stattest(bg_chrX_fit, feature="transcript",covariate="sex", getFC=TRUE, meas="FPKM")
results_transcripts <- data.frame(geneNames=ballgown::geneNames(bg_chrX_fit), geneIDs=ballgown::geneIDs(bg_chrX_fit), results_transcripts)
results_transcripts <- arrange(results_transcripts,pval)
write.csv(results_genes, "de/chrX_gene_results.csv",row.names=FALSE)
write.csv(results_transcripts, "de/chrX_transcript_results.csv",row.names=FALSE)

fpkm <- texpr(bg_chrX, meas='FPKM')
fpkm <- log2(fpkm +1)
write.csv(fpkm, "de/FPKM_summary_table.csv")
jpeg('de/boxplot.jpg')
boxplot(fpkm, col=as.numeric(pheno_data$sex), las=2,ylab='log2(FPKM+1)', main = "Boxplot")
dev.off()

fpkm_summary <- texpr(bg_chrX, meas='all')
write.csv(fpkm_summary, "de/FPKM_summary.csv",row.names=FALSE)
```

## Network analysis

- at gene level using [[GeneMANIA]](https://genemania.org/)
- at protein level using [[STRING]](https://string-db.org/)

## Pathway analysis

- DAVID Bioinformatics Resources 6.8 [[DAVID]](https://david.ncifcrf.gov/home.jsp)

## Sofeware requirement

* [SAMtools](http://samtools.sourceforge.net/)
* [HISAT2](https://ccb.jhu.edu/software/hisat2/index.shtml)
* [StringTie](https://ccb.jhu.edu/software/stringtie/)
* [Bioconductor-ballgown](https://www.bioconductor.org/packages/release/bioc/html/ballgown.html)






















