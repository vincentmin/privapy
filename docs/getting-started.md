# Getting Started

## Installation

To install the package, run:

```bash
pip install privapy
```

## Usage

### text

```python
from privapy.text import TextCleaner

text = "I live in New York and work at Google. My email is john@google.com"
cleaner = TextCleaner(steps="all")
cleaned_text = cleaner.clean(text)
# 'I live in <<ENT>> and work at <<ENT>. My email is <<EMAIL>>'
```

### image

```python
from privapy.image import ImageCleaner
from PIL import Image

cleaner = ImageCleaner()
img = Image.open("image.jpg")
cleaned_image = cleaner.clean(img)
```

input image (`img`):
![input image](_static/input.png)
output image (`cleaned_image`):
![output image](_static/output.png)

## Coming in future releases

- text
  - Add more cleaning methods
  - Add Spacy integration
- image
  - Add more cleaning methods
    - blackout
    - pixelate
  - Add more detection methods
    - face detection
    - dlib
    - mediapipe
