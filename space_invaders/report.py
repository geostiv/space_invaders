import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


class Report:
    """
    Creates a report containing the possible positions of invaders on a radar sample.

    The threshold parameter is used to enhance the result.
    A lower threshold reduces the noise, but increases the probability for false negatives.
    A higher threshold increases the noise and the probability for false positives.
    """

    def __init__(self, invader_sample, radar_heatmap, detection_threshold=None):
        self.invader_sample = invader_sample
        self.radar_heatmap = self._enhance(radar_heatmap, detection_threshold)

    def save(self, path, dpi=300):
        fig, _ = plt.subplots()
        sns.heatmap(
            self.radar_heatmap,
            vmin=self.radar_heatmap.min(),
            vmax=self.radar_heatmap.max(),
            cbar=False,
        )
        plt.axis("off")
        fig.savefig(path, dpi=dpi)

    def _enhance(self, radar_heatmap, detection_threshold):
        """
        Filters noise in the radar heatmap using a given detection threshold.

        The detector uses the edit distance (= score) to detect invaders.
        The smaller the score, the higher the probability for the presence of an invader.
        To reduce noise, a threshold is used to emphasize the scores below that threshold.
        Scores equal to or above the threshold are set to the maximum value (size of the invader sample).
        """
        if detection_threshold:
            max_detection_score = self.invader_sample.size * detection_threshold
            radar_heatmap[
                radar_heatmap > max_detection_score
            ] = self.invader_sample.size
        return radar_heatmap
