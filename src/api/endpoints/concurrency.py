import asyncio
import multiprocessing
import threading
import time

from fastapi import APIRouter
from fastapi.params import Depends

from ...services.concurrency_service import ConcurrencyService, get_concurrency_service

router = APIRouter()


# Run a CPU-bound task in a separate process
def run_cpu_task(results_queue, service: ConcurrencyService):
    result = service.cpu_bound_task()
    results_queue.put(result)


# ----- Synchronous (Baseline) -----
@router.get("/sync-io")
def sync_io(service: ConcurrencyService = Depends(get_concurrency_service)):
    start = time.time()
    results = [service.io_bound_task(1) for _ in range(3)]
    end = time.time()
    return {"results": results, "time_taken": end - start}


@router.get("/sync-cpu")
def sync_cpu(service: ConcurrencyService = Depends(get_concurrency_service)):
    start = time.time()
    results = [service.cpu_bound_task() for _ in range(3)]
    end = time.time()
    return {"results": results, "time_taken": end - start}


# ----- Threading (I/O-bound) -----
@router.get("/threaded-io")
def threaded_io(service: ConcurrencyService = Depends(get_concurrency_service)):
    start = time.time()
    threads = []
    results = []
    for _ in range(3):
        thread = threading.Thread(target=lambda: results.append(service.io_bound_task(1)))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end = time.time()
    return {"results": results, "time_taken": end - start}


# ----- Multiprocessing (CPU-bound) -----
@router.get("/multiprocess-cpu")
def multiprocess_cpu(service: ConcurrencyService = Depends(get_concurrency_service)):
    start = time.time()
    processes = []
    results_queue = multiprocessing.Queue()

    for _ in range(3):
        process = multiprocessing.Process(
            target=run_cpu_task,  # Use standalone function
            args=(results_queue, service)
        )
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    results_list = []
    while not results_queue.empty():
        results_list.append(results_queue.get())

    end = time.time()
    return {"results": results_list, "time_taken": end - start}


# ----- Coroutines (asyncio, I/O-bound) -----
@router.get("/async-io")
async def async_io():
    start = time.time()

    async def run_io_task():
        await asyncio.sleep(1)  # Simulate async I/O
        return f"Async IO-bound task completed after 1 sec"

    tasks = [run_io_task() for _ in range(3)]
    results = await asyncio.gather(*tasks)
    end = time.time()
    return {"results": results, "time_taken": end - start}
