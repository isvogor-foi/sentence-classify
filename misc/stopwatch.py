import time
from functools import wraps


def stopwatch(trace_name):
    def time_profiler(method):
        @wraps(method)
        def time_profile(*args, **kw):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()
            if "log_time" in kw:
                name = kw.get("log_name", method.__name__.upper())
                kw["log_time"][name] = int((te - ts) * 1000)
            else:
                print(f"({trace_name}) {method.__name__} id ({id(method)}) {(te - ts) * 1000} ms")
            return result

        return time_profile

    return time_profiler
