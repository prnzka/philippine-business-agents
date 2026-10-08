# Contributing

## The most valuable contribution: corrections

Philippine regulation moves. Revenue regulations supersede each other, contribution rates follow
legislated schedules, wage orders are issued and sometimes enjoined, and agencies reorganise
which of them handles what.

**If an agent cites a superseded rule, a wrong threshold, or the wrong agency, please say so.**
Open an issue or a PR with the primary source — the RR number, the circular, the agency page.
That is worth more than a new agent.

Please do not submit a correction sourced from a blog or an SEO guide. Those are the reason the
error exists.

## Adding an agent

1. Read [`docs/AGENT_STANDARD.md`](docs/AGENT_STANDARD.md) first. It is the contract every file
   follows, including the two mandatory sections.
2. Check the [README index](../README.md#the-agents) for overlap. Extending an existing agent is
   usually better than adding a near-duplicate.
3. Put the file in the category folder it belongs to. Name it `kebab-case.md`, and make the
   frontmatter `name` identical to the filename without the extension.
4. Write a `description` that is a **routing signal** — the concrete situations in which this
   agent should be chosen. It is read by the orchestrator model, not by a human browsing.
5. Include every required section. `## Verify-before-advising` and `## Limits` are not optional.
6. Update the README index — or run the index generator if you have one; a maintainer will
   regenerate it either way.

### What gets a PR rejected

- **Generic advice with "Philippines" pasted on.** If the body would read identically for a US
  business, it does not belong here. The Philippine specifics — the RA number, the form, the
  agency, the local practice — are the entire value.
- **Hardcoded rates presented as current fact**, without a `## Verify-before-advising` entry.
- **Advice that requires a professional's signature**, without saying so.
- **Anything that helps a user break the law.** Splitting entities to stay under the VAT
  threshold, nominee arrangements for foreign equity, misdeclaring customs value, fake reviews,
  forced resignations, selling unregistered FDA products. An agent should name the exposure and
  offer the lawful route.
- **An agent that overlaps an existing one** without a clear reason the split is useful.

## Agents that would be welcome

The library is still growing. Sectors not yet covered, roughly in order of how many Philippine
businesses they would serve:

- **Mining and quarrying** — MGB permits, and the LGU-level quarrying that is far more common
- **Telecoms, ISPs and cable** — NTC permits, and the small community ISP model
- **Funeral and memorial services** — a large, regulated and entirely uncovered sector
- **Pre-need plans** beyond distribution — the Pre-Need Code and the trust fund obligations
- **Shipping, ports and freight forwarding** — MARINA, PPA, and customs brokerage as a practice
- **Gaming, amusement and e-sports** — PAGCOR and LGU amusement regulation
- **Private hospitals, dialysis and elder care** — DOH licensing at facility scale
- **Broadcast and film production** — MTRCB, NTC, and production incentives
- **Sports and entertainment management** — talent, events and the labour side
- **Religious and non-profit organisations** — SEC non-stock registration, donee institution
  status, and the tax treatment of donations
- **Crypto and virtual asset services** beyond the BSP licensing summary
- **Franchise brokerage and business brokering**

Other useful work:

- **Regional specifics.** Most of this repository is accurate nationally but Metro Manila-shaped.
  Agents or sections covering Cebu, Davao, Iloilo, Cagayan de Oro and BARMM specifics would
  genuinely improve it.
- **Filipino and Cebuano versions of the owner-facing deliverables** — the checklists, the staff
  briefings, the policy summaries. The agent instructions stay in English; the output that reaches
  a worker or a store owner should be in their language.
- **Worked examples** with real (anonymised) numbers.
- **Testing agents against other models.** These are written to be model-agnostic, but they are
  mostly exercised on one. If an agent behaves badly on a model you use — ignores the
  verification section, drops the limits, over-asserts a figure — that is a useful issue to open.

## Style

- Instructions in English. Use the Filipino or Taglish term where it is the actual vocabulary of
  the thing, and gloss it once. Do not translate for decoration.
- Write for a competent practitioner. Short sentences, concrete nouns, no filler.
- Name the law, the form, the agency, the threshold. Specificity is the product.
- Tables and decision trees over prose where the content is a decision.
- An agent should be prepared to say "do not do this" and "this needs a lawyer."

## Checks before you open a PR

```bash
# frontmatter name matches the filename
for f in categories/*/*.md; do
  n=$(grep -m1 '^name:' "$f" | sed 's/name: *//')
  b=$(basename "$f" .md)
  [ "$n" = "$b" ] || echo "MISMATCH: $f ($n)"
done

# the two mandatory sections are present
grep -L "## Verify-before-advising" categories/*/*.md
grep -L "## Limits" categories/*/*.md

# every agent referenced in a "Hand off to" section exists
```

A maintainer runs a validator that checks the above plus that every `## Hand off to` reference
resolves to an agent in the repository. Broken references will be flagged.

## Code of conduct

Be straightforward and useful. Disagree about substance, with sources. Nobody here is obliged to
anybody's time.
