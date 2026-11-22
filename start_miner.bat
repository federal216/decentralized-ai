@echo off
title DecentralizedAI ($DEAI) - GPU Worker Node
color 0A
cls

echo ===============================================================================
echo       DECENTRALIZED AI ($DEAI) - EDGE GPU WORKER NODE LAUNCHER
echo          Sovereign DePIN Neural Compute Mesh on Solana Devnet
echo ===============================================================================
echo.

:: Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Python is not installed or not added to PATH.
    echo Please install Python 3.10+ from https://www.python.org/downloads/
    pause
    exit /b
)

:: Prompt Wallet Address
echo [INFO] Enter your Solana Wallet Address to receive $DEAI mining rewards.
set /p WALLET="Solana Wallet (or press Enter for demo wallet): "

if "%WALLET%"=="" (
    set WALLET=44tR4526AbfPED9Zrc7oT2hM5W4ARqTWmHMAAJmAhvb7
)

echo.
echo [*] Starting Worker Node with Wallet: %WALLET%
echo [*] Connecting to Solana Devnet RPC...
echo [*] Press Ctrl+C at any time to pause mining.
echo.

python scripts\worker_node.py --wallet %WALLET% --network devnet

pause
