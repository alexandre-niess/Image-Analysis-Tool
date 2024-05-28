import numpy as np
from PIL import Image


def analyze_image(image_path):
    # Load the image and convert to a numpy array
    image = Image.open(image_path)
    image_np = np.array(image)

    # Splitting the RGB components
    red, green, blue = image_np[:, :, 0], image_np[:, :, 1], image_np[:, :, 2]

    # Define colors and thresholds
    star_threshold = 250
    meteor_color = [255, 0, 0, 255]  # RGBA for red
    water_color = [0, 0, 255, 255]   # RGBA for blue

    # Count stars
    stars_count = np.sum((red >= star_threshold) & (
        green >= star_threshold) & (blue >= star_threshold))

    # Count meteors
    meteors_count = np.sum(np.all(image_np == meteor_color, axis=-1))

    # Water mask
    water_mask = np.all(image_np == water_color, axis=-1)

    # Count meteors falling on water
    meteor_fall_on_water_count = 0
    for col in range(image_np.shape[1]):
        meteor_column = (image_np[:, col, :] == meteor_color).all(axis=-1)
        water_column = water_mask[:, col]
        if np.any(meteor_column) and np.any(water_column):
            meteor_positions = np.where(meteor_column)[0]
            # First water pixel in the column
            water_level = np.where(water_column)[0][0]
            if np.any(meteor_positions < water_level):
                meteor_fall_on_water_count += 1

    return stars_count, meteors_count, meteor_fall_on_water_count


# Example usage:
image_path = './meteor_challenge_01.png'
results = analyze_image(image_path)
print("Stars count:", results[0])
print("Meteors count:", results[1])
print("Meteors falling on water count:", results[2])
