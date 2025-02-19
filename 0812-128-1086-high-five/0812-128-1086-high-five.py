class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        '''
        st1: [90,80,85,70,100,60,75]
        st2: [85,92,88,79,95]
        
        list_combined: [[1,90], [1,90], [1,85]..., [2,85], [2,92]...]
        
        
        sorted scores std 1: [100, 90, 85, 80, 75, 70, 60] top5/5 == ans
        sorted scores std 2: [95, 92, 88, 85, 79] top5/5 == ans
        
        final output: [[1, average top5], [2, average top5]]
        
        TC: o(nlogn)
        
        using heap: tc: inserting o(log5) == o(1) per score
        TC: o(nlog(5)) = o(n)
        SC: o(n)
        '''
        
        """
        Calculate the top 5 average for each student.

        :param items: List of [student_id, score]
        :return: List of [student_id, top_5_average]
        """
        # Dictionary to store student scores using min-heaps
        student_scores = defaultdict(list)

        # Step 1: Process each (id, score) pair
        for student_id, score in items:
            heapq.heappush(student_scores[student_id], score)  # Insert score in min-heap

            # Keep only the top 5 scores
            if len(student_scores[student_id]) > 5:
                heapq.heappop(student_scores[student_id])  # Remove the lowest score

        # Step 2: Compute averages
        result = []
        for student_id in sorted(student_scores.keys()):  # Sort students by ID
            top_five = student_scores[student_id]
            avg = sum(top_five) // len(top_five)  # Compute integer division of the average
            result.append([student_id, avg])

        return result
        