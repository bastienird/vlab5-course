Overview
================
VLab Course Team

> **Estimated duration:** 30 minutes
>
> **Format:** lab notebook (Explainer video + real-time walkthrough
> incoming)
>
> **Prerequisites:** Access to VLab5, completion of VLab5 platform
> orientation.

------------------------------------------------------------------------

## Course map (Pages)

- **Intro to RStudio in VLab5**  
  `intro-rstudio.qmd` - Launch options (D4Science vs Google Cloud),
  RStudio panes (Console, Terminal, Environment,
  Files/Plots/Packages/Help/Viewer), system checks (R/RStudio versions,
  RAM).

- **Project Organization**  
  `project-organization.qmd` - Pre-installed repositories in
  `~/GitHubRepos`, stable vs dev structure, quick terminal command to
  list repos, README locations.

- **Running scripts in a loaded repository**  
  `running-scripts-in-loaded-repo.qmd` - Open `.Rproj`, run
  `renv::restore()`, render example Rmd (`summary_catch.Rmd` in
  `geoflow-tunaatlas`), pattern for Shiny apps (`shiny::runApp()`).

- **Deploy repos in your own VLab (Bonus)**  
  `deploy-repos-in-vlab-rstudioserver.qmd` - High-level notes for
  advanced users: RStudio Server image, preload script, global `renv`
  cache at image build-time, and optional per-project/per-user cache
  notes.

------------------------------------------------------------------------

## Learning objectives

By the end of this lesson, learners will be able to:

- Navigate the VLab5 RStudio environment confidently.
- Understand the structure of project repositories, including **stable
  vs dev** versions.
- Use `renv::restore()` to initialize a **reproducible** R environment.
- Execute a complete R script within VLab5.
- *(Bonus)* Understand how the **shared package cache** works within the
  infrastructure.
- *(Bonus)* Deploy a repo in their **own VLab** environment if needed.

------------------------------------------------------------------------

## What you will do

- Launch RStudio (D4Science or Google Cloud) and inspect the
  environment.
- Explore pre-installed repos in `~/GitHubRepos` and locate main
  scripts.
- Restore packages with `renv::restore()` and run a full workflow (Rmd
  or Shiny).
- Inspect outputs in `outputs/` and review logs.
- *(Bonus)* Review how deployment works and how to configure a global
  cache.

------------------------------------------------------------------------

## Expected outcome

By the end of this lesson, learners will:

- Identify and choose an appropriate repository.
- Execute a full R workflow in VLab5.
- *(Bonus)* Understand package dependencies and `renv` logic.

------------------------------------------------------------------------
