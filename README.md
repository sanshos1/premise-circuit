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

