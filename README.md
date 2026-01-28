# Video Scene Cut Detection: Histogram Analysis

This repository contains an implementation of **Video Scene Cut Detection** using histogram-based analysis. The project explores how to automatically identify transitions between different scenes in a video file.

## Project Overview

The core objective of this project is to implement a robust scene cut detection algorithm. By comparing the cumulative histograms of consecutive video frames, the system can identify the point of maximum difference, which typically corresponds to a scene transition.

### Key Features

- **Grayscale Conversion**: Preprocesses video frames by converting them to grayscale to simplify histogram computation.
- **Histogram Analysis**: Computes brightness histograms for every frame in the video.
- **Cumulative Histogram Comparison**: Uses the sum of absolute differences between consecutive cumulative histograms to detect scene changes.
- **Efficient Processing**: Leverages NumPy for vectorized operations, allowing for fast analysis of video data.

## Repository Structure

| File | Description |
| :--- | :--- |
| `ex1.py` | The main implementation script containing the scene cut detection logic. |
| `ex1_test.py` | A test script to verify the accuracy of the scene cut detection algorithm. |
| `README.md` | Documentation providing an overview of the project and its components. |
| `LICENSE` | MIT License for the project. |

## Requirements

The project requires the following Python libraries:
- `numpy`
- `mediapy` (for video reading)

You can install the dependencies using:
```bash
pip install numpy mediapy
```

## Usage

To run the scene cut detection:
```python
from ex1 import main

# Example usage
frame_indices = main("path/to/video.mp4", video_type=1)
print(f"Scene cut detected between frames: {frame_indices}")
```

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

## Authors
- Malak Laham
