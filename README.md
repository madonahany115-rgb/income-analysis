# Income Analysis with Pandas

## Project Overview

This project focuses on exploring, cleaning, analyzing, and preparing an income dataset using Python and Pandas.

The main target column is `Income`.

## Project Structure

```text
income-analysis/
│
├── data/
│   ├── row/
│   │   └── data.csv
│   │
│   └── processed/
│       └── cleaned_data.csv
│
├── income_analysis.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Dataset

The original dataset is stored in:

`data/row/data.csv`

The cleaned and processed dataset is stored in:

`data/processed/cleaned_data.csv`

## Data Analysis

The project includes:

* Dataset exploration
* Data types and missing-value analysis
* Duplicate detection and removal
* Categorical data exploration
* Missing-value handling
* Income analysis using `groupby()`
* Average income analysis across different categories
* IQR-based outlier detection
* Gender encoding
* One-Hot Encoding
* Exporting the processed dataset

## Outlier Detection

Potential outliers were investigated using the Interquartile Range (IQR) method for:

* Age
* Number of Dependents
* Work Experience
* Household Size
* Income

Income outliers were reported rather than automatically removed.

## Before and After

### Before

The original dataset is available in:

`data/row/data.csv`

### After

The processed dataset is available in:

`data/processed/cleaned_data.csv`

The processed data contains encoded categorical variables and is prepared for further analysis or machine learning tasks.

## Technologies

* Python
* Pandas

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

Run the analysis script using:

```bash
python income_analysis.py
```
