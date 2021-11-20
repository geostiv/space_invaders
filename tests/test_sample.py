import pytest
import numpy as np
from space_invaders.sample import Sample


STRING_SAMPLE = """
---
ooo
"""


@pytest.fixture(scope="module")
def sample_data():
    return np.array(
        [
            list("---"),
            list("ooo"),
        ]
    )


@pytest.fixture(scope="module")
def sample(sample_data):
    return Sample(sample_data)


def test_init_empty_sample():
    actual = Sample()
    expected = Sample(data=np.array([]))
    assert actual == expected.data


def test_init_non_empty_sample(sample_data):
    expected = Sample(data=sample_data)
    assert np.array_equal(sample_data, expected.data)


def test_to_string(sample):
    assert str(sample) == STRING_SAMPLE.strip()


def test_row_count(sample):
    assert sample.row_count == 2


def test_column_count(sample):
    assert sample.column_count == 3


def test_shape(sample):
    assert sample.shape == (2, 3)


def test_size(sample):
    assert sample.size == sample.shape[0] * sample.shape[1]


def test_get_row(sample):
    actual = sample.get_row(0)
    expected = np.array(list("---"))
    assert np.array_equal(actual, expected)


def test_get_column():
    actual = Sample(data=np.array([["-"]])).get_column(0)
    expected = np.array(list("-"))
    assert np.array_equal(actual, expected)


def test_equal(sample_data):
    data = sample_data
    left = Sample(data=data)
    right = Sample(data=data)
    assert left == right


def test_not_equal(sample_data):
    left = Sample(data=sample_data)
    right = Sample(data=np.array(list("--")))
    assert left != right
