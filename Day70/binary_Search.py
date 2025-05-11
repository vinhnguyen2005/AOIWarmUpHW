class BinarySearch:
    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def first_occurrence(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                if mid == 0 or arr[left] != target:
                    return mid
                right = mid - 1
                
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def smallest_greater_than_x(self, arr, x):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] >= x:
                right = mid - 1
            else:
                left = mid + 1
        return left if left < len(arr) else -1
    
    def count_recursive(self, arr, target, left, right):
        if left > right:
            return 0
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return 1 + self.count_recursive(arr, target, left, mid - 1) + self.count_recursive(arr, target, mid + 1, right)
        elif arr[mid] < target:
            return self.count_recursive(arr, target, mid + 1, right)
        else:
            return self.count_recursive(arr, target, left, mid - 1)
        
    def test(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 9
        print("Binary Search:", self.binary_search(arr, target))
        print("First Occurrence:", self.first_occurrence(arr, target))
        print("Smallest Greater Than X:", self.smallest_greater_than_x(arr, target))
        print("Count Recursive:", self.count_recursive(arr, target, 0, len(arr) - 1))
        
if __name__ == "__main__":
    bs = BinarySearch()
    bs.test()
    
    