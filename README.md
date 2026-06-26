# Image Metadata Cleaner & Batch Renamer

A simple Python script that removes image metadata and renames images sequentially.

## Features

- Removes EXIF and other embedded metadata.
- Preserves the original image quality.
- Renames images in sequential order.
- Supports JPG, JPEG, and PNG images.
- Saves processed images to a separate output folder.

## Folder Structure

```
project/
│
├── input_photos/
│   ├── image1.jpg
│   ├── image2.png
│   └── ...
│
├── output_photos/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository.

```bash
git clone <repository-url>
cd <repository-folder>
```

2. Install the required dependency.

```bash
pip install -r requirements.txt
```

## Usage

1. Place all images inside the `input_photos` directory.

2. Run the script.

```bash
python main.py
```

3. The processed images will be saved in the `output_photos` directory.

## Output

Original files:

```
Vacation.jpg
IMG_1234.jpeg
Screenshot.png
```

Output files:

```
photo_0001.jpg
photo_0002.jpeg
photo_0003.png
```

## Supported Formats

- `.jpg`
- `.jpeg`
- `.png`

## How It Works

The script:

1. Reads every image from the `input_photos` folder.
2. Creates a new image containing only the pixel data.
3. Removes metadata by copying only the image pixels.
4. Renames the image using the format:

```
photo_0001.jpg
photo_0002.jpg
photo_0003.png
```

5. Saves the cleaned image in the `output_photos` folder.

## Notes

- Original images are never modified.
- If the `output_photos` folder does not exist, it will be created automatically.
- Images are processed in the order returned by your operating system.
- File extensions are preserved.
