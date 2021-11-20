import numpy as np
import pytest

from space_invaders.sample import Sample
from space_invaders.detector import Detector


@pytest.fixture(scope="module")
def sample():
    return Sample(
        data=np.array(
            [
                list("123"),
                list("456"),
                list("789"),
            ]
        )
    )


def test_detect_full_match(sample):
    assert Detector.detect(sample, sample) == 0


def test_detect_partial_match(sample):
    other_sample = Sample(
        data=np.array(
            [
                list("023"),
                list("406"),
                list("780"),
            ]
        )
    )
    assert Detector.detect(sample, other_sample) == 3


def test_detect_full_mismatch(sample):
    assert Detector.detect(sample, Sample(np.zeros(sample.shape))) == sample.size
