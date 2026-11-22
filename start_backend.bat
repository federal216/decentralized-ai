@echo off
title DecentralizedAI ($DEAI) - Mesh Telemetry Backend
color 0B
cls

echo ===============================================================================
echo       DECENTRALIZED AI ($DEAI) - CENTRAL MESH TELEMETRY BACKEND
echo            FastAPI Server with Live Solana Devnet RPC Gateway
echo ===============================================================================
echo.
echo [*] Launching API Server on http://localhost:8000
echo [*] Interactive Swagger Docs: http://localhost:8000/docs
echo [*] Telemetry Endpoint:       http://localhost:8000/api/telemetry
echo.

python backend\server.py

pause
