# ClipText

ClipText is an OCR (Optical Character Recognition) utility designed to capture text from screenshots instantly. Built with Tesseract, ClipText offers accuracy and efficiency in text extraction. A supplementary Jupyter Notebook also showcases the training of a basic OCR model to underline the understanding of the technology, even though the primary app leverages Tesseract.

## Features:

- Instantly capture screenshots with the 'Print Screen' key.
- Extract text from the taken screenshot using Tesseract.
- Immediately copy the extracted text to your clipboard.

## Coming Soon Features:

- **Selective Text Capture**: Introducing the ability to crop your screen and extract text exclusively from the area of interest.
- **Refined User Interface**: Experience a cleaner and more intuitive user interaction.
- **Standalone Installer**: Hassle-free installation with our dedicated executable installer for an even smoother user experience.

## Prerequisites

- [Tesseract](https://github.com/tesseract-ocr/tesseract)

## Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/DilrajS/ClipText.git
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Make sure Tesseract is both installed and set in your system's PATH.

## How to Use

Simply execute `cliptext.py` and then press the 'Print Screen' key whenever you want to capture text from your screen.

```bash
python cliptext.py
```

## Supplementary OCR Training Notebook

This repository contains a Jupyter Notebook that details the journey of building and training an OCR (Optical Character Recognition) model from scratch using the EMNIST dataset. While the primary application of this project leverages the Tesseract OCR system due to its well-established accuracy and robustness, the notebook serves as an educational tool. It elucidates the foundational concepts and practical steps involved in crafting an OCR system, providing hands-on experience with the nuances of deep learning-based character recognition.

### Key Features and Concepts Illustrated:

- **Data Exploration and Visualization**: Gaining insights into the EMNIST dataset and understanding its structure.
- **Data Preprocessing**:
  - Image Normalization: Ensuring uniformity in pixel values to aid in model convergence.
  - Image Reshaping: Converting images to the desired shape suitable for deep learning models.
  - Label Encoding: Transforming categorical labels into a format that can be fed into neural networks.
  - Data Augmentation: Introducing variations in the training data to improve generalization.
- **Model Building and Training**:
  - Architecting a Convolutional Neural Network (CNN) suitable for character recognition.
  - Training the model using the processed dataset and monitoring performance metrics.
- **Evaluation**: Assessing the model's performance on unseen data, understanding its strengths, and identifying areas for improvement.

This notebook serves as a testament to the intricate yet fascinating world of OCR, offering both beginners and veterans insights into building an OCR system outside of industrial-strength solutions like Tesseract.


## Licensing Notes

Tesseract operates under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0). This grants the freedom to utilize, adapt, and distribute any software incorporating or embedding Tesseract without worrying about royalty implications.

## Acknowledgments

- OCR Engine: [Tesseract](https://github.com/tesseract-ocr/tesseract)
- Training Notebook Dataset: [EMNIST by TensorFlow](https://www.tensorflow.org/datasets/catalog/emnist)

## About the Author

Dilraj Sandhu

[github.com/DilrajS](https://github.com/DilrajS)
