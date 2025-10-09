
# Near Earth Asteroid Analysis 🪐 

### Project Overview

This project explores NASA’s Near-Earth Object (NEO) dataset, focusing on asteroids that come within close proximity to Earth.
Using publicly available data from NASA’s JPL Center for Near-Earth Object Studies (CNEOS) and downloaded from [Kaggle](https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects), this analysis investigates the physical and orbital characteristics that influence whether an asteroid is classified as potentially hazardous.


# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content
* The dataset includes key attributes such as estimated diameter, relative velocity, miss distance, and absolute magnitude of over 27000 asteroids with 90000 observations.
Additional features have been added (based upon the original data). For example number of observations per object, was engineered to capture tracking frequency and observation density.

### Columns in `Data/Raw/neo.csv` (source file)

- `id` — integer unique identifier for the NEO .
- `name` — object name or designation (string). Comprises an identifier and the year first observed.
- `est_diameter_min` — estimated minimum diameter (kilometres).
- `est_diameter_max` — estimated maximum diameter (kilometres).
- `relative_velocity` — relative approach velocity ( km/h).
- `miss_distance` — miss distance at close approach.
- `orbiting_body` — the body the object is approaching (`Earth`). 
- `sentry_object` — boolean indicating whether the object is listed on the [Sentry Risk Table](https://cneos.jpl.nasa.gov/sentry/).
- `absolute_magnitude` — absolute magnitude H (brightness; lower = brighter/larger).
- `hazardous` — boolean flag for potentially hazardous status (True/False).

### Feature Engineered Columns

- `est_diameter_mean`(min + max) / 2 -	Represents the best single-value estimate of asteroid size
- `diameter_range`(max − min) - Indicates uncertainty or shape variability
- `relative_velocity`(mean) - average relative velocity across observations
- `absolute_magnitude`(mean) - average magnitude across observations
- `observations` - aggregated for each object (range 1-43)
- `hazardous_enc` - encoded hazardous status (1 for True, 0 for False)

### Log-transformed columns (added to `Data/Processed/features.csv`)

To stabilise variance and reduce heavy right-skew in several distance/size/velocity columns I added safe, non-destructive log transforms in the processed features file. 
- `est_diameter_min_log1p`, `est_diameter_max_log1p` — log1p of original diameter bounds (km). Useful for plotting and linear-model inputs.
- `est_diameter_mean_log1p`, `est_diameter_range_log1p` — log1p of the derived mean and range of diameter; compresses extreme values and reduces influence of large outliers.
- `relative_velocity_mean_log1p` — log1p of average relative approach velocity; helps visualisation and models when velocity varies across orders of magnitude.
- `miss_distance_mean_log1p`, `miss_distance_min_log1p` — log1p of miss distances to compress the very large distance scale and reveal structure at smaller scales.

- These transformed columns are kept alongside the originals so as to choose the most appropriate representation for modelling or visualisation. 

- All transformations are documented in `jupyter_notebooks/ETL.ipynb` so the pipeline is reproducible and auditable.

### saved datasets & columns

**Observations (observations.csv)**
* name
* est_diameter_min
* est_diameter_max
* relative_velocity
* miss_distance
* absolute_magnitude
* hazardous
* observations

**Features (features.csv)**
* name
* est_diameter_min
* est_diameter_max
* relative_velocity_mean
* miss_distance_mean
* miss_distance_min
* absolute_magnitude_mean
* hazardous
* observations
* est_diameter_range
* est_diameter_mean
* est_diameter_min_log1p
* est_diameter_max_log1p
* est_diameter_mean_log1p
* est_diameter_range_log1p
* relative_velocity_mean_log1p
* miss_distance_mean_log1p
* miss_distance_min_log1p*
* hazardous_enc


## Business Requirements

The requirements of the project are to:

* Identify potentially dangerous asteroids
    - Detail: Use the hazard flag and derived metrics (size, miss distance, velocity) to identify potentially hazardous objects. 

* Investigate which physical properties contribute to hazardous status
    - Detail: Run hypothesis tests and simple predictive models to quantify how diameter, velocity and miss distance relate to the `hazardous` label. Include uncertainty estimates and effect sizes.
    
* Understanding these properties may help to mitigate the threats posed
    - Detail: Summarise practical implications of the findings (e.g., which features most strongly drive risk scores) and note limitations for operational use.
    

Hazardous asteroids may:
* Be a direct threat to Earth if large enough
    - Context: Large bodies with small miss distances present the highest theoretical risk; however, this project's size estimates are approximate and should be treated as indicative only.
   
* Disrupt communications and other satellites
    - Context: Objects that intersect LEO/GEO-altitude orbits are of interest for satellite operators. 

* Be a threat to other near earth objects e.g. space telescopes
    - Context: Secondary effects (debris, close passes) may pose risk to valuable space assets; this project only flags potential concerns for further study.
    

### Scope, audience, and disclaimer

- Purpose: This repository is a small, educational training project intended to demonstrate data engineering, exploratory analysis, and basic predictive modelling techniques using an open NEO dataset. It is not intended for operational, commercial, or scientific decision-making.
- Intended audience: students, data-science learners, and reviewers interested in reproducible analysis workflows.
- Non-operational disclaimer: analyses, visualisations, and models produced here are exploratory. They are not validated for policy, emergency response, or mission planning. Any real-world interpretation should rely on authoritative sources (e.g., NASA/JPL CNEOS) and domain expert review.
- Success criteria (project): reproducible ETL producing clean datasets, documented hypothesis tests and EDA, baseline model with evaluation metrics, and clear documentation (README, reports, ethics note).



## **Hypothesis and how to validate?**

The hypotheses for this project are as follows:
* #### **Physical and Predictive Hypotheses** 🚀
    * **Larger asteroids** (greater estimated diameters) are more likely to be classified as hazardous.
        * **Validation**
            1. Compare diameter distributions between hazardous vs non-hazardous objects with a boxplot / violin plot.
            2. Run a two-sample test (Mann–Whitney U if non-normal, t-test if approx normal) to check median/mean differences.
            3. Fit a simple logistic regression: is_hazardous ~ log(diameter). Check coefficient sign, p-value, and AUC.
        * **Supportive result**: Hazardous group has significantly larger diameters (p < 0.05) and positive diameter coefficient in logistic regression with meaningful effect size

    * **Closer approaches to Earth** (smaller miss distances) are associated with a higher likelihood of hazard classification.
        * **Validation**
            1. Visualize miss distance distributions by hazard status
            2. Use Mann–Whitney U or t-test for distance differences.
            3. Logistic regression
        * **Supportive result**: Hazardous asteroids concentrate at smaller miss distances (statistically significant) and miss_distance has a negative, significant logistic coefficient.

    * **Higher relative velocities** correlate with greater hazard potential (due to increased impact energy).
        * **Validation**
            1. Plot velocity distributions by hazard status.
            2. Statistical test (Mann–Whitney U / t-test).
            3. Logistic regression
        * **Supportive result**: Hazardous objects show significantly higher relative velocities
    * **Absolute magnitude** (brightness) inversely correlates with hazard level — brighter (larger) objects are more likely to be hazardous. 
        * **Validation**
            1. Visualize H by hazard status.
            2. Test difference with Mann–Whitney U / t-test.
            3. Logistic regression: hazardous ~ -absolute_magnitude (or use H and expect negative coefficient)
        * **Supportive result**: Supportive result: Hazardous asteroids have lower median H (statistical significance) and H coefficient indicates brighter objects increase hazard odds.

    * A combination of **size**, **speed**, and **miss distance** can effectively predict hazard status.
        * **Validation**
            1. Train a multivariate classifier (logistic regression, random forest, or XGBoost) using those features.
            2. Use cross-validation and report AUC, precision, recall, and calibration (reliability plot).
            3. Run ablation: compare model using all three vs models using subsets 
        * **Supportive result**: Multivariate model achieves substantially higher AUC (e.g., >0.80 if baseline is ~0.5–0.6) and ablation shows each feature contributes measurable lift.

* #### **Observational Hypotheses** 🔭
    * NEOs with more recorded **observations** tend to be closer and larger.
        * **Validation**
            1. Scatter plots: observation_count vs miss_distance and observation_count vs diameter (use log scales).
            2. Compute Spearman correlation (robust to nonlinearity) for observation_count with miss_distance and with diameter.
            3. Regress observation_count (or log count) on miss_distance and diameter to quantify effects.
        * **Supportive result**: Negative Spearman for observation_count vs miss_distance, positive Spearman vs diameter (both significant).

    * **Potentially hazardous asteroids** are observed more frequently due to higher monitoring priority.
        * **Validation**
            1. Compare observation_count distributions by hazard status (boxplot/histogram).
            2. Mann–Whitney U / t-test to check difference.
            3. Poisson or negative binomial regression: observation_count ~ is_hazardous + controls (e.g., discovery_year) to estimate incidence rate ratio..
        * **Supportive result**: Hazardous objects have higher median observation counts and hazard indicator has a positive, significant rate ratio.

    * There is a positive correlation between the number of **observations** and an asteroid’s **brightness** or **size**.
        * **Validation**
            1. Calculate Spearman correlations for observation_count vs H and observation_count vs diameter.
            2. Visualize with binned summaries (median diameter per log observation_count bin).
            3. 
        * **Supportive result**: Positive correlation with diameter and negative correlation with H (remembering H scale), both significant.


    * (*Note: H = Absolute Magnitude, scale direction: lower H = brighter/larger* )



## Project Plan


This project plan maps work into clear phases, links each phase to the notebooks and files in this repository, and lists deliverables and acceptance criteria so progress can be tracked against the project board.

### Phases & mapping

- Phase 1 — Data collection & ETL
    - Files / notebooks: `jupyter_notebooks/ETL.ipynb`, `Data/Raw/neo.csv`
    - Tasks: confirm data provenance, standardise types and units, impute or document missing values, engineer base features, and write versioned processed outputs to `Data/Processed/`.
    - Deliverables: `Data/Processed/neo_clean.csv`, `Data/Processed/neo_features.csv`.
    - Acceptance criteria: raw file backed up, processed files produced, validation report created with row counts and missingness, and unit conversions documented.

- Phase 2 — Exploratory Data Analysis (EDA)
    - Files / notebooks: `jupyter_notebooks/Modelling.ipynb` (EDA sections) and `jupyter_notebooks/Visualisation.ipynb`
    - Tasks: visualise distributions, test primary hypotheses (see Hypotheses section), and produce figures for the dashboard.
    - Deliverables: EDA notebooks with plots, summary figures saved to `reports/figures/`, and a short findings document.
    - Acceptance criteria: figures are reproducible from processed data and include captions, axes, and uncertainty where relevant.

- Phase 3 — Modelling & validation
    - Files / notebooks: `jupyter_notebooks/Modelling.ipynb`
    - Tasks: build predictive models (logistic regression, random forest), evaluate via cross-validation, and produce model diagnostics and calibration plots.
    - Deliverables: model notebook, saved model artefacts (if used), evaluation metrics and an entry in `reports/` explaining model limitations.
    - Acceptance criteria: model reproducibility, stratified CV reported, AUC/PR metrics documented, and clear failure modes described.

- Phase 4 — Dashboard & visual story
    - Files / notebooks: `jupyter_notebooks/Visualisation.ipynb`, `dashboard/` (if created)
    - Tasks: design user-facing visualisations to communicate key insights for technical and non-technical audiences, prepare narrative and captions.
    - Deliverables: interactive dashboard or static figure set, README instructions for running the dashboard.
    - Acceptance criteria: visuals annotated, accessible (alt text), and tested on a small sample dataset.

- Phase 5 — Documentation & Deployment
    - Files: `README.md`, Jupyter Notebooks (`ETL.ipynb`,`Visualisation.ipynb`,`Modelling.ipynb`) and a dashboard  for deployment
    - Tasks: finalize documentation and deploy (optional) to Heroku or other platform.
    - Deliverables: polished README  and working deployment instructions.
    - Acceptance criteria: repository is self-contained for a reviewer to reproduce the main result following the README.

### Timeline & milestones

- Milestone 1: ETL complete and processed datasets available (linked on project board).
- Milestone 2: EDA visualisations and hypothesis tests complete.
- Milestone 3: Baseline predictive model built and validated.
- Milestone 4: Dashboard / visual story prepared and documented.
- Milestone 5: Final report, ethics note, and deployment documentation completed.

## Glossary

* **neo** - near earth object, classified as an object which can pass within 45m km of the earth's orbit
* **h** - The absolute magnitude (intrinsic brightness) of an object (Inverted scale)
* **GEO** -  Geostationary Equatorial Orbit
* **LEO** - Low Earth Orbit
* **AU** - Astronomical Unit - based upon the earth's average distance from the sun (roughly 150m km)





## The rationale to map the business requirements to the Data Visualisations
* List your business requirements and a rationale to map them to the Data Visualisations

## Analysis techniques used
* List the data analysis methods used and explain limitations or alternative approaches.
* How did you structure the data analysis techniques. Justify your response.
* Did the data limit you, and did you use an alternative approach to meet these challenges?
* How did you use generative AI tools to help with ideation, design thinking and code optimisation?

## Ethical considerations
* Privacy and personal data
    * The dataset is astronomical and does not contain personal data.
* There are few ethical or societal issues regarding this project.
    * Legal and ethical consderations would be covered by the [Space Treaty](https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/introouterspacetreaty.html) under the governance of the UN.
* Dual use and misuse
    * Near-Earth object (NEO) analysis could inform planetary defense policy or, in theory, be misused in other contexts - e.g. exploitation of resources, misinformation regarding threat (sensationlism).
However, this project is an exploration of already existing and publicly available data and is unlikely to pose any ethical issues.

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
* How were data insights communicated to technical and non-technical audiences?
* Explain how the dashboard was designed to communicate complex data insights to different audiences.

### Dashboard wireframes (brief)

Below are four concise wireframes for a compact dashboard. Each wireframe includes purpose, main widgets, data sources, interactions, and acceptance criteria. These are framework-agnostic and can be implemented with Plotly Dash, Streamlit, Voila, or a static report.

1) Overview / Home
     - Purpose: At-a-glance summary of dataset.
     - Main widgets:
         - Header with project title.
         - KPI cards: Total NEOs, # Potentially Hazardous (PHA), Average estimated diameter, closest approaches.
         - Hazard ranking table (top 10) with sortable columns: `id`, `name`, `est_mean_diameter`, `miss_distance_min_km`, `relative_velocity_km_s`, `hazardous`.
         - Small global map or scatter with points sized by diameter and coloured by hazard flag (hover shows quick stats).
     - Interactions: Click a row in hazard table opens Object Detail pane; filter bar (hazardous only, diameter min, miss distance max).
     

2) Object Detail (drill-down)
     - Purpose: Show complete known history and metrics for a single NEO.
     - Main widgets:
         - Title with `name` and `id`, hazard flag and key stats (diameter range, mean, kinetic energy proxy).
         - Model explainability panel: feature importance for this object (if per-object prediction), and a short natural-language explanation.
     - Interactions: Hover for per-event details;
     - Data sources: per-approach records (if available) or aggregated fields from `neo_features`.
     

3) Models & Evaluation
     - Purpose: Present modelling approach, key metrics, and diagnostics used to predict `hazardous`.
     - Main widgets:
         - Model summary card (type, train/test split, features used, date trained).
         - Performance plots: ROC curve, Precision-Recall curve, confusion matrix, calibration plot.
         - Feature importance bar chart (global) and partial dependence / ICE for top 3 features.
         - Toggle to view model behaviour under alternate class-weighting or threshold.
     - Interactions: Slider to adjust classification threshold and view resulting precision/recall; dropdown to switch model versions.
     
     
4) Data & ETL status
     - Purpose: Show ETL logs, data schema, data quality summaries and allow a limited admin view.
     - Main widgets:
         - ETL status panel with last run time, row counts for raw vs processed
         - Schema viewer: column names, types, and example values (linked to `Data/Raw/neo.csv`).
         - Data quality charts: missingness heatmap, distributions for key fields (`est_mean_diameter`, `miss_distance_km`, `relative_velocity_km_s`).
         - Quick actions: Re-run ETL, regenerate features, export processed dataset.
     - Interactions: Click a column in schema viewer to highlight its distribution and missingness; download buttons for processed assets.
     

Layout & design notes
- Sidebar filter panel (persistent): global filters for date range, hazard flag, diameter min/max, miss distance threshold, and observation count. Filters affect all pages.
- Responsiveness: On mobile, stack KPI cards and convert tables to scrollable lists; maps collapse to summary charts.
- Accessibility: All charts include descriptive captions and alt text; colour palettes are colourblind-safe; provide high-contrast mode.



## Unfixed Bugs
* Please mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
* Did you recognise gaps in your knowledge, and how did you address them?
* If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

## Development Roadmap
* What challenges did you face, and what strategies were used to overcome these challenges?
* What new skills or tools do you plan to learn next based on your project experience? 

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.
