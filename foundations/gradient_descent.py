class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = float(init)
        for _ in range(iterations):
            x = x - learning_rate * (2 * x)
        
        result = round(x, 5)
        if iterations == 0:
            return int(result)   # 5 → 5
        return float(result)     # 0.0 → 0.0, 4.08536 → 4.08536
