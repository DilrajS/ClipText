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

Within this repository, you'll find a Jupyter Notebook illustrating the process of training an OCR model using the EMNIST dataset. The main application relies on Tesseract because of its robust accuracy — a result of extensive research and investment. However, the provided notebook offers a conceptual dive into OCR's workings.

### Concepts Highlighted in the Notebook:

- Data loading and preprocessing
  - Normalization
  - Reshaping
  - Data Augmentation
  - Orientation Correction
  - Label Encoding

## Licensing Notes

Tesseract operates under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0). This grants the freedom to utilize, adapt, and distribute any software incorporating or embedding Tesseract without worrying about royalty implications.

## Acknowledgments

- OCR Engine: [Tesseract](https://github.com/tesseract-ocr/tesseract)
- Training Notebook Dataset: [EMNIST by TensorFlow](https://www.tensorflow.org/datasets/catalog/emnist)

## About the Author

Dilraj Sandhu

[github.com/DilrajS](https://github.com/DilrajS)
