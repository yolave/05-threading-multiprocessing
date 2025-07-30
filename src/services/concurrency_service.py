import time
import math


class ConcurrencyService:
    # Simulate an I/O-bound task (e.g., API call, DB query)
    @classmethod
    def io_bound_task(cls, delay: float = 1):
        time.sleep(delay)
        return f"IO-bound task completed after {delay} sec"

    # Simulate a CPU-bound task (e.g., heavy computation)
    @classmethod
    def cpu_bound_task(cls, n: int = 10_000_000):
        total = 0
        for i in range(n):
            total += math.sqrt(i)
        return f"CPU-bound task completed with sum {total:.2f}"


concurrency_service = ConcurrencyService()


def get_concurrency_service() -> ConcurrencyService:
    return concurrency_service
