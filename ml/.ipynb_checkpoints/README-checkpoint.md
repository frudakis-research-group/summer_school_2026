# 🚀 Hands-on Session: Introduction to Python & Machine Learning

Welcome! This hands-on session consists of three exercises covering Python programming and introductory machine learning.

## 🎯 Learning Objectives

By the end of this session, you will:

* 🐍 Become familiar with basic Python programming.
* 🧪 Build a simple machine learning model for predicting gas adsorption in Metal–Organic Frameworks (MOFs).
* 🖼️ Train a basic neural network for image classification.

---

## 📚 Exercises

### Exercise 1 — Python Basics

Write a Python program that:

* Prints a menu with **meals**, **desserts**, and **drinks** together with their prices.
* Asks the user to order one item from each category.
* Asks whether the user is **above 25 years old** (`yes`/`no`).
* Applies a **20% discount** if the user is **below 25 years old** and the total cost is **greater than 50**.
* Prints the final amount to pay.

---

### Exercise 2 — Predicting Gas Adsorption in MOFs

Build a simple machine learning model to predict gas adsorption in Metal–Organic Frameworks (MOFs).

The dataset used in this exercise is from:

> Boyd, P. G., Chidambaram, A., García-Díez, E., *et al.* *Data-driven design of metal–organic frameworks for wet flue gas CO₂ capture.* **Nature** 576, 253–256 (2019). https://doi.org/10.1038/s41586-019-1798-7

The dataset is hosted externally and must be downloaded before running the notebook.

Run the following commands **inside a Jupyter notebook cell**:

```bash
!wget "https://archive.materialscloud.org/records/nsp7v-2dk91/files/screening_data.tar.gz?download=1" -O dataset.tar.gz

!tar -xvf dataset.tar.gz
```

---

### Exercise 3 — Image Classification

Train a basic neural network to classify images. This exercise provides a simple introduction to image classification using neural networks.

---

## ▶️ Getting Started

1. Open the repository in Binder or clone it locally.
2. Install the required Python packages (if running locally).
3. Download the MOFs dataset.
4. Work through the notebooks in order.
