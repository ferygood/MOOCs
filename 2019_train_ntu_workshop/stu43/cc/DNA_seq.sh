#step 0 (fastq file quality check): fastqc (fastqc version: 0.11.8)
fastqc -o ./ -f fastq \
/home/train2019/csw/raw/Tumor_chr13_region_r1.fastq.gz \
/home/train2019/csw/raw/Tumor_chr13_region_r2.fastq.gz \
/home/train2019/csw/raw/Normal_chr13_region_r1.fastq.gz \
/home/train2019/csw/raw/Normal_chr13_region_r2.fastq.gz

##data pre-processing
#step 1 (alignment): bwa mem (bwa version: 0.7.17-r1188) & samtools view  (samtools version: 1.9)
bwa mem -t 1 -K 100000000 -R '@RG\tID:group1\tLB:SureSelectXT2_v6\tPL:illumina\tPU:batch\tSM:Tumor' \
/home/train2019/csw/ref/genome.fa \
/home/train2019/csw/raw/Tumor_chr13_region_r1.fastq.gz \
/home/train2019/csw/raw/Tumor_chr13_region_r2.fastq.gz \
| samtools view -@ 0 -bt /home/train2019/csw/ref/genome.fa -o Tumor.bam

bwa mem -t 1 -K 100000000 -R '@RG\tID:group1\tLB:SureSelectXT2_v6\tPL:illumina\tPU:batch\tSM:Normal' \
/home/train2019/csw/ref/genome.fa \
/home/train2019/csw/raw/Normal_chr13_region_r1.fastq.gz \
/home/train2019/csw/raw/Normal_chr13_region_r2.fastq.gz \
| samtools view -@ 0 -bt /home/train2019/csw/ref/genome.fa -o Normal.bam

#Step 2 (mark duplicates): picard SortSam & picard MarkDuplicates (picard version: 2.20.1)
picard SortSam \
CREATE_INDEX=true \
INPUT=Tumor.bam \
OUTPUT=Tumor_sorted.bam \
SORT_ORDER=coordinate 

picard SortSam \
CREATE_INDEX=true \
INPUT=Normal.bam \
OUTPUT=Normal_sorted.bam \
SORT_ORDER=coordinate 
	
picard MarkDuplicates \
CREATE_INDEX=true \
I=Tumor_sorted.bam \
O=Tumor_sorted_markdup.bam \
M=Tumor_marked_dup_metrics.txt  

picard MarkDuplicates \
CREATE_INDEX=true \
I=Normal_sorted.bam \
O=Normal_sorted_markdup.bam \
M=Normal_marked_dup_metrics.txt  

#Step 3 (Base quality score recalibration): gatk BaseRecalibrator & gatk ApplyBQSR  (gatk4 version: 4.1.2.0)
gatk BaseRecalibrator \
-R /home/train2019/csw/ref/genome.fa \
-L chr13:32310000-32980000 \
-ip 100 \
-I Tumor_sorted_markdup.bam \
--known-sites /home/train2019/csw/known/dbsnp_138.hg19.vcf \
--known-sites /home/train2019/csw/known/1000G_omni2.5.hg19.sites.vcf \
--known-sites /home/train2019/csw/known/Mills_and_1000G_gold_standard.indels.hg19.sites.vcf \
-O Tumor_recal.table

gatk BaseRecalibrator \
-R /home/train2019/csw/ref/genome.fa \
-L chr13:32310000-32980000 \
-ip 100 \
-I Normal_sorted_markdup.bam \
--known-sites /home/train2019/csw/known/dbsnp_138.hg19.vcf \
--known-sites /home/train2019/csw/known/1000G_omni2.5.hg19.sites.vcf \
--known-sites /home/train2019/csw/known/Mills_and_1000G_gold_standard.indels.hg19.sites.vcf \
-O Normal_recal.table


gatk ApplyBQSR \
-R /home/train2019/csw/ref/genome.fa \
-I Tumor_sorted_markdup.bam \
--bqsr-recal-file Tumor_recal.table \
-O Tumor_recal.bam

gatk ApplyBQSR \
-R /home/train2019/csw/ref/genome.fa \
-I Normal_sorted_markdup.bam \
--bqsr-recal-file Tumor_recal.table \
-O Normal_recal.bam

##Somatic variant calling
#Step 1 (panel of normal): not build in this course
#Step 1-1  Run Mutect2 in tumor-only mode for each normal sample.
gatk Mutect2 \
--java-options "-Xmx3G -Djava.io.tmpdir=./" \
-R /home/train2019/csw/ref/genome.fa \
-I /home/train2019/csw/pon/normal1.bam \
-L chr13:32310000-32980000 \
-ip 100 \
--max-mnp-distance 0 \
--native-pair-hmm-threads 1 \
-O normal1.vcf.gz 

gatk Mutect2 \
--java-options "-Xmx3G -Djava.io.tmpdir=./" \
-R /home/train2019/csw/ref/genome.fa \
-I /home/train2019/csw/pon/normal2.bam \
-L chr13:32310000-32980000 \
-ip 100 \
--max-mnp-distance 0 \
--native-pair-hmm-threads 1 \
-O normal2.vcf.gz 

gatk Mutect2 \
--java-options "-Xmx3G -Djava.io.tmpdir=./" \
-R /home/train2019/csw/ref/genome.fa \
-I /home/train2019/csw/pon/normal3.bam \
-L chr13:32310000-32980000 \
-ip 100 \
--max-mnp-distance 0 \
--native-pair-hmm-threads 1 \
-O normal3.vcf.gz 

#Step 1-2  Create a GenomicsDB from the normal Mutect2 calls.
gatk GenomicsDBImport \
-R /home/train2019/csw/ref/genome.fa \
-L chr13:32310000-32980000 \
--genomicsdb-workspace-path pon_db \
-V normal1.vcf.gz \
-V normal2.vcf.gz \
-V normal3.vcf.gz

#Step 1-3  Combine the normal calls using CreateSomaticPanelOfNormals.
gatk CreateSomaticPanelOfNormals \
-R /home/train2019/csw/ref/genome.fa \
-V gendb://pon_db \
-O pon.vcf.gz

#Step 2 (Variant calling): gatk Mutect2
gatk Mutect2 \
-R /home/train2019/csw/ref/genome.fa \
--java-options "-Xmx3G -Djava.io.tmpdir=./" \
-I Tumor_recal.bam \
-I Normal_recal.bam \
-normal Normal \
-L chr13:32310000-32980000 \
-ip 100 \
--native-pair-hmm-threads 1 \
--f1r2-tar-gz  f1r2.tar.gz \
--germline-resource /home/train2019/csw/known/af-only-gnomad.raw.sites.hg19.vcf.gz \
--panel-of-normals  pon.vcf.gz \
-O Tumor.vcf.gz 

#Step 3 (Learn read orientation model): gatk LearnReadOrientationModel
gatk LearnReadOrientationModel \
-I f1r2.tar.gz \
-O Tumor-sample-artifact-prior.tar.gz

#Step 4 (Contamination estimation): gatk GetPileupSummaries & gatk CalculateContamination
gatk GetPileupSummaries \
-I Tumor_recal.bam \
-V /home/train2019/csw/known/small_exac_common_3_hg19.vcf.gz \
-L /home/train2019/csw/known/small_exac_common_3_hg19.vcf.gz \
-O pileups.table

gatk GetPileupSummaries \
-I Normal_recal.bam \
-V /home/train2019/csw/known/small_exac_common_3_hg19.vcf.gz \
-L /home/train2019/csw/known/small_exac_common_3_hg19.vcf.gz \
-O normal_pileups.table

gatk CalculateContamination \
-I pileups.table \
-matched normal_pileups.table \
--tumor-segmentation segments.tsv \
-O contamination.table

#step 5 (Filter false positive variants): gatk FilterMutectCalls
gatk FilterMutectCalls \
-R /home/train2019/csw/ref/genome.fa \
-V Tumor.vcf.gz \
--orientation-bias-artifact-priors Tumor-sample-artifact-prior.tar.gz \
--contamination-table contamination.table \
--tumor-segmentation segments.tsv \
-O Tumor_matched_m2_oncefiltered.vcf.gz


#before annotation (Sites that have been marked as filtered will be excluded from the output)
gatk SelectVariants \
-R  /home/train2019/csw/ref/genome.fa \
-V  Tumor_matched_m2_oncefiltered.vcf.gz \
-L chr13:32310000-32980000 \
--exclude-filtered \
-O  Tumor_exclude_filtered.vcf

