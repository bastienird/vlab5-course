Bonus Personal renv cache on RStudio Server (BlueCloud 2026
infrastructure)
================
VLab Course Team

> This independent note explains how **any RStudio Server user on the
> infrastructure** can use a **shared/global `renv` cache** without
> modifying Docker images or course repositories.

## Why use a personal `renv` cache setting?

- Avoid reinstalling the same packages for every project.  
- Speed up `renv::restore()` across projects by reusing binaries.  
- Keep full reproducibility (each project still uses its own
  `renv.lock`).

------------------------------------------------------------------------

## Option A — Set a user-level cache in `~/.Renviron`

Create (or edit) a file named `~/.Renviron` and add:

``` r
RENV_PATHS_CACHE=~/blue-cloud-dataspace/GlobalFisheriesAtlas/cacheRenv
```

Then **restart R** (Session → Restart R). From now on, all your projects
will use this cache automatically.

**Notes:**

- The path can be **any directory** you can read/write.  
- Using a location under **`~/blue-cloud-dataspace/`** makes the cache
  accessible across workspaces on the infrastructure (shared but
  possibly a bit slower than other folders from the workspace).
- To avoid issues caused by cache corruption or accidental deletions
  (since the cache folders are shared), you can isolate your project
  libraries from the mutual cache using:

``` r
renv::isolate()
```

This command copies all the required packages directly into the renv
folder of your project. Be cautious when running this locally, as it can
significantly increase disk usage.

------------------------------------------------------------------------

## Option B — Set a project-level cache in `<project>/.Renviron`

If you prefer to scope the cache setting to a **single project**, create
a file named `.Renviron` in the **project root** (next to `.Rproj`)
with:

``` r
RENV_PATHS_CACHE=~/blue-cloud-dataspace/GlobalFisheriesAtlas/cacheRenv
```

Restart R inside the project. Only this project will use that cache.

------------------------------------------------------------------------

## Verify your configuration

Run these checks in the R console:

``` r
# What cache path is currently active?
Sys.getenv("RENV_PATHS_CACHE")

# Where does renv think the cache lives?
renv::paths$cache()

# Project environment status (optional)
renv::status()
```

If you change `~/.Renviron` or `<project>/.Renviron`, **restart R** to
apply.

------------------------------------------------------------------------

## Using the cache with projects

Inside any project (after opening the `.Rproj`):

``` r
renv::restore()   # will reuse packages from the shared cache when versions match
```

Packages required by `renv.lock` will be **linked or installed once**
into the cache and reused next time.

------------------------------------------------------------------------

## Good practices & caveats

- Keep the cache path **stable**; moving it breaks existing links.  
- If the cache becomes very large, you can clean unused entries with
  `renv::cache_clean()` (advanced).  
- The cache is **per R version**; upgrading R may create a new cache
  tree.  
- Shared locations improve reuse across projects and users, but network
  storage can be slower than local disk.

------------------------------------------------------------------------

## Notes on group-specific caches

In this course, we configured our cache in:

``` r
~/blue-cloud-dataspace/GlobalFisheriesAtlas/cacheRenv
```

because it is the one we use in the Vlab 5.

But you are free to define a **different cache path** that matches your
own setup:

- A cache specific to your **group of projects**
- A cache specific to your **VLab instance**

This flexibility lets different groups share a cache internally while
keeping separation from other workspaces.
