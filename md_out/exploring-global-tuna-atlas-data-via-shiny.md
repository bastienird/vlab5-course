Exploring Global Tuna Atlas data via Shiny
================
VLab Course Team

> **Objective:** Learn how to interact with processed GTA datasets
> through dynamic **Shiny** applications, understand the
> **benefits/limits** of each app, and how CWP-formatted datasets fit
> in.  
> **Prerequisite:** Good understanding of GTA datasets (Levels, effort,
> CPUE).  
> **Presentation:** Hands-on demo + self‑exploration + short quiz.  
> **Outcome:** Learners can use a Shiny app to explore GTA datasets
> **with or without writing code**.

------------------------------------------------------------------------

## Quick start in VLab5

Shiny apps can be accessed in **two ways**:

1.  From the **Shiny Apps tab** in VLab → directly launch stable or dev
    versions of available apps.
2.  From the repository in `~/GitHubRepos` → open the `.Rproj`, restore
    packages, and run `shiny::runApp()`.

> All Shiny apps have **stable and dev versions**, except
> **darwin_core_viewer** which is only available as a stable version in
> the Shiny Apps tab.

## Outside Vlab 5

If you’re not (yet) a VLab5 member, you can still run the Shiny app
locally using Docker.

> **Note:** Docker images can be large and the app may require several
> GB of RAM.

> We **strongly recommend** running this Shiny app on **VLab5 RStudio
> Server** because it can require **a lot of RAM** (often **32 GB**,
> depending on dataset size and filters). VLab5 provides:

> - a consistent environment (R/RStudio, system libs),
> - higher memory availability than many laptops,
> - fewer installation issues (GDAL/PROJ, curl, etc. already present).

``` bash

docker pull ghcr.io/<name-of-the-shiny-app-repo-eg.firms-gta/tunaatlas_pie_map_shiny> #(first time only)
docker run --rm --name tunaatlas \
  -p 3838:3838 \
  ghcr.io/<name-of-the-shiny-app-repo-eg.firms-gta/tunaatlas_pie_map_shiny>
```

and then open http://127.0.0.1:3838/

------------------------------------------------------------------------

## Shiny Apps in this lesson

### Main apps (available in Shiny Apps tab)

- **tunaatlas_pie_map_shiny** (stable + dev)  
  *Purpose:* Visualize **any dataset in CWP format** (catch/effort) with
  interactive **maps and plots**.  
  *GitHub:* <https://github.com/firms-gta/tunaatlas_pie_map_shiny>
  *Vlab5:*
  <https://blue-cloud.d4science.org/group/globalfisheriesatlas/global-tuna-atlas>
  *Docs:* See repo **README** for supported schemas, required columns,
  and examples.

- **shiny_compare_tunaatlas_datasets** (stable + dev)  
  *Purpose:* **Compare** harmonized GTA datasets (e.g., different Zenodo
  DOIs / releases / parameters).  
  *GitHub:* <https://github.com/firms-gta/tunaatlas_pie_map_shiny>
  *Vlab5:*
  <https://blue-cloud.d4science.org/group/globalfisheriesatlas/comparison-globaltunaatlas-datasets>
  *Docs:* README describes how to reference DOIs and comparison keys.

### Additional app

- **darwin_core_viewer** (stable only)  
  *Purpose:* Minimal viewer for **Darwin Core** biodiversity data
  (maps + plots). Good **template** for custom viewers.  
  *GitHub:* <https://github.com/firms-gta/darwin_core_viewer> *Vlab5:*
  <https://blue-cloud.d4science.org/group/globalfisheriesatlas/darwin-core-viewer>
  *Docs:* README covers expected Darwin Core fields (e.g.,
  `scientificName`, `eventDate`, `decimalLatitude/Longitude`).

------------------------------------------------------------------------

## Example walkthroughs

### A) Explore a CWP dataset with `tunaatlas_pie_map_shiny`

1.  From the **Shiny Apps tab**, open the stable version
    (recommended).  
    *(Alternatively, run locally with `shiny::runApp()` after restoring
    packages.)*  
2.  A formatted dataset is already loaded. You can as well choose a
    different dataset to explore in the ‘Choose dataset’ panel.
3.  **Filter** → by species, gear, year range, area.  
4.  **Visualize** → interactive map (e.g., 5° grid) + plots; export as
    needed (see README).

**Strengths**: quick exploration, map‑centric, supports broad CWP
datasets.  
**Limits**: depends on schema conformity; heavy datasets may be slow.

### B) Compare several GTA releases with `shiny_compare_tunaatlas_datasets`

1.  From the **Shiny Apps tab**, open dev or stable version.  
2.  Datasets are already loaded from DOIs. If you want to explore other
    datasets, just update the DOI.csv file in the repository.  
3.  **Choose keys** (year/area/gear/species).  
4.  **Inspect differences** → tables/plots of differences, coverage, and
    changes.

**Strengths**: release comparisons, quick differences across versions.  
**Limits**: assumes comparable schemas; interpret differencies carefully
as the differences of processes for each datasets are complex.

------------------------------------------------------------------------

## Strengths vs. limitations of GUI tools

**Strengths**

- Lower barrier to entry — no code needed.  
- Fast exploratory analysis & visual quality assurance.  
- Standardized filters/views reduce errors.

**Limitations**

- Less flexible than writing code for bespoke analytics.  
- Performance can degrade on very large datasets.  
- Schema assumptions must be respected (CWP format).

<!-- --- -->
<!-- ## Optional: Where CWP fits -->
<!-- - **CWP standards** (species, gear, area) are the **backbone** of harmonization.   -->
<!-- - Shiny apps expect datasets that follow these codes; otherwise mapping fails or fields won’t populate.   -->
<!-- - If you need a refresher, see Lesson **3.1** (standards & FAIR) or Module 1. -->

------------------------------------------------------------------------

<!-- ## Bonus: What is ShinyProxy? -->
<!-- A container‑based platform for **hosting Shiny apps** at scale (auth, routing, resource control). The GTA apps can be served through ShinyProxy.   -->
<!-- > Coordinate with your platform admin (e.g., **Julien Barde**) for deployment specifics (images, memory, user mapping).   -->
<!-- > See each repo’s **README** for containerization notes or Dockerfiles. -->
<!-- 📌 There is also a **Shiny App Deployment Guide**, but this will be covered in a **separate bonus lesson**. -->
<!-- --- -->
<!-- ## Mini Task + Quick Quiz -->
<!-- **Task (5–10 min)**   -->
<!-- - Launch `tunaatlas_pie_map_shiny` from the Shiny Apps tab, load a CWP catch dataset, filter for one species (e.g., `SKJ`) and 2015–2020, and export a plot. -->
<!-- **Quiz (2 items)**   -->
<!-- 1) Which constraint is **most** crucial for these apps to work?   -->
<!-- - A) File naming   -->
<!-- - B) CWP schema conformity ✅   -->
<!-- - C) Folder depth   -->
<!-- 2) `shiny_compare_tunaatlas_datasets` is mainly used to…   -->
<!-- - A) Edit raw CSVs   -->
<!-- - B) Compare DOI releases ✅   -->
<!-- - C) Generate CPUE -->
