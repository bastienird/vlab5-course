Bonus (Advanced): Deploy repositories in your own VLab
================
VLab Course Team

> This optional guide is for **advanced users** who want to understand
> how the VLab5 RStudio environment itself is deployed and how to
> reproduce something similar in their own VLab.

------------------------------------------------------------------------

## 1) Deployment of RStudio Server in a VLab

The deployment process is documented in this D4Science support ticket:  
<https://support.d4science.org/issues/23536#note-15>

The RStudio server setup for VLab5 is managed in the following
repository:  
<https://code-repo.d4science.org/gCubeSystem/rstudio-d4science/src/branch/fisheriesatlas-vlab5>

Key files include:

- **07_vlab5_github_repositories.sh** — defines which GitHub
  repositories (stable/dev) are preloaded into the environment.  
  [View
  script](https://code-repo.d4science.org/gCubeSystem/rstudio-d4science/src/branch/fisheriesatlas-vlab5/07_vlab5_github_repositories.sh)
- **Dockerfile** — defines the RStudio server Docker image and how
  repositories and dependencies are installed.  
  [View
  Dockerfile](https://code-repo.d4science.org/gCubeSystem/rstudio-d4science/src/branch/fisheriesatlas-vlab5/Dockerfile)

> ⚠️ This is more **technical and system-level**. If you are interested
> in customizing or deploying your own RStudio VLab instance, we can
> schedule a dedicated walkthrough.

------------------------------------------------------------------------

## 2) Managing a Global `renv` cache in Docker images

When building custom RStudio Docker images for your own VLab, it is
possible to preconfigure a **shared global cache** for `renv`. This
ensures that all projects within the VLab use the same package cache,
saving time and storage.

This is done by adding a line to `.Renviron.site` **during Docker
build**:

``` dockerfile
RUN echo 'RENV_PATHS_CACHE="~/blue-cloud-dataspace/GlobalFisheriesAtlas/cacheRenv"' \
  >> "${R_HOME}/etc/Renviron.site"
```

Reference: <https://support.d4science.org/issues/29739>

### Key points:

- You can set `RENV_PATHS_CACHE` to **any directory**, depending on your
  VLab setup.  
- Using **`~/blue-cloud-dataspace/`** is recommended: it is accessible
  across all users and all VLab instances (though slightly slower than
  local storage).  
- `.Renviron.site` ensures the cache is **global to the image** — every
  repository opened in RStudio will reuse this shared cache.

Effectively: - Each repository still has its own `renv.lock` file (to
ensure reproducibility).  
- But the **package binaries** are stored once in the shared cache,
instead of reinstalling them for every project.

------------------------------------------------------------------------

## 3) The truly simple path (what to consider)

If you want to deploy **the same setup** as VLab5 in *your own* VLab,
here are the essentials to look at and adapt per VLab:

1.  **D4Science ticket (reference implementation & notes):**
    - See: https://support.d4science.org/issues/23536#note-15  
      *(Contains key decisions & parameters used for the Fisheries Atlas
      VLab RStudio.)*
2.  **RStudio Server image for D4Science (to adapt):**
    - Repo:
      https://code-repo.d4science.org/gCubeSystem/rstudio-d4science/src/branch/fisheriesatlas-vlab5
    - Files to review:
      - `Dockerfile`  
        https://code-repo.d4science.org/gCubeSystem/rstudio-d4science/src/branch/fisheriesatlas-vlab5/Dockerfile
      - `07_vlab5_github_repositories.sh` (preloads the course
        repositories)  
        https://code-repo.d4science.org/gCubeSystem/rstudio-d4science/src/branch/fisheriesatlas-vlab5/07_vlab5_github_repositories.sh

> If this is interesting for your team, we can do a short technical
> walkthrough per VLab, since each environment may require minor
> adjustments (base image, permissions, storage mounts, etc.).

------------------------------------------------------------------------

## 4) Summary

- **Basic users**: You don’t need to worry about this — VLab5 is already
  configured.  
- **Advanced users**: You can adapt the Dockerfile and scripts for your
  own VLab deployment, preload specific repos, and configure a global
  `renv` cache.  
- **Best practice**: Use a cache in `blue-cloud-dataspace` for shared
  accessibility across all VLab instances.

> ✅ If you are interested in deploying or customizing your own RStudio
> environment with these settings, reach out — we can provide a
> step-by-step session on adapting the Dockerfile and repository scripts
> for your use case.
