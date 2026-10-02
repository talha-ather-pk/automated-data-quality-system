import subprocess
import sys
import time
import os

start_time = time.time()

os.makedirs(
    "logs",
    exist_ok=True
)

print(sys.executable)

print("================================")
print("DATA QUALITY PIPELINE STARTED")
print("================================")

print("\nRunning Profiling Module...")
subprocess.run(
    [sys.executable, "src/profiling/profiler.py"]
)

print("\nRunning Cleaning Module...")
subprocess.run(
    [sys.executable, "src/cleaning/cleaner.py"]
)

print("\nRunning Validation Module...")
subprocess.run(
    [sys.executable, "src/validation/validator.py"]
)

print("\n================================")
print("PIPELINE COMPLETED")
print("================================")

end_time = time.time()

execution_time = round(
    end_time - start_time,
    2
)

print(
    f"\nExecution Time: {execution_time} seconds"
)

with open(
    "logs/pipeline.log",
    "a"
) as file:

    file.write(
        f"Pipeline executed in "
        f"{execution_time} seconds\n"
    )
