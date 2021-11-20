import numpy as np
import editdistance


class Detector:
    "Detects a specific invader in a radar sample slice by using the edit distance measure."

    @staticmethod
    def detect(radar_sample, invader_sample):
        row_distances = []
        for row in range(radar_sample.row_count):
            radar_row = radar_sample.get_row(row)
            invader_row = invader_sample.get_row(row)
            row_distances.append(editdistance.eval(radar_row, invader_row))
        return Detector._compute_score(row_distances)

    @staticmethod
    def _compute_score(data):
        return np.sum(data)
