# NTU-CGM-2019-workshop
## Genome-wide association analysis with application in R & PLINK


<H2>

### Course material (only for educational purpose)

**PDF file** [[link to the slide]](https://drive.google.com/file/d/1usAGH5mMQVNgzIZv34q3nImgNlh8uOMO/view?usp=sharing)

**Example Data** [[link to the data]](https://drive.google.com/file/d/12GakkcKLLRKF2Y9BAWJ91aHX1T7Koq0E/view?usp=sharing)

Note1: The HapMap III raw data are processed by totally following the reference (https://cran.r-project.org/web/packages/plinkQC/vignettes/HapMap.pdf). To easily display the data management process, an addtional data manipulation was conducted.

Note2: Traits are simulated via generalized linear model (GLM) in R.

Note3: there's a reference about the criteria of sample relatedness:
Data quality control in genetic case-control association studies. Nat Protoc. 5, 1564–1573 (2010). DOI: 10.1038/nprot.2010.116

<H2>

### Activate the environment (qy)
```
source /opt/miniconda3/bin/activate /opt/miniconda3/envs/qy/
```


<H2>

### Data management (with PLINK)
Perform quality control for "rawdata" and PCA for population stratification issue. '/home/train2019/qy/' is the path for 'rawdata'; '/home/train2019/$(whoami)/qy/' is the path for storing the output which here is named 'qcdata'. You can change the output filename (here is 'qcdata') whatwver you like.
```
plink --bfile /home/train2019/qy/rawdata --geno 0.1 --maf 0.01 --mind 0.05 --hwe 0.000001 --make-bed --pca --out /home/train2019/$(whoami)/qy/qcdata
```

<H2>

### R markdown document links:
1. **Basic R command** [[rmd]](https://juuyhcngvzilmlh4agozha-on.drv.tw/CGM%20work/2019_CGM_workshop/WWW/00_Basic_rmd.html) keep updating...

2. **PCA** [[rmd]](https://juuyhcngvzilmlh4agozha-on.drv.tw/CGM%20work/2019_CGM_workshop/WWW/01_PCA_rmd.html) [[txt]](https://drive.google.com/file/d/1gixSzyMbxKmbEls2vq25wu0oCzd6LvY8/view?usp=sharing)

3. **Analysis** [[rmd]](https://juuyhcngvzilmlh4agozha-on.drv.tw/CGM%20work/2019_CGM_workshop/WWW/02_analysis.html) [[txt]](https://drive.google.com/file/d/1y9QSm_MEjFnhj1v09F0oK8748-J-J5Wl/view?usp=sharing)

4. **Manhattan plot** [[rmd]](https://juuyhcngvzilmlh4agozha-on.drv.tw/CGM%20work/2019_CGM_workshop/WWW/03_manhattan_plot_rmd.html) [[txt]](https://drive.google.com/file/d/181dv75P4cFqzK-f68Ncu-NL6D_ka1PhQ/view?usp=sharing)

