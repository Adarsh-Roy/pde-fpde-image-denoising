# Non-Local Morphological PDEs for Image Processing

This repository contains the complete code implementation and results for our B.Tech Major Project titled **"Non-Local Morphological PDEs for Image Processing"**, carried out by **Adarsh Roy** and **Abhinna Agarwal** under the supervision of **Dr. Mani Mehra**, Department of Mathematics, IIT Delhi.

---

## 🧠 Project Overview

This project explores the use of **non-local morphological Partial Differential Equations (PDEs)** and **p-Laplacian operators** on graph structures for advanced image denoising and smoothing.

We extend traditional local models with **graph-based non-local operators** and also introduce **fractional order anisotropic diffusion models** for improved preservation of image features.

---

## 📖 Full Report

A complete PDF report of the project including theory, methodology, and results is available here:

👉 [`main.pdf`](./main.pdf)

---

## 📁 Folder Structure

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

## ⚙️ Installation

Make sure Python ≥ 3.8 is installed. Then install dependencies:

```bash
pip install numpy scipy matplotlib opencv-python scikit-image tqdm
pip install torch
```

Then check the instructions for installing `torch_pdegraph` locally [here](https://github.com/aGIToz/Pytorch_pdegraph).

---

## 🚀 Running the Code

1. Clone the repository:

   ```bash
   git clone https://github.com/Adarsh-Roy/pde-fpde-image-processing.git
   cd pde-fpde-image-processing
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

## 🔌 Dependencies and Libraries

This project heavily uses:

- **[`torch_pdegraph`](https://github.com/aGIToz/Pytorch_pdegraph)**: For pre-built morphological and diffusion operators on graphs.
- **`numpy`, `matplotlib`, `scikit-image`**: For image manipulation and visualization.

Special thanks to the developers of **`torch_pdegraph`** for enabling easy-to-use GPU-compatible graph PDE modeling.

---

## 📊 Sample Results

**Graph PDE Denoising** with different α and β values:

- α = 1.0, β = 0.0 → ∞-Laplacian
- α = 0.5, β = 0.5 → Normalized p-Laplacian
- α = 0.0, β = 1.0 → Laplacian

**Fractional PDE Results** with α ∈ [1.0, 2.2] showed improved edge preservation and reduced noise for intermediate values.

Visual comparisons and figures are included in the `main.pdf`.

---

## 👨‍💻 Authors

- **Adarsh Roy** - [GitHub](https://github.com/Adarsh-Roy)
- **Abhinna Agarwal** - [GitHub](https://github.com/abhinnAg)

Supervised by: **Dr. Mani Mehra**, IIT Delhi

---

## 📚 References

- Bougleux et al., *Nonlocal Regularization on Weighted Graphs* (2009)
- Elmoataz et al., *Morphological PDEs on Graphs* (2012)
- Lindqvist, *Notes on the p-Laplace Equation* (2006)
- Aronsson, *Infinity Laplacian Theory* (1967)
- torch_pdegraph: <https://github.com/aGIToz/Pytorch_pdegraph>

---
