class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        total_sum = 0

        for s in salary:
            total_sum += s

        return (total_sum - min_salary - max_salary) / (len(salary) - 2)
