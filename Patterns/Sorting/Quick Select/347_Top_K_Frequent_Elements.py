class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right) -> int:
            pivot_frequency = count[unique[right]]

            # move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] <= pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        left, right = 0, len(unique) - 1
        k_less = len(unique) - k
        while True:
            # find the pivot position in a sorted list
            pivot_index = partition(left, right)

            # if the pivot is in its final sorted position
            if pivot_index == k_less:
                return unique[-k:]
            # go right
            elif pivot_index < k_less:
                left = pivot_index + 1
            # go left
            else:
                right = pivot_index - 1
