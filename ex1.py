import mediapy as media
import numpy as np

def main(video_path, video_type):
    """
    Main entry point for ex1
    :param video_path: path to video file
    :param video_type: category of the video (either 1 or 2)
    :return: a tuple of integers representing the frame number for which the scene cut was detected (i.e. the last frame index of the first scene and the first frame index of the second scene)
    """
    # Read the video using mediapy
    video = media.read_video(video_path)

    # Convert the video to grayscale
    video = np.mean(video, axis=3).astype(np.uint8)

    # Flatten the video frames to compute histograms efficiently since histograms aren't affected by pixel position
    num_frames, height, width = video.shape
    flattened_frames = video.reshape(num_frames, -1)  # new shape: (num_frames, height * width)

    # Compute histograms for all frames at once
    brightness_levels = 256
    histograms = np.array([np.histogram(frame, bins=brightness_levels, range=(0, brightness_levels))[0] for frame in flattened_frames])

    # Compute cumulative histograms for all frames
    cumulative_histograms = np.cumsum(histograms, axis=1)

    # Compute the sum of absolute differences between consecutive cumulative histograms
    differences = np.sum(np.abs(np.diff(cumulative_histograms, axis=0)), axis=1)

    # Find the index of the frame pair with the maximum difference
    max_diff_index = np.argmax(differences)
    return int(max_diff_index), int(max_diff_index + 1)
