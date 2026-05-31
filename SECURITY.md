# Security Policy

Thesis OS is an open-source core for investment research workflows. It should not contain secrets.

## Reporting

If you find a security issue, open a private security advisory on GitHub if available. If not, open an issue without including exploit details or secrets.

## Secret Handling

Never commit:

- API keys
- OAuth tokens
- Browser cookies
- Broker sessions
- Account identifiers
- Telegram sessions
- Private vaults
- Paid raw data

## Public / Private Split

The public repository should contain schemas, templates, examples, and adapter interfaces.

Private deployments should keep credentials, real adapters, private vaults, and real portfolio data outside this repository.

## Promotion Boundary

Do not use this repository to publish private portfolio data, selective profitable predictions, live stock recommendations, or target-price promotion. Thesis OS is a framework, not investment advice or a signal service.

See [Promotion And Compliance Guardrails](docs/promotion-and-compliance.md).
