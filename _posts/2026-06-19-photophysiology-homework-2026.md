---
layout: post
title: Photophysiology Homework 2026
date: '2026-06-19'
categories: Analysis
tags: photophysiology R algae fluorescence
---

This post reports a photophysiology exercise from the Research Methods course. The exercise is treated as preliminary results for testing how habitat/light environment may affect algal photophysiology.

## Aim

The aim was to compare photophysiological performance of algae assigned to two groups, `Light` and `Dark`, and to evaluate whether the available class data provide preliminary evidence for differences in photosynthetic response between these groups. These groups are treated as proxies for habitat/light environment.

Because the dataset is small and uneven among taxa, the results are interpreted as preliminary evidence that can guide a better follow-up experiment rather than as a definitive test of habitat effects.

## Experimental Design

The design was a preliminary comparative exercise. Algal specimens were divided into two groups in the supplied metadata:

- `Light`: specimens assigned to the Light group.
- `Dark`: specimens assigned to the Dark group.

The raw data include 13 Light specimens and 8 Dark specimens. Specimens were recorded by algal taxon in the metadata table. Several taxa were represented in both groups, allowing paired taxon-level comparison between Light and Dark. Other taxa were present in only one group and were included in descriptive plots and summary tables but not in paired tests.

The raw photophysiology measurements were recorded on 16 April 2026. The exact field site, GPS coordinates, collection depth/height on shore, transport time, transport temperature, and species-identification key were not included in the data files supplied for this exercise. Therefore, those details should be added from the original field notebook if the exercise is later converted into a fully replicable experiment.

## Materials and Methods

### Specimen Collection and Identification

The submitted data package contains two photophysiology measurement files and one metadata file. The metadata file lists the experimental group, sample number, algal taxon, and sample ID for each specimen. The method used to identify the algal taxa was not included in the supplied files, so this report uses the taxon names as provided in the course metadata.

The metadata contained one spelling inconsistency: `Galxaura` in the Dark group and `Galaxaura` in the Light group. For the paired analysis, this was treated as the same taxon and corrected to `Galaxaura` in the processed analysis table. The raw metadata file is kept unchanged.

### Specimen Metadata

| Group | Sample | Taxon | Sample ID |
|---|---:|---|---|
| Dark | 1 | Colpomenia | Dark_1 |
| Dark | 2 | Dictyota | Dark_2 |
| Dark | 8 | Galxaura | Dark_8 |
| Dark | 5 | Jania | Dark_5 |
| Dark | 4 | Padina | Dark_4 |
| Dark | 6 | Red UNK | Dark_6 |
| Dark | 3 | Sargassum | Dark_3 |
| Dark | 7 | Ulva | Dark_7 |
| Light | 8 | Cistosera | Light_8 |
| Light | 12 | Colpomenia | Light_12 |
| Light | 6 | Cudiom | Light_6 |
| Light | 11 | Dictyota | Light_11 |
| Light | 10 | Galaxaura | Light_10 |
| Light | 2 | Halopteris | Light_2 |
| Light | 5 | Hypnea | Light_5 |
| Light | 1 | Jania | Light_1 |
| Light | 3 | Namaliun | Light_3 |
| Light | 7 | Padina | Light_7 |
| Light | 4 | Sargassum | Light_4 |
| Light | 9 | Ulva | Light_9 |
| Light | 13 | Ulva | Light_13 |

**Table 1.** Specimen metadata supplied for the photophysiology exercise. The table links the raw ETR column number to the taxon and sample ID used in the analysis.

### Photophysiology Measurements

Photophysiology data were supplied as two semicolon-separated files:

- `data/light.csv`
- `data/dark.csv`

Each file contains the measurement date, measurement time, PAR level, fluorescence variables, and ETR columns for each specimen. The Light file contains `ETR1` to `ETR13`; the Dark file contains `ETR1` to `ETR8`.

Measurements were supplied as light-response measurements. PAR increased stepwise from 0 upward, and ETR was recorded for each specimen at each PAR step. The analysis used the ETR columns because the course script defines them as the relevant values for fitting photosynthesis-irradiance curves.

ETR values equal to zero when PAR was greater than zero were treated as missing values, because the course script states that these values indicate that the measurement for that specimen had ended.

### Data Processing and Curve Fitting

The analysis was performed in R using the reproducible script `photophysiology_homework_2026.Rmd`. The raw Light and Dark files were read into R, date and time columns were converted to date/time objects, and ETR columns were reshaped from wide format to long format. Metadata were joined by group and sample number.

Light samples `Light_3` and `Light_9` were removed before curve fitting because the course script identified them as curves that did not reach the expected response shape. No Dark samples were removed.

For each retained specimen, ETR was fitted as a function of PAR using the non-linear model from the class script:

`ETR = Am * ((AQY * PAR) / sqrt(Am^2 + (AQY * PAR)^2)) - Rd`

The extracted and calculated parameters were:

| Parameter | Meaning |
|---|---|
| `Am` | Asymptotic maximum ETR, interpreted as maximum photosynthetic electron transport capacity. |
| `AQY` | Initial slope of the curve, interpreted as apparent quantum yield or light-use efficiency. |
| `Rd` | Fitted intercept/respiration-like parameter in ETR units. |
| `Ik` | Saturation irradiance proxy, calculated as `Am / AQY`. |

Only taxa represented in both Light and Dark groups were used for paired Light-Dark comparison. Paired Wilcoxon signed-rank tests were used as exploratory tests, and p-values were adjusted using the Benjamini-Hochberg method. Because sample size was small, effect sizes and plots were interpreted together with p-values.

The R packages used were:

| Package | Version |
|---|---:|
| dplyr | 1.2.1 |
| tidyr | 1.3.2 |
| lubridate | 1.9.5 |
| hms | 1.1.4 |
| ggplot2 | 4.0.3 |
| purrr | 1.2.2 |
| broom | 1.0.13 |
| patchwork | 1.3.2 |
| openxlsx | 4.2.8.1 |
| knitr | 1.51 |

**Table 2.** R packages used for data manipulation, curve fitting, plotting, and exporting results.

## Results

### Photosynthesis-Irradiance Curves

![Photosynthesis-irradiance curves](https://raw.githubusercontent.com/gayafrank/Gaya---Research-method-2026/main/photophysiology_homework_2026/figures/figure_1_pi_curves.png)

**Figure 1.** Photosynthesis-irradiance curves for retained Light and Dark specimens. Points show observed ETR values and lines show fitted non-linear curves.

### Calculated Photophysiology Measurements

| Sample ID | Sample | Taxon | Group | Am | AQY | Rd | Ik |
|---|---:|---|---|---:|---:|---:|---:|
| Dark_1 | 1 | Colpomenia | Dark | 33.960 | 0.2076 | -0.345 | 163.6 |
| Dark_2 | 2 | Dictyota | Dark | 12.813 | 0.3079 | 0.252 | 41.6 |
| Dark_3 | 3 | Sargassum | Dark | 5.982 | 0.2410 | 0.018 | 24.8 |
| Dark_4 | 4 | Padina | Dark | 40.569 | 0.2150 | 0.087 | 188.6 |
| Dark_5 | 5 | Jania | Dark | 8.783 | 0.0679 | -0.144 | 129.3 |
| Dark_6 | 6 | Red UNK | Dark | 8.071 | 0.2015 | 0.077 | 40.1 |
| Dark_7 | 7 | Ulva | Dark | 17.600 | 0.1446 | 0.238 | 121.7 |
| Dark_8 | 8 | Galaxaura | Dark | 16.855 | 0.1345 | -0.428 | 125.3 |
| Light_1 | 1 | Jania | Light | 33.253 | 0.1241 | -0.392 | 267.9 |
| Light_2 | 2 | Halopteris | Light | 6.483 | 0.1138 | -0.074 | 57.0 |
| Light_4 | 4 | Sargassum | Light | 30.126 | 0.1530 | -0.670 | 196.9 |
| Light_5 | 5 | Hypnea | Light | 23.410 | 0.1635 | 0.054 | 143.2 |
| Light_6 | 6 | Cudiom | Light | 8.827 | 0.1394 | 0.136 | 63.3 |
| Light_7 | 7 | Padina | Light | 47.082 | 0.1841 | -0.557 | 255.7 |
| Light_8 | 8 | Cistosera | Light | 13.887 | 0.1422 | -0.030 | 97.7 |
| Light_10 | 10 | Galaxaura | Light | 7.948 | 0.1224 | -0.121 | 65.0 |
| Light_11 | 11 | Dictyota | Light | 31.169 | 0.1391 | 0.054 | 224.1 |
| Light_12 | 12 | Colpomenia | Light | 16.828 | 0.1228 | -0.136 | 137.1 |
| Light_13 | 13 | Ulva | Light | 17.731 | 0.0986 | -0.085 | 179.8 |

**Table 3.** Calculated photophysiology parameters extracted from the fitted photosynthesis-irradiance curves. `Ik` was calculated as `Am/AQY`.

### Summary of Fitted Parameters

![Parameter boxplots](https://raw.githubusercontent.com/gayafrank/Gaya---Research-method-2026/main/photophysiology_homework_2026/figures/figure_2_parameter_boxplots.png)

**Figure 2.** Fitted photophysiology parameters in Light and Dark groups. Points represent individual taxa/specimens.

| Parameter | Group | n | Mean | SD | Min | Q25 | Median | Q75 | Max |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AQY | Dark | 8 | 0.1900 | 0.0733 | 0.0679 | 0.1421 | 0.2045 | 0.2215 | 0.3079 |
| AQY | Light | 11 | 0.1366 | 0.0241 | 0.0986 | 0.1226 | 0.1391 | 0.1476 | 0.1841 |
| Am | Dark | 8 | 18.0790 | 12.6512 | 5.9816 | 8.6049 | 14.8339 | 21.6898 | 40.5690 |
| Am | Light | 11 | 21.5221 | 12.7588 | 6.4829 | 11.3566 | 17.7312 | 30.6472 | 47.0819 |
| Ik | Dark | 8 | 104.3842 | 61.3853 | 24.8202 | 41.2207 | 123.4942 | 137.9091 | 188.6494 |
| Ik | Light | 11 | 153.4213 | 77.3773 | 56.9885 | 81.3046 | 143.2214 | 210.5159 | 267.8714 |
| Rd | Dark | 8 | -0.0307 | 0.2531 | -0.4277 | -0.1942 | 0.0475 | 0.1244 | 0.2516 |
| Rd | Light | 11 | -0.1655 | 0.2613 | -0.6701 | -0.2639 | -0.0854 | 0.0122 | 0.1361 |

**Table 4.** Summary statistics for fitted photophysiology parameters by group.

### Paired Light-Dark Comparison

The taxa included in paired comparisons were Colpomenia, Dictyota, Galaxaura, Jania, Padina, Sargassum, and Ulva.

| Parameter | p-value | BH-adjusted p-value |
|---|---:|---:|
| AQY | 0.1083 | 0.2166 |
| Am | 0.2719 | 0.2719 |
| Ik | 0.1083 | 0.2166 |
| Rd | 0.2049 | 0.2719 |

**Table 5.** Paired Wilcoxon tests comparing Light and Dark values for taxa represented in both groups.

![Paired differences and ratios](https://raw.githubusercontent.com/gayafrank/Gaya---Research-method-2026/main/photophysiology_homework_2026/figures/figure_3_paired_differences_ratios.png)

**Figure 3.** Paired taxon comparison between Light and Dark groups. The top panels show absolute differences and the bottom panels show ratios. A ratio of 1 indicates no difference between groups.

![Q-Q plots](https://raw.githubusercontent.com/gayafrank/Gaya---Research-method-2026/main/photophysiology_homework_2026/figures/figure_4_qq_plots.png)

**Figure 4.** Q-Q plots for fitted parameters. With the small sample size, these plots are used for visual assessment rather than strong distributional claims.

## Interpretation

The fitted curves produced interpretable parameter estimates for 11 Light specimens and 8 Dark specimens after two problematic Light curves were removed. The paired tests did not produce Benjamini-Hochberg adjusted p-values below 0.05 for `Am`, `AQY`, `Rd`, or `Ik`. Therefore, the available data do not provide strong statistical evidence for a consistent difference between Light and Dark groups.

This does not mean that habitat/light exposure has no biological effect. The sample size is small, the design is uneven among taxa, and some taxa show large taxon-specific differences in the paired difference and ratio plots. For example, Dictyota showed higher fitted `Am` and `Ik` in the Light group than in the Dark group, while Colpomenia showed lower fitted `Am` in the Light group than in the Dark group. This suggests that taxon identity should be controlled in a follow-up experiment.

The main conclusion is that these data are useful as preliminary results, but not as a strong final test of habitat effects. A better follow-up experiment should use a balanced design with the same taxa sampled from replicated habitat/light environments, with the same number of specimens per taxon and habitat. The field site, shore height or depth, collection time, transport conditions, acclimation time, and species-identification method should be recorded explicitly. This would make it possible to separate habitat effects from taxon-specific differences and sampling imbalance.

## Supporting Files

The supporting files for this post are saved in `photophysiology_homework_2026/`:

- [`data/Photophysiology_metadata.csv`](https://github.com/gayafrank/Gaya---Research-method-2026/blob/main/photophysiology_homework_2026/data/Photophysiology_metadata.csv): specimen metadata table.
- [`data/light.csv`](https://github.com/gayafrank/Gaya---Research-method-2026/blob/main/photophysiology_homework_2026/data/light.csv): raw Light group photophysiology file.
- [`data/dark.csv`](https://github.com/gayafrank/Gaya---Research-method-2026/blob/main/photophysiology_homework_2026/data/dark.csv): raw Dark group photophysiology file.
- [`photophysiology_homework_2026.Rmd`](https://github.com/gayafrank/Gaya---Research-method-2026/blob/main/photophysiology_homework_2026/photophysiology_homework_2026.Rmd): reproducible R analysis source.
- [`photophysiology_parameters_tidy.csv`](https://github.com/gayafrank/Gaya---Research-method-2026/blob/main/photophysiology_homework_2026/outputs/photophysiology_parameters_tidy.csv): tidy calculated photophysiology table.
- [`photophysiology_parameters_with_readme.xlsx`](https://github.com/gayafrank/Gaya---Research-method-2026/blob/main/photophysiology_homework_2026/outputs/photophysiology_parameters_with_readme.xlsx): Excel output with `Data` and `ReadMe` sheets.
- [`photophysiology_homework_environment.RData`](https://github.com/gayafrank/Gaya---Research-method-2026/blob/main/photophysiology_homework_2026/outputs/photophysiology_homework_environment.RData): saved R environment.
- [`photophysiology_summary_table.csv`](https://github.com/gayafrank/Gaya---Research-method-2026/blob/main/photophysiology_homework_2026/outputs/photophysiology_summary_table.csv): exported summary table.
- [`paired_wilcoxon_tests.csv`](https://github.com/gayafrank/Gaya---Research-method-2026/blob/main/photophysiology_homework_2026/outputs/paired_wilcoxon_tests.csv): exported statistical test table.
- [`paired_taxon_differences.csv`](https://github.com/gayafrank/Gaya---Research-method-2026/blob/main/photophysiology_homework_2026/outputs/paired_taxon_differences.csv): exported paired taxon differences and ratios.
- [`package_versions.csv`](https://github.com/gayafrank/Gaya---Research-method-2026/blob/main/photophysiology_homework_2026/outputs/package_versions.csv): package names and versions.
