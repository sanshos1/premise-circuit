# Premise Circuit

Most reviews inspect assumptions one by one. Real conclusions fail in chains.

Premise Circuit stores an ordered dependency graph: early premises feed intermediate claims, which feed terminal conclusions. A separate auditor supplies two public evidence records. GenLayer validators classify every premise as supported, contradicted, or unknown and bind every material classification to source indexes and byte digests. The contract then propagates the result without another model call.

A contradiction invalidates every downstream node. An unknown premise places downstream nodes at risk unless a contradiction has already invalidated them. Only a graph whose terminal nodes remain supported becomes `VERIFIED`; other terminal outcomes are `AT_RISK` or `INVALID`.

Forward-only edges make cycles impossible. Duplicate IDs, self-auditing, incomplete partitions, unattributed material findings, repeated evidence origins, and replayed audits fail closed.

## Verify

```text
genvm-lint check contracts/contract.py
python -m pytest -q
```

The evidence records are operator-created fixtures mirrored across two hosts. Host separation tests retrieval behavior; it does not establish independent authorship.

## StudioNet proof

- Contract: [`0x899F1B7235F8A87f749F43FBd0C944f7a31E001F`](https://explorer-studio.genlayer.com/address/0x899F1B7235F8A87f749F43FBd0C944f7a31E001F)
- Deployment: [`0x3e70065d63c6a4294ca7300844b6cd109c80c6a13d1254e9b80fa19e8d87a8b8`](https://explorer-studio.genlayer.com/transactions/0x3e70065d63c6a4294ca7300844b6cd109c80c6a13d1254e9b80fa19e8d87a8b8)
- Live audit: [`0x93f6f79da6441746a09fce9a03f9c208bd375e5f556d38bcffbba109213905f5`](https://explorer-studio.genlayer.com/transactions/0x93f6f79da6441746a09fce9a03f9c208bd375e5f556d38bcffbba109213905f5)
- Result: `ROUTE-1791073000`, five supported nodes, `VERIFIED`.
- Deployed source SHA-256: `d89b87742279bc955609da6298ba2c7fe185cc6ddd5972ec41e177014e280d48`, exact match.

