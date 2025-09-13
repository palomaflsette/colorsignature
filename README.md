# 🎨 Color Signature

**Extract and visualize the dominant color palette from any image using machine learning**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg)](https://opencv.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

> Transform any image into its essential color DNA using K-Means clustering and computer vision

## ✨ Features

- 🔍 **Smart Color Extraction**: Uses K-Means clustering to identify the most dominant colors
- 📊 **Visual Analytics**: Generates beautiful bar charts showing color distribution percentages  
- 🎯 **Customizable**: Choose how many colors to extract (3, 5, 10, or any number you want)
- 🖼️ **Multiple Formats**: Works with PNG, JPG, and other common image formats
- 🚀 **Fast Processing**: Optimized image resizing for quick analysis
- 📈 **Quantified Results**: Get exact RGB values and percentage breakdowns

## 🚀 Quick Start

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/colorsignature.git
cd colorsignature
```

2. **Set up the environment**

**Option A: Using Conda (Recommended)**
```bash
conda env create -f env.yml
conda activate colorsignature
```

**Option B: Using pip**
```bash
pip install -r requirements.txt
```

### Usage

**Basic Usage:**
```python
from color_pallet_analyzer import extract_color_palette

# Extract 5 dominant colors and show visualization
color_signature = extract_color_palette('your_image.jpg', number_of_colors=5)

# Print results
for color, percentage in color_signature.items():
    print(f"RGB{color}: {percentage:.2f}%")
```

**Run the example:**
```bash
python color_pallet_analyzer.py
```

## 🎨 Examples

### Classic Artworks Analysis

| Image | Color Palette |
|-------|---------------|
| 🌅 **Monet's Impression Sunrise** | Warm oranges, deep blues, soft yellows |
| ⭐ **Van Gogh's Starry Night** | Swirling blues, bright yellows, dark purples |
| 🌺 **Flamboyant Tree** | Vibrant reds, lush greens, earthy browns |

*Sample images included in `assets/imgs/` for testing*

## 🔧 API Reference

### `extract_color_palette(image_path, number_of_colors, show_chart=True)`

**Parameters:**
- `image_path` (str): Path to your image file
- `number_of_colors` (int): Number of dominant colors to extract
- `show_chart` (bool): Whether to display the color distribution chart

**Returns:**
- `dict`: Color palette as `{(R, G, B): percentage}` pairs

**Example Output:**
```python
{
    (45, 87, 44): 23.45,    # Dark green: 23.45%
    (201, 176, 55): 18.32,  # Golden yellow: 18.32%
    (89, 67, 31): 15.67,    # Brown: 15.67%
    (178, 34, 34): 12.89,   # Red: 12.89%
    (70, 130, 180): 10.23   # Steel blue: 10.23%
}
```

## 🛠️ How It Works

1. **Image Preprocessing**: Loads and converts image to RGB format
2. **Optimization**: Resizes image to 100x100 pixels for faster processing
3. **Pixel Analysis**: Reshapes image data into a pixel array
4. **K-Means Clustering**: Groups similar colors into clusters
5. **Color Quantification**: Calculates the percentage of each dominant color
6. **Visualization**: Creates an intuitive bar chart of the color palette

## 📊 Technical Details

- **Algorithm**: K-Means clustering with k=number_of_colors
- **Color Space**: RGB (Red, Green, Blue)
- **Image Processing**: OpenCV for efficient image manipulation
- **Machine Learning**: scikit-learn for clustering algorithms
- **Visualization**: matplotlib for beautiful charts

## 🎯 Use Cases

- **Art Analysis**: Study color compositions in paintings and artwork
- **Brand Design**: Extract brand colors from logos and marketing materials  
- **Interior Design**: Analyze room colors for decoration planning
- **Fashion**: Identify trending colors in clothing and accessories
- **Photography**: Understand color themes in your photo collections
- **Web Design**: Generate color schemes from inspiration images

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenCV** for powerful computer vision capabilities
- **scikit-learn** for machine learning algorithms
- **matplotlib** for beautiful data visualization
- **NumPy** for efficient numerical computing

---

<div align="center">

**Made with ❤️ for artists, designers, and color enthusiasts**

[⭐ Star this repo](../../stargazers) • [🐛 Report Bug](../../issues) • [💡 Request Feature](../../issues)

</div>
