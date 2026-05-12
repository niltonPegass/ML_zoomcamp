# Deep Learning with PyTorch — Clothing Image Classification

This project applies **deep learning** to image classification using **PyTorch** and **transfer learning**. It is part of the ML Zoomcamp curriculum (Module 08 — Deep Learning), adapted from the original TensorFlow/Keras version to use PyTorch.

---

## Why Deep Learning?

Deep learning is a subfield of machine learning built on neural networks with multiple layers. Unlike previous chapters that dealt with tabular data, here we work directly with **images** — a domain where deep learning particularly excels.

Instead of structured rows and columns, the input is now a grid of pixels. Deep neural networks learn to extract visual patterns (edges, textures, shapes) automatically across their layers, making them the standard approach for image classification tasks.

---

## Use Case

Imagine a fashion marketplace where a user wants to list a clothing item for sale. They upload a photo, and a **classification service** analyzes the image and suggests the appropriate category automatically — for example, identifying the item as a *t-shirt* or a *dress*.

That service is exactly what we build here: a neural network that receives a clothing image and returns a predicted category label.

---

## Problem Framing

This is a **multi-class classification** task:

| Property | Details |
|---|---|
| **Input** | A clothing image |
| **Output** | One of 10 clothing category labels |
| **Task type** | Multi-class classification |

---

## Dataset

We use the [clothing-dataset-small](https://github.com/alexeygrigorev/clothing-dataset-small) — a curated subset of the [full clothing dataset](https://github.com/alexeygrigorev/clothing-dataset) (~5,000 images, 20 classes), keeping only the **10 most popular categories**.

| Property | Details |
|---|---|
| **Categories** | dress, hat, longsleeve, outwear, pants, shirt, shoes, shorts, skirt, t-shirt |
| **Splits** | Train / Validation / Test (pre-organized, no manual split needed) |
| **Input size** | Images resized to 224 × 224 pixels |

---

## Methodology

### Transfer Learning with MobileNetV2

Rather than training from scratch, we use **MobileNetV2** — a model pre-trained on ImageNet (1.4M images, 1000 classes). Its convolutional layers are **frozen**, reusing already-learned visual features, while a custom classification head is trained for our 10-class problem.

**Model architecture:**

| Stage | Component |
|---|---|
| Feature extraction | MobileNetV2 backbone (frozen) |
| Pooling | Global Average Pooling |
| Inner layer | Fully connected + ReLU |
| Regularization | Dropout |
| Output | Fully connected → 10 classes |

### Training

PyTorch requires an **explicit training loop** — forward pass, loss computation (`CrossEntropyLoss`), backward pass, and weight update (`Adam optimizer`) — unlike Keras's `model.fit()`. This gives more control and visibility into what happens during training.

### Key Techniques Applied

| Technique | Purpose |
|---|---|
| **Hyperparameter tuning** | Learning rate, inner layer size, and dropout rate are systematically tested |
| **Dropout regularization** | Randomly disables neurons during training to prevent overfitting |
| **Data augmentation** | Random rotations, crops, and flips applied to training images only, to improve generalization |
| **Model checkpointing** | Best model state is saved automatically whenever validation accuracy improves |
| **ONNX export** | Trained model is exported to a portable format ready for deployment |

---

## PyTorch vs TensorFlow/Keras

| Concept | TensorFlow / Keras | PyTorch |
|---|---|---|
| Data loading | `ImageDataGenerator` | `Dataset` + `DataLoader` |
| Training | `model.fit()` | Manual training loop |
| Dense layer | `keras.layers.Dense()` | `nn.Linear()` |
| Loss | `CategoricalCrossentropy` | `CrossEntropyLoss` |
| Optimizer | `keras.optimizers.Adam` | `optim.Adam` |
| Model saving | `.h5` / `.keras` | `.pth` / `.pt` |
| Device management | Automatic | Explicit `.to(device)` |

---

## Environment

- **Platform:** Google Colab (GPU-enabled)
- **Main libraries:** PyTorch, torchvision, Pillow, NumPy

---

## References

- [ML Zoomcamp — Module 08 Deep Learning](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/08-deep-learning)
- [Clothing Dataset (full)](https://github.com/alexeygrigorev/clothing-dataset)
- [Clothing Dataset Small](https://github.com/alexeygrigorev/clothing-dataset-small)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [ONNX Documentation](https://onnx.ai/)
- Original curriculum by [Alexey Grigorev](https://github.com/alexeygrigorev) — PyTorch adaptation based on ML Zoomcamp Module 08
