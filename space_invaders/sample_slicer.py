from space_invaders.sample_slice import SampleSlice


class SampleSlicer:
    "Creates all possible slices of a sample, given a specific target shape."

    def __init__(self, target_shape):
        self.target_shape = target_shape

    @property
    def target_shape(self):
        return self._target_shape

    @target_shape.setter
    def target_shape(self, shape):
        self._target_shape = shape
        self.row_count, self.column_count = shape

    def slices(self, sample):
        self.sample = sample
        self._check_if_slicable()

        for row_index in range(self._compute_max_row_index()):
            for column_index in range(self._compute_max_column_index()):
                yield self._get_slice(row_index, column_index)

    def _check_if_slicable(self):
        if (
            self.sample.row_count < self.row_count
            or self.sample.column_count < self.column_count
        ):
            raise ValueError("The window size exceeds the size of the original sample")

    def _compute_max_row_index(self):
        return self.sample.row_count - self.row_count + 1

    def _compute_max_column_index(self):
        return self.sample.column_count - self.column_count + 1

    def _get_slice(self, row_index, column_index):
        end_row_index = row_index + self.row_count
        end_column_index = column_index + self.column_count
        return SampleSlice(
            data=self.sample.data[
                row_index:end_row_index, column_index:end_column_index
            ],
            start_row=row_index,
            start_column=column_index,
        )
