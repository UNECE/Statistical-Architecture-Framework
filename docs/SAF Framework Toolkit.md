SAF Toolkit
============

Created on: 2026-10-12
Workgroup SAF: Trygve Falch (Statistics Norway, SSB), Jakob Engdahl (Statistics Sweden, SCB), Cedric Couralet (Statistics France, Insee), Pascal Fransen (Statistics Netherlands, CBS) and Daan Swinkels (Statistics Netherlands, CBS)

Current version: 0.5

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-10-12 | Structure proposal: concept, identifiers, entry routes, instrument list for Motivation and Strategy, one worked instrument (SAF-TK-M03) |
| 0.2 | 2026-10-12 | Reading guide parts on entry points and the architecture function moved from the framework into *Getting started* and SAF-TK-G01; Adoption register (SAF-TK-G02) confirmed; fixed format for toolkit references in the framework |
| 0.3 | 2026-10-12 | SAF-TK-G01 refers to capability 4.1.7 Architecture management;  |
| 0.4 | 2026-11-03 | Value stream maturity checklists and end-to-end scenarios moved from the framework into SAF-TK-V01 to V10; SAF-TK-G05 Steady-state record added |
| 0.5 | 2026-11-04 | NSI application guidance and illustrative examples of the Motivation and Strategy chapters moved into SAF-TK-M01 to M09 and S01 to S05; Business Architecture instruments added to *Planned instruments*; British spelling |


## Content

[1. About the toolkit](#about-the-toolkit)

[2. Getting started](#getting-started)

[3. General instruments](#general-instruments)

[4. Motivation instruments](#motivation-instruments)

[5. Strategy instruments](#strategy-instruments)

[6. Value stream instruments](#value-stream-instruments)

[7. Planned instruments](#planned-instruments)

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
| SAF-TK-V | Value streams | Statistical Data Value Chain |
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
| 2 | SAF-TK-V01 to V10, for that value stream | Maturity gaps across design, implementation, execution and management |
| 3 | SAF-TK-S02 Capability assessment (limited scope) | The capabilities involved and their state |
| 4 | SAF-TK-M03 Assessment record | The problem stated as an assessment of a driver |
| 5 | SAF-TK-M06 Principle set | The principles that guide the solution |
| 6 | SAF-TK-M07 Requirements derivation | Testable requirements for the solution |
| 7 | SAF-TK-M08 Constraint register | Limits on the solution |
| 8 | SAF-TK-S05 Strategy and course of action canvas | The tactic that solves the problem |
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
| SAF-TK-G05 | Steady-state record and gate log | Template | Steady-State Architecture, *How each state is described* and each state's *Quality gate* | Draft |

**SAF-TK-G02 Adoption register.** One table for all decisions to adopt, adapt or extend SAF elements. One row per element: the SAF identifier, the decision, the NSI identifier, an explanation, the owner and the date. The other templates each record one kind of element; the register brings their decisions together. It shows at a glance how the NSI architecture relates to the SAF, and what a new SAF version changes for the NSI.

**SAF-TK-G03 Reference model mapping.** Maps SAF principles, capabilities and standards to a national reference model such as NORA or GovS 005, with the order of precedence from the reading guide.

**SAF-TK-G04 Legal register.** Lists applicable legal provisions and the drivers, constraints, requirements and principles they lead to.

**SAF-TK-G05 Steady-state record and gate log.** Two parts. The *state record* documents how the NSI implements one steady state, using the ten attributes of the Steady-State Architecture as headings (definition, domains, quality gate, metadata, security, ownership, versioning, handover, traceability, examples). The *gate log* records each run of a quality gate. The gate criteria themselves stay in the framework, in each state's *Quality gate* table; the log refers to them and does not repeat them.

| Artefact version | State | Gate criterion (from the state's gate table) | Result (pass / conditional / fail) | Flag or action | Evidence | Decided by | Date |
|---|---|---|---|---|---|---|---|
| *e.g. RD-TAX-2026Q3-001* | *#1* | *Completeness against agreement* | *Conditional* | *14 unknown business IDs flagged* | *Intake report* | *Role* | *YYYY-MM-DD* |

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

**SAF-TK-M01 Stakeholder map.** Maps SAF-ST01 to SAF-ST07 onto named NSI stakeholders, with concerns, influence and the views each one needs. The NSI identifies who represents each stakeholder and records their concerns. The concerns determine which views the NSI produces: a CIO needs a capability and investment view, a privacy officer a view of data flows and protection measures. Review the map at the start of each architecture cycle.

**SAF-TK-M02 Driver recognition.** Records which SAF drivers apply, which national drivers are added, and who raised them. An NSI applies the drivers in four steps:

1. **Recognise.** Decide which SAF drivers apply to the national situation, and add national drivers where needed.
2. **Assess.** Analyse what each driver means for the NSI: strengths, weaknesses, risks and opportunities (SAF-TK-M03).
3. **Respond.** Derive or confirm the goals that answer the assessed drivers (SAF-TK-M04).
4. **Trace.** Link capabilities, programmes and architecture decisions to the drivers they address.

**SAF-TK-M04 Goal alignment.** Links SAF goals to the goals of the NSI strategic plan, and records national goals without an SAF counterpart. Each relevant goal is then translated into measurable outcomes (SAF-TK-M05) and, where needed, into objectives for programmes and projects. Each NSI can follow this path at its own pace, while working towards the same shared direction.

**SAF-TK-M05 Outcome and indicator sheet.** Per outcome: indicator, baseline, target, owner and measurement moment. The NSI selects the SAF outcomes that match its goals, starts from the indicative measures in the SAF, sets target values for its own context, and monitors them in its planning and control cycle.

**SAF-TK-M06 Principle set and dispensation record.** The adopted principle set in the TOGAF four-part format (name, statement, rationale, implications), plus a record for each approved deviation. The NSI takes the SAF principles into its own principle set, adapts the wording to national policy where needed, and adds national principles. Architecture reviews test compliance against the set; deviations follow the documented dispensation process.

**SAF-TK-M07 Requirements derivation.** Derives requirements for one solution, with a verification method for each requirement, from three sources: goals and outcomes (what must the solution provide to contribute to a goal, and how will the outcome be measured?), principles (what does each relevant SAF principle mean for this solution?), and SAF reference content (which building blocks apply, such as the quality gate and minimum metadata of a steady state, and what do they require?).

*Example (illustrative).* The examples show how a requirement is derived and traced. They are not SAF requirements.

| Source | Requirement | Applies to | How to verify |
|---|---|---|---|
| SAF-P09 No data without metadata and classification | No dataset is registered in a steady state without its minimum metadata set and an AIC classification | Data catalogue and registration process | Registration is refused when mandatory metadata is missing |
| SAF-G4 Support for data innovation | A new method can move from the innovation environment to production without manual re-implementation | Analytical platform and deployment pipeline | Time and effort for one pilot method to reach production |
| SAF-P07 Implement loosely coupled processes and systems | Business domains exchange data only through registered steady states, not through each other's internal data | All production processes | Architecture review of data flows between domains |

**SAF-TK-M08 Constraint register.** Records constraints with source, fixed or negotiable, and the goals, requirements or solutions they affect. Review a constraint when its source changes, for example after new legislation or a new government policy on cloud use.

*Example (illustrative).* The examples show the form of a constraint. They are not SAF constraints, and their content differs per country.

| Constraint | Source | Fixed or negotiable | Affects |
|---|---|---|---|
| Statistical microdata is processed only within the NSI's own controlled environment | National statistical law and confidentiality policy | Fixed | Platform and hosting choices for SAF-G3; data sharing under SAF-G2 |
| Personal data is processed in line with the GDPR, including data minimisation and purpose limitation | EU legislation | Fixed | Design of data acquisition and standardisation; SAF-P11 Privacy by design |
| Public cloud services are used only for business support functions, not for statistical production | Government or NSI cloud policy | Negotiable | Technology choices for SAF-G3 and SAF-G4 |

**SAF-TK-M09 Value and meaning brief.** A one-page brief for a board or ministry: the values that matter to key stakeholders, the outcomes that deliver them, and how the SAF should be understood internally. Use the value part to build the business case for architecture work, in investment proposals, annual reports and briefings. Use the meaning part when introducing the SAF internally, for example in an architecture charter, an onboarding programme or a management briefing. What the NSI's own core concepts mean, such as "statistical product" or "steady state", belongs in its glossary.

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

**SAF-TK-S01 Capability model tailoring.** Per SAF capability: adopt, adapt, extend or not applicable, with the NSI name and owner. The NSI maps the SAF capability model onto its own organisation and checks which capabilities it has, which it lacks and which are specific to its mandate. Decisions are also recorded in SAF-TK-G02.

**SAF-TK-S02 Capability assessment and heatmap.** Scores each capability on current maturity, target maturity and importance for the goals and outcomes it is linked to. The gap and importance together give the heatmap: capabilities with a low maturity and a high contribution to goals are the investment candidates. Each candidate is then traced to the processes, applications and platforms that realise it.

**SAF-TK-S03 Value stream tailoring and capability mapping.** Most NSIs produce statistics in a similar sequence, so the SAF value streams fit most of them. The NSI checks the stages of VS-01 to VS-10 against its own production chain, adapts names where needed, and maps its own capabilities to each stage. It then uses the value streams to assess where in the chain improvements create the most value for users.

**SAF-TK-S04 Resource profile.** Per key capability: the resources it depends on, by the six SAF resource types, with risks such as single experts or expiring agreements. Missing or at-risk resources feed the NSI's courses of action (SAF-TK-S05).

*Example (illustrative).*

| Resource | Type | Supports capabilities | Note |
|---|---|---|---|
| Access to the national population register | Data and information; relationships and agreements | 1.2.2 Secondary data collection; 2.1.4 Statistical register management | Depends on a provision agreement that must be renewed |
| Team of methodologists for estimation | People and skills | 1.3.5 Estimating population parameters; 2.2.3 Methodology | Small team; knowledge concentrated in few people |
| Shared data processing platform | Technology | 1.3 Processing; 2.1.1 Data lifecycle management | Shared by several statistical domains |

**SAF-TK-S05 Strategy and course of action canvas.** Describes an organisation or domain strategy with SAF building blocks: drivers and assessments, goals and outcomes, principles, chosen courses of action, capabilities and resources developed, and the roadmap order. When all strategies use these building blocks, overlaps and conflicts between them become visible. Most NSIs work with three levels:

1. **Organisation strategy.** The overall direction of the NSI, usually in a multi-annual plan approved by its board or ministry.
2. **Domain strategies.** Strategies for a specific area, such as data, metadata, IT, cloud, security or privacy. Each one refines the organisation strategy for its domain.
3. **Tactics and roadmaps.** Concrete approaches and their order in time, for example in a programme plan.

Each NSI names its own strategies. A small NSI may have one IT strategy that covers applications, infrastructure and cloud; a large NSI may have separate strategies for each. What matters is that the strategies are consistent with each other and traceable to the motivation.

*Example (illustrative): domain strategies NSIs often develop.* They are not a required set.

| Strategy | Typical question it answers | Mainly develops |
|---|---|---|
| Data strategy | How do we manage and use data as an asset? | 2.1 Data management; VS-01 to VS-06 |
| Metadata strategy | How do we make data findable, understandable and reusable? | 2.1.2 Metadata management |
| IT strategy | What do we reuse, buy or build, and on which platforms? | 3.2 Computerisation and automation; VS-09 |
| Cloud strategy | Which workloads may run where, and under which conditions? | 3.2.5 IT infrastructure; 3.3 Security and privacy |
| Information security strategy | How do we protect information and systems? | 3.3 Security and privacy; VS-07 |
| Privacy and confidentiality strategy | How do we protect respondents and keep statistical confidentiality? | 3.3.1 Privacy management; 1.3.7 Statistical disclosure |

Other strategies NSIs develop include strategies for data acquisition, dissemination and open data, artificial intelligence, innovation, workforce and skills, and sourcing and partnerships. Reference strategies published by other organisations are listed in the framework, *Courses of Action*.

# 6. Value stream instruments {#value-stream-instruments}

| ID | Instrument | Kind | Supports SAF section | Status |
|---|---|---|---|---|
| SAF-TK-V01 | VS-01 maturity checklist and scenarios | Checklist | Statistical Data Value Chain, *VS-01 Data Acquisition and Ingestion* | Draft |
| SAF-TK-V02 | VS-02 maturity checklist and scenarios | Checklist | Statistical Data Value Chain, *VS-02 Data Standardization and Integration* | Draft |
| SAF-TK-V03 | VS-03 maturity checklist and scenarios | Checklist | Statistical Data Value Chain, *VS-03 Data Editing and Enrichment* | Draft |
| SAF-TK-V04 | VS-04 maturity checklist and scenarios | Checklist | Statistical Data Value Chain, *VS-04 Estimation, Analysis, and Statistical Modeling* | Draft |
| SAF-TK-V05 | VS-05 maturity checklist and scenarios | Checklist | Statistical Data Value Chain, *VS-05 Statistical Product Composition* | Draft |
| SAF-TK-V06 | VS-06 maturity checklist and scenarios | Checklist | Statistical Data Value Chain, *VS-06 Dissemination and Service Delivery* | Draft |
| SAF-TK-V07 | VS-07 maturity checklist and scenarios | Checklist | Statistical Data Value Chain, *VS-07 Governance and Compliance* | Draft |
| SAF-TK-V08 | VS-08 maturity checklist and scenarios | Checklist | Statistical Data Value Chain, *VS-08 Innovation and Methodological Development* | Draft |
| SAF-TK-V09 | VS-09 maturity checklist and scenarios | Checklist | Statistical Data Value Chain, *VS-09 Infrastructure and Platform Enablement* | Draft |
| SAF-TK-V10 | VS-10 maturity checklist and scenarios | Checklist | Statistical Data Value Chain, *VS-10 Customer and Stakeholder Engagement* | Draft |

The ten value stream instruments share one purpose, one way of use and one set of steps. These are described once below. Each instrument then contains only its checklist and its scenarios.

**Purpose**

Each instrument shows how mature the NSI is in one value stream, across all four process types: design, implementation, execution and management. It does not look at execution alone. The scenarios show what a mature value stream looks like in practice, from design to improvement.

**Use it when**

| Entry route | ADM phase |
|---|---|
| Problem-driven route (step 2), for the value stream where the problem occurs; strategic route, as input to SAF-TK-S02 | Baseline and target descriptions in Phase B; gap analysis in Phases B and E |

**Inputs**

- The value stream description in the SAF, and the states it consumes and produces (Steady-State Architecture).
- The NSI's own process documentation, agreements, quality reports and audit findings for the value stream.
- The tailoring of the value stream from SAF-TK-S03, if available.

**Steps**

1. Answer each checklist question with *yes*, *partly* or *no*, and record the evidence.
2. For the primary value streams (VS-01 to VS-06), look at the four groups together. A strong execution group with weak design or management groups usually points to an ad hoc process.
3. Read the scenario closest to the NSI's own situation, and compare it with current practice.
4. For each *no* or *partly*, agree an action and an owner.

**Output and next step**

A maturity profile per value stream. Weak points on capabilities feed SAF-TK-S02. Actions feed SAF-TK-S05. Record decisions in SAF-TK-G02.

## SAF-TK-V01 VS-01 Data Acquisition and Ingestion {#saf-tk-v01}

**Checklist**


**Design Maturity**

- [ ] Do we have documented data requirements specifications for each data source?
- [ ] Do we have a formal collection methodology document that is reviewed and versioned?
- [ ] Do we have a defined metadata schema for raw data, including required metadata fields at ingestion?
- [ ] Do we have explicit validation rules and quality criteria documented before collection begins?
- [ ] Do we have a privacy impact assessment for each data source?

**Implementation Maturity**

- [ ] Are our collection instruments built from design specifications (not ad-hoc)?
- [ ] Are validation rules implemented as automated checks (not manual inspection)?
- [ ] Is metadata capture automated at each ingestion point?
- [ ] Do we have a formal testing process (technical, field, security) before going to production?
- [ ] Are operational procedures documented and maintained?

**Execution Maturity**

- [ ] Do we confirm data requirements and source availability at the start of each cycle?
- [ ] Are data sharing agreements actively managed and verified per cycle?
- [ ] Do we capture ingestion metadata for every dataset received?
- [ ] Do we perform automated structural validation before accepting data?
- [ ] Do we register every raw dataset in a metadata catalogue with provenance links?

**Management Maturity**

- [ ] Do we track KPIs (response rates, rejection rates, timeliness) across cycles?
- [ ] Do we produce data quality reports for each ingested dataset?
- [ ] Do we regularly assess metadata completeness and quality?
- [ ] Do we produce audit and compliance reports?
- [ ] Do we have a formal improvement process that feeds back into design?

**Example (illustrative): end-to-end scenarios**

Each scenario walks through **all four process types**, demonstrating how the governance pattern works in practice.

### Scenario A: Household Budget Survey (Primary Collection)

**Design Phase:** Statistical designers define the information need — monthly household expenditure by category, income sources, and household composition. Methodologists design a mixed-mode approach: a CAWI diary for daily entry over two weeks, with CAPI follow-up for non-respondents. Metadata architects define the raw data schema: 156 variables across 12 expenditure categories, with code lists from COICOP (the international classification of household expenditure). Quality criteria are set at a minimum 60% response rate, diary completion rate of at least 80% of days, and delivery to processing within 30 days of collection period end. The privacy framework specifies pseudonymisation at point of receipt, with purpose limited to expenditure statistics and CPI input.

**Implementation Phase:** Data engineers build the CAWI diary portal — a responsive web app with daily spending entry and barcode scanning for receipts, configured for 12 languages. System configurators set up the CAPI tablet app with offline capability, GPS logging for urban/rural classification, and interview recording consent. Ingestion workflows are configured so that CAWI responses are aggregated daily, CAPI interviews uploaded at the end of the field period, and paper diaries OCR-scanned in batches. The full pipeline is tested with a 200-household pilot in two municipalities, with metadata propagation verified end-to-end.

**Execution Phase:** For cycle Q3-2026, 8,000 households are sampled from the population register. CAWI invitations go out and a response monitoring dashboard tracks daily completion rates. After week two, CAPI is deployed to 2,400 non-responding households. After week four, 312 paper diaries are received from elderly respondents. Each channel generates ingestion metadata, and all 7,240 completed diaries pass structural validation. Raw data is registered in the catalogue with full provenance — per household: mode, completion dates, and diary completeness score.

**Management Phase:** Response rate reaches 90.5% against the 60% target. CAWI diary completeness is 87% of days (target 80%). Quality scoring identifies three municipalities with unusually low CAWI completion, suggesting possible broadband issues. Metadata completeness is 99.8%. Improvement recommendations: add SMS reminders for CAWI to improve daily completion; investigate broadband-gap municipalities for a CAPI-first approach next cycle. Recommendations are fed back to the design team for the Q1-2027 methodology update.

### Scenario B: Tax Register Administrative Data (Secondary Collection)

**Design Phase:** Statistical designers define the data requirement — quarterly corporate income tax declarations for all legal entities, for use in national accounts and business statistics. The data model maps the tax authority's XML schema to the NSI's raw data structure: 47 fields retained, 12 derived, corporate ID as the linkage key. The SLA is set at delivery within 45 calendar days of quarter end, minimum 98% of expected records, in XML format with XSD validation. Validation rules cover XSD schema validation, corporate ID referential integrity against the business register, and amount fields within historical range (plus or minus three standard deviations). Privacy framework: data is received under the Statistics Act mandate, with pseudonymisation deferred to the standardisation phase (VS-02.0) per agreement.

**Implementation Phase:** System configurators set up a dedicated SFTP endpoint with mutual TLS authentication and IP whitelist. Data engineers configure automated ingestion: file arrival triggers a validation pipeline (XSD check, checksum, virus scan, completeness, referential integrity, range check). Metadata registration is automated — on successful validation, a provenance record is created and linked to the agreement, and quality scores are calculated and stored. The pipeline is tested with Q1-2026 historical data resubmission; all validation rules are verified and one false-positive range check is identified and the threshold adjusted.

**Execution Phase:** Q3-2026: the tax authority delivers the quarterly file via SFTP on day 38 (within the 45-day SLA). The automated pipeline triggers: XSD valid, SHA-256 checksum matches manifest, virus scan clean, 2,347,891 records (99.2% of expected — above the 98% threshold), 14 corporate IDs not in the business register (flagged but not rejected — known lag in register updates). Raw data is stored in original XML format, assigned dataset ID `RD-TAX-2026Q3-001`. Metadata is registered: provenance, quality assessment (completeness=99.2%, timeliness=OnTime, conformance=Pass with 14 flags), and agreement reference. The "Raw Data Registered" event is published and VS-02.0 is notified.

**Management Phase:** The Q3 quality scorecard shows completeness at 99.2% (stable — consistent with Q1=99.1% and Q2=99.3%) and timeliness on time, seven days ahead of the SLA deadline. The 14 unmatched corporate IDs are all newly registered businesses with a register update lag of two to four weeks, consistent with previous quarters. SLA compliance stands at 100% for 12 consecutive quarters. Metadata completeness is 100%. No improvement recommendations are needed — the process is mature and stable, with an annual agreement renewal review scheduled for Q4.

### Scenario C: Web-Scraped Price Data (Emerging Source)

**Design Phase:** Statistical designers define the requirement — daily retail prices from major online retailers for CPI basket items covering 500 product categories and 25 retailer websites. The methodology involves no bilateral agreement (public web data), with the legal framework based on the statistics act mandate and a public interest assessment. The data model captures product URL, product name, price, currency, timestamp, retailer, product category (COICOP), and availability status. Validation rules specify that price must be positive, currency must be EUR or local, timestamp must be within 24 hours, the product URL must resolve, and price changes exceeding 50% from the previous day are flagged for review (not rejected). Quality criteria: minimum 85% of target URLs successfully scraped per day, with price change detection within 24 hours. Privacy considerations confirm no personal data is involved, with terms-of-service compliance documented per retailer.

**Implementation Phase:** Data engineers build web scrapers — one module per retailer, headless browser for JavaScript-rendered pages, with proxy rotation to avoid rate limiting. Daily scheduling is configured so that scraping runs at 03:00 local time with results aggregated by 06:00. Volatility handling includes website structure change detection via DOM fingerprinting, with automatic alerts when a scraper breaks. Metadata capture records per-scrape provenance: URL, timestamp, HTTP status, scraper version, and DOM fingerprint. The system is tested with a two-week parallel run comparing scraped prices against manually collected prices for 50 products, achieving 94% agreement (within the acceptance threshold).

**Execution Phase:** Daily operation scrapes 12,500 URLs across 25 retailers. On 2026-03-15, 11,875 URLs are successful (95% — above the 85% threshold), with 625 failures (HTTP 404: product pages removed or restructured). Forty-seven price changes exceeding 50% are flagged for manual review: 41 are confirmed genuine (seasonal sales) and 6 are identified as scraper errors (wrong element selected due to DOM change). Raw data is stored as daily JSON files with full scrape metadata. Metadata is registered: daily provenance, quality scores, scraper version, and DOM fingerprint per retailer.

**Management Phase:** The weekly quality dashboard shows an average daily success rate of 93.2% (above the 85% threshold). Retailer `ElectroShop` shows a declining success rate from 98% to 72% over three weeks — a website redesign detected by DOM fingerprinting. Monthly price comparison against official CPI field collection shows 96.1% agreement for overlapping products (above the 90% acceptance threshold). Improvement recommendations: rebuild the `ElectroShop` scraper for the new DOM structure (implementation action), investigate two new retailers for coverage expansion (design action), and evaluate retailer API access as an alternative to scraping for the top five retailers (design action that may lead to a transition from scraping to API-based secondary collection). Recommendations are fed back to the design team, with the `ElectroShop` scraper rebuild prioritised for the next sprint.


**Sources**

SAF Statistical Data Value Chain, *VS-01 Data Acquisition and Ingestion*; Steady-State Architecture, the states it consumes and produces.

## SAF-TK-V02 VS-02 Data Standardization and Integration {#saf-tk-v02}

**Checklist**


**Design Maturity**

- [ ] Do we have a documented canonical target data model for standardised data?
- [ ] Do we have a formal classification mapping strategy (deterministic correspondence tables) with an explicit version policy?
- [ ] Do we have harmonised concept and variable definitions, and rules to record cross-source definition differences as metadata (flagged for VS-03)?
- [ ] Do we have explicit structural, classification, and semantic conformance rules documented before standardisation begins?
- [ ] Do we have a defined identifier-removal/pseudonymisation design for the State #1 → State #2 transition?

**Implementation Maturity**

- [ ] Are our mapping and format-coercion rules built from design specifications (not ad-hoc scripts), and value-preserving?
- [ ] Are mapping services deterministic, with unmapped/free-text values routed to VS-03 rather than coded here?
- [ ] Is conformance validation implemented as automated checks, including a no-loss-of-content (no value changed) check?
- [ ] Is lineage capture automated for every mapping and format-coercion operation?
- [ ] Do we have a formal testing process (technical, pilot, correspondence-mapping verification) before going to production?

**Execution Maturity**

- [ ] Do we profile incoming raw data and produce a structure-gap assessment each cycle?
- [ ] Do we map source codes to standards 1-to-1, capturing the version applied and preserving the original?
- [ ] Do we record unit/currency/reference-period bases and definition differences as metadata (without converting values)?
- [ ] Do we validate structural and semantic conformance before accepting standardised data?
- [ ] Do we register every standardised dataset with full mapping lineage to its raw source?

**Management Maturity**

- [ ] Do we track KPIs (mapping coverage, unmapped-value rate, conformance pass rate) across cycles?
- [ ] Do we assess mapping completeness and orphan-code rate?
- [ ] Do we govern classification version lifecycles and correspondence tables?
- [ ] Do we produce audit, privacy, and standards-compliance reports?
- [ ] Do we have a formal improvement process that feeds back into design (e.g., correspondence-table extension)?

**Example (illustrative): end-to-end scenarios**

Each scenario walks through **all four process types**, demonstrating how the governance pattern works in practice.

### Scenario A: Labour Force Survey (Survey, Deterministic Mapping)

**Design Phase:** Data architects define the canonical LFS data model — person and household entities keyed to a pseudonymous personal identifier, with occupation, education, employment status, and region as core variables. Classification stewards adopt ISCED-2011 for education and NUTS-3 for region and build deterministic correspondence tables from the survey's source education and region codes to those standards; they also define the version policy. The design records that the survey's employment-status definition differs from the harmonised ILO definition — this difference is captured as metadata and flagged for VS-03, not reconciled here — and that free-text occupation strings are **not** coded in VS-02 but handed to VS-03 for ISCO-08 coding. The privacy design specifies that the direct personal identifier is replaced with a pseudonymous key at standardisation.

**Implementation Phase:** Data engineers build the mapping & format-coercion component that restructures raw survey returns into the canonical model and casts types, and configure the ISCED and NUTS-3 correspondence-table lookups. The conformance pipeline is configured with structural, classification, semantic, and no-loss-of-content checks, and the pseudonymisation component is implemented. The pipeline is tested on a 2,000-record synthetic sample; correspondence mappings are verified against the source code lists (100% of source codes resolve), and the routing of free-text occupation to VS-03 is confirmed.

**Execution Phase:** For cycle Q3-2026, a Raw Data Registered event arrives for 42,000 LFS returns. Profiling confirms the expected structure. The component coerces the format and maps source education codes 1-to-1 to ISCED-2011 and source region codes to NUTS-3; the 42,000 free-text occupation strings are flagged and passed to VS-03 for coding. The employment-status definition difference is recorded as metadata, the personal identifier is pseudonymised, and conformance validation passes — including the no-loss-of-content check (42,000 records, no value changed). The standardised dataset is registered with full lineage, and a Standardized Data Registered event notifies VS-03.0.

**Management Phase:** Mapping coverage for education and region is 99.9%, with 4 orphan source codes investigated and corrected in the correspondence table. The unmapped-value rate (free-text occupation routed to VS-03) is as expected. Conformance pass rate is 100% on first run. Improvement recommendations: extend the region correspondence table to cover two newly created NUTS-3 codes; confirm with VS-03 that occupation coding volumes are within capacity. Recommendations are fed back to design for the next cycle.

### Scenario B: Tax Register to Business Statistics (Multi-Source Integration)

**Design Phase:** Data architects define the canonical business statistics model keyed to the statistical business register (SBR) identifier, with turnover, employment, and economic activity as core measures. Classification stewards adopt NACE Rev. 2 for activity and build a deterministic correspondence table from the tax authority's internal activity codes. The design requires that each turnover figure carry its currency, unit ("thousands of EUR"), and reference-period basis (the VAT register's fiscal year) **as metadata** — values are recorded as received and **not** converted; converting turnover to a common unit and aligning the fiscal year to the calendar year are explicitly VS-03 activities. Conformance rules require SBR-key referential integrity and that every value is preserved unchanged.

**Implementation Phase:** Data engineers build the mapping & format-coercion component: tax internal-code → NACE Rev. 2 via the maintained correspondence table (1-to-1), XML reformatting and type casting, and SBR-key linkage. The unit/currency/period bases are captured as metadata fields. The conformance pipeline checks SBR referential integrity and verifies that every turnover value is byte-for-byte unchanged and record counts match. The pipeline is tested on Q1-2026 historical data; one activity-code correspondence gap is found and the table updated.

**Execution Phase:** Q3-2026: a Raw Data Registered event arrives for 2,347,891 tax records. Profiling flags activity as the tax internal code and turnover in thousands of EUR on a fiscal-year basis. Standardisation maps activity to NACE Rev. 2 (99.4% coverage; 0.6% with no correspondence flagged for VS-03), coerces the XML, links the SBR key, and records the turnover unit and fiscal-year basis as metadata — turnover values are left exactly as received. Fourteen records lack an SBR match (newly registered businesses, known register lag) and are flagged but retained. Conformance passes with every value unchanged. The standardised dataset `SD-BUS-2026Q3-001` is registered with lineage to `RD-TAX-2026Q3-001`, and VS-03.0 is notified that unit/period conversion remains to be done.

**Management Phase:** NACE mapping coverage is 99.4% (stable across quarters); the 0.6% unmapped activity codes are passed to VS-03. The 14 unmatched SBR keys match the known register-update lag. No-loss-of-content confirmed: turnover values and record counts identical before and after. SLA on processing time met. Improvement recommendation: extend the NACE correspondence table for the new business-activity codes, and schedule adoption planning for the upcoming NACE revision. Recommendations fed back to design.

### Scenario C: Web-Scraped Price Data (Emerging Source Standardisation)

**Design Phase:** Data architects define the canonical price record — product, retailer, price, currency, unit, reference day, and (where available) a source category code — keyed to a product-offer identifier. The design recognises that web-scraped data is largely uncoded and heterogeneous, so VS-02's role is deliberately small: coerce the scraped JSON into the canonical record structure and record each item's currency, unit, and scrape timestamp **as metadata**, leaving prices exactly as received. Where a retailer supplies a category code that has a maintained correspondence to COICOP-2018, that code is mapped 1-to-1; products with only a free-text name (no source code) are **not** classified here. Coding products to COICOP, converting currencies to EUR, and normalising units are all explicitly **VS-03** activities. Conformance rules require structural conformance and preservation of the count of distinct price observations.

**Implementation Phase:** Data engineers build the component that coerces the scraped JSON into the canonical structure and captures currency/unit/timestamp metadata, and configure the correspondence-table lookup for any retailer category codes that map to COICOP. The conformance pipeline checks structural conformance and observation-count preservation. The pipeline is tested on a sample; the structure coercion and metadata capture are verified, and the routing of unclassified products to VS-03 is confirmed.

**Execution Phase:** For 2026-03-15, a Raw Data Registered event arrives for 11,875 scraped price records. Profiling confirms structure. VS-02 coerces the records into the canonical structure, maps the subset of products that carry a correspondence-bearing retailer category code to COICOP-2018, and records each price's currency, unit, and timestamp as metadata — prices are unchanged. The majority of products (free-text only) are flagged for VS-03 classification. Conformance passes, with the distinct-observation count preserved (no value changed). The standardised daily price dataset is registered with lineage to the raw scrape, and VS-03.0 is notified that product classification and currency/unit conversion remain.

**Management Phase:** The weekly dashboard shows structural conformance at 99.6% and a high unmapped-value rate (most products lack a source code and are handed to VS-03) — expected for this source type and a useful signal that the bulk of the work for web data is downstream. Observation-count preservation is 100%. Improvement recommendations: where a retailer begins supplying category codes, add the corresponding correspondence table to raise VS-02 mapping coverage; otherwise no VS-02 change is warranted. Recommendations are fed back to the design team.


**Sources**

SAF Statistical Data Value Chain, *VS-02 Data Standardization and Integration*; Steady-State Architecture, the states it consumes and produces.

## SAF-TK-V03 VS-03 Data Editing and Enrichment {#saf-tk-v03}

**Checklist**


**Design Maturity**

- [ ] Do we have documented error-detection and editing rules with a selective-editing strategy?
- [ ] Do we have a formal imputation methodology with mandated imputation flags?
- [ ] Do we have documented derivation specifications and a coding methodology for free-text values?
- [ ] Do we have integration/linkage rules with a disclosure-risk assessment design?
- [ ] Do we have a quality-versioning and edit-audit-trail policy defined before editing begins?

**Implementation Maturity**

- [ ] Are our editing rules built from design specifications (not ad-hoc fixes)?
- [ ] Do our imputation services flag every imputed value with its method?
- [ ] Is edit-lineage capture (original value, rule, reason, actor) automated for every change?
- [ ] Can a quality version be reproduced from the standardised input plus the recorded rules?
- [ ] Do we have a formal testing process (technical, edit-impact, reproducibility, imputation evaluation)?

**Execution Maturity**

- [ ] Do we run error detection and selective-editing diagnostics each cycle?
- [ ] Do we record the original value, rule, and reason for every edit?
- [ ] Do we flag imputed values and never overwrite observed values?
- [ ] Do we document the formula and inputs for every derived variable and conversion?
- [ ] Do we register every processed dataset as an immutable, identified quality version?

**Management Maturity**

- [ ] Do we track KPIs (edit rate, imputation rate, over-editing) across cycles?
- [ ] Do we evaluate quality improvement against the State #2 baseline?
- [ ] Do we govern editing-rule and imputation-model versions and the quality-version store?
- [ ] Do we produce edit-audit, disclosure-risk, and methodology-compliance reports?
- [ ] Do we have a formal improvement process that feeds back into design?

**Example (illustrative): end-to-end scenarios**

Each scenario walks through **all four process types**, demonstrating how the governance pattern works in practice.

### Scenario A: Labour Force Survey (Coding, Editing, and Imputation)

**Design Phase:** Editing methodologists define consistency rules (e.g., age vs. labour-market status, hours vs. employment status) and a selective-editing strategy. Imputation specialists design regression imputation for item non-response on income, with constraints keeping imputed income in the respondent's plausible band. A coding methodology is designed for the free-text occupation strings handed over from VS-02 (ISCO-08, computer-assisted with a 0.85 confidence threshold, expert review below it). The versioning policy and edit audit-trail requirements are set.

**Implementation Phase:** Data engineers build the consistency-check and editing engine, configure the ISCO-08 coding service with its review queue, configure the income imputation model, and stand up the quality-version store. The pipeline is tested on a synthetic sample; the edit-impact test confirms edits move quality in the intended direction, the reproducibility test regenerates an identical version, and imputation is evaluated against a holdout sample (RMSE within target).

**Execution Phase:** For cycle Q3-2026, a Standardized Data Registered event arrives for 42,000 LFS returns. Error detection flags inconsistencies and outliers; auto-corrections are applied and high-impact records adjudicated. The 42,000 free-text occupations are coded to ISCO-08 (88% auto-coded, the rest computer-assisted and manually reviewed). Income non-response (9%) is imputed and flagged. Employment-status is harmonised to the ILO definition per the reconciliation rule. A quality version is created with full edit lineage and registered; VS-04.0 is notified.

**Management Phase:** Edit rate is 6.2%, imputation rate 9%, over-editing indicator low (selective editing working). Coding completion is 99.7%; a holdout re-check shows imputation RMSE stable. Improvement recommendations: refine two consistency rules generating false positives; retrain the occupation coder with this cycle's reviewed cases. Recommendations fed back to design.

### Scenario B: Tax Register to Business Statistics (Editing, Conversion, Integration, Derivation)

**Design Phase:** The team designs outlier and consistency rules for turnover and employment, a value-reconciliation rule for the definition difference VS-02 recorded between the survey and VAT register, and conversion rules to turn turnover (recorded by VS-02 as "thousands of EUR" on a fiscal-year basis) into units on a calendar-year basis. Derived indicators (turnover-per-employee, productivity index) are specified with formulae and classification, and linkage rules join the tax data to the structural business survey on the SBR key.

**Implementation Phase:** Engineers build the editing engine, the unit/period conversion routines, the integration component (SBR-key linkage with conflict resolution), and the derivation calculators. Edit-impact and reproducibility tests pass; the conversion routine is checked so the original value remains recoverable from lineage.

**Execution Phase:** Q3-2026: a Standardized Data Registered event arrives for 2,347,891 tax records. Outliers and duplicates are detected and corrected with full lineage. Turnover is converted to units on the calendar year (conversion factor and original value stored), the tax and survey sources are integrated on the SBR key with the reconciliation rule applied where they disagree, and turnover-per-employee is derived. A quality version `PD-BUS-2026Q3-001` is created with lineage to `SD-BUS-2026Q3-001`, and VS-04.0 is notified.

**Management Phase:** Edit rate 1.8%, conversion applied to 100% of turnover with original values preserved, reconciliation applied to 12,400 linked units. No-residual-violation check passes. Disclosure-risk report confirms the linkage stays within assessed bounds. Improvement recommendation: tighten the outlier band for one NACE class; document a recurring reconciliation case as a standing rule. Recommendations fed back to design.

### Scenario C: Web-Scraped Price Data (Coding, Imputation, Derivation)

**Design Phase:** The team designs the product classification (COICOP-2018) handed over from VS-02 for the free-text product names that had no source code, including an ML-assisted classifier with a confidence threshold and a review workflow. Currency-to-EUR and unit-to-standard-quantity conversion rules are designed from the bases VS-02 recorded, an imputation rule fills gaps where a product was not scraped on a given day (carry-forward with a staleness limit), and a daily price-index input is derived.

**Implementation Phase:** Engineers configure the COICOP classifier and review queue, the currency/unit conversion routines, the carry-forward imputation with its staleness flag, and the derivation of the index input. The classifier is evaluated against a manually-classified sample (90% agreement); below-threshold products route to review.

**Execution Phase:** For 2026-03-15, a Standardized Data Registered event arrives for 11,875 records. Products without a source code are classified to COICOP (95% above threshold, 5% reviewed). Prices are converted to EUR and standard units (original values preserved in lineage). Missing daily prices are imputed by carry-forward and flagged with staleness. The daily index input is derived. A quality version is created with full lineage and registered; VS-04.0 is notified.

**Management Phase:** Coding completion 99.2%, imputation rate (carry-forward) 4.8% with staleness within limits, conversion applied to all prices with originals preserved. A holdout check on classification shows 93% accuracy. Improvement recommendations: retrain the classifier for one recurring misclassified category; tighten the carry-forward staleness limit. Recommendations fed back to design.


**Sources**

SAF Statistical Data Value Chain, *VS-03 Data Editing and Enrichment*; Steady-State Architecture, the states it consumes and produces.

## SAF-TK-V04 VS-04 Estimation, Analysis, and Statistical Modeling {#saf-tk-v04}

**Checklist**


**Design Maturity**

- [ ] Do we have a documented estimation strategy and accuracy-measurement approach per output?
- [ ] Do we have a formal weighting/calibration methodology with defined auxiliary variables and totals?
- [ ] Do we have documented aggregation and model specifications with required diagnostics?
- [ ] Do we have a validation policy and a statistical disclosure control policy defined before estimation begins?
- [ ] Do we have a quality-measurement and output-versioning policy?

**Implementation Maturity**

- [ ] Are our weighting/estimation engines built from design specifications (not ad-hoc scripts)?
- [ ] Does variance estimation reflect both the survey design and imputation uncertainty?
- [ ] Can an output be reproduced identically from the processed input plus the recorded methodology?
- [ ] Is disclosure-control tooling implemented and applied before handover?
- [ ] Do we have a formal testing process (technical, reproducibility, benchmark, accuracy)?

**Execution Maturity**

- [ ] Do we confirm the pre-approved approach and current calibration totals each cycle?
- [ ] Do we attach methodology, weights, and an accuracy measure to every estimate?
- [ ] Do we document model assumptions, diagnostics, and limitations?
- [ ] Do we validate soundness and coherence and explain movements/revisions?
- [ ] Do we apply disclosure control and register every output as an immutable version?

**Management Maturity**

- [ ] Do we track KPIs (accuracy/CV, revisions, reproducibility, timeliness) across cycles?
- [ ] Do we assess coherence and conduct revision analysis?
- [ ] Do we govern methodology/model versions and the output-version store?
- [ ] Do we produce reproducibility-audit, disclosure-control, and methodology-compliance reports?
- [ ] Do we have a formal improvement process that feeds back into design?

**Example (illustrative): end-to-end scenarios**

Each scenario walks through **all four process types**, demonstrating how the governance pattern works in practice.

### Scenario A: Labour Force Survey (Design-Based Estimation)

**Design Phase:** Estimation methodologists design a design-based strategy for the employment rate, calibrated to population totals by age × sex × region, with a variance estimator that accounts for the survey design and for the income/non-response imputation flagged in VS-03. Target parameters, domains (national and NUTS-2), coherence criteria with prior quarters, and the disclosure-control policy for small cells are specified.

**Implementation Phase:** Engineers configure the GREG calibration engine (pinned register totals), the estimation engine, and a replication-based variance component that inflates variance for imputed values; they implement coherence checks against prior quarters and small-cell suppression. Reproducibility and back-series tests pass; accuracy measures match expectations on test data.

**Execution Phase:** For Q3-2026, a Processed Data Registered event arrives. The approach and calibration totals are confirmed; calibration converges and weighted margins reproduce the register. The employment rate is estimated at 71.4% (95% CI ±0.5pp national, wider at NUTS-2), with variance inflated for imputation. Coherence checks against Q2 pass; small NUTS-2 cells are suppressed by SDC. An output version is created with methodology, weights, and accuracy, and registered; VS-05.0 is notified.

**Management Phase:** Average CV for key estimates is stable, the coherence-check pass rate is 100%, and the preliminary-vs-final revision is within tolerance. Reproducibility audit confirms the figures regenerate from inputs + methodology. Improvement recommendations: add an auxiliary variable to the calibration to reduce variance for youth-employment estimates. Recommendations fed back to design.

### Scenario B: Tax Register to Business Statistics (Register-Based + Small-Area Estimation)

**Design Phase:** The team designs register-based aggregation of turnover and employment by NACE × region, and a small-area model for domains where direct aggregates are unstable. Accuracy measures, coherence criteria with national accounts inputs, and disclosure control for dominant-unit cells are specified.

**Implementation Phase:** Engineers build the aggregation pipeline (designed domains, units, rounding), the small-area model with its diagnostics, and dominance-rule suppression for confidentiality. Reproducibility and benchmark tests against the prior year pass; the small-area model's prediction intervals are verified.

**Execution Phase:** Q3-2026: a Processed Data Registered event arrives for the integrated business dataset. Aggregates are computed by NACE × region; unstable small domains are estimated with the small-area model and flagged distinctly from direct aggregates. Dominant-unit cells are suppressed by SDC. Coherence with national-accounts inputs is checked. `OD-BUS-2026Q3-001` is created with methodology and accuracy, linked to `PD-BUS-2026Q3-001`, and VS-05.0 is notified.

**Management Phase:** Coherence with national accounts is within tolerance; revision analysis shows stable estimates; the small-area model fit is monitored across cycles. Disclosure-control report confirms no dominant-unit disclosure. Improvement recommendation: recalibrate the small-area model after two more cycles of data. Recommendations fed back to design.

### Scenario C: Web-Scraped Price Data (Index Estimation)

**Design Phase:** The team designs the price-index estimation (e.g., a GEKS or Törnqvist multilateral index) over the COICOP items coded in VS-03, with quality-adjustment treatment, an approach for new/disappearing products, and coherence criteria against the official CPI. The disclosure policy is light (aggregated indices), and the accuracy approach for the index is specified.

**Implementation Phase:** Engineers build the index estimator, the new/disappearing-product handling, and seasonal/quality adjustment, plus coherence checks against the official CPI. Reproducibility and back-series tests pass; the index is benchmarked against the official series on historical data.

**Execution Phase:** For the monthly run, a Processed Data Registered event arrives. The multilateral index is computed over COICOP items using the carry-forward-imputed daily prices flagged in VS-03 (their uncertainty noted), new products are chained in, and the index is validated for coherence against the official CPI movement. An output version with methodology and accuracy is created and registered; VS-05.0 is notified.

**Management Phase:** The scraped index tracks the official CPI within the agreed tolerance; revision magnitude is small. Reproducibility audit passes. Improvement recommendations: refine the new-product chaining rule for one volatile category, and evaluate a longer multilateral window. Recommendations fed back to design.


**Sources**

SAF Statistical Data Value Chain, *VS-04 Estimation, Analysis, and Statistical Modeling*; Steady-State Architecture, the states it consumes and produces.

## SAF-TK-V05 VS-05 Statistical Product Composition {#saf-tk-v05}

**Checklist**


**Design Maturity**

- [ ] Do we have documented product specifications with their component outputs and selection rules?
- [ ] Do we have formal composite-indicator and time-series construction specifications?
- [ ] Do we have documented internal-consistency and coherence checks with tolerances?
- [ ] Do we have content templates and an editorial-review policy for interpretive content?
- [ ] Do we have an approval, confidentiality, and product-versioning policy defined before composition begins?

**Implementation Maturity**

- [ ] Are our composition engines built from design specifications (not ad-hoc spreadsheets)?
- [ ] Do composites carry an uncertainty measure derived from their components?
- [ ] Can a product be reproduced identically from its component versions plus the composition method?
- [ ] Is the approval workflow and versioning store implemented and tamper-evident?
- [ ] Do we have a formal testing process (technical, coherence, reproducibility)?

**Execution Maturity**

- [ ] Do we select pinned component output versions and carry their accuracy metadata forward?
- [ ] Do we construct composites without re-estimating component outputs?
- [ ] Do we run internal-consistency and coherence checks and explain discrepancies?
- [ ] Do we produce reviewed interpretive content consistent with the data and its caveats?
- [ ] Do we approve and register every product as an immutable version with full lineage?

**Management Maturity**

- [ ] Do we track KPIs (coherence pass rate, approval iterations, reproducibility) across cycles?
- [ ] Do we assess coherence and interpretability of products?
- [ ] Do we govern product/version lifecycles and the product-version store?
- [ ] Do we produce reproducibility-audit, approval/confidentiality, and standards-compliance reports?
- [ ] Do we have a formal improvement process that feeds back into design?

**Example (illustrative): end-to-end scenarios**

Each scenario walks through **all four process types**, demonstrating how the governance pattern works in practice.

### Scenario A: Labour Market Quarterly Publication

**Design Phase:** Product managers specify the quarterly labour-market publication: employment and unemployment rates (national and NUTS-2), a vacancy indicator, narrative, and a regional visualisation, drawing on the validated LFS and administrative outputs. Coherence checks against prior quarters and the approval workflow are designed.

**Implementation Phase:** Engineers configure the integration engine (pinned LFS/administrative outputs), the time-series engine for the headline series, coherence checks vs. prior quarters, and the content/approval tooling. Coherence and reproducibility tests pass on historical data.

**Execution Phase:** For Q3-2026, an Output Data Registered event arrives. The team integrates the pinned `OD-LFS-2026Q3` outputs (carrying their CIs), constructs the seasonally-relevant series, and runs coherence checks (all reconcile; coherent with Q2). The commentary explains the 0.3pp employment-rate rise and notes its significance; visualisations are produced and editorially reviewed. The product is approved and registered as an immutable version with full lineage; VS-06.0 is notified.

**Management Phase:** Coherence-check pass rate is 100%, approval completed in one iteration, all component CIs correctly propagated. Improvement recommendation: add an automated check comparing the vacancy indicator to a related administrative series. Recommendations fed back to design.

### Scenario B: Structural Business Statistics Composite Product

**Design Phase:** The composite SBS product is specified to integrate the register-based and survey-based turnover/employment estimates for the same NACE × region domains, with internal-consistency checks (domains sum to totals) and coherence vs. national-accounts inputs.

**Implementation Phase:** Engineers configure integration of the pinned `OD-BUS` outputs, the consistency checks, and dominance-aware confidentiality validation for the composite. Coherence and reproducibility tests pass.

**Execution Phase:** Q3-2026: an Output Data Registered event arrives. The register- and survey-based components are integrated for overlapping domains; NACE-class turnover sums to the published total; the components agree within tolerance except one domain, which is returned to VS-04 for review rather than adjusted. Once resolved, the product is approved and registered (`SP-BUS-2026Q3-001`) with lineage to its components; VS-06.0 is notified.

**Management Phase:** One coherence discrepancy this cycle (resolved upstream); component reuse rate high; reproducibility audit passes. Improvement recommendation: tighten the tolerance for the recurring domain and document the reconciliation. Recommendations fed back to design.

### Scenario C: Consumer Price Index Product

**Design Phase:** The CPI product is specified to compose the headline all-items index and main divisions from the validated item indices, with chaining/rebasing rules, coherence checks against the prior month and year, and analytical commentary.

**Implementation Phase:** Engineers configure the index-composition engine (designed weights and chaining), coherence checks, and the commentary/approval tooling. Coherence and reproducibility tests pass; the composed headline matches the expected value on test data.

**Execution Phase:** For the monthly run, an Output Data Registered event arrives with the validated item indices. The headline and division indices are composed with the period weights, coherence checks confirm consistency with the prior month and year, and the commentary explains the main contributors to the monthly change. The product is approved and registered with full lineage; VS-06.0 is notified.

**Management Phase:** Coherence pass rate 100%, headline reproducible from item indices + weights, approval in one iteration. Improvement recommendation: enhance the contributions visualisation for the commentary. Recommendations fed back to design.


**Sources**

SAF Statistical Data Value Chain, *VS-05 Statistical Product Composition*; Steady-State Architecture, the states it consumes and produces.

## SAF-TK-V06 VS-06 Dissemination and Service Delivery {#saf-tk-v06}

**Checklist**


**Design Maturity**

- [ ] Do we have a documented dissemination and access strategy mapped to user groups and channels?
- [ ] Do we have a final disclosure-control and de-identification policy with disclosure-risk criteria?
- [ ] Do we have channel, format, accessibility, and documentation standards defined?
- [ ] Do we have a user-support, promotion, and usage/feedback model?
- [ ] Do we have a release-governance policy with equal-access controls and a release calendar?

**Implementation Maturity**

- [ ] Are our publication, API, dashboard, and research-access services built from design specifications (on VS-09 platforms)?
- [ ] Is final disclosure-control tooling implemented with an enforced disclosure-risk gate?
- [ ] Is release timing/embargo and equal-access enforcement implemented?
- [ ] Are documentation, support, and usage-monitoring services implemented?
- [ ] Do we have a formal testing process (technical, accessibility, security/disclosure, release rehearsal)?

**Execution Maturity**

- [ ] Do we confirm channels, formats, and timing for each release?
- [ ] Do we apply final disclosure control and pass a disclosure-risk gate before publishing?
- [ ] Do we release through the confirmed channels with managed timing and equal access?
- [ ] Do we accompany every release with documentation and user support?
- [ ] Do we monitor usage and collect feedback each cycle?

**Management Maturity**

- [ ] Do we track KPIs (punctuality, disclosure-gate pass rate, usage, satisfaction) across cycles?
- [ ] Do we assess accessibility, reach, and clarity?
- [ ] Do we govern channel/release lifecycles and the release-version store?
- [ ] Do we produce disclosure, equal-access, accessibility, and security compliance reports (with VS-07)?
- [ ] Do we have a formal improvement process that feeds back into design and VS-10?

**Example (illustrative): end-to-end scenarios**

Each scenario walks through **all four process types**, demonstrating how the governance pattern works in practice.

### Scenario A: Labour Market Quarterly Release

**Design Phase:** The dissemination strategy targets policymakers (press release), researchers (API + series download), and the public (dashboard), with a pre-announced release calendar and a media embargo policy. Final disclosure-control rules for small NUTS-2 cells, accessibility standards, and the documentation standard are designed.

**Implementation Phase:** Engineers configure the publication page, the SDMX API, and the dashboard on the VS-09 platform, the SDC tooling for small-cell suppression, and embargo/equal-access release tooling. Accessibility, disclosure, and release-rehearsal tests pass.

**Execution Phase:** A Statistical Product Registered event arrives for the Q3-2026 labour-market product. The team confirms the plan, applies final SDC (suppressing two small NUTS-2 cells), and clears the disclosure-risk gate. At 09:00 the figures publish simultaneously on the website, API, and dashboard; embargoed media publish at the same moment. Documentation and methodology notes accompany the release; the helpdesk handles queries. Usage and feedback are collected. A Statistics Released event is published.

**Management Phase:** On-time release rate 100%, disclosure-gate passed first time, API availability 99.95%, usage up 12% on the prior quarter. Improvement recommendation: add a plain-language summary after feedback showed confusion about the confidence interval. Recommendations fed back to design and VS-10.

### Scenario B: Business Statistics — Microdata via Secure Research Environment

**Design Phase:** The strategy provides aggregate tables openly and de-identified business microdata through a secure research environment (SRE) for accredited researchers. The de-identification standard, output-checking rules, and SRE access model are designed with VS-07.

**Implementation Phase:** Engineers configure the open tables on the portal and the SRE access service with output checking on the VS-09 platform; the de-identification component and disclosure gate are configured. Security/disclosure and accessibility tests pass.

**Execution Phase:** A Statistical Product Registered event arrives for the SBS product. Aggregate tables are disclosure-controlled and published openly; the microdata is de-identified to the standard and made available in the SRE. Accredited researchers are onboarded with the data dictionary and methodology; the helpdesk handles output-checking so researchers' exported results also meet disclosure rules. Usage in the SRE is logged. A Statistics Released event is published.

**Management Phase:** Disclosure-gate pass rate 100%, no disclosure incidents, SRE onboarding time within target. Improvement recommendation: add a self-service output-checking pre-screen to reduce helpdesk load. Recommendations fed back to design and VS-10.

### Scenario C: Consumer Price Index — Headline Release and Dashboard

**Design Phase:** The CPI dissemination strategy provides a headline press release, an API for the series, and an interactive dashboard, on a fixed pre-announced calendar with a tight embargo (price indices are market-sensitive). Accessibility and documentation standards are designed.

**Implementation Phase:** Engineers configure the release page, the API, and the dashboard, plus strict embargo/equal-access release tooling (CPI is market-sensitive). Disclosure (light, aggregated indices), accessibility, and release-rehearsal tests pass.

**Execution Phase:** A Statistical Product Registered event arrives for the monthly CPI product. The plan is confirmed, the light disclosure check passes, and at the scheduled minute the headline, API series, and dashboard go live simultaneously with strict equal access. Documentation explains the monthly movement and contributions; the helpdesk handles media queries. Usage spikes are monitored. A Statistics Released event is published.

**Management Phase:** Punctuality 100% (critical for a market-sensitive release), no embargo breaches, dashboard views at record highs on release day. Improvement recommendation: add a contributions-to-change visual to the dashboard after user feedback. Recommendations fed back to design and VS-10.


**Sources**

SAF Statistical Data Value Chain, *VS-06 Dissemination and Service Delivery*; Steady-State Architecture, the states it consumes and produces.

## SAF-TK-V07 VS-07 Governance and Compliance {#saf-tk-v07}

**Checklist**

- [ ] Do we have documented governance frameworks and policies covering data, metadata, ethics, confidentiality, and quality?
- [ ] Have we mapped applicable regulation (GDPR, statistics law) to concrete compliance procedures?
- [ ] Are data-governance roles (owner, steward, custodian) assigned and metadata/lineage processes in place?
- [ ] Do we monitor quality and compliance on dashboards, and audit/certify periodically?
- [ ] Is there a closed loop that feeds audit findings and regulatory change back into the frameworks?

**Example (illustrative): end-to-end scenarios**

**Scenario A — A new regulation lands.** A change to data-protection law is detected (07.2/07.6). VS-07 assesses the impact, updates the privacy and confidentiality policy, issues a "Policy update" to all streams, and verifies adoption at the next audit — the chain stays compliant without each stream interpreting the law independently.

**Scenario B — Pre-production method approval.** VS-08 proposes a new machine-learning coding method. VS-07 assesses it against the compliance criteria (privacy, transparency, quality) before VS-08's 08.5 transfer to production, certifies it, and records the decision — so only sound, compliant methods reach the production streams.

**Scenario C — Preparing a Code of Practice peer review.** Ahead of the periodic European Statistics Code of Practice peer review, VS-07 assembles the evidence base from its dashboards and the streams' compliance reporting (07.4/07.5): policy register, audit trail summaries, quality indicators, and incident records. Gaps surfaced by the self-assessment — say, an outdated revision policy — are remediated through 07.6 before the review. The peer-review outcome and its recommendations enter the governance backlog, and the resulting certification is published as external assurance.


**Sources**

SAF Statistical Data Value Chain, *VS-07 Governance and Compliance*; Steady-State Architecture, the states it consumes and produces.

## SAF-TK-V08 VS-08 Innovation and Methodological Development {#saf-tk-v08}

**Checklist**

- [ ] Do we maintain a prioritised innovation backlog drawn from both technology scanning and the production streams' improvement needs?
- [ ] Do we test new methods in controlled PoCs before committing?
- [ ] Do we evaluate soundness, scalability, and ethics before development?
- [ ] Is there a governed transfer gate (with VS-07 approval) for moving methods into production?
- [ ] Do we disseminate results and build staff capability so innovations are sustained?

**Example (illustrative): end-to-end scenarios**

**Scenario A — ML-assisted coding.** A production stream (VS-03) repeatedly flags free-text occupation coding as costly. VS-08 picks this up (08.1), pilots an ML coder (08.2), evaluates accuracy and bias (08.3), builds a documented reference implementation (08.4), and — after VS-07 approval and on a VS-09 platform — transfers it into VS-03 (08.5), then trains the coding team (08.6).

**Scenario B — New data source (web-scraped prices).** VS-10 reports demand for more timely price statistics. VS-08 researches web-scraping and multilateral index methods, evaluates feasibility and quality against the official CPI, documents the method, and transfers it into VS-01/VS-04, sharing the methodology across the price-statistics team.

**Scenario C — The gate says no.** A vendor demo convinces a statistical domain that a generative-AI assistant could draft analytical commentary (VS-05). VS-08 takes it through the pipeline: the PoC (08.2) shows impressive fluency, but the evaluation (08.3) finds unexplainable variation between runs and no way to meet the methodological-transparency requirement, and VS-07's compliance pre-assessment concurs. The idea is stopped at the gate, the rationale is documented and shared (08.6), and a narrower, compliant alternative — template-based drafting with human sign-off — is added to the backlog. A healthy 08.3 gate is one that sometimes says no.


**Sources**

SAF Statistical Data Value Chain, *VS-08 Innovation and Methodological Development*; Steady-State Architecture, the states it consumes and produces.

## SAF-TK-V09 VS-09 Infrastructure and Platform Enablement {#saf-tk-v09}

**Checklist**

- [ ] Do we derive infrastructure requirements from business capabilities and data volumes (not ad-hoc)?
- [ ] Do we have architecture blueprints for storage, processing, integration, and secure access?
- [ ] Are environments provisioned with governance, monitoring, and security controls built in?
- [ ] Do we provide integration/orchestration and the event interfaces the streams rely on?
- [ ] Do we monitor performance, manage incidents, and guarantee availability and disaster recovery?
- [ ] Is there a modernisation path that adopts new technology (often from VS-08) and retires the obsolete?

**Example (illustrative): end-to-end scenarios**

**Scenario A — Onboarding a secure research environment.** VS-06 needs to release de-identified microdata to accredited researchers. VS-09 captures the requirement (09.1), designs the SRE architecture (09.2), provisions it with access controls and output checking (09.3/09.4), and assures its security and availability (09.5) under VS-07's policy — so VS-06 can deliver controlled microdata access reliably.

**Scenario B — Adopting a cloud processing platform.** VS-08 validates a scalable processing technology. VS-09 designs and provisions the platform (09.2/09.3), enables integration with the existing pipelines (09.4), assures performance and continuity (09.5), and folds it into the modernisation roadmap (09.6), so the production streams gain capacity without disruption.

**Scenario C — Scaling for the census peak.** The census (VS-01) will multiply ingestion and processing volumes for three months. VS-09 derives the peak requirements with the census team (09.1), updates the capacity plan and architecture (09.2), provisions elastic compute and storage ahead of the field period (09.3), and load-tests the ingestion event interfaces end to end (09.4). During the peak it monitors throughput and availability against the agreed service levels (09.5); afterwards the surge capacity is released and the lessons feed the modernisation roadmap (09.6). The chain experiences the census as business as usual.


**Sources**

SAF Statistical Data Value Chain, *VS-09 Infrastructure and Platform Enablement*; Steady-State Architecture, the states it consumes and produces.

## SAF-TK-V10 VS-10 Customer and Stakeholder Engagement {#saf-tk-v10}

**Checklist**

- [ ] Have we mapped and segmented our stakeholders (users, providers, partners, policymakers)?
- [ ] Do we systematically collect and analyse user needs and translate them into requirements?
- [ ] Do we manage a service/product portfolio aligned to those needs and to strategy?
- [ ] Do we operate user support and manage key relationships, monitoring satisfaction?
- [ ] Do we measure impact and feed insight back into design and innovation (VS-08)?

**Example (illustrative): end-to-end scenarios**

**Scenario A — A new user need becomes a product.** Through consultation (10.2) VS-10 learns that regional policymakers need more granular labour-market data. It logs the requirement, adds a candidate product to the portfolio (10.3), routes the need to design (VS-04/VS-05) and, where new methods are required, to VS-08. Once released by VS-06, VS-10 monitors uptake and satisfaction (10.6) and refines the offering.

**Scenario B — Closing the feedback loop.** VS-06.5 reports confusion about confidence intervals in a release. VS-10 analyses the feedback (10.2/10.6), provides targeted user guidance and a plain-language explainer (10.5), and feeds a documentation improvement back to VS-05/VS-06 design — turning a usability problem into a concrete improvement.

**Scenario C — A new audience emerges.** Monitoring shows journalists increasingly republishing statistics from third-party aggregators, sometimes incorrectly. VS-10 identifies data journalists as a distinct segment (10.1), consults them on their needs — machine-readable releases, embeddable visuals, plain-language methodology notes (10.2) — and adds a media-service offer to the portfolio (10.3). The channel requirements are routed to VS-06 and VS-09, an embargoed media briefing service is set up under VS-07's equal-access policy (10.4/10.5), and citation accuracy in the press is tracked as an impact measure (10.6).


**Sources**

SAF Statistical Data Value Chain, *VS-10 Customer and Stakeholder Engagement*; Steady-State Architecture, the states it consumes and produces.

# 7. Planned instruments {#planned-instruments}

| Area | Instrument | Reason for later |
|---|---|---|
| Maturity | Modernisation maturity scan | Builds on the UNECE Modernisation Maturity Models; needs a decision on scope and scale |
| Maturity | Architecture capability maturity scan | Builds on the ACMM in the TOGAF Series Guide on Architecture Maturity Models; deepens SAF-TK-G01 |
| Business Architecture | Reference model selection (Steady-State or Medallion) | Selection criteria are in the BA chapter; chapter still in review |
| Business Architecture | Role mapping and RACI template | Maps departments, teams and job profiles onto SAF actors and roles; waits for the role reference to stabilise |
| Business Architecture | Process template and process mapping | Maps NSI processes onto the SAF process model (PRD, OVA, DLM, MDS, DSP) |
| Business Architecture | Function template and organisation-to-function mapping | Maps organisational units onto the SAF business functions (FUN) |
| Governance | Architecture review checklist | Can build on the ESS EARF compliance review template |

# Annex A. Instrument index {#annex-a-instrument-index}

| ID | Instrument | Referenced from SAF framework |
|---|---|---|
| SAF-TK-G01 | Architecture function quick check | Introduction, *Reading guide* |
| SAF-TK-G02 | Adoption register | Introduction, Reading guide, *Positioning the SAF in your own architecture* |
| SAF-TK-G03 | Reference model mapping | Introduction, Reading guide, *Combining the SAF with other reference models* |
| SAF-TK-G04 | Legal register | Introduction, Reading guide, *Legislation and regulation* |
| SAF-TK-G05 | Steady-state record and gate log | Steady-State Architecture, *How each state is described* |
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
| SAF-TK-V01 to V10 | Value stream maturity checklists and scenarios | Statistical Data Value Chain, end of each value stream |
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
| K10 | Value stream maturity checklists and end-to-end scenarios moved from the framework into SAF-TK-V01 to V10, unchanged in content. Checklists for VS-07 to VS-10 are not yet split by process type, and the scenarios still name some old stage numbers; to be aligned when the value streams are rewritten in the ten-attribute format. | Open |
