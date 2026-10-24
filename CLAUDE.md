# Project context (read this first, every session)

This repo is one of 5 flagship portfolio projects for a GitHub profile aimed at an AI engineer / CTO path. The profile must show production engineering, system architecture, cost optimization and security, through decisions and measured evidence, not feature lists.

The owner works in the KEAL framework (Koukoui Enterprise AI Lifecycle): four gates (Discovery, Feasibility, Development, Governance), each needing a self sign-off backed by an evidence link. Notion is the source of truth for tasks and status (links below).

## Hard constraints
1. **Free tiers only.** Never add a paid service, a paid dependency, or a step that needs a payment method. If something seems to need paying, stop and propose a free alternative.
2. **No secrets** in the repo, frontend bundles, logs or commits. Use `.env.example`, platform secret stores and a pre-commit secret scan (gitleaks).
3. **Never fabricate or round up numbers.** Every figure in the README or docs must trace to committed data or a logged run. Label estimates as estimates. Record the date for every price or limit.
4. Provider limits and model names live in **config**, not in code.
5. **Never run model-generated or untrusted code on the host.** Use an isolated container with no network.
6. Use **synthetic data only** for anything resembling personal data.

## How to work
- Start each session by reading this file and `docs/`. Check the Notion Build Tasks for this project (if the Notion connector is available) and take the lowest-order "To do" task.
- Run feasibility tests first. If one fails, stop and report before building on that assumption.
- For architecture-impacting choices, write a short ADR in `docs/adr/` (context, options, decision, cost) and ask the owner before committing to it.
- Prefer the smallest implementation that passes the test. Keep commits small with clear messages.
- Write tests. Where it makes sense, the local dev path is one command (Docker Compose or a make target).
- A task is **Done only with evidence**: a commit, test output, chart or run log. Put the link in the Notion task's Evidence URL.
- If unsure about a provider limit or API detail, check the official docs and say what you verified. Anything marked **VERIFY** must be confirmed before you rely on it.
- When using the Notion connector: set Status to "In progress" when you start a task, "Done" (plus Evidence URL) when finished, and put decisions in Notes. Never delete rows.

## Required in every repo
README (live demo link at the top, architecture diagram, results, cost table, limitations), `docs/adr/`, `docs/threat-model.md`, `docs/ops.md` (monitoring, rollback), `docs/keal-gates.md` (gates passed, with evidence links).

## Demo rules
The live demo shows its evidence, has a graceful fallback for every failure and budget state, shows a privacy notice, and enforces rate limits. It never shows a raw error page.

Notion links: Command Center https://app.notion.com/p/3fde9a5ffec081a4b7c4f59a7092dba7 , Build Tasks https://app.notion.com/p/0043b09ab6e047c9b90ab8662936e183

---

# Project: Secure Agent Code Execution Sandbox (gVisor / Docker)
Notion page (full brief): https://app.notion.com/p/3fde9a5ffec081a98ea2e8898fe1c503

## Goal
An isolation layer that lets an AI agent run Python/Bash without compromising the host, proven by an automated attack-test suite. The demo is a **recorded attack-test dashboard** (static, Cloudflare Pages), not a public "run any code" box.

## Why no live code box
Public arbitrary code execution is the riskiest thing to host, and gVisor needs a host that permits it, which free hosting probably does not (VERIFY). Stretch goal only: a Pyodide in-browser playground, documented as a lighter isolation tier in an ADR.

## Safety rules for this repo
- The attack catalog is **defensive testing of your own sandbox**. Attack scripts run ONLY inside the sandbox under test, or inside a disposable VM/container. Never run them on the host machine, and never aim anything at third-party systems.
- Keep attack scripts minimal and descriptive of the behavior class being tested. Do not write weaponized exploits.
- Default-deny network egress, strict CPU/memory/time limits, a fresh sandbox per execution, no persistence between runs.

## Task order (mirror in Notion Build Tasks)
1. Write the threat model FIRST (escape, resource exhaustion, network exfiltration, persistence, abuse of the demo as free compute, prompt injection steering the agent into hostile code)
2. Feasibility: confirm where gVisor can run for your own test runs (local, CI or a free notebook environment) (VERIFY)
3. ADR comparing plain Docker vs. gVisor vs. microVM
4. Build the sandbox
5. Attack catalog written from the threat model
6. Automate the suite; record outputs as committed artifacts
7. Measure startup and per-execution overhead
8. Static dashboard from recorded results
9. State clearly what gVisor does not protect against; ops note (patching, incident steps)
