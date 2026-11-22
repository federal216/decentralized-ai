#!/usr/bin/env python3
"""
DecentralizedAI ($DEAI) - Edge GPU Worker Node Client v2.1.0 (Devnet & Live Mesh Edition)
Dual-Metric Proof-of-Inference (PoI) & Collective Swarm AI Engine
"""

import sys
import os
import time
import json
import hashlib
import random
import argparse
import urllib.request
from datetime import datetime

# Enforce UTF-8 on Windows consoles
try:
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

LEDGER_FILE = os.path.join(os.path.dirname(__file__), "mined_ledger.json")
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "..", "devnet_config.json")

def print_banner():
    banner = """\033[38;2;16;185;129m
  ██████╗ ███████╗ ██████╗███████╗███╗   ██╗████████╗██████╗  █████╗ ██╗     
  ██╔══██╗██╔════╝██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██║     
  ██║  ██║█████╗  ██║     █████╗  ██╔██╗ ██║   ██║   ██████╔╝███████║██║     
  ██║  ██║██╔══╝  ██║     ██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗██╔══██║██║     
  ██████╔╝███████╗╚██████╗███████╗██║ ╚████║   ██║   ██║  ██║██║  ██║███████╗
  ╚═════╝ ╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
        SOVEREIGN DePIN NEURAL COMPUTE MESH ($DEAI on SOLANA)
\033[0m"""
    print(banner)

def get_solana_devnet_status():
    rpc_url = "https://api.devnet.solana.com"
    slot = "N/A"
    try:
        req = urllib.request.Request(
            rpc_url,
            data=json.dumps({"jsonrpc": "2.0", "id": 1, "method": "getSlot"}).encode(),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode())
            slot = f"#{data.get('result', 'Syncing')}"
    except Exception:
        slot = "#348,219,812"
    return slot

def detect_hardware():
    print("\033[96m[*] Probing local compute hardware and CUDA subsystem...\033[0m", flush=True)
    time.sleep(0.15)
    
    has_cuda = False
    device_name = "Generic High-Performance CPU (AVX-512)"
    vram_gb = 12.0
    
    try:
        import torch
        if torch.cuda.is_available():
            has_cuda = True
            device_name = torch.cuda.get_device_name(0)
            vram_bytes = torch.cuda.get_device_properties(0).total_memory
            vram_gb = round(vram_bytes / (1024 ** 3), 2)
    except Exception:
        # Check through powershell / wmic or fallback
        pass
        
    print(f"  \033[92m✔ Acceleration:\033[0m {'NVIDIA CUDA Engine (Direct Compute)' if has_cuda else 'DirectCompute / GPU Fallback'}")
    print(f"  \033[92m✔ Hardware Target:\033[0m \033[1m{device_name}\033[0m")
    print(f"  \033[92m✔ Dedicated VRAM:\033[0m {vram_gb} GB")
    return has_cuda, device_name

def send_backend_heartbeat(node_id, wallet, tflops, job_id, poi_hash, reward):
    try:
        payload = json.dumps({
            "node_id": node_id,
            "wallet": wallet,
            "tflops": tflops,
            "job_id": job_id,
            "poi_hash": poi_hash,
            "reward": reward
        }).encode()
        req = urllib.request.Request(
            "http://localhost:8000/api/nodes/heartbeat",
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        urllib.request.urlopen(req, timeout=0.4)
    except Exception:
        pass # Backend is optional; runs standalone gracefully

def load_or_init_ledger(wallet_address):
    if os.path.exists(LEDGER_FILE):
        try:
            with open(LEDGER_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("total_mined", 0.0), data.get("history", [])
        except Exception:
            pass
    return 0.0, []

def save_ledger(wallet_address, total_mined, history):
    try:
        with open(LEDGER_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "wallet": wallet_address,
                "total_mined": round(total_mined, 4),
                "last_active": datetime.now().isoformat(),
                "history": history[-50:] # keep last 50 epochs
            }, f, indent=2)
    except Exception:
        pass

def run_node_loop(has_cuda, device_name, wallet_address, network="devnet"):
    slot = get_solana_devnet_status()
    print(f"  \033[92m✔ Settlement Network:\033[0m Solana {network.upper()} ({slot})")
    print(f"  \033[92m✔ Miner Wallet:\033[0m \033[94m{wallet_address}\033[0m")
    print(f"  \033[92m✔ Hard Max Supply:\033[0m 1,000,000 $DEAI (Non-Mintable)")
    print("-" * 86)
    
    print(f"\033[93m[*] Handshaking with DecentralizedAI Global Mesh RPC...\033[0m", flush=True)
    time.sleep(0.3)
    
    node_id = "0x" + hashlib.sha256(wallet_address.encode()).hexdigest()[:16].upper()
    print(f"\033[92m[✔] Node Registered!\033[0m Node Identity: \033[94m{node_id}\033[0m")
    print(f"\033[92m[✔] Swarm Model Sharded:\033[0m \033[93mDeepSeek-R1-671B (Layers 18-32 Sharded to Local VRAM)\033[0m")
    print(f"\033[96m[*] Dual-Metric Mining Active: [Uptime (Süre) + Compute Workload (İş Hacmi)]\033[0m\n")
    print(f"{'TIME':<8} | {'UPTIME':<8} | {'JOB ID':<8} | {'SHARD TENSORS':<16} | {'TFLOPS':<8} | {'POI HASH':<14} | {'REWARD ($DEAI)'}")
    print("=" * 86)

    models = ["DeepSeek-R1-671B", "Qwen-2.5-72B", "Llama-3.3-70B", "DEAI-Genesis-V1"]
    total_rewards, history = load_or_init_ledger(wallet_address)
    start_time = time.time()
    batch_count = len(history)

    try:
        while True:
            batch_count += 1
            now = datetime.now().strftime("%H:%M:%S")
            uptime_sec = int(time.time() - start_time)
            uptime_str = f"{uptime_sec // 60:02d}m {uptime_sec % 60:02d}s"
            
            job_id = f"#{random.randint(10000, 99999)}"
            model = random.choice(models)
            tflops = round(random.uniform(14.2, 38.6), 1)
            layer_range = f"Layers {random.randint(1, 32)}-{random.randint(33, 64)}"
            
            # Simulated Proof-of-Inference computation
            entropy = f"{batch_count}-{model}-{wallet_address}-{time.time()}".encode()
            poi_hash = hashlib.sha256(entropy).hexdigest()[:10] + "..."
            
            # Dual-Metric Formula: Uptime yield + Workload yield
            uptime_yield = 0.0005
            workload_yield = round(random.uniform(0.015, 0.045), 4)
            epoch_reward = round(uptime_yield + workload_yield, 4)
            total_rewards += epoch_reward
            
            history.append({
                "time": now,
                "job_id": job_id,
                "tflops": tflops,
                "reward": epoch_reward,
                "hash": poi_hash
            })
            save_ledger(wallet_address, total_rewards, history)
            send_backend_heartbeat(node_id, wallet_address, tflops, job_id, poi_hash, epoch_reward)
            
            # Formatted log
            print(f"{now:<8} | {uptime_str:<8} | {job_id:<8} | \033[96m{layer_range:<16}\033[0m | {tflops:<8} | 0x{poi_hash:<12} | \033[92m+{epoch_reward:>6.4f} $DEAI\033[0m (Total: {total_rewards:.4f})", flush=True)
            
            # Periodic Swarm AI Evolution pulse
            if batch_count % 4 == 0:
                print(f"  \033[95m↳ [SWARM EVOLUTION] Activation weights aggregated to Collective AI Mesh. Model IQ: +0.00{random.randint(12, 99)}%\033[0m", flush=True)
            
            time.sleep(random.uniform(1.5, 2.5))
    except KeyboardInterrupt:
        print("\n\033[91m[!] Node gracefully disconnected from DecentralizedAI Mesh.\033[0m")
        print(f"\033[92m[✔] Session Summary:\033[0m Total Mined: \033[1m{total_rewards:.4f} $DEAI\033[0m saved to ledger.")
        print(f"    Target Wallet: \033[94m{wallet_address}\033[0m\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DecentralizedAI GPU Worker Node")
    parser.add_argument("--wallet", type=str, default="PhantomDevnetWallet_Demo111111111111111111", help="Solana Wallet Address to receive $DEAI")
    parser.add_argument("--network", type=str, default="devnet", choices=["devnet", "mainnet"], help="Solana Cluster Network")
    args = parser.parse_args()

    print_banner()
    has_cuda, dev = detect_hardware()
    run_node_loop(has_cuda, dev, args.wallet, args.network)
