# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Near-Earth Asteroid Analysis

A comprehensive data analytics project analyzing Near-Earth Asteroids (NEAs) using ETL processes, statistical analysis, machine learning, and interactive dashboards.

## Project Overview

This project provides an in-depth analysis of Near-Earth Asteroids, including:
- **ETL Pipeline** - Data collection, cleaning, and transformation
- **Exploratory Data Analysis** - Statistical analysis and visualizations
- **Machine Learning Models** - Predictive modelling for asteroid characteristics
- **Power BI Dashboard** - Interactive dashboard with comprehensive visualizations

## Project Documentation

- **[PROJECT_PLAN.md](PROJECT_PLAN.md)** - Comprehensive project plan with all phases and tasks
- **[GITHUB_ISSUES_TEMPLATES.md](GITHUB_ISSUES_TEMPLATES.md)** - Ready-to-use GitHub issue templates
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick reference guide for the project

## Getting Started

See the sections below for setup instructions.

## Project Structure

```
Near-Earth-Asteroid-Analysis/
├── inputs/
│   └── datasets/
│       ├── raw/              # Raw data from sources
│       ├── cleaned/          # Cleaned data
│       └── processed/        # Processed data for modelling
├── outputs/
│   ├── eda/
│   │   ├── univariate/       # Univariate analysis plots
│   │   └── multivariate/     # Multivariate analysis plots
│   ├── visualizations/       # Advanced visualizations
│   ├── models/               # Saved ML models
│   ├── powerbi_data/         # Data exports for Power BI
│   └── powerbi/              # Power BI files (.pbix)
├── jupyter_notebooks/        # All analysis notebooks
├── PROJECT_PLAN.md          # Detailed project plan
├── GITHUB_ISSUES_TEMPLATES.md  # Issue templates
├── QUICK_REFERENCE.md       # Quick reference guide
├── README.md                # This file
└── requirements.txt         # Python dependencies
```

## How to use this repo

1. Use this template to create your GitHub project repo. Click the **Use this template** button, then click **Create a new repository**.

1. Copy the URL of your repository to your clipboard.

1. In VS Code, select **File** -> **Open Folder**.

1. Select your `vscode-projects` folder, then click the **Select Folder** button on Windows, or the **Open** button on Mac.

1. From the top menu in VS Code, select **Terminal** > **New Terminal** to open the terminal.

1. In the terminal, type `git clone` followed by the URL of your GitHub repository. Then hit **Enter**. This command will download all the files in your GitHub repository into your vscode-projects folder.

1. In VS Code, select **File** > **Open Folder** again.

1. This time, navigate to and select the folder for the project you just downloaded. Then, click **Select Folder**.

1. A virtual environment is necessary when working with Python projects to ensure each project's dependencies are kept separate from each other. You need to create your virtual environment, also called a venv, and then ensure that it is activated any time you return to your workspace.
Click the gear icon in the lower left-hand corner of the screen to open the Manage menu and select **Command Palette** to open the VS Code command palette.

1. In the command palette, type: *create environment* and select **Python: Create Environment…**

1. Choose **Venv** from the dropdown list.

1. Choose the Python version you installed earlier. Currently, we recommend Python 3.12.8

1. **DO NOT** click the box next to `requirements.txt`, as you need to do more steps before you can install your dependencies. Click **OK**.

1. You will see a `.venv` folder appear in the file explorer pane to show that the virtual environment has been created.

1. **Important**: Note that the `.venv` folder is in the `.gitignore` file so that Git won't track it.

1. Return to the terminal by clicking on the TERMINAL tab, or click on the **Terminal** menu and choose **New Terminal** if no terminal is currently open.

1. In the terminal, use the command below to install your dependencies. This may take several minutes.

 ```console
 pip3 install -r requirements.txt
 ```

1. Open the `jupyter_notebooks` directory, and click on the notebook you want to open.

1. Click the **kernel** button and choose **Python Environments**.

Note that the kernel says `Python 3.12.8` as it inherits from the venv, so it will be Python-3.12.8 if that is what is installed on your PC. To confirm this, you can use the command below in a notebook code cell.

```console
! python --version
```

## Deployment Reminders

* Set the `.python-version` Python version to a [Heroku-22](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version that closest matches what you used in this project.
* The project can be deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the **Deploy** tab, select **GitHub** as the deployment method.
3. Select your repository name and click **Search**. Once it is found, click **Connect**.
4. Select the branch you want to deploy, then click **Deploy Branch**.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button **Open App** at the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the `.slugignore` file.
