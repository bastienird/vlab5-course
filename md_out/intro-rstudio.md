Introduction to VLab5 and RStudio Server
================
VLab Fisheries Atlas Course Team: Grasset Bastien, Barde Julien

## Getting Started with RStudio in VLab5

This short notebook will guide you through the key features and
technical setup of the RStudio Server in VLab5.

### Launching the Environment

To begin working in VLab5 with R workflows, start by navigating to the
**Analytics** section on the platform.

You have two main options to launch an RStudio session:

1.  **RStudio on D4Science (Start)** – This is the default environment.
    It includes all preloaded repositories you’ll use in this course
    (both stable and dev versions). It has limited RAM compared to the
    second option.
2.  **RStudio on GoogleCloud (Start)** – This environment offers more
    RAM and computing power, which can be useful for heavier
    computations. However, it does *not* include the preloaded
    repositories by default. If you use it, you’ll need to manually
    configure and copy the necessary projects.

Once you launch either version, you’ll enter a standard **RStudio Server
interface** directly in your browser.

RStudio is organized into four panes:

- **Top-left**: Script editor
- **Bottom-left**: Console and Terminal
  - The **Console** is where you type and run R code interactively.
  - The **Terminal** provides access to a Unix shell, useful for running
    system commands (e.g., Git, file management).
  - The **Background Jobs** tab (when visible) lets you launch
    long-running scripts without blocking the console. You can track
    progress and logs independently.

> 🧩 These tabs are modular: you can show or hide panes using the **menu
> bar** → `View > Panes` or via the small gear icons in the top-right of
> each panel.

- **Top-right**: Environment, History, Git, Connections, Build, Tutorial
  - The **Environment** tab lists all current objects (datasets, models,
    functions).
  - **History** tracks all commands you’ve run.
  - **Git** appears if the project is under version control.
  - **Build** is used for R packages or Quarto/Bookdown projects.
  - **Tutorial** can show RStudio tutorials if available.
- **Bottom-right**: Files, Plots, Packages, Help, and Viewer
  - This pane lets you navigate directories, visualize plots,
    install/view packages, access help pages, and render HTML outputs.

To explore the technical setup of your session, run the following lines
of code in the R console:

### Verifying the Technical Environment

#### Check R Version

``` r
R.version.string
```

    [1] "R version 4.2.3 (2023-03-15)"

#### Check RStudio Version

``` r
rstudioapi::versionInfo()
```

This returns information such as: - `version`: RStudio version installed
(e.g., `2023.3.0.386`) - `release_name`: Code name for the release
(e.g., `Cherry Blossom`) - `mode`: Whether you’re on the server version

#### System Information

``` r
Sys.info()
```

                                                              sysname 
                                                              "Linux" 
                                                              release 
                                                 "4.15.0-189-generic" 
                                                              version 
                       "#200-Ubuntu SMP Wed Jun 22 19:53:37 UTC 2022" 
                                                             nodename 
    "jupyter-bastien-2egrasset65011--rname-2d-52-53tudio-53erver-4fp" 
                                                              machine 
                                                             "x86_64" 
                                                                login 
                                                            "unknown" 
                                                                 user 
                                                             "jovyan" 
                                                       effective_user 
                                                             "jovyan" 

You’ll see OS-level details such as: - `sysname`: Operating system -
`release`: Kernel version - `machine`: Architecture (usually `x86_64`) -
`user`: Your current user session (likely `jovyan`)

#### RAM Availability (in GB)

``` r
# Note: this uses system-level shell command
system("free -g")
```

This command shows approximate memory allocation: - `total`: Total
memory available (e.g., 125 GB) - `used` and `available`: What’s
currently in use or free

> ⚠️ **Note**: The number you see in “available” RAM may be lower (e.g.,
> 32 GB) due to container quotas or dynamic allocation. The full
> infrastructure may have more memory, but your session may be limited
> based on demand and environment.
>
> 📊 To get a user-friendly view of the actual allocated RAM, go to the
> **top-right Environment panel** in RStudio and click **“Memory usage
> report”**. This tool gives you a live snapshot of RAM used by your
> session.

#### List of Installed Packages

``` r
installed.packages()[1:20, c("Package", "Version")]
```

                Package       Version 
    antiword    "antiword"    "1.3.4" 
    base64enc   "base64enc"   "0.1-3" 
    bslib       "bslib"       "0.7.0" 
    cachem      "cachem"      "1.0.8" 
    cli         "cli"         "3.6.2" 
    commonmark  "commonmark"  "2.0.0" 
    digest      "digest"      "0.6.35"
    evaluate    "evaluate"    "0.23"  
    fastmap     "fastmap"     "1.1.1" 
    fontawesome "fontawesome" "0.5.2" 
    fs          "fs"          "1.6.3" 
    glue        "glue"        "1.7.0" 
    highr       "highr"       "0.10"  
    htmltools   "htmltools"   "0.5.8" 
    jquerylib   "jquerylib"   "0.1.4" 
    jsonlite    "jsonlite"    "1.8.8" 
    knitr       "knitr"       "1.45"  
    lifecycle   "lifecycle"   "1.0.4" 
    litedown    "litedown"    "0.7"   
    magrittr    "magrittr"    "2.0.3" 

This shows the first 20 installed packages and their versions. You can
increase the number for a full list.

#### Load a Test Package (optional)

``` r
# Try loading a utility package
require(antiword)
```

    Loading required package: antiword

If successful, this confirms that the package and its dependencies are
correctly installed.

------------------------------------------------------------------------

### Notes

- All environments and package lists may evolve over time.
- The VLab infrastructure will be updated regularly to keep
  compatibility with the course materials.
- You can always re-run this notebook to verify your session.

------------------------------------------------------------------------

**Next step:** Now that you know your environment, proceed to [Project
Organization](project-organization.qmd) and explore the available
repositories!
