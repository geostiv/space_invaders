import numpy as np


class InvaderFinder:
    "Uses a SampleSlicer and Detector to find a specific invader in the radar sample."

    @staticmethod
    def find(radar_sample, invader_sample, slicer, detector):
        radar_heatmap = np.empty(
            (
                radar_sample.shape[0] - invader_sample.shape[0] + 1,
                radar_sample.shape[1] - invader_sample.shape[1] + 1,
            )
        )
        for radar_slice in slicer.slices(radar_sample):
            score = detector.detect(radar_slice, invader_sample)
            radar_heatmap[radar_slice.start_row, radar_slice.start_column] = score
        return radar_heatmap
