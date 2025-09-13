import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from collections import Counter

def extract_color_palette(image_path, number_of_colors, show_chart=True):
    """
    Extracts and quantifies the dominant color palette from an image using K-Means clustering.
    
    :param image_path: The path to the image file.
    :param number_of_colors: The number of dominant colors to extract.
    :param show_chart: If True, displays a chart of the color palette.
    :return: A dictionary of colors (R, G, B) and their percentage.
    """
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    resized_image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_AREA)
    pixels = resized_image.reshape(-1, 3)

    kmeans = KMeans(n_clusters=number_of_colors, random_state=42, n_init=10)
    kmeans.fit(pixels)

    total_pixels = len(kmeans.labels_)
    counts = Counter(kmeans.labels_)
    
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    palette = {}
    dominant_colors_rgb = []
    percentages = []

    for cluster_index, count in sorted_counts:
        color_rgb = tuple(kmeans.cluster_centers_[cluster_index].astype('uint8'))
        percentage = (count / total_pixels) * 100
        
        palette[color_rgb] = percentage
        dominant_colors_rgb.append(color_rgb)
        percentages.append(percentage)

    if show_chart:
        plt.figure(figsize=(10, 5))
        bars = plt.bar(range(number_of_colors), percentages, color=[tuple(c/255.0 for c in color) for color in dominant_colors_rgb])
        
        plt.title(f'Color Signature of: {image_path.split("/")[-1]}')
        plt.ylabel('Percentage (%)')
        plt.xticks([]) # Hide x-axis ticks
        
        for i, bar in enumerate(bars):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{percentages[i]:.1f}%', ha='center', va='bottom')

        plt.ylim(0, max(percentages) + 10)
        plt.show()

    return palette

if __name__ == '__main__':
    your_image_path = 'assets/imgs/flamboyant.png' 
    
    try:
        color_signature = extract_color_palette(your_image_path, number_of_colors=5)
        print("Color Signature (RGB: Percentage):")
        for color, percentage in color_signature.items():
            print(f"Color {color}: {percentage:.2f}%")
    except FileNotFoundError:
        print(f"Error: The file '{your_image_path}' was not found.")