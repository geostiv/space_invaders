# Context

Given an invader sample, this tool searches for that invader in a radar sample. The result is a heatmap of the radar sample, showing potential occurrences of the invader.

### Usage

Install the required packages listed in the file *requirements.txt*.

Run the file *main.py* in the root folder. You can find the results (radar heatmaps as PNG files) in the folder *heatmaps/\<radar>*.

### Searching for multiple invaders (in multiple radar samples)

You can search for multiple invaders in one go by placing a text file with the invader pattern in the folder *samples/invaders* and adding the filename (without suffix) to the **KNOWN_INVADERS** list in *constants.py*. The same is true for radar samples, where the folder for the pattern files is *samples/radar* and the list in *constants.py* is **RECORDED_RADARS**.

### Fine-tuning the result heatmap

The constant **INVADER_DETECTION_THRESHOLD** in *constants.py* lets you control the noise filtering in the radar heatmap containing the found invaders. You can set it to values between 0 and 1, where a lower value means less noise, but also a higher probability for false negative, i.e. missing potential invaders.

A higher value is more likely to detect more invaders, but it also increases noise and the probability for false positives. The default value is 0.4, which means that 60% of the invader sample must match with the underlying slice of the radar sample.