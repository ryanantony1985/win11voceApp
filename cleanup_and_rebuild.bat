@echo off
cd /d "%~dp0"

echo Cleaning up build artifacts...

if exist build (
    echo Removing build directory...
    rmdir /s /q build
)

if exist dist (
    echo Removing dist directory...
    rmdir /s /q dist
)

if exist package_layout (
    echo Removing package_layout directory...
    rmdir /s /q package_layout
)

if exist *.msix (
    echo Removing MSIX packages...
    del /q *.msix
)

echo Cleanup complete.

echo Starting rebuild...
call build_app.bat
