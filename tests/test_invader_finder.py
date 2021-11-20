import numpy as np
import pytest

from space_invaders.detector import Detector
from space_invaders.invader_finder import InvaderFinder
from space_invaders.sample_slice import Sample
from space_invaders.sample_slicer import SampleSlicer


@pytest.fixture(scope="module")
def radar():
    return Sample(
        data=np.array(
            [
                list("--oo"),
                list("--oo"),
                list("oo--"),
                list("oo--"),
            ]
        )
    )


def test_find_unknown_invader(radar):
    invader = Sample(
        data=np.array(
            [
                list("xxx"),
                list("xxx"),
                list("xxx"),
            ]
        )
    )
    actual = InvaderFinder.find(
        radar,
        invader,
        SampleSlicer(invader.shape),
        Detector,
    )
    expected = np.array(
        [
            [9, 9],
            [9, 9],
        ]
    )
    assert np.array_equal(actual, expected)


def test_find_known_invader(radar):
    invader = Sample(
        data=np.array(
            [
                list("--o"),
                list("--o"),
                list("oo-"),
            ]
        )
    )
    actual = InvaderFinder.find(
        radar,
        invader,
        SampleSlicer(invader.shape),
        Detector,
    )
    expected = np.array(
        [
            [0, 3],
            [3, 4],
        ]
    )
    assert np.array_equal(actual, expected)
