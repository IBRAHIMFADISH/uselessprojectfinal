import cv2
import numpy as np
import math
import os

# --- Ask the user for image file path ---
image_path = input("Enter the path to your donut image (e.g., doughnut.jpg): ").strip()
# Check if file exists
if not os.path.isfile(image_path):
    print(" Image file not found.")
    exit()

# --- Load the image ---
image = cv2.imread(image_path)
if image is None:
    print(" Unable to load the image.")
    exit()

# --- Preprocessing ---
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# --- Threshold to isolate the hole (dark region) ---
_, thresh = cv2.threshold(blurred, 40, 255, cv2.THRESH_BINARY_INV)

# --- Find contours ---
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# --- Detect circular hole ---
found = False
for cnt in contours:
    area = cv2.contourArea(cnt)
    if 500< area < 20000: # Adjust range based on donut size
        perimeter = cv2.arcLength(cnt, True)
        if perimeter == 0:
            continue
        circularity = 4 * math.pi * area / (perimeter ** 2)

        if circularity > 0.5:
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            hole_area = math.pi * (radius ** 2)

            # Draw and annotate
            cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 0), 2)
            label = f"Radius: {radius:.1f}px | Area: {hole_area:.1f}px²"
            cv2.putText(image, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            print(f" {label}")
            found = True
            break

if not found:
    print(" No suitable donut hole detected.")
# --- Show and save result ---
cv2.imshow("Donut Hole Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save result image
output_path = "output_donut_detection.png"
cv2.imwrite(output_path, image) 
print(f" Result saved as {output_path}")