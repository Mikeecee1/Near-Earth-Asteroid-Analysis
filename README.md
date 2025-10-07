
# Near Earth Asteroid Analysis 🪐 

### Project Overview

This project explores NASA’s Near-Earth Object (NEO) dataset, focusing on asteroids that come within close proximity to Earth.
Using publicly available data from NASA’s JPL Center for Near-Earth Object Studies (CNEOS) and downloaded from [Kaggle](https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects), this analysis investigates the physical and orbital characteristics that influence whether an asteroid is classified as potentially hazardous.


# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content
* The dataset includes key attributes such as estimated diameter, relative velocity, miss distance, and absolute magnitude of over 27000 asteroids with 90000 observations.
Additional features have been added (based upon the original data). For example number of observations per object, was engineered to capture tracking frequency and observation density.



## Business Requirements

The requirements of the project are to:
* Identify potentially dangerous asteroids
* Investigate which physical properties contribute to hazardous status
* Understanding these properties may help to mitigate the threats posed

Hazardous asteroids may:
* Be a direct threat to earth if large enough
* Disrupt communications and other satellites
* Be a threat to other near earth objects e.g. space telescopes



## **Hypothesis and how to validate?**

The hypotheses for this project are as follows:
* **Physical and Predictive Hypotheses** 🚀
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

    * **Higher relative velocities** correlate with greater hazard potential due to increased impact energy.
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
        * **Supportive result**: upportive result: Multivariate model achieves substantially higher AUC (e.g., >0.80 if baseline is ~0.5–0.6) and ablation shows each feature contributes measurable lift.

*  **Observational Hypotheses** 🔭
    * NEOs with more recorded **observations** tend to be closer and larger.
        * **Validation**
            1. Scatter plots: observation_count vs miss_distance and observation_count vs diameter (use log scales).
            2. Compute Spearman correlation (robust to nonlinearity) for observation_count with miss_distance and with diameter.
            3. Regress observation_count (or log count) on miss_distance and diameter to quantify effects.
        * **Supportive result**: Negative Spearman for observation_count vs miss_distance, positive Spearman vs diameter (both significant).

    * **Potentially hazardous asteroids** are observed more frequently due to higher monitoring priority.
        * * **Validation**
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
* Outline the high-level steps taken for the analysis.
* How was the data managed throughout the collection, processing, analysis and interpretation steps?
* Why did you choose the research methodologies you used?

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
