import subprocess
import sys

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