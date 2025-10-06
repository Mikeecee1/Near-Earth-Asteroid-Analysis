# GitHub Issues Template

This file contains ready-to-use GitHub issue templates based on the project plan. Copy and paste these into GitHub Issues to create individual issues for tracking.

---

## Phase 1: ETL Issues

### Issue Template: Data Source Identification and Access

**Title:** [ETL] Data Source Identification and Access

**Labels:** `etl`, `phase-1`, `high-priority`

**Description:**
Identify and gain access to Near-Earth Asteroid datasets from reliable sources (e.g., NASA's JPL, Minor Planet Center, or Kaggle datasets).

**Tasks:**
- [ ] Research available NEA datasets
- [ ] Identify primary data source(s)
- [ ] Set up API access or download permissions
- [ ] Document data source(s) in README
- [ ] Create data dictionary with field descriptions

**Acceptance Criteria:**
- Data source(s) identified and accessible
- Data dictionary documented
- Initial raw data downloaded

**Estimated Time:** 1-2 days

---

### Issue Template: Raw Data Extraction

**Title:** [ETL] Raw Data Extraction

**Labels:** `etl`, `phase-1`, `high-priority`

**Description:**
Create a notebook to extract raw data from identified sources and store it in the project repository.

**Tasks:**
- [ ] Create `01_DataCollection.ipynb` notebook
- [ ] Implement data extraction logic (API calls or file downloads)
- [ ] Create `inputs/datasets/raw/` directory structure
- [ ] Save raw data in appropriate format (CSV, JSON, etc.)
- [ ] Add data extraction timestamp and metadata
- [ ] Document extraction process in notebook

**Acceptance Criteria:**
- Raw data successfully extracted
- Data stored in `inputs/datasets/raw/` directory
- Extraction process fully documented
- Notebook runs without errors

**Estimated Time:** 2-3 days

---

### Issue Template: Data Quality Assessment

**Title:** [ETL] Data Quality Assessment

**Labels:** `etl`, `phase-1`, `high-priority`

**Description:**
Assess the quality of raw data, identify missing values, duplicates, and anomalies.

**Tasks:**
- [ ] Create `02_DataQualityAssessment.ipynb` notebook
- [ ] Generate data profiling report using ydata-profiling
- [ ] Identify missing values per column
- [ ] Check for duplicate records
- [ ] Identify outliers and anomalies
- [ ] Document data quality issues
- [ ] Create summary statistics

**Acceptance Criteria:**
- Data quality report generated
- All issues documented
- Summary statistics calculated
- Recommendations for data cleaning documented

**Estimated Time:** 2-3 days

---

### Issue Template: Data Cleaning and Transformation

**Title:** [ETL] Data Cleaning and Transformation

**Labels:** `etl`, `phase-1`, `high-priority`

**Description:**
Clean and transform raw data based on quality assessment findings.

**Tasks:**
- [ ] Create `03_DataCleaning.ipynb` notebook
- [ ] Handle missing values (imputation or removal)
- [ ] Remove or handle duplicates
- [ ] Handle outliers appropriately
- [ ] Standardize data formats
- [ ] Create derived features if needed
- [ ] Validate cleaned data
- [ ] Save cleaned data to `inputs/datasets/cleaned/`

**Acceptance Criteria:**
- Data cleaning logic implemented
- Cleaned data validated
- Transformation steps documented
- Cleaned data saved in appropriate format

**Estimated Time:** 3-4 days

---

### Issue Template: Feature Engineering

**Title:** [ETL] Feature Engineering

**Labels:** `etl`, `phase-1`, `medium-priority`

**Description:**
Engineer relevant features for analysis and modelling based on domain knowledge of asteroids.

**Tasks:**
- [ ] Create `04_FeatureEngineering.ipynb` notebook
- [ ] Identify relevant features for asteroid analysis
- [ ] Create new features (e.g., orbital characteristics, proximity metrics)
- [ ] Transform categorical variables
- [ ] Scale/normalize numerical features
- [ ] Document feature engineering decisions
- [ ] Save processed data to `inputs/datasets/processed/`

**Acceptance Criteria:**
- New features created and validated
- Feature transformations documented
- Processed dataset ready for analysis and modelling
- Feature list and descriptions documented

**Estimated Time:** 3-4 days

---

## Phase 2: Visualization & Statistical Analysis Issues

### Issue Template: EDA - Univariate Analysis

**Title:** [Visualization] Exploratory Data Analysis - Univariate Analysis

**Labels:** `visualization`, `phase-2`, `high-priority`, `eda`

**Description:**
Perform univariate analysis to understand individual feature distributions.

**Tasks:**
- [ ] Create `05_EDA_Univariate.ipynb` notebook
- [ ] Create distribution plots for numerical features
- [ ] Create frequency plots for categorical features
- [ ] Generate summary statistics
- [ ] Identify key insights from individual features
- [ ] Save visualizations to `outputs/eda/univariate/`

**Acceptance Criteria:**
- All features analyzed individually
- Visualizations generated and saved
- Key insights documented
- Notebook fully documented

**Estimated Time:** 2-3 days

---

### Issue Template: EDA - Bivariate/Multivariate Analysis

**Title:** [Visualization] Exploratory Data Analysis - Bivariate/Multivariate Analysis

**Labels:** `visualization`, `phase-2`, `high-priority`, `eda`

**Description:**
Analyze relationships between features and identify patterns.

**Tasks:**
- [ ] Create `06_EDA_Multivariate.ipynb` notebook
- [ ] Create correlation matrix and heatmap
- [ ] Generate scatter plots for key feature pairs
- [ ] Create pair plots for feature relationships
- [ ] Analyze categorical vs numerical relationships
- [ ] Identify feature interactions
- [ ] Save visualizations to `outputs/eda/multivariate/`

**Acceptance Criteria:**
- Feature relationships analyzed
- Correlation analysis completed
- Key patterns identified
- Visualizations saved

**Estimated Time:** 3-4 days

---

### Issue Template: Statistical Hypothesis Testing

**Title:** [Statistical Analysis] Hypothesis Testing

**Labels:** `statistical-analysis`, `phase-2`, `medium-priority`

**Description:**
Conduct statistical tests to validate hypotheses about asteroid characteristics.

**Tasks:**
- [ ] Create `07_StatisticalTests.ipynb` notebook
- [ ] Define hypotheses about asteroid data
- [ ] Perform appropriate statistical tests (t-tests, chi-square, ANOVA, etc.)
- [ ] Calculate p-values and confidence intervals
- [ ] Interpret test results
- [ ] Document statistical findings
- [ ] Create visualizations for test results

**Acceptance Criteria:**
- Hypotheses clearly defined
- Statistical tests performed correctly
- Results interpreted and documented
- Visualizations created

**Estimated Time:** 2-3 days

---

### Issue Template: Advanced Visualizations

**Title:** [Visualization] Advanced Interactive Visualizations

**Labels:** `visualization`, `phase-2`, `medium-priority`

**Description:**
Create advanced interactive visualizations using Plotly for deeper insights.

**Tasks:**
- [ ] Create `08_AdvancedVisualizations.ipynb` notebook
- [ ] Create 3D scatter plots for orbital characteristics
- [ ] Build interactive time-series visualizations
- [ ] Create geographical/spatial visualizations if applicable
- [ ] Build interactive dashboards using Plotly
- [ ] Save interactive plots to `outputs/visualizations/`

**Acceptance Criteria:**
- Advanced visualizations created
- Interactive elements functional
- Visualizations saved in appropriate formats
- Notebook documented

**Estimated Time:** 3-4 days

---

### Issue Template: Key Insights Documentation

**Title:** [Documentation] Analysis Findings and Key Insights

**Labels:** `documentation`, `phase-2`, `medium-priority`

**Description:**
Document all key findings from EDA and statistical analysis.

**Tasks:**
- [ ] Create `ANALYSIS_FINDINGS.md` document
- [ ] Summarize key patterns discovered
- [ ] Document statistical test results
- [ ] Highlight important correlations
- [ ] Identify features important for modelling
- [ ] Create executive summary

**Acceptance Criteria:**
- Comprehensive findings document created
- All key insights documented
- Document includes visualizations
- Recommendations for next phase included

**Estimated Time:** 1-2 days

---

## Phase 3: Machine Learning Modelling Issues

### Issue Template: Define ML Problem and Target Variable

**Title:** [ML] Define ML Problem and Target Variable

**Labels:** `machine-learning`, `phase-3`, `high-priority`

**Description:**
Define the machine learning problem(s) to solve (classification, regression, clustering).

**Tasks:**
- [ ] Define the ML problem type(s)
- [ ] Identify target variable(s)
- [ ] Define success metrics (accuracy, RMSE, F1-score, etc.)
- [ ] Document business objectives
- [ ] Create baseline model expectations
- [ ] Document in `ML_OBJECTIVES.md`

**Acceptance Criteria:**
- ML problem clearly defined
- Target variable(s) identified
- Success metrics documented
- Baseline performance established

**Estimated Time:** 1-2 days

---

### Issue Template: Data Preparation for Modelling

**Title:** [ML] Data Preparation for Modelling

**Labels:** `machine-learning`, `phase-3`, `high-priority`

**Description:**
Prepare data specifically for machine learning modelling.

**Tasks:**
- [ ] Create `09_ModelDataPreparation.ipynb` notebook
- [ ] Split data into train/validation/test sets
- [ ] Handle class imbalance if applicable
- [ ] Encode categorical variables
- [ ] Scale features appropriately
- [ ] Create feature matrix and target vector
- [ ] Save prepared datasets

**Acceptance Criteria:**
- Data split appropriately
- All features properly prepared
- Datasets saved for modelling
- Data leakage prevented

**Estimated Time:** 2-3 days

---

### Issue Template: Baseline Model Development

**Title:** [ML] Baseline Model Development

**Labels:** `machine-learning`, `phase-3`, `high-priority`

**Description:**
Develop baseline models to establish performance benchmarks.

**Tasks:**
- [ ] Create `10_BaselineModels.ipynb` notebook
- [ ] Implement simple baseline models (dummy classifier, linear models)
- [ ] Train models on training data
- [ ] Evaluate on validation set
- [ ] Record baseline metrics
- [ ] Document model assumptions

**Acceptance Criteria:**
- Baseline models implemented
- Performance metrics recorded
- Results documented
- Benchmark established

**Estimated Time:** 2-3 days

---

### Issue Template: Advanced Model Development and Selection

**Title:** [ML] Advanced Model Development and Selection

**Labels:** `machine-learning`, `phase-3`, `high-priority`

**Description:**
Develop and compare multiple advanced ML models.

**Tasks:**
- [ ] Create `11_AdvancedModels.ipynb` notebook
- [ ] Implement multiple algorithms (Random Forest, XGBoost, etc.)
- [ ] Perform cross-validation
- [ ] Compare model performance
- [ ] Use Yellowbrick for model evaluation visualizations
- [ ] Select best performing model(s)
- [ ] Document model comparison

**Acceptance Criteria:**
- Multiple models trained and evaluated
- Cross-validation performed
- Best model(s) identified
- Comparison documented with visualizations

**Estimated Time:** 4-5 days

---

### Issue Template: Hyperparameter Tuning

**Title:** [ML] Hyperparameter Tuning

**Labels:** `machine-learning`, `phase-3`, `medium-priority`

**Description:**
Optimize selected model(s) through hyperparameter tuning.

**Tasks:**
- [ ] Create `12_HyperparameterTuning.ipynb` notebook
- [ ] Define hyperparameter search space
- [ ] Implement GridSearch or RandomSearch
- [ ] Perform cross-validated tuning
- [ ] Evaluate tuned models
- [ ] Document optimal parameters
- [ ] Save tuned models

**Acceptance Criteria:**
- Hyperparameter tuning completed
- Optimal parameters identified
- Model performance improved
- Tuned models saved

**Estimated Time:** 3-4 days

---

### Issue Template: Feature Importance Analysis

**Title:** [ML] Feature Importance Analysis

**Labels:** `machine-learning`, `phase-3`, `medium-priority`

**Description:**
Analyze feature importance and perform feature selection.

**Tasks:**
- [ ] Create `13_FeatureImportance.ipynb` notebook
- [ ] Extract feature importance from models
- [ ] Create feature importance visualizations
- [ ] Perform permutation importance analysis
- [ ] Identify redundant features
- [ ] Document key features
- [ ] Optionally retrain with selected features

**Acceptance Criteria:**
- Feature importance analyzed
- Visualizations created
- Key features identified
- Results documented

**Estimated Time:** 2-3 days

---

### Issue Template: Model Evaluation and Testing

**Title:** [ML] Model Evaluation and Testing

**Labels:** `machine-learning`, `phase-3`, `high-priority`

**Description:**
Thoroughly evaluate final model(s) on test set.

**Tasks:**
- [ ] Create `14_ModelEvaluation.ipynb` notebook
- [ ] Evaluate model on test set
- [ ] Generate confusion matrix (if classification)
- [ ] Calculate all relevant metrics
- [ ] Create ROC curves and precision-recall curves
- [ ] Analyze model errors
- [ ] Document final performance

**Acceptance Criteria:**
- Model evaluated on unseen test data
- All metrics calculated
- Performance visualizations created
- Results meet success criteria

**Estimated Time:** 2-3 days

---

### Issue Template: Model Persistence and Versioning

**Title:** [ML] Model Persistence and Versioning

**Labels:** `machine-learning`, `phase-3`, `medium-priority`

**Description:**
Save and version final model(s) for deployment.

**Tasks:**
- [ ] Create model saving pipeline
- [ ] Save final model(s) to `outputs/models/`
- [ ] Save model metadata and performance metrics
- [ ] Create model card with documentation
- [ ] Version models appropriately
- [ ] Test model loading and inference

**Acceptance Criteria:**
- Models saved successfully
- Metadata documented
- Model can be loaded and used for predictions
- Version control implemented

**Estimated Time:** 1-2 days

---

## Phase 4: Power BI Dashboard Issues

### Issue Template: Dashboard Requirements and Wireframe Design

**Title:** [Dashboard] Requirements and Wireframe Design

**Labels:** `dashboard`, `powerbi`, `phase-4`, `high-priority`, `design`

**Description:**
Define dashboard requirements and create wireframe designs.

**Tasks:**
- [ ] Identify key stakeholders and their needs
- [ ] Define dashboard objectives
- [ ] List required visualizations and metrics
- [ ] Create low-fidelity wireframe sketches
- [ ] Create high-fidelity wireframe designs
- [ ] Get feedback on wireframes
- [ ] Document in `DASHBOARD_DESIGN.md`

**Acceptance Criteria:**
- Dashboard requirements documented
- Wireframes created (low and high fidelity)
- Key metrics and KPIs identified
- Design approved by stakeholders

**Estimated Time:** 2-3 days

---

### Issue Template: Data Preparation for Power BI

**Title:** [Dashboard] Data Preparation for Power BI

**Labels:** `dashboard`, `powerbi`, `phase-4`, `high-priority`

**Description:**
Prepare and export data in format suitable for Power BI.

**Tasks:**
- [ ] Create `15_PowerBIDataPrep.ipynb` notebook
- [ ] Prepare data aggregations for dashboard
- [ ] Create calculated fields and metrics
- [ ] Export data in Power BI compatible format (CSV, Excel)
- [ ] Create data refresh strategy documentation
- [ ] Save export files to `outputs/powerbi_data/`

**Acceptance Criteria:**
- Data prepared and aggregated
- Export files created
- Data structure optimized for Power BI
- Documentation complete

**Estimated Time:** 2-3 days

---

### Issue Template: Power BI Data Model Setup

**Title:** [Dashboard] Power BI Data Model Setup

**Labels:** `dashboard`, `powerbi`, `phase-4`, `high-priority`

**Description:**
Set up data model and relationships in Power BI.

**Tasks:**
- [ ] Import data into Power BI Desktop
- [ ] Create data model with appropriate relationships
- [ ] Define measures and calculated columns
- [ ] Set up hierarchies
- [ ] Optimize data types
- [ ] Test data model
- [ ] Document data model structure

**Acceptance Criteria:**
- Data successfully imported
- Relationships established
- Measures created and tested
- Data model documented

**Estimated Time:** 2-3 days

---

### Issue Template: Dashboard Visualizations Development

**Title:** [Dashboard] Visualizations Development

**Labels:** `dashboard`, `powerbi`, `phase-4`, `high-priority`

**Description:**
Develop all dashboard visualizations based on wireframe designs.

**Tasks:**
- [ ] Create overview/summary page
- [ ] Build asteroid characteristics visualizations
- [ ] Create orbital dynamics visualizations
- [ ] Develop risk assessment visuals (if applicable)
- [ ] Add interactive filters and slicers
- [ ] Implement drill-through functionality
- [ ] Create tooltips and info buttons

**Acceptance Criteria:**
- All visualizations created per wireframes
- Interactive elements functional
- Dashboard follows design guidelines
- Performance optimized

**Estimated Time:** 4-5 days

---

### Issue Template: Dashboard Interactivity and User Experience

**Title:** [Dashboard] Interactivity and User Experience

**Labels:** `dashboard`, `powerbi`, `phase-4`, `medium-priority`

**Description:**
Enhance dashboard with interactivity and improve user experience.

**Tasks:**
- [ ] Add cross-filtering between visuals
- [ ] Implement bookmarks for different views
- [ ] Create navigation between pages
- [ ] Add reset filters button
- [ ] Optimize visual layouts for different screen sizes
- [ ] Add branding and styling
- [ ] Test user flows

**Acceptance Criteria:**
- Interactive features functional
- Navigation intuitive
- User experience smooth
- Dashboard responsive

**Estimated Time:** 2-3 days

---

### Issue Template: Dashboard Testing and Quality Assurance

**Title:** [Dashboard] Testing and Quality Assurance

**Labels:** `dashboard`, `powerbi`, `phase-4`, `high-priority`, `testing`

**Description:**
Test dashboard thoroughly and ensure data accuracy.

**Tasks:**
- [ ] Verify all calculations and metrics
- [ ] Cross-check data with source
- [ ] Test all interactive features
- [ ] Test on different devices/browsers (if published)
- [ ] Identify and fix bugs
- [ ] Get user feedback
- [ ] Document known issues

**Acceptance Criteria:**
- All calculations verified
- No critical bugs
- Dashboard tested on target platforms
- Test results documented

**Estimated Time:** 2-3 days

---

### Issue Template: Dashboard Documentation and Deployment

**Title:** [Dashboard] Documentation and Deployment

**Labels:** `dashboard`, `powerbi`, `phase-4`, `medium-priority`, `deployment`

**Description:**
Create user documentation and deploy dashboard.

**Tasks:**
- [ ] Create user guide for dashboard
- [ ] Document all metrics and calculations
- [ ] Create FAQ section
- [ ] Set up data refresh schedule (if applicable)
- [ ] Publish to Power BI Service (if applicable)
- [ ] Configure access permissions
- [ ] Save `.pbix` file to `outputs/powerbi/`

**Acceptance Criteria:**
- User documentation complete
- Dashboard deployed
- Access configured
- Refresh schedule set up

**Estimated Time:** 2-3 days

---

## Cross-Cutting Issues

### Issue Template: Project Documentation

**Title:** [Documentation] Project Documentation

**Labels:** `documentation`, `ongoing`, `medium-priority`

**Description:**
Maintain comprehensive project documentation throughout all phases.

**Tasks:**
- [ ] Update README with project description
- [ ] Document all assumptions and decisions
- [ ] Create data dictionary
- [ ] Document code conventions
- [ ] Add inline code comments
- [ ] Create architecture diagrams
- [ ] Document lessons learned

**Acceptance Criteria:**
- README comprehensive and up-to-date
- All notebooks well-documented
- Supporting documentation complete

**Estimated Time:** Ongoing

---

### Issue Template: Code Quality and Standards

**Title:** [Quality] Code Quality and Standards

**Labels:** `code-quality`, `ongoing`, `medium-priority`

**Description:**
Ensure code quality and adherence to standards throughout the project.

**Tasks:**
- [ ] Follow PEP 8 style guidelines
- [ ] Implement error handling
- [ ] Write reusable functions
- [ ] Organize code into modules if needed
- [ ] Remove unused code and notebooks
- [ ] Optimize performance
- [ ] Add docstrings to functions

**Acceptance Criteria:**
- Code follows style guidelines
- Error handling implemented
- Code organized and clean
- Performance acceptable

**Estimated Time:** Ongoing

---

### Issue Template: Version Control and Collaboration

**Title:** [Version Control] Best Practices

**Labels:** `version-control`, `ongoing`, `medium-priority`

**Description:**
Maintain proper version control practices throughout the project.

**Tasks:**
- [ ] Use meaningful commit messages
- [ ] Create feature branches for major changes
- [ ] Regular commits with logical changesets
- [ ] Update .gitignore as needed
- [ ] Tag major milestones
- [ ] Resolve merge conflicts promptly

**Acceptance Criteria:**
- Clean commit history
- Proper branching strategy followed
- No sensitive data in repository

**Estimated Time:** Ongoing

---

### Issue Template: Environment and Dependency Management

**Title:** [Setup] Environment and Dependency Management

**Labels:** `setup`, `high-priority`

**Description:**
Ensure reproducible environment setup and dependency management.

**Tasks:**
- [ ] Verify all required packages in requirements.txt
- [ ] Pin package versions appropriately
- [ ] Test installation on clean environment
- [ ] Document environment setup in README
- [ ] Create .env.example for any environment variables
- [ ] Update requirements before deployment

**Acceptance Criteria:**
- Requirements.txt up-to-date
- Environment reproducible
- Setup documented
- Dependencies optimized for deployment

**Estimated Time:** 1-2 days

---

## How to Use These Templates

1. Copy the issue template you want to create
2. Go to your GitHub repository
3. Click on "Issues" tab
4. Click "New Issue"
5. Paste the template content
6. Add the appropriate labels
7. Assign to team members if applicable
8. Create the issue

## Recommended Labels to Create

Create these labels in your GitHub repository for better organization:

- `etl` - For ETL phase issues
- `phase-1` - Phase 1 issues
- `phase-2` - Phase 2 issues
- `phase-3` - Phase 3 issues
- `phase-4` - Phase 4 issues
- `visualization` - Visualization related
- `eda` - Exploratory Data Analysis
- `statistical-analysis` - Statistical analysis tasks
- `machine-learning` - ML related issues
- `dashboard` - Dashboard related
- `powerbi` - Power BI specific
- `documentation` - Documentation tasks
- `high-priority` - High priority
- `medium-priority` - Medium priority
- `low-priority` - Low priority
- `design` - Design related
- `testing` - Testing related
- `deployment` - Deployment related
- `code-quality` - Code quality issues
- `setup` - Setup and configuration
- `version-control` - Version control related
- `ongoing` - Ongoing tasks
