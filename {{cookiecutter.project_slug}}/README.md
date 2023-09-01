# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Usage

### Install dependencies

```bash
pip install -r requirements.dev.txt
conda env create -f conda_env.yaml
```

### Run the project

```bash
mlflow run .
```

## Project structure

```
├── data                # Data files for the project. (e.g. csv, json, etc.)
│   ├── models              # Trained and serialized models, model predictions, or model summaries.
│   ├── external            # Data from third party sources.
│   ├── interim             # Intermediate data that has been transformed.
│   ├── processed           # The final, canonical data sets for modeling.
│   └── raw                 # The original, immutable data dump.
├── docs                # Documentation for the project.(e.g. data dictionaries, manuals, etc., Markdown)
├── src                 # Source code for use in this project.
├── scripts             # Scripts for common tasks, e.g. running the model.
├── notebooks           # Jupyter notebooks. Naming convention is a number (for ordering, e.g., 01.preprocess.ipynb, 02.train.ipynb, 03.evaluate.ipynb, etc.)
├── references          # Papers, reference manuals, and all other explanatory materials.
├── reports             # Reports and presentations.(e.g. md, pdf, html, etc.)
│   └── figures             # Generated graphics and figures to be used in reporting.
├── requirements.dev.txt# The requirements file for reproducing the analysis environment, e.g.
├── conda_env.yaml      # The requirements file for reproducing the analysis environment, e.g.
├── MLproject           # The MLflow project file that describes the project structure and dependencies.
├── README.md           # This file.
├── main.py             # The main entry point for the project.(use MLflow to run)
├── noxfile.py          # Configuration of the Nox automation tool.
├── .pre-commit-config.yaml # Configuration of the pre-commit tool.
```

## References

- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [mlflow](https://mlflow.org/)
