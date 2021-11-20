import numpy as np


class Sample:
    """
    Stores a 2D-array of a pattern.

    Objects of this class can be used to store and process radar or invader samples.
    """

    def __init__(self, data=np.array([])):
        self.data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data
        try:
            self._row_count, self._column_count = new_data.shape
        except ValueError:
            self._row_count = 0
            self._column_count = 0

    @property
    def row_count(self):
        return self._row_count

    @property
    def column_count(self):
        return self._column_count

    @property
    def shape(self):
        return (self.row_count, self.column_count)

    @property
    def size(self):
        return self.row_count * self.column_count

    def get_row(self, row):
        return self.data[row]

    def get_column(self, column):
        return self.data[:, column]

    def __str__(self):
        return ("\n").join("".join(line) for line in self.data)

    def __eq__(self, other):
        return np.array_equal(self.data, other.data)
