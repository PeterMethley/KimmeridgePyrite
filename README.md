# Using Pyrite to Explore the Diagenesis of the Kimmeridge Clay Formation
### *Peter Methley, March 2021*
## Python Code for Processing, Visualisation and Modelling of Geochemical Data

This code was written using Python 3.7 (from Anaconda) on Windows 10, using the JupyterLab IDE (https://jupyter.org/).

Packages required:
* `numpy`
* `pandas`
* `scipy`
* `ipywidgets`
* `plotly`
* `Pillow` (for image rendering)
* `kaleido` (for image export only)
* `nodejs` (for JupyterLab extensions)

In Anaconda/Miniconda, these can be installed using the terminal command `conda install ` followed by the name of the package.

To use the interactive functionality, the following JupyterLab extensions should be installed:
* `jupyterlab-plotly`
* `@jupyter-widgets/jupyterlab-manager`
* `plotlywidget`

These can be installed using the terminal command <br>
`jupyter labextension install jupyterlab-plotly @jupyter-widgets/jupyterlab-manager plotlywidget`

Once the packages are installed, the notebooks should be run from start to end in the following order:
1. **`S_Isotopes.ipynb`:** corrects the raw sulphur isotope data from `./Data/S_isotopes_raw.csv`using the true isotope ratios of the NBS-127 and S3 standards and outputs the corrected $\delta^{34}\mathrm{S}$ to `./Data/S_isotopes_processed.csv`

2. **`Data_Amalgamation.ipynb`:** This combines the corrected $\delta^{34}\mathrm{S}$ with the iron speciation data from `./Data/Fe_speciation.csv` and qualitative data from `./Data/Qualitative_info.csv`, calculates various ratios and errors, then outputs the final data-table to `./Data/Log_data_combined.csv`. Graphs of stratigraphic variations are also plotted, along with a customisable bivariate plot.

3. **`Iron_Model.ipynb`:** creates the iron speciation cross-plot, and models the evolution of the data as H<sub>2</sub>S is added under sulphide-limited conditions.

4. **`S_Model.ipynb`:** This contains the steady-state reactive transport model that predicts the pyrite concentrations and sulphur isotopes under varying conditions.

(*Note that 3 and 4 can be run in either order, and any notebook can be run once the processed data `.csv` files have been created*)

If you cannot run JupyterLab, the notebooks (albeit without the interactive graphs) are available in HTML format in the `./HTML_Notebooks` folder. These files should be openable in any browser.