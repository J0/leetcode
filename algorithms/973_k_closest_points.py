class Solution:
    def euclidean_distance(self, x, y):
        return x ** 2 + y ** 2

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        output = []
        for point in points:
            distance = self.euclidean_distance(point[0], point[1])
            distance_with_point = (distance, point)
            heapq.heappush(heap, distance_with_point)
        for res in range(K):
            point = heapq.heappop(heap)[1]
            output.append(point)
        return output
