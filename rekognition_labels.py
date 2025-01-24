# Copyright (c) 2025 Mohammad Shafay Joyo

import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from io import BytesIO
import os
import csv

# Ensuring the output folder exists
if not os.path.exists('output'):
    os.makedirs('output')

def detect_labels(photo, bucket):
    client = boto3.client('rekognition', region_name='us-east-2')

    try:
        # Detecting labels in the image
        response = client.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
            MaxLabels=10
        )

        # Appedning to the log file
        log_file_path = "output/log.txt"
        with open(log_file_path, "a") as log_file:
            log_file.write(f"Detected labels for {photo}:\n")
            for label in response['Labels']:
                log_file.write(f"Label: {label['Name']}, Confidence: {label['Confidence']}\n")

        # Load and display the image from S3 with bounding boxes
        s3 = boto3.resource('s3')
        obj = s3.Object(bucket, photo)
        img_data = obj.get()['Body'].read()
        img = Image.open(BytesIO(img_data))

        # Plotting the image
        fig, ax = plt.subplots()
        ax.imshow(img)

        # Drawing bounding boxes around detected labels
        for label in response['Labels']:
            for instance in label.get('Instances', []):
                bbox = instance.get('BoundingBox')
                if bbox:
                    left = bbox['Left'] * img.width
                    top = bbox['Top'] * img.height
                    width = bbox['Width'] * img.width
                    height = bbox['Height'] * img.height
                    rect = patches.Rectangle((left, top), width, height, linewidth=1, edgecolor='r', facecolor='none')
                    ax.add_patch(rect)
                    label_text = f"{label['Name']} ({round(label['Confidence'], 2)}%)"
                    plt.text(left, top - 2, label_text, color='r', fontsize=8, bbox=dict(facecolor='white', alpha=0.7))

        # Saving the image to the output folder
        output_image_path = f"output/{photo.split('/')[-1]}_labeled.png"
        plt.axis('off')
        plt.savefig(output_image_path)
        plt.close(fig)  
        print(f"Processed image saved to: {output_image_path}")

    except Exception as e:
        print(f"Error processing {photo}: {str(e)}")

def process_images_in_bucket(bucket, folder_prefix):
    s3 = boto3.client('s3', region_name='us-east-2')
    try:
        response = s3.list_objects_v2(Bucket=bucket, Prefix=folder_prefix)

        if 'Contents' not in response:
            print(f"No files found in folder '{folder_prefix}' in bucket '{bucket}'.")
            return

        # Processing each file in the folder
        for obj in response['Contents']:
            photo = obj['Key']
            if photo.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
                print(f"\nProcessing {photo}...")
                detect_labels(photo, bucket)

    except Exception as e:
        print(f"Error listing objects in folder '{folder_prefix}': {str(e)}")

def main():
    bucket = 'joyofirst'  
    folder_prefix = 'images/'  
    process_images_in_bucket(bucket, folder_prefix)

if __name__ == "__main__":
    main()
