"""
Verification script for SmolVLA + LIBERO + MuJoCo on Mac M3
This checks all critical components are installed and working
"""
import sys

def check_import(module_name, display_name=None):
    display_name = display_name or module_name
    try:
        __import__(module_name)
        print(f"✓ {display_name}")
        return True
    except ImportError as e:
        print(f"✗ {display_name}: {e}")
        return False

print("=" * 60)
print("Checking installations for Mac M3...")
print("=" * 60)

# Core packages
check_import("torch", "PyTorch")
check_import("torchvision")
check_import("transformers", "Hugging Face Transformers")
check_import("accelerate")
check_import("mujoco", "MuJoCo")
check_import("robosuite", "Robosuite")
check_import("libero", "LIBERO")
check_import("gymnasium")
check_import("cv2", "OpenCV")
check_import("PIL", "Pillow")
check_import("numpy")
check_import("h5py")

print("=" * 60)

# Check PyTorch MPS (not CUDA!)
import torch
print(f"\nPyTorch version: {torch.__version__}")
print(f"MPS (Metal) available: {torch.backends.mps.is_available()}")
print(f"MPS built: {torch.backends.mps.is_built()}")

if torch.backends.mps.is_available():
    print("✓ GPU acceleration via Metal Performance Shaders is ready!")
    # Test MPS with a simple operation
    try:
        x = torch.ones(1, device="mps")
        y = x * 2
        print(f"✓ MPS device test successful: {y}")
    except Exception as e:
        print(f"✗ MPS device test failed: {e}")
else:
    print("✗ MPS not available - will use CPU only")
    print("   Check that you have:")
    print("   - macOS 12.3 or later")
    print("   - PyTorch 2.0 or later")
    print("   - ARM64 Python (not x86_64)")

# Check architecture
import platform
print(f"\nArchitecture: {platform.machine()}")
if platform.machine() == "arm64":
    print("✓ Running native ARM64 Python")
else:
    print("✗ Running x86_64 (Rosetta) - performance will be degraded")
    print("   Reinstall Python using: brew install python@3.10")

# Check Robosuite version (critical!)
try:
    import robosuite
    version = robosuite.__version__
    print(f"\nRobosuite version: {version}")
    if version.startswith("1.4"):
        print("✓ Robosuite 1.4.x - correct version for LIBERO!")
    else:
        print("✗ Robosuite version may not be compatible with LIBERO")
        print("   Recommended: pipenv install robosuite==1.4.1")
except Exception as e:
    print(f"✗ Could not determine Robosuite version: {e}")

# Check NumPy version
import numpy as np
print(f"\nNumPy version: {np.__version__}")
major, minor = map(int, np.__version__.split('.')[:2])
if major == 1 and 21 <= minor < 24:
    print("✓ NumPy version is compatible")
else:
    print("✗ NumPy version may cause issues")
    print("   Recommended: pipenv install 'numpy>=1.21.0,<1.24.0'")

print("=" * 60)
print("\n✓ Setup verification complete!")
print("\nNext steps:")
print("1. Test MuJoCo: Load a basic simulation")
print("2. Test LIBERO: Load a task environment")
print("3. Test SmolVLA: Load model from HuggingFace")
print("=" * 60)