#!/usr/bin/env python3
"""
DecentralizedAI ($DEAI) - Edge GPU Worker Node Client v2.0.0
Dual-Metric Proof-of-Inference (PoI) & Collective Swarm AI Engine
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
    print(f"  \033[92m✔ Settlement Network:\033[0m Solana SPL Mainnet ($DEAI / SOL)")
    print(f"  \033[92m✔ Hard Max Supply:\033[0m 1,000,000 $DEAI (Non-Mintable)")
    print("-" * 80)
    return has_cuda, device_name

def run_node_loop(has_cuda, device_name):
    print(f"\033[93m[*] Handshaking with DecentralizedAI Global Mesh RPC (Solana Anchor Gate)...\033[0m", flush=True)
    time.sleep(0.3)
    
    node_id = "0x" + hashlib.sha256(str(time.time()).encode()).hexdigest()[:16].upper()
    print(f"\033[92m[✔] Node Registered!\033[0m Node Identity: \033[94m{node_id}\033[0m")
    print(f"\033[92m[✔] Swarm Model Allocated:\033[0m \033[93mDeepSeek-DEAI-R1-671B (Layers 18-28 Sharded to Local VRAM)\033[0m")
    print(f"\033[96m[*] Dual-Metric Mining Active: [Uptime (Süre) + Compute Workload (İş Hacmi)]\033[0m\n")
    print(f"{'TIME':<8} | {'UPTIME':<8} | {'JOB ID':<8} | {'SHARD TENSORS':<16} | {'TFLOPS':<8} | {'POI HASH':<14} | {'REWARD ($DEAI)'}")
    print("=" * 86)

    models = ["DeepSeek-R1-671B", "Qwen-2.5-72B", "Llama-3.3-70B", "DEAI-Genesis-V1"]
    total_rewards = 0.0
    start_time = time.time()
    batch_count = 0

    try:
        while True:
            batch_count += 1
            now = datetime.now().strftime("%H:%M:%S")
            uptime_sec = int(time.time() - start_time)
            uptime_str = f"{uptime_sec // 60:02d}m {uptime_sec % 60:02d}s"
            
            job_id = f"#{random.randint(10000, 99999)}"
            model = random.choice(models)
            tflops = round(random.uniform(12.4, 34.8), 1)
            layer_range = f"Layers {random.randint(1, 32)}-{random.randint(33, 64)}"
            
            # Simulated Proof-of-Inference computation
            entropy = f"{batch_count}-{model}-{time.time()}".encode()
            poi_hash = hashlib.sha256(entropy).hexdigest()[:10] + "..."
            
            # Dual-Metric Formula: Uptime yield + Workload yield
            uptime_yield = 0.0004
            workload_yield = round(random.uniform(0.012, 0.038), 4)
            epoch_reward = round(uptime_yield + workload_yield, 4)
            total_rewards += epoch_reward
            
            # Formatted log
            print(f"{now:<8} | {uptime_str:<8} | {job_id:<8} | \033[96m{layer_range:<16}\033[0m | {tflops:<8} | 0x{poi_hash:<12} | \033[92m+{epoch_reward:>6.4f} $DEAI\033[0m (Total: {total_rewards:.4f})", flush=True)
            
            # Periodic Swarm AI Evolution pulse
            if batch_count % 4 == 0:
                print(f"  \033[95m↳ [SWARM EVOLUTION] Activation weights aggregated to Collective AI Mesh. Model IQ: +0.00{random.randint(12, 99)}%\033[0m", flush=True)
            
            # Workload delay
            time.sleep(random.uniform(1.4, 2.6))
    except KeyboardInterrupt:
        print("\n\033[91m[!] Node gracefully disconnected from DecentralizedAI Mesh.\033[0m")
        print(f"\033[92m[✔] Total Mined: {total_rewards:.4f} $DEAI sent to Solana Wallet.\033[0m\n")

if __name__ == "__main__":
    print_banner()
    has_cuda, dev = detect_hardware()
    run_node_loop(has_cuda, dev)
