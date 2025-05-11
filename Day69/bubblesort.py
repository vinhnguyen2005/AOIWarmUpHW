class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self, ascending=True):
        arr = self.arr.copy()
        check_already_sorted = True
        for i in range(len(arr) - 1):
            if (ascending and arr[i] > arr[i + 1]) or (not ascending and arr[i] < arr[i + 1]):
                check_already_sorted = False
                break
        if check_already_sorted:
            return arr
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    def count_swaps(self):
        arr = self.arr.copy()
        n = len(arr)
        swap_count = 0
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swap_count += 1
                    swapped = True
            if not swapped:
                break
        return swap_count

    @staticmethod
    def test_bubble_sort():
        assert BubbleSort([64, 34, 25, 12, 22, 11, 90]).sort() == [11, 12, 22, 25, 34, 64, 90]
        assert BubbleSort([5, 1, 4, 2, 8]).sort() == [1, 2, 4, 5, 8]
        assert BubbleSort([3]).sort() == [3]
        assert BubbleSort([]).sort() == []
        print("All tests in test_bubble_sort passed!")

    @staticmethod
    def test_descending_bubble_sort():
        assert BubbleSort([64, 34, 25, 12, 22, 11, 90]).sort(ascending=False) == [90, 64, 34, 25, 22, 12, 11]
        assert BubbleSort([5, 1, 4, 2, 8]).sort(ascending=False) == [8, 5, 4, 2, 1]
        assert BubbleSort([3]).sort(ascending=False) == [3]
        assert BubbleSort([]).sort(ascending=False) == []
        print("All tests in test_descending_bubble_sort passed!")

    @staticmethod
    def test_count_swaps():
        assert BubbleSort([5, 1, 4, 2, 8]).count_swaps() == 4
        assert BubbleSort([3]).count_swaps() == 0
        assert BubbleSort([]).count_swaps() == 0
        print("All tests in test_count_swaps passed!")

def main():
    BubbleSort.test_bubble_sort()
    BubbleSort.test_descending_bubble_sort()
    BubbleSort.test_count_swaps()

if __name__ == "__main__":
    main()
