# Security policy

This repository must contain public work only. Private keys, seeds, passphrases, encrypted key backups, signing utilities with local access, mail exports, private logs, customer data, and claim credentials are excluded. A public DID and public key are identifiers, not signing secrets; pre-existing public records remain unchanged.

Agents must work from explicit public-file allowlists. Do not inspect sibling private directories, encrypted vaults, historical chat exports, or raw backups. Do not rely on .gitignore as a security boundary. Review the precise file list before every upload; never upload a parent project directory or run git add -A from it.

No signing or wallet connection is part of the offline tools. Scripts have no network calls and use only supplied hypothetical economic inputs. Unknown rewards and market prices must not become claimed assets.

## Reporting

For this repository, contact anthony@mitsumata.io privately with a minimal, secret-free description. Do not include real keys, passwords, private financial records, or exploitable details in public issues.

For FLOP protocol or infrastructure vulnerabilities, use [FLOP's security policy](https://github.com/flop-labs/yellowpaper/blob/main/SECURITY.md). It directs private reporting and currently describes a pre-mainnet project with no bug bounty program. This project cannot promise a bounty or allocation.

If exposure is suspected, stop publication and signing, preserve a safe incident record, and let the operator handle credential rotation and revocation privately. Never echo a suspected secret to explain the problem.
