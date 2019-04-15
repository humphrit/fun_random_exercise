"""
Created 2019-04-15
@author: Thomas Humphries
"""


def group_array_elements(array, number_of_groups):
    """
    Splits the contents of the passed array into
    a number of equally sized arrays.

    >>> group_array_elements([[1, 2], [3, 4], [5, 6], [7, 8]], 2)
    [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

    When the array cannot be divided exactly into the number
    specified, the final part has a length equal to the remainder.

    >>> group_array_elements([1, 2, 3, 4, 5], 3)
    [[1, 2], [3, 4], [5]]

    When the length of the array is one more than the number of groups required
    the first element in the new array is longer than the others.

    >>> group_array_elements([1, 2, 3, 4, 5], 4)
    [[1, 2], [3], [4], [5]]

    Parameters
    ----------
    array : list
        an array of length >= 0
    number_of_groups : int
        a positive integer - the number of groups required

    Returns
    -------
    list
        an array divided into the requested number of groups
    """

    if number_of_groups > len(array) or len(array) == 1:
        divided_array = array
    elif number_of_groups == len(array) - 1:
        divided_array = [array[:2]] + [[x] for x in array[2:]]
    else:
        group_sizes = int((len(array)/number_of_groups)+0.5)
        divided_array = [array[group_sizes*i: group_sizes*i+group_sizes]
                         for i in range(number_of_groups)]
    return divided_array
