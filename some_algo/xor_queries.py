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
            else:
                query_result = reduce(int_xor, arr[left:right])
                result.append(query_result)
                result_cache[left] = {right: query_result}
        return result
