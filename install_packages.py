#!/usr/bin/env python3
"""
Alternative installation script - Use if batch file fails
Run: python install_packages.py
"""

import subprocess
import sys
import time

def install_package(package_name, package_version):
    """Install a single package with retries"""
    full_package = f"{package_name}=={package_version}"
    max_retries = 3
    
    # Special handling for Pillow to avoid build failures
    extra_args = ["--only-binary", ":all:"] if package_name == "Pillow" else []
    
    for attempt in range(1, max_retries + 1):
        try:
            print(f"\n{'='*60}")
            print(f"Installing: {full_package}")
            print(f"Attempt: {attempt}/{max_retries}")
            print(f"{'='*60}\n")
            
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", full_package,
                 "--default-timeout=1000", "--retries=5"] + extra_args,
                check=True,
                timeout=600  # 10 minutes timeout
            )
            
            print(f"\n✓ {full_package} installed successfully!\n")
            return True
            
        except subprocess.TimeoutExpired:
            print(f"\n✗ Installation timed out (attempt {attempt}/{max_retries})")
            if attempt < max_retries:
                print(f"Waiting 10 seconds before retry...\n")
                time.sleep(10)
            else:
                print(f"Failed to install {full_package} after {max_retries} attempts\n")
                return False
                
        except subprocess.CalledProcessError as e:
            print(f"\n✗ Installation failed with error code {e.returncode}")
            if attempt < max_retries:
                print(f"Waiting 10 seconds before retry...\n")
                time.sleep(10)
            else:
                print(f"Failed to install {full_package} after {max_retries} attempts\n")
                return False
        except Exception as e:
            print(f"\n✗ Error: {e}")
            if attempt < max_retries:
                print(f"Waiting 10 seconds before retry...\n")
                time.sleep(10)
            else:
                return False

def main():
    print("\n")
    print("="*60)
    print("  REMOTE ACCESS APP - PACKAGE INSTALLER")
    print("="*60)
    print("\nThis will install required Python packages...\n")
    
    # Check Python version
    print(f"Python version: {sys.version}\n")
    
    # Upgrade pip
    print("Upgrading pip...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip",
             "--default-timeout=1000", "--retries=5"],
            check=True,
            timeout=300
        )
        print("✓ Pip upgraded\n")
    except:
        print("⚠ Could not upgrade pip, continuing...\n")
    
    # Packages to install
    packages = [
        ("flask", "2.3.3"),
        ("flask-cors", "4.0.0"),
        ("Pillow", "12.0.0"),
        ("pynput", "1.7.6"),
    ]
    
    failed_packages = []
    
    for package_name, version in packages:
        if not install_package(package_name, version):
            failed_packages.append(f"{package_name}=={version}")
    
    # Summary
    print("\n" + "="*60)
    print("  INSTALLATION SUMMARY")
    print("="*60 + "\n")
    
    if not failed_packages:
        print("✓ All packages installed successfully!\n")
        print("You can now run: python server.py\n")
        return True
    else:
        print(f"⚠ {len(failed_packages)} package(s) failed to install:\n")
        for pkg in failed_packages:
            print(f"  - {pkg}")
        print("\nTroubleshooting:")
        print("1. Check your internet connection")
        print("2. Try using an alternative PyPI mirror:")
        print("   pip install -i https://mirrors.aliyun.com/pypi/simple/ flask==2.3.3")
        print("3. Disable your VPN if using one")
        print("4. Try updating pip: python -m pip install --upgrade pip\n")
        return False

if __name__ == "__main__":
    success = main()
    input("Press Enter to exit...")
    sys.exit(0 if success else 1)
