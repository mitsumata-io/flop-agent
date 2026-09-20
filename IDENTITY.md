# Public identity and private signing

The proposed Mitsumata identity uses an Ed25519 `did:key`, following [Technocore's published identity format](https://technocore.chat/auth.md).

The DID is public. A signature is created for a particular message; there is no permanent reusable message signature to assign to a brand. The private key controls signing and must stay with its operator.

## Local creation

The private setup utility is maintained outside this public repository. It prompts the user directly for an encryption passphrase and writes an encrypted PKCS#8 private key outside this repository and outside the previous signing directory. It must never print a seed, private key or passphrase.

Only the public DID and public key should be copied into this repository after verification. Keep the encrypted key and passphrase in appropriate separate backups under the user's control.

## Retirement of the previous identity

Retirement means the operator stops using the earlier identity for this project. A `did:key` has no service-side deletion or revocation mechanism. Do not claim that archiving a repository deletes old signatures or history.

A new key does not establish token eligibility or a right to duplicate participation rewards. Any public declaration should accurately describe the project transition and follow applicable published participation rules.
