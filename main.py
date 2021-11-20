import os

from pathlib import Path

from constants import (
    FILE_FORMAT,
    HEATMAP_ROOT,
    INVADER_DETECTION_THRESHOLD,
    INVADERS_ROOT,
    KNOWN_INVADERS,
    RADAR_ROOT,
    RECORDED_RADARS,
)
from space_invaders.detector import Detector
from space_invaders.invader_finder import InvaderFinder
from space_invaders.report import Report
from space_invaders.sample_factory import SampleFactory
from space_invaders.sample_slicer import SampleSlicer


def create_report(target_path, filename, invader, radar_heatmap):
    if not target_path.exists():
        os.makedirs(target_path)
    Report(
        invader,
        radar_heatmap,
        INVADER_DETECTION_THRESHOLD,
    ).save(Path(target_path, filename))


def read_sample(path):
    with open(path, "rt") as f:
        return SampleFactory.from_string(f.read())


def find_invader(radar, invader):
    return InvaderFinder.find(
        radar,
        invader,
        SampleSlicer(invader.shape),
        Detector,
    )


def main():
    for radar_file in RECORDED_RADARS:
        radar = read_sample(Path(RADAR_ROOT, f"{radar_file}{FILE_FORMAT}"))
        for invader_file in KNOWN_INVADERS:
            invader = read_sample(Path(INVADERS_ROOT, f"{invader_file}{FILE_FORMAT}"))
            radar_heatmap = find_invader(radar, invader)
            create_report(
                target_path=Path(HEATMAP_ROOT, radar_file),
                filename=f"{invader_file}.png",
                invader=invader,
                radar_heatmap=radar_heatmap,
            )


if __name__ == "__main__":
    main()
