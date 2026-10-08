# Philippine Business Subagents

**71 production-ready Claude Code subagents for running a business in the Philippines.**

Most AI business advice is written for a US company. It will tell a Filipino owner to form an
LLC, file a 1099, and watch their Q4 sales — none of which exist here. What exists here is
BIR Form 1701Q, the 8% gross receipts option, a barangay clearance before a mayor's permit,
13th month pay due on 24 December, a wage order that a court might have enjoined last month,
and a customer who wants to ask three questions on Messenger before they buy.

This repository is a set of specialist agents that know that. Each one covers a single domain of
Philippine business practice — citing the republic act, the BIR form, the agency, and the
threshold — and each one is built to **verify volatile figures before quoting them**, because
Philippine rates and wage orders change mid-year.

> **Not professional advice.** These agents prepare, model, draft and explain. A CPA signs
> returns, a lawyer signs contracts, a licensed professional signs plans. Every agent says so in
> its own `## Limits` section, and says it to the user too. See [DISCLAIMER.md](DISCLAIMER.md).

---

## Who this is for

- **Business owners** — from a sari-sari store to a 200-seat BPO — who want a competent second
  opinion on tax, permits, labour, pricing and growth.
- **Accountants, bookkeepers and VAs** serving Philippine SMEs, who need the structure and the
  checklists without re-deriving them each time.
- **Developers and consultants** building tools for the Philippine market.
- **Anyone starting a business here** who does not yet know which of the twelve agencies applies
  to them. Start with [`regulatory-licence-mapper`](categories/02-registration-and-permits/regulatory-licence-mapper.md).

## Quick start

Copy the agents you want into your project's or user's agents directory:

```bash
git clone https://github.com/prnzka/philippine-business-subagents.git

# all of them, for your user account
mkdir -p ~/.claude/agents
cp philippine-business-subagents/categories/*/*.md ~/.claude/agents/

# or just the tax ones, for one project
mkdir -p .claude/agents
cp philippine-business-subagents/categories/01-tax-and-bir/*.md .claude/agents/
```

Then ask in plain language — Claude routes to the right agent from its `description`:

```
Gross ko last year 2.4M, freelance web design, konti lang expenses. 8% or graduated?
Should I register for VAT? My customers are all corporate.
My Shopee sales are up 40% but I have no cash. Where is it going?
I want to open a second branch in Cebu. Walk me through it.
I got a Letter of Authority from the BIR this morning.
```

Full setup, including how to invoke an agent by name and how to adapt one, is in
[`docs/INSTALLATION.md`](docs/INSTALLATION.md).

## What makes these different

**They verify instead of asserting.** Every agent has a mandatory `## Verify-before-advising`
section listing the figures it must re-check and the primary source for each. Philippine
contribution rates, tax thresholds and minimum wages change — NCR wage orders have been issued in
tranches and then enjoined by a court mid-effectivity. An agent that confidently quotes last
year's figure is worse than no agent, so these treat every peso amount in their own prompt as
*last-known, not current*. The source list is in
[`docs/PRIMARY_SOURCES.md`](docs/PRIMARY_SOURCES.md).

**They name the law.** RA 11976 for the invoicing change, RA 9178 for the BMBE exemption,
RA 11058 for the safety programme, RA 11967 for online seller liability, RA 12009 for government
procurement, CA 108 for why nominee shareholdings are a criminal matter. An owner can check the
agent's work.

**They know where the money actually leaks.** The free-shipping contribution that is larger than
the marketplace commission. The expense disallowed entirely because a small withholding was
missed. The 13th month pay nobody accrued for. The empty backhaul. The lista with no limit. The
personal GCash account that makes the books unauditable and the business unbankable.

**They say no.** An agent that will not tell an owner their business is not ready to franchise,
not ready to expand, or not worth what they think, is not useful. Several of these are built to
deliver that answer, with the reason.

**They refuse the shortcuts.** Splitting a business to stay under the VAT threshold, nominee
arrangements to dodge foreign equity caps, misdeclaring an HS code, fake marketplace reviews,
forced resignations, unregistered FDA products on a live sell. Each agent names the exposure and
offers the lawful route instead.

---

## The agents

### Tax & BIR

`categories/01-tax-and-bir/` — 7 agents

| Agent | Use it for |
| --- | --- |
| [`bir-audit-defense`](categories/01-tax-and-bir/bir-audit-defense.md) | A client receives a Letter of Authority, Letter Notice, Notice of Discrepancy, Preliminary Assessment Notice, Final Assessment Notice or Warrant of Distraint and Levy, when a Subpoena Duces Tecum arrives, or when an owner wants to… |
| [`bir-registration-specialist`](categories/01-tax-and-bir/bir-registration-specialist.md) | A business needs to register with the BIR for the first time, update its registration (change of address, line of business, tax type, RDO transfer), register a branch, apply for Authority to Print or a POS/CAS permit, or retire a… |
| [`bookkeeping-and-invoicing`](categories/01-tax-and-bir/bookkeeping-and-invoicing.md) | Set up or clean up BIR-compliant books of account, design an invoice and receipt workflow under the EOPT invoicing rules, build a monthly closing routine, reconstruct back books before an audit, or decide between manual, loose-leaf and… |
| [`income-tax-strategist`](categories/01-tax-and-bir/income-tax-strategist.md) | Choose between the 8% gross receipts option and graduated rates, to compare OSD against itemised deductions, to evaluate BMBE or other exemptions, to plan the timing of income across years, or whenever an owner asks why their tax bill… |
| [`tax-calendar-manager`](categories/01-tax-and-bir/tax-calendar-manager.md) | Build and maintain a BIR, SEC, LGU and statutory-contribution filing calendar for a specific business, to diagnose open cases and stop-filer notices, to plan the year-end and annual-renewal season, or to catch up on missed filings and… |
| [`vat-and-percentage-tax-specialist`](categories/01-tax-and-bir/vat-and-percentage-tax-specialist.md) | Anything touching VAT or percentage tax — deciding whether to register for VAT, handling the crossing of the VAT threshold, input tax substantiation and refunds, zero-rated and exempt sales, VAT on digital services, or preparing and… |
| [`withholding-tax-specialist`](categories/01-tax-and-bir/withholding-tax-specialist.md) | Expanded withholding tax on supplier payments, withholding tax on compensation, final withholding on dividends, royalties and payments to non-residents, the 1% marketplace withholding on online sellers, and the handling of Form 2307 and… |

### Registration & Permits

`categories/02-registration-and-permits/` — 6 agents

| Agent | Use it for |
| --- | --- |
| [`bmbe-and-msme-incentives`](categories/02-registration-and-permits/bmbe-and-msme-incentives.md) | Assess BMBE eligibility under RA 9178 and secure the Certificate of Authority, to map the DTI, DOST, TESDA and Negosyo Center support a micro or small enterprise can claim, to check MSME classification for procurement and lending, or to… |
| [`business-structure-advisor`](categories/02-registration-and-permits/business-structure-advisor.md) | Choose between a sole proprietorship, partnership, One Person Corporation, stock corporation and cooperative, to decide when to incorporate an existing sole prop, to structure ownership between co-founders, or to assess foreign… |
| [`dti-sec-registration-specialist`](categories/02-registration-and-permits/dti-sec-registration-specialist.md) | Register a business name with DTI, incorporate through SEC eSPARC or OneSEC, register a cooperative with the CDA, prepare articles of incorporation and by-laws, handle SEC amendments and annual filings, or fix a rejected name or… |
| [`foreign-ownership-advisor`](categories/02-registration-and-permits/foreign-ownership-advisor.md) | A foreign national or foreign company wants to own or invest in a Philippine business, when a Filipino owner is taking in foreign equity, to check the Foreign Investment Negative List and sector caps, to choose between a subsidiary,… |
| [`lgu-permits-navigator`](categories/02-registration-and-permits/lgu-permits-navigator.md) | Barangay clearance, mayor's or business permit applications and January renewals, zoning and locational clearance, fire safety inspection certificates, sanitary permits, local business tax assessment and disputes, and for invoking RA… |
| [`regulatory-licence-mapper`](categories/02-registration-and-permits/regulatory-licence-mapper.md) | Find out which national regulators a proposed Philippine business must clear before it can legally operate — FDA, DOH, DA, PCAB, DHSUD, PRC, LTFRB, DOT, BSP, SEC secondary licences, NTC, DENR and others — and to sequence those approvals… |

### People & Labour

`categories/03-people-and-labor/` — 9 agents

| Agent | Use it for |
| --- | --- |
| [`discipline-and-termination-advisor`](categories/03-people-and-labor/discipline-and-termination-advisor.md) | Use this agent before disciplining or dismissing a Philippine employee — to identify the lawful ground, run the twin-notice due process correctly, draft the notices and decision, compute separation pay, handle redundancy or retrenchment… |
| [`dole-compliance-auditor`](categories/03-people-and-labor/dole-compliance-auditor.md) | Self-audit against Philippine labour standards before a DOLE inspection, to respond to a Notice of Results or compliance order from a labour inspection, to build an occupational safety and health programme under RA 11058, or to prepare… |
| [`hiring-and-employment-contracts`](categories/03-people-and-labor/hiring-and-employment-contracts.md) | Draft Philippine employment contracts, set up probationary employment with enforceable standards, structure project-based, fixed-term, part-time and seasonal engagements, write job offers and job descriptions, or handle the employment… |
| [`hr-policy-and-handbook-writer`](categories/03-people-and-labor/hr-policy-and-handbook-writer.md) | Write a Philippine employee handbook, a code of conduct with a schedule of offences and penalties, an attendance and leave policy, an anti-sexual harassment and Safe Spaces policy, a telecommuting policy, or the mandatory workplace… |
| [`payroll-and-statutory-contributions`](categories/03-people-and-labor/payroll-and-statutory-contributions.md) | Build or audit a Philippine payroll — SSS, PhilHealth and Pag-IBIG computation and remittance, withholding tax on compensation, 13th month pay, holiday and night differential and overtime premiums, final pay on separation, and the… |
| [`recruitment-and-retention-specialist`](categories/03-people-and-labor/recruitment-and-retention-specialist.md) | Hire in the Philippine labour market — sourcing channels, compensation benchmarking, interviewing and assessment, handling counter-offers and ghosting, onboarding, and reducing the turnover that costs SMEs more than their payroll error… |
| [`remote-team-and-gig-manager`](categories/03-people-and-labor/remote-team-and-gig-manager.md) | Manage remote and hybrid teams in the Philippines under the Telecommuting Act, to engage Filipino workers for offshore clients, to work with gig and platform workers such as riders and online freelancers, or to build the management… |
| [`worker-classification-advisor`](categories/03-people-and-labor/worker-classification-advisor.md) | Ever a Philippine business pays someone as a freelancer, consultant, contractor, commission agent, "pakyaw" worker or virtual assistant, when engaging a manpower agency or subcontractor, or when assessing exposure from workers who have… |
| [`workplace-safety-officer`](categories/03-people-and-labor/workplace-safety-officer.md) | Build an occupational safety and health programme under RA 11058 and DO 198, determine the safety officer and committee requirements for an establishment, run a hazard assessment, handle a work accident and its reporting, or prepare for… |

### Finance & Accounting

`categories/04-finance-and-accounting/` — 5 agents

| Agent | Use it for |
| --- | --- |
| [`budgeting-and-forecasting`](categories/04-finance-and-accounting/budgeting-and-forecasting.md) | Build an annual budget for a Philippine SME, create a driver-based financial model, forecast with Philippine seasonality and inflation, run scenarios for expansion or a cost shock, or set up a monthly variance review the owner will… |
| [`cash-flow-manager`](categories/04-finance-and-accounting/cash-flow-manager.md) | Build a Philippine SME cash flow forecast, diagnose why a profitable business has no cash, plan for the December and January obligation cluster, manage the gap between marketplace payout cycles and supplier terms, or triage a business… |
| [`collections-and-receivables`](categories/04-finance-and-accounting/collections-and-receivables.md) | Set credit terms for Philippine customers, build a collections process, recover overdue accounts including from corporate and government payors, handle the informal "lista" and utang culture in retail, or decide when to escalate to… |
| [`financial-statements-specialist`](categories/04-finance-and-accounting/financial-statements-specialist.md) | Prepare Philippine financial statements under PFRS for SMEs or PFRS for Small Entities, assemble the audited financial statements pack for BIR and SEC filing, reconcile statements filed with different agencies, prepare statements a bank… |
| [`pricing-and-margin-analyst`](categories/04-finance-and-accounting/pricing-and-margin-analyst.md) | Price a product or service for the Philippine market, compute true landed and fully loaded costs, work out whether a marketplace or reseller channel is actually profitable after fees, decide how to absorb a cost increase, or diagnose… |

### Sales & Marketing

`categories/05-sales-and-marketing/` — 6 agents

| Agent | Use it for |
| --- | --- |
| [`b2b-and-government-sales`](categories/05-sales-and-marketing/b2b-and-government-sales.md) | Sell to Philippine corporates and government — PhilGEPS registration and public bidding under RA 12009, accreditation as a corporate supplier, proposals and quotations, the billing pack that gets paid, and deciding whether a government… |
| [`customer-service-and-retention`](categories/05-sales-and-marketing/customer-service-and-retention.md) | Build a Philippine customer service operation across Messenger, Viber, marketplace chat and phone, handle complaints and refunds under the Consumer Act and the Internet Transactions Act, manage reviews and ratings, or build repeat… |
| [`filipino-consumer-insights`](categories/05-sales-and-marketing/filipino-consumer-insights.md) | Understand how Filipino consumers actually decide and buy — segmentation by income class and region, the sachet and tingi economy, payday and remittance cycles, social proof and group decision-making, and what differs between Metro… |
| [`meta-ads-strategist`](categories/05-sales-and-marketing/meta-ads-strategist.md) | Plan and run Facebook, Instagram and Messenger advertising for a Philippine business — campaign structure, Messenger-first funnels, budget allocation in pesos, creative testing, audience targeting for Philippine segments, and diagnosing… |
| [`taglish-copywriter`](categories/05-sales-and-marketing/taglish-copywriter.md) | Write Philippine marketing copy — Facebook and TikTok ad copy, Messenger scripts, product listings, SMS and Viber broadcasts, landing pages and email — in English, Filipino or Taglish, pitched to a specific segment rather than to a… |
| [`tiktok-and-live-selling-strategist`](categories/05-sales-and-marketing/tiktok-and-live-selling-strategist.md) | TikTok content and TikTok Shop strategy in the Philippines, running live selling sessions on TikTok or Facebook, building an affiliate and creator programme, or deciding whether live selling fits a business at all. |

### E-commerce & Online Selling

`categories/06-ecommerce-and-online-selling/` — 4 agents

| Agent | Use it for |
| --- | --- |
| [`ecommerce-logistics-and-fulfilment`](categories/06-ecommerce-and-online-selling/ecommerce-logistics-and-fulfilment.md) | Choose couriers and negotiate rates in the Philippines, design a packing and dispatch operation, manage COD and failed deliveries, handle inter-island and remote-area shipping, decide between self-fulfilment and a platform fulfilment… |
| [`ecommerce-tax-compliance`](categories/06-ecommerce-and-online-selling/ecommerce-tax-compliance.md) | The tax and regulatory compliance of selling online in the Philippines — BIR registration for online sellers, the 1% marketplace withholding under RR 16-2023, invoicing for online orders, VAT on digital services and marketplace fees,… |
| [`marketplace-seller-strategist`](categories/06-ecommerce-and-online-selling/marketplace-seller-strategist.md) | Launch or improve a Shopee, Lazada or TikTok Shop store in the Philippines — listing optimisation, fee and margin analysis, campaign and voucher participation, shop ratings and seller tier, platform ads, and deciding which platforms a… |
| [`online-store-and-payments`](categories/06-ecommerce-and-online-selling/online-store-and-payments.md) | Build a direct online store for a Philippine business, choose and integrate payment methods (GCash, Maya, QR Ph, cards, bank transfer, COD), select a payment gateway, reduce checkout abandonment, or decide whether a direct channel is… |

### Operations & Supply Chain

`categories/07-operations-and-supply-chain/` — 4 agents

| Agent | Use it for |
| --- | --- |
| [`inventory-and-procurement`](categories/07-operations-and-supply-chain/inventory-and-procurement.md) | Set reorder points and safety stock for a Philippine business, fix stock accuracy and overselling across channels, reduce shrinkage and expiry, manage multi-channel stock allocation, or free up the cash locked in slow-moving inventory. |
| [`sari-sari-and-retail-operations`](categories/07-operations-and-supply-chain/sari-sari-and-retail-operations.md) | Philippine neighbourhood and small-format retail — sari-sari stores, mini-groceries, market stalls and small shops. Covers product mix, tingi repacking, the lista credit ledger, supplier and distributor relationships, store layout,… |
| [`sop-and-quality-builder`](categories/07-operations-and-supply-chain/sop-and-quality-builder.md) | Document standard operating procedures for a Philippine SME, build a quality control process, prepare for ISO or HACCP certification, create training materials for frontline staff, or make a business run without the owner present. |
| [`supplier-sourcing-advisor`](categories/07-operations-and-supply-chain/supplier-sourcing-advisor.md) | Find and qualify suppliers for a Philippine business — Divisoria and local wholesale markets, local manufacturers, importing from China via 1688 and Alibaba, OEM and private label arrangements, supplier negotiation, and avoiding the… |

### Legal & Compliance

`categories/08-legal-and-compliance/` — 5 agents

| Agent | Use it for |
| --- | --- |
| [`consumer-protection-advisor`](categories/08-legal-and-compliance/consumer-protection-advisor.md) | Philippine consumer protection compliance — Consumer Act obligations on warranty, labelling, pricing and advertising, the Internet Transactions Act for online sellers, DTI sales promotion permits, responding to a DTI consumer complaint,… |
| [`contracts-and-agreements-drafter`](categories/08-legal-and-compliance/contracts-and-agreements-drafter.md) | Draft Philippine commercial agreements — service agreements, supply and distribution contracts, leases, non-disclosure agreements, founders' and shareholders' agreements, consultancy and contractor agreements, and terms of sale — for… |
| [`data-privacy-compliance-officer`](categories/08-legal-and-compliance/data-privacy-compliance-officer.md) | Data Privacy Act compliance in the Philippines — determining whether NPC registration is required, designating and equipping a DPO, writing privacy notices and consent mechanisms, building the records of processing, handling a data… |
| [`dispute-resolution-advisor`](categories/08-legal-and-compliance/dispute-resolution-advisor.md) | A Philippine business is in a dispute — with a customer, supplier, landlord, partner or employee. Covers barangay conciliation, small claims court, demand letters, mediation and arbitration, bounced cheques under BP 22, and deciding… |
| [`trademark-and-ip-specialist`](categories/08-legal-and-compliance/trademark-and-ip-specialist.md) | Register a trademark with IPOPHL, clear a brand name before launch, respond to an opposition or an infringement claim, handle copyright and trade secrets, file a Declaration of Actual Use, or deal with counterfeits of the client's product. |

### Industry Verticals

`categories/09-industry-verticals/` — 8 agents

| Agent | Use it for |
| --- | --- |
| [`agribusiness-advisor`](categories/09-industry-verticals/agribusiness-advisor.md) | Philippine agriculture and agribusiness — farm enterprise planning, post-harvest and value-adding, cooperatives and consolidation, DA and FPA registrations, organic certification, crop and livestock financing through ACPC and Landbank,… |
| [`bpo-and-outsourcing-advisor`](categories/09-industry-verticals/bpo-and-outsourcing-advisor.md) | Build or run a Philippine BPO, call centre, virtual assistant agency or outsourced services business — pricing offshore services, PEZA or BOI registration, night shift and 24/7 labour compliance, client contracts and SLAs, data security… |
| [`construction-business-advisor`](categories/09-industry-verticals/construction-business-advisor.md) | Philippine construction and contracting businesses — PCAB licensing and categories, bidding and estimating, construction contracts and retention, progress billing and cash flow, construction safety under DOLE DO 13, subcontractor… |
| [`food-safety-and-fda-compliance`](categories/09-industry-verticals/food-safety-and-fda-compliance.md) | Philippine FDA compliance on food, cosmetics, supplements, medical devices and household hazardous substances — Licence to Operate, Certificate of Product Registration, labelling, permissible claims, GMP and HACCP, importation, and… |
| [`food-service-operations`](categories/09-industry-verticals/food-service-operations.md) | Philippine food businesses — carinderia, restaurant, café, food cart, catering, cloud kitchen and commissary. Covers permits and sanitary requirements, food cost and menu engineering, kitchen operations, delivery platform economics, and… |
| [`real-estate-and-leasing-advisor`](categories/09-industry-verticals/real-estate-and-leasing-advisor.md) | Philippine property matters in a business context — negotiating and reviewing commercial leases, evaluating a site, buying or selling property and the taxes involved, running a rental or boarding house business, subdivision and… |
| [`tourism-and-hospitality-business`](categories/09-industry-verticals/tourism-and-hospitality-business.md) | Philippine tourism and hospitality businesses — resorts, hotels, homestays and short-term rentals, tour operators and travel agencies, dive and adventure operators. Covers DOT accreditation, LGU and environmental requirements,… |
| [`transport-and-logistics-business`](categories/09-industry-verticals/transport-and-logistics-business.md) | Philippine transport and logistics businesses — trucking and delivery fleets, LTFRB franchises for public transport and TNVS, courier and last-mile operations, warehousing, freight forwarding, and the driver employment and vehicle… |

### Growth & Funding

`categories/10-growth-and-funding/` — 6 agents

| Agent | Use it for |
| --- | --- |
| [`business-plan-writer`](categories/10-growth-and-funding/business-plan-writer.md) | Write a business plan for a Philippine SME — for a lender, a government programme, an investor, or for the owner's own decision-making. Also use to pressure-test an existing plan or to write a feasibility study. |
| [`business-valuation-and-exit-advisor`](categories/10-growth-and-funding/business-valuation-and-exit-advisor.md) | Value a Philippine SME, prepare it for sale, structure a share sale or an asset sale and understand the tax difference, hand a business to the next generation, bring in or buy out a partner, or wind a business down properly. |
| [`expansion-and-branch-strategist`](categories/10-growth-and-funding/expansion-and-branch-strategist.md) | Decide whether and how a Philippine business should open a second location, expand to another city or region, add a product line or channel, or scale operations — including the registration, tax and labour consequences of a branch, and… |
| [`franchise-developer`](categories/10-growth-and-funding/franchise-developer.md) | Franchise a Philippine business or to evaluate buying a franchise — the EO 169 minimum terms for MSME franchisees, disclosure practice, franchise fees and royalties, the operations manual and training system, territory and site… |
| [`investor-pitch-and-fundraising`](categories/10-growth-and-funding/investor-pitch-and-fundraising.md) | Raise equity for a Philippine business — pitch deck and data room, valuation and deal structure, the Philippine angel and VC landscape, term sheets and shareholder agreements, due diligence readiness, and whether raising equity is the… |
| [`msme-loan-navigator`](categories/10-growth-and-funding/msme-loan-navigator.md) | Find and compare financing for a Philippine SME — bank term loans and credit lines, SB Corporation and government programme lending, Landbank and DBP, microfinance, cooperative credit, invoice and purchase order financing, and the… |

### Technology & Digital

`categories/11-technology-and-digital/` — 5 agents

| Agent | Use it for |
| --- | --- |
| [`automation-and-ai-advisor`](categories/11-technology-and-digital/automation-and-ai-advisor.md) | Find where a Philippine SME should automate or apply AI — chat response, bookkeeping data entry, inventory updates, content production, customer follow-up — and where automation is the wrong answer because labour is cheap and the… |
| [`cybersecurity-for-smes`](categories/11-technology-and-digital/cybersecurity-for-smes.md) | Protect a Philippine small business from the attacks it actually faces — account takeover on Facebook and e-wallets, business email compromise and supplier payment fraud, online scams against customers using the brand, ransomware, and… |
| [`data-and-analytics-for-sme`](categories/11-technology-and-digital/data-and-analytics-for-sme.md) | Work out which few numbers a Philippine SME should actually track, build a simple dashboard or report from the data the business already has, analyse sales and customer data, or replace gut-feel decisions with evidence the owner can see… |
| [`small-business-systems-advisor`](categories/11-technology-and-digital/small-business-systems-advisor.md) | Choose and implement the software a Philippine SME actually needs — POS, accounting, inventory, payroll, CRM — including BIR requirements for computerised systems, and to decide what to keep on paper or a spreadsheet instead. |
| [`website-and-seo-advisor`](categories/11-technology-and-digital/website-and-seo-advisor.md) | Decide whether a Philippine business needs a website, build one that converts on a mobile connection, rank for local and Philippine search, set up Google Business Profile for a physical location, or diagnose a site that gets traffic but… |

### Exports & Global Market

`categories/12-exports-and-global-market/` — 6 agents

| Agent | Use it for |
| --- | --- |
| [`cross-border-payments-advisor`](categories/12-exports-and-global-market/cross-border-payments-advisor.md) | Receive payments from abroad or pay foreign suppliers from the Philippines — comparing Wise, Payoneer, PayPal, banks and remittance channels on true cost, managing FX exposure, BSP registration of foreign investment, and the tax… |
| [`export-readiness-advisor`](categories/12-exports-and-global-market/export-readiness-advisor.md) | Assess whether a Philippine business is ready to export, navigate exporter registration and documentation, meet destination-market requirements and certifications, price for export, find buyers, and use DTI, CITEM and FTA advantages. |
| [`freelancer-and-digital-nomad-tax`](categories/12-exports-and-global-market/freelancer-and-digital-nomad-tax.md) | Philippine-based freelancers, virtual assistants, online professionals and consultants with foreign clients — BIR registration, the 8% versus graduated choice, invoicing foreign clients, VAT zero-rating on service exports, and the tax… |
| [`import-and-customs-navigator`](categories/12-exports-and-global-market/import-and-customs-navigator.md) | Import into the Philippines — importer accreditation and CPRS, HS classification and duty, VAT on importation, customs clearance and brokers, landed cost computation, regulated and restricted goods, and resolving a shipment held at customs. |
| [`ofw-and-diaspora-market`](categories/12-exports-and-global-market/ofw-and-diaspora-market.md) | Sell to Overseas Filipino Workers and the Filipino diaspora, to build a business serving remittance-receiving households in the Philippines, or to help an OFW set up a Philippine business from abroad — including the specific failure… |
| [`peza-boi-incentives-advisor`](categories/12-exports-and-global-market/peza-boi-incentives-advisor.md) | Assess PEZA and BOI registration for a Philippine enterprise — the CREATE and CREATE MORE incentive regimes, the income tax holiday followed by the enhanced deduction regime or the special rate on gross income, export thresholds and… |
---

## Common starting points

| Situation | Start here |
| --- | --- |
| Starting a business, do not know what is required | [`regulatory-licence-mapper`](categories/02-registration-and-permits/regulatory-licence-mapper.md) → [`business-structure-advisor`](categories/02-registration-and-permits/business-structure-advisor.md) → [`lgu-permits-navigator`](categories/02-registration-and-permits/lgu-permits-navigator.md) |
| Freelancer with foreign clients, not registered | [`freelancer-and-digital-nomad-tax`](categories/12-exports-and-global-market/freelancer-and-digital-nomad-tax.md) |
| Paying too much tax, or on the wrong regime | [`income-tax-strategist`](categories/01-tax-and-bir/income-tax-strategist.md) |
| Profitable on paper, no cash | [`cash-flow-manager`](categories/04-finance-and-accounting/cash-flow-manager.md) → [`pricing-and-margin-analyst`](categories/04-finance-and-accounting/pricing-and-margin-analyst.md) |
| Selling online, growing but not earning | [`marketplace-seller-strategist`](categories/06-ecommerce-and-online-selling/marketplace-seller-strategist.md) |
| Paying people as "freelancers" | [`worker-classification-advisor`](categories/03-people-and-labor/worker-classification-advisor.md) — read this one before it becomes a claim |
| A BIR notice arrived | [`bir-audit-defense`](categories/01-tax-and-bir/bir-audit-defense.md) |
| About to dismiss someone | [`discipline-and-termination-advisor`](categories/03-people-and-labor/discipline-and-termination-advisor.md) — before you act, not after |
| A customer data breach | [`data-privacy-compliance-officer`](categories/08-legal-and-compliance/data-privacy-compliance-officer.md) — the NPC clock is short |
| An OFW funding a business back home | [`ofw-and-diaspora-market`](categories/12-exports-and-global-market/ofw-and-diaspora-market.md) |
| Thinking about a second branch | [`expansion-and-branch-strategist`](categories/10-growth-and-funding/expansion-and-branch-strategist.md) |
| Want to sell the business one day | [`business-valuation-and-exit-advisor`](categories/10-growth-and-funding/business-valuation-and-exit-advisor.md) — five years early, not five months |

Agents hand off to each other. Each one ends with a `## Hand off to` list, and every reference in
this repository resolves to an agent that exists.

## How an agent is built

Every file follows the same contract — role statement, `## When you are invoked`,
`## Philippine ground truth`, `## Decision framework`, `## Deliverables`,
`## Verify-before-advising`, `## Hand off to`, `## Limits`. The last two and the verification
section are mandatory.

The full standard, including the voice guidance and the anti-patterns, is in
[`docs/AGENT_STANDARD.md`](docs/AGENT_STANDARD.md). Read it before contributing.

## Contributing

Corrections are the most valuable contribution. If an agent cites a superseded rule, a wrong
threshold, or an agency that no longer handles something, open an issue or a PR with the primary
source. Philippine regulation moves and this repository will drift without that.

Also welcome: new agents for sectors not yet covered (healthcare practices, education, mining,
energy, security agencies, recruitment), regional specifics, and Filipino or Cebuano translations
of the owner-facing deliverables.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[MIT](LICENSE). Use them commercially, adapt them for your firm, ship them in your product.

---

*Para sa mga negosyanteng Pilipino. Built for people running real businesses here.*
