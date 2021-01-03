import matplotlib.pyplot as plt

# Set style to use for plots
import numpy

plt.style.use('ggplot')


class Charts:
    def __init__(self, data, title, xl, yl):
        self.data = data
        self.title = title
        self.xl = xl
        self.yl = yl

    def _set_details(self):
        """
        A private function to set details of the plot.
        """
        plt.xlabel(xlabel=self.xl)
        plt.ylabel(ylabel=self.yl)
        plt.title(label=self.title)

    def plot_histogram(self):
        """
        Plots a histogram with data, title, x-axis and y-axis label as parameters
        """
        keys = self.data.keys()
        values = self.data.values()
        self._set_details()
        try:
            plt.bar(keys, values)
            plt.show()
        except numpy.core._exceptions.UFuncTypeError:
            print("Bad dictionary")
            return None

