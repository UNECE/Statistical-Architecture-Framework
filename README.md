# UNECE SAF Reference Architecture

This project provides a reference architecture for use in a National Statistics Organisation (NSO), expressed using the ArchiMate modeling language. The architecture aims to support statistical production, data management, and digital transformation initiatives in line with UNECE standards.

## Overview

- **Purpose:** Offer a reusable, standards-based architecture blueprint for NSOs.
- **Modeling Language:** [ArchiMate](https://www.opengroup.org/archimate/)
- **Tool:** [Archi](https://www.archimatetool.com/) (open-source ArchiMate modeling tool)

## Repository Structure

- `/models/` — ArchiMate model files (`*.archimate`)
- `/docs/` — Documentation and rendered views
- `/scripts/` — Automation and integration scripts

## Using the Archi Tool with GitHub

1. **Install Archi:**
    - Download from [archimatetool.com](https://www.archimatetool.com/download/).

2. **Clone this repository:**
    ```sh
    git clone https://github.com/your-org/unece-saf.git
    ```

3. **Open the Model in Archi:**
    - Launch Archi.
    - Use `File > Import > ArchiMate Model` to open `.archimate` files from `/models/`.

4. **Version Control Workflow:**
    - Save your model changes in Archi.
    - Commit and push updates using Git:
      ```sh
      git add models/
      git commit -m "Update reference architecture"
      git push
      ```

5. **Collaboration Tips:**
    - Use branches for feature/model changes.
    - Resolve merge conflicts in Archi by importing and merging models.

## References

- [UNECE Statistical Architecture Framework](https://statswiki.unece.org/display/arch)
- [ArchiMate Specification](https://pubs.opengroup.org/architecture/archimate3-doc/)
- [Archi User Guide](https://www.archimatetool.com/user-guide/)

---

For questions or contributions, please open an issue or submit a pull request.