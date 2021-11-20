import pytest
import numpy as np
from space_invaders.sample_slice import SampleSlice


def test_equal():
    left = SampleSlice(data=np.array([list("---")]), start_row=0, start_column=0)
    right = SampleSlice(data=np.array([list("---")]), start_row=0, start_column=0)
    assert left == right


def test_equal_with_different_data():
    left = SampleSlice(data=np.array([list("---")]), start_row=0, start_column=0)
    right = SampleSlice(data=np.array([]), start_row=0, start_column=0)
    assert left != right


def test_equal_with_different_start_row():
    left = SampleSlice(data=np.array([]), start_row=0, start_column=0)
    right = SampleSlice(data=np.array([]), start_row=1, start_column=0)
    assert left != right


def test_equal_with_different_start_column():
    left = SampleSlice(data=np.array([]), start_row=0, start_column=0)
    right = SampleSlice(data=np.array([]), start_row=0, start_column=1)
    assert left != right


def test_init_default_sample_slice():
    actual = SampleSlice()
    expected = SampleSlice(data=np.array([]), start_row=0, start_column=0)
    assert actual == expected
