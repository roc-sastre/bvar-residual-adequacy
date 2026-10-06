# Computational success and residual-adequacy limits in a small US Bayesian VAR

Roc Sastre. Research note, 6 October 2026.

This diagnostic replication package supports the note's application-specific diagnostic argument:
successful computation, monitored convergence and structural precision did not
clear the residual conditions required for substantive interpretation. Material
discrepancies and unresolved predictive cutoffs retain their distinct meanings.

## Scope and verification

Read the frozen [PDF](manuscript/research_note.pdf) or [source](manuscript/research_note.tex).
[Diagnostic records](diagnostic_records.json) transcribe every approved table row,
map principal claims to preserved evidence IDs, and project four diagnostic gate
flags. [Provenance](PROVENANCE.md) explains the source chain and limitations.

Run `python -B validate.py` from this directory using Python 3.10 or later.
The validator needs only the standard library, reads only this package, performs
no network access and writes no outputs. It verifies the exact file inventory,
hashes, frozen row transcriptions, claim-map structure and withholding flags.
Keep `.gitattributes` when exporting this folder as a new repository: its `-text`
rule preserves the approved bytes across Git checkouts, including on Windows.
Checksums detect changes relative to this manifest; they are not signatures or
an independent guarantee against coordinated replacement of files and manifest.

This is preserved-record verification. It does not reproduce estimation,
sampling, residual diagnostic calculations or historical replay from inputs.
Historical independent reconstructions are attestations in the frozen evidence
chain. The private inputs cannot be recovered from this package. Each scientific
quantity exposed here was already approved in the frozen note or its evidence
chain; validation creates no new scientific quantity.

## Withheld-response policy

Substantive impulse-response estimates, plots, distributions, response-event
probabilities and response objects remain withheld. Posterior draws and parameter
objects allowing their recovery are excluded. Aggregate Monte Carlo precision
and spectral-root diagnostics in the note are admissible diagnostic evidence.
Impact signs describe imposed restrictions, not estimated economic findings.

## Environment

Static verification: Python standard library; no third-party Python dependency.
Optional manuscript compilation: pdfLaTeX with article, fontenc, inputenc,
lmodern, geometry, amsmath, amssymb, booktabs, array, tabularx, longtable,
hyperref and microtype. The bibliography is embedded and there are no image,
external bibliography or data dependencies. Compilation can alter PDF bytes;
the shipped approved PDF is the immutable reference. Do not replace it.

Historical evidence environment, as recorded in the note: MATLAB R2026a Update 5,
PCWIN64, Statistics toolbox 26.1. That environment and its software are not
distributed and are not required for this package's static verification.
Exact historical equality does not imply portability to arbitrary environments.

## Licences and release status

Copyright 2026 Roc Sastre. The following file-specific licence map applies:

| Material | Licence |
|---|---|
| `validate.py` | MIT; see [MIT licence](LICENSE-MIT.txt) |
| `manuscript/research_note.tex`, `manuscript/research_note.pdf`, `README.md`, `PROVENANCE.md`, `CITATION.cff`, `MANIFEST.json`, `diagnostic_records.json` | Creative Commons Attribution 4.0 International; see [CC BY 4.0 licence](LICENSE-CC-BY-4.0.txt) |
| `.gitattributes` | MIT |

Licence texts retain their own notices. Cite Roc Sastre and the research note,
link to the applicable licence, and indicate changes as required by that licence.
The licences apply only to the distributed material, not to withheld inputs,
third-party papers, software or private research records.

Public repository: https://github.com/roc-sastre/bvar-residual-adequacy.
[Release v1.0.0](https://github.com/roc-sastre/bvar-residual-adequacy/releases/tag/v1.0.0)
archives verified commit `92fa3adf19a558ffb713e6a9cd9a4d889bf3864b`.
Version-specific archive DOI: [10.5281/zenodo.23195194](https://doi.org/10.5281/zenodo.23195194).
[Zenodo record](https://zenodo.org/records/23195194) preserves the exact eleven-file
release payload; the PDF attached to the GitHub Release has the frozen checksum.
This DOI identifies the diagnostic replication package, not a separate journal
publication. DOI metadata was added after release in one follow-up commit, with
manifest hashes updated; the v1.0.0 tag and its frozen package are unchanged.
The author’s existing personal website will receive a separate research-note
entry through a reviewed pull request; the historical thesis entry is preserved.

Only this sanitized package may be copied into a new repository with fresh Git
history. The private research repository and its history are excluded.
