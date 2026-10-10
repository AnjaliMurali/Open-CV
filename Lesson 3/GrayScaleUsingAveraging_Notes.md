# OpenCV – Grayscale Image by Averaging

## 1. Import libraries

```python
import cv2
import numpy as np
```

* `cv2` → OpenCV library for image processing.
* `numpy` → used for arrays and numerical calculations.

---

## 2. Read the image

```python
img = cv2.imread('Lesson 3/images/pika.png')
```

* Reads the image from the given path.
* OpenCV reads a color image in **BGR** format.
* Each pixel has 3 values:

```text
[B, G, R]
```

Example:

```text
[100, 150, 200]
```

---

## 3. Convert image to `int32`

```python
img = img.astype(np.int32)
```

* Normally, image pixels are stored as `uint8`.
* `uint8` can store values from **0 to 255**.
* We use `int32` to safely perform calculations such as:

```text
100 + 150 + 200 = 450
```

* This prevents the **overflow warning**.

---

## 4. Get image dimensions

```python
(row, col) = img.shape[0:2]
```

* `row` → number of rows (image height).
* `col` → number of columns (image width).

For example:

```text
img.shape = (600, 800, 3)

row = 600
col = 800
```

The `3` represents the three color channels:

```text
B, G, R
```

---

## 5. Visit every pixel

```python
for i in range(row):
    for j in range(col):
```

* The **outer loop** goes through each row.
* The **inner loop** goes through each column.
* Together, they visit every pixel in the image.

---

## 6. Calculate the average of BGR

```python
average = int(sum(img[i, j]) / 3)
```

For example, if a pixel is:

```text
[100, 150, 200]
```

Then:

```text
Average = (100 + 150 + 200) / 3
        = 450 / 3
        = 150
```

So:

```text
average = 150
```

---

## 7. Make the pixel grayscale

```python
img[i, j] = [average, average, average]
```

If:

```text
average = 150
```

then:

```text
[100, 150, 200]
```

becomes:

```text
[150, 150, 150]
```

### Important idea

A grayscale pixel has the **same value in all three channels**:

```text
[B, G, R]

[100, 100, 100] → dark gray
[150, 150, 150] → gray
[255, 255, 255] → white
[0, 0, 0]       → black
```

---

## 8. Convert back to `uint8`

```python
img = img.astype(np.uint8)
```

* The calculations were done using `int32`.
* After calculations, convert the image back to `uint8`.
* `uint8` is the standard image format for pixel values from **0 to 255**.

---

## 9. Display the image

```python
cv2.imshow('Grayscale Image by Averaging', img)
```

* Displays the grayscale image.
* The text is the title of the window.

---

## 10. Wait for a key

```python
cv2.waitKey(0)
```

* `0` means wait indefinitely.
* The window stays open until a key is pressed.

---

## 11. Close the window

```python
cv2.destroyAllWindows()
```

* Closes all OpenCV windows.

---

# ⭐ Main Concept to Remember

The program converts a color image to grayscale using:

```text
BGR pixel
   ↓
Add B + G + R
   ↓
Divide by 3
   ↓
Find average
   ↓
Set B = G = R = average
   ↓
Grayscale pixel
```

### Example

```text
Original pixel:
[60, 120, 180]

Average:
(60 + 120 + 180) / 3
= 120

New pixel:
[120, 120, 120]
```

The program repeats this process for **every pixel**.

---

# Important Lines to Know

| Code                          | Meaning                                 |
| ----------------------------- | --------------------------------------- |
| `cv2.imread()`                | Read an image                           |
| `img.astype(np.int32)`        | Convert data type for safe calculations |
| `img.shape`                   | Get image dimensions                    |
| `img[i, j]`                   | Access a particular pixel               |
| `sum()`                       | Add BGR values                          |
| `/ 3`                         | Calculate average                       |
| `[average, average, average]` | Create grayscale pixel                  |
| `astype(np.uint8)`            | Convert back to normal image format     |
| `cv2.imshow()`                | Display image                           |
| `cv2.waitKey(0)`              | Wait for a key                          |
| `cv2.destroyAllWindows()`     | Close windows                           |

# One-Line Definition

**Grayscale conversion by averaging means finding the average of the B, G, and R values of each pixel and assigning that average to all three channels.**
