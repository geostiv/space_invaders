import numpy as np

from space_invaders.sample import Sample


class SampleSlice(Sample):
    "A slice of a sample, additionally storing the start row and column of the slice in the original sample."

    def __init__(self, data=np.array([]), start_row=0, start_column=0):
        super().__init__(data=data)
        self._start_row = start_row
        self._start_column = start_column

    @property
    def start_row(self):
        return self._start_row

    @property
    def start_column(self):
        return self._start_column

    def __str__(self):
        pattern = ("\n").join("".join(line) for line in self.data)
        return f"Row: {self.start_row}; Column: {self.start_column}\n{pattern}"

    def __eq__(self, other):
        return (
            np.array_equal(self.data, other.data)
            and self.start_row == other.start_row
            and self.start_column == other.start_column
        )
