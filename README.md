# SmolVLA + LIBERO (MuJoCo + Robosuite) Pipenv Template

A complete setup for running SmolVLA (Vision-Language-Action model) in simulation using LIBERO benchmarks on MuJoCo physics engine, optimized for Apple Silicon M3 Macs. This template repository bootstraps a ready-to-use `pipenv` environment for running **SmolVLA** with the **LIBERO** benchmark stack, including:

- **SmolVLA**: 450M parameter vision-language-action model for robotics
- **LIBERO**: Benchmark suite of 130 language-conditioned robot manipulation tasks
- **MuJoCo**: Physics engine for robotics simulation
- **PyTorch with MPS**: GPU acceleration via Metal Performance Shaders
- **Robosuite 1.4.1**: Robot simulation framework (correct version for LIBERO)
- All dependencies managed with **Pipenv** for reproducible builds


The goal of this template is to eliminate environment setup friction and provide a personal reproducible starting point for my research and experimentation.

## 🚀 Quick Start (5 Minutes)

### Prerequisites

Before you begin, make sure you have:

1. **macOS 12.3 or later** (for MPS support)
2. **Homebrew** installed ([install here](https://brew.sh))
3. **Python 3.10** (ARM64 native)
4. **Pipenv** for dependency management

### Step 1: Install System Requirements

```bash
# Install Python 3.10 (ARM64 native)
brew install python@3.10

# Verify it's ARM64 (should show "arm64", NOT "x86_64")
python3.10 -c "import platform; print(f'Architecture: {platform.machine()}')"

# Install Pipenv
pip3 install --user pipenv

# Install system dependencies for MuJoCo
brew install glfw cmake
```

### Step 2: Clone This Repository

```bash
git clone https://github.com/Artifex2002/Template_Mac-VLA.git
cd Template_Mac-VLA  # or whatever you wanna rename your repo to
```

### Step 3: Install All Dependencies

```bash
# This single command creates a new pipenv virtual env & installs everything!
pipenv install

# This reads Pipfile.lock and installs:
# - PyTorch with MPS support
# - LIBERO (with our structural fix)
# - MuJoCo, Robosuite, and all dependencies
# - Exact same versions as the original setup
```

### Step 4: Verify Installation

```bash
# Run the verification script
pipenv run python verify_installation_m3.py
```

You should see all green checkmarks:
```
✓ PyTorch
✓ MuJoCo
✓ Robosuite
✓ LIBERO
✓ MPS (Metal) available: True
✓ Running native ARM64 Python
```

### Step 5: First-Time Setup

On first use, LIBERO will ask about dataset location:

```bash
pipenv run python -c "import libero; print('Setup complete!')"
```

When prompted: **Press 'N'** to use the default dataset location.

That's it! 🎉

## 📚 Template Structure

```
Template_Mac-VLA/
├── LIBERO/                    # LIBERO benchmark suite (with fixes)
│   └── libero/
│       ├── __init__.py       # Custom fix for nested structure
│       ├── libero/           # Actual LIBERO code
│       ├── lifelong/         # Lifelong learning algorithms
│       └── configs/          # Configuration files
├── Pipfile                    # Dependency specifications
├── Pipfile.lock              # Locked dependency versions (IMPORTANT!)
├── verify_installation_m3.py  # Verification script
└── README.md                  # This file
```

## ⚠️ Important Notes

### Why Robosuite 1.4.1?

**Critical**: This project uses Robosuite **1.4.1** specifically. 

- ✅ Robosuite 1.4.1 - Compatible with LIBERO
- ❌ Robosuite 1.5.0+ - Breaks LIBERO (SingleArmEnv was removed)

The Pipfile.lock ensures you get the correct version.

### Why the LIBERO __init__.py Fix?

The LIBERO repository has a nested structure that prevents direct import. We've added a custom `LIBERO/libero/__init__.py` file that fixes this issue. This file is included in the repo, so you don't need to do anything!

🎉 **Happy coding!**
