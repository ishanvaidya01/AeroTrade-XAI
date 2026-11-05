# Security Policy

## Supported versions

This project does not publish versioned releases. Security fixes are applied to
the latest commit on the `main` branch.

| Version | Supported |
|---|---|
| Latest `main` | Yes |
| Older commits, forks, and modified deployments | No |

## Reporting a vulnerability

Please report security issues privately. Do **not** open a public issue.

- Email: [ishan.vaidya01@gmail.com](mailto:ishan.vaidya01@gmail.com)
- GitHub Security Advisories: [open a private advisory](https://github.com/ishanvaidya01/AeroTrade-XAI/security/advisories/new)

Include a description of the issue, reproduction steps, affected files or
configuration, and the potential impact. If you believe a credential has been
exposed, do not include the credential itself; describe where it appeared and
rotate it immediately.

## Scope

Examples of in-scope reports:

- Committed API keys, tokens, or other secrets
- Prompt-injection paths that cause the agent to take unintended actions
- Unsafe handling of untrusted scenario or news content
- Dependency vulnerabilities that are reachable from this application
- Injection or cross-site scripting issues in rendered LLM output
- Denial-of-service paths such as unbounded agent tool loops

Out of scope:

- The accuracy or business suitability of the heuristic route metrics
- Vulnerabilities in third-party services (GDELT, Open-Meteo, Open ER API,
  model providers) that do not affect this codebase
- Issues requiring a compromised host, browser extension, or user account
- Missing security headers on a local development server

## Response expectations

Reports are handled on a best-effort basis by the maintainer. You can expect an
acknowledgement when the report is reviewed and an update if a fix is planned.
No fixed response or remediation deadline is promised.

## Operational guidance

- Keep provider keys in a local `.env` file. The file is ignored by Git, but it
  must still be protected on disk.
- Use separate, rotated keys for deployments. Never reuse a personal key in a
  public demo.
- Review prompts and model output before enabling any future action that can
  book, purchase, or modify a shipment.
- Pin and audit dependencies before deploying this prototype to a shared or
  production environment.
