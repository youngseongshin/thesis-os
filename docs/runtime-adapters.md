# Runtime Adapters

Thesis OS is the investment-domain core. It defines the objects and loop:

```text
evidence -> screener candidate -> thesis -> action/prediction -> feedback
```

The core can run in several runtimes:

| Runtime | Best for | How it should use Thesis OS |
|---|---|---|
| CLI | local experiments and reproducible demos | run commands such as `quickstart-stock`, `alpha run-quant-screener`, and `arki build-dashboard` |
| cron / launchd / systemd | simple recurring jobs | schedule market refresh, screener refresh, wiki build, and feedback evaluation commands |
| GitHub Actions | public CI and examples | verify schemas, demos, sample outputs, and docs stay runnable |
| OpenClaw | long-running local agent systems | host Alpha, Lattice, and Arki as persistent agents with skills, memory, chat gateways, and operational logs |
| Custom app/server | product deployments | call Thesis OS modules from an API, dashboard, or private data pipeline |

## Boundary

The public repository should not require a specific runtime. A user should be able to run the quickstart with only Python:

```bash
thesis-os quickstart-stock --out ./quickstart_run
```

OpenClaw is the reference runtime for the original long-running deployment, but it is not required to understand or use the open-source core.

## Adapter Contract

Runtime adapters should provide:

- command execution
- scheduling
- secrets outside the public repo
- delivery surfaces such as Telegram, email, web, or files
- durable logs
- memory promotion policy
- failure handling

They should not change the Thesis OS object model. The same `Evidence`, `ScreenerCandidate`, `Thesis`, `Action`, `Prediction`, and `Feedback` objects should remain valid whether the runtime is CLI, cron, GitHub Actions, OpenClaw, or a custom app.
