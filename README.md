# Mitsumata FLOP Agent

Independent research and agent development by [Mitsumata](https://mitsumata.io), maintained as [mitsumata-io](https://github.com/mitsumata-io).

This repository contains a reproducible, offline economics tool and a participation evidence framework. It is not a deployed FLOP node, inference agent, wallet, or claim service. No airdrop allocation or upstream contribution credit is verified.

## Run the research tool

Python 3.10 or later, standard library only. No account, wallet, signing key, network connection, or package installation is needed.

```console
python economics.py --cash-cost 100 --hours 4 --hourly-cost 25 --tokens 0
python economics.py --cash-cost 100 --hours 4 --hourly-cost 25 --tokens 1000 --liquid-fraction 0.25 --realization-probability 0.5 --token-price 2
python -m unittest -v
python verify_project.py
```

The second command is an illustrative scenario, not a FLOP forecast. It yields a total cost of 200, probability-weighted liquid tokens of 125, a break-even price of 1.60, and scenario net profit of 50 in the chosen currency. At zero token realization, the same work loses its full cost. Unverified allocations default to zero in the tool.

## Participation and attribution

- [Current requirements and gaps](PARTICIPATION.md)
- [Contribution evidence and submission process](CONTRIBUTIONS.md)
- [Project context and decision rules](PROJECT_CONTEXT.md)
- [Current status](STATUS.md)
- [Official source register](SOURCES.md)
- [Security policy](SECURITY.md)

The pre-existing [public identity record](public-identity.json) is retained unchanged. A DID is a public identifier; its corresponding private key is kept outside this repository. An identity record or GitHub commit is not proof of FLOP reward eligibility.

The project is a clean Mitsumata start. The retired EvolPolf history is preserved separately, and no prior contribution credit is imported or duplicated.
