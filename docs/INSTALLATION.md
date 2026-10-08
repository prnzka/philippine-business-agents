# Installation and use

These agents are plain Markdown files. Each has a short YAML header and a body of instructions.
Nothing in them is tied to a particular AI vendor, so there are two ways to use them: paste one
into whatever assistant you already use, or install the set into a tool that supports subagents.

## Option 1 — any AI assistant, no setup

This works with any model and is the fastest way to start.

1. Find the agent for your situation in the [README index](../README.md#the-agents).
2. Open the file and copy **everything below the `---` header block**.
3. Paste it in as the system prompt, custom instruction, project instruction or custom-assistant
   instruction for a new conversation.
4. Describe your situation and let it work.

The YAML header (`name`, `description`, `tools`, `model`) is routing metadata for tools that
support subagents. It is not part of the instructions and can be dropped.

If your assistant supports a project or workspace with persistent instructions, put the agent
there and the setup survives between conversations.

**Combining a few agents.** Most real questions touch two or three domains — tax and labour, or
pricing and e-commerce. Paste the relevant bodies in together under headings. Beyond about three,
the instructions start to dilute; better to work one domain at a time and follow the
`## Hand off to` list at the end of each agent.

## Option 2 — tools with subagent support

Some tools read a directory of agent files and route to them automatically based on each agent's
`description`. Copy the files into whichever directory your tool uses.

```bash
git clone https://github.com/prnzka/philippine-business-agents.git
cd philippine-business-agents
```

The category folders are for browsing. Agent files are flat `.md` files, so copy them out:

```bash
# everything, available everywhere
mkdir -p ~/.claude/agents
cp categories/*/*.md ~/.claude/agents/
```

PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\agents"
Get-ChildItem categories -Recurse -Filter *.md | Copy-Item -Destination "$env:USERPROFILE\.claude\agents"
```

> The `~/.claude/agents/` path above is the convention used by Claude Code, which is one tool that
> reads this layout. Substitute the directory your own tool uses — check its documentation for
> where it looks for agent or persona files. The agent files themselves are the same either way.

### Install a subset instead

Installing the whole library gives the model a long list to route across. If you only need one or
two domains, install those:

```bash
mkdir -p .claude/agents
cp categories/01-tax-and-bir/*.md .claude/agents/
cp categories/03-people-and-labor/*.md .claude/agents/
```

A practical starter set for most small businesses:

```bash
cp categories/01-tax-and-bir/income-tax-strategist.md \
   categories/01-tax-and-bir/bir-registration-specialist.md \
   categories/01-tax-and-bir/tax-calendar-manager.md \
   categories/02-registration-and-permits/lgu-permits-navigator.md \
   categories/03-people-and-labor/payroll-and-statutory-contributions.md \
   categories/03-people-and-labor/worker-classification-advisor.md \
   categories/04-finance-and-accounting/cash-flow-manager.md \
   categories/04-finance-and-accounting/pricing-and-margin-analyst.md \
   .claude/agents/
```

Then add the one or two sector agents that match the business.

## Option 3 — build them into your own product

If you are building an assistant for Philippine businesses, the agent bodies work as system
prompts in any API. The MIT licence permits commercial use.

A few notes if you do:

- The `description` field is written as a **routing signal** — it names the concrete situations in
  which the agent applies. It is designed to be fed to a router or classifier.
- The `## Verify-before-advising` section names the figures the agent must not assert from memory.
  If your product has web access or a data source, wire it to those checks.
- The `## Hand off to` list is a dependency graph between agents. `scripts/validate_agents.py`
  parses it, and you can use the same parse to build a routing map.
- The `## Limits` section is the refusal and escalation boundary. Keep it.

## Finding the right agent

```bash
# every agent and what it is for
grep -h -A3 '^name:' categories/*/*.md | less

# agents that mention a topic
grep -l -i "minimum wage" categories/*/*.md
grep -l -i "fda" categories/*/*.md
```

Or read the grouped index in the [README](../README.md#the-agents) — functional agents for running
any business, sector agents for the business you are in.

## Giving an agent your actual numbers

These agents are most useful with real data. They will ask for it, and it helps to have it ready:

- **Tax and finance agents** — the BIR Certificate of Registration, the last two years of returns,
  twelve months of monthly sales and expenses, bank and e-wallet statements.
- **Payroll and labour agents** — headcount by status, the pay structure, the region (for the wage
  order), and the current contribution computation.
- **E-commerce agents** — the platform seller centre reports, which carry the fee breakdown that
  makes channel margin computable.
- **Pricing agents** — the full cost build, including the costs you are not currently counting.
- **Sector agents** — the licence or permit you hold, and the one you have been told you need.

Agents that compute carry a `Bash` tool in their header so a capable tool can let them build the
model rather than estimate. With a plain chat assistant, ask it to show the arithmetic.

## Adapting an agent

These are prompts. Edit them.

Common adaptations:

- **Add your firm's own process** to the `## Deliverables` section so the output matches your
  templates.
- **Narrow the scope** — an agent for one LGU, one industry, or one client's situation.
- **Translate the owner-facing deliverables** into Filipino or Cebuano while keeping the
  instructions in English.
- **Drop or change the header.** `tools` and `model` are conventions of the tools that read them;
  other runtimes ignore them. The `model` values in this repository name model tiers from one
  common convention — substitute your own, or remove the field.

Keep the `## Verify-before-advising` and `## Limits` sections. They are what stop an agent from
confidently quoting a figure that changed last quarter, or from drafting something that needs a
licensed professional's signature.

## Keeping up to date

Philippine rates, thresholds and wage orders change, and so do these files.

```bash
cd philippine-business-agents && git pull
```

Then re-copy the agents you installed. If an agent gave you a figure that has since changed, that
is the repository drifting — please open an issue with the primary source. See
[CONTRIBUTING.md](../CONTRIBUTING.md).
