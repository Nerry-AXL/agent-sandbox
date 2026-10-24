#!/usr/bin/env python3
# Simple test script to run inside sandbox
# Used to verify basic execution works

import sys
import os
import platform

print("=" * 50)
print("Sandbox Test Script")
print("=" * 50)
print()

print("Environment:")
print(f"  Python: {platform.python_version()}")
print(f"  Platform: {platform.platform()}")
print(f"  Machine: {platform.machine()}")
print(f"  Processor: {platform.processor()}")
print()

print("Process Info:")
print(f"  PID: {os.getpid()}")
print(f"  UID: {os.getuid()}")
print(f"  GID: {os.getgid()}")
print()

print("Test Execution:")
print("  Status: SUCCESS")
print("  Message: Hello from inside the sandbox!")
print()

print("=" * 50)
print("Test completed successfully")
print("=" * 50)

sys.exit(0)
