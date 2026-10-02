# GenLayer HelloWorld example

A small Python DSL contract stores a string. `get_storage()` reads it and `update_storage(new_storage)` replaces it. Initial value: `Hello from GenLayer!`.

## Source and validation

The source is `hello_world.py`. Python syntax can be checked without executing or deploying it:

```sh
python -m py_compile hello_world.py
```

This check does not validate the GenLayer VM, SDK compatibility, contract permissions, or deployment. The GenLayer runtime is required to execute the decorators and contract. This repository does not pin or bundle that runtime. Use the official [GenLayer documentation](https://docs.genlayer.com/) to select and configure the environment matching your target network.

## Usage example

In a compatible GenLayer environment, read `get_storage()`, then call `update_storage("A new value")` with an authorized test account, and read again. A write changes chain state and needs separate transaction authorization. No deployment or chain write was performed during this review.

## Limits and deployment status

The former abbreviated address and transaction hash did not allow verification. No deployment success or supported testnet version is asserted here. Supply a full address, full transaction hash, network identifier, and explorer receipt before documenting a verified deployment. This example does not establish airdrop eligibility.
