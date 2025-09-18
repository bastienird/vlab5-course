Project organization
================
VLab Course Team

## Project organization

All project repositories used in this course are **pre-installed** in
your environment.

### 📁 Where to find them

Projects are located in:

``` bash
cd ~/GitHubRepos
```

To view the full list of repositories (including `dev` and `stable`
subfolders), you can run the following in the Terminal:

``` bash
find ~/GitHubRepos -maxdepth 2 -exec ls -ld {} \;
```

This will show the folder structure and help you identify which projects
are available.

### 🗂 ️Types of repositories

- Some repositories include **only a `dev` version** → they are
  currently under development.
- Others include both:
  - `stable/`: the latest **release** from the `main` branch.
  - `dev/`: the most recent **push** to the `dev` branch.

### 📦 List of projects

| Repository                           | Versions     | Description                                                                                                                                                                                | Main Script                      | GitHub                                                                  |
|--------------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|-------------------------------------------------------------------------|
| **geoflow-tunaatlas**                | stable + dev | Prepares the **Global Tuna Atlas** datasets (Levels 0, 1, 2; effort and CPUE) and deploys them to Zenodo. Also contains Dockerfiles for downloading source datasets and running workflows. | `launching_jsons_creating_GTA.R` | [GitHub](https://github.com/firms-gta/geoflow-tunaatlas)                |
| **tunaatlas_pie_map_shiny**          | stable + dev | A Shiny app for **visualizing any dataset in CWP format** with various plots and maps.                                                                                                     | global.R                         | [GitHub](https://github.com/firms-gta/tunaatlas_pie_map_shiny)          |
| **shiny_compare_tunaatlas_datasets** | dev only     | A Shiny app to **compare GTA datasets** from zenodo DOIs.                                                                                                                                  | global.R                         | [GitHub](https://github.com/firms-gta/shiny_compare_fisheries_datasets) |
| **darwin_core_viewer**               | dev only     | A basic Shiny app **to visualize biodiversity data using the** **Darwin Core** data format. Provides maps and plots. Designed as a starting point for custom apps.                         | `app.R`                          | [GitHub](https://github.com/firms-gta/darwin_core_viewer)               |

> 📌 Documentation for each project is available in the **README.md**
> files within the folders, and on the respective GitHub repositories.

------------------------------------------------------------------------

You can open and explore any of these projects directly in RStudio by
navigating to the appropriate folder using the **Files tab**, or via
`setwd("~/GitHubRepos/<project>/<version>/<project>")` in your console.

Ready to run your first workflow? Jump to the next section [Running
Rscripts in a loaded project](running-scripts-in-loaded-repo.qmd) about
the running of some scripts in the Vlab infrastructure of BlueCloud
2026.
