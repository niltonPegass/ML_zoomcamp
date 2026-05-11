# Deep Learning with PyTorch - Image Classification

This project builds an image classification model using **PyTorch** and **transfer learning**. It is part of the ML Zoomcamp curriculum (Module 08 - Deep Learning), adapted from the original TensorFlow/Keras version to use PyTorch instead.

---

## Problem Overview

Given a clothing image, the goal is to correctly identify which of **10 clothing categories** it belongs to. This is a **multi-class classification** task where:

- The input is an image of a clothing item
- The output is a predicted category label (e.g., *pants*, *dress*, *t-shirt*)

Instead of training a model from scratch, we leverage a model pre-trained on ImageNet and fine-tune it for this specific task - a technique known as **transfer learning**.

---

## Dataset

The dataset used is the [clothing-dataset-small](https://github.com/alexeygrigorev/clothing-dataset-small), a subset of a larger clothing image collection.

| Property | Details |
|---|---|
| **Categories** | dress, hat, longsleeve, outwear, pants, shirt, shoes, shorts, skirt, t-shirt |
| **Splits** | Train / Validation / Test |
| **Input size** | Images resized to 224 × 224 pixels |
| **Organization** | One directory per class label |

---

## Methodology

### 1. Pre-trained Model - MobileNetV2

Rather than training from scratch, we start from **MobileNetV2**, pre-trained on ImageNet (1.4M images, 1000 classes). The convolutional layers are **frozen** - we reuse their learned feature representations (edges, textures, shapes) and only train the new classification head added on top.

### 2. Model Architecture

The custom model follows this structure:

| Stage | Component |
|---|---|
| Feature extraction | MobileNetV2 backbone (frozen) |
| Pooling | Global Average Pooling |
| Inner layer | Fully connected (Dense) + ReLU |
| Regularization | Dropout |
| Output | Fully connected → 10 classes (logits) |

### 3. Training

PyTorch uses an **explicit training loop** - unlike Keras's `model.fit()`. Each epoch:
1. Forward pass → compute loss (`CrossEntropyLoss`)
2. Backward pass → compute gradients
3. Optimizer step → update weights (`Adam`)
4. Validation phase → evaluate without gradient updates

### 4. Hyperparameter Tuning

The following hyperparameters are tuned through experimentation:

| Hyperparameter | Values tested | Best found |
|---|---|---|
| Learning rate | 0.0001, 0.001, 0.01, 0.1 | **0.001** |
| Inner layer size | 10, 100, 1000 | **varies** |
| Dropout rate | 0.0, 0.2, 0.5, 0.8 | **0.2** |

### 5. Regularization - Dropout

To prevent overfitting, **Dropout** is applied after the inner layer. During training, a fraction of activations is randomly set to zero, forcing the network to learn more robust representations. Dropout is automatically disabled during evaluation/inference.

### 6. Data Augmentation

To artificially expand the training set and improve generalization, random transformations are applied **only to training images**:

- Random rotation (±10°)
- Random resized crop (zoom effect)
- Random horizontal flip

Validation and test images are **never augmented** - only resized and normalized.

### 7. Model Checkpointing

During training, the model is saved whenever validation accuracy improves. This ensures the best-performing version is preserved even if later epochs show degradation.

### 8. Export to ONNX

After training, the model is exported to **ONNX** (Open Neural Network Exchange) format for deployment - enabling use with optimized runtimes and in language-agnostic environments (e.g., the serverless module).

---

## Key Concepts

| Concept | Description |
|---|---|
| Transfer Learning | Reusing a model trained on one task for a different task |
| CNN | Convolutional neural network - specialized for image data |
| Dropout | Regularization technique that prevents overfitting |
| Data Augmentation | Creating variations of training images to improve generalization |
| Checkpointing | Saving the best model state during training |
| ONNX | Portable format for model deployment across platforms |

---

## PyTorch vs TensorFlow/Keras - Quick Reference

| Concept | TensorFlow / Keras | PyTorch |
|---|---|---|
| Data loading | `ImageDataGenerator` | `Dataset` + `DataLoader` |
| Training | `model.fit()` | Manual training loop |
| Layers | `keras.layers.Dense()` | `nn.Linear()` |
| Loss | `CategoricalCrossentropy` | `CrossEntropyLoss` |
| Optimizer | `keras.optimizers.Adam` | `optim.Adam` |
| Saving | `.h5` / `.keras` | `.pth` / `.pt` |
| Device | Automatic | Explicit `.to(device)` |

---

## Environment

- **Platform:** Google Colab (GPU available via `torch.cuda.is_available()`)
- **Main libraries:** PyTorch, torchvision, Pillow (PIL), NumPy

---

## References

- [ML Zoomcamp - Module 08 Deep Learning](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/08-deep-learning)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [torchvision Models](https://pytorch.org/vision/stable/models.html)
- [ONNX Documentation](https://onnx.ai/)
- Original workshop by [Alexey Grigorev](https://github.com/alexeygrigorev), PyTorch adaptation from the ML Zoomcamp Deep Learning module
