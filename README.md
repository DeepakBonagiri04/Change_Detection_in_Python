
---

### 📁 `README_Change_Detection.md`
```markdown
# Change Detection App

## 🔹 Overview
This Streamlit tool detects changes between two satellite images of the same region taken at different times. It highlights changes using difference maps and offers threshold control for better tuning.

## 🔹 Features
- Upload two images (Image A and Image B)
- Automatic preprocessing
- Image subtraction or SSIM-based comparison
- Adjustable threshold slider
- View and download detected changes

## 🔹 Requirements
```bash
pip install streamlit opencv-python scikit-image numpy

streamlit run change_detection_app.py
