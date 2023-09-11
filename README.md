# Automatic Number Plate Recognition (ANPR) System

The Automatic Number Plate Recognition (ANPR) system is a Python-based application that employs OpenCV for locating and recognizing license plates in images.

## Note:
This repository is currently in an incomplete state.While it provides a basic implementation of the ANPR system, there are several planned enhancements and features that are yet to be implemented.
I'll be adding further files soon.

## Overview

The ANPR system is divided into two main components:

- **Plate Localization**:
   - This component identifies potential license plates within an input image using image preprocessing techniques and contour analysis.

- **Character Segmentation and Recognition**:
   - This component extracts individual characters from the identified license plates and utilizes OCR (Optical Character Recognition) to recognize the characters.

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV library
- Tesseract OCR engine
- pytesseract library

### Installation

1. Install Python dependencies:

    ```
    pip install opencv-python-headless pytesseract pillow
    ```

2. Install Tesseract OCR:

    - **Ubuntu**:

        ```
        sudo apt-get install tesseract-ocr
        ```

    - **Other Platforms**:
        - Refer to the [official installation guide](https://github.com/tesseract-ocr/tesseract).

## Usage

1. Place the input images in the `input_images` directory.

2. Run the ANPR system:

    ```
    python anpr_system.py
    ```

   - The system will process each image in the `input_images` directory.
   - Detected plates and recognized characters will be displayed.

## Customization

- To adjust preprocessing techniques or algorithms, modify the following functions in `anpr_system.py`:

   - `localize_plate`: Customize the plate localization algorithm.
   - `segment_characters`: Adjust character segmentation techniques.

- For training a custom OCR model, refer to the [Tesseract documentation](https://github.com/tesseract-ocr/tesseract).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project is based on the OpenCV and Tesseract OCR libraries, which are open-source and widely used in the computer vision community.

