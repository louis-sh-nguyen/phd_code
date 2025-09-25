# Supplementary Code & Data for PhD Thesis

This repository contains the code, scripts, and datasets that support the analyses and figures in the PhD thesis:

- **Title**: Advanced Measurement and Modelling of Permeation and Sorption of CO₂ in Engineering Polymers  
- **Author**: Louis Nguyen  
- **Supervisors**: Dr. Christopher James Tighe, Prof. Amparo Galindo, Prof. George Jackson

## Requirements
- Conda (Anaconda or Miniconda)
- Git (optional)
- Python 3.12+

Core Python libraries (installed via the environment file):
- NumPy, Pandas, SciPy, Matplotlib

## Quick Start

1. Clone the repository and enter the project folder:

```bash
git clone https://github.com/louis-sh-nguyen/phd_code.git
cd phd_code
```

2. Create and activate the conda environment:

```bash
conda env create -f environment.yml
conda activate permeation-env
```

3. Extract any `.zip` archives found in the `data/` subfolders (place each archive's contents alongside the `.zip` file).

4. Launch JupyterLab or Jupyter Notebook and run the notebooks in the chapter folders:

```bash
jupyter notebook
```

## Project layout (top-level)

```
phd_code/
├── environment.yml
├── LICENSE
├── README.md
├── thesis.mplstyle
├── Chapter4_Crystallinity-measurement/
│   ├── analysis-notebooks/
│   ├── data/
│   └── plotting-notebooks/
├── Chapter5_Solubility-modelling/
│   ├── data/
│   └── plotting-notebooks/
├── Chapter6_Solubility-measurement/
│   ├── data/
│   └── plotting-notebooks/
└── Chapter7_Permeation-measurement-modelling/
    ├── data/
    └── plotting-notebooks/
```

(See the repository for the full, detailed tree and files.)

## Related repositories

- Chapter 4 (Crystallinity): https://github.com/louis-sh-nguyen/polymer-characterisation  
- Chapter 5 (Solubility modelling): https://github.com/louis-sh-nguyen/NE_SAFT  
- Chapter 6 (Solubility measurement): https://github.com/louis-sh-nguyen/rubotherm_EOS  
- Chapter 7 (Permeation analysis): https://github.com/louis-sh-nguyen/object-oriented-pemeation-analysis  
- GUI guide for permeation app: https://imperialcollegelondon.github.io/ReCoDe-permeation-analysis-app/

## Contact
- Email: louis.sh.nguyen@gmail.com  
- LinkedIn: https://www.linkedin.com/in/louis-sh-nguyen/
