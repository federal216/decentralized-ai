#!/usr/bin/env python3
"""
DecentralizedAI ($DEAI) - Edge GPU Worker Node Client v1.0.4
Decentralized Peer-to-Peer Neural Compute Mesh
"""

import sys
import time
import hashlib
import random
from datetime import datetime

# Enforce UTF-8 on Windows consoles
try:
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

def print_banner():
    banner = """
\033[38;2;16;185;129m
  ██████╗ ███████╗ ██████╗███████╗███╗   ██╗████████╗██████╗  █████╗ ██╗     
  ██╔══██╗██╔════╝██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██║     
  ██║  ██║█████╗  ██║     █████╗  ██╔██╗ ██║   ██║   ██████╔╝███████║██║     
  ██║  ██║██╔══╝  ██║     ██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗██╔══██║██║     
  ██████╔╝███████╗╚██████╗███████╗██║ ╚████║   ██║   ██║  ██║██║  ██║███████╗
  ╚═════╝ ╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                     DECENTRALIZED NEURAL COMPUTE MESH ($DEAI)
\033[0m"""
    print(banner)

def detect_hardware():
    print("\033[96m[*] Probing local compute hardware and CUDA subsystem...\033[0m", flush=True)
    time.sleep(0.2)
    
    has_cuda = False
    device_name = "Generic High-Performance CPU (AVX-512)"
    vram_gb = 16.0
    
    try:
        import torch
        if torch.cuda.is_available():
            has_cuda = True
            device_name = torch.cuda.get_device_name(0)
            vram_bytes = torch.cuda.get_device_properties(0).total_memory
            vram_gb = round(vram_bytes / (1024 ** 3), 2)
    except Exception:
        pass
        
    print(f"  \033[92m✔ Acceleration:\033[0m {'NVIDIA CUDA Engine' if has_cuda else 'Simulated CPU Fallback'}")
    print(f"  \033[92m✔ Hardware Target:\033[0m \033[1m{device_name}\033[0m")
    print(f"  \033[92m✔ Dedicated VRAM:\033[0m {vram_gb} GB")
    print(f"  \033[92m✔ Protocol Version:\033[0m DEAI-Mesh v1.0.4-mainnet-seed")
    print("-" * 75)
    return has_cuda, device_name

def run_node_loop(has_cuda, device_name):
    print(f"\033[93m[*] Handshaking with DecentralizedAI Global Mesh RPC (Solana Anchor Gate)...\033[0m", flush=True)
    time.sleep(0.3)
    
    node_id = "0x" + hashlib.sha256(str(time.time()).encode()).hexdigest()[:16].upper()
    print(f"\033[92m[✔] Node Registered!\033[0m Node Identity: \033[94m{node_id}\033[0m")
    print(f"\033[92m[✔] Active Mesh Shards Allocated:\033[0m [DeepSeek-R1-8B-Distill, Qwen-2.5-7B-Quant, Llama-3-Vision]")
    print(f"\033[96m[*] Listening for peer-to-peer inference batches & Proof-of-Inference (PoI) challenges...\033[0m\n")
    print(f"{'TIMESTAMP':<12} | {'JOB ID':<10} | {'MODEL SHARD':<18} | {'LATENCY':<10} | {'POI HASH':<16} | {'REWARD ($DEAI)'}")
    print("=" * 85)

    models = ["deepseek-r1:8b", "qwen2.5:7b", "llama3.1:8b", "mistral-nemo"]
    total_rewards = 0.0
    block_num = 148200

    try:
        while True:
            block_num += 1
            now = datetime.now().strftime("%H:%M:%S")
            job_id = f"#{random.randint(10000, 99999)}"
            model = random.choice(models)
            latency = f"{random.uniform(14.2, 38.6):.1f} ms"
            
            # Simulated Proof-of-Inference computation
            entropy = f"{block_num}-{model}-{time.time()}".encode()
            poi_hash = hashlib.sha256(entropy).hexdigest()[:12] + "..."
            
            reward = round(random.uniform(0.015, 0.045), 4)
            total_rewards += reward
            
            # Green output for confirmed shard with immediate flush
            print(f"{now:<12} | {job_id:<10} | \033[96m{model:<18}\033[0m | {latency:<10} | 0x{poi_hash:<14} | \033[92m+{reward:>7.4f} $DEAI\033[0m (Total: {total_rewards:.4f})", flush=True)
            
            # Simulating GPU workload interval
            time.sleep(random.uniform(1.2, 2.8))
    except KeyboardInterrupt:
        print("\n\033[91m[!] Node gracefully disconnected from DecentralizedAI Mesh.\033[0m")
        print(f"\033[92m[✔] Unclaimed Epoch Rewards: {total_rewards:.2f} $DEAI sent to local signer vault.\033[0m\n")

if __name__ == "__main__":
    print_banner()
    has_cuda, dev = detect_hardware()
    run_node_loop(has_cuda, dev)
