class LinearSearch:
    @staticmethod
    def linear_search(arr, target):
        for index, value in enumerate(arr):
            if value == target:
                return index
        return -1

    @staticmethod
    def linear_search_with_res_arr(arr, target):
        result = []
        for index, value in enumerate(arr):
            if value == target:
                result.append(index)
        return result
    
    @staticmethod
    def find_greater(arr, x):
        result = []
        for index, value in enumerate(arr):
            if value > x:
                result.append(index)
        return result
    
    @staticmethod
    def find_all_div_by_3(arr):
        result = []
        for index, value in enumerate(arr):
            if value % 3 == 0:
                result.append(index)
        return result
    
    @staticmethod
    def test_linear_search():
        assert LinearSearch.linear_search([1, 2, 3, 4, 5], 3) == 2
        assert LinearSearch.linear_search([1, 2, 3, 4, 5], 6) == -1
        assert LinearSearch.linear_search([], 1) == -1
        assert LinearSearch.linear_search([1], 1) == 0
        assert LinearSearch.linear_search([1], 2) == -1
        print("All tests in test_linear_search passed!")

    @staticmethod
    def test_linear_search_with_res_arr():
        assert LinearSearch.linear_search_with_res_arr([1, 2, 3, 4, 5], 3) == [2]
        assert LinearSearch.linear_search_with_res_arr([1, 2, 3, 4, 3, 5], 3) == [2, 4]
        assert LinearSearch.linear_search_with_res_arr([], 1) == []
        assert LinearSearch.linear_search_with_res_arr([1], 1) == [0]
        assert LinearSearch.linear_search_with_res_arr([1], 2) == []
        print("All tests in test_linear_search_with_res_arr passed!")

    @staticmethod
    def test_find_greater():
        assert LinearSearch.find_greater([1, 2, 3, 4, 5], 3) == [3, 4]
        assert LinearSearch.find_greater([1, 2, 3, 4, 5], 5) == []
        assert LinearSearch.find_greater([], 1) == []
        assert LinearSearch.find_greater([1], 0) == [0]
        print("All tests in test_find_greater passed!")

    @staticmethod
    def test_find_all_div_by_3():
        assert LinearSearch.find_all_div_by_3([1, 2, 3, 4, 5, 6]) == [2, 5]
        assert LinearSearch.find_all_div_by_3([1, 2, 4, 5]) == []
        assert LinearSearch.find_all_div_by_3([]) == []
        assert LinearSearch.find_all_div_by_3([3]) == [0]
        print("All tests in test_find_all_div_by_3 passed!")


def main():
    LinearSearch.test_linear_search()
    LinearSearch.test_linear_search_with_res_arr()
    LinearSearch.test_find_greater()
    LinearSearch.test_find_all_div_by_3()


if __name__ == "__main__":
    main()
