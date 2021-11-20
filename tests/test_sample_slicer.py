import pytest
import numpy as np

from space_invaders.sample import Sample
from space_invaders.sample_slicer import SampleSlicer


@pytest.fixture(scope="module")
def sample():
    return Sample(
        data=np.array(
            [
                list("1234567"),
                list("2345678"),
                list("3456789"),
                list("4567890"),
            ]
        )
    )


def test_slice_first_sample(sample):
    actual = next(SampleSlicer((2, 3)).slices(sample))
    expected = Sample(
        data=np.array(
            [
                list("123"),
                list("234"),
            ]
        ),
    )
    assert np.array_equal(actual.data, expected.data)


def test_slice_sample_with_max_valid_sample_size(sample):
    actual = next(SampleSlicer(sample.shape).slices(sample))
    expected = Sample(data=sample.data)
    assert np.array_equal(actual.data, expected.data)


def test_slice_sample(sample):
    sample_rows, sample_cols = sample.shape
    actual = list(SampleSlicer((sample_rows - 1, sample_cols - 1)).slices(sample))
    expected = [
        Sample(
            data=np.array(sample.data[0 : sample_rows - 1, 0 : sample_cols - 1]),
        ),
        Sample(
            data=np.array(sample.data[0 : sample_rows - 1, 1:sample_cols]),
        ),
        Sample(
            data=np.array(sample.data[1:sample_rows, 0 : sample_cols - 1]),
        ),
        Sample(
            data=np.array(sample.data[1:sample_rows, 1:sample_cols]),
        ),
    ]
    for act, exp in zip(actual, expected):
        assert np.array_equal(act.data, exp.data)


def test_exception_is_raised_if_sample_has_more_rows_than_sample(sample):
    with pytest.raises(ValueError) as ex:
        next(SampleSlicer((sample.shape[0] + 1, 1)).slices(sample))
    assert str(ex.value) == "The window size exceeds the size of the original sample"


def test_exception_is_raised_if_sample_has_more_columns_than_sample(sample):
    with pytest.raises(ValueError) as ex:
        next(SampleSlicer((1, sample.shape[1] + 1)).slices(sample))
    assert str(ex.value) == "The window size exceeds the size of the original sample"
