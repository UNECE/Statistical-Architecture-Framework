SAF Toolkit
============

Created on: 2026-10-12
Workgroup SAF: Trygve Falch (Statistics Norway, SSB), Jakob Engdahl (Statistics Sweden, SCB), Cedric Couralet (Statistics France, Insee), Pascal Fransen (Statistics Netherlands, CBS) and Daan Swinkels (Statistics Netherlands, CBS)

Current version: 0.3

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-10-12 | Structure proposal: concept, identifiers, entry routes, instrument list for Motivation and Strategy, one worked instrument (SAF-TK-M03) |
| 0.2 | 2026-10-12 | Reading guide parts on entry points and the architecture function moved from the framework into *Getting started* and SAF-TK-G01; Adoption register (SAF-TK-G02) confirmed; fixed format for toolkit references in the framework |
| 0.3 | 2026-10-12 | SAF-TK-G01 refers to capability 4.1.7 Architecture management;  |


## Content

[1. About the toolkit](#about-the-toolkit)

[2. Getting started](#getting-started)

[3. General instruments](#general-instruments)

[4. Motivation instruments](#motivation-instruments)

[5. Strategy instruments](#strategy-instruments)

[6. Planned instruments](#planned-instruments)

[Annex A. Instrument index](#annex-a-instrument-index)

[Annex B. Sources and reuse](#annex-b-sources-and-reuse)

# 1. About the toolkit

## Purpose

The SAF Toolkit helps an NSI apply the Statistical Architecture Framework (SAF) to its own organisation. The SAF describes *what* an NSI architecture contains and *why*. The toolkit describes *how* an NSI builds it, step by step. It offers templates, checklists and routes that an architect can use directly in a workshop, a strategy process or a project.

The toolkit is published separately from the framework. The framework changes slowly, because it holds reference content. The toolkit changes faster, because it improves with every NSI that uses it. Each instrument refers to the SAF section it supports, and each SAF section refers back to its instruments.

## What an instrument is

An instrument is one practical tool for one task. Three kinds exist:

| Kind | What it does | Example |
|---|---|---|
| Template | A structure to record SAF elements for the NSI | Assessment record |
| Checklist | A short set of questions to test readiness or completeness | Architecture function quick check |
| Route | An ordered set of instruments for one entry point | Strategic route |

Maturity scans are a fourth kind. They are planned for a later version (see *Planned instruments*).

Every instrument follows the same structure:

1. **Purpose.** What the instrument produces, and why.
2. **Use it when.** The entry routes and TOGAF ADM phases in which it applies.
3. **Inputs.** The SAF elements and NSI information it needs.
4. **Steps.** How to fill it in, in a few short steps.
5. **Template.** The table or checklist itself.
6. **Example (illustrative).** A filled-in example, linked to SAF identifiers. Examples show the form; they are never requirements.
7. **Output and next step.** What the result feeds into, and which instrument comes next.
8. **Sources.** The standards and practices the instrument builds on.

## Identifiers

Each instrument has a stable identifier: **SAF-TK-** followed by a letter for its area and a two-digit number.

| Prefix | Area | Supports SAF chapter |
|---|---|---|
| SAF-TK-G | General | Introduction (reading guide) and cross-cutting use |
| SAF-TK-M | Motivation | Motivation |
| SAF-TK-S | Strategy | Strategy |
| SAF-TK-R | Routes | All chapters |

Later areas follow the same pattern, for example SAF-TK-B for Business Architecture. Identifiers are never reused. A retired instrument keeps its identifier with the status *Retired*.

## How the toolkit relates to the framework

Each SAF section that has an instrument ends with a toolkit reference in a fixed format:

| **Toolkit:** SAF-TK-M03 Assessment record |
|---|

The toolkit uses the same identifiers as the framework (SAF-D, SAF-G, SAF-P, capability numbers, VS-01 to VS-10). An NSI that fills in the templates therefore keeps the link to the SAF automatically, as the reading guide recommends (*Keep the SAF identifiers*). The toolkit refers to framework sections by their title, not by their number.

The order of instruments follows the order in which an NSI usually works, not the order of the framework chapters. For example, the stakeholder map comes first, although Stakeholders is the last section of the Motivation chapter.

## Status of instruments

| Status | Meaning |
|---|---|
| Planned | Listed, not yet written |
| Draft | Written, under review by the SAF core team |
| Released | Reviewed and published |
| Retired | No longer maintained; identifier kept |

Review follows the same process as the SAF framework content.

## Reuse and licence

The toolkit builds on existing instruments wherever possible (see *Annex B*). It refers to TOGAF and ArchiMate but does not reproduce their content (SAF-C1).

# 2. Getting started

There is no single starting point for the SAF. The right entry depends on what the NSI wants to achieve and how mature its architecture practice is. This chapter helps an NSI choose an entry, check whether it has the minimal architecture function in place, and follow the route that belongs to its entry.

## Three entries, one destination

**Strategic entry.** The NSI starts with the Motivation layer. It recognises and assesses the SAF drivers, relates the SAF goals to its own strategic plan, and adopts or adapts the principles. It then assesses its capabilities against the SAF capability model and decides on courses of action. This entry suits an NSI that is preparing a new multi-annual strategy or modernisation programme.

**Problem-driven entry.** The NSI starts where it has a concrete problem, for example in data acquisition, metadata or dissemination. It uses the relevant value stream and steady states to analyse the problem, and works back to the capabilities and principles involved. This entry suits an NSI that wants quick, visible results and builds its architecture practice step by step.

**Project entry.** The NSI uses the SAF in one project, for example the design of a new data platform. The project applies the SAF principles and the business architecture as design guidance. The results are then reused in other projects. This entry suits an NSI with a small or new architecture function.

The three entries lead to the same place. Over time, the NSI builds a complete and connected architecture, regardless of where it started. An NSI that already has a mature architecture function follows a fourth route: it aligns its existing architecture with the SAF.

## Choose your route

| Situation of the NSI | Entry | Route | First steps |
|---|---|---|---|
| New strategy or modernisation programme | Strategic | SAF-TK-R01 Strategic route | Drivers and assessments; goals; capability assessment |
| Urgent problem in one part of the chain | Problem-driven | SAF-TK-R02 Problem-driven route | Relevant value stream; steady states; capabilities involved |
| New or small architecture function | Project | SAF-TK-R03 Project route | Principles; business architecture for one project |
| Mature architecture function | Strategic, combined with an alignment check | SAF-TK-R04 Alignment route | Map the existing architecture onto the SAF elements |

## SAF-TK-G01 Architecture function quick check

**Purpose**

Using the SAF requires an architecture function. That function does not have to be large, but some elements must be in place. TOGAF calls this the *architecture capability*. This checklist shows where the NSI stands, and which elements it needs before it starts its route.

In the SAF capability model, this function is capability **4.1.7 Architecture management**: the ability to develop, maintain and govern the enterprise architecture of the NSI, and to use it in decisions on strategy, investment and change. It is closely related to *Policy and planning* (4.1.2) and *Change management* (4.1.3).

**Use it when**

At the start of every route, and again once a year.

**Steps**

1. For each element, decide whether the NSI meets the minimal setup, the mature setup, or neither.
2. Record the evidence, for example a mandate letter, a meeting agenda or a repository.
3. For each element below the minimal setup, agree an action and an owner.
4. Start the route once all elements reach the minimal setup. The project route can start earlier.

**Template**

| Element | Minimal setup | Mature setup | Current state (none / minimal / mature) | Evidence | Action | Owner |
|---|---|---|---|---|---|---|
| Roles | One or two architects with a mandate from management | A team of enterprise, domain and solution architects | | | | |
| Governance | Architecture topics on the agenda of an existing management meeting | An architecture board with a clear mandate and a dispensation process | | | | |
| Principles | The SAF principles adopted, with a simple way to record deviations | A maintained principle set, tested in every project review | | | | |
| Repository and tooling | A shared folder with ArchiMate models made in a free tool | A managed architecture repository with versioning and reports | | | | |
| Knowledge | Basic knowledge of TOGAF and ArchiMate | Certified architects and an internal training offer | | | | |
| Involvement of the business | Key decisions discussed with business owners | Business owners for each capability and value stream | | | | |

An NSI does not need all elements before it starts. A minimal setup is enough for the project route. The function can then grow with the use of the framework.

**Output and next step**

A known starting position. Continue with the first instrument of the chosen route. The result is also a first assessment of capability 4.1.7 in SAF-TK-S02.

**Sources**

SAF Introduction, *Reading guide*. SAF capability model, 4.1.7 *Architecture management*. TOGAF Standard, 10th Edition: architecture capability (referenced, not reproduced).

## SAF-TK-R01 Strategic route

| Step | Instrument | Result |
|---|---|---|
| 1 | SAF-TK-G01 Architecture function quick check | Known starting position |
| 2 | SAF-TK-M01 Stakeholder map | Stakeholders and concerns |
| 3 | SAF-TK-M02 Driver recognition | Applicable SAF and national drivers |
| 4 | SAF-TK-M03 Assessment record | What each driver means for the NSI |
| 5 | SAF-TK-M04 Goal alignment | SAF goals linked to the strategic plan |
| 6 | SAF-TK-M05 Outcome and indicator sheet | Measurable outcomes |
| 7 | SAF-TK-M06 Principle set and dispensation record | Adopted principle set |
| 8 | SAF-TK-S01 Capability model tailoring | NSI capability model |
| 9 | SAF-TK-S02 Capability assessment and heatmap | Investment priorities |
| 10 | SAF-TK-S05 Strategy and course of action canvas | Chosen courses of action |
| Throughout | SAF-TK-G02 Adoption register | Record of adopt, adapt, extend |

## SAF-TK-R02 Problem-driven route

| Step | Instrument | Result |
|---|---|---|
| 1 | SAF-TK-S03 Value stream tailoring | The stage where the problem occurs |
| 2 | SAF-TK-S02 Capability assessment (limited scope) | The capabilities involved and their state |
| 3 | SAF-TK-M03 Assessment record | The problem stated as an assessment of a driver |
| 4 | SAF-TK-M06 Principle set | The principles that guide the solution |
| 5 | SAF-TK-M07 Requirements derivation | Testable requirements for the solution |
| 6 | SAF-TK-M08 Constraint register | Limits on the solution |
| 7 | SAF-TK-S05 Strategy and course of action canvas | The tactic that solves the problem |
| Throughout | SAF-TK-G02 Adoption register | Record of adopt, adapt, extend |

## SAF-TK-R03 Project route

| Step | Instrument | Result |
|---|---|---|
| 1 | SAF-TK-G01 Architecture function quick check | Minimal setup in place |
| 2 | SAF-TK-M06 Principle set | Principles applied to the project |
| 3 | SAF-TK-M08 Constraint register | Project constraints |
| 4 | SAF-TK-M07 Requirements derivation | Project requirements, traced to goals and principles |
| 5 | SAF-TK-G02 Adoption register | Reusable results recorded for the next project |

Business Architecture instruments will be added to this route in a later version.

## SAF-TK-R04 Alignment route

| Step | Instrument | Result |
|---|---|---|
| 1 | SAF-TK-G01 Architecture function quick check | Confirmed mature setup |
| 2 | SAF-TK-G02 Adoption register | Existing NSI elements mapped onto SAF elements |
| 3 | SAF-TK-G03 Reference model mapping | SAF aligned with national reference models |
| 4 | SAF-TK-S02 Capability assessment and heatmap | Gaps against the SAF capability model |

# 3. General instruments

| ID | Instrument | Kind | Supports | Status |
|---|---|---|---|---|
| SAF-TK-G01 | Architecture function quick check | Checklist | Getting started (this toolkit); capability 4.1.7 | Draft |
| SAF-TK-G02 | Adoption register | Template | Reading guide, *Positioning the SAF in your own architecture* | Planned |
| SAF-TK-G03 | Reference model mapping | Template | Reading guide, *Combining the SAF with other reference models* | Planned |
| SAF-TK-G04 | Legal register | Template | Reading guide, *Legislation and regulation* | Planned |

**SAF-TK-G02 Adoption register.** One table for all decisions to adopt, adapt or extend SAF elements. One row per element: the SAF identifier, the decision, the NSI identifier, an explanation, the owner and the date. The other templates each record one kind of element; the register brings their decisions together. It shows at a glance how the NSI architecture relates to the SAF, and what a new SAF version changes for the NSI.

**SAF-TK-G03 Reference model mapping.** Maps SAF principles, capabilities and standards to a national reference model such as NORA or GovS 005, with the order of precedence from the reading guide.

**SAF-TK-G04 Legal register.** Lists applicable legal provisions and the drivers, constraints, requirements and principles they lead to.

# 4. Motivation instruments

| ID | Instrument | Kind | Supports SAF section | Status |
|---|---|---|---|---|
| SAF-TK-M01 | Stakeholder map | Template | Stakeholders | Planned |
| SAF-TK-M02 | Driver recognition | Template | Drivers | Planned |
| SAF-TK-M03 | Assessment record | Template | Assessment | Draft |
| SAF-TK-M04 | Goal alignment | Template | Goals | Planned |
| SAF-TK-M05 | Outcome and indicator sheet | Template | Outcomes | Planned |
| SAF-TK-M06 | Principle set and dispensation record | Template | Architecture Principles | Planned |
| SAF-TK-M07 | Requirements derivation | Template | Requirements | Planned |
| SAF-TK-M08 | Constraint register | Template | Constraints | Planned |
| SAF-TK-M09 | Value and meaning brief | Template | Value; Meaning | Planned **[K5]** |

**SAF-TK-M01 Stakeholder map.** Maps SAF-ST01 to SAF-ST07 onto named NSI stakeholders, with concerns, influence and the views each one needs.

**SAF-TK-M02 Driver recognition.** Records which SAF drivers apply, which national drivers are added, and who raised them.

**SAF-TK-M04 Goal alignment.** Links SAF goals to the goals of the NSI strategic plan, and records national goals without an SAF counterpart.

**SAF-TK-M05 Outcome and indicator sheet.** Per outcome: indicator, baseline, target, owner and measurement moment. Starts from the indicative measures in the SAF.

**SAF-TK-M06 Principle set and dispensation record.** The adopted principle set in the TOGAF four-part format (name, statement, rationale, implications), plus a record for each approved deviation.

**SAF-TK-M07 Requirements derivation.** Derives requirements for one solution from goals, outcomes, principles and SAF reference content, with a verification method for each requirement.

**SAF-TK-M08 Constraint register.** Records constraints with source, fixed or negotiable, and the goals and requirements they affect.

**SAF-TK-M09 Value and meaning brief.** A one-page brief for a board or ministry: the values that matter to key stakeholders, the outcomes that deliver them, and how the SAF should be understood internally.

## SAF-TK-M03 Assessment record (worked instrument)

**Purpose**

The assessment record captures what each SAF driver means for one NSI. It turns a generic force into a specific finding: a strength, weakness, opportunity or threat, based on evidence. The result explains why some goals get priority over others. It also gives a baseline, so that a later assessment can show progress.

**Use it when**

| Entry route | ADM phase |
|---|---|
| Strategic route (step 4) and problem-driven route (step 3) | Phase A, Architecture Vision; baseline descriptions in Phases B to D |

Repeat the assessment once a year, or when a driver changes.

**Inputs**

- The drivers recognised in SAF-TK-M02.
- Evidence the NSI already has, such as an application portfolio overview, audit findings, a staff survey or a capability assessment (SAF-TK-S02).
- The stakeholders from SAF-TK-M01 who own the evidence.

**Steps**

1. Take one driver at a time. Start with the drivers that stakeholders raised most often.
2. For each driver, ask: what does this force mean for us today? Write each answer as one factual sentence.
3. Classify each finding as a strength, weakness, opportunity or threat.
4. Record the evidence for each finding. A finding without evidence is marked *To be substantiated*.
5. Indicate which goal or outcome the finding affects, and how strongly.
6. Agree the findings with the owner of the evidence, and record the date.

**Template**

| Assessment ID | Driver | Finding | Type | Evidence | Affects | Impact | Owner | Date |
|---|---|---|---|---|---|---|---|---|
| *NSI-AS-nn* | *SAF-D or national driver* | *One factual sentence* | *Strength / Weakness / Opportunity / Threat* | *Source document or data* | *SAF-G or SAF-O* | *High / Medium / Low* | *Name or role* | *YYYY-MM-DD* |

**Example (illustrative)**

| Assessment ID | Driver | Finding | Type | Evidence | Affects | Impact | Owner | Date |
|---|---|---|---|---|---|---|---|---|
| NSI-AS-01 | SAF-D5 Resource constraints and organisational agility | Two thirds of our processing runs on platforms out of vendor support | Weakness | Application portfolio scan | SAF-G3 Modernisation of statistical systems | High | CIO | 2026-11-01 |
| NSI-AS-02 | SAF-D1 Evolving data ecosystems and partnerships | A national data space is being set up, and we are invited to join | Opportunity | Government programme plan | SAF-G2 Harmonised reference framework | Medium | Head of data acquisition | 2026-11-01 |
| NSI-AS-03 | SAF-D3 Trust, scientific rigour and data protection | We cannot show which source data version each published figure is based on | Weakness | Internal audit finding | SAF-O2 Enhanced data quality | High | Quality manager | 2026-11-01 |

**Output and next step**

The assessment record feeds SAF-TK-M04 Goal alignment: findings with a high impact set the priority of goals. Weaknesses on capabilities feed SAF-TK-S02. Record the decisions in SAF-TK-G02.

*Modelling hint.* In ArchiMate, model each finding as an Assessment element, associated with its Driver and influencing the affected Goal or Outcome.

**Sources**

TOGAF Standard, 10th Edition: Phase A and baseline description (referenced, not reproduced). SWOT analysis as a common analysis format. SAF Motivation chapter, section *Assessment*.

# 5. Strategy instruments {#strategy-instruments}

| ID | Instrument | Kind | Supports SAF section | Status |
|---|---|---|---|---|
| SAF-TK-S01 | Capability model tailoring | Template | Capability Model | Planned |
| SAF-TK-S02 | Capability assessment and heatmap | Template | Capability Model; *How NSIs use this chapter* | Planned **[K6]** |
| SAF-TK-S03 | Value stream tailoring and capability mapping | Template | Value Streams | Planned **[K7]** |
| SAF-TK-S04 | Resource profile | Template | Resources | Planned |
| SAF-TK-S05 | Strategy and course of action canvas | Template | Courses of Action | Planned |

**SAF-TK-S01 Capability model tailoring.** Per SAF capability: adopt, adapt, extend or not applicable, with the NSI name and owner. Decisions are also recorded in SAF-TK-G02.

**SAF-TK-S02 Capability assessment and heatmap.** Scores each capability on current maturity, target maturity and importance for the goals. The gap and importance together give the heatmap and the investment candidates.

**SAF-TK-S03 Value stream tailoring and capability mapping.** Checks the stages of VS-01 to VS-10 against the NSI production chain, and maps capabilities to stages.

**SAF-TK-S04 Resource profile.** Per key capability: the resources it depends on, by the six SAF resource types, with risks such as single experts or expiring agreements.

**SAF-TK-S05 Strategy and course of action canvas.** Describes an organisation or domain strategy with SAF building blocks: drivers and assessments, goals and outcomes, principles, chosen courses of action, capabilities and resources developed, and the roadmap order.

# 6. Planned instruments {#planned-instruments}

| Area | Instrument | Reason for later |
|---|---|---|
| Maturity | Modernisation maturity scan | Builds on the UNECE Modernisation Maturity Models; needs a decision on scope and scale |
| Maturity | Architecture capability maturity scan | Builds on the ACMM in the TOGAF Series Guide on Architecture Maturity Models; deepens SAF-TK-G01 |
| Business Architecture | Reference model selection (Steady-State or Medallion) | Selection criteria are in the BA chapter; chapter still in review |
| Business Architecture | Steady-state quality gate checklist | Depends on review of States #1 to #6 |
| Governance | Architecture review checklist | Can build on the ESS EARF compliance review template |

# Annex A. Instrument index {#annex-a-instrument-index}

| ID | Instrument | Referenced from SAF framework |
|---|---|---|
| SAF-TK-G01 | Architecture function quick check | Introduction, *Reading guide* |
| SAF-TK-G02 | Adoption register | Introduction, Reading guide, *Positioning the SAF in your own architecture* |
| SAF-TK-G03 | Reference model mapping | Introduction, Reading guide, *Combining the SAF with other reference models* |
| SAF-TK-G04 | Legal register | Introduction, Reading guide, *Legislation and regulation* |
| SAF-TK-R01 to R04 | Entry routes | Introduction, *Reading guide* |
| SAF-TK-M01 | Stakeholder map | Motivation, *Stakeholders* |
| SAF-TK-M02 | Driver recognition | Motivation, *Drivers* |
| SAF-TK-M03 | Assessment record | Motivation, *Assessment* |
| SAF-TK-M04 | Goal alignment | Motivation, *Goals* |
| SAF-TK-M05 | Outcome and indicator sheet | Motivation, *Outcomes* |
| SAF-TK-M06 | Principle set and dispensation record | Motivation, *Architecture Principles* |
| SAF-TK-M07 | Requirements derivation | Motivation, *Requirements* |
| SAF-TK-M08 | Constraint register | Motivation, *Constraints* |
| SAF-TK-M09 | Value and meaning brief | Motivation, *Meaning* and *Value* |
| SAF-TK-S01 | Capability model tailoring | Strategy, *Capability Model* |
| SAF-TK-S02 | Capability assessment and heatmap | Strategy, *How NSIs use this chapter* |
| SAF-TK-S03 | Value stream tailoring and capability mapping | Strategy, *Value Streams* |
| SAF-TK-S04 | Resource profile | Strategy, *Resources* |
| SAF-TK-S05 | Strategy and course of action canvas | Strategy, *Courses of Action* |
| (planned) | Modernisation maturity scan | Motivation, *How NSIs use this chapter* |

# Annex B. Sources and reuse {#annex-b-sources-and-reuse}

| Source | Owner | Reused for | How | Licence |
|---|---|---|---|---|
| TOGAF Standard, 10th Edition, incl. Series Guides *Business Capabilities* and *Value Streams* | The Open Group | G01, M06, S01, S02, S03 | Referenced, not reproduced | Open Group licence (SAF-C1) |
| TOGAF Series Guide *Architecture Maturity Models* (US DoC ACMM) | The Open Group | Later EA maturity scan | Referenced | Open Group licence |
| ESS Enterprise Architecture Reference Framework (EARF): principles mapping, business capability model, ArchiMate models, compliance review template | Eurostat | G03, S01; later review checklist | Structure as inspiration; mapping where useful | To be confirmed **[K1]** |
| Modernisation Maturity Models | UNECE HLG-MOS | Later modernisation maturity scan | Basis for dimensions and levels | To be confirmed **[K1]** |
| Maturity Model on Quality Culture, with Excel assessment checklist | UN EG-NQAF | Format example for checklists | Format only | To be confirmed |
| MADR, Markdown Any Decision Records | ADR community | M06 dispensation record | Template adapted | MIT or CC0 |
| GC Enterprise Architecture Framework and EARB presenter template | Government of Canada | R03 project route; later review checklist | Inspiration | To be confirmed |
| GSBPM and GAMSO | UNECE HLG-MOS | Context in S01 and S03 | Referenced | CC BY 4.0 |

---

# Review notes for the core team (remove before publication)

| ID | Note | Status |
|---|---|---|
| K1 | Licence, ownership and attribution of sources for SAF and toolkit. Licences of ESS EARF, Modernisation Maturity Models and GC material to be checked before reuse. | Open: Daan consults UNECE contact |
| K2 | Reading guide parts on entry points and the architecture function moved to *Getting started* and SAF-TK-G01. | Decided 2026-10-12 |
| K3 | The project route is thin without Business Architecture instruments. | Open |
| K4 | Toolkit reference added to Stakeholders (M01) and to the reading guide section *Positioning the SAF in your own architecture* (G02). | Decided 2026-10-12 |
| K5 | One instrument for Value and Meaning (M09), while the framework has two sections. | Open |
| K6 | SAF-TK-S02 needs a simple maturity scale (proposal: 0 to 5, aligned with ACMM levels). | Open |
| K7 | SAF-TK-S03 can reuse the working table *capabilities × value stream stages* (CBS working file, not yet validated). | Open |
| K8 | Fixed format for toolkit references in the framework: **Toolkit:** SAF-TK-xnn Name. | Decided 2026-10-12 |
| K9 | *Architecture management* added to the capability model as 4.1.7 under *Strategy and leadership*; G01 refers to it. Capability count becomes 56. | Decided 2026-10-12 |
