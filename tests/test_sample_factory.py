import pytest
import numpy as np
from space_invaders.sample import Sample
from space_invaders.sample_factory import SampleFactory


STRING_SAMPLE = """
---
ooo
"""


def test_from_string():
    actual = SampleFactory.from_string(STRING_SAMPLE)
    expected = Sample(
        data=np.array(
            [
                list("---"),
                list("ooo"),
            ]
        )
    )
    assert actual == expected


def test_from_string_raises_type_error_if_not_string():
    with pytest.raises(TypeError) as ex:
        SampleFactory.from_string(1234)
    assert str(ex.value) == "The given data must be a string"
