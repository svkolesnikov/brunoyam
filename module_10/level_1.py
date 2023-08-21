import unittest


def merge_sort(a):
    if (len(a) < 2):
        return a[:]
    else:
        median = int(len(a) / 2)
        left = merge_sort(a[:median])
        right = merge_sort(a[median:])
        return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1
    return res


class TestSort(unittest.TestCase):
    def test_sort(self):
        ar = [1, 5, 2, 76, 3, 0, 1, 4, 6, -1]
        ar_ms = merge_sort(ar)
        ar_test = sorted(ar)

        j = 0
        for i in range(len(ar)):
            if ar_test[i] == ar_ms[i]:
                j += 1

        self.assertEqual(j, len(ar))

if __name__ == '__main__':
    unittest.main()
