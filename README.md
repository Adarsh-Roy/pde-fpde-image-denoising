# Non-Local Morphological PDEs for Image Processing

This repository contains the complete code implementation and results for our B.Tech Major Project titled **"Non-Local Morphological PDEs for Image Processing"**, carried out by **Adarsh Roy** and **Abhinna Agarwal** under the supervision of **Dr. Mani Mehra**, Department of Mathematics, IIT Delhi.

---

## Project Overview

This project explores the use of **non-local morphological Partial Differential Equations (PDEs)** and **p-Laplacian operators** on graph structures for advanced image denoising and smoothing.

We extend traditional local models with **graph-based non-local operators** and also introduce **fractional order anisotropic diffusion models** for improved preservation of image features.

---

## 📖 Full Report

A complete PDF report of the project including theory, methodology, and results is available here:

[main.pdf](https://github.com/Adarsh-Roy/pde-fpde-image-denoising/blob/main/main.pdf)

---

## Folder Structure

```
.
├── barbara.png                 # Sample grayscale image used in experiments
├── main.pdf                    # Final project report
├── fpde.ipynb                  # Notebook for fractional PDE-based image denoising
├── pde_big_graph.ipynb         # PDE implementation on large graph (non-local)
├── pde_mid_graph.ipynb         # PDE on mid-sized grid graph
├── pde_small_graph.ipynb       # PDE on small 4/8-adjacency grid
├── pLaplacianDiffusion.py      # Graph-based p-Laplacian diffusion using torch_pdegraph
├── psnr.ipynb                  # Notebook to compute PSNR for denoising results
└── README.md
```

---

## Installation

Make sure Python ≥ 3.8 is installed. Then install dependencies:

```bash
pip install numpy scipy matplotlib opencv-python scikit-image tqdm
pip install torch
```

Then check the instructions for installing `torch_pdegraph` locally [here](https://github.com/aGIToz/Pytorch_pdegraph).

---

## Running the Code

1. Clone the repository:

   ```bash
   git clone https://github.com/Adarsh-Roy/pde-fpde-image-denoising.git
   cd pde-fpde-image-denoising
   ```

2. For fractional PDE model:

   ```bash
   jupyter notebook fpde.ipynb
   ```

3. For non-local PDEs on graphs:

   ```bash
   jupyter notebook pde_big_graph.ipynb
   # or try pde_small_graph.ipynb or pde_mid_graph.ipynb
   ```

4. To compute PSNR of results:

   ```bash
   jupyter notebook psnr.ipynb
   ```

5. For direct PyTorch-based graph PDE experiments:

   ```bash
   python pLaplacianDiffusion.py
   ```

---

## Dependencies and Libraries

This project heavily uses:

- **[`torch_pdegraph`](https://github.com/aGIToz/Pytorch_pdegraph)**: For pre-built morphological and diffusion operators on graphs.
- **`numpy`, `matplotlib`, `scikit-image`**: For image manipulation and visualization.

Special thanks to the developers of **`torch_pdegraph`** for enabling easy-to-use GPU-compatible graph PDE modeling.

---

## Sample Results

**Graph PDE Denoising** with different α and β values:

- α = 1.0, β = 0.0 → ∞-Laplacian
- α = 0.5, β = 0.5 → Normalized p-Laplacian
- α = 0.0, β = 1.0 → Laplacian

**Fractional PDE Results** with α ∈ [1.0, 2.2] showed improved edge preservation and reduced noise for intermediate values.

Visual comparisons and figures are included in [main.pdf](https://github.com/Adarsh-Roy/pde-fpde-image-denoising/blob/main/main.pdf).

---

## Authors

- **Adarsh Roy** - [GitHub](https://github.com/Adarsh-Roy)
- **Abhinna Agarwal** - [GitHub](https://github.com/abhinnAg)

Supervised by: **Dr. Mani Mehra**, IIT Delhi

---

## References

### Main papers

- **PDE / graph-based model:** Abderrahim Elmoataz, Xavier Desquesnes, and Olivier Lézoray. [*Non-Local Morphological PDEs and p-Laplacian Equation on Graphs With Applications in Image Processing and Machine Learning*](https://doi.org/10.1109/JSTSP.2012.2216504). IEEE Journal of Selected Topics in Signal Processing, 6(7), 764–779, 2012. Introduces the graph operators that interpolate between the Laplacian and infinity Laplacian, used for the project's graph-based denoising experiments.
- **FPDE / fractional-order model:** Jian Bai and Xiang-Chu Feng. [*Fractional-Order Anisotropic Diffusion for Image Denoising*](https://doi.org/10.1109/TIP.2007.904971). IEEE Transactions on Image Processing, 16(10), 2492–2502, 2007. Provides the fractional-order anisotropic diffusion model and Fourier-domain numerical scheme used for the project's fractional denoising experiments.

### Supporting references

- S. Bougleux, A. Elmoataz, and M. Melkemi. [*Local and Nonlocal Discrete Regularization on Weighted Graphs for Image and Mesh Processing*](https://bougleux.users.greyc.fr/articles/bougleux-ijcv09.pdf). International Journal of Computer Vision, 84, 220–236, 2009.
- V.-T. Ta, A. Elmoataz, and O. Lézoray. [*Partial Difference Equations over Graphs: Morphological Processing of Arbitrary Discrete Data*](https://doi.org/10.1007/978-3-540-88690-7_50). European Conference on Computer Vision (ECCV), LNCS 5304, 668–680, 2008.
- Y.-L. You and M. Kaveh. *Fourth-Order Partial Differential Equations for Noise Removal*. IEEE Transactions on Image Processing, 9(10), 1723–1730, 2000.
- P. Lindqvist. [*Notes on the p-Laplace Equation*](https://www.math.ntnu.no/~lqvist/p-laplace.pdf). University of Jyväskylä, Department of Mathematics and Statistics, Report 102, 2006.
- G. Aronsson. *Extension of Functions Satisfying Lipschitz Conditions*. Arkiv för Matematik, 6(6), 551–561, 1967.

### Software

- [*Pytorch_pdegraph*](https://github.com/aGIToz/Pytorch_pdegraph): PyTorch library used for graph PDE operators.

---
