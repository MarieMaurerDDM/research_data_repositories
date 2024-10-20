# Research Data Repositories

Retrieve and visualize metadata from CLARIN research data repositories in Germany for an explorative study on linguistic research data.

## Project structure
* `/src`: Source code for downloading and saving OAI-PMH XML metadata to the system
  * `/dariah`: Dariah specific configuration for downloading records
  * `/clarin`: specific configuration for downloading records
  * `/refinements`: JSON files for OpenRefine
    * `/jobs_column`: JSON files describing OpenRefine jobs per column. Can be used to refine downloaded records following DCMI recommendations.
    * `/jobs_repository`: JSON files describing OpenRefine jobs per repository. Mainly for documentation purposes.
  * `/utils`: Shared functionality
  * `/visualizations`: Jupyter Notebooks holding visualization logic per repository.
  * `download_records.py`: Download records. Here you can specify which repositories to actually download.
* `/data`: Downloaded data (not committed) and refinement results (committed)
  * `/refined`: CSV results for each repository after refinement steps

### Setting up the environment

* Setting up a virtual environment in VSCode with Venv
* Install required dependencies (requirements.txt)
* To make sure locale imports (e.g. `src/utils`) work:
  * either add `src` to `PYTHONPATH` environment variable or
  * or add a `src.pth` file to `.venv/Lib/site-packages` containing the path to `src`

### Executing program

* Download records:
  1. Configure which data sources to download in `/download_records.py`
  2. Configure which repository to download in `/src/<repository>`
  3. Run `/download_records.py`
  4. Records will be saved in `/data/<data-source>/<repository>`
* Execute visualizations:
  1. Open Jupyter Notebooks in `/src/visualizations`
  2. Sequentially execute notebook cells to make sure, all modules are correctly initialized

## Authors

Marie Maurer / [GitHub](https://github.com/MarieMaurerDDM)
