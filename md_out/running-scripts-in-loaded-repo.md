Running Rscripts in a loaded project
================
VLab Course Team

Before running any code in a repository, make sure you are **inside the
correct R project** (`.Rproj`). This activates project-specific settings
(including `renv`) and sets the working directory properly.

------------------------------------------------------------------------

## Step 1 — Open the project (`.Rproj`)

Open a project using one of these options:

- **From the Files pane** (bottom-right): navigate to the repository
  folder and click the `.Rproj` file.
- **Programmatically (requires `rstudioapi`)**:

``` r
if (!requireNamespace("rstudioapi", quietly = TRUE)) install.packages("rstudioapi")
rstudioapi::openProject("~/GitHubRepos/geoflow-tunaatlas/stable")
```

> Opening the `.Rproj` ensures that `renv` is activated via the
> project’s `.Rprofile` and that your working directory is correct.

------------------------------------------------------------------------

## Step 2 — Restore the Project environment with `renv`

The [`renv` package](https://rstudio.github.io/renv/) manages
**project-specific R environments** to guarantee **reproducibility**. It
records exact package versions in `renv.lock` and restores them on any
machine.

Run this once per project:

``` r
renv::restore()
```

What this does:

- Installs missing packages **or** links them from VLab’s **shared
  cache** (fast).
- Aligns your session’s packages with the versions expected by the
  project.

Useful tips:

``` r
# Check environment status (optional)
renv::status()

# If prompted after updates, restart your R session
if (requireNamespace("rstudioapi", quietly = TRUE)) rstudioapi::restartSession()
```

> ✅ **Always** run `renv::restore()` when you open a **new**
> repository.  
> ℹ️ A later section of this course dives deeper into `renv`, shared
> caches in VLab, and linking multiple repos to a common cache
> directory.

If you want to use the cache renv with your own projects or within your
Vlab feel free to follow this tutorial [renv cache
path](renv-cache-path.qmd).

------------------------------------------------------------------------

## Example with geoflow-tunaatlas project

### Step 3: Explore the `.Rmd` report

The file `summary_catch.Rmd` is an R Markdown document that allows you
to explore catch datasets and generate visual outputs like maps and
plots. A similar file is also available for effort data.

You can render the entire report at once using:

``` r
rmarkdown::render("summary_catch.Rmd")
```

However, for learning purposes, we recommend exploring the file
chunk-by-chunk to understand each step in the workflow.

Open the file in the RStudio editor and review each code block, which
typically includes: - Data loading from zenodo, or in the VLab from
existing folder (to avoid re-downloading data) - Data transformation and
filtering - Visualization with maps and plots - Output generation

### Outputs

Executing the full `.Rmd` will generate an HTML report and may also
create visual outputs or data files, often saved in the same directory
or an `outputs/` subfolder.

Note: `geoflow-tunaatlas` is the most complex repository used in this
course. It contains several scripts, workflows, and Docker-related files
beyond the `.Rmd` example shown here.

------------------------------------------------------------------------

## Other repositories

For all of the other repositories in this course: -
`tunaatlas_pie_map_shiny` - `shiny_compare_tunaatlas_datasets` -
`darwin_core_viewer` the usage is much simpler. You typically only need
two commands to get started:

``` r
renv::restore()
shiny::runApp()
```

These repositories are Shiny apps that can be launched directly after
restoring the environment.

You’re now ready to explore and execute workflows and Shiny apps across
all repositories in VLab!
