# GenLayer Intelligent Contracts

Smart contracts deployed on **GenLayer Testnet (Bradbury)**.

## 📋 About

This repo contains intelligent contracts written for the GenLayer blockchain using Python-based DSL. Part of the GenLayer Builder Journey program.

## 📄 Contracts

### HelloWorld

A simple storage contract that stores and retrieves a string value.

**Features:**
- `get_storage()` → Returns the stored string (view)
- `update_storage(new_value)` → Updates the stored string (write)

**Contract Address:** `0xF3...3404`

**Transaction:** `0x57d6...fbb9`

**Status:** ✅ ACCEPTED | ✅ SUCCESS

### Run Locally

```bash
# Install GenLayer CLI
pip install genlayer

# Deploy
genlayer deploy hello_world.py
```

## 🛠️ Tech Stack

- **Language:** Python (GenLayer DSL)
- **Network:** GenLayer Testnet (Bradbury)
- **Type:** Intelligent Contract

## 🔗 Links

- [GenLayer](https://genlayer.com/)
- [GenLayer Docs](https://docs.genlayer.com/)
- [X: @Demarco639](https://x.com/Demarco639)
