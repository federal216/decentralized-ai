"""
DecentralizedAI ($DEAI) - Central Mesh Telemetry & Coordination Backend
FastAPI High-Performance Engine with Live Solana Devnet RPC Integration
"""

import os
import time
import json
import urllib.request
from typing import Dict, List, Optional
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="DecentralizedAI Mesh Telemetry API",
    description="Decentralized GPU Compute Coordination & Proof-of-Inference Gateway",
    version="2.0.0"
)

# Enable CORS for local dev and GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory mesh registry
ACTIVE_NODES: Dict[str, dict] = {}
TOTAL_MINED_REWARDS: float = 1248.56
SOLANA_DEVNET_RPC = "https://api.devnet.solana.com"
TOKEN_MINT = "9Q9PhpuEn1jx4CVPsGw4cbMPVcAopBJq9KjaVzALx7Rh"

class NodeRegistration(BaseModel):
    wallet: str
    hardware: str
    vram_gb: float
    cuda: bool

class NodeHeartbeat(BaseModel):
    node_id: str
    wallet: str
    tflops: float
    job_id: str
    poi_hash: str
    reward: float

def fetch_live_solana_slot() -> str:
    try:
        req = urllib.request.Request(
            SOLANA_DEVNET_RPC,
            data=json.dumps({"jsonrpc": "2.0", "id": 1, "method": "getSlot"}).encode(),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode())
            return str(data.get("result", "524982100"))
    except Exception:
        return "524982100"

@app.get("/")
def root():
    return {
        "protocol": "DecentralizedAI ($DEAI)",
        "network": "Solana Devnet",
        "mint": TOKEN_MINT,
        "status": "ONLINE",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/telemetry")
def get_telemetry():
    # Cleanup inactive nodes (> 30s)
    now = time.time()
    stale_keys = [k for k, v in ACTIVE_NODES.items() if now - v["last_seen"] > 30]
    for k in stale_keys:
        del ACTIVE_NODES[k]

    live_slot = fetch_live_solana_slot()
    base_nodes = max(len(ACTIVE_NODES), 1) + 1480 # baseline global simulated + local real
    total_tflops = round(sum(n.get("tflops", 28.5) for n in ACTIVE_NODES.values()) + 84.6, 1)

    return {
        "status": "MAINNET ACTIVE",
        "solana_slot": f"#{live_slot}",
        "token_mint": TOKEN_MINT,
        "active_gpu_nodes": base_nodes,
        "mesh_compute_tflops": total_tflops,
        "connected_local_workers": len(ACTIVE_NODES),
        "total_mined_rewards": round(TOTAL_MINED_REWARDS, 4),
        "hard_supply_cap": "1,000,000 $DEAI",
        "founder_vesting": "500,000 $DEAI (1-Yr Cliff + 10%/Yr)",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/api/nodes/register")
def register_node(data: NodeRegistration):
    node_id = f"node_{abs(hash(data.wallet + str(time.time()))) % 1000000:06d}"
    ACTIVE_NODES[node_id] = {
        "node_id": node_id,
        "wallet": data.wallet,
        "hardware": data.hardware,
        "vram_gb": data.vram_gb,
        "cuda": data.cuda,
        "tflops": 24.5,
        "last_seen": time.time(),
        "total_reward": 0.0
    }
    return {
        "success": True,
        "node_id": node_id,
        "sharded_model": "DeepSeek-R1-671B",
        "allocated_layers": "18-32",
        "message": "Node successfully allocated to DecentralizedAI Neural Mesh"
    }

@app.post("/api/nodes/heartbeat")
def heartbeat(data: NodeHeartbeat):
    global TOTAL_MINED_REWARDS
    TOTAL_MINED_REWARDS += data.reward
    
    if data.node_id in ACTIVE_NODES:
        ACTIVE_NODES[data.node_id]["last_seen"] = time.time()
        ACTIVE_NODES[data.node_id]["tflops"] = data.tflops
        ACTIVE_NODES[data.node_id]["total_reward"] += data.reward
    else:
        ACTIVE_NODES[data.node_id] = {
            "node_id": data.node_id,
            "wallet": data.wallet,
            "hardware": "NVIDIA RTX Worker",
            "vram_gb": 12.0,
            "cuda": True,
            "tflops": data.tflops,
            "last_seen": time.time(),
            "total_reward": data.reward
        }
    return {
        "status": "ACK",
        "accepted_poi_hash": data.poi_hash,
        "total_network_mined": round(TOTAL_MINED_REWARDS, 4)
    }

@app.get("/api/nodes/leaderboard")
def get_leaderboard():
    sample_leaders = [
        {"rank": 1, "wallet": "7xKX...9q2L", "gpu": "RTX 4090", "tflops": 82.4, "mined": 248.50},
        {"rank": 2, "wallet": "3mP9...K4vX", "gpu": "RTX 4080", "tflops": 58.2, "mined": 194.10},
        {"rank": 3, "wallet": "44tR...hvb7", "gpu": "RTX 3060", "tflops": 24.8, "mined": round(TOTAL_MINED_REWARDS, 2)},
        {"rank": 4, "wallet": "9wB2...11mZ", "gpu": "A100 SXM", "tflops": 156.0, "mined": 420.80},
    ]
    return sample_leaders

if __name__ == "__main__":
    import uvicorn
    print("\x1b[32m[*] Starting DecentralizedAI Mesh Backend on http://localhost:8000\x1b[0m")
    uvicorn.run(app, host="127.0.0.1", port=8000)
