---
layout: post
title: "qPCR Gene Selection and Relative Quantification"
date: 2026-06-24
categories: notebook
tags: qpcr gene-expression Chlorella relative-quantification
---

## Assignment Goal

This post has two parts. The first part describes a qPCR gene-expression plan for selected genes in *Chlorella vulgaris*. The second part explains the Delta-Delta Ct method for relative quantification using the class qPCR workbook.

## Part 1: qPCR Gene Selection

### Organism and Experimental Condition

The selected organism is *Chlorella vulgaris*, the same green microalga used in the previous primer-design assignment. *Chlorella vulgaris* is a unicellular photosynthetic alga, so changes in light conditions can directly affect photosynthesis, redox balance, and cellular stress.

The planned experimental condition is acute high-light stress. Cultures would be divided into a control group grown under normal light and a treatment group exposed to stronger light for a short period before RNA extraction. This treatment is biologically relevant because excess light can increase excitation pressure in the photosynthetic system and promote reactive oxygen species formation. The qPCR hypothesis is that stress-response and antioxidant genes will increase in expression in the high-light treatment compared with the control.

### Selected Genes

| Gene | qPCR role | Main biological function | Expected expression under high-light stress |
|---|---|---|---|
| `HSP70` | Target gene | Molecular chaperone involved in protein folding and protection of stressed proteins | Increase |
| `APX` | Target gene | Ascorbate peroxidase, an antioxidant enzyme involved in hydrogen peroxide detoxification | Increase |
| `TUB` / beta-tubulin | Reference gene | Cytoskeletal housekeeping gene used for normalization | Remain relatively stable |

### Target Gene 1: `HSP70`

I chose `HSP70` because it is a classic cellular stress-response gene. Hsp70 proteins act as molecular chaperones that help proteins fold correctly and prevent damaged or partially unfolded proteins from aggregating. This makes `HSP70` a useful marker for treatments that disturb protein stability.

In a high-light experiment, I expect `HSP70` expression to increase in the treated *Chlorella vulgaris* cultures. High light can cause secondary cellular stress through excess energy absorption and oxidative pressure. If proteins become damaged or unstable, the cells should need more chaperone activity. Therefore, higher `HSP70` mRNA in the treatment would support the hypothesis that the high-light exposure caused a general cellular stress response.

### Target Gene 2: `APX`

I chose `APX` because ascorbate peroxidase is directly connected to antioxidant defense in photosynthetic organisms. APX enzymes remove hydrogen peroxide using ascorbate as an electron donor and are part of the ascorbate-glutathione antioxidant system.

In the high-light treatment, I expect `APX` expression to increase. Excess light can increase reactive oxygen species production in photosynthetic cells, especially when absorbed light energy is greater than the capacity for carbon fixation and electron transport. Because APX helps detoxify hydrogen peroxide, higher `APX` expression would indicate that the cells are responding to oxidative stress.

### Reference Gene: `TUB` / Beta-Tubulin

I would use beta-tubulin as the reference gene because tubulin is a structural housekeeping gene required for basic cytoskeletal function. A reference gene should have stable expression across the control and treatment groups so that differences in target gene Ct values mainly reflect biological regulation rather than differences in RNA input, cDNA synthesis, or total template amount.

For this experiment, I expect tubulin expression to be more stable than `HSP70` or `APX` because the planned treatment is short-term high-light stress, not a treatment specifically targeting cytoskeletal structure or cell division. However, this assumption should be tested before final analysis. A stronger qPCR experiment would compare several candidate reference genes, such as tubulin, actin, and 18S rRNA, and choose the most stable one.

## Part 2: Relative Quantification Classwork

The classwork data compare gene expression between a `DMSO Control` sample and an `Inhibitor treatment` sample. The workbook uses `Tubulin` as the reference gene.

The Delta-Delta Ct method estimates relative expression by comparing a target gene to a reference gene and then comparing the treated sample to the control sample.

The calculation steps are:

1. Calculate Delta Ct for each sample:

   `Delta Ct = Ct target gene - Ct reference gene`

2. Calculate Delta-Delta Ct:

   `Delta-Delta Ct = Delta Ct treatment - Delta Ct control`

3. Convert Delta-Delta Ct to fold change:

   `Fold change = 2^(-Delta-Delta Ct)`

A fold change greater than 1 means the gene has higher relative expression in the inhibitor treatment than in the DMSO control. A fold change lower than 1 means the gene has lower relative expression in the inhibitor treatment.

### Example Calculation

For `NGN`, the workbook gives:

| Step | Value |
|---|---:|
| Ct in DMSO control | 28.3512 |
| Ct in inhibitor treatment | 27.3529 |
| Tubulin Ct in DMSO control | 23.2956 |
| Tubulin Ct in inhibitor treatment | 23.2956 |
| Delta Ct in DMSO control | 5.0556 |
| Delta Ct in inhibitor treatment | 4.0574 |
| Delta-Delta Ct | -0.9983 |
| Fold change | 1.9976 |

The `NGN` fold change is about 2.00, so `NGN` expression is approximately two times higher in the inhibitor treatment than in the DMSO control.

### Classwork Results

![qPCR fold-change graph]({{ site.baseurl }}/qpcr_homework_2026/figures/figure_1_qpcr_fold_change.svg)

**Figure 1.** Relative gene expression in the inhibitor treatment compared with the DMSO control. Fold change was calculated as `2^(-Delta-Delta Ct)` after normalization to `Tubulin`. The dashed line at 1 marks no change relative to the DMSO control.

| Gene | Delta Ct control | Delta Ct treatment | Delta-Delta Ct | Fold change |
|---|---:|---:|---:|---:|
| ascs | 5.7985 | 5.2131 | -0.5854 | 1.5005 |
| Delta | 2.6681 | 2.2424 | -0.4257 | 1.3432 |
| ets | 1.4212 | 1.1418 | -0.2794 | 1.2137 |
| foxA | 1.0703 | 0.4269 | -0.6434 | 1.5620 |
| gcm | 5.0588 | 4.8827 | -0.1761 | 1.1298 |
| NGN | 5.0556 | 4.0574 | -0.9983 | 1.9976 |
| opt | 7.7249 | 8.4126 | 0.6877 | 0.6208 |
| pak3 | 2.1102 | 1.9992 | -0.1110 | 1.0800 |
| pak4 | 2.2756 | 1.9570 | -0.3186 | 1.2471 |
| pitx | 6.3826 | 8.4286 | 2.0460 | 0.2422 |
| SM30 | -2.3268 | -1.5292 | 0.7976 | 0.5753 |
| sm50 | 0.4046 | 1.5152 | 1.1105 | 0.4631 |
| soxC | 1.7765 | 1.0323 | -0.7442 | 1.6750 |
| synB | 0.8306 | 0.7639 | -0.0667 | 1.0473 |

### Interpretation

The inhibitor treatment increased the relative expression of several genes. The strongest increase was observed for `NGN`, with a fold change of about 2.00. Other genes with higher expression in the treatment included `soxC`, `foxA`, `ascs`, and `Delta`.

Several genes showed lower relative expression in the inhibitor treatment. The strongest decrease was observed for `pitx`, with a fold change of about 0.24. This means that `pitx` expression in the inhibitor treatment was about one quarter of its expression in the DMSO control after normalization to `Tubulin`. Other decreased genes included `sm50`, `SM30`, and `opt`.

The genes with fold changes close to 1, such as `synB`, `pak3`, and `gcm`, changed only slightly between the DMSO control and inhibitor treatment. These genes show weaker evidence of treatment-related expression change in this classwork calculation.

Overall, the Delta-Delta Ct analysis shows that the inhibitor treatment does not affect all genes equally. Some developmental or regulatory genes increase, some decrease, and some remain close to the control level. The biological interpretation would depend on what pathway the inhibitor affects and what developmental roles these genes have.

## References

- Previous notebook organism context: [Primer Design and Phylogenetic Analysis of *Chlorella vulgaris*]({{ site.baseurl }}/notebook/2026/05/11/chlorella-phylogenetic-primer-design-post.html)
- Livak, K. J. and Schmittgen, T. D. 2001. Analysis of relative gene expression data using real-time quantitative PCR and the 2^-Delta Delta Ct method. [Methods](https://pubmed.ncbi.nlm.nih.gov/11846609/).
- Tavaria, M., Gabriele, T., Kola, I., and Anderson, R. L. 1996. A hitchhiker's guide to the human Hsp70 family. [Cell Stress & Chaperones](https://pubmed.ncbi.nlm.nih.gov/9222585/).
- Shigeoka, S., Ishikawa, T., Tamoi, M., Miyagawa, Y., Takeda, T., Yabuta, Y., and Yoshimura, K. 2002. Regulation and function of ascorbate peroxidase isoenzymes. [Journal of Experimental Botany](https://doi.org/10.1093/jexbot/53.372.1305).
