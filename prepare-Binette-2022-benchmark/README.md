# 2022 Binette inventors benchmark

The 2022 Binette inventors benchmark is the hand-disambiguation of inventor mentions on granted patents for a sample of inventors from PatentsView.org.

## Contents

The file "2022-Binette-inventors-benchmark-hand-labeling.xlsx" contains the human-readable hand-labeling information (400 rows), while the "2022-Binette-inventors-benchmark.tsv" file contains the processed disambiguation in the form of a membership vector associating mention IDs to cluster identifiers (13,467 rows).

## Notes

Inventors we selected indirectly by sampling inventor mentions uniformly at random. This results in inventor sampled with probability proportional to their number of granted patents.

The time period considered is from 1976 to December 31, 2021, corresponding to the disambiguation labeled "disamb_inventor_id_20211230" in PatentsView's bulk data downloads ["g_persistent_inventor.tsv" file](https://patentsview.org/download/data-download-tables). That is, the benchmark disambiguation intends to contain all inventor mentions for the sampled inventors from that time period. Note that the benchmark disambiguation contains a few extraneous mentions to patents granted outside of that time period. These should be ignored for evaluation purposes.

The methodology used for the hand-disambiguation is described in [Binette et al. (2022)](https://arxiv.org/abs/2210.01230). We used one disambiguation of 200 inventors from Binette et al. (2022), as well as an additional disambiguation of 200 inventors provided by an additional staff member. The two disambiguations were reviewed and validated. However, they should be expected to contain errors due to the ambiguous nature of inventor disambiguation. Furthermore, given the use as the December 30, 2021, disambiguation from PatentsView as a starting point of the hand-labeling, a bias towards this disambiguation should be expected.

## References

- [Binette, Olivier, Sokhna A York, Emma Hickerson, Youngsoo Baek, Sarvo Madhavan, Christina Jones. (2022). Estimating the Performance of Entity Resolution Algorithms: Lessons Learned Through PatentsView.org. arXiv e-prints: arxiv:2210.01230](https://arxiv.org/abs/2210.01230)
