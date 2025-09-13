import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def extract_color_palette(image_path, number_of_colors, show_chart=True):
    """
    Extracts the dominant color palette from an image using K-Means clustering.
    
    :param image_path: The path to the image file.
    :param number_of_colors: The number of dominant colors to extract.
    :param show_chart: If True, displays a chart of the color palette.
    :return: A list of tuples (R, G, B) representing the color palette.
    """

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


    resized_image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_AREA)

    pixels = resized_image.reshape(-1, 3)


    kmeans = KMeans(n_clusters=number_of_colors, random_state=42, n_init=10)
    kmeans.fit(pixels)

    
    dominant_colors = kmeans.cluster_centers_.astype('uint8')

    if show_chart:
        plt.figure(figsize=(8, 4))
        plt.pie(np.ones(number_of_colors), colors=dominant_colors/255.0, labels=[f'Color #{i+1}' for i in range(number_of_colors)])
        plt.title(f'Color Signature of: {image_path.split("/")[-1]}')
        plt.show()

    return dominant_colors

# --- USAGE EXAMPLE ---
if __name__ == '__main__':
    
    your_image_path = 'your_image_here.jpg' 
    
    try:
        palette = extract_color_palette(your_image_path, number_of_colors=5)
        print("Color Palette (RGB):")
        print(palette)
    except FileNotFoundError:
        print(f"Error: The file '{your_image_path}' was not found.")
        print("Please check the filename and make sure it is in the same folder as the script.")