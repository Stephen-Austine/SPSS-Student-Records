# SPSS Student Records

A small, reproducible SPSS (`.sav`) dataset for learning how to define and
document variables. It contains five student records and five variables,
with a mix of nominal, ordinal, and scale measurement levels.

The project also includes a command-line inspection utility and automated
tests that verify the dataset's shape, missing values, summaries, and value
labels.

## Table of contents

- [Dataset overview](#dataset-overview)
- [Learning objectives](#learning-objectives)
- [Project structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Inspecting the data](#inspecting-the-data)
- [Working in IBM SPSS](#working-in-ibm-spss)
- [Using the dataset in Python](#using-the-dataset-in-python)
- [Tests and validation](#tests-and-validation)
- [Data quality and privacy](#data-quality-and-privacy)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Dataset overview

The data file is [`data/dataset_1A.sav`](data/dataset_1A.sav). It contains:

| Property | Value |
| --- | --- |
| Records (cases) | 5 |
| Variables (columns) | 5 |
| Missing values | None |
| Format | IBM SPSS Statistics `.sav` |

### Data dictionary

| Variable | Label | SPSS measurement level | Encoding or value labels |
| --- | --- | --- | --- |
| `Name` | `initials` | Nominal | Initials stored as text |
| `Age` | `in years` | Scale | Numeric age in years |
| `place_of_Residence` | *(not set)* | Nominal | Residence stored as text |
| `School_year` | *(not set)* | Ordinal | `2 = sophomore`, `3 = junior` |
| `Grade_Statistics` | *(not set)* | Ordinal | `0 = F`, `1 = E`, `2 = D`, `3 = C`, `4 = B`, `5 = A` |

### Basic summaries

- Ages range from 22 to 35 years.
- Mean age is 28.0 years.
- The `Grade_Statistics` values use numeric codes 0 through 5.
- Mean numeric grade code is 3.6.
- The SPSS value-label metadata translates the grade codes to letter grades.
- `School_year` codes 2 and 3 are labelled `sophomore` and `junior`.

The numeric representation is intentional. Ordinal grades and school years can
be stored as numbers in SPSS while a value label makes each code readable in
the Data View, output, and Variable View.

## Learning objectives

This repository is designed to demonstrate how a data analyst should:

1. Distinguish nominal, ordinal, and scale variables.
2. Give variables clear names and descriptive labels.
3. Use numeric codes for ordered categories.
4. Attach human-readable value labels to category codes.
5. Check row count, column count, missing values, and summary statistics.
6. Preserve variable metadata when exporting or reopening a `.sav` file.
7. Inspect SPSS files from a terminal without requiring the SPSS desktop
   application.

### Measurement-level guide

| Level | Use for | Example in this dataset |
| --- | --- | --- |
| Nominal | Categories with no meaningful order | `Name`, `place_of_Residence` |
| Ordinal | Categories with a meaningful order | `School_year`, `Grade_Statistics` |
| Scale | Numeric measurements suitable for a continuous scale | `Age` |

When preparing or reviewing data in SPSS, use **Measure** in Variable View:

- **Nominal** for categories that do not have a natural order.
- **Ordinal** for categories whose order matters.
- **Scale** for numeric quantities such as age or height.

## Project structure

| Path | Purpose |
| --- | --- |
| [`data/dataset_1A.sav`](data/dataset_1A.sav) | Source SPSS dataset with five cases and five variables |
| [`inspect_sav.py`](inspect_sav.py) | Reads one or more `.sav` files and prints metadata and a preview |
| [`tests/test_data.py`](tests/test_data.py) | pytest checks for shape, missing values, summaries, and labels |
| [`requirements.txt`](requirements.txt) | Runtime and test dependencies |
| [`pyproject.toml`](pyproject.toml) | pytest and Ruff configuration |
| [`LICENSE`](LICENSE) | MIT license |

## Requirements

- Python 3.10 or newer
- pip
- A terminal or command prompt
- IBM SPSS Statistics if you want to edit the file in the SPSS desktop interface

No SPSS installation is required to inspect or test the file from Python.
`pyreadstat` reads the SPSS binary format directly.

The Python dependencies are:

| Package | Purpose |
| --- | --- |
| `pandas` | Tabular data and basic DataFrame operations |
| `pyreadstat` | Reading `.sav` files and SPSS variable metadata |
| `tabulate` | Rendering the optional Markdown or text tables |
| `pytest` | Running the automated test suite |

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/<your-username>/spss-student-records.git
cd spss-student-records
```

Create and activate a virtual environment.

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Windows (PowerShell)

```powershell
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks virtual-environment activation, open PowerShell as your
user and run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then activate the environment again.

## Quick start

After installing the dependencies:

```bash
# Inspect the dataset
python inspect_sav.py data/dataset_1A.sav

# Print a Markdown data dictionary
python inspect_sav.py --markdown data/dataset_1A.sav

# Run all tests
python -m pytest
```

An interpreter is not started when you execute `inspect_sav.py`; the script
prints directly to standard output.

## Inspecting the data

### Text output

```bash
python inspect_sav.py data/dataset_1A.sav
```

Text mode prints:

1. The filename and dimensions.
2. One row in a data-dictionary table for every variable.
3. Each variable's label, measurement level, missing-value count, and labels.
4. The first five records as a preview.

### Markdown output

```bash
python inspect_sav.py --markdown data/dataset_1A.sav
```

Markdown mode is suitable for pasting output into documentation or issue
reports. Unlike text mode, it does not add a DataFrame preview.

### Inspect multiple files

The script accepts more than one path:

```bash
python inspect_sav.py data/dataset_1A.sav data/another_dataset.sav
python inspect_sav.py --markdown data/dataset_1A.sav data/another_dataset.sav
```

For a missing or unreadable file, the script reports the underlying
`pyreadstat`/filesystem error. Verify the path and file extension first.

## Working in IBM SPSS

To open the dataset in the SPSS desktop application:

1. Choose **File > Open > Data**.
2. Select [`data/dataset_1A.sav`](data/dataset_1A.sav).
3. Open **Variable View** to inspect variable names, labels, types, measures,
   and value labels.
4. Open **Data View** to inspect the five cases and category codes.

### Reviewing value labels

The value labels are metadata stored in the `.sav` file. In SPSS:

1. Open **Variable View**.
2. Select `School_year` or `Grade_Statistics`.
3. Open the value-label editor for that variable.
4. Confirm that each numeric code has the intended descriptive label.

To display labels in SPSS views and output, enable the appropriate
**Value Labels** display option. Numeric values remain the underlying encoded
data; they do not become text permanently.

### Editing or exporting

If you modify the dataset in SPSS, save it as a new `.sav` file and keep the
original unchanged. When exporting to CSV, remember that:

- Value labels may not be exported with the data.
- The output may contain numeric codes instead of grade names.
- Column labels and SPSS measurement levels are `.sav` metadata, not a CSV
  standard feature.
- Missing-value definitions should be documented separately.

## Using the dataset in Python

### Load data and metadata

```python
import pyreadstat

df, meta = pyreadstat.read_sav("data/dataset_1A.sav")

print(df)
print(df.shape)
print(df.dtypes)
```

`df` is a pandas `DataFrame`. `meta` contains SPSS metadata returned by
`pyreadstat`.

### Inspect variable labels and levels

```python
import pyreadstat

_, meta = pyreadstat.read_sav("data/dataset_1A.sav")

for name in meta.column_names:
    print(name)
    print("  label:", meta.column_names_to_labels.get(name))
    print("  measure:", meta.variable_measure.get(name))
    print("  value labels:", meta.variable_value_labels.get(name, {}))
```

### Read value labels

```python
import pyreadstat

_, meta = pyreadstat.read_sav("data/dataset_1A.sav")

print(meta.variable_value_labels["School_year"])
# {2.0: "sophomore", 3.0: "junior"}

print(meta.variable_value_labels["Grade_Statistics"])
# {0.0: "F", 1.0: "E", 2.0: "D", 3.0: "C", 4.0: "B", 5.0: "A"}
```

### Summarize and check missing values

```python
import pyreadstat

df, _ = pyreadstat.read_sav("data/dataset_1A.sav")

print("Shape:", df.shape)
print("Missing values:", df.isna().sum().to_dict())
print("Mean age:", df["Age"].mean())
print("Mean grade code:", df["Grade_Statistics"].mean())
```

## Tests and validation

The test configuration in [`pyproject.toml`](pyproject.toml) enables the
repository's `tests/` directory and makes the project root importable.

Run the suite from the repository root:

```bash
python -m pytest
```

For a concise pass/fail summary:

```bash
python -m pytest -q
```

The current tests verify:

- The dataset contains exactly five rows and five columns.
- It has no missing values.
- Mean age is 28.0.
- Mean statistics grade code is 3.6.
- `School_year` maps code 2 to `sophomore` and code 3 to `junior`.
- `Grade_Statistics` maps code 5 to `A`.

You can rerun tests after changing the `.sav` file or inspection logic.
For a failing test, inspect the exact assertion and compare it with the data,
metadata, or test fixture.

## Data quality and privacy

The dataset is intentionally small and is intended for instructional use.
It is not a production student information system.

Before sharing or publishing derived data:

- Review whether `Name` contains real participants or identifiable initials.
- Remove or replace identifiers if a record may be linked to a person.
- Do not publish the data with sensitive contact, financial, health, or
  academic details.
- Verify that the source owner has approved publication.
- Add provenance and collection context if you distribute a derived version.
- Document any data cleaning or replacement of missing values.

If values are approximate or fabricated, label the dataset as synthetic or
teaching data rather than as authoritative student records.

## Troubleshooting

### `python` is not found

Use `python3` on macOS/Linux:

```bash
python3 --version
python3 inspect_sav.py data/dataset_1A.sav
```

On Windows, use the Python launcher:

```powershell
py -3.10 --version
py -3.10 inspect_sav.py data/dataset_1A.sav
```

### `ModuleNotFoundError: No module named 'pandas'`

Ensure the virtual environment is active, then install the requirements:

```bash
python -m pip install -r requirements.txt
```

### `pyreadstat` installation fails

Confirm that you are using Python 3.10 or newer, upgrade pip, and retry:

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

### The file cannot be found

Run commands from the repository root or provide an absolute path:

```bash
python inspect_sav.py /full/path/to/dataset_1A.sav
```

On macOS/Linux, verify the relative path with:

```bash
ls data
```

### Markdown output is not available

Ensure `tabulate` is installed:

```bash
python -m pip install tabulate
```

This package is also included in `requirements.txt`.

## License

This project is released under the [MIT License](LICENSE). The license notice
applies to the repository code and documentation. Confirm the rights and
privacy requirements for any dataset before redistributing it.
