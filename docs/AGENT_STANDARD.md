# Agent Authoring Standard

Every agent in this repo follows the same contract. If you contribute one, match this.

Agents are **model-agnostic**: a YAML header of routing metadata, and a body that works as a
system prompt in any assistant. Write the body so it stands alone — somebody will paste it into a
tool you have never heard of.

## 1. File shape

```markdown
---
name: kebab-case-name
description: One sentence starting with "Use this agent when..." — this is what the
  orchestrator model reads to decide whether to route to you. Be specific about
  triggers, not aspirational about quality.
tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch
model: sonnet
---

You are a <role> ...
```

The header is metadata for tools that read it. Runtimes that do not read it ignore it, and a user
pasting the agent into a chat assistant drops it entirely — so **no instruction may live in the
header**. Everything the agent needs goes in the body.

- `name` must equal the filename without `.md`.
- `description` is a routing signal, not marketing copy. Name the concrete situations. This is the
  field a router, a classifier or an orchestrating model reads to decide whether to route here.
- `tools` — the capabilities the agent needs, named in a common convention. Grant the minimum.
  Most advisory agents need `Read, Write, Edit, WebSearch, WebFetch`; only agents that compute
  (payroll, tax, pricing, unit economics) need `Bash`. Tools that use different names map these
  across; tools without a tool system ignore them.
- `model` — a capability tier, not a vendor commitment. Use `haiku` for lookups, `sonnet` for most
  agents, `opus` for agents doing legal reasoning or multi-variable optimisation. These names come
  from one common convention; substitute the equivalent tier on whatever model you run. Keep the
  three-tier vocabulary so the validator and the routing stay consistent across the repo.

## 2. Required body sections

| Section | Purpose |
|---|---|
| Role statement | Who the agent is and whose problem it solves. First line, no heading. |
| `## When you are invoked` | A numbered opening move. What the agent asks or checks first. |
| `## Philippine ground truth` | The domain knowledge that makes the agent PH-specific. Laws by RA number, agency names, forms by number, thresholds. |
| `## Decision framework` | How the agent reasons — tables, branch logic, or a scored checklist. Not vibes. |
| `## Deliverables` | The artefacts it produces, named. |
| `## Verify-before-advising` | The volatile figures it must re-check and where. **Mandatory.** |
| `## Hand off to` | Other agents in this repo it should defer to. |
| `## Limits` | What it must refuse or escalate to a licensed professional. **Mandatory.** |

## 3. The verification rule

Philippine rates, thresholds, and wage orders change — sometimes mid-year, sometimes
under injunction. An agent that confidently states a stale number is worse than no agent.

So every agent must:

1. Treat every peso figure in its own prompt as **last-known, not current**.
2. Name the primary source for each volatile figure (BIR RR number, NWPC wage order,
   SSS circular, the agency's own site — not a blog).
3. State the as-of date whenever it quotes a figure to the user.
4. Say plainly when it could not verify, instead of guessing.

The canonical primary sources are in [`docs/PRIMARY_SOURCES.md`](PRIMARY_SOURCES.md).

## 4. Voice

Instructions are written in English. Use the Filipino or Taglish term where that is the
*actual* vocabulary of the thing — `kabit na resibo`, `padala`, `suki`, `utang/lista`,
`13th month`, `barangay clearance`, `cedula`, `tiangge`, `palengke` — and gloss it once.
Do not translate for decoration.

Agents should write back to the business owner in plain language. A carinderia owner and
a CFO are both valid readers; the agent asks which one it is talking to and adjusts.

## 5. Anti-patterns

- Generic business advice with "Philippines" pasted on. If the body would be identical for
  a US business, the agent does not belong here.
- Hardcoded tax tables presented as current fact.
- Telling the owner what a lawyer or CPA must sign off on, without saying so.
- Agents that overlap. Check the index first; extend an existing agent instead.
