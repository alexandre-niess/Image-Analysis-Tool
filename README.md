# Image Analysis Tool

This repository contains a Python script for analyzing images to count the number of stars, meteors, and meteors falling on water. The script utilizes `numpy` for numerical operations and `PIL` (Python Imaging Library) for image processing.

## Features

- **Count Stars**: Identifies and counts the number of stars in an image based on RGB thresholds.
- **Count Meteors**: Detects and counts meteors represented by a specific color.
- **Meteors Falling on Water**: Determines the number of meteors falling into water based on their respective colors.

## Requirements

- Python 3.x
- numpy
- pillow (PIL Fork)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image-analysis-tool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd image-analysis-tool
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your image file in the project directory.
2. Modify the `image_path` variable in the script to point to your image file.
3. Run the script:
   ```bash
   python analyze_image.py
   ```
4. The script will output the counts of stars, meteors, and meteors falling on water.

## Example

```python
# Example usage:
image_path = './meteor_challenge_01.png'
results = analyze_image(image_path)
print("Stars count:", results[0])
print("Meteors count:", results[1])
print("Meteors falling on water count:", results[2])
```

### Output based on the image in this repository

```
Stars count: 315
Meteors count: 328
Meteors falling on water count: 105
```

## Script Details

### analyze_image(image_path)

- **Input**: 
  - `image_path` (str): Path to the image file.

- **Output**: 
  - A tuple containing:
    - `stars_count` (int): Number of stars.
    - `meteors_count` (int): Number of meteors.
    - `meteor_fall_on_water_count` (int): Number of meteors falling into water.

- **Processing Steps**:
  1. Load the image and convert it to a numpy array.
  2. Split the RGB components of the image.
  3. Define the colors and thresholds for stars, meteors, and water.
  4. Count the stars based on the RGB threshold.
  5. Count the meteors by identifying pixels matching the meteor color.
  6. Create a mask for water and count meteors that fall into water based on their positions.



## Contact

For any questions or suggestions, acess the "Contato" section of my [website](https://alexandre-niess.github.io/SitePortifolio/).

