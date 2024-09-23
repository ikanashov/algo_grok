from typing import List


# Time Limit Exceeded
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        from functools import reduce

        def int_xor(first: int, second: int):
            return first ^ second

        result = []
        result_cache = {}
        for query in queries:
            left, right = query[0], query[1] + 1
            from_cache_left = result_cache.get(left, {})
            from_cache = from_cache_left.get(right, None)
            if from_cache:
                result.append(from_cache)
            elif from_cache_left and result_cache[left].get("last") < right:
                last_right = result_cache[left].get("last")
                last_xor = result_cache[left][last_right]
                query_result = reduce(int_xor, [last_xor] + arr[last_right:right])
                result.append(query_result)
                result_cache[left][right] = query_result
                result_cache[left]["last"] = right
            else:
                query_result = reduce(int_xor, arr[left:right])
                result.append(query_result)
                if not result_cache.get(left, None):
                    result_cache[left] = {right: query_result}
                    result_cache[left]["last"] = right
                else:
                    result_cache[left][right] = query_result
                    if result_cache[left]["last"] < right:
                        result_cache[left]["last"] = right
        return result


from xor_test import queries


q = queries
arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
expected = [2, 7, 14, 8]

sol = Solution()

assert expected == sol.xorQueries(arr=arr, queries=queries)
