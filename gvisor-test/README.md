# gVisor Feasibility Test

## Goal
Confirm where gVisor can run for development and testing of the sandbox.

## What we're testing
- Can gVisor run on local Windows machine (via WSL2 + Docker Desktop)
- Can gVisor run in GitHub Actions CI
- Can gVisor run in free cloud notebook environments (Kaggle, Colab)
- Installation and configuration steps
- Basic execution test

## Success criteria
- Identify at least one free environment where gVisor works
- Document installation steps
- Verify basic container execution with gVisor runtime
- Measure startup overhead vs standard runc

## Test environments

### Option 1: Local (WSL2 + Docker Desktop)
- **Pros**: Full control, fast iteration
- **Cons**: Requires Windows with WSL2
- **Status**: VERIFY

### Option 2: GitHub Actions
- **Pros**: Free CI, reproducible
- **Cons**: Limited runtime (6 hours max)
- **Status**: VERIFY

### Option 3: Kaggle Notebooks
- **Pros**: Free GPU environment
- **Cons**: May not allow gVisor installation
- **Status**: VERIFY - likely blocked

### Option 4: Google Colab
- **Pros**: Free environment
- **Cons**: May not allow gVisor installation
- **Status**: VERIFY - likely blocked

## Expected result

Based on documentation research:
- **Local (WSL2)**: Should work - Docker Desktop supports gVisor via `runsc`
- **GitHub Actions**: Should work - Ubuntu runners can install gVisor
- **Kaggle/Colab**: Likely blocked - restricted container runtime access

## Files
- `test-gvisor.sh` - Installation and test script
- `test-container.py` - Simple Python script to run in sandbox
- `results.txt` - Test output
