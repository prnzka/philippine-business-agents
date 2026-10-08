# Philippine Business Agents

**A growing library of AI subagents for running a business in the Philippines.**

Most AI business advice is written for a US company. It will tell a Filipino owner to form an
LLC, file a 1099, and watch their Q4 sales — none of which exist here. What exists here is
BIR Form 1701Q, the 8% gross receipts option, a barangay clearance before a mayor's permit,
13th month pay due on 24 December, a wage order that a court might have enjoined last month,
and a customer who wants to ask three questions on Messenger before they buy.

This repository is a set of specialist agents that know that. Each one covers a single domain of
Philippine business practice — citing the republic act, the BIR form, the agency, and the
threshold — and each one is built to **verify volatile figures before quoting them**, because
Philippine rates and wage orders change mid-year.

**They work with any AI model.** Each agent is a plain Markdown file: a short YAML header and a
body of instructions. Drop them into a tool that supports subagents, or paste one in as a system
prompt or a custom instruction for whatever assistant you already use. Nothing here is tied to a
single vendor. See [`docs/INSTALLATION.md`](docs/INSTALLATION.md).

> **Not professional advice.** These agents prepare, model, draft and explain. A CPA signs
> returns, a lawyer signs contracts, a licensed professional signs plans. Every agent says so in
> its own `## Limits` section, and says it to the user too. See [DISCLAIMER.md](DISCLAIMER.md).

---

## Who this is for

- **Business owners** — from a sari-sari store to a 200-seat BPO — who want a competent second
  opinion on tax, permits, labour, pricing and growth.
- **Accountants, bookkeepers and VAs** serving Philippine SMEs, who need the structure and the
  checklists without re-deriving them each time.
- **Developers and consultants** building tools and assistants for the Philippine market.
- **Anyone starting a business here** who does not yet know which agency applies to them. Start
  with [`regulatory-licence-mapper`](categories/02-registration-and-permits/regulatory-licence-mapper.md).

## Quick start

**Any AI assistant.** Open the agent file for your situation, copy the body, and paste it in as a
system prompt, a custom instruction or a project instruction. Then describe your situation. That
is the whole setup, and it works with any model.

**Tools with subagent support.** Copy the files into the agents directory your tool reads —
for example:

```bash
git clone https://github.com/prnzka/philippine-business-agents.git

# everything
mkdir -p ~/.claude/agents
cp philippine-business-agents/categories/*/*.md ~/.claude/agents/

# or just one domain, for one project
mkdir -p .claude/agents
cp philippine-business-agents/categories/01-tax-and-bir/*.md .claude/agents/
```

Then ask in plain language, and let the assistant route from each agent's `description`:

```
Gross ko last year 2.4M, freelance web design, konti lang expenses. 8% or graduated?
Should I register for VAT? My customers are all corporate.
My Shopee sales are up 40% but I have no cash. Where is it going?
I want to open a second branch in Cebu. Walk me through it.
I got a Letter of Authority from the BIR this morning.
```

Full setup for different tools and models, including how to adapt an agent, is in
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
procurement, RA 8042 for why illegal recruitment carries decades, CA 108 for why nominee
shareholdings are a criminal matter. An owner can check the agent's work.

**They know where the money actually leaks.** The free-shipping contribution that is larger than
the marketplace commission. The expense disallowed entirely because a small withholding was
missed. The 13th month pay nobody accrued for. The empty backhaul. The lista with no limit. The
security agency billing rate that cannot carry a 12-hour post. The personal GCash account that
makes the books unauditable and the business unbankable.

**They say no.** An agent that will not tell an owner their business is not ready to franchise,
not ready to expand, or not worth what they think, is not useful. Several of these are built to
deliver that answer, with the reason.

**They refuse the shortcuts.** Splitting a business to stay under the VAT threshold, nominee
arrangements to dodge foreign equity caps, misdeclaring an HS code, fake marketplace reviews,
forced resignations, unregistered FDA products on a live sell, a non-physician with a syringe,
recruiting for overseas work without a licence. Each agent names the exposure and offers the
lawful route instead.

---

## The agents

Organised in two groups: **functional** agents for running any business, and **sector** agents for
the business you are actually in. More are being added — see
[CONTRIBUTING.md](CONTRIBUTING.md) if you want to add one.

### Running any business

#### Tax & BIR

| Agent | Use it for |
| --- | --- |
| [`bir-audit-defense`](categories/01-tax-and-bir/bir-audit-defense.md) | A client receives a Letter of Authority, Letter Notice, Notice of Discrepancy, Preliminary Assessment Notice, Final Assessment Notice or Warrant of Distraint and Levy, when a Subpoena Duces Tecum arrives, or when an owner… |
| [`bir-registration-specialist`](categories/01-tax-and-bir/bir-registration-specialist.md) | A business needs to register with the BIR for the first time, update its registration (change of address, line of business, tax type, RDO transfer), register a branch, apply for Authority to Print or a POS/CAS permit, or… |
| [`bookkeeping-and-invoicing`](categories/01-tax-and-bir/bookkeeping-and-invoicing.md) | Set up or clean up BIR-compliant books of account, design an invoice and receipt workflow under the EOPT invoicing rules, build a monthly closing routine, reconstruct back books before an audit, or decide between manual,… |
| [`income-tax-strategist`](categories/01-tax-and-bir/income-tax-strategist.md) | Choose between the 8% gross receipts option and graduated rates, to compare OSD against itemised deductions, to evaluate BMBE or other exemptions, to plan the timing of income across years, or whenever an owner asks why their… |
| [`tax-calendar-manager`](categories/01-tax-and-bir/tax-calendar-manager.md) | Build and maintain a BIR, SEC, LGU and statutory-contribution filing calendar for a specific business, to diagnose open cases and stop-filer notices, to plan the year-end and annual-renewal season, or to catch up on missed… |
| [`vat-and-percentage-tax-specialist`](categories/01-tax-and-bir/vat-and-percentage-tax-specialist.md) | Anything touching VAT or percentage tax — deciding whether to register for VAT, handling the crossing of the VAT threshold, input tax substantiation and refunds, zero-rated and exempt sales, VAT on digital services, or… |
| [`withholding-tax-specialist`](categories/01-tax-and-bir/withholding-tax-specialist.md) | Expanded withholding tax on supplier payments, withholding tax on compensation, final withholding on dividends, royalties and payments to non-residents, the 1% marketplace withholding on online sellers, and the handling of… |

#### Registration & Permits

| Agent | Use it for |
| --- | --- |
| [`bmbe-and-msme-incentives`](categories/02-registration-and-permits/bmbe-and-msme-incentives.md) | Assess BMBE eligibility under RA 9178 and secure the Certificate of Authority, to map the DTI, DOST, TESDA and Negosyo Center support a micro or small enterprise can claim, to check MSME classification for procurement and… |
| [`business-structure-advisor`](categories/02-registration-and-permits/business-structure-advisor.md) | Choose between a sole proprietorship, partnership, One Person Corporation, stock corporation and cooperative, to decide when to incorporate an existing sole prop, to structure ownership between co-founders, or to assess… |
| [`dti-sec-registration-specialist`](categories/02-registration-and-permits/dti-sec-registration-specialist.md) | Register a business name with DTI, incorporate through SEC eSPARC or OneSEC, register a cooperative with the CDA, prepare articles of incorporation and by-laws, handle SEC amendments and annual filings, or fix a rejected name… |
| [`foreign-ownership-advisor`](categories/02-registration-and-permits/foreign-ownership-advisor.md) | A foreign national or foreign company wants to own or invest in a Philippine business, when a Filipino owner is taking in foreign equity, to check the Foreign Investment Negative List and sector caps, to choose between a… |
| [`lgu-permits-navigator`](categories/02-registration-and-permits/lgu-permits-navigator.md) | Barangay clearance, mayor's or business permit applications and January renewals, zoning and locational clearance, fire safety inspection certificates, sanitary permits, local business tax assessment and disputes, and for… |
| [`regulatory-licence-mapper`](categories/02-registration-and-permits/regulatory-licence-mapper.md) | Find out which national regulators a proposed Philippine business must clear before it can legally operate — FDA, DOH, DA, PCAB, DHSUD, PRC, LTFRB, DOT, BSP, SEC secondary licences, NTC, DENR and others — and to sequence those… |

#### People & Labour

| Agent | Use it for |
| --- | --- |
| [`discipline-and-termination-advisor`](categories/03-people-and-labor/discipline-and-termination-advisor.md) | Use this agent before disciplining or dismissing a Philippine employee — to identify the lawful ground, run the twin-notice due process correctly, draft the notices and decision, compute separation pay, handle redundancy or… |
| [`dole-compliance-auditor`](categories/03-people-and-labor/dole-compliance-auditor.md) | Self-audit against Philippine labour standards before a DOLE inspection, to respond to a Notice of Results or compliance order from a labour inspection, to build an occupational safety and health programme under RA 11058, or… |
| [`hiring-and-employment-contracts`](categories/03-people-and-labor/hiring-and-employment-contracts.md) | Draft Philippine employment contracts, set up probationary employment with enforceable standards, structure project-based, fixed-term, part-time and seasonal engagements, write job offers and job descriptions, or handle the… |
| [`hr-policy-and-handbook-writer`](categories/03-people-and-labor/hr-policy-and-handbook-writer.md) | Write a Philippine employee handbook, a code of conduct with a schedule of offences and penalties, an attendance and leave policy, an anti-sexual harassment and Safe Spaces policy, a telecommuting policy, or the mandatory… |
| [`payroll-and-statutory-contributions`](categories/03-people-and-labor/payroll-and-statutory-contributions.md) | Build or audit a Philippine payroll — SSS, PhilHealth and Pag-IBIG computation and remittance, withholding tax on compensation, 13th month pay, holiday and night differential and overtime premiums, final pay on separation, and… |
| [`recruitment-and-retention-specialist`](categories/03-people-and-labor/recruitment-and-retention-specialist.md) | Hire in the Philippine labour market — sourcing channels, compensation benchmarking, interviewing and assessment, handling counter-offers and ghosting, onboarding, and reducing the turnover that costs SMEs more than their… |
| [`remote-team-and-gig-manager`](categories/03-people-and-labor/remote-team-and-gig-manager.md) | Manage remote and hybrid teams in the Philippines under the Telecommuting Act, to engage Filipino workers for offshore clients, to work with gig and platform workers such as riders and online freelancers, or to build the… |
| [`worker-classification-advisor`](categories/03-people-and-labor/worker-classification-advisor.md) | Ever a Philippine business pays someone as a freelancer, consultant, contractor, commission agent, "pakyaw" worker or virtual assistant, when engaging a manpower agency or subcontractor, or when assessing exposure from workers… |
| [`workplace-safety-officer`](categories/03-people-and-labor/workplace-safety-officer.md) | Build an occupational safety and health programme under RA 11058 and DO 198, determine the safety officer and committee requirements for an establishment, run a hazard assessment, handle a work accident and its reporting, or… |

#### Finance & Accounting

| Agent | Use it for |
| --- | --- |
| [`budgeting-and-forecasting`](categories/04-finance-and-accounting/budgeting-and-forecasting.md) | Build an annual budget for a Philippine SME, create a driver-based financial model, forecast with Philippine seasonality and inflation, run scenarios for expansion or a cost shock, or set up a monthly variance review the owner… |
| [`cash-flow-manager`](categories/04-finance-and-accounting/cash-flow-manager.md) | Build a Philippine SME cash flow forecast, diagnose why a profitable business has no cash, plan for the December and January obligation cluster, manage the gap between marketplace payout cycles and supplier terms, or triage a… |
| [`collections-and-receivables`](categories/04-finance-and-accounting/collections-and-receivables.md) | Set credit terms for Philippine customers, build a collections process, recover overdue accounts including from corporate and government payors, handle the informal "lista" and utang culture in retail, or decide when to… |
| [`financial-statements-specialist`](categories/04-finance-and-accounting/financial-statements-specialist.md) | Prepare Philippine financial statements under PFRS for SMEs or PFRS for Small Entities, assemble the audited financial statements pack for BIR and SEC filing, reconcile statements filed with different agencies, prepare… |
| [`pricing-and-margin-analyst`](categories/04-finance-and-accounting/pricing-and-margin-analyst.md) | Price a product or service for the Philippine market, compute true landed and fully loaded costs, work out whether a marketplace or reseller channel is actually profitable after fees, decide how to absorb a cost increase, or… |

#### Sales & Marketing

| Agent | Use it for |
| --- | --- |
| [`b2b-and-government-sales`](categories/05-sales-and-marketing/b2b-and-government-sales.md) | Sell to Philippine corporates and government — PhilGEPS registration and public bidding under RA 12009, accreditation as a corporate supplier, proposals and quotations, the billing pack that gets paid, and deciding whether a… |
| [`customer-service-and-retention`](categories/05-sales-and-marketing/customer-service-and-retention.md) | Build a Philippine customer service operation across Messenger, Viber, marketplace chat and phone, handle complaints and refunds under the Consumer Act and the Internet Transactions Act, manage reviews and ratings, or build… |
| [`filipino-consumer-insights`](categories/05-sales-and-marketing/filipino-consumer-insights.md) | Understand how Filipino consumers actually decide and buy — segmentation by income class and region, the sachet and tingi economy, payday and remittance cycles, social proof and group decision-making, and what differs between… |
| [`meta-ads-strategist`](categories/05-sales-and-marketing/meta-ads-strategist.md) | Plan and run Facebook, Instagram and Messenger advertising for a Philippine business — campaign structure, Messenger-first funnels, budget allocation in pesos, creative testing, audience targeting for Philippine segments, and… |
| [`taglish-copywriter`](categories/05-sales-and-marketing/taglish-copywriter.md) | Write Philippine marketing copy — Facebook and TikTok ad copy, Messenger scripts, product listings, SMS and Viber broadcasts, landing pages and email — in English, Filipino or Taglish, pitched to a specific segment rather than… |
| [`tiktok-and-live-selling-strategist`](categories/05-sales-and-marketing/tiktok-and-live-selling-strategist.md) | TikTok content and TikTok Shop strategy in the Philippines, running live selling sessions on TikTok or Facebook, building an affiliate and creator programme, or deciding whether live selling fits a business at all. |

#### E-commerce & Online Selling

| Agent | Use it for |
| --- | --- |
| [`ecommerce-logistics-and-fulfilment`](categories/06-ecommerce-and-online-selling/ecommerce-logistics-and-fulfilment.md) | Choose couriers and negotiate rates in the Philippines, design a packing and dispatch operation, manage COD and failed deliveries, handle inter-island and remote-area shipping, decide between self-fulfilment and a platform… |
| [`ecommerce-tax-compliance`](categories/06-ecommerce-and-online-selling/ecommerce-tax-compliance.md) | The tax and regulatory compliance of selling online in the Philippines — BIR registration for online sellers, the 1% marketplace withholding under RR 16-2023, invoicing for online orders, VAT on digital services and… |
| [`marketplace-seller-strategist`](categories/06-ecommerce-and-online-selling/marketplace-seller-strategist.md) | Launch or improve a Shopee, Lazada or TikTok Shop store in the Philippines — listing optimisation, fee and margin analysis, campaign and voucher participation, shop ratings and seller tier, platform ads, and deciding which… |
| [`online-store-and-payments`](categories/06-ecommerce-and-online-selling/online-store-and-payments.md) | Build a direct online store for a Philippine business, choose and integrate payment methods (GCash, Maya, QR Ph, cards, bank transfer, COD), select a payment gateway, reduce checkout abandonment, or decide whether a direct… |

#### Operations & Supply Chain

| Agent | Use it for |
| --- | --- |
| [`inventory-and-procurement`](categories/07-operations-and-supply-chain/inventory-and-procurement.md) | Set reorder points and safety stock for a Philippine business, fix stock accuracy and overselling across channels, reduce shrinkage and expiry, manage multi-channel stock allocation, or free up the cash locked in slow-moving… |
| [`sop-and-quality-builder`](categories/07-operations-and-supply-chain/sop-and-quality-builder.md) | Document standard operating procedures for a Philippine SME, build a quality control process, prepare for ISO or HACCP certification, create training materials for frontline staff, or make a business run without the owner present. |
| [`supplier-sourcing-advisor`](categories/07-operations-and-supply-chain/supplier-sourcing-advisor.md) | Find and qualify suppliers for a Philippine business — Divisoria and local wholesale markets, local manufacturers, importing from China via 1688 and Alibaba, OEM and private label arrangements, supplier negotiation, and… |

#### Legal & Compliance

| Agent | Use it for |
| --- | --- |
| [`consumer-protection-advisor`](categories/08-legal-and-compliance/consumer-protection-advisor.md) | Philippine consumer protection compliance — Consumer Act obligations on warranty, labelling, pricing and advertising, the Internet Transactions Act for online sellers, DTI sales promotion permits, responding to a DTI consumer… |
| [`contracts-and-agreements-drafter`](categories/08-legal-and-compliance/contracts-and-agreements-drafter.md) | Draft Philippine commercial agreements — service agreements, supply and distribution contracts, leases, non-disclosure agreements, founders' and shareholders' agreements, consultancy and contractor agreements, and terms of… |
| [`data-privacy-compliance-officer`](categories/08-legal-and-compliance/data-privacy-compliance-officer.md) | Data Privacy Act compliance in the Philippines — determining whether NPC registration is required, designating and equipping a DPO, writing privacy notices and consent mechanisms, building the records of processing, handling a… |
| [`dispute-resolution-advisor`](categories/08-legal-and-compliance/dispute-resolution-advisor.md) | A Philippine business is in a dispute — with a customer, supplier, landlord, partner or employee. Covers barangay conciliation, small claims court, demand letters, mediation and arbitration, bounced cheques under BP 22, and… |
| [`trademark-and-ip-specialist`](categories/08-legal-and-compliance/trademark-and-ip-specialist.md) | Register a trademark with IPOPHL, clear a brand name before launch, respond to an opposition or an infringement claim, handle copyright and trade secrets, file a Declaration of Actual Use, or deal with counterfeits of the… |

#### Growth & Funding

| Agent | Use it for |
| --- | --- |
| [`business-plan-writer`](categories/09-growth-and-funding/business-plan-writer.md) | Write a business plan for a Philippine SME — for a lender, a government programme, an investor, or for the owner's own decision-making. Also use to pressure-test an existing plan or to write a feasibility study. |
| [`business-valuation-and-exit-advisor`](categories/09-growth-and-funding/business-valuation-and-exit-advisor.md) | Value a Philippine SME, prepare it for sale, structure a share sale or an asset sale and understand the tax difference, hand a business to the next generation, bring in or buy out a partner, or wind a business down properly. |
| [`expansion-and-branch-strategist`](categories/09-growth-and-funding/expansion-and-branch-strategist.md) | Decide whether and how a Philippine business should open a second location, expand to another city or region, add a product line or channel, or scale operations — including the registration, tax and labour consequences of a… |
| [`franchise-developer`](categories/09-growth-and-funding/franchise-developer.md) | Franchise a Philippine business or to evaluate buying a franchise — the EO 169 minimum terms for MSME franchisees, disclosure practice, franchise fees and royalties, the operations manual and training system, territory and… |
| [`investor-pitch-and-fundraising`](categories/09-growth-and-funding/investor-pitch-and-fundraising.md) | Raise equity for a Philippine business — pitch deck and data room, valuation and deal structure, the Philippine angel and VC landscape, term sheets and shareholder agreements, due diligence readiness, and whether raising… |
| [`msme-loan-navigator`](categories/09-growth-and-funding/msme-loan-navigator.md) | Find and compare financing for a Philippine SME — bank term loans and credit lines, SB Corporation and government programme lending, Landbank and DBP, microfinance, cooperative credit, invoice and purchase order financing, and… |

#### Technology & Digital

| Agent | Use it for |
| --- | --- |
| [`automation-and-ai-advisor`](categories/10-technology-and-digital/automation-and-ai-advisor.md) | Find where a Philippine SME should automate or apply AI — chat response, bookkeeping data entry, inventory updates, content production, customer follow-up — and where automation is the wrong answer because labour is cheap and… |
| [`cybersecurity-for-smes`](categories/10-technology-and-digital/cybersecurity-for-smes.md) | Protect a Philippine small business from the attacks it actually faces — account takeover on Facebook and e-wallets, business email compromise and supplier payment fraud, online scams against customers using the brand,… |
| [`data-and-analytics-for-sme`](categories/10-technology-and-digital/data-and-analytics-for-sme.md) | Work out which few numbers a Philippine SME should actually track, build a simple dashboard or report from the data the business already has, analyse sales and customer data, or replace gut-feel decisions with evidence the… |
| [`digital-products-and-online-courses`](categories/10-technology-and-digital/digital-products-and-online-courses.md) | Philippine digital product businesses — online courses, templates, ebooks, memberships, subscriptions, SaaS micro-products and paid communities — covering pricing, platform choice and payments, content IP, refund and claims… |
| [`small-business-systems-advisor`](categories/10-technology-and-digital/small-business-systems-advisor.md) | Choose and implement the software a Philippine SME actually needs — POS, accounting, inventory, payroll, CRM — including BIR requirements for computerised systems, and to decide what to keep on paper or a spreadsheet instead. |
| [`website-and-seo-advisor`](categories/10-technology-and-digital/website-and-seo-advisor.md) | Decide whether a Philippine business needs a website, build one that converts on a mobile connection, rank for local and Philippine search, set up Google Business Profile for a physical location, or diagnose a site that gets… |

#### Exports & Global Market

| Agent | Use it for |
| --- | --- |
| [`cross-border-payments-advisor`](categories/11-exports-and-global-market/cross-border-payments-advisor.md) | Receive payments from abroad or pay foreign suppliers from the Philippines — comparing Wise, Payoneer, PayPal, banks and remittance channels on true cost, managing FX exposure, BSP registration of foreign investment, and the… |
| [`export-readiness-advisor`](categories/11-exports-and-global-market/export-readiness-advisor.md) | Assess whether a Philippine business is ready to export, navigate exporter registration and documentation, meet destination-market requirements and certifications, price for export, find buyers, and use DTI, CITEM and FTA… |
| [`freelancer-and-digital-nomad-tax`](categories/11-exports-and-global-market/freelancer-and-digital-nomad-tax.md) | Philippine-based freelancers, virtual assistants, online professionals and consultants with foreign clients — BIR registration, the 8% versus graduated choice, invoicing foreign clients, VAT zero-rating on service exports, and… |
| [`import-and-customs-navigator`](categories/11-exports-and-global-market/import-and-customs-navigator.md) | Import into the Philippines — importer accreditation and CPRS, HS classification and duty, VAT on importation, customs clearance and brokers, landed cost computation, regulated and restricted goods, and resolving a shipment… |
| [`ofw-and-diaspora-market`](categories/11-exports-and-global-market/ofw-and-diaspora-market.md) | Sell to Overseas Filipino Workers and the Filipino diaspora, to build a business serving remittance-receiving households in the Philippines, or to help an OFW set up a Philippine business from abroad — including the specific… |
| [`peza-boi-incentives-advisor`](categories/11-exports-and-global-market/peza-boi-incentives-advisor.md) | Assess PEZA and BOI registration for a Philippine enterprise — the CREATE and CREATE MORE incentive regimes, the income tax holiday followed by the enhanced deduction regime or the special rate on gross income, export… |


### By sector

#### Retail & Trade

| Agent | Use it for |
| --- | --- |
| [`fuel-lpg-and-regulated-retail`](categories/12-retail-and-trade/fuel-lpg-and-regulated-retail.md) | Philippine retail of regulated commodities — gasoline stations, LPG dealerships and refilling, rice and grains retailing, and the sale of tobacco and alcohol. Covers DOE licensing, the LPG Industry Regulation Act, NFA/DA… |
| [`hardware-and-construction-supply`](categories/12-retail-and-trade/hardware-and-construction-supply.md) | Philippine hardware stores and construction supply businesses — product breadth and stocking, PS mark and ICC requirements on construction materials, credit to contractors, delivery and hauling, cement and steel sourcing, and… |
| [`pharmacy-and-drugstore-business`](categories/12-retail-and-trade/pharmacy-and-drugstore-business.md) | Philippine drugstores and pharmacies — FDA Licence to Operate, the licensed pharmacist requirement, prescription and dangerous drugs handling, the Generics Act and Cheaper Medicines Act obligations, PhilHealth Konsulta… |
| [`retail-store-operations`](categories/12-retail-and-trade/retail-store-operations.md) | Philippine small-format retail beyond the sari-sari store — apparel and RTW, appliances, general merchandise, bookstores, toys, gift shops, dry goods stalls — covering store location and layout, product mix, markdowns,… |
| [`sari-sari-and-retail-operations`](categories/12-retail-and-trade/sari-sari-and-retail-operations.md) | Philippine neighbourhood and small-format retail — sari-sari stores, mini-groceries, market stalls and small shops. Covers product mix, tingi repacking, the lista credit ledger, supplier and distributor relationships, store… |
| [`wholesale-and-distribution-business`](categories/12-retail-and-trade/wholesale-and-distribution-business.md) | Philippine wholesale, trading and distribution businesses — securing a distributorship or dealership, route-to-market and coverage, trade terms and credit to retailers, consignment, sales force management, and serving… |

#### Food & Beverage

| Agent | Use it for |
| --- | --- |
| [`catering-and-events-business`](categories/13-food-and-beverage/catering-and-events-business.md) | Philippine catering, events and mobile food businesses — pricing per head, event contracts and deposits, food safety for off-site service, permits for mobile and pop-up food, staffing an event, and the seasonality of the… |
| [`food-manufacturing-and-commissary`](categories/13-food-and-beverage/food-manufacturing-and-commissary.md) | Philippine food manufacturing and commissary operations — scaling a home kitchen into a registered food business, FDA Licence to Operate and product registration, GMP and HACCP, shelf life and packaging, co-packing and toll… |
| [`food-safety-and-fda-compliance`](categories/13-food-and-beverage/food-safety-and-fda-compliance.md) | Philippine FDA compliance on food, cosmetics, supplements, medical devices and household hazardous substances — Licence to Operate, Certificate of Product Registration, labelling, permissible claims, GMP and HACCP,… |
| [`food-service-operations`](categories/13-food-and-beverage/food-service-operations.md) | Philippine food businesses — carinderia, restaurant, café, food cart, catering, cloud kitchen and commissary. Covers permits and sanitary requirements, food cost and menu engineering, kitchen operations, delivery platform… |
| [`water-refilling-and-beverage`](categories/13-food-and-beverage/water-refilling-and-beverage.md) | Philippine water refilling stations and small beverage businesses — the sanitary permit and DOH water supply rules, the water testing schedule, operator certification, container handling, delivery routes and the economics of a… |

#### Health & Personal Care

| Agent | Use it for |
| --- | --- |
| [`diagnostic-laboratory-business`](categories/14-health-and-personal-care/diagnostic-laboratory-business.md) | Philippine clinical laboratories, imaging centres and drug testing facilities — DOH licensing by service capability, the pathologist and medical technologist requirements, quality control and proficiency testing, radiation… |
| [`fitness-and-sports-facility`](categories/14-health-and-personal-care/fitness-and-sports-facility.md) | Philippine gyms, fitness studios, sports facilities and courts — membership and package economics, trainer engagement and certification, liability and waivers, equipment capital and maintenance, permits, and the retention… |
| [`laundry-and-home-services`](categories/14-health-and-personal-care/laundry-and-home-services.md) | Philippine laundry shops and home service businesses — laundromats and labandera services, housekeeping and cleaning companies, pest control (which requires an FPA licence), aircon cleaning and appliance servicing, and the… |
| [`medical-and-dental-clinic`](categories/14-health-and-personal-care/medical-and-dental-clinic.md) | Philippine medical, dental and allied health clinics — DOH licensing, PhilHealth and HMO accreditation, the PRC professional requirements, clinic economics and scheduling, medical records and data privacy, and the rules on who… |
| [`salon-spa-and-beauty-services`](categories/14-health-and-personal-care/salon-spa-and-beauty-services.md) | Philippine salons, barbershops, spas, nail and lash studios, and aesthetic clinics — DOH and LGU permits, the massage therapist and aesthetician licensing position, sanitation, FDA rules on the products used and sold, stylist… |
| [`veterinary-and-pet-services`](categories/14-health-and-personal-care/veterinary-and-pet-services.md) | Philippine veterinary clinics, pet grooming, boarding, daycare and pet retail — the PRC veterinarian and BAI requirements, veterinary drug handling, rabies and animal welfare obligations, boarding liability, and the economics… |

#### Education & Training

| Agent | Use it for |
| --- | --- |
| [`driving-school-business`](categories/15-education-and-training/driving-school-business.md) | Philippine driving schools — LTO accreditation, the land and course requirements, instructor qualifications, the theoretical driving course and practical driving course programmes, vehicle fleet and insurance, and the… |
| [`private-school-and-preschool`](categories/15-education-and-training/private-school-and-preschool.md) | Establish or run a Philippine private school, preschool or daycare — the DepEd permit to operate and government recognition, ownership and capital requirements, teacher licensing, tuition fee regulation, the voucher programme,… |
| [`tutorial-review-and-training-center`](categories/15-education-and-training/tutorial-review-and-training-center.md) | Philippine tutorial centres, review centres, TESDA-registered training institutions, assessment centres and online course businesses — UTPRAS program registration, CHED review centre rules, trainer qualifications, pricing and… |

#### Professional & Creative Services

| Agent | Use it for |
| --- | --- |
| [`bpo-and-outsourcing-advisor`](categories/16-professional-and-creative-services/bpo-and-outsourcing-advisor.md) | Build or run a Philippine BPO, call centre, virtual assistant agency or outsourced services business — pricing offshore services, PEZA or BOI registration, night shift and 24/7 labour compliance, client contracts and SLAs,… |
| [`creative-and-advertising-agency`](categories/16-professional-and-creative-services/creative-and-advertising-agency.md) | Philippine creative, advertising, photography, video production and events-marketing businesses — pricing creative work, usage rights and licensing, client contracts and revisions, media buying and markups, talent and model… |
| [`it-and-software-services-agency`](categories/16-professional-and-creative-services/it-and-software-services-agency.md) | Philippine IT services, software development and web agencies — pricing projects and retainers, scope control, client contracts and IP ownership, serving foreign clients and the tax that follows, developer hiring and retention… |
| [`professional-practice-advisor`](categories/16-professional-and-creative-services/professional-practice-advisor.md) | Philippine PRC-licensed professionals in practice — accountants, engineers, architects, surveyors, nurses, psychologists and others — covering the professional tax receipt, practice structure and partnership restrictions,… |
| [`repair-and-technical-services`](categories/16-professional-and-creative-services/repair-and-technical-services.md) | Philippine repair and technical service businesses — phone and computer repair, appliance servicing, electronics repair, and small equipment service — covering pricing diagnosis and labour, parts sourcing and counterfeit risk,… |

#### Financial & Regulated Services

| Agent | Use it for |
| --- | --- |
| [`cooperative-management`](categories/17-financial-and-regulated-services/cooperative-management.md) | Philippine cooperatives — CDA registration and the Cooperative Code, governance and the general assembly, the statutory funds and reserves, the cooperative tax exemption and its conditions, credit cooperative lending and… |
| [`insurance-agency-and-brokerage`](categories/17-financial-and-regulated-services/insurance-agency-and-brokerage.md) | Philippine insurance agencies, brokerages and HMO distribution — Insurance Commission licensing for agents and brokers, the agent-versus-broker distinction, commission structures, the Pre-Need Code, bancassurance and digital… |
| [`lending-and-financing-company`](categories/17-financial-and-regulated-services/lending-and-financing-company.md) | Philippine lending and financing companies — the SEC Certificate of Authority and minimum capital, the Lending Company Regulation Act and Financing Company Act, Truth in Lending disclosure, interest and fee caps, the… |
| [`pawnshop-and-money-service-business`](categories/17-financial-and-regulated-services/pawnshop-and-money-service-business.md) | Philippine pawnshops and money service businesses — BSP registration and authority to operate, the pawnshop rate and service charge caps, remittance agents, money changers, e-money and virtual asset service providers, AMLA… |
| [`recruitment-and-placement-agency`](categories/17-financial-and-regulated-services/recruitment-and-placement-agency.md) | Philippine recruitment and placement agencies — DMW licensing for overseas deployment, DOLE licensing for local placement, the illegal recruitment offences and their severe penalties, the no-placement-fee rules, joint and… |
| [`security-and-manpower-agency`](categories/17-financial-and-regulated-services/security-and-manpower-agency.md) | Philippine private security agencies and manpower, janitorial and job contracting businesses — PNP SOSIA licensing under RA 5487 as amended, DOLE contractor registration, the labour-only contracting prohibition, solidary… |

#### Manufacturing & Production

| Agent | Use it for |
| --- | --- |
| [`garments-and-handicraft-production`](categories/18-manufacturing-and-production/garments-and-handicraft-production.md) | Philippine garments, apparel, bags, footwear, furniture and handicraft production — sampling and costing, subcontracting and homeworkers, the DOLE homeworker rules, quality and sizing consistency, OTOP and export routes, and… |
| [`machine-shop-and-fabrication`](categories/18-manufacturing-and-production/machine-shop-and-fabrication.md) | Philippine machine shops, metal fabrication, welding and steel works businesses — job quoting and machine rates, welder and operator certification, PCAB and structural work boundaries, equipment and capability decisions,… |
| [`printing-and-signage-business`](categories/18-manufacturing-and-production/printing-and-signage-business.md) | Philippine printing, tarpaulin, signage, and promotional item businesses — job costing and quoting, equipment and consumable economics, BIR accreditation for printing invoices and receipts, signage permits, copyright and… |
| [`small-manufacturer-advisor`](categories/18-manufacturing-and-production/small-manufacturer-advisor.md) | Philippine light manufacturing businesses — costing a bill of materials, capacity and bottleneck analysis, make-versus-buy, factory siting and DENR permits, equipment decisions, production scheduling, and scaling from a… |

#### Property, Construction & Trades

| Agent | Use it for |
| --- | --- |
| [`construction-business-advisor`](categories/19-property-construction-and-trades/construction-business-advisor.md) | Philippine construction and contracting businesses — PCAB licensing and categories, bidding and estimating, construction contracts and retention, progress billing and cash flow, construction safety under DOLE DO 13,… |
| [`property-management-and-rentals`](categories/19-property-construction-and-trades/property-management-and-rentals.md) | Philippine rental and property management businesses — apartments, dormitories, boarding houses, condominium units, commercial and warehouse leasing — covering the Rent Control Act, deposits, lawful eviction, tenant screening,… |
| [`real-estate-and-leasing-advisor`](categories/19-property-construction-and-trades/real-estate-and-leasing-advisor.md) | Philippine property matters in a business context — negotiating and reviewing commercial leases, evaluating a site, buying or selling property and the taxes involved, running a rental or boarding house business, subdivision… |
| [`specialty-trades-and-installation`](categories/19-property-construction-and-trades/specialty-trades-and-installation.md) | Philippine electrical, plumbing, air-conditioning, solar installation and other specialty trade businesses — the licensed professional and PCAB specialty classification requirements, trade certification, service contracts and… |

#### Transport, Tourism & Automotive

| Agent | Use it for |
| --- | --- |
| [`automotive-sales-and-service`](categories/20-transport-tourism-and-automotive/automotive-sales-and-service.md) | Philippine automotive businesses — car and motorcycle dealerships, used vehicle trading, auto repair and service shops, parts retail, emission testing and private motor vehicle inspection centres, and vulcanising and… |
| [`tourism-and-hospitality-business`](categories/20-transport-tourism-and-automotive/tourism-and-hospitality-business.md) | Philippine tourism and hospitality businesses — resorts, hotels, homestays and short-term rentals, tour operators and travel agencies, dive and adventure operators. Covers DOT accreditation, LGU and environmental requirements,… |
| [`transport-and-logistics-business`](categories/20-transport-tourism-and-automotive/transport-and-logistics-business.md) | Philippine transport and logistics businesses — trucking and delivery fleets, LTFRB franchises for public transport and TNVS, courier and last-mile operations, warehousing, freight forwarding, and the driver employment and… |

#### Agriculture, Energy & Environment

| Agent | Use it for |
| --- | --- |
| [`agribusiness-advisor`](categories/21-agriculture-energy-and-environment/agribusiness-advisor.md) | Philippine agriculture and agribusiness — farm enterprise planning, post-harvest and value-adding, cooperatives and consolidation, DA and FPA registrations, organic certification, crop and livestock financing through ACPC and… |
| [`livestock-poultry-and-aquaculture`](categories/21-agriculture-energy-and-environment/livestock-poultry-and-aquaculture.md) | Philippine livestock, poultry, swine and aquaculture businesses — BAI and BFAR registration, biosecurity and disease outbreak exposure, contract growing arrangements, feed and feed conversion economics, environmental permits… |
| [`renewable-energy-and-solar-business`](categories/21-agriculture-energy-and-environment/renewable-energy-and-solar-business.md) | Philippine renewable energy businesses — rooftop solar installation and EPC, net metering, solar retail and distribution, biogas and biomass projects, energy service companies, and the Renewable Energy Act incentives — plus… |
| [`waste-recycling-and-environmental-services`](categories/21-agriculture-energy-and-environment/waste-recycling-and-environmental-services.md) | Philippine waste, recycling and environmental service businesses — junk shops and material recovery, hauling and treatment under DENR accreditation, e-waste, composting, septic and desludging services, and the Extended… |
---

## Common starting points

| Situation | Start here |
| --- | --- |
| Starting a business, do not know what is required | [`regulatory-licence-mapper`](categories/02-registration-and-permits/regulatory-licence-mapper.md) → [`business-structure-advisor`](categories/02-registration-and-permits/business-structure-advisor.md) → [`lgu-permits-navigator`](categories/02-registration-and-permits/lgu-permits-navigator.md) |
| Freelancer with foreign clients, not registered | [`freelancer-and-digital-nomad-tax`](categories/11-exports-and-global-market/freelancer-and-digital-nomad-tax.md) |
| Paying too much tax, or on the wrong regime | [`income-tax-strategist`](categories/01-tax-and-bir/income-tax-strategist.md) |
| Profitable on paper, no cash | [`cash-flow-manager`](categories/04-finance-and-accounting/cash-flow-manager.md) → [`pricing-and-margin-analyst`](categories/04-finance-and-accounting/pricing-and-margin-analyst.md) |
| Selling online, growing but not earning | [`marketplace-seller-strategist`](categories/06-ecommerce-and-online-selling/marketplace-seller-strategist.md) |
| Paying people as "freelancers" | [`worker-classification-advisor`](categories/03-people-and-labor/worker-classification-advisor.md) — read this one before it becomes a claim |
| A BIR notice arrived | [`bir-audit-defense`](categories/01-tax-and-bir/bir-audit-defense.md) |
| About to dismiss someone | [`discipline-and-termination-advisor`](categories/03-people-and-labor/discipline-and-termination-advisor.md) — before you act, not after |
| A customer data breach | [`data-privacy-compliance-officer`](categories/08-legal-and-compliance/data-privacy-compliance-officer.md) — the NPC clock is short |
| An OFW funding a business back home | [`ofw-and-diaspora-market`](categories/11-exports-and-global-market/ofw-and-diaspora-market.md) |
| Thinking about a second branch | [`expansion-and-branch-strategist`](categories/09-growth-and-funding/expansion-and-branch-strategist.md) |
| Want to sell the business one day | [`business-valuation-and-exit-advisor`](categories/09-growth-and-funding/business-valuation-and-exit-advisor.md) — five years early, not five months |
| Opening a food business | [`food-service-operations`](categories/13-food-and-beverage/food-service-operations.md) → [`food-safety-and-fda-compliance`](categories/13-food-and-beverage/food-safety-and-fda-compliance.md) |
| Putting a product on a supermarket shelf | [`food-manufacturing-and-commissary`](categories/13-food-and-beverage/food-manufacturing-and-commissary.md) — count the FDA registrations first |
| Running a licensed practice or clinic | [`professional-practice-advisor`](categories/16-professional-and-creative-services/professional-practice-advisor.md) · [`medical-and-dental-clinic`](categories/14-health-and-personal-care/medical-and-dental-clinic.md) |
| Anything involving a national licence — lending, pawnshop, security, recruitment | [Financial & Regulated Services](categories/17-financial-and-regulated-services/) — the licence is always the first question |

Agents hand off to each other. Each one ends with a `## Hand off to` list, and every reference in
this repository resolves to an agent that exists — the validator checks it.

## How an agent is built

Every file follows the same contract — role statement, `## When you are invoked`,
`## Philippine ground truth`, `## Decision framework`, `## Deliverables`,
`## Verify-before-advising`, `## Hand off to`, `## Limits`. The last two and the verification
section are mandatory.

The full standard, including the voice guidance and the anti-patterns, is in
[`docs/AGENT_STANDARD.md`](docs/AGENT_STANDARD.md). Read it before contributing.

Run the validator before opening a PR:

```bash
python scripts/validate_agents.py
```

It checks the frontmatter, the required sections, and that every hand-off reference resolves.

## Contributing

Corrections are the most valuable contribution. If an agent cites a superseded rule, a wrong
threshold, or an agency that no longer handles something, open an issue or a PR with the primary
source. Philippine regulation moves and this repository will drift without that.

Also welcome: new agents for sectors not yet covered, regional specifics beyond Metro Manila, and
Filipino or Cebuano versions of the owner-facing deliverables.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[MIT](LICENSE). Use them commercially, adapt them for your firm, ship them in your product, run
them on whatever model you like.

---

*Para sa mga negosyanteng Pilipino. Built for people running real businesses here.*
