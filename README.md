🍩
Basic Details

  - **Team Name:**royal warriors*
  - **Team Members:**
      - Team Lead: ibrahim fadish tayyib
      - Member 2: clinton anton

### Project Description

This project uses computer vision techniques to analyze an image of a donut and automatically detect the circular hole. The program then calculates and displays the radius and area of the detected hole, providing a quantitative analysis of its size.

### The Problem (that doesn't exist)

Imagine a scenario where a large-scale bakery needs to ensure consistency in its products. Manually measuring the size of donut holes is time-consuming and prone to human error. This project offers a fun and practical solution to automatically quantify the dimensions of a donut's hole from a simple image.

### The Solution (that nobody asked for)

We developed a Python script that leverages the OpenCV library to process an image. By using a series of filters and contour detection algorithms, the program can accurately identify the dark, circular region of the donut's hole, filter out irrelevant shapes, and then perform the necessary calculations to determine its radius and area.

### Technical Details

**Technologies/Components Used**

For Software:

  - **Languages used:** Python 3
  - **Libraries used:**
      - `cv2` (OpenCV) for image processing.
      - `numpy` for numerical operations.
      - `math` for mathematical calculations (e.g., PI).
      - `os` for handling file paths.

### Implementation

The program follows a clear pipeline:

1. **Image Preprocessing:** The input image is converted to grayscale and then blurred to reduce noise and enhance the edges of the donut hole.
2. **Thresholding:** A binary inverse threshold is applied to isolate dark regions (the donut hole) as a white shape on a black background.
3. **Contour Detection:** The script finds all contours (continuous curves) in the thresholded image.
4. **Hole Identification:** The contours are filtered based on their area and circularity to find the one most likely to be the donut hole.
5. **Calculation & Annotation:** For the identified contour, the script calculates its radius and area and then draws a circle and a label on the original image with the results.

### Installation

No special installation is required beyond the standard Python libraries.

```bash
# Install OpenCV and numpy
pip install opencv-python numpy
```

### Run

To run the program, navigate to the project directory in your terminal and execute the following command, providing the path to your donut image when prompted.

```bash
# Run the script
python your_script_name.py
```

### Schematic & Circuit
