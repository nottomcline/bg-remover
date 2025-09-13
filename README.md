# Background Removal Script

This Python script removes the background from images using [rembg](https://github.com/danielgatis/rembg). It supports single images or batch processing of all images in a folder.

The output is saved as PNG files to preserve transparency.

---

## Features

- Remove backgrounds from PNG, JPG, JPEG, WEBP, BMP files
- Batch process a directory of images
- Choose different models (`u2net`, `u2netp`, etc.)
- Fast processing using a reusable session

---

## Requirements

- Python 3.9+
- `rembg` library
- Optional: `venv` for isolated environments

---

## Setup

### 1. Create a virtual environment

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### Usage

Single image

```bash
python remove_bg.py --input path/to/image.jpg --output path/to/output.png
```

--input or -i : path to the image file
--output or -o : path to the output file (will be PNG to preserve transparency)

Batch processing (directory)

```bash
python remove_bg.py --input path/to/images_folder --output path/to/output_folder
```

All images with supported extensions (.png, .jpg, .jpeg, .webp, .bmp) in the folder will be processed.
Output files will have \_no_bg appended to their filename.

Optional: Specify model

```bash
python remove_bg.py --input images --output output --model u2netp
```

Common model names: u2net (default), u2netp, u2net_human_seg
