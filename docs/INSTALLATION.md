# Installation and use

## Where agent files go

Claude Code reads subagents from two locations:

| Location | Scope |
| --- | --- |
| `.claude/agents/` in a project | That project only. Takes precedence on a name clash. |
| `~/.claude/agents/` (`%USERPROFILE%\.claude\agents\` on Windows) | Every project for your user |

Agent files are flat `.md` files in those directories — the category folders in this repository
are for browsing, not for installation. Copy the files out of them.

## Install everything

```bash
git clone https://github.com/prnzka/philippine-business-subagents.git
cd philippine-business-subagents

# user-wide
mkdir -p ~/.claude/agents
cp categories/*/*.md ~/.claude/agents/
```

PowerShell:

```powershell
git clone https://github.com/prnzka/philippine-business-subagents.git
cd philippine-business-subagents
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\agents"
Get-ChildItem categories -Recurse -Filter *.md | Copy-Item -Destination "$env:USERPROFILE\.claude\agents"
```

## Install a subset

Installing all 71 gives Claude a long list to route across. If you only need one domain, install
that category:

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

## Using them

**Let Claude route.** Each agent's `description` says when it applies. Describe your situation and
Claude picks:

```
Gross ko last year 2.4M, freelance web design, konti lang expenses. 8% or graduated?
```

**Or name the agent:**

```
Use the pricing-and-margin-analyst to check whether my Shopee listings are profitable.
```

**Check what is installed** with `/agents` in Claude Code, which also lets you create and edit
agents interactively.

## Verify what these agents hold

```bash
# list every agent with its description
grep -h -A2 '^name:' categories/*/*.md | head -50

# find the agents covering a topic
grep -l -i "minimum wage" categories/*/*.md
```

## Giving an agent your actual numbers

These agents are most useful with real data. They will ask for it, and it helps to have it ready:

- **Tax and finance agents** — the BIR Certificate of Registration, the last two years of returns,
  twelve months of monthly sales and expenses, bank and e-wallet statements.
- **Payroll and labour agents** — headcount by status, the pay structure, the region (for the wage
  order), and the current contribution computation.
- **E-commerce agents** — the platform seller centre reports, which carry the fee breakdown that
  makes channel margin computable.
- **Pricing agents** — the full cost build, including the costs you are not currently counting.

Agents that compute are granted the `Bash` tool so they can build the model rather than estimate.

## Adapting an agent

These are plain Markdown prompts. Edit them.

Common adaptations:

- **Add your firm's own process** to the `## Deliverables` section so the output matches your
  templates.
- **Narrow the scope** — an agent for one LGU, one industry, or one client's situation.
- **Change the model** in the frontmatter. `opus` for the legal and multi-variable agents,
  `sonnet` for most, `haiku` if you only want lookups.
- **Tighten the tools.** Most advisory agents need only `Read, Write, Edit, WebSearch, WebFetch`.

Keep the `## Verify-before-advising` and `## Limits` sections. They are what stop an agent from
confidently quoting a figure that changed last quarter, or from drafting something that needs a
professional's signature.

## Not using Claude Code

The agent bodies are provider-agnostic Markdown. Strip the YAML frontmatter and use the body as a
system prompt in any assistant, or as a reference document. The frontmatter's `tools` and `model`
fields are Claude Code conventions.
