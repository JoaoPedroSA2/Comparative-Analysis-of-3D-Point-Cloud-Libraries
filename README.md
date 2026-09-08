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

Example:

```python
DATASETS = {
    "bunny": {
        "caminho": r"",
        "tipo": "small"
    }

```

## Results

The results are saved automatically as:

```text
resultados/resultados_{biblioteca}_{dataset}_{tipo}.txt

```

Containing the benchmark information for:

- Open3d
- PyntCloud
- Trimesh

## Author

**João Pedro Santana Alves**

Computer Science Student at **INATEL (National Institute of Telecommunications)**

- 💻 GitHub: https://github.com/JoaoPedroSA2
- 💼 LinkedIn: https://www.linkedin.com/in/joao-santana2/
- 📧 Email: joao.santana@gec.inatel.br
---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.





