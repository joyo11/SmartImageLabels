# SmartImageLabels

## Overview
The SmartImageLabels project leverages AWS Rekognition to detect and label objects in images stored in an S3 bucket. This application automatically processes images, identifies objects within them, and displays the results with bounding boxes around the recognized objects. It's designed to provide users with automated image analysis using machine learning, simplifying the task of image labeling and categorization.

## Features
- **Image Labeling**: Automatically detects and labels objects in images using AWS Rekognition.
- **Bounding Boxes**: Draws bounding boxes around the detected objects for visual reference.
- **Confidence Scores**: Displays the confidence score for each detected label to gauge accuracy.
- **Image Display**: Presents the original image with the detected labels and bounding boxes overlaid.
- **Batch Processing**: Processes multiple images stored in an S3 bucket, one after another.

## Technologies Used
- **Python**: Backend script for interacting with AWS Rekognition and S3.
- **AWS Rekognition**: Image analysis service used for object detection and labeling.
- **AWS S3**: Stores the images to be analyzed and processed.
- **Matplotlib**: Used to display images with bounding boxes and labels.
- **PIL (Pillow)**: Image manipulation library used for image processing.

## Prerequisites
Ensure the following are installed:
- **Python 3.6+**
- **AWS CLI**: For configuring AWS credentials.
- **boto3**: AWS SDK for Python.
- **Matplotlib**: For visualizing the results.
- **Pillow**: For image manipulation.


Install the necessary Python packages using `pip`:

```bash
pip install boto3 matplotlib pillow
```

## Setup

### Clone the Repository
Clone the project repository :

```bash
git clone https://github.com/joyo11/SmartImageLabels.git
```


## Code Structure

### Backend (Python)
- **rekognition_labels.py**: Main script for detecting labels in images and displaying the results.
- **S3 Integration**: Uses `boto3` to interact with AWS S3 and Rekognition services.
- **Image Handling**: Uses `PIL` (Pillow) to load images and `Matplotlib` to display the image with labels.

## Contact
For any questions or inquiries, feel free to reach out:
- **Email**: [shafay11august@gmail.com](mailto:shafay11august@gmail.com)

---

### Notes
This project is designed for educational purposes and demonstrates the use of AWS Rekognition and S3 for automatic image label detection. Future enhancements could include:
- Support for processing images from different sources (e.g., local files, URLs).
- Implementing a user interface to allow users to upload images and view results interactively.
- Storing label detection results in a database for future reference and analysis.
- Integrating more advanced image processing techniques (e.g., facial recognition, object detection).




