class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a maxHeap
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)  # No need for reverse argument

        while len(maxHeap) > 1:
            # Get the two largest stones
            largest1 = heapq.heappop(maxHeap)
            largest2 = heapq.heappop(maxHeap)

            # If they are the same, discard both. Otherwise, put the difference back.
            if largest1 != largest2:
                heapq.heappush(maxHeap, largest1 - largest2)

        # Check if there's any stone left (heap is empty)
        return abs(maxHeap[0]) if maxHeap else 0
        