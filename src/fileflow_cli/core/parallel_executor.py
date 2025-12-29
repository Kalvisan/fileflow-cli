"""Parallel processing executor for FileFlowCLI."""

import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Callable, Any, Optional, Iterator, Dict
from queue import Queue


class ParallelExecutor:
    """Dynamic parallel processing system for FileFlowCLI."""
    
    def __init__(self, max_workers: int = 4):
        """
        Initialize parallel executor.
        
        Args:
            max_workers: Maximum number of worker threads (default: 4)
        """
        self.max_workers = max_workers
        self._lock = threading.Lock()
        self._progress = {"completed": 0, "total": 0, "errors": 0}
    
    def execute_parallel(
        self,
        tasks: List[Callable],
        callback: Optional[Callable[[int, Any], None]] = None,
        error_handler: Optional[Callable[[Exception, int], None]] = None
    ) -> List[Any]:
        """
        Execute tasks in parallel.
        
        Args:
            tasks: List of callable tasks to execute
            callback: Optional callback function(completed_count, result)
            error_handler: Optional error handler function(exception, task_index)
        
        Returns:
            List of results in order of task submission
        """
        self._progress = {"completed": 0, "total": len(tasks), "errors": 0}
        results = [None] * len(tasks)
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            future_to_index = {
                executor.submit(task): idx
                for idx, task in enumerate(tasks)
            }
            
            # Process completed tasks
            for future in as_completed(future_to_index):
                idx = future_to_index[future]
                try:
                    result = future.result()
                    results[idx] = result
                    
                    with self._lock:
                        self._progress["completed"] += 1
                    
                    if callback:
                        callback(self._progress["completed"], result)
                
                except Exception as e:
                    with self._lock:
                        self._progress["errors"] += 1
                    
                    if error_handler:
                        error_handler(e, idx)
                    else:
                        print(f"Error in task {idx}: {e}")
        
        return results
    
    def execute_batch_parallel(
        self,
        batches: List[List[Callable]],
        callback: Optional[Callable[[int, int, Dict], None]] = None,
        error_handler: Optional[Callable[[Exception, int, int], None]] = None
    ) -> Iterator[Dict[str, Any]]:
        """
        Execute batches of tasks in parallel.
        
        Args:
            batches: List of batches, each containing callable tasks
            callback: Optional callback function(batch_num, completed_in_batch, batch_results)
            error_handler: Optional error handler function(exception, batch_num, task_index)
        
        Yields:
            Dictionary with batch progress information
        """
        total_batches = len(batches)
        
        for batch_num, batch in enumerate(batches, 1):
            batch_results = self.execute_parallel(
                batch,
                callback=lambda completed, result: None,  # Batch-level callback handled separately
                error_handler=lambda e, idx: error_handler(e, batch_num, idx) if error_handler else None
            )
            
            progress_info = {
                "batch_num": batch_num,
                "total_batches": total_batches,
                "batch_size": len(batch),
                "completed": batch_num,
                "results": batch_results,
                "progress": self._progress.copy()
            }
            
            if callback:
                callback(batch_num, len(batch_results), progress_info)
            
            yield progress_info
    
    def get_progress(self) -> Dict[str, int]:
        """
        Get current progress information (thread-safe).
        
        Returns:
            Dictionary with progress stats
        """
        with self._lock:
            return self._progress.copy()
    
    def reset_progress(self) -> None:
        """Reset progress counters."""
        with self._lock:
            self._progress = {"completed": 0, "total": 0, "errors": 0}

