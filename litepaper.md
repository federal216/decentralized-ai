# DecentralizedAI ($DEAI) — Technical Litepaper v1.0
### The Sovereign DePIN Compute Mesh for Open-Source Artificial Intelligence
**Network:** Solana (SPL) / Base Layer-2  
**Symbol:** `$DEAI`  
**Total Supply:** 1,000,000,000 $DEAI (Fixed, Non-Mintable)  
**Tax:** 0% Buy / 0% Sell | Liquidity: 100% Fair Launch  

---

## 1. Executive Summary & The Problem

The artificial intelligence revolution is currently bottlenecked by a centralized oligopoly: **AWS, Microsoft Azure, Google Cloud, and OpenAI**. 

### The Triad of Centralization Failure:
1. **Draconian Censorship & Black-Box Alignment:** Centralized frontier models actively sanitize, suppress, and steer informational queries according to proprietary corporate agendas.
2. **Exorbitant API Extraction:** Startups and retail developers are bled dry by opaque token pricing and rate limits.
3. **Single Point of Failure (SPOF):** An outage in AWS us-east-1 halts global AI applications overnight.

Meanwhile, over **150,000,000 consumer GPUs** (NVIDIA RTX 3060, 3080, 4070, 4090) sit idle across the globe, consuming negligible baseline power while gaming rigs sleep.

**DecentralizedAI ($DEAI)** bridges this chasm by constructing an open-source, peer-to-peer decentralized physical infrastructure network (DePIN) that aggregates consumer GPUs into a unified, censorship-resistant neural inference supercomputer.

---

## 2. Protocol Architecture & Proof-of-Inference (PoI)

```
[ Client Application / API Query ]
              │
              ▼
   [ DEAI Discovery Gateway ]
              │
    ┌─────────┴─────────┐
    ▼                   ▼
[ Worker Node A ]   [ Worker Node B ]
(RTX 3060 Laptop)   (RTX 4090 Desktop)
    │                   │
    └─────────┬─────────┘
              ▼
   [ Consensus Validator ]
 (Cryptographic PoI Check)
              │
              ▼
[ Verified Output + $DEAI Emission ]
```

### 2.1 Proof-of-Inference (PoI) Consensus
Traditional Proof-of-Work (PoW) burns electrical energy computing useless SHA-256 hashes. **Proof-of-Inference (PoI)** harnesses this raw compute for real-world mathematical utility:

1. **Shard Dispatch:** A heavy LLM query (e.g., DeepSeek-R1 8B or Qwen 2.5) is partitioned into lightweight tensor shards.
2. **Deterministic Sampling:** Random worker nodes compute the intermediate activations.
3. **Zero-Knowledge Challenge:** The network sends a micro-challenge verification matrix. If the node's returned tensor matches deterministic baseline checkpoints, the node is awarded a cryptographic block reward in `$DEAI`.
4. **Slashing Penalty:** Malicious nodes returning hallucinated or corrupted tensors are slashed and de-registered from the peer routing table.

---

## 3. Supported Model Zoo

DecentralizedAI natively runs quantizations of the world's most elite open-source models:
* **DeepSeek-R1 (8B & 14B Distill):** High-reasoning mathematical and clinical logic.
* **Qwen 2.5 (7B & 14B Coder):** Deterministic algorithmic execution.
* **Llama 3.1 (8B Instruct):** General conversational intelligence.
* **Whisper & Vision Encoders:** Multimodal image and speech synthesis.

---

## 4. Tokenomics ($DEAI)

A clean, institutional, un-ruggable economic architecture:

* **Total Supply:** 1,000,000,000 `$DEAI` (One Billion Tokens, strictly capped).
* **Launch Mechanism:** 100% Fair Launch on Solana via Pump.fun / Raydium bonding curve.
* **Taxes:** **0% Buy / 0% Sell.** Zero hidden fees or transaction tithes.
* **Ownership:** Smart contract ownership renounced upon migration.
* **Liquidity:** 100% burned / permanently locked.

### The Deflationary "Compute-and-Burn" Flywheel:
When enterprise clients or developers query the DecentralizedAI API mesh:
* **80% of query fees** are distributed directly to active GPU worker nodes as hardware compensation.
* **20% of query fees** are automatically market-bought and **burned forever**, shrinking the circulating supply with every generated token.

---

## 5. Roadmap

* **Phase 1 (Q4 2024 - Q1 2025):** 
  - $DEAI Token Fair Launch & Community Formation.
  - Python CLI Worker Node (`worker_node.py`) public release on GitHub.
  - Testnet Node Registry with live telemetry dashboard.
* **Phase 2 (Q2 2025):**
  - Web-based 1-click node client (WebGPU execution in Chrome/Brave).
  - DeepSeek-R1 distributed sharding across consumer hardware.
  - DexScreener & CoinGecko / CoinMarketCap Fast-Track Verification.
* **Phase 3 (Q3 2025):**
  - Enterprise SDK (drop-in replacement for `openai` Python package).
  - Mainnet DAO governance & decentralized hardware staking.

---

## 6. Official Verified Links
* **Portal:** https://federal216.github.io/decentralized-ai/
* **GitHub Repository:** https://github.com/federal216/decentralized-ai
* **Contract:** Announced on official launch
* **Disclaimer:** *$DEAI is a decentralized utility token powering a peer-to-peer compute network. Not financial advice. Zero investment guarantees.*
