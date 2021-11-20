# Percentage for maximum difference between the invader
# and the respective region in the radar sample.
# Lower values -> less noise, more false negatives.
# Higher values -> more noise, more false positives.
#
# Example:
# A threshold of 0.4 means that 60% of the
# radar sample slice must match with the invader sample.
INVADER_DETECTION_THRESHOLD = 0.4


# File names
KNOWN_INVADERS = ["fat", "slimy"]
RECORDED_RADARS = ["independence_day"]
FILE_FORMAT = ".txt"

# Root folders
HEATMAP_ROOT = "heatmaps"
INVADERS_ROOT = "samples/invaders"
RADAR_ROOT = "samples/radar"
