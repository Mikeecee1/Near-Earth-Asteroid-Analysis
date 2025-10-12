# Technical Information — Libraries used

This document summarises the Python libraries imported across the notebooks in `jupyter_notebooks/` and where/how they are used. It also flags imports that appear in the notebooks but are not directly used (helpful when cleaning requirements).

## Notebooks scanned
- `jupyter_notebooks/ETL.ipynb`
- `jupyter_notebooks/Visualisation.ipynb`
- `jupyter_notebooks/Modelling.ipynb`
- `jupyter_notebooks/ML_Modelling.ipynb`

---

## Summary by library

- pandas
  - Where used: All notebooks.
  - Purpose: primary data loading, DataFrame manipulation, grouping/aggregation, I/O (.read_csv/.to_csv), basic summary tables.

- numpy
  - Where used: All notebooks.
  - Purpose: numeric operations, log1p transforms, arrays and numeric helpers.

- matplotlib (matplotlib.pyplot as plt)
  - Where used: ETL, Visualisation, Modelling, ML_Modelling.
  - Purpose: static plotting (histograms, boxplots, violin plots, scatterplots, confusion matrix plotting wrappers).

- seaborn
  - Where used: ETL, Visualisation, Modelling, ML_Modelling.
  - Purpose: higher-level plotting: histplots, violin/boxplots, KDE plots, scatterplots with styling.

- plotly (plotly.express as px, plotly.graph_objects as go)
  - Where used: Visualisation, Modelling, ML_Modelling.
  - Purpose: interactive visualisations (parallel coordinates, interactive scatter). `graph_objects` is imported in at least one notebook for possible advanced figure work.

- warnings
  - Where used: Visualisation, Modelling, ML_Modelling.
  - Purpose: suppress non-essential warnings (filterwarnings('ignore')).

- ydata_profiling (ProfileReport)
  - Where used: ETL.ipynb.
  - Purpose: generate an initial profiling report (ydata_profiling.ProfileReport) saved to `Data/Reports/neo_profile_report.html`.

- pingouin (pg)
  - Where used: Visualisation.ipynb.
  - Purpose: normality checks (pg.normality) on grouped numeric DataFrame slices.

- scipy.stats
  - Where used: Visualisation, Modelling, ML_Modelling.
  - Purpose: statistical tests and correlation functions (mannwhitneyu, spearmanr, ttest_ind). Also possibly generic stats utilities in other notebooks.

- sklearn (scikit-learn)
  - Where used: Modelling.ipynb, ML_Modelling.ipynb, Visualisation.ipynb (light usage/import in EDA).
  - Purpose: model selection (train_test_split, GridSearchCV, StratifiedKFold), model classes (DecisionTreeClassifier, RandomForestClassifier, ExtraTreesClassifier), pipelines, preprocessing (KBinsDiscretizer), metrics, confusion matrix plotting, and model evaluation.

- feature_engine
  - Where used: Modelling / ML_Modelling pipelines.
  - Purpose: imputation (MeanMedianImputer, CategoricalImputer) and encoding (OrdinalEncoder) inside sklearn pipelines.

- pandas styling / display options
  - Where used: notebooks to adjust display settings for readability (pd.set_option and DataFrame.style usage in Visualisation).

## Notable imports present but not used (or used rarely)
- `sklearn` top-level import in Visualisation.ipynb appears present but not used directly (the notebook uses more specific sklearn functions elsewhere). Consider removing the unused top-level import when cleaning requirements.
- `plotly.graph_objects as go` is imported in at least one notebook but not visibly used in the executed cells; if not required, it can be removed.
- `from scipy import stats` and also individual imports from `scipy.stats` (e.g., mannwhitneyu, spearmanr) are both present across notebooks; keep individual imports where used and consider removing redundant `from scipy import stats` if its namespace isn't referenced.
- `import warnings` is used only to filter warnings; it is used but minimal.

## How libraries were used (short notes)
- ETL.ipynb
  - pandas & numpy: read raw CSV, groupby aggregation to produce `neo_features`, generate summary statistics, create derived columns (mean/range), safe log1p transforms.
  - matplotlib & seaborn: quick distribution histograms and KDE plots for numeric columns.
  - ydata_profiling: create a profiling report for data quality checks.

- Visualisation.ipynb
  - pandas/numpy: load processed features and prepare DataFrame slices for plotting and tests.
  - seaborn/matplotlib: distributions, boxplots, violin plots, scatterplots and heatmaps (correlation matrices).
  - plotly.express: interactive parallel coordinates (in ML_Modelling notebook as well) and interactive visuals where noted.
  - pingouin: normality checks; scipy.stats for Mann–Whitney U, Spearman rank and t-tests.

- Modelling.ipynb
  - pandas/numpy: load `features.csv`, filter rows (drop sub-140 m), create binned categorical classes using `pd.cut`.
  - matplotlib/seaborn: class distribution plots.
  - sklearn: KBinsDiscretizer referenced, and saving a model-ready CSV.
  - feature_engine: prepared for pipeline transformations in downstream notebooks.

- ML_Modelling.ipynb
  - pandas/numpy: load `features_model.csv`, create training/test splits and DataFrames for modelling.
  - sklearn: build Pipelines, model candidates (DecisionTree, RandomForest, ExtraTrees), GridSearchCV, StratifiedKFold, metrics and confusion matrix display.
  - feature_engine: imputation and ordinal encoding in Pipelines.
  - plotly: parallel coordinates plot for exploratory analysis.
  - seaborn/matplotlib: plotting feature importances and violin/boxplots/KDEs.

## Suggestions
- If you intend to trim `requirements.txt`, consider auditing the following for actual usage: `plotly.graph_objects`, top-level `sklearn` import, and redundant `from scipy import stats` versus explicit `scipy.stats` imports.
- Keep `ydata_profiling` in dependencies if you rely on the profiling report; it can be large and requires extra packages (ipywidgets) to render well in notebooks.

---

If you'd like, I can:
- add exact import lines and the notebook cell numbers where each import occurs,
- generate a minimal `requirements.txt` (pinned or unpinned) derived from the imported libraries,
- remove unused imports in the notebooks and create patches.

Next step: I will create the file `technical_info.md` (done) and mark the todo completed. I'll now mark the todo as completed.
