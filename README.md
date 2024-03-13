# Basic Digital Image Processing Application(HW.py)

This project is a Python application for basic digital image processing(homework from NSYSU CSE course). It allows users to perform various operations on images such as opening, saving, displaying, adjusting contrast and brightness, resizing, rotating, and applying spatial filters. It also supports processing both grayscale and color images, including transformations like RGB to HSI conversion, and enhancing details using RGB complements. The application is built using Tkinter for the GUI, PIL for image handling, and matplotlib for plotting histograms and image transformations.

## Features

- Open and display image files, including support for .raw image format.
- Save the processed images to your system.
- Adjust contrast and brightness through linear, exponential, and logarithmic adjustments.
- Resize and rotate images.
- Perform gray-level slicing, bit-plane slicing, and histogram equalization.
- Apply spatial filters for smoothing, sharpening, median filtering, and applying Laplacian masks.
- Convert RGB images to HSI model and visualize the components.
- Enhance image details using RGB complements.
- Perform advanced operations like FFT processing and DFT steps visualization.
- Specific functionalities for color image processing including component extraction and segmentation.

## Prerequisites

Before running the application, ensure you have Python installed on your system. The application has been tested with Python 3.10.11. Additionally, you will need the following Python packages:

- Tkinter
- PIL (Pillow)
- matplotlib
- numpy

You can install these packages using pip:

```bash
pip install Pillow matplotlib numpy
```

## Running the Application
To run the application, navigate to the directory containing the script and run:

```bash
python fin.py
```
Replace fin.py with the name of the script if you have renamed it.

## Using the Application
Upon launching the application, you will be presented with a GUI where you can choose to open an image file to start processing. The interface provides buttons and entry fields for various image processing operations. Choose an operation, adjust the parameters if necessary, and click the corresponding button to apply the operation.

## Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.


---


# Advanced Digital Image Processing Toolkit(fin.py)

This toolkit provides a comprehensive suite of tools for digital image processing(final project from NSYSU CSE course). It is divided into two main components: the first focuses on basic image manipulations including adjusting contrast, resizing, rotating, and applying filters. The second component introduces advanced features such as watermarking, image overlaying, RGB to HSI conversion, and component analysis among others. The projects leverage Python libraries such as Tkinter for the GUI, PIL (Pillow) for image manipulation, matplotlib for visualization, along with custom modules `sheep` and `shineWu` for specialized processing.

## Features

- **Basic Operations**: Open, save, display, adjust contrast/brightness, resize, rotate, gray-level slicing, histogram equalization, and more.
- **Advanced Operations**: Add watermarks, overlay images with adjustable RGBA parameters, RGB to HSI conversion, extract RGB components, apply spatial filters, and more.
- **Visualization**: Display the original image alongside processed versions, including histograms and HSI components.
- **Custom Processing**: Utilize custom algorithms provided in `sheep` and `shineWu` modules for tasks like lowpass watermarking, color diffusion, and creating camouflage images.

## Prerequisites

- Python 3.9 or newer
- Tkinter (usually included with Python)
- PIL (Pillow)
- matplotlib
- numpy

You can install the necessary Python packages using pip:

```bash
pip install Pillow matplotlib numpy
```

## Running the Applications
Basic Image Processing: Navigate to the directory containing fin.py and run:
```bash
python fin.py
```

## Usage
- For both applications, use the GUI to interact with the functionalities provided.
- To apply basic image processing operations, use the buttons and fields in the first application's window.
- For advanced operations, including watermarking and image overlaying, use the second application's interface.
## Contributing
Contributions are welcome! Please feel free to fork the repository, make changes, and submit pull requests with your enhancements.

## Dependencies
Make sure the custom modules sheep and shineWu are correctly imported and accessible within the project's directory if they are part of the advanced image processing functionalities.
