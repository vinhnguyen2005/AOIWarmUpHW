    arr_copy = self.arr.copy()  
        n = len(arr_copy)
        swap_count = 0
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr_copy[j] > arr_copy[j + 1]:
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                    swap_count += 1
                    swapped = True
            if not swapped:
                break
        return swap_count