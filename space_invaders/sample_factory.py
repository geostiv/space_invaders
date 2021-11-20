import numpy as np

from space_invaders.sample import Sample


class SampleFactory:
    "Creates Sample objects from different sources."

    @staticmethod
    def from_string(data: str):
        if not isinstance(data, str):
            raise TypeError("The given data must be a string")
        return Sample(
            np.array(
                [list(line) for line in data.split("\n") if line],
            ),
        )
