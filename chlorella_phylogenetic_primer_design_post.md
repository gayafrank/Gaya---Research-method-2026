# Primer Design and Phylogenetic Analysis of *Chlorella vulgaris* Using the 18S rRNA/ITS Region

## Objective

The objective of this project was to document a basic bioinformatics workflow for algal species identification. The workflow included collecting related DNA sequences from NCBI, aligning them in MEGA, identifying conserved and variable regions, constructing a phylogenetic tree, and designing primers for the selected target sequence.

## Target Organism and Marker Gene Region

The target organism selected for this project was *Chlorella vulgaris*. The DNA region used was the nuclear ribosomal region containing the partial 18S rRNA gene, ITS1, 5.8S rRNA gene, ITS2, and partial 28S rRNA gene.

This region was selected because 18S rRNA and ITS regions are commonly used for algal identification and comparison between related species. The 18S rRNA region is relatively conserved, which helps with alignment between related taxa, while the ITS regions are more variable and can help distinguish closely related species.

## Sequences Collected from NCBI

The sequences were collected from NCBI in FASTA format. The main target sequence was *Chlorella vulgaris* FR865658.1. Additional related sequences were downloaded to compare the target organism with closely related taxa.

| Accession number | Organism | Region |
|---|---|---|
| FR865658.1 | *Chlorella vulgaris* | 18S rRNA, ITS1, 5.8S rRNA, ITS2, 28S rRNA |
| FM205832.1 | *Chlorella vulgaris* | 18S rRNA, ITS1, 5.8S rRNA, ITS2, 28S rRNA |
| FR865660.1 | *Chlorella vulgaris* | 18S rRNA, ITS1, 5.8S rRNA, ITS2, 28S rRNA |
| FR865661.1 | *Chlorella emersonii* | 18S rRNA, ITS1, 5.8S rRNA, ITS2, 28S rRNA |

The sequences were saved in one FASTA file and then imported into MEGA for alignment and phylogenetic analysis.

## Multiple Sequence Alignment

The sequences were aligned using MEGA12. In MEGA, a new DNA alignment was created and the FASTA file was imported. The sequences were aligned using the ClustalW alignment method.

Alignment steps:

1. Opened MEGA12.
2. Selected **Align → Edit/Build Alignment**.
3. Created a new **DNA** alignment.
4. Imported the FASTA file containing the *Chlorella* sequences.
5. Selected all sequences.
6. Used **Alignment → Align by ClustalW**.
7. Saved the alignment as a MEGA alignment file.

![Multiple sequence alignment in MEGA](images/alaignment.png)

Figure 1: Multiple sequence alignment of *Chlorella* sequences in MEGA12.

## Conserved and Variable Regions

After alignment, conserved and variable regions were identified by visually examining the aligned sequences in MEGA.

Conserved regions were defined as positions where all sequences had the same nucleotide. In the alignment screenshot, many columns are conserved and are marked by `*` above the alignment.

Variable regions were defined as positions where at least one sequence differed from the others. These differences included SNPs and indels.

### SNPs

A SNP, or single nucleotide polymorphism, is a position in the alignment where one sequence has a different nucleotide compared with the others. In the alignment, SNPs were visible in columns where the *Chlorella emersonii* sequence differed from the *Chlorella vulgaris* sequences.

For example, in the visible alignment region, most positions are conserved among the three *Chlorella vulgaris* sequences, while the *Chlorella emersonii* sequence contains several nucleotide substitutions. These substitutions represent variable sites or SNPs.

### Indels

An indel is an insertion or deletion. In the alignment, indels appear as gaps marked with `-`. In the visible alignment, gaps are present at the beginning of some sequences, especially in FR865660.1 and FR865661.1, compared with FR865658.1 and FM205832.1. These gaps represent insertion/deletion differences between the sequences.

## Primer Design

Primers were designed for the target sequence *Chlorella vulgaris* FR865658.1 using NCBI Primer-BLAST. The input PCR template was accession FR865658.1, which is a 2,780 bp genomic DNA sequence containing the 18S rRNA gene, ITS1, 5.8S rRNA gene, ITS2, and 28S rRNA gene.

The primer design settings used in Primer-BLAST were:

| Parameter | Value used |
|---|---|
| PCR template | FR865658.1 |
| PCR product size | 300–800 bp |
| Number of primers to return | 10 |
| Minimum primer Tm | 57.0°C |
| Optimum primer Tm | 60.0°C |
| Maximum primer Tm | 63.0°C |
| Maximum Tm difference | 3°C |
| Specificity check | Enabled |
| Search mode | Automatic |
| Database | RefSeq mRNA |
| Organism field | `'Chlorella vulgaris' C-169 (taxid:574566)` as shown in Primer-BLAST |
| Maximum target amplicon size | 4000 bp |

![Primer-BLAST settings](images/blans_settings.png)

Figure 2: Primer-BLAST settings used for primer design of the *Chlorella vulgaris* target sequence.

Primer-BLAST returned several possible primer pairs. Primer pair 1 was selected because it had suitable primer length, similar melting temperatures, acceptable GC content, and an expected product size within the requested range.

### Selected Primer Pair

| Primer | Sequence 5′ → 3′ | Length | Start | Stop | Tm | GC content |
|---|---|---:|---:|---:|---:|---:|
| Forward primer | TGAAGTGTTCGGATTGGCGA | 20 bp | 1650 | 1669 | 59.97°C | 50.00% |
| Reverse primer | GAACCGGGAAGGTCAGATCC | 20 bp | 2287 | 2268 | 59.82°C | 60.00% |

Expected PCR product length: **638 bp**.

Primer-BLAST reported that the primer pair was specific to the input template in the selected database, with no other targets found under the selected search conditions.

![Graphical view of Primer-BLAST primer pairs](images/blast_results.png)

Figure 3: Graphical view of the selected Primer-BLAST primer pair and expected PCR product.

## Phylogenetic Tree Construction

A phylogenetic tree was constructed in MEGA12 using the aligned sequences.

Tree-building settings:

| Parameter | Setting used |
|---|---|
| Software | MEGA12 |
| Alignment method | ClustalW |
| Sequence type | DNA |
| Tree-building method | Neighbor-Joining |
| Substitution model | Kimura 2-parameter |
| Bootstrap replicates | 1000 |
| Gaps/missing data treatment | Pairwise deletion |

The tree was generated from the multiple sequence alignment. The final tree included four taxa: three *Chlorella vulgaris* sequences and one *Chlorella emersonii* sequence.

![Neighbor-Joining phylogenetic tree in MEGA](images/tree.png)

Figure 4: Neighbor-Joining phylogenetic tree of *Chlorella vulgaris* and *Chlorella emersonii* sequences generated in MEGA12.

## Interpretation of the Phylogenetic Tree

The phylogenetic tree shows that the three *Chlorella vulgaris* sequences clustered together, while *Chlorella emersonii* was more distant. This result is expected because sequences from the same species should be more similar to each other than to a related but different species.

FR865658.1 and FR865660.1 clustered very closely together, with a bootstrap value of 99. This indicates strong support for this branch. FM205832.1 also grouped near the other *Chlorella vulgaris* sequences, while FR865661.1 formed a more distant branch.

Overall, the tree supports the expected relationship between the sequences: the *Chlorella vulgaris* sequences are more closely related to one another than to *Chlorella emersonii*.

## Summary

In this workflow, *Chlorella vulgaris* was selected as the target algal organism, and the 18S rRNA/ITS region was used as the barcode region. Related sequences were downloaded from NCBI and aligned in MEGA using ClustalW. Conserved regions, SNPs, and indels were identified from the alignment. Primers were designed using NCBI Primer-BLAST, and the selected primer pair produced an expected 638 bp amplicon. Finally, a Neighbor-Joining phylogenetic tree was constructed in MEGA using the Kimura 2-parameter model and 1000 bootstrap replicates.
