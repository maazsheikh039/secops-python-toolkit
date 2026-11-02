# DNS Resolution and Anomaly Simulation Suite

A comprehensive set of Bash and Python security utilities designed to query DNS resource records, simulate complex DNS anomalies (NXDOMAIN storms, Fast Flux C&C networks, and high-entropy DGA patterns), and perform heuristic threat detection.

## Objectives
- Perform targeted DNS record queries (`A`, `AAAA`, `MX`, `NS`, `TXT`) using `dig` and `dnspython`.
- Automate DNS query logging and status tracking via Bash scripting.
- Simulate advanced DNS attack vectors including Fast Flux IP rotation and algorithmic domain generation (DGA).
- Implement algorithmic threat heuristics (Shannon entropy calculations, character length checks, numeric ratio thresholds) to flag suspicious domains.

## Tools Used
- **DNS Utilities:** `dig`, `bind9-host`
- **Python 3** (`dnspython`, `collections`, `random`)
- **Linux CLI / Bash**

## Key Skills Demonstrated
- **Threat Intelligence Engineering:** Identifying malicious domain characteristics such as high randomness and rapid IP flux.
- **DNS Protocol Analysis:** Parsing and querying DNS resolution responses.
- **Heuristic Detection Modeling:** Calculating Shannon entropy to distinguish between human-readable domain names and machine-generated DGA strings.

## Troubleshooting Log
- *DNS Resolver Library:* Ensured `dnspython` is installed inside the working environment.
- *Network Connectivity:* Verified outbound port 53 UDP/TCP connectivity for public DNS resolution tests.
