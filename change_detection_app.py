import cv2
import os
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Paths
input_folder = "task_2_output/input"
output_folder = "task_2_output/output"
os.makedirs(output_folder, exist_ok=True)

# Get all "before" images
before_images = [f for f in os.listdir(input_folder) if f.endswith(".jpg") and "~2" not in f]

for before_file in before_images:
    base_name = before_file.replace(".jpg", "")
    after_file = base_name + "~2.jpg"
    output_file = base_name + "~3.jpg"

    before_path = os.path.join(input_folder, before_file)
    after_path = os.path.join(input_folder, after_file)
    output_path = os.path.join(output_folder, output_file)

    if not os.path.exists(after_path):
        print(f"[WARNING] After image not found for {before_file}")
        continue

    # Load images in grayscale for SSIM
    before = cv2.imread(before_path)
    after = cv2.imread(after_path)
    gray_before = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    gray_after = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    # Compute SSIM and get difference map
    score, diff = ssim(gray_before, gray_after, full=True)
    diff = (diff * 255).astype("uint8")

    # Threshold the difference map
    _, thresh = cv2.threshold(diff, 200, 255, cv2.THRESH_BINARY_INV)

    # Find contours of the differences
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes on the "after" image
    for cnt in contours:
        if cv2.contourArea(cnt) > 100:  # Ignore small noise
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(after, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Save result
    cv2.imwrite(output_path, after)
    print(f"[INFO] Saved: {output_file}")