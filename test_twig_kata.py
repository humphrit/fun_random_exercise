"""
Created 2019-04-15
@author: Tom Humphries
"""

import twig_kata as twig


def test_group_array_elements():
    """
    Tests twig_kata.group_array_elements function
    Returns
    -------
    None
    """

    assert twig.group_array_elements([1, 2, 3, 4, 5], 3) == \
        [[1, 2], [3, 4], [5]]
    assert twig.group_array_elements([[1, 2], [3, 4], [5, 6], [7, 8]], 2) == \
        [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    assert twig.group_array_elements([1, 2, 3, 4, 5, 6], 10) == \
        [1, 2, 3, 4, 5, 6]
    assert twig.group_array_elements([1, 2, 3, 4, 5], 1) == [[1, 2, 3, 4, 5]]
    assert twig.group_array_elements([1, 2, 3, 4], 3) == [[1, 2], [3], [4]]
    assert twig.group_array_elements([1, 2, 3], 3) == [[1], [2], [3]]
    assert twig.group_array_elements([1], 1) == [1]
    assert twig.group_array_elements([1, 2], 2) == [[1], [2]]
