# COMPARATIVE ANALYSIS OF 3D POINT CLOUD LIBRARIES

# 3D Point Cloud Libraries

Comparative analysis of features, performance, and algorithms in the Open3D, PyntCloud, and Trimesh libraries.

##Requirements

Install dependencies:

```bash
uv sync

```

## Datasets

Before running the experiments, is necessary to download the required datasets separately.

The datasets can be found in Standford original site: https://graphics.stanford.edu/data/3Dscanrep/

The Clouds used was: Stanford Bunny, Thai Statue, Lucy 

## Running

run the main scripts:

```bash
uv run main.py

```

the program will automatically execute all datasets defined in:

```bash
dataset_config.py

```

Each dataset must contain:

- `caminho`: path to the `.ply` file
- `tipo`: `small`, `medium` or `large`


