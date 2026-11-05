SAF Architecture Framework
============================

Created on: 07-07-2025
Workgroup SAF: Trygve Falch (Statistics Norway, SSB), Jakob Engdahl (Statistics Sweden, SCB), Cedric Couralet (Statistics France, Insee), Pascal Fransen (Statistics Netherlands, CBS) and Daan Swinkels (Statistics Netherlands, CBS)

Current version: 0.9

| Version | Date | Change |
|---|---|---|
|0.1|2025-07-07|Initial version|
|0.2|2026-06-01|Review processed|
|0.3|2026-07-31|Restructuring, Start with Business Architecture|
|0.4|2026-09-01|Merging Business Architecture content|
|0.5|2026-10-10|Restructured motivation section, TOGAF and ArchiMate context added|
|0.6|2026-10-11|Restructured strategy section|
|0.7|2026-10-12|Restructured business section, added business actors, roles and collaborations|
|0.8|2026-10-31|Consolidated and structured Steady State detail content|
|0.9|2026-11-04|Simplified: maturity checklists, scenarios and NSI application guidance moved to the SAF Toolkit; rules common to all steady states stated once; all value streams in the ten-attribute format, old per-stream documents and summaries removed; Motivation and Strategy compacted; cross-cutting definitions stated once; British spelling|


## Content

[Preface](#preface)

-   [Acknowledgements](#acknowledgements)

[Introduction](#introduction)

-   [Purpose](#purpose)
-   [Definition of Scope](#definition-of-scope)
-   [Target Audience](#target-audience)
-   [Expected value](#expected-value)
-   [Constraints & Assumptions](#constraints-assumptions)
-   [Reading guide](#reading-guide)

[Motivation](#motivation)

-   [Purpose of this chapter](#purpose-of-this-chapter)
-   [Position in the framework](#position-in-the-framework)
-   [How NSIs use this chapter](#how-nsis-use-this-chapter)
-   [Motivation concepts in the SAF](#motivation-concepts-in-the-saf)
-   [Drivers](#drivers)
-   [Goals](#goals)
-   [Meaning](#meaning)
-   [Outcomes](#outcomes)
-   [Architecture Principles](#architecture-principles)
-   [Value](#value)
-   [Stakeholders](#stakeholders)

[Strategy](#strategy)

-   [Purpose of this chapter](#purpose-of-this-chapter-1)
-   [Position in the framework](#position-in-the-framework-1)
-   [How NSIs use this chapter](#how-nsis-use-this-chapter-1)
-   [Strategy concepts in the SAF](#strategy-concepts-in-the-saf)
-   [Capability Model](#capability-model)
-   [Value Streams](#value-streams)
-   [Resources](#resources)
-   [Courses of Action](#courses-of-action)

[Business Architecture](#business-architecture)

-   [Purpose of this chapter](#purpose-of-this-chapter-2)
-   [Position in the framework](#position-in-the-framework-2)
-   [How NSIs use this chapter](#how-nsis-use-this-chapter-2)
-   [Relationship with the statistical standards](#relationship-with-the-statistical-standards)
-   [Business architecture concepts in the SAF](#business-architecture-concepts-in-the-saf)
-   [How the business architecture is built up](#how-the-business-architecture-is-built-up)
-   [Structure of this chapter](#structure-of-this-chapter)
-   [Business Actors, Business Roles and Business Collaborations](#business-actors-business-roles-and-business-collaborations)
-   [Business Processes](#business-processes)
-   [Business Functions](#business-functions)
-   [Business Services, Events and Objects](#business-services-events-and-objects)
-   [Reference Models for the Statistical Data Value Chain](#reference-models-for-the-statistical-data-value-chain)

[Steady-State Architecture](#steady-state-architecture)

-   [Overview](#overview)
-   [Boundary Position #0: Source Data](#boundary-position-0-source-data)
-   [State #1: Raw Data](#state-1-raw-data)
-   [State #2: Standardized Data](#state-2-standardized-data)
-   [State #3: Processed Data](#state-3-processed-data)
-   [State #4: Statistics](#state-4-statistics)
-   [State #5: Released Data](#state-5-released-data)
-   [Boundary Position #6: Consumed Data](#boundary-position-6-consumed-data)

[Statistical Data Value Chain](#statistical-data-value-chain)

-   [Value Chains Introduction](#value-chains-introduction)
-   [Principles to Apply](#principles-to-apply)
-   [VS-01 Data Acquisition and Ingestion](#vs-01-data-acquisition-and-ingestion)
-   [VS-02 Data Standardization and Integration](#vs-02-data-standardization-and-integration)
-   [VS-03 Data Editing and Enrichment](#vs-03-data-editing-and-enrichment)
-   [VS-04 Estimation, Analysis, and Statistical Modeling](#vs-04-estimation-analysis-and-statistical-modeling)
-   [VS-05 Statistical Product Composition](#vs-05-statistical-product-composition)
-   [VS-06 Dissemination and Service Delivery](#vs-06-dissemination-and-service-delivery)
-   [VS-07 Governance and Compliance](#vs-07-governance-and-compliance)
-   [VS-08 Innovation and Methodological Development](#vs-08-innovation-and-methodological-development)
-   [VS-09 Infrastructure and Platform Enablement](#vs-09-infrastructure-and-platform-enablement)
-   [VS-10 Customer and Stakeholder Engagement](#vs-10-customer-and-stakeholder-engagement)

# Preface

The Statistical Architecture Framework (SAF) was developed to support the modernisation of official statistics. This framework responds to the need of national statistical institutes and their partners for shared guidelines and standards. Producing statistics must remain credible, secure, and efficient. At the same time, organisations must adapt quickly to new data sources, higher user expectations, and tighter regulations and budgets. The SAF provides a solid foundation for this and help organisations guide these changes in a controlled and structured way.

This new framework replaces the older CSPA and CSDA standards, but it reuses the elements that are still current and valuable. The SAF combines the core ideas from these previous framework into a single, logical, and coherent model. While the framework continues to focus on cooperation, reuse, and standards, the focus has shifted heavily toward a practical application of the framework in an organisation. It is specifically designed to be used directly within ongoing programmes and projects. This helps teams make concrete choices when designing and implementing new processes and solutions.

The fundamental principle of the framework is that data and its descriptions are the most important assets of a statistical organisation. Information is not just a tool to run processes, but the core of the organisation. The SAF therefore treats this information as an NSIs most valuable asset that must be professionally managed throughout its entire lifecycle. It must support systems that can work with both traditional and modern, new data sources and information flows. In addition, it offers a practical guide for collecting, combining, and publishing data.

The SAF builds on a modular approach where systems are constructed from loose, flexible components. It promotes the reuse of these digital building blocks, both within an organisation and between different organisations. This prevents projects from independently building the same tools, which reduces duplication and lowers costs. Furthermore, it ensures a clear separation between business methods, data, and the underlying technology. This separation is essential for keeping complex IT landscapes manageable and successfully scaling them up. The framework is designed to be used at multiple levels at the same time. It helps with strategic planning, designing specific IT solutions, and monitoring how different projects align with one another. 

The SAF does not replace existing statistical models, but rather works closely alongside them. It forms the connecting link between organisational strategy, business processes, and technology. This connection helps organisations make consistent decisions and makes sure that organisation policy is translated into practice. To improve communication between teams, the SAF uses different visual models. By using a standard notation style, organisations can easily compare and reuse each other's designs. Finally, the SAF is a living framework that will continuously evolve based on practical experience, community feedback, and new technological developments.

## Acknowledgements

TODO

# Introduction

The Statistical Architecture Framework (SAF) provides a common architectural basis for the design, delivery, and evolution of statistical production in National Statistical Institutes (NSIs) and related organisations. It brings together architectural concepts, reference structures, and practical guidance that support consistent decision-making across portfolios and programmes. SAF aims to help statistical organisations modernise with control, while preserving the institutional qualities that make official statistics credible: transparency, quality, impartiality, reproducibility, and public trust.

Statistical organisations are facing a period of accelerated change. Data ecosystems are evolving and increasingly depend on partnerships and shared infrastructures. Artificial intelligence and rapid technological advances are changing how data can be collected, processed, and interpreted, while also introducing new risks and new expectations. At the same time, trust, scientific rigor, and data protection requirements are becoming more prominent and more demanding. These changes occur in an uncertain and fragmented global environment, where information integrity and societal confidence cannot be taken for granted. All of this is happening under sustained resource constraints, requiring organisations to be more agile and deliberate in how they prioritise, reuse, and industrialise capabilities. SAF is intended to support organisations in quickly responding to these drivers without fragmenting their architecture, governance, and implementation landscape in the process.

SAF replaces earlier reference documentation by consolidating core architectural ideas into a single framework that is more usable in practice. It is not designed as a theoretical reference alone. It is designed to be applied. SAF supports the translation of strategy into capabilities, services, and implementation choices. It supports alignment across business, methodology, data, applications, and technology. It also supports collaboration between organisations by promoting common patterns, shared viewpoints, and comparable architectural descriptions.

## Purpose

The purpose of SAF is to provide an authoritative, consistent, and actionable framework for developing and governing statistical architectures. It aims to support coherent modernisation across NSIs by providing shared structures for describing needs, designing solutions, and managing change. SAF helps ensure that investments in platforms, data management, methods, and delivery practices strengthen each other instead of competing. It also helps organisations to demonstrate traceability from policy and strategy to implemented solutions, including the controls required for confidentiality, integrity, accountability, and lawful processing.

SAF is intended to enable better outcomes in three areas. First, interoperability and reuse, both within an organisation and across organisational boundaries.

 Second, quality and robustness, by making architectural choices explicit and reviewable, and by promoting consistent handling of data, metadata, and methodological assets. Third, overall statistical production  effectiveness, by providing a common language and set of expectations that connects architects, methodologists, engineers, managers, and oversight functions.

## Definition of Scope

SAF covers the enterprise architecture concerns that are most relevant to statistical production and dissemination, including the supporting functions that enable them. It addresses the design and evolution of capabilities, information assets, applications and services, and underlying infrastructure and deployment arrangements. It also considers the cross-cutting concerns that are essential for official statistics, such as governance, security, privacy, auditability, reproducibility and the responsible use of data and advanced analytics.

To ensure consistency and practical applicability, SAF is organised according to a TOGAF-aligned structure. It addresses motivation and principles, strategic direction and target outcomes, and the architecture domains that connect intent to implementation. This includes business architecture, data architecture, application architecture, and technology and infrastructure considerations, as well as deployment and operationalisation aspects. SAF also includes viewpoints that are tailored to distinct roles and activities within an NSI, enabling the same underlying architecture to be communicated and assessed from multiple perspectives without losing coherence.

SAF does not prescribe a single operating model, a single technology stack, or a single organisational design. It recognises that NSIs differ in mandate, maturity, and context. Instead, it provides a shared architectural foundation that can be adapted to local realities while remaining comparable across organisations. It also assumes that terminology and detailed definitions are managed through a dedicated glossary, which is maintained alongside the framework.

## Target Audience

This documentation is primarily written for enterprise and data architects, IT architects, methodologists, and IT delivery teams. It is also intended for senior decision-makers such as CIOs and CTOs, and for privacy officers, policy makers, and managers who carry responsibility for compliance, traceability, and responsible data use.

These groups and individuals can use this framework as a reference and as a working instrument. It can be applied when shaping strategy and roadmaps, when designing new capabilities and platforms, and when assessing initiatives for alignment and risk. It can be used to structure architectural work in programmes and projects, and to support governance decisions by making assumptions, dependencies, and trade-offs explicit. It can also be used to support communication across disciplines by establishing shared architectural concepts and consistent viewpoints.

Different roles will use SAF in different ways, while relying on the same underlying content. Enterprise and data architects will use it to define target states, standards, patterns, and architecture decisions across the organisation. IT architects and delivery teams will use it to translate those decisions into solution designs, implementation plans, and operational controls. Methodologists will use it to connect methods and process design to the enabling data and technology arrangements, and to support repeatability and scientific rigor. CIOs, CTOs, managers, and policy makers will use it to understand the implications of strategic choices, to prioritise investment, and to oversee risk and compliance. Privacy officers and assurance functions will use it to assess whether designs incorporate adequate safeguards, traceability, and accountability.

SAF is most effective when it is used consistently across the lifecycle of change. It supports early-stage framing by clarifying drivers, objectives, and constraints. It supports design by providing reference structures and viewpoints that guide architecture development. It supports delivery by improving alignment between architecture and implementation decisions. It supports operation and evolution by making dependencies and responsibilities explicit, enabling controlled change and measurable improvement.

## Expected value

The expected value of SAF is a stronger and more coherent statistical architecture practice across NSIs. It supports faster and safer modernisation by reducing ambiguity and rework. It supports reuse by encouraging common building blocks and comparable solution descriptions. It supports trust by embedding governance and assurance concerns into architecture, rather than treating them as afterthoughts. It also supports collaboration across organisations, where shared approaches to interoperability, data governance, and service orientation reduce the effort required to work together.
In providing a common framework with practical orientation, SAF aims to help statistical organisations remain resilient and responsive. It supports them in delivering high-quality statistics under changing conditions, while maintaining the safeguards and institutional discipline that official statistics require.

## Constraints & Assumptions

### Use of TOGAF and ArchiMate in SAF

The SAF builds on two open standards of The Open Group, a global, vendor-neutral consortium that develops technology and architecture standards: the TOGAF® Standard and the ArchiMate® Specification. This section explains what these standards are, why the SAF uses them, and how they relate to each other and to the statistical standards of the UNECE community.

#### What TOGAF is

The TOGAF Standard is a framework for developing and governing enterprise architecture. It provides:

- **A method.** The Architecture Development Method (ADM) is an iterative cycle of phases. It runs from establishing the architecture capability and an architecture vision, through business, information systems, and technology architecture, to migration planning, implementation governance, and change management.
- **A content framework.** A common structure for the artefacts that architecture work produces, such as principles, stakeholder maps, capability models, and architecture building blocks.
- **Guidance for an architecture capability.** Advice on governance, roles, and maturity, so that architecture becomes a lasting practice rather than a one-off project.

The SAF refers to the TOGAF Standard, 10th Edition. More information is available at [The Open Group: TOGAF Standard](https://www.opengroup.org/togaf).

#### Why the SAF uses TOGAF

The SAF uses TOGAF for three reasons.

- **A shared structure:** Many NSIs already use TOGAF, or a framework derived from it, in their own architecture practice. Aligning the SAF with TOGAF lets NSIs map SAF content onto their existing repositories, governance processes, and training without translation.

- **A proven method:** TOGAF describes how to move from motivation to implementation in controlled steps. The SAF follows the same order: motivation, strategy, business architecture, data, application, and technology architecture, and implementation. This gives NSIs a recognisable path from intent to solution.

- **A common language across organisations:** TOGAF terminology is widely understood by architects, IT suppliers, and international partners. Using it reduces ambiguity when NSIs compare architectures or collaborate on shared solutions.

The SAF uses TOGAF as a **structuring reference, not as a prescription**. It tailors the TOGAF structure to official statistics and does not require NSIs to follow every ADM phase or to hold TOGAF certification. The SAF does not reproduce TOGAF content; readers are referred to the standard for its full description.

#### What ArchiMate is and how it relates to TOGAF

ArchiMate is a modelling language for enterprise architecture. Where TOGAF describes *how* to develop an architecture and *which* content to produce, ArchiMate describes *how to express* that content in consistent, unambiguous models and views. The two standards are maintained by The Open Group and are designed to work together:

| Aspect | TOGAF | ArchiMate |
|---|---|---|
| Nature | Framework and method | Modelling language and notation |
| Answers | How is architecture developed and governed? | How is architecture described and visualised? |
| Main content | ADM phases, content framework, architecture capability | Elements, relationships, viewpoints |
| Role in the SAF | Structures the chapters and the order of the framework | Notation for the models and diagrams in the SAF |

The structures of the two standards correspond. The TOGAF Preliminary Phase, Phase A, and Requirements Management correspond to the ArchiMate motivation and strategy elements. TOGAF Phases B, C, and D correspond to the ArchiMate business, application, and technology layers. TOGAF Phases E to H correspond to the ArchiMate implementation and migration elements. This correspondence is the basis for the position of each SAF chapter. The figure groups the ADM phases in three areas:

- **Strategy and Motivation:** the Preliminary Phase, Phase A (Architecture Vision), and Requirements Management.
- **Core layers:** Phases B, C, and D, which produce the Business, Application (Information Systems), and Technology architectures.
- **Implementation and Migration:** Phases E to H, which plan, govern, and change the realisation of the architecture.

|**PLACEHOLDER: Logical model of the different layers to be added**|
|---|

More information is available at [The Open Group: ArchiMate](https://www.opengroup.org/archimate-forum).

#### Relationship with statistical standards

TOGAF and ArchiMate are generic standards. The SAF complements them with the standards of the statistical community: GSBPM for statistical business processes, GAMSO for the activities of statistical organisations, GSIM for statistical information objects, and SDMX for the exchange of statistical data and metadata. TOGAF and ArchiMate provide the architectural structure and notation; the statistical standards provide the domain content. The SAF connects the two.

#### Assumptions and constraints

| ID | Type | Statement |
|---|---|---|
| SAF-A1 | Assumption | The SAF is structured according to the TOGAF Standard, 10th Edition, tailored to official statistics. |
| SAF-A2 | Assumption | Models and diagrams in the SAF use the ArchiMate 3.2 Specification. Alignment with the ArchiMate 4 Specification will be assessed in a later version of the SAF. |
| SAF-A3 | Assumption | NSIs can apply the SAF without TOGAF or ArchiMate certification. Basic familiarity with both standards helps but is not required. |
| SAF-A4 | Assumption | Terminology and definitions are maintained in a separate SAF glossary, which takes precedence over definitions in this document. |
| SAF-C1 | Constraint | The SAF refers to TOGAF and ArchiMate but does not reproduce their content. Use of the standards is subject to the licence terms of The Open Group. |
| SAF-C2 | Constraint | The SAF does not prescribe a technology stack, tool, or organisational design (see *Definition of Scope*). |

TOGAF and ArchiMate are registered trademarks of The Open Group.

## Reading guide

This reading guide explains how the SAF is built, in which order to read it, and how an NSI can start using it. It also explains how the SAF fits into an NSI's own architecture, how it combines with other reference models, and how legislation enters the architecture.

### 1. How the SAF is structured

The SAF follows the layers of TOGAF and ArchiMate (see *Constraints & Assumptions*). Each layer answers one question. Each layer is justified by the layer above it, and each layer gives direction to the layer below it.

|**PLACEHOLDER: Overview of the SAF layers and chapters**|
|---|

| Chapter | Question it answers | Main content | Status **[RG4]** |
|---|---|---|---|
| Motivation | *Why* does the NSI change, and what does it want to achieve? | Stakeholders, drivers, assessments, goals, outcomes, principles, requirements, constraints, meaning, value | Developed |
| Strategy | *What* must the NSI be able to do, and how does it get there? | Capability model, value streams, resources, courses of action and strategies | Developed |
| Business Architecture | *How* is the statistical work organised? | Business domains, reference models for the data value chain (Steady-State, Medallion), steady states, value stream detail, roles | In development |
| Data Architecture | *Which* data and metadata are needed, and how are they structured? | To be developed | Planned |
| Application Architecture | *Which* applications and services support the work? | To be developed | Planned |
| Technology Architecture | *On which* platforms and infrastructure does it run? | To be developed | Planned |
| Implementation and Tooling | *How* is the architecture realised and governed? | To be developed | Planned |

Every section that describes an architecture concept follows the same pattern:

1. **The concept.** What the concept means, based on ArchiMate and TOGAF.
2. **How the SAF applies it.** Why the SAF uses the concept, and how it fits into an NSI's own architecture.
3. **Relationships with other concepts.** How the concept connects to the rest of the framework.
4. **SAF elements or examples.** The reference content of the SAF, or illustrative examples where the content is specific to each NSI.
5. **Toolkit.** A reference to templates and instruments in the SAF toolkit.

This pattern makes it possible to read a single section without reading the whole document, and still see how it connects to the rest.

The SAF contains two kinds of content. **Reference content** is shared by most NSIs and can be adopted directly, such as the drivers, goals, principles, capability model and value streams. **Illustrative content** shows the form of elements that each NSI defines for itself, such as assessments, requirements, constraints, resources and courses of action. Illustrative content is never a requirement.

### 2. Reading order

The SAF is best read top-down, at least once: from Motivation, through Strategy, to the architecture domains. This order follows the logic of the framework. A business architecture choice only makes sense once the goals and capabilities behind it are clear.

Applying the SAF is different from reading it. Application is iterative. An NSI does not complete the Motivation layer before it starts on its business architecture. It works in cycles, like the TOGAF Architecture Development Method: each cycle refines the motivation, strategy and architecture a little further, and each change in a driver or goal can start a new cycle.

Different readers can follow different routes through the document (see *Target Audience* for the roles).

| Reader | Start with | Then read | Focus |
|---|---|---|---|
| CIO, CTO, board member | Introduction, Motivation | Strategy: capability model, courses of action | Why change is needed, what it delivers, how to prioritise |
| Enterprise or data architect | Introduction, Motivation | Strategy, Business Architecture, later domains | The full chain, and how to adopt it in the NSI architecture |
| IT architect, delivery team | Motivation: principles | Business Architecture, later domains | Design rules and reference models for solutions |
| Methodologist | Strategy: value streams | Business Architecture: steady states | Where methods are applied, and how quality and lineage are secured |
| Privacy officer, auditor | Motivation: principles, constraints | Business Architecture: steady states; VS-07 | Where protection and compliance are built into the chain |
| Policy maker, manager | Introduction, Motivation: goals, value | Strategy: courses of action | What the framework means for the organisation |

### 3. Positioning the SAF in your own architecture

TOGAF describes a range of architectures, from generic to specific, called the *Enterprise Continuum* **[RG2]**. It runs from foundation architectures, which apply to any organisation, through common systems and industry architectures, to the architecture of one specific organisation.

| Level in the Enterprise Continuum | Example | Who owns it |
|---|---|---|
| Foundation architecture | TOGAF, ArchiMate | The Open Group |
| Common systems architecture | Generic reference architectures for, for example, data platforms or identity management | Industry and standards bodies |
| Industry architecture | **The SAF**, for official statistics | UNECE statistical community |
| Organisation-specific architecture | The enterprise architecture of an NSI | The NSI |

The SAF is an industry architecture. It is not the architecture of any single NSI. Each NSI builds its own organisation-specific architecture, using the SAF as its reference. In practice, this works as follows:

1. **Adopt, adapt or extend.** For each SAF element, the NSI decides whether to adopt it as it is, adapt it to the national context, or add NSI-specific elements:
    - **Adopt.** Use an SAF element as is, when it matches the national situation.
    - **Adapt.** Refine an SAF element with national specifics, such as a national statistics act or a government-wide digital strategy.
    - **Extend.** Add elements that are specific to the NSI, while keeping a reference to the closest SAF element where one exists.

    The decisions are recorded in SAF-TK-G02 Adoption register.
2. **Keep the SAF identifiers.** When an NSI adapts an SAF element, it keeps a reference to the SAF identifier, for example SAF-P07 or capability 2.1.2. This keeps the NSI architecture comparable with the SAF and with other NSIs, and makes it easier to adopt future SAF versions.
3. **Layer the architecture.** The NSI enterprise architecture sets the direction for solution architectures in programmes and projects. Solution architectures do not refer to the SAF directly, but to the NSI architecture that applies it.

|**PLACEHOLDER: From SAF reference architecture to NSI enterprise architecture to solution architecture**|
|---|

### 4. Combining the SAF with other reference models

The SAF rarely stands alone. NSIs also work with statistical standards, with reference models of their own government, and with generic frameworks. These models complement each other, but they can also overlap or conflict.

| Family | Examples | Role next to the SAF |
|---|---|---|
| Statistical standards and models | GSBPM, GAMSO, GSIM, SDMX; the ESS Enterprise Architecture Reference Framework (ESS EARF) | Provide the statistical domain content. The SAF connects them in one architecture |
| Government reference models | The European Interoperability Framework (EIF) and Reference Architecture (EIRA); national reference models such as those listed below | Often mandatory or leading for public organisations. The SAF fits within them |
| Generic frameworks and bodies of knowledge | TOGAF, ArchiMate, DAMA-DMBOK | Provide structure, notation and professional practice |

Examples of national government reference models **[RG3]**:

| Country | Reference model | Owner |
|---|---|---|
| Netherlands | NORA, Netherlands Government Reference Architecture | Dutch government (ICTU) |
| United Kingdom | GovS 005 Digital, Government Functional Standard | Cabinet Office, Government Digital and Data |
| Canada | Government of Canada Enterprise Architecture Framework | Treasury Board of Canada Secretariat |
| Australia | Australian Government Architecture (AGA) | Digital Transformation Agency |
| New Zealand | Government Enterprise Architecture for New Zealand (GEA-NZ) | Government Chief Digital Officer |
| Norway | National architecture principles for digitalisation of the public sector | Norwegian Digitalisation Agency (Digdir) |
| United States | Federal Enterprise Architecture Framework (FEAF) | Office of Management and Budget |

The SAF works best when the NSI combines models at the level of elements, not documents:

- **Principles.** Map the SAF principles to the principles of the national reference model. Many will be equivalent. Where both exist, the NSI uses one set and records the mapping.
- **Capabilities and functions.** Map the SAF capability model to the capability or function model of the national framework, where one exists. This makes the NSI comparable with other government organisations as well as with other NSIs.
- **Standards.** Check which standards the national model prescribes, for example for exchange formats, identity or security. These standards become requirements or constraints in the NSI architecture.

When models conflict, a simple order of precedence helps:

1. Legislation comes first.
2. Mandatory government standards and reference models come next.
3. Within the statistical domain, the SAF and the statistical standards apply.
4. Generic frameworks and practices fill the remaining gaps.

A deviation from a higher level is a decision for the NSI's architecture governance, and is documented.

| **Toolkit:** SAF-TK-G03 Reference model mapping |
|---|

### 5. Legislation and regulation

Official statistics operate under strict legal frameworks. Legislation shapes what an NSI may collect, how it must protect data, and how it must publish. The SAF does not describe legislation, because it differs per country. It does describe where legislation enters the architecture.

Legislation enters the architecture through the motivation elements:

| A legal provision that… | Is recorded as… | Example |
|---|---|---|
| Creates pressure to change | Driver | A new regulation that requires access to privately held data for statistics |
| Sets a limit on the design | Constraint | Statistical microdata may only be processed within the NSI's controlled environment |
| Imposes an obligation on a solution | Requirement | Personal data in a data acquisition process is minimised to what is needed |
| Expresses a lasting rule for all decisions | Principle | Privacy by design (SAF-P11) |

This approach makes legislation traceable. From a legal provision, the NSI can follow the path to the requirements and constraints it creates, to the solutions that meet them, and to the evidence that shows compliance. In the other direction, every design decision that is driven by law can be traced back to its legal basis.

Three levels of legislation are relevant for most NSIs:

| Level | Examples |
|---|---|
| International statistical frameworks | UN Fundamental Principles of Official Statistics; European Statistics Code of Practice; Regulation (EC) No 223/2009 on European statistics |
| Horizontal EU legislation | GDPR; Data Governance Act; Data Act; AI Act; NIS2 Directive; Interoperable Europe Act (Regulation (EU) 2024/903) |
| National legislation | National statistics act; archives legislation; national rules on government information security and open government |

For NSIs outside the EU, the horizontal level consists of the corresponding national or regional legislation.

Compliance is not a separate layer. It is built into the architecture: legal requirements are part of the quality gates of the steady states, of the principles, and of the governance in value stream VS-07 *Governance and Compliance*. A legal register helps to keep the overview: a list of applicable legal provisions, with the drivers, constraints, requirements and principles they lead to.

| **Toolkit:** SAF-TK-G04 Legal register |
|---|

### 6. Conventions used in this document

| Convention | Meaning |
|---|---|
| SAF-ST, SAF-D, SAF-G, SAF-O, SAF-P, SAF-M, SAF-V | Identifiers of reference elements in the Motivation layer |
| 1.2.1, 2.1.2, … | Capability numbers in the capability model |
| VS-01 to VS-10, VS-01.1, … | Value streams and their stages |
| #0 to #6 | Steady states of data and their boundary positions |
| SAF-A, SAF-C | Assumptions and constraints of the SAF itself (see *Constraints & Assumptions*) |
| *Illustrative* | Examples that show the form of an element. They are not requirements |
| PLACEHOLDER | Content that will be added, such as an ArchiMate view or a figure |
| Toolkit (planned) | A toolkit instrument that does not exist yet; it is listed in *Planned instruments* in the Toolkit |
| Toolkit | The SAF toolkit, a separate set of templates and instruments for applying the framework |

Terms are defined in the SAF glossary, which takes precedence over definitions in this document (SAF-A4). The SAF uses British English spelling.

# Motivation

## Purpose of this chapter

The Motivation chapter explains why the SAF exists. It also explains why architecture decisions in an NSI are taken the way they are. It records the forces that act on statistical organisations, the results they want to achieve, the rules that guide their decisions, and the parties whose concerns must be addressed.

Without an explicit motivation, architecture is a set of models without a reason. With it, every capability, process, data state, application or platform choice can be traced back to a need and a result. That traceability makes architecture defensible, whether in a governance board, a budget discussion or an international review.

## Position in the framework

Motivation is the first layer of the SAF and the foundation for the other layers. The Strategy layer translates motivation into capabilities and value streams. The architecture domains (business, data, application and technology) then translate strategy into design. In TOGAF terms, motivation sits in the Strategy and Motivation area at the start of the ADM cycle (see *Use of TOGAF and ArchiMate in SAF*). It holds the content that TOGAF produces before any architecture domain is designed, and that content keeps steering the architecture in all later phases.

| ADM phase | Role of motivation in this phase | SAF sections |
|---|---|---|
| Preliminary | Establish the architecture capability: who the architecture serves and which rules guide decisions | Stakeholders, Architecture Principles |
| A. Architecture Vision | Explain why change is needed, what must be achieved and what value it brings | Drivers, Goals, Outcomes, Meaning, Value |
| Requirements Management | Turn goals into requirements and constraints, and keep them traceable through every phase | Requirements, Constraints |
| B, C, D. Core architectures | Justify design choices in business, application and technology architecture | Traceability from each design decision back to a goal and a driver |
| E to H. Implementation & Migration | Prioritise solutions and work packages; reassess when drivers change | Drivers and goals as criteria for prioritisation and change requests |

Three consequences follow from this position.

- **Motivation comes first.** In TOGAF, no architecture domain is designed until stakeholders, drivers, goals and principles are agreed. The SAF follows the same order. Every later element must be traceable to the motivation.
- **Motivation stays active throughout the cycle.** In Requirements Management, at the centre of the ADM, goals are refined into requirements, and those requirements are checked in every phase. Motivation is the reference against which each architecture decision is tested, not a one-off introduction.
- **Motivation closes the loop.** In Phase H (Architecture Change Management), a new or changed driver, such as a new regulation or a new data source, triggers a change request. The cycle then returns to the Preliminary Phase or Phase A, and the motivation elements become the starting point of the next iteration.

The Strategy layer shares the Strategy and Motivation area with the Motivation layer. Motivation explains *why*. Strategy describes *what* the NSI must be able to do (capabilities) and *how* it creates value (value streams). Strategy is the bridge to Phase B, Business Architecture.

## How NSIs use this chapter

The motivation elements in this chapter are a reference set. They describe internal and external forces and intentions that most NSIs share. Modelling the motivation layer is not mandatory, but the SAF strongly recommends it. Most NSIs have a motivation, but it is implicit: it lives in strategy documents, board decisions and the experience of staff, and is rarely connected to architecture decisions. Making it explicit, in SAF terms, helps an NSI in four ways.

- **It justifies investment.** If every programme can be traced to a driver and a goal, an investment proposal rests on shared reasoning, not on individual preference. Boards and ministries can see what a proposal responds to, and what is at stake if it is not funded. The same links set priorities: work that addresses several drivers, or contributes to a key outcome, comes before work that addresses none.
- **It makes decisions consistent.** Principles turn intentions into decision rules, so similar questions get similar answers, whichever team or architect is involved. When circumstances change, for example through new legislation, the documented links show which goals, principles and capabilities are affected, and the NSI can review those decisions instead of starting over.
- **It preserves knowledge.** Staff move on and projects end. A documented motivation keeps the reasoning behind past decisions available, so new staff can see why the architecture looks the way it does.
- **It supports collaboration between NSIs.** With the same concepts and identifiers, NSIs quickly see where their interests overlap. That makes it easier to start joint projects, share components and compare approaches. A documented motivation is also useful evidence in external assessments, such as peer reviews.

An NSI adopts, adapts or extends each SAF motivation element (see *Positioning the SAF in your own architecture* in the Reading guide). The Toolkit instrument named in the table below supports each step.

| **Toolkit (planned):** Modernisation maturity scan (see *Planned instruments* in the Toolkit) |
|---|

## Motivation concepts in the SAF

| SAF section | ArchiMate element | What it is | SAF content | Toolkit |
|---|---|---|---|---|
| Drivers | Driver | An external or internal condition that motivates an organisation to set goals and to change. A force, not a problem and not a solution. | Reference: SAF-D1 to SAF-D5 | SAF-TK-M02 |
| Goals | Goal | A statement of intent: the direction or end state an organisation wants to achieve. It says *what*, not *how* or *how much*. | Reference: SAF-G1 to SAF-G5 | SAF-TK-M04 |
| Meaning | Meaning | The knowledge or interpretation a concept has in a given context: *what does this signify?* | Reference: SAF-M1 to SAF-M4 | SAF-TK-M09 |
| Outcomes | Outcome | An end result that has been, or is intended to be, achieved: what will be different once a goal has been followed. | Reference: SAF-O1 to SAF-O6 | SAF-TK-M05 |
| Architecture Principles | Principle | A durable, general rule that guides how an organisation designs, builds and changes its information provision, for all decisions within its scope. | Reference: SAF-P01 to SAF-P11 | SAF-TK-M06 |
| Value | Value | The worth, usefulness or importance of something to a stakeholder: *what is it worth, and to whom?* | Reference: SAF-V1 to SAF-V6 | SAF-TK-M09 |
| Assessment | Assessment | The result of analysing a driver for one organisation: what the driver means for it today. | Defined by each NSI | SAF-TK-M03 |
| Requirements | Requirement | A statement of need that a specific solution, process or platform must meet to contribute to a goal. | Defined by each NSI | SAF-TK-M07 |
| Constraints | Constraint | A factor that limits how goals can be realised: the boundaries within which a solution must be built. | Defined by each NSI | SAF-TK-M08 |
| Stakeholders | Stakeholder | An individual, group or organisation with an interest in the effects of the architecture **[R8]**, with concerns such as cost, risk, quality or compliance. | Reference: SAF-ST01 to SAF-ST07 | SAF-TK-M01 |

The concepts form a chain. Stakeholders have concerns about drivers. An assessment records what a driver means for one NSI. Drivers motivate goals. Outcomes make goals measurable. Principles guide how goals are pursued, and requirements and constraints make them concrete for a solution. Meaning and value express why the result matters to stakeholders.

### Relationships between the motivation elements

| Element | Relationship | Example in the SAF |
|---|---|---|
| Stakeholders → Drivers | Stakeholders have concerns about drivers and often raise them | CIOs and CTOs (SAF-ST01) raise resource constraints (SAF-D5) |
| Assessment → Drivers | An assessment analyses a driver for one NSI | "Two thirds of our processing runs on platforms out of vendor support" assesses SAF-D5 |
| Drivers → Goals | Drivers motivate goals | Resource constraints (SAF-D5) motivate cost efficiency (SAF-G1) |
| Drivers → Principles | Drivers explain why a principle exists | Trust and data protection (SAF-D3) explain privacy by design (SAF-P11) |
| Drivers → Constraints | Some drivers are the origin of constraints | SAF-D3 is the origin of data protection constraints |
| Assessment → Goals | Assessments influence which goals an NSI sets and how it prioritises them | A weakness on SAF-D5 makes modernisation (SAF-G3) a priority |
| Outcomes → Goals | Outcomes make goals measurable | Increased efficiency (SAF-O5) shows progress on cost efficiency (SAF-G1); improved interoperability (SAF-O3) on the harmonised reference framework (SAF-G2) |
| Assessment → Outcomes | A new assessment shows whether outcomes have been reached | The share of unsupported platforms falls after a modernisation programme (SAF-O1) |
| Principles → Goals | Principles guide how goals are pursued | Open-source participation (SAF-P01) guides cost efficiency (SAF-G1); loose coupling (SAF-P07) guides modernisation (SAF-G3) |
| Stakeholders → Goals | Stakeholders own goals | CIOs and CTOs (SAF-ST01) and NSIs (SAF-ST05) own modernisation (SAF-G3) |
| Requirements → Goals, Outcomes | Requirements make goals concrete for a solution and make outcomes measurable in it | SAF-G4 leads to a requirement for automated testing in the production pipeline; lineage recording contributes to SAF-O2 |
| Requirements → Principles | Requirements apply principles to a specific solution | SAF-P09 becomes the requirement that no dataset is handed over without its minimum metadata **[R5]** |
| Constraints → Goals, Requirements, Principles | Constraints limit how goals can be realised, bound the solutions that can meet a requirement, and set the limits within which principles apply | A ban on public cloud for statistical microdata limits SAF-G3; a scalability requirement must be met on premises; SAF-P01's reuse–open source–buy–build order applies within public procurement rules |
| Stakeholders → Constraints | Stakeholders often own or impose constraints | A privacy officer applies data protection law; a ministry sets the budget |
| Outcomes → Value | Outcomes deliver value to stakeholders | Enhanced data quality (SAF-O2) delivers trust and legitimacy (SAF-V6); improved interoperability (SAF-O3) delivers cross-border comparability (SAF-V1) |
| Meaning → Value, Goals | Meaning explains how value is interpreted and frames how goals are understood | The SAF as common language (SAF-M4) explains why cross-border comparability (SAF-V1) is achievable; the SAF as bridge between strategy and technology (SAF-M1) underpins strategic alignment (SAF-V4); the SAF as foundation for transformation (SAF-M3) frames modernisation (SAF-G3) |
| Stakeholders → Meaning, Value | Meaning is shaped for and by stakeholders; stakeholders perceive value | IT and data professionals (SAF-ST04) read the SAF through its notation (SAF-M4); policy makers (SAF-ST03) value trust and legitimacy (SAF-V6); researchers (SAF-ST06) value innovation enablement (SAF-V2) |
| Stakeholders → Viewpoints | Stakeholder concerns determine which views are produced | Privacy officers need data-flow and protection views |
| Stakeholders → Business actors and roles | A stakeholder may also act in the architecture | Data providers are stakeholders and actors in VS-01 |
| Meaning → Glossary | The meaning of individual terms is recorded in the glossary | The definition of "steady state" |
| Capabilities (Strategy) | Capabilities are developed in response to drivers, through goals, and realise goals and outcomes; a capability maturity assessment is a structured form of assessment | AI and technological acceleration (SAF-D2) drives investment in methodology (2.2.3), which supports data innovation (SAF-G4); metadata management (2.1.2) realises enhanced data quality (SAF-O2); a low score on 2.1.2 |
| Value streams (Strategy) | Value streams show where a driver or goal affects the production chain, produce outcomes and create value stage by stage; each applies a subset of the principles | SAF-D1 affects data acquisition (VS-01); sustainable compliance (SAF-G5) is put into practice in VS-07; the steady-state handovers in VS-01 to VS-06 contribute to SAF-O3; VS-06 delivers released statistics to users; VS-07 enforces SAF-P09, P10 and P11 across the chain |
| Steady states (Steady-State Architecture) | Principles shape the design rules; quality gates make outcomes observable; gate criteria and minimum metadata work as reusable requirements | SAF-P07, P08, P09 and P11 underpin the design rules; lineage and metadata per state provide evidence for SAF-O2; the criteria for registering data in State #1 |

### Elements defined by each NSI

The SAF does not define assessments, requirements or constraints, because they depend on the situation, the solution and the maturity of each NSI. It describes how they are used, and the Toolkit provides templates and illustrative examples.

**Assessment.** An assessment records what a driver means for one NSI: a strength, a weakness, an opportunity or a threat. A driver describes a force; an assessment describes how that force affects this NSI, today. Assessments are specific to one organisation ("two thirds of our processing runs on platforms out of vendor support"), based on evidence such as an application portfolio scan, an audit finding, a maturity assessment or a staff survey (an opinion without evidence is not an assessment), and they change as the NSI acts on them, so they are reviewed regularly, for example once a year. A generic assessment would contradict the concept itself. Assessments are the link between the generic SAF drivers and the goals of an NSI. Without them, an NSI jumps from "the world is changing" straight to "we must modernise", and nobody can see why this particular goal has priority. An assessment also gives a baseline: if the next assessment of the same driver is better, the NSI can show progress. Assessments are produced in the *Assess* step of applying drivers, often as a SWOT analysis, and feed the *Respond* step, in which the NSI derives or confirms its goals. In TOGAF terms, they are part of Phase A and of the baseline description of each architecture domain.

**Requirements.** A goal says what the NSI wants to achieve; a requirement says what a specific solution, process or platform must do or provide to contribute to it. Requirements apply to a specific solution ("the new processing platform records the lineage of every registered dataset"), are testable in an architecture review or an acceptance test, and are derived, not invented: a requirement that cannot be traced to a goal, an outcome or a principle needs a justification. Principles and goals are deliberately general and only change a design when they are made concrete. Requirements connect the motivation layer to the architecture domains, and let an architecture board test whether a solution really contributes to the goals it claims to serve. In TOGAF, they are managed in Requirements Management and checked against each architecture decision. An NSI derives them from goals and outcomes, from principles, and from SAF reference content. The SAF already contains content that works as requirements: the quality gate and minimum metadata set of each steady state, which an NSI that adopts the steady-state model can use directly for the processes and platforms that produce and store each state, and the principle tables of each value stream.

**Constraints.** A requirement describes what a solution must do; a constraint describes the boundaries within which it must be done. Constraints are usually not chosen by the architect. They limit the solution space ("personal data may not be processed outside the EU" excludes certain cloud services, whatever their other merits), they come from outside the design (legislation, government policy, budget, staffing, existing contracts, technical dependencies), and they differ in how fixed they are: a legal constraint cannot be negotiated, a budget or policy constraint may change, so recording the source shows which ones can be challenged. Constraints that stay implicit cause late surprises in a procurement, a privacy assessment or a security review. Recording them early, and linking them to the goals they affect, keeps the architecture realistic and makes trade-offs visible: when a constraint blocks a goal, the board can accept that or challenge the constraint. In TOGAF, constraints are identified in Phase A and managed with requirements in Requirements Management. These are constraints on an NSI's own architecture, different from the *Constraints & Assumptions* of the SAF itself (SAF-C1, SAF-C2). Some apply to almost every NSI, such as data protection law and the statistical confidentiality required by national statistical law. *Definition of Scope* leaves the technology stack and organisational design to the NSI and its constraints, and SAF-P10 and SAF-P11 point to the legal and security frameworks that usually impose constraints.

## Drivers

Drivers make the SAF a response to real pressures instead of an abstract ideal. With them, an NSI can explain to its board, its ministry or a peer review why change is needed, and what happens without it. They also help to set priorities: an investment that responds to several drivers deserves more attention than one that responds to none. "Rapid technological change" is a driver. "Our methods cannot use administrative data" is an assessment of that driver for one NSI. "Integrate new data sources into production" is a goal.

Drivers exist independently of the NSI: an NSI can respond to a driver, but cannot decide whether it exists. External drivers come from technology, legislation, society, politics or the economy; internal drivers from legacy systems, skills or organisational structure. Drivers are relatively stable and usually stay relevant for several years; short-lived events, such as an incident or a budget round, are recorded as assessments. The SAF drivers are common to the UNECE statistical community.

### SAF drivers

| ID | Driver | Type | Description | Architectural response in the SAF |
|---|---|---|---|---|
| **SAF-D1** | Evolving data ecosystems and partnerships | External | Official statistics move from isolated data collection to a wider data ecosystem. Surveys now sit next to administrative, commercial, platform and community data. This opens up new forms of collaboration, but makes NSIs dependent on actors, technologies and infrastructures they do not control. Open source is part of this ecosystem: a shared base for innovation, transparency and lower costs, developed with peers, academia and private partners. | Architectures for secure data sharing, standard interfaces and transparent governance, so that NSIs can take part in national data platforms and European data spaces, where production may span several environments and jurisdictions. Openness is combined with strong governance and clear accountability, so that collaboration does not compromise the integrity of official statistics. |
| **SAF-D2** | Artificial intelligence and technological acceleration | External | AI, automation and rapid technological progress change how data is created, processed and used. New tools can automate routine tasks, improve analysis and strengthen quality assurance, but raise the question of what relevant and trusted statistics mean when users rely on intelligent systems. NSIs must both use AI and make their outputs usable by AI: internally through automation, machine learning and advanced analytics within secure and transparent limits; externally through statistics that are machine-readable, machine-understandable and interoperable with the platforms of policy makers, researchers and citizens. | A risk-based approach: processes that demand methodological rigour and control stay tightly governed, less sensitive areas can be automated further. Modular, standards-based design lets an NSI adopt new technology at its own pace, while it stays fully accountable for quality, data protection and independence. |
| **SAF-D3** | Trust, scientific rigour and data protection | External | Trust is the basis of official statistics. Misinformation, privacy concerns and unregulated data providers put it under pressure. Compliance alone does not maintain public confidence; scientific rigour, transparency and clear accountability for the handling of data are also needed. | Trust and protection built into the architecture: governance and technical controls that protect confidentiality, keep methods sound and make processes traceable. Oversight is strict where sensitivity and quality demands are high; where risks are lower, more automation and shared solutions are possible. |
| **SAF-D4** | Uncertain and polarised global environment | External | Global tensions, political polarisation and shifting power relations affect how official statistics are demanded and perceived. Cross-border data flows require statistical systems to stay open and interoperable, without giving up national and institutional integrity. | A stable base for cooperation: interoperable architectures based on shared standards let NSIs exchange data and methods securely. Design principles that protect independence and transparency help NSIs stay credible and comparable, even when facts themselves are contested. |
| **SAF-D5** | Resource constraints and organisational agility | Internal and external | Many NSIs must do more with limited budgets, ageing systems and a shortage of specialist staff, while demand for timely, detailed and cross-domain output keeps growing. Meeting that demand requires efficiency and the ability to adapt quickly. | Flexibility and reuse as core principles: modular design, shared services and scalable solutions that reduce duplication. Clear governance of priorities lets NSIs shift capacity, modernise step by step and keep delivering quality output under financial and staffing pressure, without large reinvestment. |

| **Toolkit:** SAF-TK-M02 Driver recognition |
|---|

## Goals

Goals define what success looks like, for the SAF and for the NSIs that apply it. They give direction to the Strategy layer: capabilities and value streams are developed because they contribute to a goal. Without explicit goals, modernisation can turn into a series of technical upgrades that nobody can explain.

Goals are qualitative and directional: "modernise statistical systems" sets a direction, while a measurable result such as "retire all platforms out of vendor support by 2029" is an outcome. They are long-term, usually spanning several planning cycles and outliving individual programmes, and they only have meaning if a stakeholder recognises them as their intention. The SAF goals are shared by the UNECE statistical community and cover operational and strategic needs. Some focus on efficiency, modernisation and compliance, which keep an NSI sustainable. Others support innovation and collaboration, such as the use of new data sources or advanced analytics. Together they make sure that modernisation does not weaken the core values of official statistics: neutrality, accuracy and reliability.

### SAF goals

| ID | Goal | Description | Architectural direction in the SAF |
|---|---|---|---|
| **SAF-G1** | Cost efficiency and resource sharing | Budgets are limited and demand keeps growing, so NSIs must work as efficiently as possible. By sharing services, reusing solutions, improving interoperability and pooling resources, NSIs gain capabilities they could not build alone and avoid duplicate work. Efficiency then supports quality and long-term sustainability instead of competing with them. | Shared services, reusable components, and open-source components and community platforms where they improve transparency, collaboration and cost. Modular architectures and clear governance let NSIs adapt to new needs, shift capacity and modernise step by step, without large reinvestments. |
| **SAF-G2** | Harmonised reference framework | Without a shared architectural reference, NSIs build isolated solutions that reduce comparability and raise long-term costs. The SAF offers a common base of standards, patterns and practices that NSIs adapt to their own context while staying interoperable across borders and domains. | Common reference models and consistent design principles. Collaboration increasingly takes place on shared infrastructures, such as national data platforms and international data spaces, and harmonisation is a condition for taking part. Consistent principles help NSIs protect the integrity of official statistics and reuse shared and open solutions safely. |
| **SAF-G3** | Modernisation of statistical systems | Many NSIs still depend on fragmented legacy IT that slows down innovation and response. Moving to modular, service-based architectures that are secure, scalable and easier to maintain reduces technical debt, improves reliability and speeds up the delivery of new and better statistics. | Service-based design. Modernisation more often happens with several parties, from national infrastructures to cross-border data spaces, so the SAF sets principles for access control, data protection and accountability in those settings. A risk-based approach to automation: critical processes stay tightly governed to protect methodological rigour; less sensitive steps can be automated or shared. |
| **SAF-G4** | Support for data innovation | New data and methods are central to the future of official statistics, yet many NSIs struggle to introduce a new source or product: their production systems are built for predictability and stability, qualities that are necessary but slow down change. New sources, methods and products must enter production without loss of quality or consistency. | Architectures that combine robustness with flexibility. Versioning, validation and automated testing keep production reliable as it changes. Shared platforms and processes help prototypes move into operational use. Open source lets NSIs build on each other's work, supported by patterns for the safe reuse of open components. |
| **SAF-G5** | Sustainable compliance | Compliance with laws, standards and ethical principles underpins the trust in and legitimacy of official statistics. Statistical production is now part of a wider data and technology ecosystem, so compliance must extend beyond statistical standards, inside and outside the statistical domain. | GSBPM, GSIM and SDMX remain the basis for consistent processes, metadata management and data exchange, combined with relevant standards for data management, AI and cloud, so that NSIs stay interoperable with modern platforms. With consistent governance and open, verifiable technology, compliance is designed in from the start and becomes an enabler: innovation, data sharing and collaboration take place in controlled and auditable environments, with transparency, scientific rigour and privacy by design in every process. |

| **Toolkit:** SAF-TK-M04 Goal alignment |
|---|

## Meaning

Meaning answers the question *what does this signify?* Value answers a different question: *what is it worth, and to whom?* The SAF uses meaning at the level of the framework itself: the meaning elements describe how the statistical community should understand the SAF. Architecture frameworks are easily misread. IT staff may see a technical blueprint; managers may see administrative overhead. Explicit meaning elements set the intended interpretation, so that all stakeholders read the framework in the same way.

Two interpretations matter most. First, the SAF connects strategy and technology: every technology decision, from a new platform to a redesigned process, can be traced to a strategic objective. Next, the SAF is a common language for the UNECE statistical community: shared models, practices and principles reduce duplicate work and make collaboration easier. This makes the SAF relevant beyond IT, to statisticians, policy makers and the citizens who depend on reliable statistics and information.

### SAF meaning elements

| ID | Meaning | Description |
|---|---|---|
| **SAF-M1** | Bridge between strategy and technology | The SAF links strategic objectives, such as relevance and efficiency, to technology choices. IT investments are justified by what they contribute to the mission. |
| **SAF-M2** | Catalyst for collaboration | The SAF is a common framework for the statistical community. It makes joint platforms, interoperable systems and harmonised standards possible, and strengthens what UNECE members can do together. |
| **SAF-M3** | Foundation for digital transformation | The SAF is more than a set of technical models. It is the basis for digital transformation in official statistics, without loss of methodological rigour or institutional trust. |
| **SAF-M4** | Common language and notation | Through TOGAF and ArchiMate, stakeholders share one language and notation. This reduces misunderstanding and raises architectural maturity across the community. |

| **Toolkit:** SAF-TK-M09 Value and meaning brief |
|---|

## Outcomes

Outcomes show stakeholders what adopting the framework returns. They connect long-term goals to concrete changes in capabilities, processes and systems, and make progress measurable, for one NSI and across the community. Outcomes are results, not activities: "introduce a metadata catalogue" is an activity, "every registered dataset has complete metadata and lineage" is an outcome. They are measurable, or at least observable, because an outcome without an indicator cannot be used to steer. Capabilities, value streams and solutions exist to produce them.

SAF outcomes are technical as well as societal. On the technical side, NSIs gain simpler processes, better metadata management and faster system development. On the societal side, the SAF supports trust, transparency and comparability, which informed policy and public accountability depend on. Outcomes also change over time: as an NSI matures, it sets new targets and adjusts its course. The indicative measures below are examples and the starting point of SAF-TK-M05.

### SAF outcomes

| ID | Outcome | Description | Indicative measures (illustrative) |
|---|---|---|---|
| **SAF-O1** | Accelerated modernisation | NSIs modernise faster and with less rework, because they start from shared reference models, patterns and building blocks instead of designing from scratch. | Lead time from decision to production for a new statistical product; share of solution designs that reuse SAF building blocks |
| **SAF-O2** | Enhanced data quality | Governance, metadata and lineage are part of the architecture. Statistical output therefore meets high standards of quality and reliability. Quality is designed in, not checked afterwards. | Share of datasets with complete metadata and lineage; revision rate of published figures |
| **SAF-O3** | Improved interoperability | NSIs reach higher interoperability across systems, domains and borders. This makes international collaboration easier, improves comparability and simplifies the use of external data sources. | Share of data exchanges using standard interfaces (e.g. SDMX); number of components shared between NSIs |
| **SAF-O4** | Improved trust and transparency | Openness, security and transparency in the architecture help to build and keep public trust. This strengthens the reputation of NSIs and the legitimacy of their output. | Results of public trust surveys; number of confidentiality or security incidents |
| **SAF-O5** | Increased efficiency | Reuse, harmonisation and standardisation reduce duplicate work. The result is lower IT costs, shorter development cycles and more efficient processing. | Number of redundant systems retired; processing time per production cycle; IT cost per statistical product |
| **SAF-O6** | Shared knowledge base | A community of practice across UNECE members exchanges lessons learned, reusable components and knowledge. This leads to continuous improvement at lower cost. | Number of reusable components and patterns published; number of NSIs contributing |

| **Toolkit:** SAF-TK-M05 Outcome and indicator sheet |
|---|

## Architecture Principles

Principles turn goals into decision rules. When an NSI chooses between technologies, solutions or designs, principles make the choice consistent and explainable, and they give an architecture board a shared basis for reviewing projects. They matter in official statistics because production runs in a closely connected environment, where a choice in one place affects many others. They prevent short-term convenience from undermining long-term sustainability, a real risk for NSIs with legacy systems and tight budgets. And they create accountability: when stakeholders know the principles behind a decision, investments and trade-offs are easier to explain. Principles are durable and rarely change.

The SAF follows the TOGAF template, which describes each principle by its name, its statement (the rule itself), its rationale (why the rule exists and what it brings) and its implications (what following it requires in cost, resources and activities). A principle is only useful if it is applied; a principle that never changes a decision is a slogan. Principles take effect only when they are part of governance: architecture reviews test compliance, and deviations follow a documented dispensation process. The Statistical Data Value Chain shows how each value stream applies the principles.

### SAF architecture principles

| ID | Principle | Statement | Rationale | Implications |
|---|---|---|---|---|
| **SAF-P01** | Actively participate in open-source communities to maintain collective control over statistical processes | Statistical organisations build statistical capabilities on shared open-source software, contribute to its communities, and release software they develop for statistical production as open source by default. Non-statistical processes use standard applications. | Critical statistical methods stay under the collective control of the official-statistics community rather than vendors, and open methods are transparent and reproducible. Sharing costs and contributing, not only consuming, keeps common components alive. | Contribution is planned and funded, improvements go back to the community project, and choices follow the order reuse, open source, buy, build, with building justified. Own components are released under an open licence unless security or confidentiality prevents it, and purchased software must support open standards, APIs and data export. |
| **SAF-P02** | Active support | Hardware and software have an active user community or vendor support. As a rule of thumb, the latest or second-to-last major version is used. | Business continuity requires fast and competent support when something breaks. Security requires that known vulnerabilities are fixed in time. | Support status is a selection criterion for every component. Components that approach end of support are flagged in the life cycle plan. |
| **SAF-P03** | Active life cycle management | Systems and components are kept up to date according to an agreed life cycle management (LCM) policy. | Without LCM, systems become outdated and vulnerable, and technical debt builds up. Paying off that debt later takes disproportionate effort and creates continuity risks. | Every component has an owner and a life cycle plan. LCM has a structural budget, not only when problems arise. |
| **SAF-P04** | Maximise the benefits for the organisation | IT decisions maximise the benefit for the organisation as a whole. | Decisions taken from an organisation-wide view have more long-term value than decisions taken from a departmental view. The principle stands for "service above self". | Local optimisations need justification against organisation-wide priorities. Shared solutions are preferred over departmental ones, even when they fit one department less well. |
| **SAF-P05** | IT and technology is everyone's business | All parts of the organisation take part in the IT decisions needed to reach organisational goals. | The users of IT are its main stakeholders. IT only fits the business when business experts and technical staff set goals and objectives together. | Business ownership of each information system is assigned explicitly. Architecture and change decisions are taken in joint business and IT forums. |
| **SAF-P06** | Business continuity | Work continues despite system or staff outages. | The more an NSI depends on its systems, the more their reliability matters. Hardware failures, disasters and data corruption must not stop statistical production or release. | Continuity requirements are part of every design. Critical processes have fallback arrangements, and recovery is tested regularly. |
| **SAF-P07** | Implement loosely coupled processes and systems | Processes and systems are built as independently as possible. They share functionality and logic through standard interfaces. | Loose coupling makes it easier to change or replace a single process or system. It also improves scalability and robustness, and it makes different security and privacy requirements easier to enforce. | Domains exchange data through defined interfaces, such as the steady-state handovers. Direct dependencies on another domain's internal data or logic are avoided. |
| **SAF-P08** | Data is shared property | Statistical data that adds value for internal or external users is shared. | Sharing enables reuse. In data collection, reuse reduces response burden. In processing, it avoids duplicate work on cleaning and analysing data. | Data is registered and findable in a catalogue. Before new data is collected, reuse of existing data is checked. Access is governed, not withheld by default. |
| **SAF-P09** | No data without metadata and classification | All shared data has metadata that describes its content and meaning as well as possible, and an AIC classification (availability, integrity, confidentiality). | Metadata makes data FAIR. An AIC classification sets the technical and organisational measures that laws, regulations and security standards require. | Metadata and classification are recorded when data is registered, not afterwards. Data without the required metadata is not handed over. |
| **SAF-P10** | Security by design | Security is an integral part of every solution. Security mechanisms are consistent across all layers of the architecture and scale from small to large objects. | Security added afterwards costs more, works less well and leaves gaps between layers. | Security requirements are set in the design phase of every solution and tested before production. |
| **SAF-P11** | Privacy by design | Privacy is an integral part of system architecture and business processes. | Privacy added afterwards conflicts with functionality and leaves risks. Built in from the start, it becomes part of the core functionality without limiting it. | Privacy impact is assessed in the design phase. Measures such as pseudonymisation, data minimisation and disclosure control are placed at defined points in the value chain. |
: SAF architecture principles {tbl-colwidths="[8,17,25,25,25]"}

| **Toolkit:** SAF-TK-M06 Principle set and dispensation record |
|---|

## Value

Value makes the case for architecture in terms that stakeholders recognise. Architecture competes with other priorities for money and attention, and it only gets support when its long-term worth is clear. Value is always value *for someone*: the same outcome can be worth a lot to one stakeholder and little to another. An outcome is a result; value is what that result is worth to a stakeholder. A goal is an intention of the organisation; value is the reason a stakeholder cares whether the goal is reached. Meaning is how something is interpreted; value is how much it is worth.

The SAF creates value at several levels. For NSIs, it means lower risk, more agility and better alignment between IT and business. For international organisations, it means harmonisation and comparability. For citizens and policy makers, it means statistics they can rely on. Value also has a time dimension. Without a framework, modernisation tends to be fragmented, costly and short-lived. The SAF gives a stable base that reduces technical debt and makes investments last.

### SAF value elements

| ID | Value | Description |
|---|---|---|
| **SAF-V1** | Cross-border comparability | Statistics are worth more when they can be compared across borders. Common standards, models and processes make that comparison meaningful. |
| **SAF-V2** | Innovation enablement | The SAF lowers the barriers for AI, machine learning, real-time analytics and big data. NSIs can experiment safely and keep their methods sound. |
| **SAF-V3** | Risk reduction | Compliance, security and governance are built into the architecture. This reduces the risk of system failures, data breaches and regulatory non-compliance, and protects the trust of citizens and stakeholders. |
| **SAF-V4** | Strategic alignment | IT initiatives contribute directly to the mission of producing official statistics. This improves governance, prioritisation and the impact of IT investments. |
| **SAF-V5** | Sustainability | Efficient, modern architectures with less technical debt give NSIs a clear path forward, without repeated and costly overhauls. |
| **SAF-V6** | Trust and legitimacy | Transparency, ethical practice and robust security strengthen the position of NSIs as authoritative providers of public data. |

| **Toolkit:** SAF-TK-M09 Value and meaning brief |
|---|

## Stakeholders

Architecture is never developed in isolation. Knowing the stakeholders makes clear whose concerns the architecture must address, who should take part in governance and decisions, and which views each audience needs. Involvement also builds support: people who take part in architecture decisions are more likely to back them.

A stakeholder is not the same as a business actor or role. An actor or role performs work in the architecture, for example a data steward who registers datasets. A stakeholder has an interest in the architecture, whether or not it performs work in it. The same person or organisation can be both. SAF stakeholders range from CIOs and technical experts within NSIs to international organisations, policy makers, researchers and society as a whole. Their interests differ, and the framework has to balance them. IT professionals turn SAF principles into systems. Policy makers care about the results those systems make possible. UNECE keeps the SAF harmonised and relevant across countries.

### SAF stakeholders

| ID | Stakeholder | Category | Key concerns | What the SAF offers |
|---|---|---|---|---|
| **SAF-ST01** | CIOs and CTOs of NSIs | Within the NSI | Strategic IT investment, alignment of IT with business goals, compliance | A framework to compare options, align IT with business goals and show compliance with international standards |
| **SAF-ST02** | Citizens and society | Society | Trustworthy, transparent and modern statistics | Statistics that support democratic accountability and informed public debate |
| **SAF-ST03** | Government policy makers | Society | Timely, accurate and comparable data in accessible formats | Better statistical production and dissemination (indirect benefit) |
| **SAF-ST04** | IT and data professionals | Within the NSI | Common patterns, tools and practices; collaboration across institutions | Shared patterns and practices that save effort and shorten the learning curve |
| **SAF-ST05** | National Statistical Institutes (NSIs) | Statistical community | Structured guidance for enterprise architecture; efficiency; quality | Guidance tailored to official statistics and aligned with international practice |
| **SAF-ST06** | Researchers and academia | Society | Access to high-quality data and metadata for research | Systems designed for openness, data sharing and rich metadata |
| **SAF-ST07** | UNECE and other international bodies | Statistical community | Relevance, coherence and adoption of the framework | A custodial role for UNECE; alignment with the modernisation work of Eurostat and the UN Statistics Division |

| **Toolkit:** SAF-TK-M01 Stakeholder map |
|---|

# Strategy

## Purpose of this chapter

The Strategy chapter translates motivation into what an NSI must be able to do and how it creates value. Motivation explains *why* change is needed. Strategy describes *what* the organisation needs: its capabilities, the resources behind them, the value streams they support and the courses of action that develop them.

These elements are deliberately independent of organisation structure, processes and systems. Departments, processes and applications change often. Capabilities and value streams change slowly. Anchoring architecture work in this layer lets an NSI compare itself with peers, plan investments over several years, and reorganise or replace technology without losing sight of what it must deliver.

## Position in the framework

The Strategy layer shares the Strategy and Motivation area of the TOGAF ADM with the Motivation layer (see *Position in the framework* in the Motivation chapter). It receives direction from goals and outcomes. It gives direction to the business architecture: value stream stages are realised by business processes, and capabilities are realised by people, processes, information and technology in the lower layers.

|**PLACEHOLDER: Position of the Strategy layer between Motivation and the architecture domains**|
|---|

In TOGAF terms, the Strategy chapter supports capability-based planning. Capabilities and value streams are part of the Architecture Vision (Phase A) and of the baseline and target Business Architecture (Phase B). Courses of action and resources return in Phases E and F, where the NSI decides how and in which order capabilities are developed.

## How NSIs use this chapter

The capability model and the value streams in this chapter are a reference. Most NSIs perform the same core activities, so these elements are largely shared across the community. An NSI adopts, adapts or extends them, as it does the motivation elements.

The capability model is the most practical starting point. An NSI can assess the maturity of each capability, mark where its goals require improvement, and use the result to prioritise investment. Value streams show where in the production chain a capability creates value, and which stakeholders notice a weak capability first.

Resources and courses of action are specific to each NSI. The SAF explains these concepts, and the Toolkit provides templates and illustrative examples to record them.

| **Toolkit:** SAF-TK-S02 Capability assessment and heatmap |
|---|

## Strategy concepts in the SAF

| SAF section | ArchiMate element | Question it answers | Identifier | Toolkit |
|---|---|---|---|---|
| Capability Model | Capability | What must the NSI be able to do? | Capability number (e.g. 1.2.1) | SAF-TK-S01, SAF-TK-S02 |
| Value Streams | Value Stream | Which sequence of stages creates value for a stakeholder? | VS-01 to VS-10 | SAF-TK-S03 |
| Resources | Resource | Which assets does the NSI have or need to perform its capabilities? | Defined by the NSI | SAF-TK-S04 |
| Courses of Action | Course of Action | Which approach will the NSI take to develop its capabilities and reach its goals? | Defined by the NSI | SAF-TK-S05 |

The concepts form a chain. Capabilities are what the NSI can do. Resources are what it uses to do it: people, data, knowledge, technology and money. Value streams show where capabilities create value for a stakeholder. Courses of action describe how the NSI will strengthen its capabilities and resources to reach its goals.

### Relationships between the strategy elements

| Element | Relationship | Example in the SAF |
|---|---|---|
| Capabilities → Goals and outcomes (Motivation) | Capabilities realise goals and outcomes | Metadata management (2.1.2) realises enhanced data quality (SAF-O2) |
| Capabilities → Assessment (Motivation) | A capability maturity assessment is a structured form of assessment | A low maturity score for Statistical quality management (2.1.3) |
| Capabilities → Value streams | Capabilities enable value stream stages; a weak capability shows up as a weak stage | Primary data collection (1.2.1) enables VS-01.3 *Collect or Receive Data* |
| Resources → Capabilities | Resources are assigned to capabilities, which are performed with them | Staff with methodological expertise are assigned to Methodology (2.2.3) |
| Business functions and processes → Capabilities | Business functions and processes realise capabilities | Business function *Classify Data* realises Data standardisation (1.3.1) |
| Capabilities → Steady states | Capabilities produce or govern steady states | Data standardisation (1.3.1) produces State #2 Standardized Data |
| Value streams → Stakeholders and value (Motivation) | A value stream creates value for a stakeholder and delivers value elements | VS-06 creates value for users of statistics (SAF-ST02, SAF-ST03, SAF-ST06) and contributes to trust and legitimacy (SAF-V6) |
| Value streams → Steady states and processes | Each primary value stream produces one steady state; business processes realise its stages | VS-02 produces State #2; the execution processes of the Standardisation domain realise the stages of VS-02 |
| Courses of action → Goals, outcomes and assessments (Motivation) | Courses of action serve goals and contribute to outcomes; assessments show why they are needed | A shared-platform strategy serves cost efficiency (SAF-G1); an assessment of SAF-D5 leads to a decision to retire legacy platforms |
| Courses of action → Principles (Motivation) | Courses of action apply principles | An application strategy applies SAF-P01 |
| Courses of action → Capabilities, resources, value streams | Courses of action develop capabilities, configure resources and improve value streams | A metadata strategy develops Metadata management (2.1.2); a workforce strategy trains data engineers; a web-first collection strategy improves VS-01; a shared platform with partner NSIs develops IT infrastructure (3.2.5) |
| Constraints (Motivation) → Resources | Constraints limit which resources can be used | Public cloud may not be used for statistical microdata |
| Assessment (Motivation) → Resources | An assessment can record a resource gap | "Two of our three methodologists for small area estimation retire within two years" |
| Capability 4.1.2 *Policy and planning* → Courses of action | This capability produces the strategies | Translating the organisation strategy into domain strategies |
| Resources → Data and technology architecture | Data and technology resources are detailed in the lower layers | The data platform as a technology resource |

## Capability Model

A business capability is what a statistical organisation must be able to do to perform its mission, deliver value and achieve its objectives, independent of processes, organisational structures or technologies. Capabilities are the enabling building blocks of the organisation and give a stable, long-term view of its functional landscape. Each capability describes a specific business purpose and outcome, realised through one or more business functions and operationalised by business processes. Capabilities are therefore the conceptual bridge between strategy and execution: they translate strategic goals into operational competence.

- **They are stable.** Statistical quality management (2.1.3) remains essential whether quality checks are manual, automated or AI-supported. Processes and applications change; the capability stays. This makes capabilities the preferred unit for strategic planning, transformation roadmaps and multi-annual investment.
- **They are independent of organisation.** A capability can be spread over several departments, or one department can hold several capabilities. The capability model does not follow the organisation chart, which lets NSIs compare themselves with each other.
- **They are hierarchical.** High-level capabilities are decomposed into more detailed ones. In the SAF, *Data management* (2.1) is decomposed into, among others, *Metadata management* (2.1.2).

A capability view makes gaps visible: where a goal requires a capability that is weak or missing, investment is needed. Capabilities with a low maturity and a high contribution to goals become candidates for investment, and each capability can be traced to the processes, applications and platforms that realise it.

| **Toolkit:** SAF-TK-S01 Capability model tailoring; SAF-TK-S02 Capability assessment and heatmap |
|---|

### Capability map

The SAF capability model has four main levels.

|**PLACEHOLDER: SAF capability map (ArchiMate)**|
|---|

| ID | Main level | Description | Reference |
|---|---|---|---|
| **1** | Primary statistical capabilities | The ability to perform the statutory statistical tasks of an NSI. | GAMSO |
| **2** | Supporting data capabilities | The ability to manage statistical data and to carry out statistical research. | |
| **3** | Supporting business capabilities | The ability to make sure that the right people, information and resources are available to support the statistical and governance capabilities. | |
| **4** | Governance capabilities | The ability to give direction to the organisation, by setting its strategy and the framework within which change takes place. | GAMSO 1.2, Strategy and Leadership |

### Capability catalogue

#### 1. Primary statistical capabilities

| ID | Capability | Description | Reference |
|---|---|---|---|
| **1.1** | **Statistical design and build** | The ability to identify information needs and set up statistical processes to meet them. | [GSBPM 5.2, Design](https://unece.github.io/GSBPM-5.2/#design-phase) |
| 1.1.1 | Needs inventory | The ability to identify the demand for statistical information and translate it into the societal questions the NSI will respond to. Needs are often identified through strategic relationships with users and stakeholders. The result is usually laid down in the NSI's multi-annual programme and the process that prepares it. | GSBPM |
| 1.1.2 | Design statistics product | The ability to translate information needs into concrete designs of datasets, process and workflow models, and rule sets and methodology, for the datasets that are released. This covers both the statistical product and the process that produces it. The process consists of process steps, rule sets for each step, the methodology, the process flow, the designs of the required datasets and the designs of shared connection points for reuse. If a required dataset is not available, a data collection assignment can follow. For primary data collection, designs then follow for sampling, questionnaires and similar instruments. | GSBPM, Design phase |
| 1.1.3 | Build statistics product | The ability to build, test and manage a statistical product until the end of its life cycle. The outputs of the design are assembled and configured into a complete operational environment in which the process can run. | GSBPM |
| **1.2** | **Data collection** | The ability to collect data for official statistics. | [GSBPM 5.2, Collect](https://unece.github.io/GSBPM-5.2/#collect-phase) |
| 1.2.1 | Primary data collection | The ability to set up and manage surveys up to completion, and to transfer the collected data and metadata for processing and analysis. Primary data collection uses one or more collection modes. The target population and sample size are set together with the client, based on the information need. Person surveys and business surveys are distinguished. A survey consists of, among other things, a sample, a questionnaire and an approach strategy. | ESS capability model |
| 1.2.2 | Secondary data collection | The ability to collect data and metadata from third parties for the production of statistics. Data that third parties have already collected is used as much as possible. | ESS capability model |
| **1.3** | **Processing** | The ability to process raw data into statistical microdata and statistics. | GSBPM, Process phase |
| 1.3.1 | Data standardisation | The ability to standardise data without loss of content. Standardisation covers data formats, category codes, linkage keys and units of measurement, such as weight, distance and time. It takes place directly after the raw data is received. Standardising as early as possible makes the rest of the process more efficient. | |
| 1.3.2 | Deriving variables and units | The ability to create new units, and values of new variables, from existing units and values of existing variables. New variables are usually derived to describe reality better. The data source was often not designed for that purpose. | |
| 1.3.3 | Check content | The ability to check datasets for irregularities, such as missing data, possible errors and outliers. Detected errors can lead to adjustment (see 1.3.4). They can also lead to a quality indicator that is used in quality reporting. Detected outliers lead to an outlier indicator, which matters for a good estimation method (see 1.3.5). | GSBPM |
| 1.3.4 | Adjusting and imputing | The ability to adjust incorrect values and to fill in missing values. Together with *Check content* (1.3.3), this capability is often called editing. Checks use editing rules, and adjustment is often based on imputation. Imputed values do not yet have to meet the editing rules. A final adjustment therefore often follows, with the editing rules as constraints. | GSBPM, ESS capability model |
| 1.3.5 | Estimating population parameters | The ability to estimate population parameters from microdata. Estimated population parameters often appear as observations, the cells, in a dimensional dataset such as a table. There are several estimation methods, including the traditional "weight and aggregate". Weights can be derived with several techniques. Sometimes weights are adjusted to give detected outliers less influence. | |
| 1.3.6 | Integrate statistics | The ability to integrate separate statistics into one consistent whole. Examples are integration systems such as the national accounts, sector accounts and labour accounts. | |
| 1.3.7 | Statistical disclosure | The ability to check datasets for privacy sensitivity and to adjust them where confidentiality would be violated. | GSBPM 6.4 |
| **1.4** | **Analysis** | The ability to examine and understand data before it is disseminated. In NSIs, statistical analysis is also called statistical research. It draws connections or conclusions from relationships in the data, such as correlations. | [GSBPM 5.2, Analyse](https://unece.github.io/GSBPM-5.2/#analyse-phase) |
| 1.4.1 | Statistical (output) analysis | The ability to validate, interpret and explain statistical output, and to finalise it for dissemination using shared methods and processes. | ESS capability model |
| **1.5** | **Dissemination** | The ability to manage the release of statistical products to internal and external users. | [GSBPM 5.2, Disseminate](https://unece.github.io/GSBPM-5.2/#disseminate-phase) |
| 1.5.1 | Publication management | The ability to manage the release of statistical output and related content according to release calendars, so that users have predictable and equal access. | ESS capability model |
| 1.5.2 | Promotion to use | The ability to promote statistical output to potential users, and to inform the press and other interested parties about it. | ESS capability model |
| 1.5.3 | Facilitate data access | The ability to make statistical data and metadata available to people and machines through multiple channels. | ESS capability model |
| 1.5.4 | Statistical information management | The ability to prepare and distribute publications about statistical output, such as press releases, interpretations and reports. | ESS capability model |

#### 2. Supporting data capabilities

| ID | Capability | Description | Reference |
|---|---|---|---|
| **2.1** | **Data management** | The ability to manage data and metadata. | |
| 2.1.1 | Data lifecycle management | The ability to manage data throughout its life cycle. | |
| 2.1.2 | Metadata management | The ability to manage metadata throughout its life cycle. | ESS capability model |
| 2.1.3 | Statistical quality management | The ability to assess quality, put control mechanisms in place and start quality improvements across the statistical value chain. | |
| 2.1.4 | Statistical register management | The ability to set up, maintain and provide register services for collecting and integrating data. This includes the management of master data. | ESS capability model |
| **2.2** | **Research** | The ability to build and record knowledge about statistical methods, products, sources and techniques. | |
| 2.2.1 | Data source exploration | The ability to explore new data sources. | ESS capability model |
| 2.2.2 | Product innovation | The ability to create new statistical products from existing data sources, and to explore new data sources that are useful and important to users. Product innovation can precede the design of a statistical product (see 1.1.2). | ESS capability model |
| 2.2.3 | Methodology | The ability to investigate new methods for the statistical process. | |
| 2.2.4 | Data services | The ability to provide data for statistical or scientific research. This applies to both internal and external datasets. These services are provided through, among other things, microdata services. | |
| 2.2.5 | User research | The ability to collect and assess user needs, and translate them into statistical output. | |

#### 3. Supporting business capabilities

| ID | Capability | Description | Reference |
|---|---|---|---|
| **3.1** | **Business operations** | The ability to manage personnel, purchasing and contracts, finance and housing, including the related systems and communication. | |
| 3.1.1 | Personnel management (HR) | The ability to make sure that enough qualified staff are available to carry out all business processes. | |
| 3.1.2 | Purchasing and contract management | The ability to acquire goods and services, and to monitor the agreements made with suppliers. | |
| 3.1.3 | Financial management | The ability to plan, organise, design, record and control the financial activities of the organisation. | |
| 3.1.4 | Communication management | The ability to communicate correctly with internal and external parties. | |
| 3.1.5 | Administrative support | The ability to support administrative tasks. | |
| 3.1.6 | Facility management | The ability to integrate people, place and process within the built environment. The description is based on ISO 41011. Facility management aims to improve the quality of life of people and the productivity of the core business. | ISO 41011 |
| 3.1.7 | Legal support | The ability to handle requests and applications, assess agreements and advise on relevant laws and regulations. | |
| 3.1.8 | Information management and archive management | The ability to keep the organisation's information sustainably accessible (FAIR). This concerns information created in supporting and management processes, not statistical information from the primary statistical process. | |
| **3.2** | **Computerisation and automation** | The ability to translate the organisation's information needs into functionality of the information provision, and to keep information systems available to support business processes. | |
| 3.2.1 | Application development | The ability to develop applications in-house. This capability is needed to fill gaps in functionality that the statistical process requires. | |
| 3.2.2 | Functional management | The ability to manage applications so that they support business processes as well as possible. An example is collecting user requirements and translating them into new application functionality. | |
| 3.2.3 | Technical management | The ability to manage system software and applications. This covers installing, configuring and managing hardware and software so that it keeps working correctly, including all measures to resolve disruptions in time. | |
| 3.2.4 | Digital workplace management | The ability to manage the resources and services that staff use in their digital workplace. Examples are laptops and desktops, mobile devices, virtual desktops, video and audio conferencing, printing, VPN and proxy services. | |
| 3.2.5 | IT infrastructure | The ability to develop, maintain and manage IT infrastructure. | |
| **3.3** | **Security and privacy** | The ability to carry out all security and privacy activities. | |
| 3.3.1 | Privacy management **[S7]** | The ability to develop, manage, apply and test the NSI's privacy policy, in order to comply with privacy laws and regulations. | |
| 3.3.2 | Security planning | The ability to identify, analyse and plan measures to secure systems, networks, the organisation and its facilities. | |
| 3.3.3 | Security incident management | The ability to identify, analyse, respond to and recover from security incidents. | |
| 3.3.4 | Logical identity and access control | The ability to make sure that a person, organisation or IT facility can only use the automated functions for which access rights have been granted. | |
| 3.3.5 | Physical security and access control | The ability to provide controlled and safe access to buildings and spaces, and to keep the people and goods in them safe. | |
| 3.3.6 | IT security services | The ability to provide IT services that support information security. Examples are endpoint protection, PKI and network security management. | |
| **3.4** | **Customer and chain interaction** | The ability to interact with customers and chain partners: providing them with the right data and information, and receiving notifications, requests and data. | |
| 3.4.1 | Services management | The ability to design, develop, implement and manage the services that the organisation provides to customers and chain partners. | |
| 3.4.2 | Contact management | The ability to maintain relationships with customers and chain partners. | [GAMSO 1.2, Manage Consumers](https://statswiki.unece.org/spaces/GAMSO/pages/247302304/Corporate+Support#CorporateSupport-GAMSOv1.2ManageConsumersManageConsumers) **[S9]** |
| 3.4.3 | Service agreement | The ability to draw up, manage and enforce service agreements with clients and chain partners. Service agreements apply to clients that receive services from the NSI, such as access for external researchers or additional statistical services. They also apply to parties that supply data for primary or secondary data collection. If a party does not comply, the NSI can take enforcement action. | |
| 3.4.4 | Self-service | The ability to let customers and chain partners answer questions about the services they use, or make justified changes to them, without help from staff. | |

#### 4. Governance capabilities

| ID | Capability | Description | Reference |
|---|---|---|---|
| **4.1** | **Strategy and leadership** | The ability to set the direction of the organisation and to manage change towards it. | GAMSO 1.2, Strategy and Leadership |
| 4.1.1 | Strategy and governance | The ability to develop a vision, and to set up and monitor the organisation and its management. | |
| 4.1.2 | Policy and planning | The ability to translate the strategy into concrete objectives, principles and plans. | |
| 4.1.3 | Change management | The ability to define and manage major changes, so that they contribute as much as possible to the objectives. | |
| 4.1.4 | Improvement management | The ability to manage daily operations, identify areas for improvement and implement improvements based on daily operations. | |
| 4.1.5 | Accountability | The ability to report to stakeholders inside and outside the organisation on how far obligations and agreements are met. | |
| 4.1.6 | Collaboration | The ability to maintain and strengthen strategic relationships with external stakeholders. Collaboration covers coordination with other statistical organisations and other external stakeholders. Within a statistical system, this coordination can follow a geographical hierarchy (local, regional, national, multinational) or a division of responsibilities between organisations. It includes identifying new opportunities for data exchange and integration. It also gives the statistical community opportunities to exchange knowledge, improve statistical infrastructure and practice, and influence statistical standards. | GAMSO 1.2, Manage Strategic Collaboration and Cooperation |
| 4.1.7 | Architecture Management | The ability to develop, maintain and govern the enterprise architecture of the NSI, and to use it in decisions on strategy, investment and change. | |

| **Toolkit:** SAF-TK-S01 Capability model tailoring |
|---|

## Value Streams **[T1]**

A value stream is a sequence of stages that together create an overall result for a stakeholder. Each stage adds a specific piece of value, and the value stream ends when the stakeholder receives the result. Value streams are seen from the stakeholder: they start with a need and end with value for someone, not following the organisation chart or the order of systems. They describe value, not work: a stage says *what value* is added, while *how* the work is done is described by business processes. And they are enabled by capabilities: each stage needs one or more capabilities.

Value streams and capabilities are two views on the same organisation. Capabilities show *what* the NSI can do; value streams show *where* that ability turns into value, which capabilities matter for which result, and which stakeholders notice a weak capability first. They also give the business architecture its structure: each stage is realised by business processes (see *Mapping to value stream stages* in Business Architecture), and the primary value streams follow the steady states of data. How each value stream works, stage by stage, is described in the Statistical Data Value Chain chapter.

### Value stream overview **[T2]** **[T3]**

The SAF has ten value streams. Six primary value streams form the statistical value chain: each consumes a registered steady state and produces the next. Four supporting value streams run across the chain and provide governance, innovation, platforms and the connection with users.

| ID | Value stream | Type | Receives value | Value created | Steady state in → out |
|---|---|---|---|---|---|
| VS-01 | Data Acquisition and Ingestion | Primary | Statistical production; data providers | Trust and readiness: data acquired correctly and ready for use | #0 → #1 |
| VS-02 | Data Standardization and Integration | Primary | Statistical production; reusers of microdata | Coherence and comparability | #1 → #2 |
| VS-03 | Data Editing and Enrichment | Primary | Statistical production; methodologists | Reliability and analytical readiness | #2 → #3 |
| VS-04 | Estimation, Analysis and Statistical Modeling | Primary | Statistical product owners | Analytical insight and statistical credibility | #3 → #4 |
| VS-05 | Statistical Product Composition | Primary | Statistical product owners; users | Coherence and interpretability | #4 → #4 (approved) |
| VS-06 | Dissemination and Service Delivery | Primary | Users: policy makers, researchers, media, businesses, the public | Impact and accessibility | #4 → #5 |
| VS-07 | Governance and Compliance | Supporting | Management, supervisory bodies, society | Integrity and accountability | Across all states |
| VS-08 | Innovation and Methodological Development | Supporting | Statistical production | Continuous improvement | Across all states |
| VS-09 | Infrastructure and Platform Enablement | Supporting | All value streams | Operational capability and continuity | Across all states |
| VS-10 | Customer and Stakeholder Engagement | Supporting | Users, data providers, partners | Relevance and trust | #5 → (#6), feedback to VS-01 |

### Value stream stages

| Stage | Name | Value added |
|---|---|---|
| VS-01.1 | Identify Data Needs and Sources | The information need is clear, and suitable sources are known |
| VS-01.2 | Establish Data Agreements and Access Rights | Data can be obtained lawfully, under agreed conditions |
| VS-01.3 | Collect or Receive Data | Data and its metadata are in NSI custody |
| VS-01.4 | Validate and Log Data Intake | The delivery is complete, intact and traceable |
| VS-01.5 | Store and Register Raw Data Artefacts | Raw data is registered and available for reuse (State #1) |
| VS-02.1 | Profile and Assess Data Structure | Differences from the target model are known |
| VS-02.2 | Apply Standard Classifications and Formats | Data uses common codes, formats and identifiers |
| VS-02.3 | Align Metadata and Semantics | Definitions and descriptions are consistent |
| VS-02.4 | Validate Structural and Semantic Conformance | Conformance to standards is confirmed |
| VS-02.5 | Register Standardized Artefacts | Standardised data is registered and available for reuse (State #2) |
| VS-03.1 | Conduct Error Detection and Quality Diagnostics | Errors, duplicates, gaps and outliers are known |
| VS-03.2 | Perform Data Editing and Correction | Incorrect values are corrected |
| VS-03.3 | Impute Missing or Non-Response Data | Missing values are filled with documented methods |
| VS-03.4 | Derive Additional Variables and Indicators | Data describes reality better than the source alone |
| VS-03.5 | Perform Quality Evaluation and Versioning | Quality is documented, and processed microdata is registered (State #3) |
| VS-04.1 | Confirm Estimation and Analytical Approach | The method fits the design and the purpose |
| VS-04.2 | Apply Weighting and Calibration | Bias from sampling, non-response and coverage is reduced |
| VS-04.3 | Estimate and Aggregate Data | Statistics and indicators are available |
| VS-04.4 | Perform Model-Based Analysis | Model-based results complement direct estimates |
| VS-04.5 | Validate and Document Results | Results are sound and documented (State #4) |
| VS-05.1 | Select and Integrate Source Datasets | Relevant results are brought together |
| VS-05.2 | Construct Composite Indicators or Indices | Indices, ratios and aggregates are available |
| VS-05.3 | Perform Consistency and Coherence Checks | The product is internally consistent |
| VS-05.4 | Generate Analytical and Interpretive Outputs | Results are explained and visualised |
| VS-05.5 | Approve and Register Statistical Products | The product is approved for release (State #4, approved) |
| VS-06.1 | Plan Dissemination and Access Strategy | Target users, channels and formats are set |
| VS-06.2 | Prepare Data for Dissemination | Output is disclosure-safe and in the right format |
| VS-06.3 | Publish and Provide Access Services | Users can find and access the output (State #5) |
| VS-06.4 | Support and Engage Users | Users understand and use the output correctly |
| VS-06.5 | Monitor Usage and Feedback | The NSI knows how its output is used |
| VS-07.1 | Define Governance Frameworks and Policies | Rules for data, metadata, ethics, confidentiality and quality are set |
| VS-07.2 | Establish Legal and Regulatory Compliance Mechanisms | Applicable rules are known and translated into procedures |
| VS-07.3 | Implement Data and Metadata Governance | Ownership, stewardship and lineage are assigned |
| VS-07.4 | Monitor Quality and Compliance Indicators | Quality and compliance status is visible |
| VS-07.5 | Audit, Certify and Report Compliance | Compliance is demonstrated |
| VS-07.6 | Update and Improve Governance Mechanisms | Governance keeps up with new rules and lessons learned |
| VS-08.1 | Identify Innovation Needs and Opportunities | Promising developments are known |
| VS-08.2 | Conduct Research and Proof-of-Concepts | Ideas are tested in a limited scope |
| VS-08.3 | Evaluate Methodological Soundness and Feasibility | Only sound and feasible innovations proceed |
| VS-08.4 | Develop and Document New Methodologies or Tools | Innovations are ready for reuse |
| VS-08.5 | Integrate Innovation into Production Environments | Innovations run in production under governance |
| VS-08.6 | Promote Knowledge Sharing and Capability Building | Staff can apply the new methods |
| VS-09.1 | Define Digital and Technical Requirements | Infrastructure needs follow from business needs |
| VS-09.2 | Design Platform and Infrastructure Architecture | Platforms are designed for storage, processing, integration and secure access |
| VS-09.3 | Provision and Configure Platforms | Environments are available with the required controls |
| VS-09.4 | Enable Integration and Orchestration Services | Processes and services are connected |
| VS-09.5 | Ensure Performance, Security and Continuity | Platforms are reliable and protected |
| VS-09.6 | Evolve and Modernise the Technical Ecosystem | The technical landscape stays current |
| VS-10.1 | Identify and Segment Stakeholders | The NSI knows its users, providers and partners |
| VS-10.2 | Collect and Analyse User Needs | Needs are translated into requirements |
| VS-10.3 | Define and Manage Service Portfolios | Services and products match the needs |
| VS-10.4 | Deliver Services and Manage Relationships | Users and partners are served |
| VS-10.5 | Engage and Communicate with Stakeholders | Stakeholders understand the output |
| VS-10.6 | Monitor Impact and Satisfaction | The NSI knows its impact and acts on it |

### Capabilities per value stream **[T4]**

|**PLACEHOLDER: ArchiMate view of capabilities serving value stream stages**|
|---|

| **Toolkit:** SAF-TK-S03 Value stream tailoring and capability mapping |
|---|

## Resources **[T6]**

A **resource** is an asset that an organisation owns or controls. Resources are what the organisation uses to perform its capabilities. A capability without the right resources exists on paper only. Resources make the capability model realistic: a maturity assessment that only looks at processes misses the most common bottleneck, not enough people with the right skills or no access to a needed data source. Linking resources to capabilities shows where a capability depends on a single expert, an outdated platform or an agreement that expires.

The SAF distinguishes six types of resources:

| Type | Examples in an NSI |
|---|---|
| People and skills | Methodologists, data engineers, subject-matter statisticians, architects |
| Data and information | Registers, survey data, administrative data deliveries, classifications, metadata |
| Knowledge | Statistical methods, process documentation, quality frameworks |
| Technology | Data platforms, processing tools, collection systems, secure processing environments |
| Financial | Structural budget, project funding, international grants |
| Relationships and agreements | Data sharing agreements, partnerships with other NSIs, supplier contracts |

Resources are owned or controlled: a resource is something the NSI has, or has secured through an agreement, such as access to administrative data under a provision agreement. They are limited, so they force choices between capabilities. And they are shared: a data platform supports collection, processing and dissemination at the same time. For an NSI, data is a resource in its own right. Registers, long time series and trusted relationships with data providers are often harder to replace than any system.

Resources are specific to each NSI, and the SAF does not list them. Technology resources are described in more detail in the application and technology architecture, and data resources in the data architecture.

| **Toolkit:** SAF-TK-S04 Resource profile |
|---|

## Courses of Action **[T6]** **[T7]**

A **course of action** is an approach or plan for configuring capabilities and resources to reach a goal. It answers the question *how will we get there?* Goals say where the NSI wants to go and capabilities say what it must be able to do; courses of action describe the choices the NSI makes to close the gap. Recording them explicitly prevents a common problem: programmes that each make sense on their own, but pull the organisation in different directions.

Courses of action range from broad to specific. ArchiMate calls the broad, long-term ones **strategies** and the narrower, shorter-term ones **tactics**. There is no hard line between the two. A strategy is usually broken down into several tactics, and tactics are realised by developing capabilities and resources. Courses of action are choices: "collect data web-first" rules out paper-first, and a plan without a choice is not a course of action. They serve goals, and one that serves no goal needs a justification. They build, strengthen, share or retire capabilities and resources.

Strategy, architecture and roadmap are related but different. A strategy sets the direction and the main choices. The architecture describes the structure that results. A roadmap sets the order and timing of the changes. Courses of action are specific to each NSI, and the SAF does not define them. Choosing a reference model for the data value chain, such as the Steady-State or the Medallion architecture (see *Reference Models for the Statistical Data Value Chain*), is itself a course of action.

### Reference strategies

The following published strategies and guidance documents can serve as reference when an NSI develops its own strategies.

| Document | Organisation | Type | Relevant for |
|---|---|---|---|
| [Statistics Canada Data Strategy](https://www.statcan.gc.ca/en/about/datastrategy) | Statistics Canada | Data strategy of an NSI | Data strategy; shows links to IT, cloud, privacy and metadata strategies |
| [Data Strategy](https://www.ons.gov.uk/aboutus/transparencyandgovernance/datastrategy/ourdatastrategy) | Office for National Statistics (UK) | Data strategy of an NSI | Data strategy |
| [ABS Data Strategy 2025–2030](https://www.abs.gov.au/about/our-organisation/our-commitments/abs-data-strategy-2025-2030) | Australian Bureau of Statistics | Data strategy of an NSI | Data strategy |
| [Data Strategy of the Secretary-General](https://www.un.org/en/content/datastrategy/index.shtml) | United Nations | Data strategy of an international organisation | Data strategy |
| [Cloud for Official Statistics](https://un-ilibrary.org/content/books/9789213587256) (2024) | UNECE | Guidance | Cloud strategy |
| [Privacy-Enhancing Technologies Guide](https://unstats.un.org/bigdata/task-teams/privacy/guide/) | UN Committee of Experts on Big Data and Data Science | Guidance | Privacy and confidentiality strategy |

| **Toolkit:** SAF-TK-S05 Strategy and course of action canvas |
|---|


# Business Architecture

## Purpose of this chapter

The business architecture describes how a statistical organisation is organised to turn data into official statistics. It shows who is involved, which processes and functions they perform, which services they offer, what triggers their work, and which information they create and exchange.

The Strategy layer describes *what* the NSI must be able to do and *where* it creates value. The business architecture describes *how* that work is organised. It is the layer where capabilities and value streams become concrete: in roles that people take on, processes they carry out, and information they hand over to each other.

For official statistics, one question deserves special attention: where does responsibility for data pass from one part of the organisation to another? A statistical value chain is long. It involves many teams and often confidential data. An untraceable change or uncontrolled reuse at any point can undermine every statistic built on that data. The SAF business architecture therefore pays explicit attention to the points where data is stored, quality-assured and handed over. These handover points are the backbone of the reference models at the end of this chapter.

The business architecture is independent of technology. It does not describe applications or platforms. It does describe the business needs that applications and platforms must support, and it is the starting point for the data, application and technology architecture.

## Position in the framework

The business architecture is the first of the core layers in TOGAF and ArchiMate (see *Position in the framework* in the Motivation chapter). In the TOGAF Architecture Development Method, it is developed in Phase B, Business Architecture. It receives direction from the Strategy layer and gives direction to the layers below it.

|**PLACEHOLDER: Position of the Business Architecture between the Strategy layer and the data, application and technology layers**|
|---|

| Direction | Relationship | Example in the SAF |
|---|---|---|
| From Strategy | Business processes realise value stream stages | The execution processes of the Standardisation domain realise the stages of VS-02 |
| From Strategy | Business functions and processes realise capabilities | The function *Classify Data* realises Data standardisation (1.3.1) |
| From Motivation | Principles and requirements shape the business design | SAF-P07 leads to loose coupling of domains through steady states |
| To Data Architecture | Business objects are realised by data objects | A registered *Raw Data* version is realised by a dataset in a data store |
| To Application Architecture | Business processes are served by application services | Data validation at intake is served by a validation service |
| To Technology Architecture | Business requirements drive platform requirements | Retention and versioning per steady state drive storage requirements |

In TOGAF, Phase B produces a baseline and a target business architecture, and the gap between them. The SAF provides a reference for the target. An NSI describes its own baseline and uses the SAF to define where it wants to go.

## How NSIs use this chapter

The SAF business architecture contains two kinds of content.

**Reference content.** Most NSIs perform the same statistical work and follow a comparable production process. The SAF therefore offers reference content for business processes, business functions, business services and business roles. NSIs use this content in the same three ways as the other SAF elements: adopt, adapt or extend.

**Concepts with examples.** Business events, business objects, contracts, representations and products are specific to each NSI. They depend on its products, its legal basis and its users. For these elements, the SAF explains the concept, how it is used, and gives examples. The toolkit provides templates.

The data value chain needs a separate choice. NSIs organise their chain in different ways, depending on their size, legal context and platforms. The SAF therefore offers more than one reference model for the chain: the Steady-State Architecture and the Medallion Architecture. An NSI chooses the model that fits, or combines them. This choice is a course of action in the sense of the Strategy chapter.

The business architecture is also the place where the NSI's own organisation meets the framework. An NSI maps its departments, teams and job profiles onto the SAF actors, roles and functions. The mapping shows which parts of the organisation carry which responsibilities, where they overlap, and where they are missing.

| **Toolkit (planned):** Role mapping and RACI template; organisation-to-function mapping (see *Planned instruments* in the Toolkit) |
|---|

## Relationship with the statistical standards

The SAF business architecture builds on the statistical standards introduced in *Relationship with statistical standards* (Introduction). The SAF process model is based on GSBPM. GAMSO, which places GSBPM in the wider context of strategy and leadership, capability development and corporate support, is the frame of reference for the business functions; the functions are described in SAF terms, so that NSIs can apply them together with their own national function models. GSIM is the reference for the business objects.

## Business architecture concepts in the SAF

The SAF uses the business layer elements of ArchiMate, and adds concepts that are specific to the statistical data value chain.

**ArchiMate business elements used in the SAF**

| Concept | ArchiMate element | Question it answers | Example | SAF content |
|---|---|---|---|---|
| Business actor | Business Actor | Who is involved: a person, team or organisation? | Data provider, NSI, research institute | Reference |
| Business role | Business Role | Which responsibility does an actor take on? | Data owner, data steward, methodologist | Reference |
| Business collaboration | Business Collaboration | Which actors or roles work together? | A data sharing partnership between an NSI and a register holder | Reference |
| Business process | Business Process | Which sequence of activities produces a defined result? | Collect, Process, Disseminate | Reference |
| Business function | Business Function | What does the organisation do continuously, grouped by required knowledge and skills? | Manage Quality | Reference |
| Business service | Business Service | Which behaviour does the organisation offer to others? | Microdata access for researchers | Reference |
| Business interface | Business Interface | Through which channel is a service offered? | A web portal, a secure data transfer channel, a helpdesk | Reference |
| Business event | Business Event | What triggers a process, or marks its result? | *Raw Data Registered*; start of a reference period | Concept and examples |
| Business object | Business Object | Which information does the business use and produce? | Raw Data, Statistical Product, Classification | Concept and examples |
| Contract | Contract | Which formal agreement governs a service or exchange? | A data provision agreement with a register holder | Concept and examples |
| Representation | Representation | In which perceptible form is information made available? | A press release, a statistical table, an API response | Concept and examples |
| Product | Product | Which coherent set of services and information is offered to users? | A statistical product with its publication and data services | Concept and examples |

**SAF-specific concepts for the data value chain**

| Concept | Definition |
|---|---|
| **Business domain** | A coherent part of the statistical process that adds one specific kind of statistical value to data and is governed as a unit. In ArchiMate, a business domain is modelled as a grouping. |
| **Data state** | A defined condition of data, characterised by the processing it has undergone and the quality criteria it meets. |
| **Steady state** | A data state that is stored, versioned, quality-assured and registered, so that it can be handed over and reused. |
| **Quality gate** | The set of criteria that data must meet before it may be registered in a state. |
| **Quality version** | An immutable, identified version of a dataset that has passed a quality gate. |
| **Handover interface** | The agreement between a producing and a consuming domain: the artefact, its required metadata, the triggering event and the transfer of responsibility. |
| **Reference model** | A generic arrangement of domains, states and handover points that an NSI can adopt and adapt, such as the Steady-State or Medallion Architecture. |

## How the business architecture is built up

ArchiMate describes each layer with three aspects: *who* acts (active structure), *what* happens (behaviour) and *what* is acted upon (passive structure). The SAF business architecture follows these aspects, and then brings them together in two integrating views.

|**PLACEHOLDER: Structure of the SAF business architecture: three ArchiMate aspects and two integrating views**|
|---|

| Part | Elements | Question |
|---|---|---|
| Active structure | Actors, roles, collaborations, interfaces | *Who* does the work, and through which channels? |
| Behaviour | Processes, functions, services, events | *What* happens, in which order, and what triggers it? |
| Passive structure | Business objects, contracts, representations, products | *Which* information is used, agreed and delivered? |
| Integrating view 1 | Mapping of processes and functions to value stream stages | *How* do processes, functions and value streams fit together? |
| Integrating view 2 | Reference models for the data value chain: Steady-State and Medallion | *Where* is data handed over, and with which quality? |

### Functions and processes

Functions and processes are easily confused, but they are different.

A **business function** groups behaviour by the knowledge, skills and resources it needs. Functions are stable. They have no start or end, and they do not depend on the order of work. *Manage Quality* is a function: it exists as long as the NSI exists.

A **business process** is a sequence of activities that leads to a defined result. A process has a trigger, a start and an end. *Collect* is a process: it starts when a collection period opens and ends when the data is stored and checked.

The two cross each other. One process uses several functions, and one function contributes to several processes. In ArchiMate, functions and processes are connected through realisation and assignment relationships. Statistical production is the clearest example: the production function is realised by the production process, which the SAF describes in detail.

### Processes and the data value chain

The process view and the data value chain look at the same production from two angles. The process follows the life cycle of one statistical product, from need to evaluation. The data value chain follows the data, from source to release, across products.

Each business domain uses the same four process types, Design, Implementation, Execution and Management, which connect the two angles. They and their GSBPM phases are described in *The four process types* in the Statistical Data Value Chain chapter.

The GSBPM phases 4 to 7 run across several business domains. *Process* (phase 5), for example, spans standardisation, editing and part of estimation. The steady states mark where, within that flow, data is handed over with a defined quality.

### Generic and model-specific content

Actors, roles, processes, functions, services, events and objects are generic. They apply to every NSI, whatever reference model it chooses for its data value chain.

The data value chain is model-specific. The business domains, steady states and quality gates differ between the Steady-State and the Medallion Architecture. That is why the SAF compares the reference models at the end of this chapter, and describes the Steady-State model in its own chapter, *Steady-State Architecture*.

## Structure of this chapter

| Section | Content | SAF content |
|---|---|---|
| Business Actors, Business Roles and Business Collaborations | Who is involved in statistical production, and with which responsibilities | Reference |
| Business Processes | The SAF process model, based on GSBPM | Reference |
| Business Functions | The SAF function model | Reference |
| Business Services, Events and Objects | Services and interfaces (reference); events, objects, contracts, representations and products (concept and examples) | Planned |
| Reference Models for the Statistical Data Value Chain | Reference models for the data value chain: comparison, selection criteria and combination. The Steady-State model is detailed in the *Steady-State Architecture* chapter, and the work per value stream in the *Statistical Data Value Chain* chapter | Reference |

Readers who want to understand the statistical data value chain can go straight to the last section. Readers who want to map their own organisation onto the SAF start with actors and roles, and with the function model.

## Business Actors, Business Roles and Business Collaborations

### The concepts

A **business actor** is a person, team or organisation that can perform behaviour. An actor is a real entity. It exists whether or not it takes part in a specific process. Examples are a ministry that supplies a register, a research institute, or the NSI itself. In the SAF, actors are described as types, not as named organisations.

A **business role** is a responsibility for performing specific behaviour. A role says what someone is accountable for, not who that someone is. One actor can take on several roles, and one role can be filled by several actors. A methodologist in a small NSI may also act as statistical designer. A large NSI may have a whole team in the role of data steward.

A **business collaboration** is a group of actors or roles that work together for a shared purpose. A collaboration performs behaviour that none of its members can perform alone. It can be permanent, such as a data governance board, or temporary, such as a project team. Collaborations can also cross the boundaries of the NSI. A data sharing partnership between an NSI and a register holder is an example.

Actors, roles and collaborations are different from stakeholders (see *Stakeholders* in the Motivation chapter). A stakeholder has an interest in the architecture. An actor or role performs work in it. The same organisation can be both. A data provider is a stakeholder with concerns about burden, and an actor that delivers data in VS-01.

### How the SAF applies actors, roles and collaborations

**Why the SAF describes actors, roles and collaborations**

Roles make responsibilities explicit. A steady state needs a data owner. A quality gate needs someone who decides. A release needs someone who approves. Without defined roles, these decisions are taken by whoever happens to be involved. That makes accountability unclear and audits difficult. Defined roles also make NSIs comparable. When two NSIs both use the role *data steward*, they can compare practices and share solutions.

**How actors, roles and collaborations fit into an NSI's own architecture**

The SAF offers a reference set of actor types, roles and collaborations. An NSI maps its own organisation onto this set. It links its departments and teams to actor types, and its job profiles to roles. One job profile often covers several SAF roles, especially in small NSIs. The mapping shows which roles are filled, which are combined, and which are missing. An NSI can then assign roles to processes, for example with a RACI matrix (responsible, accountable, consulted, informed).

The SAF roles are deliberately generic. The value streams use more specific role names, such as *Estimation Methodologist* or *Imputation Specialist*. These are specialisations of the reference roles. The mapping table at the end of this section shows how they relate.

**Relationships with other concepts**

| Related concept | Relationship | Example in the SAF |
|---|---|---|
| Stakeholders (Motivation) | A stakeholder can also be an actor | A data provider is a stakeholder and an actor in VS-01 |
| Business processes | Roles are assigned to processes | The data steward is assigned to *Register Raw Data* |
| Business functions | Roles are assigned to functions | The quality manager is assigned to *Manage Quality* |
| Business services and interfaces | Actors and roles offer or use services through interfaces | A researcher uses the microdata access service through a secure portal |
| Steady states | Each steady state has an owner, a steward and a custodian | The data owner of State #3 decides on access to processed microdata |
| Capabilities (Strategy) | Roles are part of the resources that realise capabilities | Methodologists are a key resource for Methodology (2.2.3) |

|**PLACEHOLDER: ArchiMate view of SAF actors, roles and collaborations**|
|---|

### SAF business actors

The SAF distinguishes nine actor types. They are grouped by their position relative to the NSI.

| ID | Actor | Position | Description |
|---|---|---|---|
| **ACT-01** | National Statistical Institute | Internal | The NSI is the organisation that produces official statistics under a legal mandate. It is the central actor in the SAF. The NSI owns the statistical processes and is accountable for the quality and confidentiality of its output. It enters into agreements with data providers, users and partners. In the architecture, the NSI as a whole is the actor that offers business services to society. |
| **ACT-02** | Organisational unit | Internal | An organisational unit is a department, division or team within the NSI. Units are the actors that actually carry out the work. Each unit fills one or more roles, such as data collection, methodology or dissemination. The SAF does not prescribe an organisation structure. An NSI maps its own units onto the SAF roles, so that it can see which unit is responsible for which part of the chain. |
| **ACT-03** | Data provider | External, supplies data | A data provider is an organisation that supplies data it holds to the NSI. Examples are government agencies with administrative registers, businesses with transaction data, and platform operators. The data is collected for another purpose and reused for statistics. Delivery usually takes place under a legal obligation or a data provision agreement. The NSI cannot control the quality at the source, but it can influence it through agreements and feedback. |
| **ACT-04** | Respondent | External, supplies data | A respondent is a person, household or business that provides data directly to the NSI, usually through a survey. Respondents answer questionnaires on the web, by telephone, face to face or on paper. Their burden is a constant concern for the NSI. Respondents are protected by statistical confidentiality: the NSI may not disclose their individual data. The NSI also has a duty to explain why it needs the data and how it uses it. |
| **ACT-05** | Data user | External, uses output | A data user is a person or organisation that uses the output of the NSI. Users include policy makers, researchers, journalists, businesses and members of the public. Their needs differ widely. A minister needs a clear figure, a researcher needs microdata under strict conditions, and a developer needs a reliable API. The NSI groups users into segments, so that it can design services and channels for each segment. |
| **ACT-06** | Other producer of official statistics | Statistical system | Many countries have more than one producer of official statistics. Examples are central banks, ministries with statistical units and regional statistical offices. The NSI often coordinates this national statistical system. Producers exchange data, align methods and share infrastructure. In the architecture, they are partners in collaborations and sometimes providers or users of each other's data. |
| **ACT-07** | International statistical organisation | Statistical system | International statistical organisations set standards, coordinate statistics across countries and collect national data. Examples are UNECE, Eurostat, the OECD, the IMF and the UN Statistics Division. They require NSIs to deliver data in agreed formats and on agreed dates. They also develop the shared models that the SAF builds on, such as GSBPM and GSIM. For the NSI, they are users, standard setters and partners in collaboration. |
| **ACT-08** | Supervisory and legal authority | External, oversees | A supervisory or legal authority oversees whether the NSI acts within the law. Examples are the data protection authority, a national statistics council, the national audit office and the courts. Some authorities grant the legal basis for data collection. Others assess compliance after the fact. The NSI must be able to show these authorities how it handles data, which is one reason why traceability is a core concern of the SAF. |
| **ACT-09** | Supplier and service provider | External, supports | A supplier delivers goods or services that the NSI needs but does not produce itself. Examples are software vendors, cloud and hosting providers, field work agencies and trusted third parties for pseudonymisation. Suppliers work under contracts that set requirements for security, confidentiality and continuity. When a supplier processes statistical data, the NSI remains accountable for it. The choice of suppliers is guided by SAF-P01 and by the NSI's sourcing strategy. |

### SAF business roles

The SAF reference set contains 24 roles in seven groups. The column *Process type* shows in which of the four process types of a business domain (design, implementation, execution, management) the role mainly works.

#### Governance and accountability

| ID | Role | Process type | Description |
|---|---|---|---|
| **ROL-01** | Process owner | Management | The process owner is accountable for the end-to-end performance of a business domain or value stream. This role sets the objectives of the process and decides on changes to it. The process owner makes sure the process has the people, methods and systems it needs. The role receives the quality reports of the management process and acts on them. In the steady-state model, each business domain has one process owner. |
| **ROL-02** | Data owner | Management | The data owner is accountable for a dataset or a steady state. This role decides who may access the data, for which purpose and under which conditions. The data owner also approves the retention period and the classification of the data. The role is usually held by a manager in the domain that produces the data. Data ownership is a business role, not an IT role: the data owner answers for the content, not for the storage. |
| **ROL-03** | Data steward | Execution | The data steward takes care of data on behalf of the data owner. This role registers datasets in the catalogue and maintains their metadata. The data steward checks that data meets the quality gate before it is registered. The role also handles questions from users and resolves exceptions. Data stewards are the daily point of contact for anyone who wants to find or use a dataset. |
| **ROL-04** | Data custodian | Execution | The data custodian is responsible for the safe storage and technical management of data. This role runs storage, backup and access control according to the decisions of the data owner. The custodian carries out retention and disposal. The role does not decide on the use of the data, but makes sure that decisions are applied correctly. In many NSIs, the custodian role is held by an IT or platform team. |
| **ROL-05** | Chief data officer | Management | The chief data officer is accountable for data governance across the whole NSI. This role sets the data policy and the governance framework. It assigns the data owner, steward and custodian roles to people and units. The chief data officer chairs or supports the data governance board. The role is the escalation point for conflicts about data that cross domain boundaries. |

#### Design

| ID | Role | Process type | Description |
|---|---|---|---|
| **ROL-06** | Statistical designer | Design | The statistical designer translates information needs into the design of a statistical product. This role defines the outputs, the variables, the population and the required data. The designer specifies the processes that produce the product, in close cooperation with the methodologist. The role is the link between users and production. In some NSIs this role is called product manager. |
| **ROL-07** | Methodologist | Design | The methodologist designs and assesses the statistical methods. This role covers sampling, collection methods, editing and imputation, estimation and quality measurement. The methodologist makes sure methods are sound, documented and reproducible. The role also evaluates new methods before they enter production. Specialisations exist for each step of the chain, such as estimation or editing. |
| **ROL-08** | Metadata and data architect | Design | The metadata and data architect designs the structure of data and metadata. This role defines data models, metadata schemas and the minimum metadata set of each steady state. The architect makes sure that data from different sources can be combined and compared. The role works with standards such as GSIM and SDMX. It is the bridge between the business architecture and the data architecture. |
| **ROL-09** | Classification steward | Design | The classification steward manages the classifications and code lists that the NSI uses. This role maintains national versions of international classifications, such as NACE or ISCO. The steward manages correspondence tables between versions. The role makes sure that all domains use the same version at the same time. Changes to a classification are announced and documented before they take effect. |

#### Implementation

| ID | Role | Process type | Description |
|---|---|---|---|
| **ROL-10** | Data engineer | Implementation | The data engineer builds the technical processes that move and transform data. This role develops ingestion pipelines, collection channels and processing workflows. The data engineer implements the designs of the statistical designer and the methodologist. The role also builds the automated checks that support the quality gates. The data engineer works closely with the platform engineer, who provides the environment. |
| **ROL-11** | Platform engineer | Implementation | The platform engineer provides and runs the environments in which the processes operate. This role configures platforms, storage, connectors and access controls. The platform engineer keeps environments secure, available and up to date. The role supports all value streams but is anchored in VS-09. In many NSIs, the role is also called system configurator or DevOps engineer. |
| **ROL-12** | Test manager | Implementation | The test manager plans and coordinates the testing of new or changed processes. This role covers technical tests, integration tests and field tests. The test manager checks that a process produces the expected result before it goes into production. The role reports test results to the process owner. Testing is required before any change to a process that produces a steady state. |

#### Execution

| ID | Role | Process type | Description |
|---|---|---|---|
| **ROL-13** | Data collection manager | Execution | The data collection manager runs data collection campaigns. This role plans the collection period, coordinates field staff and monitors response. The manager follows up on non-response and late deliveries. The role also handles contacts with respondents and data providers during collection. The data collection manager reports on collection progress and quality to the process owner. |
| **ROL-14** | Data quality analyst | Execution | The data quality analyst checks data during processing. This role runs validation checks, assesses results against the quality gate and logs exceptions. The analyst investigates errors and outliers and proposes corrections. The role documents quality indicators for each version of a dataset. Data quality analysts are active at every handover point in the chain. |
| **ROL-15** | Subject-matter statistician | Execution | The subject-matter statistician has in-depth knowledge of a statistical domain, such as labour market or prices. This role interprets results, checks plausibility and explains developments. The statistician carries out or supervises editing, estimation and analysis in the domain. The role writes or reviews the texts that accompany a release. Subject-matter statisticians are the experts that users and journalists turn to. |
| **ROL-16** | Disclosure control specialist | Design, Execution | The disclosure control specialist protects the confidentiality of respondents in the output. This role designs and applies disclosure control methods, such as suppression, rounding and noise. The specialist assesses the disclosure risk of tables, microdata and services. The role works at State #4 and at the gate to State #5. No output is released without a disclosure check that this role has approved. |
| **ROL-17** | Release manager | Execution | The release manager controls the publication of statistical output. This role makes sure that releases follow the release calendar and the embargo rules. The release manager checks that the output has been approved and has passed disclosure control. The role coordinates the release across channels, such as the website, the API and press releases. Equal access for all users at the moment of release is a key responsibility. |

#### Assurance

| ID | Role | Process type | Description |
|---|---|---|---|
| **ROL-18** | Quality manager | Management | The quality manager is responsible for the quality framework of the NSI. This role defines quality indicators and monitors them across the chain. The quality manager produces quality reports and leads improvement actions. The role supports process owners in the management process of their domains. It also prepares the NSI for quality reviews, such as peer reviews against the European Statistics Code of Practice. |
| **ROL-19** | Compliance officer | Management | The compliance officer makes sure that the NSI complies with laws and regulations. This role covers statistical law, data protection law and other applicable rules. The officer checks new processes and methods against compliance criteria before they go into production. The role keeps the legal register up to date. In many NSIs the data protection officer is a specific form of this role. |
| **ROL-20** | Security officer | Management | The security officer is responsible for information security and continuity. This role defines security measures and monitors their application. The officer manages security incidents and leads recovery when something goes wrong. The role assesses the security of new solutions and suppliers. It works closely with the platform engineer and the compliance officer. |
| **ROL-21** | Auditor | Management | The auditor checks independently whether processes and controls work as intended. This role can be internal, such as an internal audit department, or external, such as the national audit office or a certification body. The auditor reviews evidence, such as logs, quality reports and lineage records. The role reports findings to management and to supervisory authorities. Its work depends on the traceability that the SAF builds into the chain. |

#### Users and partners

| ID | Role | Process type | Description |
|---|---|---|---|
| **ROL-22** | Dissemination and service manager | Design, Execution | The dissemination and service manager designs and manages the services through which users receive output. This role covers publications, open data, APIs and microdata access. The manager defines channels and formats for each user segment. The role manages the portfolio of services and their service levels. It works with the release manager on the timing and with the relationship manager on user needs. |
| **ROL-23** | Relationship manager | Execution | The relationship manager maintains the relationships with key external actors. These include data providers, major users, partners and international organisations. The manager collects needs, feedback and complaints, and passes them to the right roles. The role negotiates and maintains agreements, such as data provision agreements. Relationship managers make sure that the NSI speaks with one voice to each partner. |

#### Support

| ID | Role | Process type | Description |
|---|---|---|---|
| **ROL-24** | Enterprise architect | Design, Management | The enterprise architect develops and maintains the enterprise architecture of the NSI. This role translates strategy into architecture and uses the SAF as its reference. The architect advises on investments and reviews projects against the architecture principles. The role supports the architecture board and keeps the architecture repository up to date. It is the role that realises the capability *Architecture management*. |

### SAF business collaborations

| ID | Collaboration | Members | Type | Description |
|---|---|---|---|---|
| **COL-01** | Data provision partnership | NSI, data provider, relationship manager, data owner | External, permanent | A data provision partnership is the long-term cooperation between the NSI and a data provider. It goes beyond a single delivery. The partners agree on content, format, timing and quality of the data. They also agree on how to handle changes at the source, such as a new system or a new definition. A good partnership reduces the burden for the provider and improves the quality for the NSI. |
| **COL-02** | National statistical system | NSI, other producers of official statistics | External, permanent | The national statistical system is the cooperation between all producers of official statistics in one country. The NSI usually coordinates it. The members align methods, classifications and release practices, so that national statistics are consistent. They exchange data and sometimes share infrastructure. The cooperation is often based on the national statistics law. |
| **COL-03** | International statistical cooperation | NSI, international statistical organisations, other NSIs | External, permanent | International statistical cooperation is the collaboration between NSIs and international organisations. It covers the development of standards, the exchange of data and the joint development of tools. The SAF itself is a product of this cooperation. Members take part in working groups, such as those of UNECE and the European Statistical System. The cooperation helps NSIs avoid building the same solution many times. |
| **COL-04** | Research access partnership | NSI, research institutes, data owner, disclosure control specialist | External, permanent | A research access partnership gives researchers access to microdata under strict conditions. The NSI, research institutes and sometimes funding bodies take part. The partners agree on who may access which data, for which purpose and in which environment. Output is checked for disclosure risk before it leaves the secure environment. The partnership supports science while protecting the confidentiality of respondents. |
| **COL-05** | Statistical product team | Statistical designer, methodologist, data engineer, subject-matter statistician | Internal, permanent or temporary | A statistical product team brings together the roles needed to design, build and run a statistical product. It typically includes a statistical designer, a methodologist, a data engineer and a subject-matter statistician. The team can be permanent for a product or temporary for a redesign. Working as one team shortens the path from design to production. It also makes sure that methodological and technical choices are made together. |
| **COL-06** | Data governance board | Chief data officer, data owners, data stewards, compliance officer | Internal, permanent | The data governance board steers data management across the NSI. The chief data officer chairs it, and data owners, data stewards and the compliance officer take part. The board sets data policies, resolves conflicts between domains and monitors compliance. It decides on access requests that cross domain boundaries. The board makes sure that the steady-state model is applied consistently. |
| **COL-07** | Architecture board | Enterprise architect, process owners, CIO or CTO | Internal, permanent | The architecture board steers the enterprise architecture of the NSI. The enterprise architect, process owners and the CIO or CTO take part. The board reviews projects against the architecture principles and the target architecture. It decides on deviations through a documented dispensation process. The board keeps the architecture aligned with the strategy and with the SAF. |

### Role names in the value streams

The value streams use specific role names that fit their context. The table shows how they relate to the reference roles. A specialised role inherits the responsibilities of its reference role and adds those specific to its value stream.

| Role name in the value streams | Reference role |
|---|---|
| Process Owner; Process Owners (VS-01…VS-10) | ROL-01 Process owner |
| Data Owner / Steward / Custodian | ROL-02 Data owner; ROL-03 Data steward; ROL-04 Data custodian |
| Chief Data / Governance Officer | ROL-05 Chief data officer |
| Statistical Designer; Product Manager; Model Designer; Derivation Designer; Coherence Designer | ROL-06 Statistical designer |
| Methodologist; Estimation Methodologist; Editing Methodologist; Imputation Specialist; Indicator/Index Methodologist; Head of Methodology / Innovation | ROL-07 Methodologist |
| Metadata Architect; Data Architect | ROL-08 Metadata and data architect |
| Classification Steward; Coding Specialist | ROL-09 Classification steward |
| Data Engineer; Integration Specialist; Integration Engineer; Tool / Platform Engineer | ROL-10 Data engineer |
| System Configurator; DevOps / Platform Engineer; Platform / Cloud Architect; Service Desk / Operations | ROL-11 Platform engineer |
| Test Manager | ROL-12 Test manager |
| Data Collection Manager | ROL-13 Data collection manager |
| Data Quality Analyst | ROL-14 Data quality analyst |
| Subject-Matter Analyst; Subject-Matter Reviewer; Subject-Matter Author; Subject-Matter Expert; Survey Statistician; Analyst / Modeler; Researcher / Data Scientist | ROL-15 Subject-matter statistician |
| Disclosure-Control Designer | ROL-16 Disclosure control specialist |
| Release Manager; Approval Authority | ROL-17 Release manager |
| Quality Manager | ROL-18 Quality manager |
| Compliance Officer; Legal Counsel | ROL-19 Compliance officer |
| Security & Continuity Officer | ROL-20 Security officer |
| Internal / External Auditor | ROL-21 Auditor |
| Dissemination Manager; Channel/Service Designer; Open-Data / API Product Owner; Service / Product Portfolio Manager; User-Support Lead; Service Desk / User Support | ROL-22 Dissemination and service manager |
| Account / Relationship Manager; Engagement / Communications Officer; Communications / Outreach Officer; Head of Communication / Engagement; User Researcher; Impact Analyst | ROL-23 Relationship manager |
| Chief Technology / Infrastructure Officer | Actor: management of the NSI (ACT-01); member of COL-07 |
| Trainer / Knowledge Manager | Not included in the reference set |
| Data Provider; Survey Respondent; Data User; Legal Authority; Standards Body; Methodology Authority | Actors ACT-03, ACT-04, ACT-05, ACT-08, ACT-07 |

| **Toolkit (planned):** Role mapping and RACI template |
|---|

## Business Processes

### The concept

A **business process** is a sequence of activities that produces a defined result for a customer, a stakeholder or another process. A process has a trigger, a start and an end. It has inputs and outputs, and it uses the knowledge and resources of one or more business functions. Processes describe *how* work flows, step by step. They are the part of the business architecture that people recognise most directly in their daily work.

Processes can be decomposed. A high-level process consists of sub-processes, which can in turn be broken down further. The SAF describes processes at two levels: process phases or process groups, and the sub-processes within them. More detailed levels, such as work instructions, are specific to each NSI and fall outside the SAF.

A process is not the same as a value stream stage. A value stream stage describes the value that is added. A process describes the work that adds it. One stage is usually realised by several processes, and one process can contribute to several stages.

### How the SAF applies business processes

**Why the SAF describes business processes**

Processes are where architecture meets daily operations. A shared process model lets NSIs compare how they work, reuse each other's solutions and discuss improvements in the same terms. It also links the strategic layer to the systems: value streams are realised by processes, and processes are supported by application services. Without a process model, it is hard to show which system supports which part of the work, or where a change in method affects other steps.

**How business processes fit into an NSI's own architecture**

The core of the SAF process model is GSBPM, which most NSIs already know. The SAF adds three process groups that GSBPM does not describe in detail: data management and lifecycle, microdata services and data spaces. An NSI adopts the process model as a reference, maps its own processes onto it and adds its own lower levels. A national process for, say, the monthly price index can then be traced to the SAF sub-processes it implements. The SAF does not prescribe the order of sub-processes. GSBPM is not a strict sequence: sub-processes can be skipped, repeated or run in parallel.

**Relationships with other concepts**

| Related concept | Relationship | Example in the SAF |
|---|---|---|
| Value streams (Strategy) | Processes realise value stream stages | PRD-4.3 *Run collection* realises VS-01.3 *Collect or Receive Data* |
| Capabilities (Strategy) | Processes realise capabilities | PRD-5.4 *Edit and impute* realises Adjusting and imputing (1.3.4) |
| Business functions | Processes realise functions; functions are assigned to processes | The production process realises the production function |
| Business roles | Roles are assigned to processes | ROL-14 *Data quality analyst* is assigned to PRD-5.3 *Review and validate* |
| Business events | Events trigger processes and mark their results | *Collection period opened* triggers PRD-4.3 |
| Business objects | Processes access business objects | PRD-5.8 *Finalise data files* writes the processed microdata |
| Steady states | Processes produce and consume steady states | DLM-3 *Register and catalogue data* registers a dataset in a steady state |
| Application services | Application services serve processes | A validation service serves PRD-5.3 |

**Process groups**

| Group | IDs | Basis | Scope |
|---|---|---|---|
| A. Statistical production | PRD-1 to PRD-8 | GSBPM phases and sub-processes | The production of a statistical product, from need to evaluation |
| B. Overarching processes | OVA-1 to OVA-6 | GSBPM overarching processes | Activities that run across all production phases |
| C. Data management and lifecycle | DLM-1 to DLM-11 | SAF | The management of data assets and steady states across products |
| D. Microdata services | MDS-1 to MDS-9 | SAF | Controlled access to microdata for research |
| E. Data spaces | DSP-1 to DSP-6 | SAF | Participation in data spaces, as data provider and data user |

|**PLACEHOLDER: ArchiMate view of the SAF process model**|
|---|

### A. Statistical production processes

The statistical production processes follow the eight phases of GSBPM. Each phase is described first, followed by its sub-processes. The descriptions are paraphrased from GSBPM, a model of UNECE published under the Creative Commons Attribution 4.0 licence (CC BY 4.0).

#### PRD-1 Specify Needs

| ID | Process | Description |
|---|---|---|
| **PRD-1** | **Specify Needs** | This phase starts when a new statistical need is identified, or when an existing product needs review. It establishes what users need and whether the NSI can meet that need. The phase explores options, including the use of data that already exists. It ends with a decision on whether to proceed, based on a business case. For existing products that run regularly, this phase is usually carried out only when a review is due. |
| PRD-1.1 | Identify needs | This sub-process investigates which statistics are needed and what they are needed for. The trigger can be a new policy question, a legal requirement or a user request. It also looks at changes in the needs for existing statistics. Input comes from users, stakeholders, legislation and earlier evaluations. The result is a first description of the need. |
| PRD-1.2 | Consult and confirm needs | This sub-process consults users and stakeholders to understand the need in detail. It checks what exactly they want to know, at which level of detail and how often. It also explores which constraints apply, such as timing or budget. The NSI and the users confirm the need together. The result is a confirmed and documented set of needs. |
| PRD-1.3 | Establish output objectives | This sub-process translates the confirmed needs into output objectives. It defines which statistics will be produced and which quality they must meet. Legal and confidentiality constraints are taken into account. The objectives are realistic for the data and resources that are available. The result is the basis for the design of the outputs. |
| PRD-1.4 | Identify concepts | This sub-process clarifies the concepts to be measured, from the point of view of the users. A concept such as "household income" or "unemployment" needs a clear meaning. The sub-process checks whether existing statistical concepts can be reused. Concepts may not yet match the definitions that data sources use. That mismatch is resolved later, in the design phase. |
| PRD-1.5 | Check data availability and suitability | This sub-process checks whether existing data sources can meet the need. It looks at internal data, administrative data, data spaces and other external sources. For each source, it assesses quality, coverage, timeliness and legal conditions. Reusing existing data comes before new collection, in line with SAF-P08. The result shows which gaps remain that new data must fill. |
| PRD-1.6 | Prepare and submit business case | This sub-process documents the findings of the phase in a business case. The business case describes the need, the proposed solution, the costs and the benefits. It also lists risks and alternatives. The business case is submitted to management for a decision. Approval starts the design phase. |

#### PRD-2 Design

| ID | Process | Description |
|---|---|---|
| **PRD-2** | **Design** | This phase designs the statistical product and the process that produces it. It covers outputs, variables, collection, sampling, processing, analysis and dissemination. It also defines the metadata and the quality criteria. Designs reuse existing standards, methods and components wherever possible. The results are the specifications for the build phase. |
| PRD-2.1 | Design outputs and dissemination | This sub-process designs the statistical outputs in detail. It defines tables, datasets, indicators and their metadata. It also designs how and through which channels the outputs will be disseminated. Disclosure control requirements are taken into account from the start. The design follows the output objectives from PRD-1.3. |
| PRD-2.2 | Design variables | This sub-process defines the variables to be collected and to be derived. It specifies their definitions, the types of statistical units and the classifications that apply. Existing variables and classifications are reused where possible. Each variable gets metadata that describes its meaning. The result is a variable list that all later phases use. |
| PRD-2.3 | Design collection | This sub-process determines how the data will be collected. It chooses the sources, the collection modes and the instruments, such as questionnaires or data interfaces. For administrative data and data spaces, it designs the agreements and delivery formats. Respondent burden is kept as low as possible. The design also covers the metadata and paradata to be captured. |
| PRD-2.4 | Design frame and sample | This sub-process defines the target population and the frame from which units are selected. It designs the sampling method and the sample size, where a sample is used. For register-based statistics, it defines how the population is derived from the registers. Coverage problems in the frame are identified and addressed. The result is the method used later in PRD-4.1. |
| PRD-2.5 | Design processing and analysis | This sub-process designs the methods for processing and analysis. It covers integration, coding, validation, editing, imputation, derivation, weighting and estimation. It also designs the methods for disclosure control. Methods are documented so that results can be reproduced. The designs are reviewed by methodologists before they are built. |
| PRD-2.6 | Design production systems and workflows | This sub-process designs the end-to-end workflow of the statistical process. It defines which systems and components are needed for each step. It avoids gaps and duplication between steps. Reuse of existing components and shared platforms comes first, in line with SAF-P01. The result is the blueprint for the build phase. |

#### PRD-3 Build

| ID | Process | Description |
|---|---|---|
| **PRD-3** | **Build** | This phase builds and tests the production solution. It assembles the components, configures the workflows and tests the whole process. Components are reused where possible and built only where needed. The phase ends when the process is ready for production. For regular products, this phase is only needed when something changes. |
| PRD-3.1 | Reuse or build collection instruments | This sub-process builds or reuses the instruments for data collection. Examples are electronic questionnaires, data delivery interfaces and connectors to data spaces. It follows the design from PRD-2.3. Instruments are tested for usability and correctness. The result is a set of instruments ready for collection. |
| PRD-3.2 | Reuse or build processing and analysis components | This sub-process builds or reuses the components for processing and analysis. Examples are validation rules, imputation routines and estimation programmes. The components implement the methods designed in PRD-2.5. Shared components that other products already use are preferred. Each component is documented and version-controlled. |
| PRD-3.3 | Reuse or build dissemination components | This sub-process builds or reuses the components for dissemination. Examples are table templates, publication workflows and API endpoints. It follows the design from PRD-2.1. Shared dissemination platforms are used where possible. The components are tested together with the output systems. |
| PRD-3.4 | Configure workflows | This sub-process configures the workflows that connect the components. It sets up the order of steps, the data flows and the transformations. It also configures the registration of data in the steady states. Configuration is preferred over custom code. The result is an executable workflow. |
| PRD-3.5 | Test production systems | This sub-process tests the assembled systems and their interactions. It checks that components work together and handle errors correctly. It also tests performance and security. Test results are documented and reported to the process owner. Defects are fixed before the process goes live. |
| PRD-3.6 | Test statistical business process | This sub-process tests the whole statistical process in practice. It can take the form of a pilot or a field test with real data. It checks that the process produces results of the expected quality. Problems found in the test lead to changes in design or build. The process owner decides whether the process is ready. |
| PRD-3.7 | Finalise production systems | This sub-process puts the process and its systems into production. It completes the documentation and trains the staff involved. It transfers the systems to the teams that will run and maintain them. The metadata of the process is registered. From this moment, the process can run in the collect to disseminate phases. |

#### PRD-4 Collect

| ID | Process | Description |
|---|---|---|
| **PRD-4** | **Collect** | This phase collects or acquires the data, metadata and paradata needed for the product. It covers surveys, administrative data, data from data spaces and other sources. Data is received securely and checked for completeness. The phase ends when the data is stored and registered as raw data. In the steady-state model, this phase produces State #1. |
| PRD-4.1 | Create frame and select sample | This sub-process creates the frame for this iteration of the process. It applies the method designed in PRD-2.4 to the current population. Where a sample is used, it draws the sample. The quality of the frame and the sample is checked. The result is the list of units from which data will be collected. |
| PRD-4.2 | Set up collection | This sub-process makes sure that people, processes and systems are ready to collect. It prepares the instruments, trains interviewers and informs respondents or data providers. It checks that agreements and access rights are in place. Collection channels are tested before collection starts. The collection period is planned and communicated. |
| PRD-4.3 | Run collection | This sub-process carries out the collection. Respondents complete questionnaires, and data providers deliver their data. Progress and response are monitored continuously. Non-response is followed up within the agreed strategy. Paradata about the collection is recorded. |
| PRD-4.4 | Finalise collection | This sub-process loads the collected data and metadata into a secure environment. It checks integrity, completeness and structure at intake. It registers the data as a new version of raw data. Delivery problems are reported to the data provider. The collection is closed when all expected data has been received or written off. |

#### PRD-5 Process

| ID | Process | Description |
|---|---|---|
| **PRD-5** | **Process** | This phase turns the collected data into microdata that is ready for analysis. It integrates, classifies, checks, corrects and derives data. It also calculates weights and aggregates. The phase runs across several business domains of the steady-state model. It produces States #2 and #3, and the first aggregates of State #4. |
| PRD-5.1 | Integrate data | This sub-process combines data from one or more sources into a consistent dataset. It links records that describe the same unit, using agreed keys. It resolves overlaps and conflicts between sources. Linkage uses pseudonymised keys where personal data is involved. The result is an integrated dataset with documented linkage quality. |
| PRD-5.2 | Classify and code | This sub-process assigns codes from standard classifications to the data. Examples are codes for economic activity, occupation or region. Coding can be automatic, manual or a mix of both. The classification versions used are recorded in the metadata. Coding quality is checked and documented. |
| PRD-5.3 | Review and validate | This sub-process checks the data for errors, outliers and inconsistencies. It applies the validation rules designed in PRD-2.5. It flags records that need attention. Some checks run automatically, others need expert review. The result is a dataset with quality flags and a list of issues. |
| PRD-5.4 | Edit and impute | This sub-process corrects incorrect values and fills in missing values. Corrections follow editing rules, and missing values are imputed with documented methods. Every change is recorded, so that the original value can always be traced. The impact of editing and imputation on the results is measured. The result is a complete and consistent dataset. |
| PRD-5.5 | Derive new variables and units | This sub-process creates variables and units that were not collected directly. Examples are age groups, household composition or enterprise groups. Derivations follow the specifications from PRD-2.2. Derived variables get their own metadata. The derivation rules are documented and reusable. |
| PRD-5.6 | Calculate weights | This sub-process calculates weights for the records in the dataset. Weights correct for the sample design, non-response and coverage. They follow the method designed in PRD-2.5. The quality of the weights is checked. The weights are stored with the microdata. |
| PRD-5.7 | Calculate aggregates | This sub-process calculates totals and other aggregates from the microdata. It applies the weights and the estimation methods. It can also combine lower-level aggregates into higher levels. Accuracy measures are calculated alongside the estimates. The result is the first version of the statistics. |
| PRD-5.8 | Finalise data files | This sub-process combines the results of the phase into the files used for analysis. It checks that the files are complete and consistent. It registers the processed microdata as a new version in the steady state. The metadata of the files is completed. The files are now ready for the analysis phase. |

#### PRD-6 Analyse

| ID | Process | Description |
|---|---|---|
| **PRD-6** | **Analyse** | This phase turns the processed data into statistical outputs and checks that they are fit for release. It prepares draft outputs, validates them and explains them. It also applies disclosure control. The phase ends with the approval of the content for release. In the steady-state model, it completes State #4. |
| PRD-6.1 | Prepare draft outputs | This sub-process transforms the data files into draft statistical outputs. Examples are tables, indicators, time series and charts. It also prepares the methodological notes that go with them. Drafts follow the output design from PRD-2.1. They are the input for validation and interpretation. |
| PRD-6.2 | Validate outputs | This sub-process checks the draft outputs for quality and plausibility. It compares results with earlier periods, other sources and expectations. It checks them against the quality framework. Unexpected results are investigated before they are accepted. The result is a set of validated outputs with documented quality. |
| PRD-6.3 | Interpret and explain outputs | This sub-process interprets the outputs and explains what they mean. Subject-matter experts describe developments and their causes. Deeper analyses may be carried out to support the explanation. The interpretation must be neutral and based on the data. The result is the content for publications and press releases. |
| PRD-6.4 | Apply disclosure control | This sub-process makes sure that outputs do not reveal information about individual respondents. It applies the disclosure control methods designed in PRD-2.5. Examples are suppression of cells, rounding and adding noise. The disclosure risk is assessed and documented. No output is released without passing this check. |
| PRD-6.5 | Finalise outputs | This sub-process makes sure that the statistics are fit for use. It completes the outputs and their metadata. It checks that all quality and confidentiality requirements are met. The content is approved for release by the responsible role. The approved outputs are registered as statistics ready for dissemination. |

#### PRD-7 Disseminate

| ID | Process | Description |
|---|---|---|
| **PRD-7** | **Disseminate** | This phase publishes the statistical products and supports users. It updates the output systems, produces the products and releases them. It also promotes the products and answers user questions. Equal access for all users at the moment of release is a core rule. In the steady-state model, this phase produces State #5. |
| PRD-7.1 | Update output systems | This sub-process loads the approved data and metadata into the systems used for dissemination. Examples are databases behind the website, open data portals and APIs. It checks that the data is loaded correctly and remains embargoed until release. Format and structure follow the dissemination design. The result is output that is ready for release. |
| PRD-7.2 | Produce dissemination products | This sub-process produces the products that users receive. Examples are press releases, publications, tables, visualisations and datasets. It follows the design from PRD-2.1. Products are checked for correctness and consistency before release. The result is a set of products ready to publish. |
| PRD-7.3 | Release dissemination products | This sub-process releases the products to users. It follows the release calendar and the embargo rules. All channels are updated at the same moment, so that no user gets an advantage. Errors found after release are corrected openly. The release is logged for accountability. |
| PRD-7.4 | Promote dissemination products | This sub-process brings the products to the attention of users. It uses channels such as social media, newsletters and events. It targets the user segments that have an interest in the product. Promotion helps users find and understand the statistics. Its effect is monitored. |
| PRD-7.5 | Provide user support | This sub-process answers questions and requests from users. Questions are registered and answered within agreed times. Frequent questions lead to better documentation or products. Requests for tailor-made data are handled according to confidentiality rules. Feedback from users is passed on to the product owners. |

#### PRD-8 Evaluate

| ID | Process | Description |
|---|---|---|
| **PRD-8** | **Evaluate** | This phase evaluates a specific run of the statistical process. It collects evidence, assesses quality and performance, and agrees on improvements. Evaluation can take place after every run or at set intervals. Its results feed back into the next run or into a redesign. The phase is part of the management process type of each business domain. |
| PRD-8.1 | Gather evaluation inputs | This sub-process collects the material for the evaluation. Examples are quality indicators, paradata, process logs, user feedback and staff comments. The inputs come from all earlier phases. They are brought together in one place. The result is a complete evidence base for the evaluation. |
| PRD-8.2 | Conduct evaluation | This sub-process analyses the inputs and draws conclusions. It assesses the quality of the outputs and the efficiency of the process. It compares results with targets and with earlier runs. Strengths and weaknesses are identified. The result is an evaluation report or dashboard. |
| PRD-8.3 | Agree an action plan | This sub-process agrees on actions to improve the process. It sets priorities, owners and deadlines. Actions can lead to small changes or to a full redesign. Progress on the actions is monitored. The action plan is the input for the next cycle. |

### B. Overarching processes

Overarching processes run across all phases of statistical production. They are not steps in the sequence. They apply to every phase, and to every product. They are based on the overarching processes of GSBPM.

| ID | Process | Description |
|---|---|---|
| **OVA-1** | Quality Management | This process assesses and controls the quality of products and processes. It applies the quality framework of the NSI in every phase. It defines quality indicators, measures them and reports on them. Quality problems lead to corrective actions. The process supports the NSI-wide quality management function. |
| **OVA-2** | Metadata Management | This process creates, updates, uses and archives statistical metadata in all phases. Metadata describes concepts, variables, classifications, methods and processes. It is captured when it is created, not afterwards. Metadata is shared through a catalogue, so that others can find and understand the data. The process applies SAF-P09 *No data without metadata and classification*. |
| **OVA-3** | Data Management | This process manages data throughout its life cycle in production. It covers storage, security, versioning, retention and disposal. It makes sure that data is available to the right people at the right time. The SAF details this process in group C, *Data management and lifecycle processes*. The process applies the design rules of the steady-state model. |
| **OVA-4** | Process Data Management | This process records and uses data about the execution of the statistical process. Examples are paradata from collection, logs of processing steps and timings. Process data shows how the process actually ran. It is used for monitoring, evaluation and audit. It is also the basis for lineage: the trace from output back to source. |
| **OVA-5** | Knowledge Management | This process maintains the knowledge needed to run the production process. It keeps documentation, methods and procedures up to date. It makes sure that recurring processes can be repeated in the same way. It also captures lessons learned from evaluations. Knowledge management reduces the dependence on individual staff members. |
| **OVA-6** | Data Supplier Management | This process manages the technical and operational relationship with data suppliers during production. It covers delivery schedules, formats, quality feedback and problem resolution. It keeps track of the burden placed on suppliers. It works within the agreements made at corporate level. Good supplier management improves data quality and reduces delays. |

### C. Data management and lifecycle processes

These processes manage data as an asset, across products and over its whole life. They detail the overarching process OVA-3 *Data Management*. They follow the life cycle of a steady state: promotion, gate, registration, use, revision and retirement. They apply to every reference model for the data value chain.

| ID | Process | Description |
|---|---|---|
| **DLM-1** | Plan and design data assets | This process decides which data assets the NSI needs and how they are structured. It defines datasets, their owners, their classification and their place in the steady states. It is triggered by a new product, a new source or a change in the data architecture. Planning prevents duplicate datasets and unclear ownership. The result is a documented design for each data asset. |
| **DLM-2** | Promote data through a quality gate | This process submits a dataset to the quality gate of a steady state. It checks the dataset against the gate criteria, such as completeness, structure and required metadata. The outcome is acceptance, conditional acceptance with quality flags, or rejection. Rejected data returns to the producing domain or the data provider. The process makes sure that only data of known quality enters a steady state. |
| **DLM-3** | Register and catalogue data | This process registers an accepted dataset as a new, immutable version. It assigns a persistent identifier and records the metadata in the catalogue. It publishes an event that tells consuming domains a new version is available. Registration makes the data findable for authorised users. Without registration, data cannot be handed over. |
| **DLM-4** | Classify and protect data | This process assigns a security classification to each dataset, for availability, integrity and confidentiality. It applies the protection measures that follow from the classification. It also applies pseudonymisation or other privacy measures where required. Classification is reviewed when data moves to the next steady state. The process applies SAF-P09, SAF-P10 and SAF-P11. |
| **DLM-5** | Store and version data | This process stores each registered version of a dataset safely. Earlier versions are kept, not overwritten. Backups and recovery are arranged according to the availability requirements. Storage follows the retention policy of each steady state. The process makes it possible to reproduce any statistic from the data it was built on. |
| **DLM-6** | Provide data for reuse | This process gives authorised internal users access to registered data. A user requests access, and the data owner decides on the request. Access is granted for a stated purpose and a set period. Use is logged. The process applies SAF-P08 *Data is shared property*, within the limits of confidentiality. |
| **DLM-7** | Revise data | This process handles corrections and redeliveries of data that is already registered. A correction creates a new version that passes the same quality gate. Consumers of the earlier version are notified. They decide whether to reprocess their own data. The reason for each revision is recorded. |
| **DLM-8** | Monitor data quality, lineage and use | This process monitors registered data over time. It tracks quality indicators, the lineage from source to output, and how the data is used. It detects problems, such as declining quality or unauthorised use. It reports to data owners and the data governance board. The results feed into improvements and audits. |
| **DLM-9** | Manage reference and master data | This process manages the data that other data depends on. Examples are classifications, code lists, statistical registers and population frames. It controls versions and publishes changes in advance. It makes sure that all domains use the same version at the same time. Errors in reference data affect many products, so changes are tested carefully. |
| **DLM-10** | Archive and preserve data | This process transfers data that must be kept long-term to an archive. It selects what must be preserved, based on legal obligations and reproducibility needs. It makes sure that archived data remains readable and understandable, with its metadata. Access to archived data is controlled. The process follows national archives legislation. |
| **DLM-11** | Dispose of data | This process deletes data at the end of its retention period. It checks that no statistic or obligation still depends on the data. Deletion covers all copies, including backups and working copies. Keys used for pseudonymisation are destroyed when they are no longer needed. Each disposal is recorded, so that it can be shown in an audit. |

### D. Microdata services processes

Microdata services give researchers controlled access to microdata for statistical and scientific research. Access takes place under strict conditions, usually in a secure processing environment. The NSI remains responsible for confidentiality throughout. These processes realise part of VS-06 *Dissemination and Service Delivery* and work within the collaboration COL-04 *Research access partnership*.

| ID | Process | Description |
|---|---|---|
| **MDS-1** | Authorise institutions and researchers | This process decides which institutions and researchers may use microdata services. It checks the legal status of the institution and the qualifications of the researchers. Authorised institutions sign an agreement that sets the conditions of use. Researchers confirm that they will respect confidentiality. Authorisations are reviewed periodically and can be withdrawn. |
| **MDS-2** | Assess access applications | This process handles an application to use microdata for a specific research project. The applicant describes the purpose, the data needed and the expected outputs. The NSI checks the legal basis, the public interest and whether the data requested is necessary. It also checks for special categories of data that need extra approval. The result is an approval with conditions, or a reasoned refusal. |
| **MDS-3** | Prepare research datasets | This process prepares the datasets for an approved project. It selects only the data that the project needs. It replaces identifiers with project-specific pseudonyms, so that data cannot be linked across projects. Where the project brings its own data, the NSI links it under the same rules. The prepared dataset is registered with its metadata and lineage. |
| **MDS-4** | Provide a secure processing environment | This process sets up the environment in which researchers work with the data. The environment prevents data from leaving without control. Access is limited to the authorised researchers of the project. Tools and computing power are provided as agreed. All activity in the environment is logged. |
| **MDS-5** | Facilitate privacy-preserving analysis | This process supports analysis without moving the data into one place. Examples are federated analysis, where the algorithm goes to the data, and secure multi-party computation. These techniques are used when partners cannot or may not share their data. The NSI defines the trust model, the linkage method and the output rules for each setup. The process extends microdata services to data that the NSI does not hold itself. |
| **MDS-6** | Support researchers | This process helps researchers use the data and the environment correctly. It answers questions about content, metadata and methods. It explains the rules for confidentiality and output. It handles technical problems in the environment. Good support reduces errors and speeds up research. |
| **MDS-7** | Check and release output | This process checks every output before it leaves the secure environment. It applies disclosure control rules to tables, models and other results. It also checks for risks across outputs, such as differencing between similar results. Outputs that pass are released to the researcher. Outputs that fail are returned with an explanation. |
| **MDS-8** | Monitor use and compliance | This process monitors whether institutions and researchers follow the conditions of use. It reviews logs, outputs and incidents. It also tracks the use of query or disclosure budgets where these apply. Breaches lead to measures, up to withdrawal of the authorisation. The results are reported to the data owner and to supervisory authorities where required. |
| **MDS-9** | Close projects | This process ends a research project in a controlled way. It removes the project's data and workspace. It destroys the project-specific pseudonymisation keys. It archives what must be kept for reproducibility, such as the code and the approved outputs. The closure is recorded, so that it can be shown in an audit. |

### E. Data space processes

A data space is a shared environment in which organisations exchange data under common rules, while each keeps control over its own data. Examples are the European data spaces for health, mobility or public administration. An NSI can take part as a data provider, as a data user, or both. Some NSIs also act as an access body that grants access to data on behalf of other data holders. That role is not covered by the SAF reference processes. The data space processes realise parts of VS-01 *Data Acquisition and Ingestion* and VS-06 *Dissemination and Service Delivery*.

| ID | Process | Description |
|---|---|---|
| **DSP-1** | Join a data space | This process prepares the NSI to take part in a data space. It assesses the rules of the data space against the NSI's legal mandate and policies. It signs the participation agreement and obtains the required identity and trust credentials. It sets up the technical connection, for example through a connector. The NSI decides in advance whether it joins as provider, as user, or as both. |
| **DSP-2** | Publish data offerings | This process makes NSI data visible in the data space. It describes datasets in the data space catalogue, using agreed metadata standards. It states the conditions under which the data may be used. Only data that the NSI may share under its legal mandate is offered. The offering is kept up to date when the data or the conditions change. |
| **DSP-3** | Agree data use conditions | This process agrees on the terms of a specific data exchange. Provider and user agree on purpose, duration, permitted use and security measures. The terms are recorded in a contract or usage policy that machines can check where possible. The NSI checks that the terms fit its confidentiality rules. Without agreed terms, no data is exchanged. |
| **DSP-4** | Exchange data under usage control | This process carries out the agreed data exchange. Data is transferred securely, or analysed where it resides without transfer. Usage control enforces the agreed conditions where the technology allows it. Every exchange is logged. Incoming data enters the NSI through the data acquisition process and is registered as raw data. |
| **DSP-5** | Monitor compliance and report | This process monitors whether the NSI's own exchanges follow the rules of the data space. It checks agreements, logs, incidents and the use of data. It reports security incidents within the legal deadlines. It also checks whether partners respect the conditions agreed for NSI data. Breaches lead to measures, including suspension of the exchange. |
| **DSP-6** | Participate in data space governance | This process covers the NSI's role in steering the data space. The NSI takes part in governance bodies and contributes to the rules and standards. It brings in statistical expertise on metadata, classifications, quality and confidentiality. It also evaluates whether participation still serves its mandate. When the NSI leaves a data space, this process arranges a controlled exit. |

| **Toolkit (planned):** Process template and process mapping |
|---|

## Business Functions

### The concept

A **business function** is a grouping of behaviour based on the knowledge, skills and resources it needs. A function describes *what* the organisation does on a continuous basis. It has no start or end, and it does not depend on the order in which work is done. *Manage metadata* is a function: it exists as long as the NSI exists, whatever process happens to use it. Functions are stable, because the competences an organisation needs change much more slowly than its procedures.

Functions differ from processes. A process is a sequence of activities with a trigger and a result. A function is a lasting area of competence that processes draw on. One process uses several functions, and one function serves several processes. The mapping at the end of this section shows how they relate.

Functions also differ from capabilities. A capability, in the Strategy layer, describes an *ability* the NSI has or needs. A function, in the business layer, describes the *behaviour* that delivers that ability. Functions realise capabilities. In practice, the two often have similar names, but they serve different purposes: capabilities support planning and investment, functions support the design of the organisation and its processes.

### How the SAF applies business functions

**Why the SAF describes business functions**

Functions give a stable picture of the organisation that does not change with every reorganisation or new system. They are the natural basis for assigning responsibilities: each function has an owner who maintains the competence. They also help to compare NSIs. Two NSIs may have very different processes and departments, but they will recognise the same functions. Finally, functions make gaps visible. A function that no one owns is a competence that the organisation risks losing.

**How business functions fit into an NSI's own architecture**

An NSI maps its departments and teams onto the SAF functions. The mapping shows which unit carries which function, and where functions are spread over several units. An NSI can also map the SAF functions onto a national function model, such as a government-wide model for business support. Functions that are specific to the NSI's mandate are added as extensions. The SAF function areas for statistical production, data management, microdata services and data spaces are specific to official statistics. The business support area is generic and can be replaced by a national model where one exists.

**Relationships with other concepts**

| Related concept | Relationship | Example in the SAF |
|---|---|---|
| Capabilities (Strategy) | Functions realise capabilities | FUN-7.2 *Manage metadata* realises Metadata management (2.1.2) |
| Business processes | Processes realise functions; functions are assigned to processes | PRD-5.4 *Edit and impute* uses FUN-3.3 *Process statistical data* |
| Business roles | Roles are assigned to functions | ROL-03 *Data steward* is assigned to FUN-7.3 *Manage data lifecycle and storage* |
| Business actors | Organisational units carry functions | A methodology department carries FUN-4.1 |
| Business services | Functions realise business services | FUN-8.1 realises the microdata access service |
| Application services | Application services serve functions | A metadata catalogue serves FUN-7.2 |

**Function areas**

| Area | Name | Scope |
|---|---|---|
| FUN-1 | Strategy and Leadership | Direction, governance and strategic relations of the NSI |
| FUN-2 | Capability Development | Planning, developing and maintaining the abilities of the NSI, including architecture |
| FUN-3 | Statistical Production | Designing, producing and disseminating statistics |
| FUN-4 | Methodology and Research | Statistical methods, research and innovation |
| FUN-5 | Quality Management | The quality framework and quality assurance |
| FUN-6 | Data Supplier Management | Relations, agreements and burden for data providers and respondents |
| FUN-7 | Data Management | Data and metadata as managed assets across their life cycle |
| FUN-8 | Microdata Services | Controlled access to microdata for research |
| FUN-9 | Data Space Participation | Taking part in data spaces as provider and user |
| FUN-10 | Business Support | The generic support functions of the organisation |

|**PLACEHOLDER: ArchiMate view of the SAF function model**|
|---|

### FUN-1 Strategy and Leadership

| ID | Function | Description | Capabilities |
|---|---|---|---|
| **FUN-1** | **Strategy and Leadership** | This area gives direction to the NSI. It sets the vision, the strategy and the priorities. It governs the organisation and accounts for its results. It maintains relationships with the government, the statistical community and society. All other functions work within the direction this area sets. | 4.1 |
| FUN-1.1 | Define vision and strategy | This function defines the mission, vision, goals and values of the NSI. It analyses the national and international environment, including the drivers in the Motivation layer. It translates the vision into a strategy and domain strategies. It sets priorities for the product and service portfolio. The results guide investment and change for several years. | 4.1.1, 4.1.2 |
| FUN-1.2 | Govern and steer the organisation | This function makes sure the NSI is run according to its strategy and its legal mandate. It sets up governance bodies, decision rights and the planning and control cycle. It allocates resources to programmes and departments. It monitors performance and intervenes when needed. It also accounts to the ministry, supervisory bodies and the public. | 4.1.1, 4.1.5 |
| FUN-1.3 | Manage strategic collaboration | This function maintains the strategic relationships of the NSI with other organisations. It covers the national statistical system, international statistical organisations and other governments. It identifies opportunities for joint work, data exchange and shared solutions. It represents the NSI in working groups and governance bodies. It makes sure the NSI speaks with one voice. | 4.1.6 |
| FUN-1.4 | Build public confidence | This function builds and protects public trust in official statistics. It explains the role and independence of the NSI to the public. It promotes the value of statistics and of providing data to the NSI. It responds to misuse or misinterpretation of statistics. Trust is the basis for both response and use, so this function supports the whole chain. | 1.5.2, 4.1.5 |

### FUN-2 Capability Development

| ID | Function | Description | Capabilities |
|---|---|---|---|
| **FUN-2** | **Capability Development** | This area develops and improves the abilities of the NSI. It plans improvements, carries them out and checks whether they deliver. It covers methods, processes, data, systems and skills. It also maintains the enterprise architecture that keeps improvements coherent. This area turns the strategy into concrete change. | 4.1.3, 4.1.4 |
| FUN-2.1 | Plan capability improvements | This function identifies which capabilities need to improve and in which order. It uses capability assessments, evaluations and strategic priorities. It proposes programmes and projects with a business case. It coordinates the plans across the organisation to avoid overlap. The result is a prioritised portfolio of improvements. | 4.1.3 |
| FUN-2.2 | Develop capability improvements | This function carries out approved improvements. It specifies, designs, builds and tests the change. It follows the architecture principles and reuses existing solutions where possible. It involves the people who will use the result. The function ends when the improvement is ready to be taken into use. | 4.1.3, 3.2.1 |
| FUN-2.3 | Monitor capabilities | This function checks whether capabilities perform as intended. It measures maturity and the benefits of past investments. It identifies capabilities that are declining or no longer needed. It reports to management and feeds the next planning round. Without monitoring, investments cannot be shown to pay off. | 4.1.4 |
| FUN-2.4 | Transfer capability improvements to operations | This function hands over a finished improvement to the teams that will run and support it. It arranges documentation, training and support agreements. It checks that the operating teams are ready before the handover. It closes the project or programme. A clean transfer prevents improvements from falling back into project mode. | 3.2.2 |
| FUN-2.5 | Manage enterprise architecture | This function develops and maintains the enterprise architecture of the NSI. It uses the SAF as its reference. It advises on strategy, investments and projects, and reviews them against the architecture principles. It supports the architecture board and keeps the architecture repository up to date. It keeps the NSI architecture aligned with the SAF as both evolve. | |

### FUN-3 Statistical Production

| ID | Function | Description | Capabilities |
|---|---|---|---|
| **FUN-3** | **Statistical Production** | This area produces official statistics, from the first design to the release. It is the core of the NSI's mandate. The statistical production processes (PRD) realise this area. Its functions follow the main kinds of statistical work: design, collection, processing, estimation, confidentiality and dissemination. Each function brings together the specialist knowledge for that kind of work. | 1 |
| FUN-3.1 | Design and build statistical products | This function designs statistical products and the processes that produce them. It translates information needs into outputs, variables, methods and workflows. It also builds and tests the production solution. It works closely with methodology and with the users of the product. The function owns the design of each product over its life cycle. | 1.1 |
| FUN-3.2 | Collect and acquire data | This function obtains the data that statistical products need. It runs surveys, receives administrative data and acquires data from other sources, including data spaces. It makes sure that data arrives complete, on time and under the right agreements. It keeps respondent burden as low as possible. The function delivers data into the first steady state. | 1.2 |
| FUN-3.3 | Process statistical data | This function turns raw data into reliable microdata. It integrates, standardises, codes, validates, edits and imputes data. It also derives new variables and units. It applies the methods designed for each product. The function produces standardised and processed microdata. | 1.3.1, 1.3.2, 1.3.3, 1.3.4 |
| FUN-3.4 | Estimate and analyse | This function produces statistics from microdata and checks that they are sound. It calculates weights, estimates and aggregates. It integrates statistics into consistent wholes, such as the national accounts. It validates and interprets the results. The function produces the statistics that are ready for release. | 1.3.5, 1.3.6, 1.4 |
| FUN-3.5 | Protect statistical confidentiality | This function makes sure that no output reveals information about individual respondents. It sets the confidentiality rules and the methods for disclosure control. It applies them to tables, microdata files and services. It assesses disclosure risks in new types of output. The function works across all products and channels. | 1.3.7 |
| FUN-3.6 | Disseminate statistics | This function brings statistics to users. It manages the release calendar, the publication channels and the products. It makes sure that all users get access at the same moment. It also supports users in finding and understanding the statistics. The function produces released data. | 1.5 |

### FUN-4 Methodology and Research

| ID | Function | Description | Capabilities |
|---|---|---|---|
| **FUN-4** | **Methodology and Research** | This area provides the scientific basis for statistical production. It develops and maintains statistical methods. It explores new data sources, new techniques and new products. It makes sure that innovations are sound before they enter production. This area protects the methodological quality that makes official statistics credible. | 2.2 |
| FUN-4.1 | Manage statistical and analytical methodology | This function develops, documents and maintains the methods used in production. It covers sampling, collection, editing, imputation, estimation, disclosure control and analysis. It includes methods based on machine learning and AI. It advises production teams and reviews their methods. Methods are standardised and shared across products where possible. | 2.2.3 |
| FUN-4.2 | Research and innovate | This function explores new possibilities for statistics. It investigates new data sources and new ways to use existing data. It develops prototypes of new products and methods. It evaluates whether innovations are feasible and sound. Successful innovations are handed over to production through capability development. | 2.2.1, 2.2.2 |

### FUN-5 Quality Management

| ID | Function | Description | Capabilities |
|---|---|---|---|
| **FUN-5** | **Quality Management** | This area makes sure that the NSI delivers statistics of the required quality. It maintains the quality framework and the tools to apply it. It assures quality in products and processes. It prepares the NSI for reviews and audits. This area is the corporate counterpart of the quality management process in production. | 2.1.3 |
| FUN-5.1 | Manage the quality framework | This function sets the quality standards of the NSI. It defines quality dimensions, indicators and reporting requirements. It aligns the framework with international standards, such as the European Statistics Code of Practice. It provides tools and guidance to production teams. The framework is reviewed and improved regularly. | 2.1.3 |
| FUN-5.2 | Assure and review quality | This function checks whether products and processes meet the quality standards. It monitors quality indicators and reviews quality reports. It carries out quality reviews and self-assessments. It follows up on findings with improvement actions. It also supports external reviews, such as peer reviews. | 2.1.3, 4.1.5 |

### FUN-6 Data Supplier Management

| ID | Function | Description | Capabilities |
|---|---|---|---|
| **FUN-6** | **Data Supplier Management** | This area manages the relationships with everyone who supplies data to the NSI. It covers respondents, administrative data holders and other data providers. It sets up and maintains agreements. It monitors the burden that the NSI places on suppliers. Good supplier management improves both the quality of data and the willingness to provide it. | 3.4 |
| FUN-6.1 | Manage data supplier relationships | This function maintains contact with data providers and respondent groups. It explains why the NSI needs the data and how it is used. It handles questions, complaints and feedback on data quality. It coordinates all contacts, so that a supplier deals with one NSI and not with many departments. The function builds long-term cooperation. | 3.4.2 |
| FUN-6.2 | Manage data provision agreements | This function draws up, maintains and enforces agreements with data providers. Agreements cover content, format, timing, quality, security and legal basis. The function keeps a register of all agreements. It renews or adjusts agreements when sources or needs change. It also handles enforcement when obligations are not met. | 3.4.3 |
| FUN-6.3 | Manage response burden | This function measures and limits the burden of statistical data collection. It tracks how much time and effort respondents and data providers spend. It looks for ways to reduce burden, such as reusing existing data. It coordinates surveys so that the same units are not approached too often. It reports on burden to management and government. | 1.2, 2.2.5 |

### FUN-7 Data Management

| ID | Function | Description | Capabilities |
|---|---|---|---|
| **FUN-7** | **Data Management** | This area manages data and metadata as assets of the NSI. It covers governance, metadata, the data life cycle, reference data and data protection. It works across all statistical products and domains. It makes sure that data can be found, understood, trusted and reused. The data lifecycle management processes (DLM) realise this area. | 2.1 |
| FUN-7.1 | Govern data | This function sets the rules for data management in the NSI. It defines data policies, standards and responsibilities. It assigns data owners, data stewards and data custodians. It resolves issues that cross domain boundaries. It monitors compliance with the data policies. | 2.1.1, 4.1.2 |
| FUN-7.2 | Manage metadata | This function captures, maintains and publishes metadata. Metadata describes concepts, variables, classifications, datasets, methods and processes. The function maintains the catalogue in which data can be found. It makes sure that metadata is captured when data is created. It applies international standards, such as GSIM and SDMX. | 2.1.2 |
| FUN-7.3 | Manage data lifecycle and storage | This function manages data from creation to disposal. It covers quality gates, registration, versioning, storage, retention and disposal. It keeps track of lineage, from output back to source. It makes sure that earlier versions remain available when they are needed. The function applies the design rules of the steady-state model. | 2.1.1 |
| FUN-7.4 | Manage reference and master data | This function manages the data that other data depends on. Examples are classifications, code lists, statistical registers and population frames. It controls versions and announces changes in advance. It makes sure that all domains use the same version. The function is the single source of truth for reference data. | 2.1.4 |
| FUN-7.5 | Protect data | This function protects data according to its classification. It applies measures for availability, integrity and confidentiality. It manages pseudonymisation and the keys used for it. It keeps keys separate from the data they protect. The function works closely with information security and privacy management. | 3.3.1, 3.3.4 |

### FUN-8 Microdata Services

| ID | Function | Description | Capabilities |
|---|---|---|---|
| **FUN-8** | **Microdata Services** | This area gives researchers controlled access to microdata. It covers authorisation, data preparation, secure environments and output control. It also supports analysis without moving data, using privacy-preserving techniques. The NSI remains responsible for confidentiality throughout. The microdata services processes (MDS) realise this area. | 2.2.4 |
| FUN-8.1 | Manage research access | This function decides who may use microdata, for which purpose and under which conditions. It authorises institutions and researchers. It assesses applications for research projects. It monitors whether users keep to the conditions. It withdraws access when rules are broken. | 2.2.4, 3.4.3 |
| FUN-8.2 | Prepare research data | This function prepares the datasets for each approved project. It selects only the data that the project needs. It applies project-specific pseudonyms, so that data cannot be linked across projects. It links data that researchers bring in, under the same rules. It documents the prepared data with metadata and lineage. | 2.2.4, 3.3.1 |
| FUN-8.3 | Operate secure research environments | This function provides and runs the environments in which researchers work. It controls who may enter and what may leave. It provides tools and computing power. It logs all activity. It removes data and workspaces when projects end. | 2.2.4, 3.2.5 |
| FUN-8.4 | Control research output | This function checks all results before they leave the secure environment. It applies disclosure control rules to tables, models and other output. It checks for risks across outputs, such as differencing between similar results. It keeps a record of every release. The function protects respondents while allowing research to proceed. | 1.3.7 |
| FUN-8.5 | Enable privacy-preserving analysis | This function makes analysis possible without bringing all data together. It uses techniques such as federated analysis and secure multi-party computation. It defines the trust model, the linkage method and the output rules for each setup. It works with partners who cannot or may not share their data. The function extends microdata services beyond the data the NSI holds itself. | 2.2.4, 2.2.3 |

### FUN-9 Data Space Participation

| ID | Function | Description | Capabilities |
|---|---|---|---|
| **FUN-9** | **Data Space Participation** | This area enables the NSI to take part in data spaces. The NSI can act as a data provider, as a data user, or both. The area covers agreements, technical connection and governance. It makes sure that participation fits the NSI's legal mandate and confidentiality rules. The data space processes (DSP) realise this area. | 4.1.6, 3.4 |
| FUN-9.1 | Manage data space participation | This function decides in which data spaces the NSI takes part, and in which role. It assesses the rules of each data space against the NSI's mandate. It manages participation agreements, data offerings and usage conditions. It monitors whether exchanges follow the agreed rules. It reviews participation regularly. | 4.1.6, 3.4.3 |
| FUN-9.2 | Operate data space connectivity | This function provides the technical connection to data spaces. It runs the connectors, identity credentials and catalogue entries. It carries out data exchanges under the agreed usage conditions. It logs every exchange. Incoming data is passed on to data collection and enters the first steady state. | 3.4.1, 3.2.5 |
| FUN-9.3 | Contribute to data space governance | This function represents the NSI in the governance of data spaces. It contributes to rules, standards and rulebooks. It brings in statistical expertise on metadata, classifications, quality and confidentiality. It aligns positions with other NSIs where possible. It also arranges a controlled exit when participation ends. | 4.1.6 |

### FUN-10 Business Support

| ID | Function | Description | Capabilities |
|---|---|---|---|
| **FUN-10** | **Business Support** | This area provides the people, money, information, technology and facilities that the other functions need. Its functions are similar in every public organisation. The SAF describes them only at a high level. An NSI can replace this area with the function model of its own government. The functions are still part of the SAF, because statistical work depends on them. | 3 |
| FUN-10.1 | Manage human resources | This function makes sure the NSI has enough qualified staff. It covers recruitment, development, performance and the departure of staff. It plans the skills the NSI will need in the future. It supports managers in leading their teams. Skills such as data science and methodology are scarce, which makes this function critical. | 3.1.1 |
| FUN-10.2 | Manage finance and procurement | This function manages the budget, the accounts and the purchase of goods and services. It plans and controls spending. It runs procurement procedures and manages supplier contracts. It reports on the financial position to management and government. It makes sure that spending follows the rules for public money. | 3.1.2, 3.1.3 |
| FUN-10.3 | Manage information technology | This function provides and manages the IT the NSI needs. It covers applications, platforms, infrastructure and the digital workplace. It develops, configures and maintains systems. It runs IT services and resolves disruptions. It plans the evolution of the technical landscape. | 3.2 |
| FUN-10.4 | Manage information and records | This function manages the information created in management and support processes. It keeps records according to archives legislation. It makes information findable and accessible over time. It also manages the knowledge base of the organisation. Statistical data itself is managed by FUN-7 *Data Management*. | 3.1.8 |
| FUN-10.5 | Manage legal affairs | This function provides legal advice and support. It interprets the statistics law, data protection law and other rules. It assesses agreements and contracts. It handles legal procedures and objections. It keeps the overview of legal obligations, for example in a legal register. | 3.1.7 |
| FUN-10.6 | Manage communication | This function manages internal and external communication. It covers press relations, the website, social media and internal information. It makes sure the NSI communicates clearly and consistently. It supports the release of statistics with press releases and explanations. It also handles questions from the media. | 3.1.4 |
| FUN-10.7 | Manage facilities | This function provides the buildings, workplaces and physical services the NSI needs. It covers housing, maintenance, catering and physical access. It makes sure that buildings and spaces are safe. It supports field staff with the means they need. It plans facilities in line with ways of working, such as hybrid work. | 3.1.6, 3.3.5 |
| FUN-10.8 | Manage information security and privacy | This function protects the NSI's information and the privacy of the people it concerns. It sets security and privacy policies and monitors compliance. It manages incidents and leads recovery. It assesses risks in new solutions and suppliers. It includes the role of the data protection officer. | 3.3 |
| FUN-10.9 | Manage users and services | This function manages the relationship with the users of statistics. It identifies user groups and their needs. It manages the portfolio of products and services and their service levels. It handles questions, requests and complaints. It measures user satisfaction and passes feedback on to production. | 3.4.1, 3.4.2, 2.2.5 |

### Process and function mapping

The table shows which functions each process uses. The *main function* carries the knowledge the process mainly depends on. *Supporting functions* contribute specific expertise or resources. In ArchiMate, the process realises part of the main function, and the supporting functions are related through assignment or serving relationships.

|**PLACEHOLDER: ArchiMate view of the process and function mapping**|
|---|

#### A. Statistical production processes

| Process | Name | Main function | Supporting functions |
|---|---|---|---|
| **PRD-1** | **Specify Needs** | FUN-3.1 | FUN-10.9 |
| PRD-1.1 | Identify needs | FUN-3.1 | FUN-10.9 |
| PRD-1.2 | Consult and confirm needs | FUN-3.1 | FUN-10.9 |
| PRD-1.3 | Establish output objectives | FUN-3.1 | FUN-5.1 |
| PRD-1.4 | Identify concepts | FUN-3.1 | FUN-4.1 |
| PRD-1.5 | Check data availability and suitability | FUN-3.1 | FUN-6.1, FUN-7.2 |
| PRD-1.6 | Prepare and submit business case | FUN-3.1 | FUN-1.2, FUN-2.1 |
| **PRD-2** | **Design** | FUN-3.1 | FUN-4.1 |
| PRD-2.1 | Design outputs and dissemination | FUN-3.1 | FUN-3.5, FUN-3.6 |
| PRD-2.2 | Design variables | FUN-3.1 | FUN-7.2, FUN-7.4 |
| PRD-2.3 | Design collection | FUN-3.1 | FUN-3.2, FUN-6.1 |
| PRD-2.4 | Design frame and sample | FUN-3.1 | FUN-4.1, FUN-7.4 |
| PRD-2.5 | Design processing and analysis | FUN-4.1 | FUN-3.1, FUN-3.5 |
| PRD-2.6 | Design production systems and workflows | FUN-3.1 | FUN-2.5, FUN-10.3 |
| **PRD-3** | **Build** | FUN-3.1 | FUN-10.3 |
| PRD-3.1 | Reuse or build collection instruments | FUN-3.1 | FUN-3.2 |
| PRD-3.2 | Reuse or build processing and analysis components | FUN-3.1 | FUN-4.1, FUN-10.3 |
| PRD-3.3 | Reuse or build dissemination components | FUN-3.1 | FUN-3.6, FUN-10.3 |
| PRD-3.4 | Configure workflows | FUN-3.1 | FUN-7.3, FUN-10.3 |
| PRD-3.5 | Test production systems | FUN-3.1 | FUN-10.3 |
| PRD-3.6 | Test statistical business process | FUN-3.1 | FUN-5.2 |
| PRD-3.7 | Finalise production systems | FUN-3.1 | FUN-2.4, FUN-7.2 |
| **PRD-4** | **Collect** | FUN-3.2 | FUN-6.1 |
| PRD-4.1 | Create frame and select sample | FUN-3.2 | FUN-4.1, FUN-7.4 |
| PRD-4.2 | Set up collection | FUN-3.2 | FUN-6.2 |
| PRD-4.3 | Run collection | FUN-3.2 | FUN-6.1, FUN-6.3 |
| PRD-4.4 | Finalise collection | FUN-3.2 | FUN-7.3 |
| **PRD-5** | **Process** | FUN-3.3 | FUN-3.4 |
| PRD-5.1 | Integrate data | FUN-3.3 | FUN-7.4, FUN-7.5 |
| PRD-5.2 | Classify and code | FUN-3.3 | FUN-7.4 |
| PRD-5.3 | Review and validate | FUN-3.3 | FUN-5.2 |
| PRD-5.4 | Edit and impute | FUN-3.3 | FUN-4.1 |
| PRD-5.5 | Derive new variables and units | FUN-3.3 | FUN-7.2 |
| PRD-5.6 | Calculate weights | FUN-3.4 | FUN-4.1 |
| PRD-5.7 | Calculate aggregates | FUN-3.4 | FUN-4.1 |
| PRD-5.8 | Finalise data files | FUN-3.3 | FUN-7.3 |
| **PRD-6** | **Analyse** | FUN-3.4 | FUN-3.5 |
| PRD-6.1 | Prepare draft outputs | FUN-3.4 | FUN-3.6 |
| PRD-6.2 | Validate outputs | FUN-3.4 | FUN-5.2 |
| PRD-6.3 | Interpret and explain outputs | FUN-3.4 | FUN-10.6 |
| PRD-6.4 | Apply disclosure control | FUN-3.5 | FUN-4.1 |
| PRD-6.5 | Finalise outputs | FUN-3.4 | FUN-5.2 |
| **PRD-7** | **Disseminate** | FUN-3.6 | FUN-10.9 |
| PRD-7.1 | Update output systems | FUN-3.6 | FUN-10.3 |
| PRD-7.2 | Produce dissemination products | FUN-3.6 | FUN-10.6 |
| PRD-7.3 | Release dissemination products | FUN-3.6 | FUN-1.4 |
| PRD-7.4 | Promote dissemination products | FUN-3.6 | FUN-10.6, FUN-1.4 |
| PRD-7.5 | Provide user support | FUN-10.9 | FUN-3.6 |
| **PRD-8** | **Evaluate** | FUN-5.2 | FUN-2.3 |
| PRD-8.1 | Gather evaluation inputs | FUN-5.2 | FUN-7.3 |
| PRD-8.2 | Conduct evaluation | FUN-5.2 | FUN-2.3 |
| PRD-8.3 | Agree an action plan | FUN-2.1 | FUN-5.2 |

#### B. Overarching processes

| Process | Name | Main function | Supporting functions |
|---|---|---|---|
| OVA-1 | Quality Management | FUN-5.2 | FUN-5.1 |
| OVA-2 | Metadata Management | FUN-7.2 | FUN-7.4 |
| OVA-3 | Data Management | FUN-7.3 | FUN-7.1 |
| OVA-4 | Process Data Management | FUN-7.3 | FUN-5.2 |
| OVA-5 | Knowledge Management | FUN-10.4 | FUN-4.1 |
| OVA-6 | Data Supplier Management | FUN-6.1 | FUN-6.3 |

#### C. Data lifecycle management processes

| Process | Name | Main function | Supporting functions |
|---|---|---|---|
| DLM-1 | Plan and design data assets | FUN-7.1 | FUN-2.5 |
| DLM-2 | Promote data through a quality gate | FUN-7.3 | FUN-5.2 |
| DLM-3 | Register and catalogue data | FUN-7.2 | FUN-7.3 |
| DLM-4 | Classify and protect data | FUN-7.5 | FUN-10.8 |
| DLM-5 | Store and version data | FUN-7.3 | FUN-10.3 |
| DLM-6 | Provide data for reuse | FUN-7.1 | FUN-7.3 |
| DLM-7 | Revise data | FUN-7.3 | FUN-7.2 |
| DLM-8 | Monitor data quality, lineage and use | FUN-7.1 | FUN-5.2 |
| DLM-9 | Manage reference and master data | FUN-7.4 | FUN-7.2 |
| DLM-10 | Archive and preserve data | FUN-10.4 | FUN-7.3 |
| DLM-11 | Dispose of data | FUN-7.3 | FUN-7.5 |

#### D. Microdata services processes

| Process | Name | Main function | Supporting functions |
|---|---|---|---|
| MDS-1 | Authorise institutions and researchers | FUN-8.1 | FUN-10.5 |
| MDS-2 | Assess access applications | FUN-8.1 | FUN-10.5, FUN-7.1 |
| MDS-3 | Prepare research datasets | FUN-8.2 | FUN-7.5 |
| MDS-4 | Provide a secure processing environment | FUN-8.3 | FUN-10.3, FUN-10.8 |
| MDS-5 | Facilitate privacy-preserving analysis | FUN-8.5 | FUN-4.1, FUN-7.5 |
| MDS-6 | Support researchers | FUN-8.3 | FUN-10.9 |
| MDS-7 | Check and release output | FUN-8.4 | FUN-3.5 |
| MDS-8 | Monitor use and compliance | FUN-8.1 | FUN-10.8 |
| MDS-9 | Close projects | FUN-8.3 | FUN-7.3, FUN-7.5 |

#### E. Data space processes

| Process | Name | Main function | Supporting functions |
|---|---|---|---|
| DSP-1 | Join a data space | FUN-9.1 | FUN-10.5, FUN-10.8 |
| DSP-2 | Publish data offerings | FUN-9.1 | FUN-7.2 |
| DSP-3 | Agree data use conditions | FUN-9.1 | FUN-10.5 |
| DSP-4 | Exchange data under usage control | FUN-9.2 | FUN-3.2, FUN-7.3 |
| DSP-5 | Monitor compliance and report | FUN-9.1 | FUN-10.8 |
| DSP-6 | Participate in data space governance | FUN-9.3 | FUN-1.3 |

#### Functions without a reference process

Six functions are not used by any SAF reference process. They are carried out through management, change or support processes that are specific to each NSI. Many other functions appear only as supporting functions, which is normal for strategic and support functions.

| Function | Carried out through |
|---|---|
| FUN-1.1 Define vision and strategy | The strategic planning cycle of the NSI |
| FUN-2.2 Develop capability improvements | Change programmes and projects |
| FUN-4.2 Research and innovate | Innovation projects (see VS-08) |
| FUN-10.1 Manage human resources | Generic business support processes |
| FUN-10.2 Manage finance and procurement | Generic business support processes |
| FUN-10.7 Manage facilities | Generic business support processes |

### Mapping to value stream stages

The mapping connects the Strategy layer to the business layer. A value stream stage describes the value that is added. The processes describe the work that adds it. The functions describe the competences that the work depends on.

|**PLACEHOLDER: ArchiMate view of value stream stages, processes and functions**|
|---|

#### Primary value streams

| Stage | Name | Realised by processes | Main functions |
|---|---|---|---|
| VS-01.1 | Identify Data Needs and Sources | PRD-1.1, PRD-1.5, PRD-2.3 | FUN-3.1, FUN-6.1 |
| VS-01.2 | Establish Data Agreements and Access Rights | OVA-6, DSP-1, DSP-3 | FUN-6.2, FUN-9.1, FUN-10.5 |
| VS-01.3 | Collect or Receive Data | PRD-4.1, PRD-4.2, PRD-4.3, DSP-4 | FUN-3.2, FUN-9.2 |
| VS-01.4 | Validate and Log Data Intake | PRD-4.4, DLM-2 | FUN-3.2, FUN-7.3 |
| VS-01.5 | Store and Register Raw Data Artefacts | DLM-3, DLM-4, DLM-5 | FUN-7.2, FUN-7.3, FUN-7.5 |
| VS-02.1 | Profile and Assess Data Structure | PRD-5.3 | FUN-3.3 |
| VS-02.2 | Apply Standard Classifications and Formats | PRD-5.2, DLM-9 | FUN-3.3, FUN-7.4 |
| VS-02.3 | Align Metadata and Semantics | OVA-2 | FUN-7.2 |
| VS-02.4 | Validate Structural and Semantic Conformance | PRD-5.3, DLM-2 | FUN-3.3, FUN-7.3 |
| VS-02.5 | Register Standardized Artefacts | DLM-3, DLM-4, DLM-5 | FUN-7.2, FUN-7.3, FUN-7.5 |
| VS-03.1 | Conduct Error Detection and Quality Diagnostics | PRD-5.3 | FUN-3.3 |
| VS-03.2 | Perform Data Editing and Correction | PRD-5.2, PRD-5.4 | FUN-3.3 |
| VS-03.3 | Impute Missing or Non-Response Data | PRD-5.4 | FUN-3.3, FUN-4.1 |
| VS-03.4 | Derive Additional Variables and Indicators | PRD-5.1, PRD-5.5 | FUN-3.3 |
| VS-03.5 | Perform Quality Evaluation and Versioning | PRD-5.8, DLM-2, DLM-3 | FUN-3.3, FUN-5.2, FUN-7.3 |
| VS-04.1 | Confirm Estimation and Analytical Approach | PRD-2.4, PRD-2.5 | FUN-3.1, FUN-4.1 |
| VS-04.2 | Apply Weighting and Calibration | PRD-5.6 | FUN-3.4 |
| VS-04.3 | Estimate and Aggregate Data | PRD-5.7 | FUN-3.4 |
| VS-04.4 | Perform Model-Based Analysis | PRD-6.1, PRD-6.3 | FUN-3.4 |
| VS-04.5 | Validate and Document Results | PRD-6.2, PRD-6.4, OVA-2 | FUN-3.4, FUN-3.5, FUN-7.2 |
| VS-05.1 | Select and Integrate Source Datasets | PRD-5.1, PRD-6.1 | FUN-3.4 |
| VS-05.2 | Construct Composite Indicators or Indices | PRD-5.5, PRD-5.7 | FUN-3.3, FUN-3.4 |
| VS-05.3 | Perform Consistency and Coherence Checks | PRD-6.2 | FUN-3.4, FUN-5.2 |
| VS-05.4 | Generate Analytical and Interpretive Outputs | PRD-6.3, PRD-7.2 | FUN-3.4, FUN-3.6 |
| VS-05.5 | Approve and Register Statistical Products | PRD-6.4, PRD-6.5, DLM-3 | FUN-3.4, FUN-3.5, FUN-7.2 |
| VS-06.1 | Plan Dissemination and Access Strategy | PRD-2.1 | FUN-3.1, FUN-3.6 |
| VS-06.2 | Prepare Data for Dissemination | PRD-6.4, PRD-7.1 | FUN-3.5, FUN-3.6 |
| VS-06.3 | Publish and Provide Access Services | PRD-7.2, PRD-7.3, MDS-1 to MDS-5, MDS-7, DSP-2 | FUN-3.6, FUN-8.1 to FUN-8.5, FUN-9.1 |
| VS-06.4 | Support and Engage Users | PRD-7.4, PRD-7.5, MDS-6 | FUN-3.6, FUN-8.3, FUN-10.9 |
| VS-06.5 | Monitor Usage and Feedback | PRD-8.1, MDS-8, MDS-9 | FUN-8.1, FUN-8.3, FUN-10.9 |

#### Supporting value streams

| Stage | Name | Realised by processes | Main functions |
|---|---|---|---|
| VS-07.1 | Define Governance Frameworks and Policies | DLM-1 | FUN-1.2, FUN-5.1, FUN-7.1 |
| VS-07.2 | Establish Legal and Regulatory Compliance Mechanisms | DLM-4 | FUN-10.5, FUN-10.8 |
| VS-07.3 | Implement Data and Metadata Governance | OVA-2, OVA-3, DLM-1, DLM-6 | FUN-7.1, FUN-7.2 |
| VS-07.4 | Monitor Quality and Compliance Indicators | OVA-1, DLM-8, MDS-8, DSP-5 | FUN-5.2, FUN-7.1 |
| VS-07.5 | Audit, Certify and Report Compliance | OVA-1, PRD-8.2 | FUN-1.2, FUN-5.2 |
| VS-07.6 | Update and Improve Governance Mechanisms | PRD-8.3, DLM-10, DLM-11 | FUN-2.1, FUN-7.1 |
| VS-08.1 | Identify Innovation Needs and Opportunities | PRD-1.5 | FUN-4.2 |
| VS-08.2 | Conduct Research and Proof-of-Concepts | No reference process (NSI-specific) | FUN-4.2 |
| VS-08.3 | Evaluate Methodological Soundness and Feasibility | PRD-3.6 | FUN-4.1, FUN-5.2 |
| VS-08.4 | Develop and Document New Methodologies or Tools | PRD-3.2, OVA-5 | FUN-4.1, FUN-10.4 |
| VS-08.5 | Integrate Innovation into Production Environments | PRD-3.7 | FUN-2.4, FUN-3.1 |
| VS-08.6 | Promote Knowledge Sharing and Capability Building | OVA-5 | FUN-10.1, FUN-10.4 |
| VS-09.1 | Define Digital and Technical Requirements | PRD-2.6 | FUN-2.5, FUN-3.1 |
| VS-09.2 | Design Platform and Infrastructure Architecture | PRD-2.6 | FUN-2.5, FUN-10.3 |
| VS-09.3 | Provision and Configure Platforms | PRD-3.4, MDS-4 | FUN-8.3, FUN-10.3 |
| VS-09.4 | Enable Integration and Orchestration Services | PRD-3.4, DSP-4 | FUN-9.2, FUN-10.3 |
| VS-09.5 | Ensure Performance, Security and Continuity | PRD-3.5, DLM-5 | FUN-10.3, FUN-10.8 |
| VS-09.6 | Evolve and Modernise the Technical Ecosystem | No reference process (NSI-specific) | FUN-2.2, FUN-10.3 |
| VS-10.1 | Identify and Segment Stakeholders | PRD-1.2, DSP-6 | FUN-1.3, FUN-10.9 |
| VS-10.2 | Collect and Analyse User Needs | PRD-1.1, PRD-1.2 | FUN-3.1, FUN-10.9 |
| VS-10.3 | Define and Manage Service Portfolios | PRD-2.1 | FUN-10.9 |
| VS-10.4 | Deliver Services and Manage Relationships | PRD-7.5, MDS-6, OVA-6 | FUN-6.1, FUN-10.9 |
| VS-10.5 | Engage and Communicate with Stakeholders | PRD-7.4 | FUN-1.4, FUN-10.6 |
| VS-10.6 | Monitor Impact and Satisfaction | PRD-8.1, PRD-8.2 | FUN-5.2, FUN-10.9 |

| **Toolkit (planned):** Function template and organisation-to-function mapping |
|---|

## Business Services, Events and Objects

The sections on business services and interfaces, business events, and business objects, contracts, representations and products are planned for a later version. Until then, the services, events and objects of each value stream are described in attribute 8 of the Statistical Data Value Chain chapter, and the objects handed over between value streams in the Steady-State Architecture.

|**PLACEHOLDER: Business Services and Business Interfaces; Business Events; Business Objects, Contracts, Representations and Products**|
|---|

## Reference Models for the Statistical Data Value Chain
**Why the SAF offers more than one model**
NSIs differ in size, mandate, legal context, data volumes, and technology platform. A single prescribed arrangement would fit some offices well and others poorly. The SAF therefore describes reference models: alternative, internally consistent ways of organising the value chain. Each model answers the same four questions:

1. At which points is data persisted and made available for reuse?
2. Which quality criteria must data meet at each point?
3. Who is accountable for the data at each point?
4. How are confidentiality and traceability guaranteed along the chain?

The SAF currently describes two reference models. Both follow the same underlying idea, progressive improvement of data through defined layers, but they differ in granularity and in where they place governance.

**Model A: Steady-State Architecture**

The Steady-State Architecture organises the value chain into business domains that are loosely coupled through five numbered steady states (#1 Raw, #2 Standardized, #3 Processed, #4 Statistics, #5 Released). Each state represents a specific kind of statistical value and has its own quality gate, ownership, and handover interface. The model is derived from production practice in NSIs with many statistical domains and extensive microdata reuse. It is described in full in the remainder of this chapter.

**Model B: Medallion Architecture**

The Medallion Architecture organises data into three layers of increasing quality, usually called Bronze (raw), Silver (cleansed and conformed), and Gold (curated for consumption). The pattern originates from lakehouse platforms and is a logical design pattern rather than a product. Its strength lays in its simplicity. There are three layers, a clear direction of flow, and the ability to rebuild any layer from the one below it.

As a data-engineering pattern, Medallion does not by itself define statistical semantics, accountability, or confidentiality rules per layer.

### Comparison

| Characteristic | Steady-State Architecture | Medallion Architecture |
|---|---|---|
| Number of governed handover points | Five (#1 to #5) | Three (Bronze, Silver, Gold) |
| Origin | Statistical production practice | Lakehouse data engineering |
| Granularity of quality gates | Fine: one gate per kind of statistical value | Coarse: several kinds of value combined per layer |
| Separation of standardisation and editing | Explicit (#2 vs. #3) | Combined in Silver |
| Separation of internal statistics and released data | Explicit (#4 vs. #5) | Combined in Gold unless subdivided |
| Governance overhead | Higher: more states to own, register, and audit | Lower |
| Fit with platform tooling | Platform-neutral; mapping required | Native in lakehouse platforms |
| Typical adopters | Larger NSIs, many domains, high microdata reuse | Smaller NSIs, platform-led modernisation |

### Selection criteria

The criteria below help an NSI decide which model fits best. They are indicative. No single criterion is decisive, and the SAF toolkit will provide a structured assessment.

| Criterion | Points towards Steady-State | Points towards Medallion |
|---|---|---|
| Organisational size and number of statistical domains | Many domains, many teams handing over data | Few domains, small central data team |
| Reuse of intermediate microdata across domains | High; standardised and processed microdata reused by several products | Limited; most data flows within one product chain |
| Legal requirements on pseudonymisation timing | Law or policy requires a separate, auditable pseudonymisation point | Pseudonymisation can be applied at the Silver boundary |
| Archival and reproducibility obligations | Specific states (e.g., processed microdata) must be retained long term | Retention can be defined per layer |
| Separation of internal statistics from released data | Required (embargo, different confidentiality thresholds per use) | Achievable by subdividing Gold |
| Metadata and governance maturity | Mature data ownership and catalogue practices in place | Governance capacity is limited and must stay lean |
| Technology platform | Heterogeneous landscape, on-premises and private cloud | Single lakehouse platform |
| Participation in international data exchange | Many handover points to external partners | Exchange concentrated on final outputs |

Practice within the SAF community indicates that smaller NSIs often adopt a Medallion arrangement, while larger NSIs with many domains tend towards finer-grained states. This observation is to be substantiated through the SAF toolkit assessments.

### Combining the models

The models are not mutually exclusive. The steady states can be mapped onto Medallion layers, which allows an NSI to use Medallion as its platform convention while governing data through steady states, or to start with Medallion and introduce finer states as it grows.

| Steady state | Medallion layer | Note |
|---|---|---|
| #1 Raw Data | Bronze | Direct correspondence |
| #2 Standardized Data | Silver (lower sub-layer) | In Medallion often merged with #3 |
| #3 Processed Data | Silver | Main reusable microdata layer |
| #4 Statistics | Gold (internal sub-layer) | Not yet released |
| #5 Released Data | Gold (published sub-layer) | Released after final disclosure control |
| #6 Data Products | Gold (consumption product sub-layer) | Packaged for consumption |

# Steady-State Architecture

## Overview

### Business domains

The statistical process is divided into three main business domains (Observation, Processing/Analysis, and Dissemination). Processing/Analysis is divided into four subdomains, which results in six business domains. Each domain adds one specific kind of statistical value and produces one steady state.

| # | Business domain | Value added | Business functions (ArchiMate view) | Value stream | GSBPM | State in → out |
|---|---|---|---|---|---|---|
| 1 | Observation/Collection | Data in NSI custody, authentic and traceable | Receive Data, Extract Data, Collect Survey | VS-01 | 4 | #0 → #1 |
| 2 | Standardization without loss of content | Common structure, format, and classifications | Transform Data, Anonymize Data, Classify Data | VS-02 | 5.1–5.2 | #1 → #2 |
| 3 | Editing, derivation, and non-response correction | Reliable, complete, enriched microdata | Imputate Data, Integrate Data | VS-03 | 5.3–5.5, 5.8 | #2 → #3 |
| 4 | Estimation and balancing | Representative statistics with accuracy | Estimate Data, Aggregate Data | VS-04 | 5.6–5.7, 6.1–6.4 | #3 → #4 |
| 5 | Statistically composed and composite products | Coherent, approved products | Compose Data | VS-05 | 6.5, 7.1–7.2 | #4 → #4 (approved) |
| 6 | Dissemination | Disclosure-safe, accessible released data | Data Delivery, Data Publication | VS-06 | 6.4, 7.3–7.5 | #4 → #5 |
| — | Consumption (external) | Use of statistics by society | Data Consumption, Consumption Optimisation | VS-10 (feedback) | 8 | #5 → (#6) |

The execution processes between the business domains are loosely coupled. Each has its own design and implementation. They exchange data only through steady states: handover points at the boundaries between the domains, listed in *Steady states at a glance* below. Each domain produces one state; Observation, for example, produces Raw Data. A steady state is therefore an environment where high-quality versions of data are brought together for exchange, and it also represents a value in the value chain of this data.

### The four process types

Each business domain uses the same four process types: Design provides metadata, Implementation provides the execution process, Execution provides the statistical data, and Management provides quality reports. They are described in *The four process types* in the Statistical Data Value Chain chapter. How an execution process adds statistical value, and therefore how it is designed and implemented, falls outside the scope of the SAF business architecture. That design follows from, among other things, the NSI's methodology.

### Design rules of the steady-state model

The model rests on six design rules. They apply the SAF architecture principles to the data value chain.

1. **Loose coupling through states (SAF-P07).** Domains exchange data only through registered steady states, never through each other's internal working data. A domain can change its methods or systems without affecting its neighbours, as long as the state it produces meets its quality gate.
2. **One state, one kind of value.** Each state represents exactly one kind of added statistical value. This keeps quality gates testable and accountability unambiguous.
3. **Immutable quality versions.** Data registered in a state is never overwritten. Corrections and redeliveries create a new version, so every statistic can be traced to the exact data it was built on.
4. **No state without metadata (SAF-P09).** Registration requires the minimum metadata set of the state. Data without it does not enter the state.
5. **Progressive confidentiality (SAF-P11).** Protection increases along the chain: direct identifiers are removed or pseudonymised at #2, disclosure risk is assessed at #3, initial disclosure control is applied at #4, and final disclosure control gates #5.
6. **Reuse before reprocessing (SAF-P08).** An authorised consumer that needs data at a given level of value reuses the registered state rather than repeating the upstream processing.

### Steady states at a glance

| Position | Name | Produced by | Kind of value | Mandatory? |
|---|---|---|---|---|
| (#0) | Source Data | External provider | Outside NSI custody, boundary position | n/a |
| #1 | Raw Data | VS-01 | Authentic, traceable custody | When the product collects its own data |
| #2 | Standardized Data | VS-02 | Comparability, values unchanged | Optional |
| #3 | Processed Data | VS-03 | Reliability and completeness of microdata | Always |
| #4 | Statistics | VS-04, VS-05 | Representative, approved statistics | Always |
| #5 | Released Data | VS-06 | Disclosure-safe, accessible output | When output is released |
| (#6) | Consumed Data | External users | Outside NSI control, boundary position | n/a |

### State lifecycle

Every steady state follows the same lifecycle:

1. **Promotion.** The producing domain submits a dataset to the quality gate of the target state.
2. **Gate outcome.** The dataset is accepted, conditionally accepted with explicit quality flags, or rejected. Rejected data does not enter the state; it returns to the producing domain or, for #1, to the provider.
3. **Registration.** An accepted dataset receives a persistent identifier, its metadata is registered in the catalogue, and a registration event notifies consuming domains.
4. **Consumption.** Authorised consuming domains read the registered version. Responsibility for further processing transfers on receipt of the event; custody of the registered version stays with the producer.
5. **Revision.** A correction produces a new version that passes the same gate. Consumers are notified and decide whether to reprocess. Earlier versions remain available for as long as statistics depend on them.
6. **Retirement.** A version is disposed of according to the retention policy of the state, after its lineage obligations have been met.

### Applying the steady states pragmatically {#pragmatic-steady-states}

A steady state is an agreement about data: the quality it has reached, who owns it, how it is identified and what metadata comes with it. It does not require a separate physical copy at every state, and it does not require every process to pass through all of them. An office may depart from the usual sequence in the three cases below, provided it records the choice (which state was shared or skipped, and why) in the catalogue entry. In other words, the rule is "comply or explain".

1. **Two states can share one artefact.** If nothing happens between State #4 and State #5 (no transformation and no further disclosure control), the #4 artefact does not have to be registered again as a new dataset; it is marked as released instead. The release steps still take place: release authorisation is obtained and the final disclosure check is carried out, and both are recorded even when the check changes nothing.
2. **A process can start downstream.** Not every production process begins at VS-01. Macro statistics, for example, are often built on Processed Data (#3) or Statistics (#4) that another team has already registered. State #4 explicitly allows such internal reuse as input to other statistical processes. Such a process starts from the registered artefact and its lineage points to it; there is no need to create placeholder #1 or #2 artefacts. Data that comes from outside the office still enters through VS-01 and State #1.
3. **Lineage is about traceability, not duplication.** SAF-P09 requires that every value can be traced back to where it came from. When a stream uses an artefact without changing any values, a logged process event that refers to the existing artefact version meets this requirement, and no identical copy needs to be registered. As soon as a value changes, a new version is registered.

One limit applies to all three cases. States must not be merged where this would hide a change of values (for example, standardisation at #2 and editing at #3 carried out as a single undocumented step) or a disclosure-control step (for example, #4 and #5 when additional disclosure control is applied before release).

### How each state is described

Each state below is described with the same ten attributes. NSIs can use this template to document their own implementation.

| # | Attribute | Question it answers |
|---|---|---|
| 1 | Definition and value added | What is this state and why does it exist? |
| 2 | Producing and consuming domains | Who creates it, and who may use it? |
| 3 | Quality gate | What must data satisfy to be registered? |
| 4 | Data and metadata characteristics | What does the data look like, and which metadata must accompany it? |
| 5 | Security, privacy, and access | How is the data protected, and who may see it? |
| 6 | Ownership and governance | Who is accountable? |
| 7 | Versioning, retention, and lineage | How are versions managed, how long are they kept, and how is the trace preserved? |
| 8 | Reuse and handover | How is the state made available to consumers? |
| 9 | Traceability to the framework | Which capabilities, value-stream stages, and GSBPM sub-processes relate to it? |
| 10 | Examples and anti-patterns | What does good practice look like, and what should be avoided? |

Attributes 3 to 9 contain only what is specific to each state. What all states share is described once, in *Rules common to all states*.

| **Toolkit:** SAF-TK-G05 Steady-state record and gate log |
|---|

### Rules common to all states {#rules-common-to-all-states}

The rules below apply to every state from #1 to #5. The state descriptions that follow do not repeat them. They describe only what is specific to each state, and any deviation.

**Quality gate.** Every gate has three possible outcomes: accepted, conditionally accepted with explicit quality flags, or rejected (see *State lifecycle*). Conditional acceptance is a deliberate option. Data with a known and measured issue may still be the best available data, and the flag ensures that every downstream user knows about the issue. The release gate of #5 is the only exception: its disclosure criteria allow no conditional acceptance.

**Common metadata.** The minimum metadata set of every state contains the elements below, in addition to the state-specific elements listed per state.

| Metadata element | Description |
|---|---|
| Persistent identifier and version | Unique identifier of this version (delivery, quality, analytical, approved, or release version) and its registration timestamp |
| Source reference | From #2 onward: the registered version or versions it was produced from. #1 records its provenance instead |
| Gate outcome | Accepted or conditionally accepted, with quality flags |
| Classification | Availability, integrity, and confidentiality rating, and the resulting access level and authorised roles |

**Ownership.** Three roles exist for every state. Each state adds its specific roles, and states what its data owner is accountable for.

| Role | Responsibility |
|---|---|
| Data owner | Process owner of the producing domain; accountable for the quality of the state |
| Data steward | Registers versions, maintains catalogue entries, and resolves gate exceptions |
| Data custodian | Operates storage, access control, and retention; where pseudonymisation keys exist, manages them separately from the data, under separate access rights |

**Versioning and retention.** Every registration creates a new immutable version. A redelivery, a correction, a new run, or a change of rules, models, or methods creates a new version. An earlier version is never overwritten, because later versions or published statistics may already be built on it. Each version records the exact input versions and rule versions it was produced from. Retention periods are set by national law and NSI policy; each state describes the usual arrangement.

**Reuse and handover.** Registration publishes the registration event of the state and a catalogue entry. Consumers discover a version through the catalogue and access it through the handover interface, never through the intake system or working environment of the producing domain. The producing value stream keeps custody of the registered version; the consumer takes responsibility for further processing on receipt of the event. Under SAF-P08, an authorised consumer reuses the registered version instead of repeating the upstream work. Each state lists its handover elements and its typical reuse.

**Principles.** Every state applies SAF-P07, SAF-P08, SAF-P09, SAF-P10, and SAF-P11, as described in the design rules above.


## Boundary Position #0: Source Data

**Description:** Source data is data as it exists at the data holder, before it enters the NSI: a register at a government agency, a company's accounting system, a respondent's answers before submission, or a web page. The NSI has no custody of source data and cannot guarantee its quality. It can influence it only through agreements, questionnaire design, and cooperation with the data holder.

**Why it is described:** The SAF describes #0 so that the boundary of the NSIs responsibility is explicit. Everything the NSI knows about source data is captured as metadata when the data crosses into #1: who provided it, under which agreement, through which channel, and in what condition.

## State #1: Raw Data

### 1. Definition and value added

Raw data is data received from an external data holder or respondent, placed under NSI custody in its original form, and verified for technical integrity and authenticity. It is the first point of possession. At this moment the NSI does not have access to the data at the source, so #1 is the earliest point at which the NSI can guarantee what it holds.

The value of #1 is **authentic custody**. It proves that the NSI holds exactly what the provider delivered, when it was delivered, under which legal basis, and through which channel. That proof is the foundation for all downstream traceability. If a statistic is ever questioned, the chain of evidence ends here.

### 2. Producing and consuming domains

| Role | Domain | Note |
|---|---|---|
| Producer | Observation/Collection (VS-01) | Functions: Receive Data, Extract Data, Collect Survey |
| Primary consumer | Standardisation (VS-02) | Triggered by the *Raw Data Registered* event |
| Secondary consumer | Editing (VS-03) | Only where #2 is skipped for this product |
| Occasional consumer | Innovation and Methodology (VS-08) | Source exploration, under specific authorisation |
| Assurance | Governance and Compliance (VS-07) | Audit of provenance and legal basis |

### 3. Quality gate

The gate for #1 checks technical and legal conditions only. It does not assess content; content quality is the concern of #3.

| Criterion | Check | Typical outcome on failure |
|---|---|---|
| Legal basis | A valid agreement or statutory basis covers this delivery | Reject; escalate to legal |
| Sender authenticity | Sender verified (certificate, credentials, signed delivery) | Reject |
| Integrity | Checksum or digital signature matches | Reject; request redelivery |
| Security | Malware and security scan passed | Quarantine; reject |
| Structural conformance | Delivery matches the agreed technical specification (file format, schema, encoding) | Reject or conditionally accept with flag |
| Completeness against agreement | Record counts and delivery scope within agreed tolerance | Conditionally accept with flag, or reject |
| Timeliness | Delivered within the agreed window | Accept with flag; report to relationship management |
| Metadata | Minimum metadata set captured (see attribute 4) | Hold until complete |

A late or slightly incomplete delivery is the typical case for conditional acceptance at #1.

### 4. Data and metadata characteristics

**Data.** Raw data is stored in its original format, or in a lossless technical equivalent. Permitted technical operations are those that change representation without changing content and that can be reversed: decryption, decompression, character-encoding normalisation, and container conversion. Operations that change values, codes, or record selection are not permitted at #1. The original byte stream, or a verifiable hash of it, is retained.

**Minimum metadata set** (in addition to the common metadata).

| Metadata element | Description |
|---|---|
| Provider | Organisation or respondent group that supplied the data |
| Agreement reference and legal basis | Agreement identifier, validity period, purpose limitation, and the applicable legal ground |
| Channel and method | Transfer channel (file transfer, API, data space connector, survey mode) and instrument version |
| Receipt timestamp | Moment of receipt into NSI custody |
| Integrity proof | Checksum or signature value and algorithm |
| Volume | Record count and size |
| Reference period | Period the data describes, as stated by the provider |
| Structural description | Schema or technical specification the delivery conforms to |
| Intake validation result | Number of validation errors per check, completeness rate and field coverage, and timeliness against the agreed delivery window |

In GSIM terms, #1 typically instantiates a *Data Set* received from an *Information Provider* through an *Exchange Channel* under a *Provision Agreement*.

### 5. Security, privacy, and access

Raw data usually contains direct identifiers and therefore carries the highest confidentiality rating in the chain. Access is limited to the roles that operate the intake and the standardisation process. Analysts and subject-matter staff do not work on #1.

Pseudonymisation is normally applied at the transition to #2. Some NSIs pseudonymise at the intake boundary, or receive data already pseudonymised by a trusted third party. Both variants are compatible with the model, provided the choice is documented and the key management is separated from the data. Data minimisation starts before #1: the agreement and the collection design determine that only necessary data is received.

### 6. Ownership and governance

| Role | Responsibility for #1 |
|---|---|
| Data owner | Process owner of Observation/Collection; accountable for lawful acquisition and fitness of the intake |
| Relationship manager | Handles provider follow-up on rejected or flagged deliveries (with VS-10) |

### 7. Versioning, retention, and lineage

A redelivery or correction by the provider is a new version, like any other delivery.

Retention of #1 is governed by two needs that pull in opposite directions. Reproducibility and audit favour keeping raw data; data minimisation and storage cost favour disposal. A common arrangement is to keep #1 until the dependent #3 version is verified and the audit period has passed, while #3 is the state subject to long-term archival requirements.

Lineage at #1 is the provenance record: the link from the registered version to the provider, the agreement, and the delivery event. Every downstream state must be able to trace back to a #1 version or, where a product starts from another domain's data, to the state it consumed.

### 8. Reuse and handover

One delivery can serve several statistical products. The register-based census and the labour market statistics may both draw on the same population register delivery. Reusing the registered delivery, rather than requesting the same data again from the provider, also reduces response burden.

| Handover element | Content |
|---|---|
| Artefact | Registered Raw Data version |
| Required metadata | Minimum metadata set (attribute 4) |
| Trigger event | *Raw Data Registered* |
| Responsibility transfer | VS-01 keeps custody; the consumer takes responsibility for further processing on receipt of the event |

### 9. Traceability to the framework

| Framework element | References |
|---|---|
| Capabilities | 1.2.1 Primary data collection, 1.2.2 Secondary data collection, 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 3.3.4 Logical identity and access control, 3.4.3 Service agreement |
| Value-stream stages | VS-01.3 Collect or Receive Data; VS-01.4 Validate and Log Data Intake; VS-01.5 Store and Register Raw Data Artefacts |
| GSBPM | 4.3 Run collection, 4.4 Finalise collection |

### 10. Examples and anti-patterns

**Examples**

- *Survey.* Responses from a web questionnaire are received with paradata (mode, completion time, instrument version). The delivery is registered as one #1 version per collection batch.
- *Administrative register.* A quarterly tax file arrives by file transfer, with a manifest. Checksum, schema, and record count are checked against the agreement; 14 unknown business identifiers are not a #1 issue and pass through for handling downstream.
- *Web data.* Daily scraped price data is registered with the scraper version and page fingerprint per retailer, so a change in a website's structure can be traced to the affected deliveries.

**Anti-patterns**

- Correcting obvious errors "while the file is open" at intake. Any value change belongs in #3, where it is documented.
- Overwriting a delivery with the provider's corrected version. Statistics built on the first version lose their trace.
- Giving analysts direct access to raw data for convenience. This bypasses the pseudonymisation at #2.
- Keeping only a converted copy and discarding the original. The proof of authentic custody is lost.
- Registering a delivery without its agreement reference. The legal basis can no longer be demonstrated in an audit.

## State #2: Standardized Data

### 1. Definition and value added

Standardised data is raw data that has been brought into the common structure, format, and classifications of the NSI. Its values are unchanged. Only the representation changes: fields are renamed and restructured, types are cast, source codes are mapped one-to-one to standard codes, and descriptive metadata is attached. Direct identifiers are removed or replaced with pseudonymous keys. #2 is therefore the first state in which data from different sources can be compared and combined, and the first state without direct identifiers.

The value of #2 is **comparability without loss of content**. Data that looked different at the source now uses the same structure, the same codes, and documented definitions, units, and reference periods. Because no value has changed, the trace back to the authentic delivery in #1 stays simple and deterministic. Every interpretation, correction, or conversion is left to #3, where it is documented as an edit.

#2 is an optional state. A product can go directly from #1 to #3, for example when a source already arrives in the NSI's standard structure and coding. In that case the NSI records in the catalogue that #2 was skipped, and why (see *Applying the steady states pragmatically*). **[SS1]**

### 2. Producing and consuming domains

| Role | Domain | Note |
|---|---|---|
| Producer | Standardization without loss of content (VS-02) | Functions: Transform Data, Anonymize Data, Classify Data |
| Primary consumer | Editing (VS-03) | Triggered by the *Standardized Data Registered* event |
| Secondary consumer | Other statistical products | Reuse of the same standardised source under SAF-P08, with authorisation |
| Occasional consumer | Innovation and Methodology (VS-08) | Exploration of sources and methods, under specific authorisation |
| Assurance | Governance and Compliance (VS-07) | Audit of mapping lineage and pseudonymisation |

### 3. Quality gate

The gate for #2 checks conformance and preservation. It does not assess whether values are correct; that is the concern of #3. A value that cannot be mapped is not an error of standardisation. It is a fact about the source, so it is flagged and handed to VS-03.

| Criterion | Check | Typical outcome on failure |
|---|---|---|
| Structural conformance | Fields, types, formats, and cardinalities match the target data model | Reject; re-map |
| Classification conformance | Every mapped code exists in the stated classification version; no orphan codes | Reject; correct the correspondence table |
| Mapping coverage | Share of source codes mapped one-to-one is above the agreed threshold | Conditionally accept with flag; unmapped values listed for VS-03 |
| Semantic metadata | Unit, currency, reference-period basis, and definition recorded for every variable | Hold until complete |
| No loss of content | Record counts and key measures identical to the #1 version; no value changed | Reject |
| Identifier protection | Direct identifiers removed or pseudonymised according to the privacy design | Reject; escalate to the privacy officer |
| Referential integrity | Linkage keys exist in the reference register (e.g., the statistical business register) | Conditionally accept with flag |
| Metadata and lineage | Minimum metadata set captured (see attribute 4); field-level lineage complete | Hold until complete |

Conditional acceptance is the normal outcome for many sources. Unmapped codes and unmatched keys are often caused by known lags, such as newly registered businesses. The flag ensures every downstream user knows exactly which values still need work.

### 4. Data and metadata characteristics

**Data.** Standardised data is stored in the canonical target data model. Standard codes are stored next to the original source values, so the original remains visible. Permitted operations are renaming, restructuring, type casting, reformatting (for example from CSV to a standard exchange format), key alignment, one-to-one code mapping through maintained correspondence tables, removal or pseudonymisation of direct identifiers, and dropping variables that are not needed for the statistical purpose. Operations that change values are not permitted at #2: unit or currency conversion, reference-period alignment, reconciliation of differing definitions, derivation, interpretive coding of free text, editing, and imputation. These belong to #3. **[SS2]**

**Minimum metadata set** (in addition to the common metadata).

| Metadata element | Description |
|---|---|
| Source reference | The #1 version or versions this dataset was produced from |
| Target model version | Version of the canonical data model applied |
| Mapping ruleset and engine version | Versions of the mapping rules and the tool that applied them |
| Classifications applied | Scheme and version per coded variable (e.g., NACE Rev. 2, ISCED 2011) |
| Mapping coverage and unmapped values | Coverage per variable and the list of values routed to VS-03 |
| Units, currency, and reference-period basis | Recorded per variable as received, not converted |
| Concept links and definition differences | Link to the canonical concept; recorded differences with other sources |
| Pseudonymisation record | Identifiers removed or pseudonymised, method, key reference (never the key itself) |
| Conformance assessment | Structural, classification, and semantic results; no-loss-of-content confirmation |

In GSIM terms, #2 typically instantiates a *Unit Data Set* that conforms to a *Data Structure*, whose *Represented Variables* take their values from *Statistical Classifications* and *Code Lists*.

### 5. Security, privacy, and access

#2 is the point where direct identifiers leave the working data. **Removal** deletes an identifier and ends the possibility to link on it. **Pseudonymisation** replaces it with a key that still allows records to be linked. The privacy design decides per identifier which of the two applies, and the choice is recorded in the pseudonymisation record.

Pseudonymisation keys are managed by the data custodian (see *Rules common to all states*). Staff who work on #2 and later states never have access to the keys. Some NSIs pseudonymise at intake, or receive data already pseudonymised by a trusted third party. In that case #2 confirms and records the protection that is already in place.

Standardised data is still detailed microdata. Indirect identifiers, such as date of birth, place of residence, or occupation, remain, and combinations of them can identify a person or business. The confidentiality rating of #2 therefore stays high. Access is limited to the roles that standardise and edit the data, and to authorised reusers with a stated purpose. The formal assessment of disclosure risk starts at #3. **[SS3]**

### 6. Ownership and governance

| Role | Responsibility for #2 |
|---|---|
| Data owner | Process owner of Standardisation; accountable for conformance and for applying the privacy design |
| Classification steward | Maintains the correspondence tables and the classification versions used in mapping |
| Metadata and data architect | Owns the target data model and the links to canonical concepts |

### 7. Versioning, retention, and lineage

A rule change alone also creates a new version, even when the input stays the same: a new correspondence table, a new classification version, or a revised target model.

Standardisation is deterministic, so a #2 version can be regenerated from its #1 version and the recorded rule versions. Many NSIs therefore keep #2 only as long as the dependent #3 versions are produced and reviewed. This only works while #1 and the rule versions are themselves retained. If #1 is disposed of earlier, #2 must be kept for as long as reproducibility requires.

Lineage at #2 is field-level. Each standardised value can be traced to the raw value it came from and to the mapping rule that was applied. The pseudonymisation record shows which identifiers were replaced, without revealing the keys.

### 8. Reuse and handover

One standardised source can serve many statistical products. A population register delivery is standardised once and is then used by the census, labour market statistics, and income statistics. Standardising the same source again for each product wastes effort and leads to inconsistent coding of the same source.

The list of unmapped values and the recorded units and periods travel with the handover. VS-03 then knows exactly which interpretive coding and conversions remain to be done.

| Handover element | Content |
|---|---|
| Artefact | Registered Standardized Data version |
| Required metadata | Minimum metadata set (attribute 4), including unmapped values and recorded units and periods |
| Trigger event | *Standardized Data Registered* |
| Responsibility transfer | VS-02 keeps custody; the consumer takes responsibility for editing, interpretive coding, and conversion on receipt of the event |

### 9. Traceability to the framework

| Framework element | References |
|---|---|
| Capabilities | 1.3.1 Data standardisation, 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.4 Statistical register management, 3.3.1 Privacy management, 3.3.4 Logical identity and access control |
| Value-stream stages | VS-02.1 Profile and Assess Data Structure; VS-02.2 Apply Standard Classifications and Formats; VS-02.3 Align Metadata and Semantics; VS-02.4 Validate Structural and Semantic Conformance; VS-02.5 Register Standardized Artefacts |
| SAF processes **[SS4]** | PRD-5.2 Classify and code (deterministic mapping only), PRD-5.3 Review and validate (structural checks only), DLM-2 Promote data through a quality gate, DLM-3 Register and catalogue data, DLM-4 Classify and protect data, DLM-9 Manage reference and master data |
| GSBPM | 5.1 Integrate data (key alignment only; record linkage takes place in #3), 5.2 Classify and code |
| Medallion layer **[SS4]** | Silver, lower sub-layer; in a Medallion arrangement often merged with #3 |

### 10. Examples and anti-patterns

**Examples**

- *Survey.* Labour Force Survey returns are restructured into the canonical person and household model. Source education codes are mapped one-to-one to ISCED 2011, and region codes to NUTS-3. The 42,000 free-text occupation answers are not coded here; they are listed as unmapped and handed to VS-03. The personal identifier is replaced with a pseudonymous key.
- *Administrative register.* The tax authority's internal activity codes are mapped to NACE Rev. 2 through a maintained correspondence table; 0.6% of codes have no correspondence and are flagged. Turnover stays in thousands of euro on a fiscal-year basis, and this basis is recorded as metadata. Conversion to units on a calendar-year basis takes place in #3.
- *Web data.* Scraped price records are reshaped into the canonical price record. Currency, unit, and scrape timestamp are recorded as metadata, and prices are kept exactly as received. Most products only have a free-text name and are passed to VS-03 for classification to COICOP.

**Anti-patterns**

- Converting currencies or units at #2 "because the data is open anyway". The value changes without an edit record.
- Coding free text with a classifier at #2. Interpretive coding needs review and logging, which happens in #3.
- Silently dropping records with unknown codes. This breaks the no-loss-of-content guarantee.
- Overwriting a #2 version after a correspondence table update. Statistics built on the earlier version lose their trace.
- Storing pseudonymisation keys together with the data. The protection of #2 is then only on paper.
- Skipping #2 without recording the reason. Auditors can no longer see why the state is missing.

## State #3: Processed Data

### 1. Definition and value added

Processed data is microdata whose content has been checked, corrected, completed, and enriched. Errors, duplicates, outliers, and inconsistencies have been detected and resolved. Missing values have been imputed, free text has been coded, and units, currencies, and reference periods have been converted to a common basis. Records from different sources have been linked, and new variables have been derived. Unlike in #2, values do change here, but every change is documented, attributable, and reversible.

The value of #3 is **reliability and analytical readiness**. Every estimate, model, and publication downstream rests on this microdata. The guarantee is not that values stay the same, but that no value changes without a record of the original value, the rule or decision applied, the reason, the actor, and the time. That record makes it possible to explain, reproduce, or reverse any change.

#3 is mandatory for all statistical production, because it is the microdata on which everything downstream is verifiably built. It is also the state that national archival requirements usually apply to: without it, the statistics built on it cannot be re-verified. **[SS5]**

Processing is primarily driven by the individual statistical domains. Depending on the type of data, it may also be performed by a central unit for efficiency and consistency. Either way, the result is registered as #3 under the same quality gate.

### 2. Producing and consuming domains

| Role | Domain | Note |
|---|---|---|
| Producer | Editing, derivation, and non-response correction (VS-03) | Functions: Imputate Data, Integrate Data |
| Primary consumer | Estimation and Analysis (VS-04) | Triggered by the *Processed Data Registered* event |
| Secondary consumer | Other statistical products | Reuse of processed microdata under SAF-P08, with authorisation |
| Secondary consumer | Microdata services (VS-06) | Research datasets are prepared from #3 and released as #5 **[SS6]** |
| Occasional consumer | Innovation and Methodology (VS-08) | Testing of new editing, imputation, or coding methods, under specific authorisation |
| Assurance | Governance and Compliance (VS-07) | Audit of edit lineage, methodology compliance, and disclosure risk |

### 3. Quality gate

The gate for #3 checks content quality and traceability. It is the first gate that judges whether values are plausible and complete. A dataset may pass with known remaining quality issues, as long as they are measured and documented.

| Criterion | Check | Typical outcome on failure |
|---|---|---|
| Rule conformance | No record violates the validation and editing rules after correction | Reject; re-edit |
| Edit lineage | Every changed value has its original value, rule or decision, reason, actor, and time recorded | Hold until complete |
| Imputation flags | Every imputed value carries a flag and a method code; no observed value is overwritten | Reject |
| Coding | Free-text values are coded or explicitly left uncoded with a reason; low-confidence codes are reviewed | Conditionally accept with flag |
| Conversion and reconciliation | Every unit, currency, or reference-period conversion and every reconciliation has its rule and original value recorded | Hold until complete |
| Linkage quality | Linkage rate and match quality are measured and within agreed limits | Conditionally accept with flag, or reject |
| Derived variables | Every derived variable has a formula, inputs, unit, and classification | Hold until complete |
| Quality improvement | Completeness and accuracy measured against the #2 baseline (or #1 where #2 was skipped) | Conditionally accept with flag |
| Disclosure risk | Re-identification risk of the enriched and linked data assessed against the privacy design | Reject; reduce detail or restrict access |
| Reproducibility | The version can be regenerated from its inputs plus the recorded rules and models | Reject |

Conditional acceptance is common for imputation and linkage. A linkage rate slightly below target may still give the best available data. The flag makes sure estimation in VS-04 takes the issue into account, for example in its variance estimation.

### 4. Data and metadata characteristics

**Data.** Processed data contains the processed value of every variable. The original value stays recoverable through the edit lineage, and imputed values carry a flag. Permitted operations are error detection, editing and correction, imputation, interpretive coding of free text, conversion of units, currencies, and reference periods, reconciliation of values between sources, record linkage, and derivation of new variables and units. These are the value-changing operations that #2 deliberately left open. Operations that turn microdata into statistics are not permitted at #3: weighting, calibration, estimation, and aggregation belong to #4. **[SS5]**

**Minimum metadata set** (in addition to the common metadata).

| Metadata element | Description |
|---|---|
| Source reference | The #2 version or versions, or #1 where #2 was skipped |
| Rule and model versions | Versions of the editing rules, imputation models, coding service, and derivation specifications applied |
| Edit lineage | Per changed value: original value, new value, rule or decision, reason code, actor, and time |
| Imputation record | Per imputed value: flag, method code, and the predictors or donors used |
| Coding record | Per coded value: source text, assigned code, method, and confidence |
| Conversion and reconciliation record | Rule, factor or rate, and original value for every conversion or reconciliation |
| Linkage record | Keys used, matching method, linkage rate, and match quality |
| Derived variables | Formula, inputs, unit, and classification per derived variable |
| Quality assessment | Edit rate, imputation rate, coding completion, and improvement against the baseline |
| Disclosure-risk assessment | Outcome of the re-identification risk assessment and the resulting access conditions |

In GSIM terms, #3 typically instantiates a *Unit Data Set*, extended with derived *Represented Variables*. The edits are described as *Rules* applied in *Process Steps*, which gives the edit lineage its formal structure.

### 5. Security, privacy, and access

Processed data is pseudonymised microdata, but it is richer than #2. Linking sources and deriving variables adds detail, and more detail means a higher risk that a person or business can be recognised. #3 is therefore the point where the disclosure risk of microdata is formally assessed. The outcome sets the conditions for access and reuse.

Linkage uses the pseudonymous keys created at #2. The keys themselves remain with the data custodian, separately from the data. Access to #3 is limited to the roles that edit, estimate, and analyse the data, and to authorised reusers with a stated purpose. External researchers never access #3 directly. Their access runs through the microdata services in VS-06, which prepare a project-specific dataset with its own pseudonyms and release it as #5.

The edit audit trail is itself sensitive and must be tamper-evident. It shows who changed which value and why, which is essential evidence in an audit.

### 6. Ownership and governance

| Role | Responsibility for #3 |
|---|---|
| Data owner | Process owner of Editing; accountable for the quality version and for the correct application of approved methods |
| Data custodian | In addition to the common responsibilities: archival of #3 (see attribute 7) |
| Methodologist | Owns the editing rules, imputation methodology, and derivation specifications |
| Subject-matter statistician | Adjudicates flagged records and signs off domain-specific corrections |

### 7. Versioning, retention, and lineage

Every completed editing cycle produces a new quality version. Many NSIs distinguish preliminary and final versions; both are registered as separate quality versions of #3.

#3 is usually the state with the longest retention. It is the microdata that must be preserved to re-verify published statistics, and archival legislation often applies to it. When #3 is archived, its edit lineage, imputation flags, and derived-variable definitions are archived with it. Without that metadata, the archived values cannot be interpreted.

Lineage at #3 is value-level. Each processed value can be traced back to its original value in #2 or #1, the rule or decision that changed it, and the inputs of any imputation, conversion, or derivation. Linked records keep a reference to the source records they were built from.

### 8. Reuse and handover

Processed microdata is the most valuable reusable asset in the chain. An integrated person-level dataset, edited and enriched once, can serve many statistics on labour, income, education, and health. Editing the same data twice leads to different corrections of the same record, and therefore to statistics that do not agree.

The imputation flags travel with the handover. VS-04 needs them to reflect the extra uncertainty of imputed values in its accuracy measures.

| Handover element | Content |
|---|---|
| Artefact | Registered Processed Data quality version |
| Required metadata | Minimum metadata set (attribute 4), including edit lineage, imputation flags, and derived-variable definitions |
| Trigger event | *Processed Data Registered* |
| Responsibility transfer | VS-03 keeps custody; the consumer takes responsibility for weighting, estimation, and analysis on receipt of the event |

### 9. Traceability to the framework

| Framework element | References |
|---|---|
| Capabilities | 1.3.2 Deriving variables and units, 1.3.3 Check content, 1.3.4 Adjusting and imputing, 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management, 2.1.4 Statistical register management |
| Value-stream stages | VS-03.1 Conduct Error Detection and Quality Diagnostics; VS-03.2 Perform Data Editing and Correction; VS-03.3 Impute Missing or Non-Response Data; VS-03.4 Derive Additional Variables and Indicators; VS-03.5 Perform Quality Evaluation and Versioning |
| SAF processes | PRD-5.1 Integrate data, PRD-5.2 Classify and code (interpretive coding), PRD-5.3 Review and validate, PRD-5.4 Edit and impute, PRD-5.5 Derive new variables and units, PRD-5.8 Finalise data files, DLM-2, DLM-3, DLM-7 Revise data, DLM-10 Archive and preserve data |
| GSBPM | 5.1 Integrate data, 5.2 Classify and code, 5.3 Review and validate, 5.4 Edit and impute, 5.5 Derive new variables and units, 5.8 Finalise data files |
| Medallion layer | Silver; the main reusable microdata layer |

### 10. Examples and anti-patterns

**Examples**

- *Survey.* The 42,000 free-text occupation answers handed over from #2 are coded to ISCO-08: 88% automatically, the rest computer-assisted or by experts. Item non-response on income (9%) is imputed by regression and flagged. Each coded and imputed value carries its method, so it can be reviewed or revised later.
- *Administrative register.* Turnover, received in thousands of euro on a fiscal-year basis, is converted to units on a calendar-year basis. The conversion factor and the original value are stored in the lineage. The tax data is then linked to the business survey on the statistical business register key, and a reconciliation rule resolves values where the two sources disagree.
- *Web data.* Products with only a free-text name are classified to COICOP with a machine-learning classifier; low-confidence cases are reviewed. Prices are converted to euro and standard units. Missing daily prices are filled by carry-forward and flagged with a staleness indicator.

**Anti-patterns**

- Overwriting the original value with the corrected one. The edit can no longer be explained or reversed.
- Imputing without a flag. Estimation then treats imputed values as observed and understates uncertainty.
- Correcting every outlier by hand. Over-editing costs effort, changes little in the results, and can introduce bias.
- Calculating weights or aggregates at #3. That work belongs to #4, where its method and accuracy are documented.
- Fixing values in a spreadsheet outside the editing pipeline. The change has no lineage and cannot be reproduced.
- Linking an extra source without reassessing disclosure risk. The richer dataset may identify people that #2 did not.
- Disposing of #3 once figures are published. The published statistics can then no longer be verified.

## State #4: Statistics

### 1. Definition and value added

Statistics are the results produced from processed microdata: estimates, aggregates, indices, time series, and model outputs. Each result carries the method that produced it and a measure of its accuracy, such as a standard error or confidence interval. State #4 can also hold output microdata with weights, prepared for a specific internal purpose. Initial disclosure control has been applied, so the results can potentially be released. They are not yet released: #4 may still contain detail that is confidential or not suitable for publication.

The value of #4 is **statistical credibility and coherence**. Data has become information about a population, and that information is accurate, transparent, and consistent with related statistics. Any figure in #4 can be regenerated from #3 and defended, because its method, parameters, weights, and accuracy are recorded.

#4 is produced by two domains and therefore has **two gate moments**. **[SS7]**

| Gate moment | Produced by | Status of the version | What it confirms |
|---|---|---|---|
| Analytical gate | Estimation and closed-loop (VS-04) | *Analytical* | Results are methodologically sound, accurate, coherent, and initially disclosure-controlled |
| Approval gate | Statistically composed and composite products (VS-05) | *Approved* | Results are composed into a coherent product, explained, checked against dissemination and confidentiality standards, and signed off |

Both are versions of the same state. Approval does not change an analytical version; it creates a new, immutable version with the status *approved* that refers to the analytical versions it was composed from.

### 2. Producing and consuming domains

| Role | Domain | Note |
|---|---|---|
| Producer (analytical) | Estimation and closed-loop (VS-04) | Functions: Estimate Data, Aggregate Data |
| Producer (approved) | Statistically composed and composite products (VS-05) | Function: Compose Data |
| Primary consumer (analytical) | Product composition (VS-05) | Triggered by the *Output Data Registered* event |
| Primary consumer (approved) | Dissemination (VS-06) | Triggered by the *Statistical Product Registered* event |
| Secondary consumer | Other statistical processes | Internal input for macro statistics and integration systems, such as the national accounts |
| Assurance | Governance and Compliance (VS-07) | Audit of methodology, reproducibility, and approval |

### 3. Quality gate

The two gate moments check different things. The analytical gate tests the statistics; the approval gate tests the product.

**Analytical gate (VS-04)**

| Criterion | Check | Typical outcome on failure |
|---|---|---|
| Approved method | Estimation, weighting, and model methods are approved and documented for this output | Reject; return to design |
| Weights | Calibration converged; weights within the agreed bounds | Reject; re-weight |
| Accuracy | Every estimate has an accuracy measure; imputation uncertainty from #3 is reflected | Hold until complete |
| Model diagnostics | Diagnostics of model-based results are within the agreed limits | Reject, or conditionally accept with flag |
| Soundness and coherence | Results are plausible and coherent with prior periods and related statistics; large movements are explained | Conditionally accept with flag, or reject |
| Initial disclosure control | Disclosure risk assessed and initial protection applied | Reject |
| Reproducibility | Results regenerate from #3 plus the recorded methodology and parameters | Reject |
| Metadata | Minimum metadata set captured (see attribute 4) | Hold until complete |

**Approval gate (VS-05)**

| Criterion | Check | Typical outcome on failure |
|---|---|---|
| Component selection | The exact analytical versions used are pinned and recorded | Hold until complete |
| Composition | Composite indicators, indices, and time series follow their documented specifications | Reject; re-compose |
| Consistency and coherence | Totals reconcile to components; the product is coherent with related and prior products | Return to VS-04, or conditionally accept with explained flag |
| Interpretive content | Commentary and visualisations are reviewed and consistent with the data and its accuracy | Hold until complete |
| Dissemination and confidentiality standards | The product meets the standards, including the disclosure risk of combining outputs | Reject |
| Sign-off | The designated approval authority has approved the product | Hold until approved |

Coherence problems at the approval gate are never solved by adjusting a component estimate in VS-05. If a component is wrong, it goes back to VS-04 and returns as a new analytical version.

### 4. Data and metadata characteristics

**Data.** Statistics in #4 are mostly aggregated data: tables, data cubes, indicators, indices, and time series. They can also include weighted output microdata, prepared for a specific internal use. Permitted operations are weighting and calibration, estimation and aggregation, model-based analysis, seasonal adjustment, initial disclosure control, and, at the approval stage, composition of indicators, indices, and time series from analytical versions. Changing microdata values is not permitted at #4: corrections go back to #3. Final disclosure control for release is not part of #4 either; it belongs to the transition to #5. **[SS8]**

**Minimum metadata set** (in addition to the common metadata).

| Metadata element | Description |
|---|---|
| Status | *Analytical* or *approved* |
| Source reference | The #3 versions (for analytical versions) or the analytical #4 versions (for approved versions) used |
| Methodology | Estimation, weighting, and model methods, with their versions and parameters |
| Weights and calibration totals | Calibration method, auxiliary variables, and the source and version of the totals |
| Accuracy | Standard error, coefficient of variation, or confidence interval per estimate; whether imputation uncertainty is included |
| Model diagnostics | Fit and prediction intervals for model-based results |
| Disclosure control | Method applied and outcome of the risk assessment |
| Coherence results | Outcome of the coherence checks against related and prior statistics |
| Composition record | For approved versions: composition method and the component versions used |
| Interpretive content | For approved versions: reference to commentary, key messages, and visualisations |
| Approval record | For approved versions: approval authority, date, and confidentiality clearance |

In GSIM terms, aggregated results in #4 typically instantiate a *Dimensional Data Set*, and weighted output microdata a *Unit Data Set*. Both conform to a *Data Structure* that SDMX can use for exchange.

### 5. Security, privacy, and access

Initial disclosure control is applied at the analytical gate, so the results could in principle be released. That does not make #4 public. It may still hold detailed cells, internal breakdowns, or output microdata that are only suitable for internal use. Different confidentiality thresholds can apply depending on the intended use, and the version records which threshold was applied.

Composition creates a specific risk. Two tables that are each safe on their own can together reveal a value through differencing. The approval gate therefore checks the disclosure risk of the product as a whole, not only of its components.

Approved products are usually market-sensitive or politically sensitive before their release. Access to approved versions is restricted to the people who need it to prepare the release. Every pre-release access is logged, so equal access at the moment of release can be demonstrated.

### 6. Ownership and governance

| Role | Responsibility for #4 |
|---|---|
| Data owner (analytical) | Process owner of Estimation; accountable for methodological soundness and accuracy |
| Data owner (approved) | Process owner of Product Composition; accountable for coherence and interpretability of the product |
| Approval authority | Signs off approved versions against dissemination and confidentiality standards |
| Data custodian | In addition to the common responsibilities: the pre-release access log |
| Methodologist | Owns estimation, weighting, and model methods |
| Disclosure control specialist | Owns the disclosure-control rules for internal and potential external use |

### 7. Versioning, retention, and lineage

Every estimation run produces a new analytical version. Every approval produces a new approved version that refers to the analytical versions it was built from. Revisions follow the revision policy: a preliminary figure, a revised figure, and a final figure are three separate versions.

Approved versions that were released are kept for as long as the released figures exist, because they are the direct basis of #5. Analytical versions that never led to a release can be kept for a shorter period, as long as revisions and reproducibility are covered.

Lineage at #4 has two steps. An estimate traces back to the #3 version, the method, the parameters, and the weights that produced it. An approved product traces back to the analytical versions it was composed from, and through them to #3.

### 8. Reuse and handover

#4 has two handovers, one for each gate moment. The analytical version goes to VS-05 for composition; the approved version goes to VS-06 for release.

Statistics in #4 are also reused internally. Integration systems, such as the national accounts or labour accounts, use statistics from many domains as input. Reusing the registered version instead of estimating the same figure again keeps internal use and later publication consistent.

| Handover element | Analytical version (VS-04 → VS-05) | Approved version (VS-05 → VS-06) |
|---|---|---|
| Artefact | Registered analytical #4 version | Registered approved #4 version |
| Required metadata | Methodology, weights, accuracy, model diagnostics, disclosure control, coherence results | Composition record, propagated accuracy, coherence results, interpretive content, approval record |
| Trigger event | *Output Data Registered* | *Statistical Product Registered* |
| Responsibility transfer | VS-04 keeps custody; VS-05 takes responsibility for composition and approval | VS-05 keeps custody; VS-06 takes responsibility for final disclosure control, release, and user support |

### 9. Traceability to the framework

| Framework element | References |
|---|---|
| Capabilities | 1.3.5 Estimating population parameters, 1.3.6 Integrate statistics, 1.3.7 Statistical disclosure, 1.4.1 Statistical (output) analysis, 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| Value-stream stages | VS-04.1 to VS-04.5 (analytical gate); VS-05.1 to VS-05.5 (approval gate) |
| SAF processes | PRD-5.6 Calculate weights, PRD-5.7 Calculate aggregates, PRD-6.1 Prepare draft outputs, PRD-6.2 Validate outputs, PRD-6.3 Interpret and explain outputs, PRD-6.4 Apply disclosure control (initial), PRD-6.5 Finalise outputs, PRD-7.2 Produce dissemination products (content), DLM-2, DLM-3, DLM-7 Revise data |
| GSBPM | 5.6 Calculate weights, 5.7 Calculate aggregates, 6.1 to 6.5 Analyse |
| Medallion layer | Gold, internal sub-layer; not yet released |

### 10. Examples and anti-patterns

**Examples**

- *Survey.* The Labour Force Survey estimates an employment rate of 71.4%, with a 95% confidence interval of ±0.5 percentage points at national level. The variance includes the uncertainty of imputed income from #3. This analytical version is then composed with unemployment and vacancy figures into the quarterly labour market product, which is approved and registered.
- *Administrative register.* Turnover is aggregated by industry and region. For small domains where the direct aggregate is unstable, a small-area model is used, and its results are flagged as model-based. In the approval gate, one domain fails the coherence check; it goes back to VS-04 instead of being adjusted in the product.
- *Web data.* A multilateral price index is calculated from the item prices in #3. The headline index and its main divisions are composed with the period weights, checked for coherence with the prior month and year, and approved.

**Anti-patterns**

- Approving a product by overwriting the analytical version. The difference between the tested figure and the approved figure disappears.
- Adjusting a component estimate in VS-05 to make the coherence check pass. The estimate no longer matches its documented method.
- Publishing an estimate without an accuracy measure. Users cannot judge whether a movement is meaningful.
- Treating initial disclosure control as final. Release requires the final check of the transition to #5.
- Sharing approved figures before release without logging the access. Equal access can no longer be demonstrated.
- Re-estimating a figure for internal use instead of reusing the registered version. Internal and published figures start to differ.

## State #5: Released Data

### 1. Definition and value added

Released data is statistical output that the NSI has made available outside its own organisation. It is based on an approved #4 version that has passed final disclosure control, has been documented for correct interpretation, and has been released through a trusted channel. Released data includes published tables and datasets, open data, data available through an API, deliveries to international organisations, data offered in a data space, and de-identified microdata made available to accredited researchers. #5 is the last point at which the NSI controls the data. Once users have it, it becomes consumed data, outside the NSI's control.

The value of #5 is **accessibility and trust**. Users get accurate, documented statistics through channels they can rely on, at a moment that is the same for everyone. The final disclosure check ensures that no respondent can be identified. The documentation ensures that users can interpret the figures correctly, including their accuracy and limitations.

#5 is mandatory whenever output is released. If nothing changes between the approved #4 version and the release, the same artefact can be marked as released instead of being registered again. The release steps still take place and are recorded: release authorisation, the final disclosure check, and the release itself (see *Applying the steady states pragmatically*).

### 2. Producing and consuming domains

| Role | Domain | Note |
|---|---|---|
| Producer | Dissemination (VS-06) | Functions: Data Delivery, Data Publication |
| Primary consumer | External users | Policy makers, researchers, media, businesses, and the public; use turns #5 into #6 |
| Primary consumer | International organisations | Deliveries under agreed transmission programmes, such as to Eurostat or the OECD |
| Primary consumer | Accredited researchers | Access to de-identified research datasets in a secure processing environment **[SS9]** |
| Secondary consumer | Customer and Stakeholder Engagement (VS-10) | Usage and feedback data for needs analysis and impact measurement |
| Assurance | Governance and Compliance (VS-07) | Audit of disclosure control, equal access, and release authorisation |

### 3. Quality gate

The gate for #5 is the release gate. Confidentiality is not negotiable at this boundary. Unlike the earlier gates, the disclosure criteria allow no conditional acceptance: a release that fails them is returned for further protection. **[SS10]**

| Criterion | Check | Typical outcome on failure |
|---|---|---|
| Approved source | The release is based on an approved #4 version | Reject |
| Final disclosure control | Final protection applied and disclosure-risk criteria met for every table, dataset, and dashboard | Reject; apply further protection |
| De-identification | Released microdata meets the de-identification standard for its channel | Reject |
| Documentation | Methodology notes, metadata, and user guidance are complete | Hold until complete |
| Format and accessibility | Each channel format is valid, machine-readable where required, and meets the accessibility standard | Hold until corrected |
| Release authorisation | The release has been signed off | Hold until authorised |
| Timing and equal access | Release time follows the release calendar; embargo arrangements are in place and logged | Hold until the release slot |
| Metadata | Minimum metadata set captured (see attribute 4) | Hold until complete |

### 4. Data and metadata characteristics

**Data.** One released version can have several representations, one per channel: a published table, an SDMX dataset behind an API, a dashboard, or a research dataset. All representations come from the same released version, so a user always gets the same figure through every channel. Permitted operations are final disclosure control, de-identification of microdata, formatting per channel, packaging, and adding documentation. Changing the statistical content is not permitted at #5. A correction to a released figure goes back to #4 as a new approved version and is released again with an erratum. **[SS11]**

**Minimum metadata set** (in addition to the common metadata).

| Metadata element | Description |
|---|---|
| Source reference | The approved #4 version this release is based on |
| Final disclosure control | Method applied, risk assessment outcome, and sign-off |
| De-identification | For microdata: the standard applied and the project or channel it applies to |
| Channels and formats | Every channel used, with format and access conditions |
| Release timestamp | Moment of release and reference to the release calendar |
| Embargo record | Who had pre-release access, when, and under which agreement |
| Documentation | References to methodology notes, reference metadata, and user guidance |
| Accessibility | Accessibility standard met per channel |
| Terms of use | Licence or terms under which the data may be used |
| Correction history | Errata issued and the versions they replace |

In GSIM terms, #5 is the disseminated form of a *Data Set* together with its *Referential Metadata*. SDMX defines the structure in which it is exchanged with users and international organisations.

### 5. Security, privacy, and access

After final disclosure control, most released data is public and has a low confidentiality rating. Its integrity rating is high. Users must be able to trust that a figure on the website or in the API is exactly the figure the NSI released. Channels therefore protect released data against tampering, and the NSI can prove which version was released when.

Before the release moment, the same data is highly restricted. Embargoed copies go only to parties with a formal agreement, such as accredited media, and every pre-release access is logged. No user gets the data before the release time outside that policy.

Research microdata follows a different path. It is released only to accredited researchers and only inside a secure processing environment. Each project gets its own dataset with project-specific pseudonyms, so data cannot be linked across projects. Results leave the environment only after an output check.

### 6. Ownership and governance

| Role | Responsibility for #5 |
|---|---|
| Data owner | Process owner of Dissemination; accountable for confidentiality, equal access, and the quality of the release |
| Release manager | Controls release timing, embargo, and equal access across channels |
| Disclosure control specialist | Applies and signs off the final disclosure control |
| Dissemination and service manager | Manages channels, formats, service levels, and the research access service |
| Data steward | In addition to the common responsibilities: release documentation and errata |
| Data custodian | In addition to the common responsibilities: release channels, integrity protection, and the embargo log |

### 7. Versioning, retention, and lineage

A correction never silently replaces a released figure. It produces a new approved #4 version, a new release version, and a public erratum that explains what changed and why. Earlier releases remain identifiable, so users can see which figure was available at which moment.

Released statistics are usually kept permanently, as part of the public record. National archival legislation often prescribes this. Research datasets are the exception: they are disposed of when the research project closes, together with their project-specific pseudonymisation keys. The approved code and outputs of the project are kept for reproducibility.

Lineage at #5 closes the chain. Each released figure traces back to its approved #4 version, and from there through the analytical versions, #3, and #2 to the authentic delivery in #1. This makes it possible to answer any question about a published figure, from source to release.

### 8. Reuse and handover

Release publishes the *Statistics Released* event and makes the data available through the agreed channels. #5 has no downstream production stream. Its handover is to users outside the NSI, where the data becomes consumed data (#6). Usage and feedback flow back to VS-06 and VS-10, and through them into the design of the whole chain.

Released data is the most widely reused form of NSI output. Under SAF-P08 it is offered as openly as confidentiality allows, in standard formats and with clear terms of use. Open, documented release reduces the number of individual data requests and lets users combine NSI data with other sources.

| Handover element | Content |
|---|---|
| Artefact | Released data version, in its channel-specific representations |
| Required metadata | Minimum metadata set (attribute 4), including documentation, terms of use, and correction history |
| Trigger event | *Statistics Released* |
| Responsibility transfer | The NSI remains responsible for the correctness and documentation of the release and for issuing errata; users are responsible for how they use the data |

### 9. Traceability to the framework

| Framework element | References |
|---|---|
| Capabilities | 1.3.7 Statistical disclosure, 1.5.1 Publication management, 1.5.2 Promotion to use, 1.5.3 Facilitate data access, 1.5.4 Statistical information management, 2.2.4 Data services, 3.4.1 Services management |
| Value-stream stages | VS-06.1 Plan Dissemination and Access Strategy; VS-06.2 Prepare Data for Dissemination; VS-06.3 Publish and Provide Access Services; VS-06.4 Support and Engage Users; VS-06.5 Monitor Usage and Feedback |
| SAF processes | PRD-6.4 Apply disclosure control (final), PRD-7.1 to PRD-7.5 Disseminate, MDS-3 Prepare research datasets, MDS-4 Provide a secure processing environment, MDS-7 Check and release output, MDS-9 Close projects, DSP-2 Publish data offerings, DSP-4 Exchange data under usage control |
| GSBPM | 6.4 Apply disclosure control, 7.1 to 7.5 Disseminate |
| Medallion layer | Gold, published sub-layer |

### 10. Examples and anti-patterns

**Examples**

- *Survey.* The quarterly labour market figures are released at 09:00 on the calendar date, at the same moment on the website, the API, and the dashboard. Two small regional cells are suppressed in the final disclosure check. Accredited media received an embargoed copy and publish at the same moment.
- *Administrative register.* Aggregated business statistics are published as open data. De-identified business microdata is released to accredited researchers inside a secure processing environment, with project-specific pseudonyms and output checking.
- *Web data.* The monthly price index is market-sensitive. It is released at a fixed minute with strict equal access, and the documentation explains the main contributions to the monthly change.

**Anti-patterns**

- Publishing directly from #4 without a recorded final disclosure check. There is no evidence that the release was safe.
- Correcting a published figure silently. Users who already used the old figure cannot see that it changed.
- Giving a ministry or partner early access outside the embargo policy. The NSI's independence and equal access are compromised.
- Releasing figures without methodology notes or accuracy. Users draw conclusions the data cannot support.
- Sending research microdata by email or file transfer to a researcher's own environment. Control over the data is lost.
- Releasing different figures through different channels. Users lose trust when the website and the API disagree.

## Boundary Position #6: Consumed Data

**Description:** Consumed data is released data that users have taken into their own environment and use for their own purposes. Examples are a government departments using an unemployment rate in a policy note, a researcher combining released tables with other sources, a journalist quoting an inflation figure, or an application that pulls a series from the API every day. The NSI has no custody of consumed data and cannot control how it is used, combined, or presented. It can influence correct use only through the quality of its documentation, its terms of use, its user support, and its errata.

**Why it is described:** The SAF describes #6 so that the end of the NSI's responsibility is explicit, just as #0 marks where it begins. Everything the NSI can do for correct use has to be done at #5: documentation, accuracy measures, terms of use, and a clear correction history. What the NSI learns about consumed data comes back as usage and feedback, through VS-06.5 and VS-10. That feedback closes the loop: it shapes new information needs and, through them, the next cycle of the value chain from #0 onward.
<br>
<br>
# Statistical Data Value Chain

## Value Chains Introduction

### Purpose of this chapter

This chapter describes how the statistical value chain works in practice. The Strategy chapter introduced the ten value streams, their stages, and the value they create. The Steady-State Architecture describes the results the chain hands over: the states, their quality gates, and their metadata. This chapter describes the work between those results: the stages, the processes that realise them, the roles that carry them out, and the events that connect them. Every value stream is described with the same structure, so that NSIs can compare them and map their own organisation onto them. **[VC1]**
<br>
### Where to find what

| Question | Answered in |
|---|---|
| Which value streams exist, and what value do they create? | Strategy, *Value Streams* |
| What must data satisfy at each handover point? | Steady-State Architecture, per state |
| How is the work in each value stream organised? | This chapter |
| Which actors, roles, processes, and functions exist? | Business Architecture, reference content |
| How mature is an NSI, and how does it apply a value stream? | SAF Toolkit |

The division of work between states and value streams is deliberate. A state describes the **result**: what the data looks like, which gate it passed, and how it is protected. A value stream describes the **work**: who does what, in which order, and with which controls. Gate criteria and minimum metadata sets are therefore not repeated in this chapter. Each value stream refers to the state it produces.

**Key concepts — if you are new to architecture documents** <br>
This chapter uses a handful of architecture terms. Here is what they mean in plain language; the glossary has the full definitions.

- **Value stream** — a sequence of stages that together create a statistical output. Think of it as a production line: VS-01 to VS-06 each add a specific kind of value to the data.
- **Value stream stage vs. business process** — the stage (`VS-0x.y`) says *what value* is added; the business processes (`PRD`, `DLM`, …) describe *how* the work is done. Attribute 6 of each value stream shows which processes realise each stage.
- **Steady state** — a fixed handover point: a versioned, quality-assured dataset that one stream produces and the next one consumes. There are five numbered states, #1 to #5; data still at the external provider (#0) and data in users' hands (#6) are boundary positions outside the NSI's control.
- **Business service / object / event** — what a value stream offers to others / the data artefacts it works on / the signals streams send each other (e.g. *Raw Data Registered* tells the next stream new data is ready).
- **GSBPM, GAMSO** — the international models of statistical production and of the activities of statistical organisations (see *Relationship with statistical standards* in the Introduction).

### The chain at a glance

Six primary value streams form the production chain. Each one consumes a registered state version and produces the next. They are loosely coupled (SAF-P07): a value stream needs no knowledge of the internal work of its neighbors, only of the state it receives and the state it delivers. The handover is triggered by a registration event. Four supporting value streams run continuously across the whole chain. They set the rules, develop new methods, provide the platforms, and keep the chain connected to its users and data providers.

![Value Stream Context Map](images/value-stream-context-map.png)

| VS | Value stream | Type | State in → out | Event out | Signature discipline or contribution |
|---|---|---|---|---|---|
| VS-01 | Data Acquisition and Ingestion | Primary | #0 → #1 | *Raw Data Registered* | Metadata and validation at ingestion |
| VS-02 | Data Standardization and Integration | Primary | #1 → #2 | *Standardized Data Registered* | No loss of content: map, reformat, annotate |
| VS-03 | Data Editing and Enrichment | Primary | #2 → #3 | *Processed Data Registered* | Full traceability of every value change |
| VS-04 | Estimation, Analysis and Statistical Modeling | Primary | #3 → #4 (analytical) | *Output Data Registered* | Methodological transparency, accuracy, and disclosure control on outputs |
| VS-05 | Statistical Product Composition | Primary | #4 (analytical) → #4 (approved) | *Statistical Product Registered* | Coherence and interpretability; approval before registration |
| VS-06 | Dissemination and Service Delivery | Primary | #4 (approved) → #5 | *Statistics Released* | Accessibility and trust; final disclosure-control gate |
| VS-07 | Governance and Compliance | Supporting | Across the chain | n/a | Frameworks, controls, and assurance; enforces the data principles |
| VS-08 | Innovation and Methodological Development | Supporting | Across the chain | n/a | Validated methods and tools transferred into production |
| VS-09 | Infrastructure and Platform Enablement | Supporting | Across the chain | n/a | Platforms, environments, integration, and continuity |
| VS-10 | Customer and Stakeholder Engagement | Supporting | Across the chain; feedback from #5 and #6 | n/a | Understood needs, service portfolio, relationships, and impact |

Not every statistical product passes through every primary value stream. A macro statistic, for example, often starts from statistics another domain has already registered. Such a product enters the chain downstream and its lineage points to the state it consumed (see *Applying the steady states pragmatically*). Data that comes from outside the NSI always enters through VS-01.

### How the supporting value streams differ

The four supporting value streams are not stages of the production line. They work across the whole chain and enable and constrain all six primary value streams continuously. They differ from the primary value streams in four ways:

- **No state transition.** A supporting value stream does not take data from one state to the next, so it has no registration event and no boundary interfaces of its own. It interacts with the whole chain at once.
- **A continuous cycle.** It runs as a cycle of plan, build, operate, and improve, not per production cycle.
- **An enabling output.** Its output is a capability, not data: governance and assurance (VS-07), validated methods (VS-08), platforms (VS-09), and understood needs and relationships (VS-10).
- **GAMSO instead of GSBPM.** It aligns with the GAMSO activity areas Strategy and Leadership, Capability Management, and Corporate Support, and it foregrounds principles SAF-P02 to SAF-P06.

The diagram shows both directions of the interaction: the supporting value streams provide capabilities to the chain, and the chain sends back evidence, needs, and usage.

```{mermaid}
%%| label: fig-supporting-streams
%%| fig-cap: "The four supporting streams (purple) and the primary chain: each provides a capability to the chain and receives feedback or needs from it."
%%| fig-width: 6
flowchart TB
    subgraph chain["Primary chain (VS-01 → VS-06)"]
        direction LR
        P1["VS-01"] --> P2["VS-02"] --> P3["VS-03"] --> P4["VS-04"] --> P5["VS-05"] --> P6["VS-06"]
    end

    VS07["VS-07 Governance<br/>& Compliance"]:::s -->|"rules, controls,<br/>assurance"| chain
    VS08["VS-08 Innovation &<br/>Methodological Dev."]:::s -->|"validated<br/>methods & tools"| chain
    VS09["VS-09 Infrastructure<br/>& Platform Enablement"]:::s -->|"platforms,<br/>integration, continuity"| chain
    chain -->|"compliance evidence,<br/>improvement needs, usage"| VS07 & VS08 & VS10
    VS10["VS-10 Customer &<br/>Stakeholder Engagement"]:::s -->|"user needs,<br/>communication"| chain

    classDef s fill:#7c3aed,color:#fff,stroke:#6d28d9
```

### The four process types

Every business domain, and therefore every primary value stream, runs the same four process types. **Design** decides how the work is done and delivers metadata: designs, rules, and specifications. **Implementation** builds and tests the solution and delivers the execution process. **Execution** runs the work in each production cycle and delivers the statistical data; the stages of a value stream describe this execution. **Management** monitors the work, assesses quality, and feeds improvements back to design. Design and implementation only run when something changes, execution runs every cycle, and management runs continuously.

The supporting value streams do not follow a production cycle. They run the same pattern as a continuous cycle of plan, build, operate, and improve.

| Process type | Provides | GSBPM phases | Equivalent in supporting streams |
|---|---|---|---|
| Design | Metadata: designs, rules, specifications | 1 Specify Needs, 2 Design | Plan |
| Implementation | The execution process: instruments, components, configured workflows | 3 Build | Build |
| Execution | Statistical data, registered in a state | 4 Collect, 5 Process, 6 Analyse, 7 Disseminate | Operate |
| Management | Quality reports and improvements | 8 Evaluate; overarching quality and metadata management | Improve |

![The Four-Process Governance Pattern](images/four-process-governance-pattern.png)

### How each value stream is described

Each primary value stream is described with the same ten attributes. The supporting value streams use the same attributes, with two differences: attribute 2 describes the relation to the chain instead of a state transition, and attribute 4 follows the cycle of plan, build, operate, and improve.

| # | Attribute | Question it answers |
|---|---|---|
| 1 | Purpose and value created | Why does this value stream exist, and what value does it add? |
| 2 | Position and state transition | Which state does it consume, and which does it produce? |
| 3 | Stages | Which stages create the value, and what happens in each? |
| 4 | The four process types | How is the value stream designed, built, and managed? |
| 5 | Actors and roles | Who is involved, and with which responsibility? |
| 6 | Capabilities, processes, and functions | Which SAF capabilities, processes, and functions realise the stages? |
| 7 | Principles | Which architecture principles weigh most, and how are they applied? |
| 8 | Interfaces, services, and events | What does the value stream offer and exchange, and what triggers it? |
| 9 | Key performance indicators | How is the performance of the value stream measured? |
| 10 | Examples | What does the value stream look like in practice? |

Each value stream has three ArchiMate views: (a) the value stream with its stages and the capabilities that serve them, (b) the stages and the processes and functions that realise them, and (c) the state handover and its events. Maturity checklists and detailed end-to-end scenarios for each value stream are part of the SAF Toolkit. **[VC2]**

Readers can go straight to the attributes that concern them. Operations staff read the stages in attribute 3. Methodologists and statistical designers read the Design processes, system builders the Implementation processes, and quality and compliance managers the Management processes, all in attribute 4. Managers who want the big picture read attributes 1, 2, and 10.

### Standard activities in every value stream {#standard-vs-activities}

Some sub-processes work the same way in every primary value stream. They are described once here. Each value stream lists them in its process tables, marked *(standard)*, with only its own outputs and additions.

**Test and Validate the Pipeline** (Implementation). Before a process goes into production, it is verified in full. Technical testing covers each component, and integration testing checks the end-to-end flow from the input state to registration of the output state. A pilot with real or synthetic data verifies that metadata is captured and propagated, that the quality gate is enforced, and that exceptions are handled as designed. Performance testing confirms that expected volumes fit the agreed time windows. Security testing makes sure the process meets SAF-P10. The sub-process ends with putting the production system into use and documenting the operational procedures.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Test all individual components | Unit test reports | PRD-3.5 Test production systems | |
| Test integration: end-to-end flow from input state to registration | Integration test report | PRD-3.5 Test production systems | |
| Run a pilot with real or synthetic data | Pilot report, validated metadata propagation | PRD-3.6 Test statistical business process | |
| Test performance against expected volumes | Performance test report | PRD-3.5 Test production systems | |
| Test security: penetration testing, access control verification | Security test report | PRD-3.5 Test production systems | SAF-P10; 3.3.2 Security planning |
| Finalise the production system and document operational procedures | Operational procedures manual, production-ready process | PRD-3.7 Finalise production systems | |

**Monitor Process Performance** (Management). The process owner and the quality manager collect the key performance indicators of the value stream (attribute 9) in every cycle. They track paradata: who performed each step, when, how long it took, which tools were used, and which errors occurred. Dashboards give the process owner a current view of the health of the value stream. The approach follows the Quality Management activity of GAMSO.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Collect and aggregate the key performance indicators per cycle | Process performance dashboard | OVA-4 Process Data Management; PRD-8.1 Gather evaluation inputs | GAMSO Quality Management |
| Track paradata: operator, timing, tools, errors | Paradata records | OVA-4 Process Data Management | |
| Produce process performance dashboards | Dashboard for the process owner | OVA-4 Process Data Management | |

**Audit and Compliance Reporting** (Management). This sub-process produces the evidence that the value stream operates within legal, regulatory, and organisational requirements: audit trail reports that trace every artefact from its input state to its output state, data protection reporting, and security compliance reporting, including breaches and incidents. The reports meet the obligation of capability 4.1.5 *Accountability* and feed VS-07.5 *Audit, Certify and Report Compliance*.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Produce audit trail reports: full traceability from input to output state | Audit trail summary | OVA-4 Process Data Management; DLM-8 Monitor data quality, lineage and use | 4.1.5 Accountability |
| Report on data protection compliance | Data protection compliance report | OVA-1 Quality Management | SAF-P11; 3.3.1 Privacy management |
| Report on security compliance: measures applied, breaches, incidents | Security compliance report (per cycle) | OVA-1 Quality Management | SAF-P10; 3.3.3 Security incident management |

**Continuous Improvement** (Management). This sub-process closes the governance cycle. It analyses quality and performance trends across cycles, identifies improvement opportunities, prioritises them by impact and feasibility, and feeds them back to Design. Where a new method, source, or tool is needed, the recommendation goes to VS-08. This is capability 4.1.4 *Improvement management* in practice, and connects to the GAMSO idea of transferring mature results of innovation to production.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Analyse quality and performance trends across cycles | Improvement recommendations report | PRD-8.2 Conduct evaluation | 4.1.4 Improvement management |
| Identify improvement opportunities | Updated design inputs | PRD-8.2 Conduct evaluation | 4.1.4 Improvement management |
| Prioritise improvements by impact and feasibility | Improvement tracking log | PRD-8.3 Agree an action plan | GAMSO Capability Management |
| Feed recommendations back to Design or to VS-08, and track their implementation | Design feedback (closing the cycle) | PRD-8.3 Agree an action plan | 4.1.4 Improvement management |

**Paradata.** Every process type records how it ran, in addition to the data metadata listed per value stream.

| Process type | Process metadata (paradata) produced |
|---|---|
| Design | Log of design decisions, methodology version, review and approval records |
| Implementation | Build log, test results, records of configuration changes, deployment approvals |
| Execution | Operator identity, timing, volumes, errors, tool and rule versions applied |
| Management | Dashboards of key performance indicators, quality trend analyses, improvement decisions, audit findings |

**Boundary interfaces.** Each primary value stream is loosely coupled (SAF-P07) to its neighbors through boundary interfaces. Each interface exchanges a registered, immutable artefact and its metadata, never internal working data, so neither side needs knowledge of the other's internal processing. Attribute 8 of each value stream specifies its boundaries: the artefact handed over, the metadata it must carry, the triggering event, and the point where responsibility transfers.

### Identifiers used in this chapter

| Identifier | Refers to | Defined in |
|---|---|---|
| VS-01 to VS-10, VS-01.1, … | Value streams and their stages | Strategy, *Value Streams* |
| 1.2.1, 2.1.2, … | Capabilities | Strategy, *Capability Model* |
| ACT, ROL, COL | Business actors, roles, and collaborations | Business Architecture |
| PRD, OVA, DLM, MDS, DSP | Business processes | Business Architecture, *Business Processes* |
| FUN | Business functions | Business Architecture, *Business Functions* |
| #0 to #6 | Steady states and boundary positions | Steady-State Architecture |
| SAF-P01 to SAF-P11 | Architecture principles | Motivation, *Architecture Principles* |

### Steady States of Data

The states that the value streams consume and produce are defined in the Steady-State Architecture: their quality gates, minimum metadata, the rules common to all states, and when a state may be shared or skipped (see [Applying the steady states pragmatically](#pragmatic-steady-states)). This chapter does not repeat them.

## Principles to Apply
The SAF defines eleven architecture principles, labeled SAF-P01 to SAF-P11. The six **primary** streams actively apply six of them (marked ★ below); the four **supporting** streams foreground the other five (marked †). The table shows practical guidance on how to apply each principle; the statements, rationale and implications are in *Architecture Principles* (Motivation); VS-07 in particular **enforces** the data principles (P09/P10/P11) across the whole chain.

| Principle | Name | How to apply across the value chain |
|---|---|---|
| **SAF-P01** ★ | Open-source participation | Build statistical capabilities on shared, open tooling; contribute back, so NSIs keep collective control of critical methods rather than depending on vendors. |
| **SAF-P07** ★ | Loose coupling | Exchange data only at steady-state interfaces; each stream consumes one state and produces the next without knowing the others' internals. |
| **SAF-P08** ★ | Data is shared property | Once an artefact is registered at a steady state, make it available to all authorised consumers; avoid duplicating collection, processing, or analysis. |
| **SAF-P09** ★ | No data without metadata and classification | Every artefact carries provenance (origin), methodology, accuracy, classification, and lineage (the trace back to its inputs) — captured at the point each value is created or changed. |
| **SAF-P10** ★ | Security by design | Embed access control, integrity verification, and tamper-evident audit trails in every pipeline from the start. |
| **SAF-P11** ★ | Privacy by design | Remove/pseudonymise identifiers during standardisation; assess disclosure risk on enrichment and apply statistical disclosure control before release. |
| **SAF-P02** † | Active support | Operate and support capabilities as living services, not one-off builds (VS-09 platforms, VS-10 services). |
| **SAF-P03** † | Active life cycle management | Version and govern rules, methods, models, and products across their life cycle; retire what is obsolete (VS-07, VS-08). |
| **SAF-P04** † | Maximise the benefits for the organisation | Prefer solutions that serve the whole organisation and real user value over local optimisations (VS-10, VS-07). |
| **SAF-P05** † | IT and technology is everyone's business | Treat methodology, data, and technology as a shared responsibility across business and IT (VS-08, VS-09). |
| **SAF-P06** † | Business continuity | Keep the chain running reliably and able to recover from disruption (VS-09). |
: SAF Principles {tbl-colwidths="[12,28,60]"}

★ = actively applied by the six primary value streams. † = foregrounded by the four supporting value streams (VS-07–VS-10).

**Metadata everywhere (SAF-P09):** <br>
value is only added once its context is captured — what was done, by which rule/method, with what accuracy, and traceable to its inputs.

**Confidentiality progressively applied (SAF-P11):** <br>
identifiers are removed/pseudonymised at standardisation (#2) at the latest, or earlier where that suits the process; disclosure risk is assessed on enrichment (#3), disclosure control is applied to outputs (#4), and a final disclosure check gates release (#5).

## VS-01 Data Acquisition and Ingestion

### 1. Purpose and value created

VS-01 is the entry point of the statistical value chain. It brings data from outside the NSI under NSI custody: survey responses, administrative registers, exchanges in data spaces, and new sources such as web or sensor data. It does not change the content of the data. It makes sure the data is obtained lawfully, received securely, checked for integrity, and registered with its provenance. The value created is **trust and readiness**: trust that the data was acquired correctly, and readiness for use in the rest of the chain. Everything downstream depends on this. If the acquisition of a source cannot be traced, no statistic built on it can be fully defended.

VS-01 corresponds to the business domain **Observation/Collection** (see *Steady-State Architecture, Business domains*). This section describes the business layer of that domain for all four process types: Design, Implementation, Execution, and Management.

|**PLACEHOLDER: ArchiMate view VS-01 (a) value stream and capabilities**|
|---|

<br>

### 2. Position and state transition

VS-01 is the first primary value stream. All data from outside the NSI enters the statistical system through it, before any downstream processing takes place.

VS-01 takes data from boundary position #0 to State #1. Before VS-01, the data is held by a provider or respondent, outside the NSI's control. After VS-01, it is a registered, immutable version of raw data, in NSI custody, in its original form, with provenance metadata recorded and basic quality verification completed. The quality gate, the minimum metadata set, and the protection of State #1 are described in *State #1: Raw Data* and are not repeated here. **[VC10]** VS-01 is the only entrance for data from outside the NSI: there is no side door into the chain. A product that starts from data already registered by another domain does not pass VS-01; it enters the chain downstream.

| From | To | Gate | Event out |
|---|---|---|---|
| #0 Source Data | #1 Raw Data | Gate of State #1 (legal basis, authenticity, integrity, security, structure, completeness, timeliness, metadata) | *Raw Data Registered* |

|**PLACEHOLDER: ArchiMate view VS-01 (c) state handover and events: Source Data (#0) outside the NSI boundary, the ingestion service at the boundary (metadata addition, quality and schema check), Raw Data (#1) inside the NSI**|
|---|

<br>

### 3. Stages

The stages describe the value that VS-01 adds in every production cycle. Together they form the execution process type of VS-01. In a mature steady state, most of the work has been designed and built in advance (see attribute 4). Execution then focuses on running the cycle, capturing data and metadata, and making sure the quality gate is passed.

| Stage | Name | Value added |
|---|---|---|
| VS-01.1 | Identify Data Needs and Sources | The information need is clear, and suitable sources are known |
| VS-01.2 | Establish Data Agreements and Access Rights | Data can be obtained lawfully, under agreed conditions |
| VS-01.3 | Collect or Receive Data | Data and its metadata are in NSI custody |
| VS-01.4 | Validate and Log Data Intake | The delivery is complete, intact, and traceable |
| VS-01.5 | Store and Register Raw Data Artefacts | Raw data is registered and available for reuse (State #1) |

Each stage below is described with its activities. The column *SAF process* shows the business process from *Business Processes* that the activity belongs to. The column *Other reference* shows the principles, capabilities, or external frameworks that the activity applies. **[VC9]**

<br>

#### VS-01.1 Identify Data Needs and Sources

**Value created:** *Clear understanding of what data is needed and where it can be obtained.*

This stage starts from the information need set in the design of the statistical product. In a mature steady state, the Design process *Design Data Requirements and Source Strategy* has already defined the data requirements and the source strategy. Execution in each cycle therefore focuses on confirmation rather than re-creation. The team confirms or updates the data requirements for the current production cycle. It verifies that the identified sources remain available and accessible, and checks that source metadata is current: contact persons, data formats, and delivery schedules. Before any new collection, it checks whether the data already exists as a registered state version, in line with SAF-P08. It also identifies new sources that may have become available since the last cycle. A significant change in requirements or source availability goes back to design instead of being solved during the cycle.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Confirm or update data requirements for this production cycle | Confirmed requirements for the cycle | PRD-1.1 Identify needs | |
| Check whether the data already exists as a registered state version | Reuse decision | PRD-1.5 Check data availability and suitability | SAF-P08 |
| Verify data source availability and accessibility | Source availability confirmation | PRD-1.5 Check data availability and suitability | |
| Check that source metadata is current (contacts, formats, schedules) | Updated source metadata | PRD-1.5 Check data availability and suitability; OVA-6 Data Supplier Management | |
| Identify new sources available since the last cycle | New source assessment (if any) | PRD-1.5 Check data availability and suitability | |

<br>

#### VS-01.2 Establish Data Agreements and Access Rights

**Value created:** *Legal, ethical, and transparent access to data under controlled conditions.*

Before data flows, legal and operational access must be confirmed for the current production cycle. For each source, the legal basis is established: a statutory obligation, a data provision agreement, or a usage policy in a data space. The team activates or renews data sharing agreements. It verifies compliance with data protection law for the current data scope, for example by checking that the records of processing activities (GDPR Article 30) are up to date. It confirms that access credentials and security certificates are valid and have not expired. For sources that are new in this cycle, the full agreement process is carried out. The active agreement status is recorded and linked to the upcoming deliveries. This creates a traceable chain from legal authorisation to received data, so the legal basis of each version can be shown in an audit.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Activate or renew data sharing agreements for the current cycle | Active agreement record (per source) | OVA-6 Data Supplier Management; DSP-3 Agree data use conditions | 3.4.3 Service agreement |
| Verify data protection compliance: records of processing up to date | Compliance confirmation log | DLM-4 Classify and protect data | SAF-P11 |
| Confirm that access credentials and security certificates are valid | Verified access credentials | PRD-4.2 Set up collection | SAF-P10 |
| For new sources: carry out the full agreement process | New source agreement | OVA-6 Data Supplier Management; DSP-1 Join a data space; DSP-3 Agree data use conditions | SAF-P11 |
| Record the active agreement status, linked to upcoming deliveries | Agreement-delivery link | PRD-4.2 Set up collection | |

<br>

#### VS-01.3 Collect or Receive Data

**Value created:** *Secure and verifiable transfer of authentic data into the organisation.*

This stage is the operational heart of the value stream, where data physically enters NSI custody. Primary data collection runs surveys through the designed and built instruments. Web questionnaires (CAWI) open, invitation links are sent, and response rates are monitored. Field interviewers (CAPI) are deployed with managed assignments, and telephone interview schedules (CATI) are carried out with callback management. Non-response is followed up within the agreed strategy. Secondary data collection receives administrative data through agreed channels. Secure file transfer (SFTP) accepts scheduled deliveries, APIs pull data on agreed schedules, and data space connectors support federated exchange. Emerging sources, such as web scraping, sensor data, and commercial feeds, are extracted according to their specification.

Equally critical is the metadata captured at the moment of receipt. For every dataset received, the ingestion process records the fields in the table below. This obligation follows from SAF-P09. It makes sure that no data enters the NSI without the context needed to understand its provenance and quality. At the end of this stage, the data is held by the NSI, but it has not yet been accepted.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Create the frame and select the sample for this cycle (surveys) | Frame and sample | PRD-4.1 Create frame and select sample | 1.2.1 Primary data collection |
| Prepare instruments, field staff, and channels; plan the collection period | Collection ready to start | PRD-4.2 Set up collection | |
| Run survey collection and follow up non-response | Survey responses, paradata | PRD-4.3 Run collection | 1.2.1 Primary data collection |
| Receive administrative data and data space deliveries through agreed channels | Received deliveries | PRD-4.3 Run collection; DSP-4 Exchange data under usage control | 1.2.2 Secondary data collection |
| Extract data from emerging sources according to specification | Extracted data | PRD-4.3 Run collection | |
| Capture ingestion metadata and paradata at the point of receipt | Ingestion metadata record | PRD-4.3 Run collection; OVA-4 Process Data Management | SAF-P09 |

| Ingestion metadata field | Description |
|---|---|
| Source identifier and organisation | Who provided the data |
| Timestamp of receipt | When it was received |
| Transfer method and channel | How it was delivered (SFTP, API, CAWI, and so on) |
| File hash (SHA-256) and format | Integrity verification and format record |
| Volume (record count, file size) | Scale of the delivery |
| Agreement reference | Legal basis for the data |
| Collection mode and instrument version | Survey-specific provenance |

<br>

|**PLACEHOLDER: VS-01 collection channel architecture: survey, administrative, and emerging-source channels arriving at one ingestion point, each adding its own metadata (source, timestamp, transfer method, file hash, volume, agreement reference), followed by VS-01.4**|
|---|

<br>

#### VS-01.4 Validate and Log Data Intake

**Value created:** *Confidence that received data is complete, structured, and fully traceable.*

Once data has been received, it must pass the quality gate of State #1 before it can be accepted. The validation checks completeness: expected record counts are present, required fields are populated, and the delivery matches the service level agreement. It checks structure and format against the raw data schema from *Design Data Model and Metadata Schema*. It checks security and integrity: virus scan, checksum verification (SHA-256), and digital signature validation, in line with SAF-P10. A quality assessment is carried out against the criteria from *Design Validation Rules and Quality Criteria*, producing a completeness rate, a timeliness score, and a conformance rating.

Every validation result, exception, and decision is logged in an audit trail. The trail captures data metadata (what was validated, what passed, what failed) and process metadata (who validated, when, which rules were applied, which tool version). The outcome is one of two business events. *Data Intake Validated* starts storage and registration. *Data Intake Rejected* starts exception handling according to the designed rules: notify the provider through the relationship manager, queue the delivery for manual review, or accept it conditionally with a quality flag.

No content is edited in this stage: only technical and structural validation is done. Content editing, such as correction, imputation, and harmonisation, belongs to VS-03 Data Editing and Enrichment.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Verify completeness: record counts, required fields, conformance with the service level agreement | Completeness assessment | PRD-4.4 Finalise collection | |
| Validate structure and format against the raw data schema | Structural validation result | PRD-4.4 Finalise collection; DLM-2 Promote data through a quality gate | |
| Perform security and integrity checks: virus scan, checksum, signature | Security verification result | PRD-4.4 Finalise collection | SAF-P10 |
| Carry out the quality assessment against the designed criteria | Quality assessment scores | DLM-2 Promote data through a quality gate | |
| Create the audit trail: log all validation results, exceptions, and decisions | Audit trail record | OVA-4 Process Data Management | GAMSO Quality Management |

<br>


#### VS-01.5 Store and Register Raw Data Artefacts

**Value created:** *Secure, organised, and traceable storage of raw data.*

This stage persists validated data and makes it findable for the rest of the statistical system. Each dataset version receives a unique persistent identifier (URI or UUID). It is stored in the raw data repository in its original format, in line with the loose coupling of SAF-P07. Its metadata is registered in the data catalogue, in line with SAF-P09. Each dataset is linked to its provenance record (source, method, timing), its quality assessment from VS-01.4, the governing data sharing agreement, and the classification and coding schemes it uses. Lineage from Source Data (#0) to Raw Data (#1) is recorded. Access permissions are applied according to the access control and privacy design and the decisions of the data owner. A redelivery or correction by the provider always creates a new version; it never overwrites an earlier one. The stage ends by publishing the *Raw Data Registered* event, which tells VS-02 that new raw data is available for standardisation.

**Output:** **Raw Data (State #1)**, the official handover artefact to the rest of the statistical value chain. Its structure and minimum metadata set are described in *State #1: Raw Data*. **[VC10]**

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Assign a unique persistent identifier (URI or UUID) to the dataset version | Dataset ID | DLM-3 Register and catalogue data | |
| Store the data in the raw data repository in its original format | Stored raw data artefact | DLM-5 Store and version data | SAF-P07 |
| Register metadata in the data catalogue: provenance, quality, agreement, classification, lineage | Catalogue registration | DLM-3 Register and catalogue data; OVA-2 Metadata Management | SAF-P09 |
| Apply access permissions according to the designed framework | Access-controlled dataset | DLM-4 Classify and protect data | SAF-P10, SAF-P11 |
| Publish the *Raw Data Registered* event to notify VS-02 | Event notification | DLM-3 Register and catalogue data | SAF-P07 |

### 4. The four process types

The sub-processes below are specific to VS-01. Each refines one or more SAF business processes, listed as *Refines*, which keeps it traceable to *Business Processes*. Sub-processes marked *(standard)* work as described in [Standard activities in every value stream](#standard-vs-activities); only the VS-01 specifics are listed.

#### Design: provides metadata

| Design sub-process | Refines | Main outputs |
|---|---|---|
| Design Data Requirements and Source Strategy | PRD-1.1 Identify needs; PRD-1.2 Consult and confirm needs; PRD-1.3 Establish output objectives; PRD-1.5 Check data availability and suitability; PRD-1.6 Prepare and submit business case; PRD-2.3 Design collection | Data requirements specification, source assessment, collection strategy |
| Design Collection Methodology and Instruments | PRD-2.2 Design variables; PRD-2.3 Design collection; PRD-2.4 Design frame and sample | Collection methodology, questionnaire design, sample design, communication plan |
| Design Data Model and Metadata Schema | PRD-2.2 Design variables; DLM-1 Plan and design data assets; OVA-2 Metadata Management | Raw data schema, ingestion metadata model, catalogue template |
| Design Validation Rules and Quality Criteria | PRD-2.5 Design processing and analysis; DLM-2 Promote data through a quality gate; OVA-1 Quality Management | Validation rule set, quality criteria, exception handling policy |
| Design Access Control and Privacy Framework | DLM-1 Plan and design data assets; DLM-4 Classify and protect data | Data classification, access control design, privacy impact assessment |

##### Design Data Requirements and Source Strategy

*Refines:* PRD-1.1 Identify needs; PRD-1.2 Consult and confirm needs; PRD-1.3 Establish output objectives; PRD-1.5 Check data availability and suitability; PRD-1.6 Prepare and submit business case; PRD-2.3 Design collection.

The starting point of any data acquisition effort is understanding what data is needed and where it can be obtained. This sub-process translates statistical objectives into a concrete source strategy: target populations, required variables, reference periods, and quality expectations. The team inventories and evaluates potential sources across the full spectrum: surveys, administrative registers, APIs, web sources, sensors, data spaces, and commercial data. Each source is assessed for relevance, quality, accessibility, cost, timeliness, and legal availability. Reuse of existing data comes before new collection, in line with SAF-P08. The outcome is a decision on the collection approach: primary collection (run a survey), secondary collection (reuse administrative data), or a combination of sources. The trade-offs behind that decision are documented.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define statistical needs: target population, variables, reference period, quality expectations | Data requirements specification | PRD-1.1 Identify needs; PRD-1.2 Consult and confirm needs; PRD-1.3 Establish output objectives | 1.1.1 Needs inventory |
| Inventory and evaluate potential data sources of all types | Source assessment report | PRD-1.5 Check data availability and suitability | SAF-P08 |
| Assess each source for relevance, quality, accessibility, cost, timeliness, legal availability | Source assessment report | PRD-1.5 Check data availability and suitability | |
| Decide the collection strategy: primary, secondary, or multi-source | Collection strategy decision record | PRD-2.3 Design collection | |
| Document the trade-offs between source options | Collection strategy decision record; business case | PRD-1.6 Prepare and submit business case | |

##### Design Collection Methodology and Instruments

*Refines:* PRD-2.2 Design variables; PRD-2.3 Design collection; PRD-2.4 Design frame and sample.

Once the source strategy is set, the methodology team designs how data will actually be collected. This involves selecting collection modes and defining how each mode works within the overall design. Examples are web, face-to-face, or telephone interviewing (CAWI, CAPI, CATI), secure file transfer (SFTP), automated machine-to-machine interfaces (API), data space connectors, and web scraping. For survey-based collection, the design includes the questionnaire: variable definitions, question wording, skip logic, and code lists. The sampling frame and sample selection method are designed to make the sample statistically representative. Where several modes are used, the team specifies which respondents receive which mode and the fallback sequence for non-response. A respondent communication strategy completes the design: invitation letters, reminders, and help desk scripts. Respondent burden is kept as low as possible.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Design collection modes (CAWI, CAPI, CATI, SFTP, API, data space connector, web scraping) | Collection methodology document | PRD-2.3 Design collection | 1.2.1 Primary data collection; 1.2.2 Secondary data collection |
| Design questionnaire content: variable definitions, question wording, skip logic, code lists | Questionnaire design (per mode) | PRD-2.2 Design variables; PRD-2.3 Design collection | |
| Design the sampling frame and sample selection method | Sample design and selection criteria | PRD-2.4 Design frame and sample | |
| Define the multi-mode strategy and fallback sequences | Collection methodology document | PRD-2.3 Design collection | |
| Design the respondent communication strategy | Respondent communication plan | PRD-2.3 Design collection | 3.4.2 Contact management |

##### Design Data Model and Metadata Schema

*Refines:* PRD-2.2 Design variables; DLM-1 Plan and design data assets; DLM-9 Manage reference and master data; OVA-2 Metadata Management.

This sub-process defines the target data structure of Raw Data (State #1) and the metadata that must accompany every dataset at the point of ingestion. The data model specifies fields, types, formats, and constraints for the storage area where incoming data first lands, the landing zone. Equally important is the ingestion metadata model. It prescribes what must be captured at each point of receipt: provenance (source organisation, contact, agreement reference), method (collection mode, instrument version, sampling parameters), timing (collection period, delivery and processing timestamps), and quality indicators (completeness rate, delivery timeliness, format conformance). Classification and coding schemes are defined, consistent with national and international standards. Finally, the structure of the metadata catalogue is designed so that datasets are findable, linked, and traceable. This makes active metadata a foundation for automation downstream, as emphasised by the Metadata Management capability of CSDA (Common Statistical Data Architecture).

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define the target data structure of Raw Data (State #1): fields, types, formats, constraints | Raw data schema definition | PRD-2.2 Design variables; DLM-1 Plan and design data assets | |
| Define the ingestion metadata model: provenance, method, timing, quality indicators | Ingestion metadata model | OVA-2 Metadata Management | SAF-P09 |
| Define classification and coding schemes | Classification mapping rules | DLM-9 Manage reference and master data | SAF-P09 |
| Design the metadata catalogue structure for registration and discovery | Catalogue registration template | DLM-1 Plan and design data assets; OVA-2 Metadata Management | CSDA Metadata Management |

##### Design Validation Rules and Quality Criteria

*Refines:* PRD-2.5 Design processing and analysis; DLM-2 Promote data through a quality gate; OVA-1 Quality Management; OVA-6 Data Supplier Management.

Before any data enters the NSI, the acceptance criteria and the rules for handling exceptions must be clear. This sub-process sets completeness thresholds, such as minimum record counts and required field coverage. It sets the parameters of service level agreements: delivery windows, response times, and format specifications. It defines structural validation rules: field types, value ranges, referential integrity, and format conformance. Security and integrity checks are specified in line with SAF-P10: virus scan requirements, checksum algorithms, and encryption standards. The quality dimensions to track are agreed: completeness, timeliness, conformance, and integrity. Exception handling rules distinguish between rejection, conditional acceptance with quality flags, and routing to manual review. Together, these rules make up the VS-01 part of the quality gate of State #1. The Quality Management capability of GAMSO provides the overall control framework.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define completeness thresholds and service level parameters | Quality criteria document, service level template | PRD-2.5 Design processing and analysis; OVA-6 Data Supplier Management | 3.4.3 Service agreement |
| Define structural validation rules: field types, value ranges, referential integrity | Validation rule set | PRD-2.5 Design processing and analysis | |
| Define security and integrity check specifications | Validation rule set | PRD-2.5 Design processing and analysis | SAF-P10 |
| Define the quality dimensions to track | Quality criteria document | OVA-1 Quality Management | GAMSO Quality Management |
| Design exception handling rules: rejection, conditional acceptance, manual review | Exception handling policy | DLM-2 Promote data through a quality gate | |

##### Design Access Control and Privacy Framework

*Refines:* DLM-1 Plan and design data assets; DLM-4 Classify and protect data; OVA-4 Process Data Management.

This last design sub-process makes sure that security and privacy are built in from the start, not added afterwards. Each data source receives a classification for availability, integrity, and confidentiality, in line with SAF-P09. Role-based access controls for the raw data repository are designed in line with SAF-P10: who can read, write, and administer. Privacy protection follows SAF-P11. It covers the moment of pseudonymisation (when direct identifiers are removed or replaced), purpose limitation (which uses each agreement allows), the legal basis for processing (for example, which ground of GDPR Article 6 applies to each source), and data minimisation (only necessary data is collected). Audit logging requirements, which define the access events that must be recorded, complete the design.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define the data classification (availability, integrity, confidentiality) per source | Data classification policy | DLM-4 Classify and protect data | SAF-P09 |
| Design role-based access control for the raw data repository | Access control design | DLM-1 Plan and design data assets; DLM-4 Classify and protect data | SAF-P10; 3.3.4 Logical identity and access control |
| Design privacy protection: moment of pseudonymisation, purpose limitation, legal basis, data minimisation | Privacy impact assessment | DLM-4 Classify and protect data | SAF-P11; 3.3.1 Privacy management |
| Design audit logging requirements | Audit logging specification | OVA-4 Process Data Management | SAF-P10 |

|**PLACEHOLDER: VS-01 design process decomposition: inputs (statistical needs, data sources, framework standards, legal and privacy requirements), the five design sub-processes in order, and the design document each produces, which together govern Implementation, Execution, and Management**|
|---|

#### Implementation: provides the execution process

| Implementation sub-process | Refines | Main outputs |
|---|---|---|
| Build Collection Instruments and Channels | PRD-3.1 Reuse or build collection instruments; DSP-1 Join a data space | Production-ready instruments and channels |
| Configure Data Ingestion Workflows | PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows | Automated validation, metadata capture, exception routing, events |
| Build Metadata Registration and Cataloguing | PRD-3.4 Configure workflows; DLM-3 Register and catalogue data; OVA-2 Metadata Management | Catalogue, automated metadata propagation, discovery |
| Test and Validate the Pipeline *(standard)* | PRD-3.5 Test production systems; PRD-3.6 Test statistical business process; PRD-3.7 Finalise production systems | Test reports; field test with actual data providers; penetration test of transfer channels; volumes tested against the agreed delivery windows |

##### Build Collection Instruments and Channels

*Refines:* PRD-3.1 Reuse or build collection instruments; DSP-1 Join a data space.

This sub-process turns the collection methodology into operational tools and channels. For survey-based collection, it builds or configures the instruments. A CAWI portal gets the designed question logic, support for several languages, and a layout that works on any device. A CAPI application gets offline capability and the designed questionnaire. CATI scripts get the designed routing logic. Paper forms are laid out for automated scanning (OCR) or manual data entry. For secondary and emerging sources, the receiving channels are configured. SFTP endpoints get the designed encryption and authentication, API connections get rate limiting and error handling, and data space connectors are set up according to their specifications. Secure transfer channels with end-to-end encryption are set up in line with SAF-P10. A respondent management system handles invitations, reminders, and tracking.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Build or configure survey instruments per mode (CAWI, CAPI, CATI, paper) | Production-ready instruments | PRD-3.1 Reuse or build collection instruments | 1.1.3 Build statistics product |
| Configure data receipt channels (SFTP, API, data space connectors) | Configured channel endpoints | PRD-3.1 Reuse or build collection instruments; DSP-1 Join a data space | |
| Set up secure transfer channels with end-to-end encryption | Secure channel configuration | PRD-3.1 Reuse or build collection instruments | SAF-P10 |
| Configure the respondent management system (invitations, reminders, tracking) | Respondent management system | PRD-3.1 Reuse or build collection instruments | 3.4.2 Contact management |

##### Configure Data Ingestion Workflows

*Refines:* PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows; DLM-2 Promote data through a quality gate.

This sub-process translates the designed validation rules and metadata capture requirements into automated workflows. Structural validation is implemented first: schema conformance, field types, and required fields. Alongside it come integrity checks (checksum verification, virus scanning, digital signature validation), completeness checks (record counts, field coverage thresholds), and service level checks (delivery timeliness, format conformance). Metadata capture at each ingestion point is automated, so that provenance, format, timestamps, and file hashes are extracted without manual work. The landing zone for raw data is set up with the designed access controls and storage policies. Event notifications are configured, so that VS-02 is alerted when raw data is registered. Exception handling workflows route rejected data to the right queue: provider notification, manual review, or conditional acceptance.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Implement validation rules as automated checks (structural, integrity, completeness, service level) | Automated validation pipeline | PRD-3.2 Reuse or build processing and analysis components | |
| Configure metadata capture at each ingestion point | Automated metadata extraction | PRD-3.4 Configure workflows | SAF-P09 |
| Set up the raw data landing zone with access controls and storage policies | Configured repository | PRD-3.4 Configure workflows; DLM-4 Classify and protect data | |
| Configure event notifications for downstream consumers | Publication of the *Raw Data Registered* event | PRD-3.4 Configure workflows | SAF-P07 |
| Configure exception handling workflows | Rejection routing and manual review queues | PRD-3.4 Configure workflows; DLM-2 Promote data through a quality gate | |

##### Build Metadata Registration and Cataloguing

*Refines:* PRD-3.4 Configure workflows; DLM-3 Register and catalogue data; DLM-6 Provide data for reuse; OVA-2 Metadata Management.

This sub-process implements the metadata catalogue and the automated registration that make every dataset findable and traceable. Catalogue entries are built from the metadata model of *Design Data Model and Metadata Schema*. Metadata is propagated automatically into the catalogue from three sources: the collection instruments (variables, code lists, question wording), the transfer channels (source, method, timing), and the validation workflow (validation results, completeness scores). Metadata quality validation makes sure that every registered dataset has all required metadata fields. Search and discovery functions let downstream consumers find raw data and its metadata. As CSDA emphasises, the ultimate goal is active metadata: metadata that can generate collection instruments, validation rules, and processing specifications automatically.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Implement catalogue entries based on the designed metadata model | Populated metadata catalogue | DLM-3 Register and catalogue data; OVA-2 Metadata Management | |
| Configure automatic metadata propagation from instruments, channels, and validation | Automated metadata pipelines | PRD-3.4 Configure workflows | CSDA Metadata Management |
| Set up metadata quality validation | Metadata completeness checks | OVA-2 Metadata Management | SAF-P09 |
| Implement metadata search and discovery for downstream consumers | Discovery interface | DLM-6 Provide data for reuse | CSDA Metadata Management |

|**PLACEHOLDER: VS-01 implementation pipeline: the five design artefacts feeding the three build sub-processes, followed by technical testing, field test, and security and performance testing, resulting in a production-ready acquisition process and operational procedures**|
|---|

#### Execution: provides the statistical data

Execution runs the stages of VS-01 in every production cycle. The stages and their activities are described in attribute 3. A cycle starts when a collection period opens or when a provider's delivery arrives. The stages then run in order, but for continuous sources, such as daily web data, VS-01.3 to VS-01.5 repeat for every delivery. Execution applies the designs and the solution as they are; anything that needs a new rule or a new channel goes back to Design. Every delivery ends in one of three outcomes: registered, registered with quality flags, or returned to the provider.

| Aspect | VS-01 |
|---|---|
| Trigger | *Collection period opened*; *Delivery received* |
| Cadence | Per survey cycle; per delivery for administrative and web data |
| Performed by | ROL-13 Data collection manager, ROL-14 Data quality analyst, ROL-03 Data steward |
| Input | Source data (#0), active agreements, production-ready instruments |
| Output | Registered raw data version (#1) and its intake log |
| Control point | Gate of State #1 in VS-01.4 |
| Exception path | Rejection to the provider via ROL-23 Relationship manager; structural change at the source back to Design |

#### Management: provides quality reports

| Management sub-process | Refines | Main outputs |
|---|---|---|
| Monitor Process Performance *(standard)* | OVA-4 Process Data Management; OVA-6 Data Supplier Management; PRD-8.1 Gather evaluation inputs | Process performance dashboard; service level compliance report for all data providers (OVA-6, 3.4.3 Service agreement) |
| Assess Data Quality | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use | Data quality report, quality scorecards, trend analysis |
| Manage Metadata Lifecycle | OVA-2 Metadata Management; DLM-8 Monitor data quality, lineage and use | Metadata quality report, catalogue maintenance log, lineage audit |
| Audit and Compliance Reporting *(standard)* | OVA-1 Quality Management; OVA-4 Process Data Management; DLM-8 Monitor data quality, lineage and use | Audit trail from the external source to the raw data repository; records of processing activities (GDPR Article 30), reviews of data protection impact assessments for high-risk processing, reporting on data subject rights, and the ability to show which data the NSI holds and why; agreement compliance report confirming that all use stays within the agreements |
| Continuous Improvement *(standard)* | PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan | Improvement recommendations, for example new sources that replace sources of lower quality, modes that reduce burden or raise response, automation of manual ingestion steps, and validation rules that produce fewer false alarms; trends watched: rejection rate, metadata completeness, processing time **[VC11]** |

##### Assess Data Quality

*Refines:* OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use.

Beyond process performance, the quality of the ingested data itself is evaluated against the criteria set in *Design Validation Rules and Quality Criteria*. Each dataset is assessed on several quality dimensions. Completeness covers record counts against expectations and field coverage. Timeliness compares the delivery date with the agreed deadline. Structural accuracy covers format conformance and valid value ranges. Consistency covers consistency between fields and with earlier deliveries. Conformance covers alignment with the designed schema and classification schemes. Quality indicators are produced per dataset, per source, and per production cycle. Quality trends are tracked to detect declining sources or modes with consistently lower quality. This follows the Data Quality capability of CSDA and SAF capability 2.1.3 *Statistical quality management*.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Evaluate the quality dimensions per dataset: completeness, timeliness, accuracy, consistency, conformance | Data quality report (per cycle) | OVA-1 Quality Management | CSDA Data Quality |
| Compare the results with the designed quality criteria | Quality assessment against baseline | OVA-1 Quality Management | 2.1.3 Statistical quality management |
| Produce quality indicators per dataset, per source, per cycle | Quality scorecards (per source, per mode) | DLM-8 Monitor data quality, lineage and use | CSDA Data Quality |
| Identify quality trends across sources and modes | Quality trend analysis | DLM-8 Monitor data quality, lineage and use | 2.1.3 Statistical quality management |

##### Manage Metadata Lifecycle

*Refines:* OVA-2 Metadata Management; DLM-8 Monitor data quality, lineage and use.

The metadata that supports data acquisition must stay complete, accurate, and current throughout the data life cycle. This sub-process verifies metadata completeness: every registered dataset must have all required metadata fields, as a compliance check on SAF-P09. It assesses metadata quality: are provenance records accurate, are classifications applied correctly, and are agreement references current? The metadata catalogue is actively maintained. Outdated entries are retired, schemas are updated for new source formats, and metadata models are versioned. Lineage from source through ingestion to raw data is tracked. Reconciliation across systems makes sure that catalogue entries match the artefacts actually stored. As CSDA emphasises, metadata carries all the context needed to understand and reuse data; without it, data is effectively useless.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Verify metadata completeness for all registered datasets | Metadata quality report | OVA-2 Metadata Management | SAF-P09 |
| Assess metadata quality: accuracy, currency, correct classification | Metadata quality report | OVA-2 Metadata Management | CSDA Metadata Management |
| Maintain the metadata catalogue: retire entries, update schemas, version models | Catalogue maintenance log | OVA-2 Metadata Management | CSDA Metadata Management |
| Track metadata lineage from source through ingestion to raw data | Metadata lineage audit | DLM-8 Monitor data quality, lineage and use | CSDA Metadata Management |
| Reconcile metadata across systems | Catalogue-artefact reconciliation | OVA-2 Metadata Management | SAF-P09 |

|**PLACEHOLDER: VS-01 management feedback loop: data and paradata from Execution flowing through the five management sub-processes, with dashboards to the process owner, quality reports to the quality manager, compliance reports to VS-07, and improvement recommendations back to Design**|
|---|

#### Metadata per process type

Metadata is produced in every process type, not only in Design. The table shows the data metadata each process type of VS-01 contributes; the paradata are listed in [Standard activities in every value stream](#standard-vs-activities). In Execution, VS-01 also records the collection mode and instrument version as paradata.

| Process type | Data metadata produced |
|---|---|
| Design | Data models, variable definitions, classification schemes, expected formats, quality thresholds |
| Implementation | Schema configurations, parameters of validation rules, catalogue templates, mappings from instruments to metadata |
| Execution | Provenance, source, timestamp, file hash, volume, quality indicator values, and agreement reference per dataset |
| Management | Quality scores, lineage assessments, completeness reports, life cycle status, trend analyses |

|**PLACEHOLDER: VS-01 business object lifecycle: design artefacts govern implementation assets, which produce the process that turns Source Data (#0) into Raw Data (#1), generating provenance, quality, and audit records that management assesses and feeds back to design**|
|---|

### 5. Actors and roles

VS-01 involves more external actors than any other value stream, because it is where the NSI meets its data providers. The table shows the actors and the reference roles involved. Specialised role names used in an NSI map onto these reference roles (see *Role names in the value streams*); for example, the system configurator in the original VS-01 description is ROL-11 Platform engineer. The long-term relationship with each provider is organised in the collaboration COL-01 *Data provision partnership*.

| Actor or role | ID | Process type | Responsibility in VS-01 |
|---|---|---|---|
| Data provider | ACT-03 | External | Supplies data under a data sharing agreement: a government agency, a business, or an individual |
| Respondent | ACT-04 | External | Provides data through survey instruments: web (CAWI), face-to-face (CAPI), telephone (CATI), or paper |
| Supervisory and legal authority | ACT-08 | External | Grants or oversees the legal basis for collection, for example under the statistics law or data protection law |
| Process owner | ROL-01 | Management | Accountable for the end-to-end performance of VS-01 |
| Data owner | ROL-02 | Management | Accountable for State #1; decides on access and retention |
| Data steward | ROL-03 | Execution | Registers datasets in the catalogue, manages metadata entries, applies access controls, resolves gate exceptions |
| Data custodian | ROL-04 | Execution | Operates storage, access control, and retention |
| Statistical designer | ROL-06 | Design | Translates statistical needs into data requirements and process specifications |
| Methodologist | ROL-07 | Design | Designs collection methodology, sampling strategies, and questionnaire content |
| Metadata and data architect | ROL-08 | Design | Designs data models, metadata schemas, and classification mappings |
| Data engineer | ROL-10 | Implementation | Builds and configures ingestion workflows, collection instruments, and data channels |
| Platform engineer | ROL-11 | Implementation | Configures platforms, SFTP endpoints, API connectors, and access controls |
| Test manager | ROL-12 | Implementation | Plans and carries out testing of the acquisition process: technical tests, field tests, integration tests |
| Data collection manager | ROL-13 | Execution | Oversees collection campaigns, coordinates collection teams, and monitors response |
| Data quality analyst | ROL-14 | Execution | Performs validation checks, assesses data quality at intake, and logs exceptions |
| Quality manager | ROL-18 | Management | Monitors key performance indicators, produces quality reports, and drives continuous improvement |
| Compliance officer | ROL-19 | Management | Ensures legal and regulatory compliance and produces audit reports |
| Relationship manager | ROL-23 | Execution | Maintains provider relationships and agreements; handles rejected deliveries with the provider |

### 6. Capabilities, processes, and functions

#### Capability foundations

The table shows which capabilities from the SAF capability model VS-01 relies on, and what role they play. NSIs can use it to map the value stream to their own organisation.

| Capability group | Capabilities | Role in VS-01 |
|---|---|---|
| 1.1 Statistical design and build | 1.1.1 Needs inventory, 1.1.2 Design statistics product, 1.1.3 Build statistics product | Design the data requirements and the collection methodology, and build the acquisition process |
| 1.2 Data collection | 1.2.1 Primary data collection, 1.2.2 Secondary data collection | Carry out the collection: surveys, intake of administrative data, extraction through APIs |
| 2.1 Data management | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management, 2.1.4 Statistical register management | Manage data and metadata during ingestion, assess quality, maintain registers |
| 3.1 Business operations | 3.1.2 Purchasing and contract management | Manage contracts with data providers that are suppliers |
| 3.2 Computerisation and automation | 3.2.1 Application development, 3.2.2 Functional management | Build and maintain collection instruments and ingestion systems |
| 3.3 Security and privacy | 3.3.1 Privacy management, 3.3.2 Security planning, 3.3.3 Security incident management, 3.3.4 Logical identity and access control | Build privacy and security into all acquisition processes |
| 3.4 Customer and chain interaction | 3.4.2 Contact management, 3.4.3 Service agreement | Maintain relationships with respondents and providers, and manage data provision agreements |
| 4.1 Strategy and leadership | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improvement management, 4.1.5 Accountability | Govern the domain, plan improvements, report on compliance |

#### Stages, processes, and functions

The table shows which SAF business processes realise each stage of VS-01 and which business functions they mainly use.

| Stage | Realised by processes | Main functions |
|---|---|---|
| VS-01.1 Identify Data Needs and Sources | PRD-1.1 Identify needs; PRD-1.5 Check data availability and suitability; PRD-2.3 Design collection | FUN-3.1 Design and build statistical products; FUN-6.1 Manage data supplier relationships |
| VS-01.2 Establish Data Agreements and Access Rights | OVA-6 Data Supplier Management; DSP-1 Join a data space; DSP-3 Agree data use conditions | FUN-6.2 Manage data provision agreements; FUN-9.1 Manage data space participation; FUN-10.5 Manage legal affairs |
| VS-01.3 Collect or Receive Data | PRD-4.1 Create frame and select sample; PRD-4.2 Set up collection; PRD-4.3 Run collection; DSP-4 Exchange data under usage control | FUN-3.2 Collect and acquire data; FUN-9.2 Operate data space connectivity |
| VS-01.4 Validate and Log Data Intake | PRD-4.4 Finalise collection; DLM-2 Promote data through a quality gate | FUN-3.2 Collect and acquire data; FUN-7.3 Manage data lifecycle and storage |
| VS-01.5 Store and Register Raw Data Artefacts | DLM-3 Register and catalogue data; DLM-4 Classify and protect data; DLM-5 Store and version data | FUN-7.2 Manage metadata; FUN-7.3 Manage data lifecycle and storage; FUN-7.5 Protect data |

|**PLACEHOLDER: ArchiMate view VS-01 (b) stages realised by processes and functions**|
|---|

#### Framework mappings

This reference table maps each process type of VS-01 to the SAF business processes, the international frameworks (GSBPM, GAMSO, CSDA), and the SAF capability model. It is intended for architects and auditors; the rest of this section does not depend on it.

| Process type | SAF business processes | GSBPM | GAMSO | CSDA | SAF capabilities |
|---|---|---|---|---|---|
| Design | PRD-1.1 to PRD-1.3, PRD-1.5, PRD-1.6, PRD-2.2 to PRD-2.5, DLM-1, DLM-2, DLM-4, DLM-9, OVA-1, OVA-2, OVA-4, OVA-6 | Phase 1 Specify Needs (1.1 to 1.3, 1.5, 1.6), Phase 2 Design (2.2 to 2.5) | Production (design activities), Capability Management | Data Governance, Metadata Management | 1.1.1 Needs inventory, 1.1.2 Design statistics product, 2.1.2 Metadata management |
| Implementation | PRD-3.1, PRD-3.2, PRD-3.4 to PRD-3.7, DLM-2, DLM-3, DLM-4, DLM-6, OVA-2, DSP-1 | Phase 3 Build (3.1, 3.2, 3.4 to 3.7) | Capability Management | Data Ingestion (set-up), Data Governance (configuration) | 1.1.3 Build statistics product, 3.2.1 Application development, 3.2.2 Functional management |
| Execution | PRD-1.1, PRD-1.5, PRD-4.1 to PRD-4.4, DLM-2 to DLM-5, OVA-2, OVA-4, OVA-6, DSP-1, DSP-3, DSP-4 | Phase 4 Collect (4.1 to 4.4); 1.1 and 1.5 in their recurrent form | Production (execution) | Data Ingestion (execution) | 1.2.1 Primary data collection, 1.2.2 Secondary data collection |
| Management | OVA-1, OVA-2, OVA-4, OVA-6, DLM-8, PRD-8.1 to PRD-8.3 | Phase 8 Evaluate; overarching Quality Management and Metadata Management | Corporate Support (Quality, Data, and Metadata Management), Capability Management (improvement) | Data Quality, Data Governance, Traceability | 2.1.3 Statistical quality management, 4.1.4 Improvement management, 4.1.5 Accountability |

### 7. Principles

The following principles govern VS-01 most directly.

| Principle | Statement | Application in VS-01 |
|---|---|---|
| SAF-P01 | Actively participate in open-source communities to maintain collective control over statistical processes | Collection instruments, connectors, and ingestion tooling are reused across products first, in the order reuse, open source, buy, build. Where new tooling is needed, open-source solutions developed with other NSIs come first, and the NSI contributes back, so that it keeps collective control over critical capabilities instead of depending on vendors. **[VC3]** |
| SAF-P07 | Implement loosely coupled processes and systems | Data acquisition is independent from downstream processing. Raw Data (State #1) is the decoupling interface: downstream consumers use it without knowing how it was collected. |
| SAF-P08 | Data is shared property | Raw data, once registered, is available to all authorised consumers. Collection is not duplicated across statistical products when the same source data can serve several purposes. This also reduces response burden. |
| SAF-P09 | No data without metadata and classification | At ingestion, every dataset is enriched with provenance (where it came from and how), source, method, timestamp, quality indicators, and a classification for availability, integrity, and confidentiality. This is not a precondition that blocks ingestion, but an obligation the NSI fulfils during acquisition. |
| SAF-P10 | Security by design | Security is built into the acquisition process from the start: encrypted transfer channels, virus scanning, checksum verification, and access controls. |
| SAF-P11 | Privacy by design | Privacy protection is designed into the acquisition process from the start, not added after data has entered: the moment of pseudonymisation, purpose limitation, the legal basis for processing, and data minimisation. |

::: {.callout-note title="Principles that apply across the process types"}
Several principles apply to all four process types. SAF-P09 applies everywhere: Design defines the target metadata, Execution captures it at ingestion, and Management assesses it and closes remaining gaps. SAF-P10 applies to *Design Access Control and Privacy Framework*, to *Build Collection Instruments and Channels*, and to the stages VS-01.3 to VS-01.5. SAF-P11 starts in *Design Access Control and Privacy Framework* and carries through all process types. SAF-P07 governs the handover of State #1 to VS-02.
:::

### 8. Interfaces, services, and events

**Boundary interfaces**

VS-01 has two boundary interfaces: intake from outside the NSI, and handover to the next value stream.

| Boundary | Handed over | Required metadata | Trigger | Responsibility transfer |
|---|---|---|---|---|
| Provider or respondent → VS-01 (intake) | Delivery or survey response (#0) | Source identifier and organisation, transfer method and channel, receipt timestamp, file hash, volume, agreement reference, collection mode and instrument version (surveys) | *Delivery received* or response submitted | The provider is responsible up to receipt; VS-01 takes custody and the obligation to capture metadata (SAF-P09) at the point of receipt |
| VS-01 → VS-02 (or VS-03) (handover) | Registered raw data version (#1) | Minimum metadata set of State #1: provenance, source, collection method, receipt timestamp, file hash, agreement reference, quality assessment, classification | *Raw Data Registered* | VS-01 keeps custody of the raw artefact; the consumer takes responsibility for further processing on receipt of the event |

**Business services**

| Service | Offered to | Realised in | Interfaces |
|---|---|---|---|
| Data collection service | Respondents, data providers | VS-01.3 Collect or Receive Data | Web portals (CAWI), mobile applications (CAPI), telephone systems (CATI), paper, SFTP endpoints, REST APIs, data space connectors |
| Data agreement service | Data providers, legal authorities | VS-01.2 Establish Data Agreements and Access Rights | Agreement management, relationship manager |
| Raw data provisioning service | VS-02 Data Standardization and Integration, VS-03 Data Editing and Enrichment, other domains | VS-01.5 Store and Register Raw Data Artefacts | Event notification (*Raw Data Registered*) and a catalogue query interface to find and access raw datasets |
| Ingestion monitoring service | Process owner, quality manager | Management sub-processes *Monitor Process Performance* and *Assess Data Quality* | Dashboards and quality reports |
| Metadata catalogue service | All data consumers in the NSI | Management sub-process *Manage Metadata Lifecycle* | Search and browse interface for metadata, with metadata exchange compliant with SDMX |
| Design and methodology service | Methodologists, statistical designers, data engineers | All Design sub-processes of VS-01 | Design documents, methodology advice |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Design artefacts published* | Start of Implementation after a design change |
| *Pipeline production-ready* | End of Implementation; Execution can start |
| *Collection period opened* | Start of VS-01.3 for a survey cycle (PRD-4.3 Run collection) |
| *Agreement expired or changed* | A review in VS-01.2 before the next delivery |
| *Delivery received* | Start of VS-01.4 for that delivery |
| *Data Intake Validated* / *Data Intake Rejected* | Outcome of VS-01.4; rejection starts provider follow-up |
| *Raw Data Registered* | Completion of VS-01.5; triggers the consuming value stream |
| *Improvement recommendations issued* | Input for Design from *Continuous Improvement* |

|**PLACEHOLDER: VS-01 event choreography between data provider, NSI teams, and process management across Design, Implementation, Execution (agreement, primary or secondary collection, validation passed or failed), and Management (key performance indicators, quality, compliance, improvement recommendations)**|
|---|

**Interaction with the supporting value streams**

| Value stream | Provides to VS-01 | Receives from VS-01 |
|---|---|---|
| VS-07 Governance and Compliance | Legal register, privacy and security policy | Audit trails, compliance evidence |
| VS-08 Innovation and Methodological Development | New sources and collection methods | Improvement needs |
| VS-09 Infrastructure and Platform Enablement | Channels, storage, catalogue, event interfaces | Capacity and channel requirements |
| VS-10 Customer and Stakeholder Engagement | Provider relationships and burden insight | Provider feedback and issues |

### 9. Key performance indicators

The key performance indicators are collected per production cycle in *Monitor Process Performance*. They feed the dashboard that the process owner reviews.

| KPI | Description | Measurement |
|---|---|---|
| Response rate | Share of sampled units that provided data (surveys) | Per survey, per mode, per cycle |
| Delivery timeliness | Share of deliveries received within the agreed window | Per source, per cycle |
| Rejection rate | Share of deliveries that failed the gate of State #1 | Per source, per cycle |
| Processing time | Time from receipt to catalogue registration | Per delivery, per cycle |
| Metadata completeness | Share of required metadata fields populated at registration | Per delivery |
| Exception rate | Frequency of exception handling per check rule | Per rule, per cycle |

### 10. Examples

**Survey.** The Labour Force Survey uses a mixed-mode approach and a 2-2-2 rotation panel for longitudinal tracking. Sampled persons first receive a web invitation by email; non-respondents are called after two weeks, and hard-to-reach groups are visited by an interviewer. Adaptive questioning keeps response burden low. Each mode records its own paradata, such as completion time or interviewer identifier. Responses are registered as one #1 version per collection batch, and the data collection manager follows the response rate per mode during the cycle.

**Multi-mode census.** The 2026 census collects 70% of households by web (CAWI), 25% by interviewer (CAPI) for non-respondents and hard-to-reach areas, and 5% on paper for elderly and institutionalised populations. Each mode records its own metadata: browser type and completion time for CAWI; interviewer identifier, GPS coordinates, and interview duration for CAPI; scanning batch identifier and OCR confidence scores for paper.

**Household budget survey.** The implementation team builds a CAWI portal with a diary for daily spending, configures it in 12 languages, and implements the designed sampling filter. It also sets up an SFTP channel as a fallback for large retailers, which deliver scanner data as supplementary price information.

**Administrative register.** The agreement with the tax authority requires delivery within 45 days of quarter end and at least 98% of the expected records. Before the Q3 delivery window opens, the team checks that the SFTP credentials are valid and records the active agreement reference, to be linked to the incoming file. The file arrives by secure file transfer on day 38, with 2.3 million records, 99.2% of the expected volume. The SHA-256 checksum passes, all 47 fields conform to the schema, and the null rate on mandatory fields is 0.3%, within the 1% tolerance. Fourteen unknown business identifiers are not an intake issue; they pass through with a flag. The result is *Data Intake Validated*, and every check is logged with its timestamp, rule version, and operator identifier. The file is registered as `RD-TAX-2026Q3-001`, and the *Raw Data Registered* event notifies VS-02.

**Register-based census.** For its next census, the NSI chooses a register-first design. The population register is the primary source. A sample survey adds variables that registers do not hold, such as housing conditions and commuting patterns, and municipal records are used for validation. Design produces the mapping from register variables to census variables, the sample design of the supplementary survey, and the quality criteria for accepting register data. At the start of each reference year, the census team confirms that all 393 municipal registers are available, verifies contact persons and API endpoints, and checks that the survey frame has been updated with the latest extract of the population register.

**Web data.** Every night, 12,500 product pages of 25 retailers are scraped; on a typical day 95% succeed. Each scrape records the scraper version and a fingerprint of the page structure. When one retailer redesigns its website, the fingerprints change and the success rate drops. Management detects the trend and sends an improvement action to Design, where the scraper is rebuilt.

| **Toolkit:** SAF-TK-V01 VS-01 maturity checklist and scenarios |
|---|



## VS-02 Data Standardization and Integration

### 1. Purpose and value created

VS-02 makes data from different sources speak the same language. Once raw data is in NSI custody, VS-02 aligns its structure, format, and codes with the agreed standards of the NSI, so that datasets that looked different at the source can be compared and combined. It does this without changing any value: it re-expresses and annotates, it does not transform. The result is the same information in a common shape, expressed in standard classifications, with rich metadata and without direct identifiers. The value created is **coherence and comparability**: data from surveys, administrative registers, and external sources can flow into editing, analysis, and modelling as one structured, standardised asset.

VS-02 corresponds to the business domain **Standardization without loss of content** (see *Steady-State Architecture, Business domains*). This section describes the business layer of that domain for all four process types: Design, Implementation, Execution, and Management. Content correction, imputation, and enrichment are out of scope; they belong to VS-03 Data Editing and Enrichment.

::: {.callout-note title="Signature discipline: standardisation without loss of content"}
VS-02 only maps codes one-to-one, reformats structure, and annotates metadata. It never changes a value. Unit and currency conversion, reference-period alignment, value reconciliation across sources, derivation of new variables, and interpretive coding of free text are deliberately left to VS-03. Interpretive coding, for example coding a written job title to ISCO, needs judgement that can change informational content, so it is not a VS-02 activity. The no-loss-of-content rule covers the statistical content: records, observed values, and key measures. It does not cover direct identifiers, which are personal data rather than statistical content. Their removal or pseudonymisation at this transition (SAF-P11) therefore never counts as content loss.
:::

|**PLACEHOLDER: ArchiMate view VS-02 (a) value stream and capabilities**|
|---|

<br>

### 2. Position and state transition

VS-02 is the second primary value stream. It receives raw data from VS-01 and hands standardised data to VS-03. It is the stage that harmonises and integrates information, so that data from different sources works together, by aligning structure, format, and codes and not by changing values.

VS-02 takes data from State #1 to State #2. Before VS-02, the data is in NSI custody in its original form, usually with direct identifiers. After VS-02, it is aligned to common structures, formats, classifications, and semantics, with direct identifiers removed or pseudonymised, so that it is interoperable and comparable across sources, domains, and time. The quality gate, the minimum metadata set, and the protection of State #2 are described in *State #2: Standardized Data* and are not repeated here. **[VC10]** State #2 is optional: a source that already arrives in the standard structure and coding of the NSI can go directly from #1 to VS-03, and the skip is recorded in the catalogue.

| From | To | Gate | Event out |
|---|---|---|---|
| #1 Raw Data | #2 Standardized Data | Gate of State #2 (structural and classification conformance, mapping coverage, semantic metadata, no loss of content, identifier protection, referential integrity, metadata and lineage) | *Standardized Data Registered* |

|**PLACEHOLDER: ArchiMate view VS-02 (c) state handover and events: Raw Data (#1) from VS-01, the standardisation service at the domain boundary (profiling, classification and coding, semantic alignment, conformance check), Standardized Data (#2) handed to VS-03**|
|---|

<br>

### 3. Stages

The stages describe the value that VS-02 adds in every production cycle. Together they form the execution process type of VS-02. In a mature steady state, the target model, correspondence tables, and conformance rules have been designed and built in advance (see attribute 4). Execution then focuses on applying mappings and classifications, capturing lineage and conformance metadata, and passing the quality gate without altering content.

| Stage | Name | Value added |
|---|---|---|
| VS-02.1 | Profile and Assess Data Structure | Differences from the target model are known |
| VS-02.2 | Apply Standard Classifications and Formats | Data uses common codes, formats, and identifiers |
| VS-02.3 | Align Metadata and Semantics | Definitions and descriptions are consistent |
| VS-02.4 | Validate Structural and Semantic Conformance | Conformance to standards is confirmed |
| VS-02.5 | Register Standardized Artefacts | Standardised data is registered and available for reuse (State #2) |

Each stage below is described with its activities. The column *SAF process* shows the business process from *Business Processes* that the activity belongs to. The column *Other reference* shows the principles, capabilities, or external frameworks that the activity applies. **[VC9]**

<br>

#### VS-02.1 Profile and Assess Data Structure

**Value created:** *A clear understanding of how far incoming raw data is from the target standard, so the right mapping and format coercion can be applied.*

The stage starts when the *Raw Data Registered* event arrives from VS-01. The profiling components analyse the structure of the incoming dataset: they infer types, measure cardinalities and value distributions, and detect inconsistencies, missing fields, and structural anomalies relative to the target data model. The dataset is then compared with the target schema. The result is a structure-gap assessment: which fields map directly, which need format coercion, which source codes have a standard correspondence, and which values are uncoded and must go to VS-03. A significant or unexpected structural deviation, such as a source that has changed its schema, goes back to Design instead of being adapted ad hoc during the cycle.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Profile incoming raw data: types, cardinalities, distributions, anomalies | Data profiling report | PRD-5.3 Review and validate | GSBPM 5.1 |
| Compare the structure with the target data model | Structure-gap assessment | PRD-5.3 Review and validate | |
| Identify the format coercion and code mappings to apply | Mapping plan (per dataset) | PRD-5.3 Review and validate; PRD-5.2 Classify and code | |
| Flag unexpected structural deviations for design review | Schema-change exception (if any) | PRD-5.3 Review and validate | |

<br>

#### VS-02.2 Apply Standard Classifications and Formats

**Value created:** *Source codes re-expressed in shared, authoritative classifications and a common format, so data is comparable across sources, with no value changed.*

This is the core of standardisation. The mapping and format-coercion component applies the designed value-preserving operations to bring the data into the target format: renaming, restructuring, type casting, reformatting (for example from CSV to XML), and key alignment. The mapping services then translate values that already carry a source code into the corresponding standard code (NACE, ISCO, COICOP, NUTS, SDMX code lists) through deterministic correspondence tables, one-to-one, keeping the original value. Values without a correspondence, and free text that needs interpretation, are not coded here. They are flagged and routed to VS-03. Only the representation changes and standard codes are added. Every applied mapping and classification version is recorded as lineage.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Apply format coercion: rename, restructure, cast, reformat, align keys | Format-coerced dataset (values unchanged) | PRD-5.1 Integrate data (key alignment only) | GSBPM 5.1 |
| Map source codes to standard classifications one-to-one through correspondence tables | Standard-coded dataset (original preserved) | PRD-5.2 Classify and code; DLM-9 Manage reference and master data | 1.3.1 Data standardisation |
| Flag unmapped, uncoded, and free-text values and route them to VS-03 | Unmapped-value handover list | PRD-5.2 Classify and code | |
| Capture applied mappings and classification versions as lineage | Mapping and classification lineage | PRD-5.2 Classify and code; OVA-2 Metadata Management | SAF-P09 |

|**PLACEHOLDER: VS-02 classification mapping logic: survey, administrative, and emerging-source inputs pass format coercion and a deterministic correspondence lookup; values whose source code has a correspondence become standard-coded values with the original preserved, unmapped and free-text values go to VS-03 for interpretive coding**|
|---|

<br>

#### VS-02.3 Align Metadata and Semantics

**Value created:** *Coherent, shared meaning across datasets, so the same concept means the same thing everywhere.*

Once structure and codes are standardised, descriptive metadata and semantics are harmonised at the metadata level only. Source variables are linked to canonical concepts in the concept system. The unit of measure and reference-period basis of each variable are recorded as metadata against the standard conventions, not converted. Where sources define the same concept differently, for example two sources that define "employee" differently, the difference is recorded as metadata and flagged for VS-03 instead of being reconciled by adjusting values. Quality descriptors (completeness, accuracy, confidentiality flags) are standardised and attached. The harmonised metadata is bound to the dataset, so downstream consumers receive both the standardised data and the semantics needed to interpret it.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Link source variables to canonical concepts | Concept-aligned variables | OVA-2 Metadata Management | GSBPM 5.1 |
| Record unit of measure and reference-period basis as metadata (no conversion) | Unit and period metadata | OVA-2 Metadata Management | SAF-P09 |
| Record differing cross-source definitions as metadata and flag them for VS-03 | Definition-difference record | OVA-2 Metadata Management | 2.1.4 Statistical register management |
| Standardise and attach quality descriptors | Harmonised quality metadata | OVA-2 Metadata Management | CSDA Metadata Management |

<br>

#### VS-02.4 Validate Structural and Semantic Conformance

**Value created:** *Confidence that the standardised data conforms to standards and that no content was lost in standardisation.*

Before standardised data can be accepted, it must pass the quality gate of State #2. The automated checks from *Design Conformance Validation Rules* run on every dataset: structural validation against the target model, classification conformance, and semantic conformance. Content-preservation checks confirm that every value is unchanged and that record counts and key business measures are identical before and after. The conformance assessment gives a structural score, a mapping coverage rate, and a semantic conformance rating. Every result, exception, and decision is logged in a mapping and format-coercion audit trail, with data metadata (what was validated, what passed) and process metadata (who validated, when, which rule and engine version). The outcome is one of two business events. *Standardisation Conformed* starts registration. *Standardisation Non-Conformant* starts exception handling: re-map, route unmapped values to VS-03, or accept conditionally with a conformance flag.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Validate the structure against the target model | Structural validation result | PRD-5.3 Review and validate; DLM-2 Promote data through a quality gate | |
| Validate classification conformance: valid codes, correct version, coverage | Classification conformance result | PRD-5.3 Review and validate | |
| Validate semantic conformance: units, definitions, reference periods recorded | Semantic conformance result | PRD-5.3 Review and validate | |
| Run the no-loss-of-content checks: record and measure preservation | Content-preservation result | DLM-2 Promote data through a quality gate | GAMSO Quality Management |
| Create the audit trail: log all conformance results, exceptions, and decisions | Audit trail record | OVA-4 Process Data Management | GAMSO Quality Management |

<br>

#### VS-02.5 Register Standardized Artefacts

**Value created:** *Secure, organised, and traceable storage of standardised data, discoverable by downstream consumers.*

This stage persists conformant standardised data and makes it discoverable for the rest of the statistical system. Each dataset version receives a unique persistent identifier (URI or UUID) and is stored in the standardised data repository, in line with the loose coupling of SAF-P07. The stage confirms that identifiers have been removed or pseudonymised according to the privacy design (SAF-P11). Metadata is registered in the catalogue, in line with SAF-P09: the mapping lineage, the applied classification versions, the harmonised concept and quality metadata, and the conformance results. Lineage from Raw Data (#1) to Standardized Data (#2) is recorded, traceable to the originating source. Access permissions are applied according to the designed framework (SAF-P10). The stage ends by publishing the *Standardized Data Registered* event, which tells VS-03 that new standardised data is available for editing and enrichment.

**Output:** **Standardized Data (State #2)**, the official handover artefact to the rest of the statistical value chain. Its structure and minimum metadata set are described in *State #2: Standardized Data*. **[VC10]**

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Assign a unique persistent identifier (URI or UUID) to the dataset version | Dataset ID | DLM-3 Register and catalogue data | |
| Store the data in the standardised data repository | Stored standardised artefact | DLM-5 Store and version data | SAF-P07 |
| Confirm that identifier removal or pseudonymisation has been applied | Privacy-compliant dataset | DLM-4 Classify and protect data | SAF-P11 |
| Register metadata: mapping lineage, classification versions, harmonised concepts, conformance results | Catalogue registration | DLM-3 Register and catalogue data; OVA-2 Metadata Management | SAF-P09 |
| Apply access permissions according to the designed framework | Access-controlled dataset | DLM-4 Classify and protect data | SAF-P10 |
| Publish the *Standardized Data Registered* event to notify VS-03 | Event notification | DLM-3 Register and catalogue data | SAF-P07 |

### 4. The four process types

The sub-processes below are specific to VS-02. Each refines one or more SAF business processes, listed as *Refines*, which keeps it traceable to *Business Processes*. Sub-processes marked *(standard)* work as described in [Standard activities in every value stream](#standard-vs-activities); only the VS-02 specifics are listed. In this domain, metadata, and classification in particular, is not a by-product but the central asset being created.

#### Design: provides metadata

| Design sub-process | Refines | Main outputs |
|---|---|---|
| Design Target Data Models and Schemas | PRD-2.2 Design variables; PRD-2.5 Design processing and analysis; DLM-1 Plan and design data assets; DLM-9 Manage reference and master data | Target data model, canonical concept catalogue, structural conformance rules, integration key design |
| Design Classification Mapping Strategy | PRD-2.5 Design processing and analysis; DLM-9 Manage reference and master data | Classification standards register, version policy, correspondence tables, unmapped-value routing rules |
| Design Metadata and Semantic Harmonisation Rules | PRD-2.2 Design variables; OVA-2 Metadata Management | Harmonised concept system, unit and reference-period metadata standards, semantic mapping rules, definition-difference policy |
| Design Conformance Validation Rules | PRD-2.5 Design processing and analysis; DLM-2 Promote data through a quality gate; OVA-1 Quality Management | Validation rule sets, content-preservation checks, exception handling policy |
| Design Standardisation Registration and Privacy Framework | DLM-1 Plan and design data assets; DLM-4 Classify and protect data; OVA-4 Process Data Management | Data classification policy, access control design, lineage model, pseudonymisation design, audit logging specification |

##### Design Target Data Models and Schemas

*Refines:* PRD-2.2 Design variables; PRD-2.5 Design processing and analysis; DLM-1 Plan and design data assets; DLM-9 Manage reference and master data.

Standardisation starts from the canonical structure that all data must conform to. This sub-process specifies the target data model for Standardized Data (State #2): entities, fields, data types, formats, units of measure, cardinalities, and referential constraints. It sets canonical representations for common concepts, such as dates, geographies, currencies, and organisational and personal identifiers, so that data from surveys, registers, and external sources can be expressed consistently. It defines the structural conformance contract: what it means for a dataset to be structurally valid against the target model. Where several sources describe the same population, the integration model defines how they are aligned to a common key structure, for example the key of a business or statistical unit register.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define the canonical target data model for State #2: entities, fields, types, formats, units | Target data model specification | PRD-2.2 Design variables; DLM-1 Plan and design data assets | 1.1.2 Design statistics product |
| Define canonical representations for common concepts (dates, geography, currency, identifiers) | Canonical concept catalogue | PRD-2.2 Design variables | |
| Define the structural conformance contract and referential constraints | Structural conformance rules | PRD-2.5 Design processing and analysis | |
| Define the integration and linkage key structure for multi-source alignment | Integration key design | DLM-9 Manage reference and master data | 2.1.4 Statistical register management |

##### Design Classification Mapping Strategy

*Refines:* PRD-2.5 Design processing and analysis; DLM-9 Manage reference and master data.

Once the target structure is set, the classification steward designs how source codes are mapped one-to-one to standard classifications. The sub-process selects the authoritative classifications and code lists the NSI conforms to, such as NACE, ISCO, COICOP, NUTS, SDMX code lists, and concepts aligned with GSIM. It defines the version policy: which version applies, and how transitions between versions are handled. The mapping is deterministic: maintained correspondence tables translate a value that already carries a source code into the corresponding standard code, and the original value is kept. The design also specifies that unmapped or uncoded values are flagged and passed to VS-03, which does any interpretive coding of free text. Reference and master data sources are identified, so that mapping is anchored to authoritative registers.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Select authoritative classifications and code lists (NACE, ISCO, COICOP, NUTS, SDMX, GSIM concepts) | Classification standards register | PRD-2.5 Design processing and analysis; DLM-9 Manage reference and master data | |
| Define the classification version policy and transition handling | Classification version policy | DLM-9 Manage reference and master data | SAF-P09 |
| Design deterministic one-to-one correspondence tables from source codes to standard codes | Correspondence table set | PRD-2.5 Design processing and analysis | 1.3.1 Data standardisation |
| Define the handling of unmapped and uncoded values: flag and route to VS-03 | Unmapped-value routing rules | PRD-2.5 Design processing and analysis | |
| Identify reference and master data sources for mapping | Reference data catalogue | DLM-9 Manage reference and master data | CSDA Reference Data |

##### Design Metadata and Semantic Harmonisation Rules

*Refines:* PRD-2.2 Design variables; OVA-2 Metadata Management.

This sub-process defines how descriptive metadata and semantics are harmonised, so that data from different sources is understood consistently without any value changing. The team designs harmonised concept and variable definitions, and the metadata that records the unit of measure and reference-period basis of each variable. Semantic mapping rules link source variables to canonical concepts in the concept system, and quality descriptors (completeness, accuracy, confidentiality flags) are standardised. Where sources define the same concept differently, the design specifies that the difference is recorded as metadata and flagged for VS-03; VS-02 does not adjust values to reconcile them. The catalogue structure for standardised artefacts is designed so that lineage from raw to standardised state is fully traceable, which makes active metadata a foundation for downstream automation, as emphasised by the Metadata Management capability of CSDA.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define harmonised concept and variable definitions | Harmonised concept system | PRD-2.2 Design variables | |
| Define the unit and reference-period metadata to record per variable (no conversion) | Unit and reference-period metadata standards | OVA-2 Metadata Management | SAF-P09 |
| Design semantic mapping rules from source variables to canonical concepts | Semantic mapping rules | OVA-2 Metadata Management | CSDA Metadata Management |
| Design rules to record differing cross-source definitions as metadata and flag them for VS-03 | Definition-difference policy | OVA-2 Metadata Management | 2.1.4 Statistical register management |
| Design the catalogue structure and lineage model for standardised artefacts | Catalogue registration template | OVA-2 Metadata Management | CSDA Metadata Management |

##### Design Conformance Validation Rules

*Refines:* PRD-2.5 Design processing and analysis; DLM-2 Promote data through a quality gate; OVA-1 Quality Management.

Before any data is standardised, the criteria for "standardised" must be clear. This sub-process sets structural validation rules (field types, formats, value ranges, cardinalities, referential integrity against the target model), classification conformance rules (every mapped code belongs to the correct classification version, no orphan codes), and semantic conformance rules (units, definitions, and reference periods correctly recorded as metadata). The maximum acceptable unmapped-value rate is agreed as a coverage threshold. Exception handling rules distinguish between rejection, conditional acceptance with conformance flags, and routing of unmapped values to VS-03. The rules also verify the no-loss-of-content rule: every value is unchanged, and record counts and key business measures are identical before and after. Together, these rules make up the VS-02 part of the quality gate of State #2. The Quality Management capability of GAMSO provides the overall control framework.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define structural validation rules against the target model | Structural validation rule set | PRD-2.5 Design processing and analysis | |
| Define classification conformance rules: valid codes, correct version, no orphans | Classification conformance rules | PRD-2.5 Design processing and analysis | |
| Define semantic conformance rules: units, definitions, reference periods | Semantic conformance rules | PRD-2.5 Design processing and analysis | |
| Define the no-loss-of-content checks: record and measure preservation | Content-preservation checks | OVA-1 Quality Management | GAMSO Quality Management |
| Design exception handling rules: rejection, conditional acceptance, manual review | Exception handling policy | DLM-2 Promote data through a quality gate | |

##### Design Standardisation Registration and Privacy Framework

*Refines:* DLM-1 Plan and design data assets; DLM-4 Classify and protect data; OVA-4 Process Data Management.

This sub-process makes sure that standardised artefacts are correctly registered, traceable, and privacy-compliant. Each standardised dataset receives a classification for availability, integrity, and confidentiality (SAF-P09), and role-based access control for the standardised data repository is designed (SAF-P10). The lineage model is designed so that every standardised field can be traced back to its raw source value and the mapping rule applied. Privacy protection follows SAF-P11: standardisation is where direct identifiers are removed or replaced with pseudonymous keys. The design specifies which identifiers are dropped, which are pseudonymised, the pseudonymisation method and key management, and the data minimisation rules. Audit logging requirements, which define the mapping and format-coercion events that must be recorded, complete the design.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define the data classification (availability, integrity, confidentiality) for standardised datasets | Data classification policy | DLM-4 Classify and protect data | SAF-P09 |
| Design role-based access control for the standardised data repository | Access control design | DLM-1 Plan and design data assets; DLM-4 Classify and protect data | SAF-P10; 3.3.4 Logical identity and access control |
| Design the lineage model: standardised field, raw source value, mapping rule | Lineage model specification | DLM-1 Plan and design data assets | CSDA Traceability |
| Design identifier removal and pseudonymisation: which identifiers, method, key management, minimisation | Privacy and pseudonymisation design | DLM-4 Classify and protect data | SAF-P11; 3.3.1 Privacy management |
| Design audit logging requirements for mapping and format coercion | Audit logging specification | OVA-4 Process Data Management | SAF-P10 |

|**PLACEHOLDER: VS-02 design process decomposition: inputs (raw data model of State #1, framework standards, classification standards such as NACE, ISCO, COICOP, SDMX, legal and privacy requirements), the five design sub-processes in order, and the artefact each produces (target data model, correspondence tables, harmonised concepts, conformance rule set, lineage and privacy design), which together govern Implementation, Execution, and Management**|
|---|

#### Implementation: provides the execution process

| Implementation sub-process | Refines | Main outputs |
|---|---|---|
| Build Profiling and Mapping Engines | PRD-3.2 Reuse or build processing and analysis components | Profiling module, lineage-aware mapping and format-coercion component, versioned mapping repository |
| Configure Classification Mapping Services | PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows; DLM-9 Manage reference and master data | Mapping services with loaded correspondence tables, version control, unmapped-value routing |
| Build Conformance Validation Pipelines and Metadata Registration | PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows; DLM-3 Register and catalogue data; DLM-4 Classify and protect data; OVA-2 Metadata Management | Automated conformance pipeline, pseudonymisation component, metadata propagation, events, exception routing |
| Test and Validate the Pipeline *(standard)* | PRD-3.5 Test production systems; PRD-3.6 Test statistical business process; PRD-3.7 Finalise production systems | Test reports; mapping verification report (correspondence tables checked against the source code lists); pilot confirming one-to-one mapping, complete lineage, no loss of content, routing of unmapped values to VS-03, and identifier removal; volumes tested against processing windows |

##### Build Profiling and Mapping Engines

*Refines:* PRD-3.2 Reuse or build processing and analysis components.

This sub-process turns the target data model and mapping designs into operational tools. Profiling components analyse the structure of incoming raw data: they infer types and detect cardinalities, value distributions, and structural anomalies, so the pipeline can report how far each source is from the target model. The mapping and format-coercion component applies the designed value-preserving operations: renaming, restructuring, type casting, reformatting (for example from CSV to XML), and key alignment. It does not convert units, currencies, or reference periods; those are recorded as metadata, and any conversion takes place in VS-03. The component is declarative and lineage-aware: for each output field it records which input field and which rule produced it. All mapping logic is version-controlled, so that any standardised record can be reproduced from raw data.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Build data profiling components: type inference, cardinality, distributions, anomalies | Production-ready profiling module | PRD-3.2 Reuse or build processing and analysis components | 3.2.1 Application development |
| Build or configure the mapping and format-coercion component: rename, restructure, cast, reformat, align keys | Configured mapping component | PRD-3.2 Reuse or build processing and analysis components | |
| Configure lineage capture for every mapping and coercion operation | Lineage-aware mapping modules | PRD-3.2 Reuse or build processing and analysis components | CSDA Traceability |
| Version-control all mapping and format-coercion logic | Versioned mapping repository | PRD-3.2 Reuse or build processing and analysis components | SAF-P10 |

##### Configure Classification Mapping Services

*Refines:* PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows; DLM-9 Manage reference and master data.

The designed correspondence tables are turned into automated mapping services. Deterministic correspondence tables are loaded and connected to authoritative reference data, so that a value already carrying a source code is translated one-to-one to the corresponding standard code. Classification version control is configured, so that the correct version is applied and version transitions are managed. Values without a matching correspondence, and free-text or uncoded values, are routed to VS-03 instead of being coded here. Reference and master data connections keep the mapping synchronised with authoritative registers.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Load correspondence tables for deterministic mapping from source codes to standard codes | Configured mapping services | PRD-3.2 Reuse or build processing and analysis components | |
| Configure classification version control and transition handling | Version-controlled classifications | DLM-9 Manage reference and master data | SAF-P09 |
| Configure the routing of unmapped and uncoded values to VS-03 | Unmapped-value routing | PRD-3.4 Configure workflows | |
| Configure reference and master data connections | Synchronised reference data | DLM-9 Manage reference and master data | CSDA Reference Data |

##### Build Conformance Validation Pipelines and Metadata Registration

*Refines:* PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows; DLM-3 Register and catalogue data; DLM-4 Classify and protect data; OVA-2 Metadata Management.

This sub-process implements the conformance validation rules and the registration of standardised artefacts. Structural, classification, semantic, and content-preservation checks run as automated validations on every standardised dataset. Catalogue entries are built from the designed metadata model, and automatic propagation makes mapping lineage, applied classification versions, harmonised definitions, and conformance scores flow into the catalogue. Identifier removal and pseudonymisation are implemented according to the privacy design. Event notifications alert VS-03 when standardised data is registered, and exception workflows route non-conforming data to manual review. As CSDA emphasises, the ultimate goal is active metadata: metadata that can drive standardisation rules and downstream processing specifications.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Implement conformance checks as automated validations (structural, classification, semantic, content preservation) | Automated conformance pipeline | PRD-3.2 Reuse or build processing and analysis components | |
| Implement identifier removal and pseudonymisation according to the privacy design | Pseudonymisation component | DLM-4 Classify and protect data | SAF-P11 |
| Configure automatic metadata and lineage propagation into the catalogue | Automated metadata pipelines | DLM-3 Register and catalogue data; OVA-2 Metadata Management | CSDA Metadata Management |
| Configure the *Standardized Data Registered* event for downstream consumers | Event publication | PRD-3.4 Configure workflows | SAF-P07 |
| Configure exception handling workflows | Non-conformance routing and review queues | PRD-3.4 Configure workflows | |

|**PLACEHOLDER: VS-02 implementation pipeline: the five design artefacts feeding the three build sub-processes (target model and harmonisation rules into the profiling and mapping engines, the classification strategy into the mapping services, conformance rules and the lineage and privacy design into the conformance pipeline), followed by technical testing, pilot and mapping verification, and performance and lineage testing, resulting in a production-ready standardisation pipeline and operational procedures**|
|---|

#### Execution: provides the statistical data

Execution runs the stages of VS-02 in every production cycle. The stages and their activities are described in attribute 3. A cycle starts for each new raw data version registered by VS-01. Execution applies the designs and the solution as they are; a changed source schema or a missing correspondence that needs a new rule goes back to Design. Every dataset ends in one of three outcomes: registered, registered with conformance flags and a list of unmapped values for VS-03, or returned for re-mapping.

| Aspect | VS-02 |
|---|---|
| Trigger | *Raw Data Registered* |
| Cadence | Per registered raw data version |
| Performed by | ROL-14 Data quality analyst, ROL-03 Data steward |
| Input | Raw data version (#1), production-ready pipeline, current correspondence tables and target model |
| Output | Registered standardised data version (#2), its mapping lineage, and the list of unmapped values for VS-03 |
| Control point | Gate of State #2 in VS-02.4 |
| Exception path | Re-mapping after *Standardisation Non-Conformant*; unmapped values routed to VS-03 with conditional acceptance; schema change at the source back to Design |

#### Management: provides quality reports

| Management sub-process | Refines | Main outputs |
|---|---|---|
| Monitor Process Performance *(standard)* | OVA-4 Process Data Management; PRD-8.1 Gather evaluation inputs | Process performance dashboard; throughput report against processing windows; paradata on engine and classification versions |
| Assess Standardisation Quality | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use | Mapping completeness report, conformance and orphan-code report, conformance quality report, trend analysis |
| Manage Classification and Metadata Lifecycle | DLM-9 Manage reference and master data; OVA-2 Metadata Management; DLM-8 Monitor data quality, lineage and use | Classification version and correspondence register, metadata quality report, reference data maintenance log, lineage audit |
| Audit and Compliance Reporting *(standard)* | OVA-1 Quality Management; OVA-4 Process Data Management; DLM-8 Monitor data quality, lineage and use | Audit trail from each raw value through the mapping rules to the standardised value, supporting reproducibility and content preservation; privacy compliance record on identifier removal, pseudonymisation, and minimisation at the #1 to #2 transition; standards compliance report on adopted classifications and SDMX exchange (4.1.5 Accountability) |
| Continuous Improvement *(standard)* | PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan | Improvement recommendations, for example extending correspondence tables to raise coverage, refining mappings that produce orphan codes, adopting new classification versions, and simplifying conformance rules that produce false positives; recurring unmapped values that need interpretive coding are passed to VS-03 instead of being absorbed in VS-02; trends watched: mapping coverage, unmapped-value rate, conformance pass rate, re-mapping rate |

##### Assess Standardisation Quality

*Refines:* OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use.

Beyond process performance, the quality of the standardised data itself is evaluated against the criteria set in *Design Conformance Validation Rules*. Each dataset is assessed on several dimensions. Mapping completeness covers the share of source codes mapped one-to-one and the unmapped-value rate routed to VS-03. Classification conformance covers orphan codes and correct versions. Structural and format conformance covers alignment with the target model. Metadata completeness covers units, reference-period bases, and definitions correctly recorded. Content preservation confirms that no value changed and that record counts and key measures are identical. Quality indicators are produced per dataset, per source, and per production cycle. Trends are tracked to detect deteriorating sources, growing unmapped-value rates, or problems with classification versions. This follows the Data Quality capability of CSDA and SAF capability 2.1.3 *Statistical quality management*.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Assess mapping completeness and the unmapped-value rate | Mapping completeness report (per cycle) | OVA-1 Quality Management | 2.1.3 Statistical quality management |
| Assess classification conformance and the orphan-code rate | Conformance and orphan-code report | OVA-1 Quality Management | CSDA Data Quality |
| Assess structural and format conformance, metadata completeness, and content preservation | Conformance quality report | DLM-8 Monitor data quality, lineage and use | 2.1.3 Statistical quality management |
| Identify quality trends across sources, classifications, and cycles | Quality trend analysis | DLM-8 Monitor data quality, lineage and use | 2.1.3 Statistical quality management |

##### Manage Classification and Metadata Lifecycle

*Refines:* DLM-9 Manage reference and master data; OVA-2 Metadata Management; DLM-8 Monitor data quality, lineage and use.

The classifications and metadata that support standardisation must stay complete, accurate, and current. This sub-process governs the life cycle of classification versions: adopting new versions, for example a NACE or COICOP revision, managing transition periods, and maintaining the correspondence tables between versions. It verifies, as a compliance check on SAF-P09, that every standardised dataset carries full mapping lineage, classification versions, and harmonised concepts. It maintains the concept system, code lists, and reference data, so that mapping stays anchored to authoritative sources. Lineage from raw through standardisation to the standardised state is tracked, and reconciliation across systems makes sure that catalogue entries match the stored artefacts. As CSDA emphasises, active, well-managed metadata is what makes standardised data reusable and downstream automation possible.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Govern the classification version life cycle and correspondence tables | Classification version and correspondence register | DLM-9 Manage reference and master data | SAF-P09 |
| Verify metadata completeness for all standardised datasets | Metadata quality report | OVA-2 Metadata Management | SAF-P09 |
| Maintain the concept system, code lists, and reference data | Reference data maintenance log | DLM-9 Manage reference and master data; OVA-2 Metadata Management | CSDA Metadata Management |
| Track metadata lineage from raw through standardisation to the standardised state | Metadata lineage audit | DLM-8 Monitor data quality, lineage and use | CSDA Traceability |
| Reconcile metadata across systems | Catalogue-artefact reconciliation | OVA-2 Metadata Management | SAF-P09 |

|**PLACEHOLDER: VS-02 management feedback loop: data and paradata from Execution flowing through monitoring (key performance indicators, throughput), standardisation quality (mapping coverage), classification and metadata lifecycle (versions, reference data), audit (lineage, privacy), and continuous improvement, with dashboards to the process owner, quality reports to the quality manager, compliance reports to VS-07, and updated rules and classifications back to Design**|
|---|

#### Metadata per process type

Metadata is produced in every process type, not only in Design. The table shows the data metadata each process type of VS-02 contributes; the paradata are listed in [Standard activities in every value stream](#standard-vs-activities). In Execution, VS-02 also records the mapping coverage, the count of unmatched values, and the engine and classification versions as paradata, and Design keeps a classification version policy.

| Process type | Data metadata produced |
|---|---|
| Design | Target data models, classification schemes, code lists, source-to-target mapping rules, conformance criteria, harmonised definitions |
| Implementation | Mapping configurations, parameters of coding services and validation rules, catalogue templates |
| Execution | Per dataset: source-to-target mappings, applied classification versions, mapping and format-coercion lineage, conformance scores, profiling statistics |
| Management | Conformance scores, classification quality assessments, coverage reports, lineage assessments, trend analyses |

|**PLACEHOLDER: VS-02 business object lifecycle: design artefacts (target model, classification strategy, harmonisation, conformance, and privacy design) govern implementation assets (mapping and format coercion, mapping services, conformance pipeline, catalogue configuration), which produce the process that standardises Raw Data (#1) into Standardized Data (#2), generating mapping lineage, conformance, and audit records that management assesses and feeds back to design**|
|---|

### 5. Actors and roles

VS-02 works mostly inside the NSI. Its upstream partner is VS-01, which supplies Raw Data (#1) and its provenance metadata through the *Raw Data Registered* event. The table shows the actors and the reference roles involved. Specialised role names used in an NSI map onto these reference roles (see *Role names in the value streams*); for example, the data architect and the metadata architect of the original VS-02 description are both ROL-08 Metadata and data architect, and the system configurator is ROL-11 Platform engineer.

| Actor or role | ID | Process type | Responsibility in VS-02 |
|---|---|---|---|
| International statistical organisation (standards body) | ACT-07 | External | Maintains the classification and exchange standards the NSI conforms to, for example Eurostat and UNSD for NACE, ISCO, COICOP, and SDMX |
| Process owner | ROL-01 | Management | Accountable for the end-to-end performance of VS-02 |
| Data owner | ROL-02 | Management | Accountable for State #2: conformance and the application of the privacy design |
| Data steward | ROL-03 | Execution | Registers standardised datasets, manages metadata entries, and applies access controls |
| Data custodian | ROL-04 | Execution | Operates storage, access control, and retention; manages pseudonymisation keys separately from the data |
| Methodologist | ROL-07 | Design | Designs the mapping methodology and the cross-source harmonisation of definitions and metadata |
| Metadata and data architect | ROL-08 | Design | Designs the target data models, canonical schemas, structural conformance rules, harmonised definitions, semantic mappings, unit and period metadata, and the standardised metadata schema |
| Classification steward | ROL-09 | Design | Owns the classification strategy, code lists, and the one-to-one correspondence tables from source codes to standards |
| Data engineer | ROL-10 | Implementation | Builds and configures the profiling, mapping, and format-coercion components and the standardisation pipeline |
| Platform engineer | ROL-11 | Implementation | Configures classification services, reference data connections, and access controls |
| Test manager | ROL-12 | Implementation | Plans and carries out testing of the standardisation pipeline: technical, conformance, and integration tests |
| Data quality analyst | ROL-14 | Execution | Profiles data, assesses structural and semantic conformance, and logs unmapped values and exceptions |
| Quality manager | ROL-18 | Management | Monitors conformance key performance indicators, produces quality reports, and drives continuous improvement |
| Compliance officer | ROL-19 | Management | Ensures privacy (identifier removal) and standards compliance, and produces audit reports |

### 6. Capabilities, processes, and functions

#### Capability foundations

The table shows which capabilities from the SAF capability model VS-02 relies on, and what role they play. NSIs can use it to map the value stream to their own organisation.

| Capability group | Capabilities | Role in VS-02 |
|---|---|---|
| 1.1 Statistical design and build | 1.1.2 Design statistics product, 1.1.3 Build statistics product | Design the target data models and classification strategies, and build the standardisation pipeline |
| 1.3 Processing | 1.3.1 Data standardisation | Standardise formats, category codes, linkage keys, and the recording of units without loss of content, directly after receipt of raw data |
| 2.1 Data management | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management, 2.1.4 Statistical register management | Manage data and metadata through standardisation, harmonise semantics, assess conformance quality, align with reference registers |
| 3.2 Computerisation and automation | 3.2.1 Application development, 3.2.2 Functional management | Build and maintain mapping engines, coding services, and conformance validation pipelines |
| 3.3 Security and privacy | 3.3.1 Privacy management, 3.3.2 Security planning, 3.3.4 Logical identity and access control | Remove or pseudonymise direct identifiers and build security into the standardisation processes |
| 4.1 Governance | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improvement management, 4.1.5 Accountability | Govern the domain, steward classification standards, plan improvements, report on compliance |

#### Stages, processes, and functions

The table shows which SAF business processes realise each stage of VS-02 and which business functions they mainly use.

| Stage | Realised by processes | Main functions |
|---|---|---|
| VS-02.1 Profile and Assess Data Structure | PRD-5.3 Review and validate | FUN-3.3 Process statistical data |
| VS-02.2 Apply Standard Classifications and Formats | PRD-5.2 Classify and code; DLM-9 Manage reference and master data | FUN-3.3 Process statistical data; FUN-7.4 Manage reference and master data |
| VS-02.3 Align Metadata and Semantics | OVA-2 Metadata Management | FUN-7.2 Manage metadata |
| VS-02.4 Validate Structural and Semantic Conformance | PRD-5.3 Review and validate; DLM-2 Promote data through a quality gate | FUN-3.3 Process statistical data; FUN-7.3 Manage data lifecycle and storage |
| VS-02.5 Register Standardized Artefacts | DLM-3 Register and catalogue data; DLM-4 Classify and protect data; DLM-5 Store and version data | FUN-7.2 Manage metadata; FUN-7.3 Manage data lifecycle and storage; FUN-7.5 Protect data |

|**PLACEHOLDER: ArchiMate view VS-02 (b) stages realised by processes and functions**|
|---|

#### Framework mappings

This reference table maps each process type of VS-02 to the SAF business processes, the international frameworks (GSBPM, GAMSO, CSDA), and the SAF capability model. It is intended for architects and auditors; the rest of this section does not depend on it.

| Process type | SAF business processes | GSBPM | GAMSO | CSDA | SAF capabilities |
|---|---|---|---|---|---|
| Design | PRD-2.2, PRD-2.5, DLM-1, DLM-2, DLM-4, DLM-9, OVA-1, OVA-2, OVA-4 | Phase 2 Design (2.2, 2.5) | Production (design activities), Capability Management | Data Governance, Metadata Management, Reference and Master Data | 1.1.2 Design statistics product, 2.1.2 Metadata management, 2.1.4 Statistical register management |
| Implementation | PRD-3.2, PRD-3.4 to PRD-3.7, DLM-3, DLM-4, DLM-9, OVA-2 | Phase 3 Build (3.2, 3.4 to 3.7) | Capability Management | Data Integration (set-up), Data Governance (configuration) | 1.1.3 Build statistics product, 3.2.1 Application development, 3.2.2 Functional management |
| Execution | PRD-5.1 (key alignment only), PRD-5.2, PRD-5.3, DLM-2 to DLM-5, DLM-9, OVA-2, OVA-4 | Phase 5 Process (5.1 Integrate data, key alignment only; 5.2 Classify and code; 5.3 Review and validate, structural checks only) | Production (execution) | Data Integration (execution) | 1.3.1 Data standardisation, 2.1.2 Metadata management, 2.1.4 Statistical register management |
| Management | OVA-1, OVA-2, OVA-4, DLM-8, DLM-9, PRD-8.1 to PRD-8.3 | Phase 8 Evaluate; overarching Quality Management and Metadata Management | Corporate Support (Quality, Data, and Metadata Management), Capability Management (improvement) | Data Quality, Data Governance, Traceability | 2.1.3 Statistical quality management, 4.1.4 Improvement management, 4.1.5 Accountability |

### 7. Principles

The following principles govern VS-02 most directly.

| Principle | Statement | Application in VS-02 |
|---|---|---|
| SAF-P01 | Actively participate in open-source communities to maintain collective control over statistical processes | Classification, coding, and mapping tooling, such as SDMX libraries or coding engines, is built on open source developed with other NSIs, and the NSI contributes back. This keeps collective control over critical standardisation capabilities instead of depending on vendors. |
| SAF-P07 | Implement loosely coupled processes and systems | Standardisation is independent from upstream acquisition and downstream editing. Standardized Data (State #2) is the decoupling interface: downstream consumers use standardised, classified data without knowing the original source structure. |
| SAF-P08 | Data is shared property | Standardised data, once registered, is available to all authorised consumers. Standardisation is not repeated for each statistical product when the same standardised asset can serve several purposes. |
| SAF-P09 | No data without metadata and classification | Standardisation is where classification is applied as a first-class activity. Every standardised dataset carries source-to-target mappings, classification versions, harmonised definitions, units, and a classification for availability, integrity, and confidentiality. The principle does not require raw inputs to arrive already classified; it requires that data handed over from State #2 onward carries the required metadata and classification. VS-02 is the principal point where this obligation is fulfilled. |
| SAF-P10 | Security by design | Access controls, integrity verification, and audit logging are built into the standardisation pipeline from the start, so that every mapping and format-coercion operation is traceable and tamper-evident. |
| SAF-P11 | Privacy by design | Direct identifiers are removed or pseudonymised during standardisation, at the transition from State #1 to State #2, applying data minimisation and purpose limitation by design instead of adding privacy after data is processed. |

::: {.callout-note title="Principles that apply across the process types"}
SAF-P09 is the defining principle of VS-02 and applies to all four process types: Design defines the target classifications and mappings, Execution applies and captures them, and Management assesses classification quality and closes remaining gaps. SAF-P11 applies to *Design Standardisation Registration and Privacy Framework*, to *Build Conformance Validation Pipelines and Metadata Registration*, and to VS-02.5, where the removal or pseudonymisation of direct identifiers is confirmed. SAF-P07 governs both the intake of State #1 from VS-01 and the handover of State #2 to VS-03.
:::

### 8. Interfaces, services, and events

**Boundary interfaces**

VS-02 has two boundary interfaces: intake from VS-01, and handover to VS-03.

| Boundary | Handed over | Required metadata | Trigger | Responsibility transfer |
|---|---|---|---|---|
| VS-01 → VS-02 (intake) | Registered raw data version (#1) | Minimum metadata set of State #1: provenance, source, collection method, receipt timestamp, file hash, agreement reference, classification | *Raw Data Registered* | VS-01 keeps custody of the raw artefact; VS-02 takes responsibility for standardisation on receipt of the event |
| VS-02 → VS-03 (handover) | Registered standardised data version (#2) | Minimum metadata set of State #2: mapping lineage, classification versions, recorded unit, currency, and reference-period bases, list of unmapped and uncoded values for VS-03 to code, definition-difference records, conformance assessment, pseudonymisation record, classification | *Standardized Data Registered* | VS-02 keeps custody of the standardised artefact; VS-03 takes responsibility for editing and enrichment, including any value conversion, interpretive coding, and reconciliation, on receipt of the event |

**Business services**

| Service | Offered to | Realised in | Interfaces |
|---|---|---|---|
| Standardisation service | Raw data consumers, standardisation teams | VS-02.1 Profile and Assess Data Structure; VS-02.2 Apply Standard Classifications and Formats | Event subscription (*Raw Data Registered*) |
| Classification mapping service | Standardisation teams, methodologists, other domains that need code mapping | VS-02.2 Apply Standard Classifications and Formats | Mapping interface from source code to standard code through deterministic correspondence, correspondence table lookup, code list exchange compliant with SDMX |
| Semantic harmonisation service | Metadata architects, downstream analysts | VS-02.3 Align Metadata and Semantics | Concept links and harmonised metadata in the catalogue |
| Conformance validation service | Process owners, quality managers | VS-02.4 Validate Structural and Semantic Conformance | Conformance assessment and audit trail |
| Standardised data provisioning service | VS-03 Data Editing and Enrichment, data analysts, other domains | VS-02.5 Register Standardized Artefacts | Event notification (*Standardized Data Registered*) and a catalogue query interface to find and access standardised datasets and their lineage |
| Classification catalogue service | All data consumers in the NSI | Management sub-process *Manage Classification and Metadata Lifecycle* | Search and browse interface for classifications, code lists, and concept definitions, with metadata exchange compliant with SDMX |
| Design and methodology service | Methodologists, data architects, classification stewards | All Design sub-processes of VS-02 | Design documents, methodology advice |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Design artefacts published* | Start of Implementation after a design change |
| *Pipeline production-ready* | End of Implementation; Execution can start |
| *Raw Data Registered* | Start of VS-02.1 for that raw data version |
| *Standardisation Conformed* / *Standardisation Non-Conformant* | Outcome of VS-02.4; non-conformance starts re-mapping, routing of unmapped values to VS-03, or conditional acceptance |
| *Standardized Data Registered* | Completion of VS-02.5; triggers VS-03 |
| *Improvement recommendations issued* | Input for Design from *Continuous Improvement* |

|**PLACEHOLDER: VS-02 event choreography between VS-01, NSI teams, and process management across Design, Implementation, Execution (raw data registered, profiling, one-to-one mapping and format coercion with unit and period metadata, conformance passed or failed, registration or re-mapping and routing to VS-03), and Management (key performance indicators, mapping quality, compliance, improvement recommendations)**|
|---|

**Interaction with the supporting value streams**

| Value stream | Provides to VS-02 | Receives from VS-02 |
|---|---|---|
| VS-07 Governance and Compliance | Privacy and security policy, data and metadata governance | Audit trails of mapping lineage and pseudonymisation, privacy and standards compliance reports |
| VS-08 Innovation and Methodological Development | New mapping and classification techniques | Improvement needs; access to #2 for exploration under specific authorisation |
| VS-09 Infrastructure and Platform Enablement | Computing and orchestration for processing large datasets, storage, catalogue, event interfaces | Capacity and processing-window requirements |

### 9. Key performance indicators

The key performance indicators are collected per production cycle in *Monitor Process Performance*. They feed the dashboard that the process owner reviews.

| KPI | Description | Measurement |
|---|---|---|
| Mapping coverage | Share of source codes mapped one-to-one to a valid standard code | Per dataset, per classification |
| Unmapped-value rate | Share of values without a correspondence, routed to VS-03 | Per source, per cycle |
| Conformance pass rate | Share of datasets passing conformance on the first run | Per source, per cycle |
| Format-conformance rate | Share of records conforming to the target structure and format | Per dataset, per cycle |
| Processing time | Time from raw data registration to standardised registration | Per dataset, per cycle |
| Re-mapping rate | Frequency of datasets returned for re-mapping or design change | Per source, per cycle |

### 10. Examples

**Labour Force Survey.** The labour statistics team designs deterministic correspondence tables: source education codes map one-to-one to ISCED-2011, and source region codes map to NUTS-3. In each cycle the XML returns are coerced to the target schema and mapped through these tables. The 42,000 free-text occupation strings are not coded in VS-02. They are flagged and handed to VS-03, where occupation is coded to ISCO-08. No response value is altered; values are only re-expressed in standard codes where a deterministic correspondence exists.

**Tax register intake.** The quarterly corporate tax file, registered by VS-01, is profiled on arrival: 47 fields, the corporate identifier present at 99.8% coverage, economic activity supplied as the internal code of the tax authority, which has a maintained correspondence to NACE, and turnover in thousands of euro. The structure-gap assessment identifies the activity-code mapping and the format coercion of the XML as the VS-02 work. It records that the unit basis of turnover ("thousands of EUR") travels as metadata, and that conversion to a common unit is done in VS-03.

**Multi-source business statistics.** The business statistics data model uses the statistical business register identifier as the canonical linkage key, expresses economic activity in NACE Rev. 2 through a maintained correspondence table, and requires each turnover figure to carry its currency and reference-period basis as metadata. Survey returns, VAT register data, and structural business statistics are all aligned to this target schema. When turnover arrives from the structural business survey, the VAT register, and a commercial dataset, VS-02 links each turnover variable to the canonical concept and records that the VAT register reports on a fiscal-year basis and the survey on a calendar-year basis. The values are not adjusted to a common basis; the alignment is done in VS-03, so the difference stays transparent and the original values intact.

**Web price data.** A component coerces heterogeneous retailer price feeds into the canonical price record by reshaping fields and casting types. It records the currency, the unit (for example price per kilogram), and the scrape timestamp of each item as metadata, and stores prices exactly as received. Lineage links every standardised record to the exact raw scrape record. In conformance validation, all 11,875 records of a daily dataset conform structurally, every product whose source code has a COICOP correspondence is mapped, and the record count and observed price points match the raw scrape exactly. Products without such a code are flagged for VS-03, which also converts currencies and units to a common basis. The result is *Standardisation Conformed*, logged with rule version, engine version, and operator ID.

| **Toolkit:** SAF-TK-V02 VS-02 maturity checklist and scenarios |
|---|



## VS-03 Data Editing and Enrichment

### 1. Purpose and value created

VS-03 is where the quality of the data is actively improved. Standardised data is rarely clean: it contains errors, inconsistencies, gaps, and values that are not yet coded. VS-03 detects these problems, corrects them, fills the gaps, and derives the additional variables that analysis needs. It is the only value stream that deliberately changes values. What makes that safe is full traceability: every change is recorded against its original value, and a reproducible, versioned dataset is produced. The value created is **data reliability and analytical readiness**. The output is Processed Data: reliable, complete microdata that estimation and modelling can build on.

VS-03 improves the quality of microdata. It does not produce estimates or aggregates: estimation, weighting, aggregation, and statistical modelling belong to VS-04 Estimation, Analysis and Statistical Modeling.

VS-03 corresponds to the business domain **Editing, derivation, and non-response correction** (see *Steady-State Architecture, Business domains*). This section describes the business layer of that domain for all four process types: Design, Implementation, Execution, and Management.

::: {.callout-note title="Signature discipline: full traceability"}
Unlike VS-02, which never alters a value, VS-03 deliberately changes values to improve quality. Every edit, imputation, and derivation is rule-based, documented with a reason, attributable (who, which rule, when), and reversible. The original value is preserved beside the processed value, imputed values are flagged, and every version is reproducible. The invariant is *no undocumented or irreversible change*.
:::

|**PLACEHOLDER: ArchiMate view VS-03 (a) value stream and capabilities**|
|---|

<br>

### 2. Position and state transition

VS-03 is the third primary value stream. It receives Standardized Data from VS-02 and turns it into trustworthy, analytically sound input for estimation and modelling.

VS-03 takes data from State #2 to State #3. Before VS-03, the data is structurally aligned and coded to standards, with its values unchanged. After VS-03, its content has been validated, corrected, completed, and enriched, integrated with other datasets where applicable, with new derived variables and fully documented lineage. The quality gate, the minimum metadata set, and the protection of State #3 are described in *State #3: Processed Data* and are not repeated here. Where a product skips State #2, VS-03 consumes State #1 directly.

VS-02 deliberately leaves all value-changing work to VS-03. Together with the standardised data, VS-03 receives the metadata VS-02 attached: the recorded unit, currency, and reference-period bases, the records of definition differences, and the list of unmapped or uncoded values. VS-03 then performs the operations VS-02 deferred: interpretive coding of free text and value reconciliation across sources (VS-03.2), and unit and currency conversion, reference-period alignment, and derivation (VS-03.4).

| From | To | Gate | Event out |
|---|---|---|---|
| #2 Standardized Data | #3 Processed Data | Gate of State #3 (rule conformance, edit lineage, imputation flags, coding, conversion and reconciliation, linkage quality, derived variables, quality improvement, disclosure risk, reproducibility) | *Processed Data Registered* |

|**PLACEHOLDER: ArchiMate view VS-03 (c) state handover and events: Standardized Data (#2) from VS-02, the editing and enrichment service at the domain boundary (error detection, correction, imputation, derivation, quality versioning), Processed Data (#3) handed to VS-04**|
|---|

<br>

### 3. Stages

The stages describe the value that VS-03 adds in every production cycle. Together they form the execution process type of VS-03. In a mature steady state, the rules and methods have been designed and built in advance (see attribute 4). Execution then focuses on running the cycle, applying edits, imputations, and derivations, and capturing the full edit lineage so that every value change is documented and reversible.

| Stage | Name | Value added |
|---|---|---|
| VS-03.1 | Conduct Error Detection and Quality Diagnostics | Errors, duplicates, gaps, and outliers are known |
| VS-03.2 | Perform Data Editing and Correction | Incorrect values are corrected |
| VS-03.3 | Impute Missing or Non-Response Data | Missing values are filled with documented methods |
| VS-03.4 | Derive Additional Variables and Indicators | Data describes reality better than the source alone |
| VS-03.5 | Perform Quality Evaluation and Versioning | Quality is documented, and processed microdata is registered (State #3) |

Each stage below is described with its activities. The column *SAF process* shows the business process from *Business Processes* that the activity belongs to. The column *Other reference* shows the principles, capabilities, or external frameworks that the activity applies.

<br>

#### VS-03.1 Conduct Error Detection and Quality Diagnostics

**Value created:** *A clear, prioritised picture of where the data is wrong, incomplete, or inconsistent.*

The stage starts when the *Standardized Data Registered* event is received from VS-02. The designed detection rules run on the incoming dataset: consistency, range, outlier, duplicate, and completeness checks. Selective-editing scores are computed, so that effort goes to the problems that matter for the results. The outcome is a diagnostic report that gives the location and type of each suspected error, its severity, and its disposition: auto-correct, flag for review, or accept. No values are changed yet. This stage diagnoses; correction happens in VS-03.2.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Run consistency, range, outlier, duplicate, and completeness checks | Error diagnostic report | PRD-5.3 Review and validate | 1.3.3 Check content |
| Compute selective-editing scores and prioritise errors | Prioritised error list | PRD-5.3 Review and validate | |
| Assign a disposition: auto-correct, flag for review, or accept | Disposition list | PRD-5.3 Review and validate | |
| Log all detected issues to the edit audit trail | Audit trail entries | OVA-4 Process Data Management | SAF-P10 |

<br>

#### VS-03.2 Perform Data Editing and Correction

**Value created:** *Errors corrected and inconsistencies resolved, with every change documented and reversible.*

Auto-correction rules are applied to the records that the design earmarked for automatic treatment. Flagged records go to subject-matter statisticians, who adjudicate and correct them. For every change, the editing engine records the original value, the rule or decision applied, a reason code, the actor, and a timestamp. The edit is therefore fully attributable and reversible. This stage also carries out the interpretive coding handed over from VS-02, for example coding free-text occupation to ISCO, the international occupation classification, with low-confidence cases reviewed. Where integrated sources disagree on a value, the designed value-reconciliation rules are applied. No edit may leave a record that violates the validation rules.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Apply auto-corrections according to the designed rules | Corrected records | PRD-5.4 Edit and impute | 1.3.4 Adjusting and imputing |
| Route flagged records to subject-matter review and adjudication | Adjudicated corrections | PRD-5.4 Edit and impute | |
| Code free-text values interpretively (for example occupation to ISCO) | Coded values, confidence and review records | PRD-5.2 Classify and code | Handed over from VS-02 |
| Apply value-reconciliation rules across integrated sources | Reconciled values | PRD-5.4 Edit and impute | |
| Record original value, rule, reason, actor, and time for every change | Edit lineage records | PRD-5.4 Edit and impute; OVA-4 Process Data Management | SAF-P10 |

<br>

|**PLACEHOLDER: VS-03 editing and correction architecture: detected issues from VS-03.1 split into three paths (auto-correctable low-impact values to automatic correction, high-impact flagged values to manual adjudication, free-text values from the VS-02 handover to interpretive coding), all producing edited values whose original value, rule, and reason are written to the edit audit trail**|
|---|

<br>

#### VS-03.3 Impute Missing or Non-Response Data

**Value created:** *Complete datasets where gaps are filled with the best available estimate, clearly flagged as imputed.*

Missing and non-response values are filled with the designed imputation methods. The method is chosen per variable and missingness pattern: deterministic, donor (hot-deck or nearest-neighbor), model-based, or external-source. Acceptance constraints make sure that imputed values still satisfy the edit rules. Every imputed value receives an imputation flag and a method code, so that imputed and observed values are always distinguishable downstream, and the imputation inputs are recorded in the lineage. Imputed values never overwrite observed values; they fill only genuine gaps.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Select and apply the designed imputation method per variable and missingness pattern | Imputed values | PRD-5.4 Edit and impute | 1.3.4 Adjusting and imputing |
| Enforce acceptance constraints: imputed values satisfy the edit rules | Constraint-checked imputations | PRD-5.4 Edit and impute | |
| Flag every imputed value with a method code and record its inputs | Imputation flags and lineage | PRD-5.4 Edit and impute | SAF-P09 |
| Log imputation actions to the edit audit trail | Audit trail entries | OVA-4 Process Data Management | SAF-P10 |

<br>

#### VS-03.4 Derive Additional Variables and Indicators

**Value created:** *Enriched datasets carrying the analytical variables downstream production needs.*

The derived variables and indicators specified in design are calculated. Each one is computed from its documented formula and inputs, receives its metadata and classification, and is recorded with lineage to its inputs. This stage also computes the unit, currency, and reference-period conversions from the bases VS-02 recorded as metadata, for example converting turnover from thousands to units, or aligning a fiscal-year figure to the calendar year. Each conversion is documented with its rule and rate, so the original value remains recoverable. Where datasets are to be combined, records are linked on the designed keys, and the lineage records the linkage.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Calculate derived variables and indicators from the designed formulas | Derived variables and their metadata | PRD-5.5 Derive new variables and units | 1.3.2 Deriving variables and units |
| Compute unit, currency, and reference-period conversions from the VS-02 bases | Converted values, conversion lineage | PRD-5.5 Derive new variables and units | |
| Integrate or link datasets on the designed keys, where applicable | Integrated dataset, linkage lineage | PRD-5.1 Integrate data | 2.1.4 Statistical register management; SAF-P11 |
| Record derivation and conversion formulas and inputs as lineage | Derivation lineage | PRD-5.5 Derive new variables and units; OVA-2 Metadata Management | SAF-P09 |

<br>

#### VS-03.5 Perform Quality Evaluation and Versioning

**Value created:** *A trustworthy, traceable Processed Data version with measured quality improvement.*

This stage evaluates the result and produces the official quality version. Quality is evaluated against the State #2 baseline: improvement in completeness and accuracy, edit and imputation rates, and the number of derived variables added. The edit lineage is verified to be complete, with every change attributable and reversible. A persistent, immutable quality version of the Processed Data is created with a unique identifier. It is registered in the catalogue with its full lineage, imputation flags, derived-variable metadata, and quality assessment, in line with SAF-P09, and access permissions are applied in line with SAF-P10. If the quality is insufficient, the data goes back for re-editing or re-imputation after review. The stage ends by publishing the *Processed Data Registered* event, which tells VS-04 that new processed data is available for estimation and analysis.

**Output:** **Processed Data (State #3)**, the official handover artefact to the rest of the statistical value chain. Its structure and minimum metadata set are described in *State #3: Processed Data*.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Evaluate quality improvement against the State #2 baseline | Quality evaluation report | PRD-5.8 Finalise data files; DLM-2 Promote data through a quality gate | 2.1.3 Statistical quality management |
| Verify that the edit lineage is complete and reversible | Lineage completeness check | DLM-2 Promote data through a quality gate | SAF-P10 |
| Create an immutable, identified quality version of Processed Data | Versioned Processed Data | PRD-5.8 Finalise data files; DLM-5 Store and version data | CSDA Traceability |
| Register metadata: edit lineage, imputation flags, derived-variable metadata, quality assessment | Catalogue registration | DLM-3 Register and catalogue data; OVA-2 Metadata Management | SAF-P09 |
| Apply access permissions to the processed microdata | Access-controlled dataset | DLM-4 Classify and protect data | SAF-P10, SAF-P11 |
| Publish the *Processed Data Registered* event to notify VS-04 | Event notification | DLM-3 Register and catalogue data | SAF-P07 |

### 4. The four process types

The sub-processes below are specific to VS-03. Each refines one or more SAF business processes, listed as *Refines*, which keeps it traceable to *Business Processes*. Sub-processes marked *(standard)* work as described in [Standard activities in every value stream](#standard-vs-activities); only the VS-03 specifics are listed.

#### Design: provides metadata

Without well-designed rules and methods, editing becomes ad hoc and untraceable, and management has no baseline to measure quality improvement against.

| Design sub-process | Refines | Main outputs |
|---|---|---|
| Design Error-Detection and Validation Rules | PRD-2.5 Design processing and analysis | Validation rule set, selective-editing strategy, error taxonomy and disposition policy |
| Design Imputation Methodology | PRD-2.5 Design processing and analysis | Imputation methodology, donor and matching specification, imputation flagging standard |
| Design Derivation and Coding Specifications | PRD-2.2 Design variables; PRD-2.5 Design processing and analysis; DLM-9 Manage reference and master data | Derived-variable catalogue, coding methodology, conversion specification |
| Design Integration and Linkage Rules | PRD-2.5 Design processing and analysis; DLM-4 Classify and protect data | Linkage rule set, reconciliation policy, disclosure-risk assessment design |
| Design Quality Evaluation, Versioning, and Audit Framework | OVA-1 Quality Management; DLM-1 Plan and design data assets; DLM-4 Classify and protect data; OVA-4 Process Data Management | Quality criteria, edit audit-trail specification, versioning policy, access control and reproducibility design |

##### Design Error-Detection and Validation Rules

*Refines:* PRD-2.5 Design processing and analysis.

The starting point of editing is defining what counts as an error. This sub-process sets the validation and error-detection rules: logical and consistency checks (between fields, within a record, and against reference data), range and outlier-detection rules, duplicate-detection rules, and completeness checks. A selective-editing strategy concentrates effort on errors that materially affect results. Score functions and thresholds decide which records are auto-corrected, which are flagged for manual review, and which are left as they are. The team also designs the error taxonomy and the disposition options: auto-correct, flag for review, or accept.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define logical and consistency, range, and outlier-detection rules | Validation rule set | PRD-2.5 Design processing and analysis | 1.3.3 Check content |
| Define duplicate- and completeness-detection rules | Validation rule set | PRD-2.5 Design processing and analysis | |
| Design selective-editing score functions and review thresholds | Selective-editing strategy | PRD-2.5 Design processing and analysis | |
| Define the error taxonomy and disposition options (auto-correct, review, accept) | Error taxonomy and disposition policy | PRD-2.5 Design processing and analysis | |

##### Design Imputation Methodology

*Refines:* PRD-2.5 Design processing and analysis.

This sub-process designs how missing and non-response values are completed. The team selects imputation methods per variable and missingness type: deterministic or rule-based imputation, donor methods (hot-deck, nearest-neighbor), model-based methods (regression, ratio), and the use of external or administrative sources. It defines donor pools, matching variables, and acceptance constraints, such as the edit rules an imputed value must still satisfy. The design mandates an imputation flag on every imputed value, so that imputed and observed values are always distinguishable downstream.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Select imputation methods per variable and missingness type | Imputation methodology document | PRD-2.5 Design processing and analysis | 1.3.4 Adjusting and imputing |
| Define donor pools, matching variables, and acceptance constraints | Donor and matching specification | PRD-2.5 Design processing and analysis | |
| Specify the use of external or administrative sources for imputation | External-source imputation rules | PRD-2.5 Design processing and analysis | |
| Mandate imputation flags and method codes on every imputed value | Imputation flagging standard | PRD-2.5 Design processing and analysis | SAF-P09 |

##### Design Derivation and Coding Specifications

*Refines:* PRD-2.2 Design variables; PRD-2.5 Design processing and analysis; DLM-9 Manage reference and master data.

This sub-process specifies the new variables and indicators to be derived, and the interpretive coding handed over from VS-02. Each derived variable is defined by a formula, its input variables, its unit, and the classification it belongs to, in line with SAF-P09. For interpretive coding, the design specifies the coding scheme (for example ISCO for occupation free text, COICOP for product names), the coding approach (manual, computer-assisted, or machine-learning-assisted with confidence thresholds), and the review workflow for low-confidence cases. This is the work VS-02 deferred because it requires judgment. The team also designs how unit, currency, and reference-period conversions are computed from the bases VS-02 recorded as metadata.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Specify derived variables and indicators: formulas, inputs, units, classification | Derived-variable catalogue | PRD-2.2 Design variables | 1.3.2 Deriving variables and units |
| Design the interpretive coding approach and review workflow (free text to standard codes) | Coding methodology | PRD-2.5 Design processing and analysis; DLM-9 Manage reference and master data | |
| Design unit, currency, and reference-period conversion rules from the VS-02 metadata | Conversion specification | PRD-2.5 Design processing and analysis | |
| Define metadata and classification for every derived variable | Derived-variable metadata standard | PRD-2.2 Design variables | SAF-P09 |

##### Design Integration and Linkage Rules

*Refines:* PRD-2.5 Design processing and analysis; DLM-4 Classify and protect data.

Where Processed Data is to be integrated with other datasets, this sub-process designs the linkage. It specifies the linkage keys, for example the statistical register identifier aligned in VS-02, and deterministic and probabilistic matching rules. It sets conflict-resolution rules for linked sources that disagree on a value, and the value-reconciliation policy for the definition differences VS-02 recorded as metadata. Linkage can increase the disclosure risk of pseudonymised microdata, so a disclosure-risk assessment is designed in line with SAF-P11.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define linkage keys and deterministic and probabilistic matching rules | Linkage rule set | PRD-2.5 Design processing and analysis | GSBPM 5.1 |
| Design conflict-resolution and value-reconciliation rules across sources | Reconciliation policy | PRD-2.5 Design processing and analysis | |
| Design the disclosure-risk assessment for integration and enrichment | Disclosure-risk assessment design | DLM-4 Classify and protect data | SAF-P11; 3.3.1 Privacy management |
| Define lineage requirements for linked and reconciled values | Linkage lineage specification | PRD-2.5 Design processing and analysis | CSDA Traceability |

##### Design Quality Evaluation, Versioning, and Audit Framework

*Refines:* OVA-1 Quality Management; DLM-1 Plan and design data assets; DLM-4 Classify and protect data; OVA-4 Process Data Management.

The last design sub-process makes sure that quality is measured and that every change is traceable. It defines the quality-evaluation criteria: improvement of completeness and accuracy against the State #2 baseline. It sets the edit audit-trail requirements: original value, rule applied, reason, actor, and timestamp for every change. The versioning policy defines how versions are identified, what triggers a new version, and immutability and retention. Role-based access control for processed microdata is designed in line with SAF-P10. Reproducibility is designed in: a quality version must be regenerable from the standardised input plus the recorded rules.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define quality-evaluation criteria against the State #2 baseline | Quality criteria document | OVA-1 Quality Management | GAMSO Quality Management |
| Define edit audit-trail requirements (original value, rule, reason, actor, time) | Edit audit-trail specification | OVA-4 Process Data Management | SAF-P10 |
| Define the versioning policy: identity, triggers, immutability, retention | Versioning policy | DLM-1 Plan and design data assets | CSDA Traceability |
| Design role-based access control and reproducibility for processed microdata | Access control and reproducibility design | DLM-1 Plan and design data assets; DLM-4 Classify and protect data | SAF-P10; 3.3.4 Logical identity and access control |

|**PLACEHOLDER: VS-03 design process decomposition: inputs (State #2 schema and metadata, methodology set for editing, imputation, and derivation, framework standards, privacy and disclosure requirements feeding the linkage design), the five design sub-processes in order, and the artefact each produces (validation rule set, imputation methodology, derivation and coding specifications, linkage and reconciliation rules, versioning and audit policy), which together govern Implementation, Execution, and Management**|
|---|

#### Implementation: provides the execution process

| Implementation sub-process | Refines | Main outputs |
|---|---|---|
| Build Error-Detection and Editing Engines | PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows | Detection module, configured editing engine, edit audit-trail capture |
| Configure Imputation and Coding Services | PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows | Imputation services, coding service and review queue, conversion service |
| Build Derivation, Integration, and Versioning Pipelines | PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows; DLM-3 Register and catalogue data; DLM-5 Store and version data | Derivation pipeline, integration component, versioning store, events |
| Test and Validate the Pipeline *(standard)* | PRD-3.5 Test production systems; PRD-3.6 Test statistical business process; PRD-3.7 Finalise production systems | Test reports covering detectors, editing engine, imputation and coding services, derivation calculators, integration component, and versioning store; edit-impact test (edits and imputations move quality indicators in the intended direction, without over-editing); reproducibility test (a quality version is regenerated identically from the standardised input plus the recorded rules); imputation evaluated against a holdout or known-value sample |

##### Build Error-Detection and Editing Engines

*Refines:* PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows.

This sub-process turns the validation and editing rule designs into operational tools. Error-detection components run the designed consistency, range, outlier, duplicate, and completeness checks and compute the selective-editing scores. The editing engine applies auto-corrections according to the designed rules and routes flagged records to the review workflow. For every change it captures the original value, the rule applied, and a reason code. All editing logic is version-controlled in line with SAF-P10, so that any edit is reproducible and attributable.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Build error-detection components (consistency, range, outlier, duplicate, completeness) | Production-ready detection module | PRD-3.2 Reuse or build processing and analysis components | |
| Build or configure the editing engine (auto-correction and review routing) | Configured editing engine | PRD-3.2 Reuse or build processing and analysis components | |
| Configure edit-lineage capture (original value, rule, reason, actor) for every change | Edit audit-trail capture | PRD-3.4 Configure workflows | SAF-P10 |
| Version-control all editing logic | Versioned editing repository | PRD-3.2 Reuse or build processing and analysis components | SAF-P10 |

##### Configure Imputation and Coding Services

*Refines:* PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows.

The designed imputation and coding methodologies are translated into automated services. Imputation services are configured for each method (deterministic, donor, model-based, external-source). Donor pools and matching variables are loaded, acceptance constraints are enforced, and every imputed value is flagged with its method code. The interpretive coding service handed over from VS-02 is configured: computer-assisted or machine-learning-assisted coding of free-text values with the designed confidence thresholds, and a manual review workflow for low-confidence cases. Conversion routines are configured to compute unit, currency, and reference-period conversions from the bases VS-02 recorded.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Configure imputation services per method, with donor pools and constraints | Configured imputation services | PRD-3.2 Reuse or build processing and analysis components | |
| Enforce imputation flagging and method codes | Flagged imputation outputs | PRD-3.4 Configure workflows | SAF-P09 |
| Configure the interpretive coding service (free text to standard codes) with its review workflow | Coding service and review queue | PRD-3.2 Reuse or build processing and analysis components | |
| Configure unit, currency, and reference-period conversion routines | Conversion service | PRD-3.4 Configure workflows | |

##### Build Derivation, Integration, and Versioning Pipelines

*Refines:* PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows; DLM-3 Register and catalogue data; DLM-5 Store and version data.

This sub-process implements derivation, dataset integration, and quality versioning. Derived-variable calculators are built from the designed formulas and produce each derived variable with its metadata and classification. The integration component is configured with the designed keys and matching rules. It applies the conflict-resolution and value-reconciliation policy and captures linkage lineage. The versioning store makes each accepted Processed Data version immutable, identified, reproducible from inputs plus rules, and accompanied by its full edit lineage. Event notifications are configured, so that VS-04 is alerted when a quality version is registered.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Build derived-variable calculators from the designed formulas | Derivation pipeline | PRD-3.2 Reuse or build processing and analysis components | |
| Configure integration and linkage with conflict resolution and reconciliation | Integration component | PRD-3.2 Reuse or build processing and analysis components | |
| Build the versioning store (immutable, identified, reproducible) | Versioning store | DLM-5 Store and version data | CSDA Traceability |
| Configure the *Processed Data Registered* event for downstream consumers | Event publication | PRD-3.4 Configure workflows; DLM-3 Register and catalogue data | SAF-P07 |

|**PLACEHOLDER: VS-03 implementation pipeline: the five design artefacts feeding the three build sub-processes, followed by technical testing, edit-impact and reproducibility testing, and imputation evaluation, resulting in an operational editing pipeline and operational procedures**|
|---|

#### Execution: provides the statistical data

Execution runs the stages of VS-03 in every production cycle. The stages and their activities are described in attribute 3. A cycle starts when a new standardised version is registered. The stages then run in order. Execution applies the designed rules and methods as they are; a new rule, model, or coding scheme goes back to Design. Every cycle ends in one of two outcomes: the quality version is accepted and registered, or the quality is insufficient and records go back for re-editing or re-imputation after review.

| Aspect | VS-03 |
|---|---|
| Trigger | *Standardized Data Registered* (or *Raw Data Registered* where State #2 is skipped) |
| Cadence | Per production cycle, for each new standardised version |
| Performed by | ROL-14 Data quality analyst, ROL-15 Subject-matter statistician, ROL-09 Classification steward, ROL-03 Data steward |
| Input | Standardized Data (#2) with its unmapped values and recorded units and periods; production-ready editing pipeline |
| Output | Registered Processed Data quality version (#3) with its edit lineage |
| Control point | Gate of State #3 in VS-03.5 |
| Exception path | Insufficient quality: re-edit or re-impute after review; recurring problems or a need for new rules or models back to Design |

#### Management: provides quality reports

| Management sub-process | Refines | Main outputs |
|---|---|---|
| Monitor Process Performance *(standard)* | OVA-4 Process Data Management; PRD-8.1 Gather evaluation inputs | Process performance dashboard; throughput report against processing windows; paradata on rule and model versions and manual interventions |
| Assess Data Quality | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use | Quality improvement report, imputation quality report, consistency and over-editing report, trend analysis |
| Manage Methodology and Version Lifecycle | OVA-2 Metadata Management; OVA-5 Knowledge Management; DLM-5 Store and version data; DLM-8 Monitor data quality, lineage and use | Methodology version register, metadata quality report, version store audit, lineage audit |
| Audit and Compliance Reporting *(standard)* | OVA-1 Quality Management; OVA-4 Process Data Management; DLM-8 Monitor data quality, lineage and use | Edit audit summary showing every change attributable and reversible (original value, rule, reason, actor, time); disclosure-risk report confirming that linkage on pseudonymised microdata stays within the assessed re-identification risk (SAF-P11); methodology compliance report confirming that approved editing and imputation methods were applied (4.1.5 Accountability); security compliance report on access controls and integrity of the tamper-evident audit trail |
| Continuous Improvement *(standard)* | PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan | Improvement recommendations, for example refining edit rules that generate false positives, recalibrating imputation models, automating recurring manual edits, improving the coding service for free text, and tuning selective-editing thresholds to reduce over-editing; trends watched: error rates, over-editing, imputation quality, coding completion rate |

##### Assess Data Quality

*Refines:* OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use.

Beyond process performance, the quality improvement achieved is evaluated against the criteria set in *Design Quality Evaluation, Versioning, and Audit Framework*. Each processed dataset is assessed on several dimensions: accuracy improvement (error rates before and after editing), completeness improvement (missingness before and after imputation), imputation quality (against holdout or known values), consistency (no residual rule violations), and coherence of derived variables. Quality indicators are produced per dataset, per source, and per cycle. Trends are tracked to detect over-editing, deteriorating sources, or imputation models that need recalibration. This follows the Data Quality capability of CSDA and SAF capability 2.1.3 *Statistical quality management*.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Evaluate accuracy and completeness improvement against the baseline | Quality improvement report (per cycle) | OVA-1 Quality Management | 2.1.3 Statistical quality management |
| Assess imputation quality against holdout or known values | Imputation quality report | OVA-1 Quality Management | CSDA Data Quality |
| Check for residual rule violations and over-editing | Consistency and over-editing report | DLM-8 Monitor data quality, lineage and use | 2.1.3 Statistical quality management |
| Identify quality trends across sources, variables, and cycles | Quality trend analysis | DLM-8 Monitor data quality, lineage and use | 2.1.3 Statistical quality management |

##### Manage Methodology and Version Lifecycle

*Refines:* OVA-2 Metadata Management; OVA-5 Knowledge Management; DLM-5 Store and version data; DLM-8 Monitor data quality, lineage and use.

The editing methodology and the quality versions it produces must stay current, complete, and well governed. This sub-process governs the life cycle of editing rules, imputation models, and derivation specifications: it versions them, manages transitions, and retires obsolete rules. It verifies metadata completeness as a compliance check on SAF-P09: every processed dataset must carry full edit lineage, imputation flags, and derived-variable metadata. It governs the version store: retention, immutability, and reconciliation of catalogue entries with stored versions. Metadata lineage from the standardised state through editing to the processed state is tracked. As CSDA emphasises, complete, well-managed lineage is what makes edited data trustworthy and reusable.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Govern the life cycle and versions of editing rules, imputation models, and derivation specifications | Methodology version register | OVA-5 Knowledge Management; OVA-2 Metadata Management | SAF-P03 |
| Verify metadata completeness (edit lineage, imputation flags, derived-variable metadata) | Metadata quality report | OVA-2 Metadata Management | SAF-P09 |
| Govern the version store: retention, immutability, reconciliation with the catalogue | Version store audit | DLM-5 Store and version data | CSDA Traceability |
| Track metadata lineage from the standardised to the processed state | Metadata lineage audit | DLM-8 Monitor data quality, lineage and use | CSDA Traceability |

|**PLACEHOLDER: VS-03 management feedback loop: data and paradata from Execution flowing through the five management sub-processes (edit and imputation rates, quality improvement, rules and versions, edit auditability and privacy), with dashboards to the process owner, quality reports to the quality manager, compliance reports to VS-07, and improvement recommendations back to Design**|
|---|

#### Metadata per process type

In VS-03, metadata is what keeps value changes transparent: every edit, imputation, and derivation must be self-describing. The table shows the data metadata each process type of VS-03 contributes; the paradata are listed in [Standard activities in every value stream](#standard-vs-activities). VS-03 also records edit-impact test outcomes in Implementation, and edit and imputation rates, rule and model versions, and manual-override records in Execution, as paradata.

| Process type | Data metadata produced |
|---|---|
| Design | Editing and validation rule sets, imputation methodology, derivation formulas, integration and linkage rules, quality-version policy |
| Implementation | Engine configurations, rule parameters, imputation model parameters, derivation definitions, versioning templates |
| Execution | Per-record edit lineage (original value, rule, reason), imputation flags and methods, derived-variable formulas and inputs, quality-version identifiers |
| Management | Quality-improvement scores against the baseline, edit and imputation rate reports, lineage assessments, trend analyses |

|**PLACEHOLDER: VS-03 business object lifecycle: design artefacts (validation rules, imputation methodology, derivation and coding specifications, versioning and audit policy) govern implementation assets (editing and imputation engines, derivation pipeline, integration component, versioning store), which produce the process that edits and enriches Standardized Data (#2) into Processed Data (#3), generating edit lineage, imputation flags, and quality versions that management assesses and feeds back to design**|
|---|

### 5. Actors and roles

VS-03 is mostly internal: it receives its input from VS-02 and hands its output to VS-04, and both handovers are covered by the boundary interfaces in attribute 8. The table shows the actors and the reference roles involved. Specialised role names used in an NSI map onto these reference roles (see *Role names in the value streams*); for example, the editing methodologist and the imputation specialist in the original VS-03 description are both ROL-07 Methodologist, and the coding specialist is ROL-09 Classification steward. The design, build, and running of the editing process are often organised in the collaboration COL-05 *Statistical product team*.

| Actor or role | ID | Process type | Responsibility in VS-03 |
|---|---|---|---|
| International statistical organisation | ACT-07 | External | Acts as methodology authority: sets the editing, imputation, and derivation methods the NSI conforms to, for example Eurostat guidance |
| Process owner | ROL-01 | Management | Accountable for the end-to-end performance of VS-03 |
| Data owner | ROL-02 | Management | Accountable for State #3 and for the correct application of approved methods |
| Data steward | ROL-03 | Execution | Registers processed datasets and quality versions, manages metadata entries, applies access controls |
| Data custodian | ROL-04 | Execution | Operates storage of quality versions, access control, and retention; keeps pseudonymisation keys separate from the data |
| Statistical designer | ROL-06 | Design | As derivation designer: specifies derived variables and indicators, formulas, and required inputs |
| Methodologist | ROL-07 | Design | As editing methodologist: designs error-detection and editing rules, the selective-editing strategy, and quality criteria. As imputation specialist: designs imputation methodology, models, donor strategies, and imputation flags |
| Classification steward | ROL-09 | Execution | As coding specialist: performs interpretive coding of free-text values to standard classifications, handed over from VS-02 |
| Data engineer | ROL-10 | Implementation | Builds and configures the editing, imputation, derivation, and integration engines and the pipeline |
| Platform engineer | ROL-11 | Implementation | Configures editing services, connections to reference and donor data, and access controls |
| Test manager | ROL-12 | Implementation | Plans and carries out testing of the editing pipeline: technical, edit-impact, and reproducibility tests |
| Data quality analyst | ROL-14 | Execution | Runs error detection, evaluates quality improvement, and logs edit lineage and exceptions |
| Subject-matter statistician | ROL-15 | Execution | Reviews flagged records, adjudicates edits, and signs off domain-specific corrections |
| Quality manager | ROL-18 | Management | Monitors quality-improvement indicators, produces quality reports, and drives continuous improvement |
| Compliance officer | ROL-19 | Management | Ensures edit auditability and disclosure-risk compliance and produces audit reports |

### 6. Capabilities, processes, and functions

#### Capability foundations

The table shows which capabilities from the SAF capability model VS-03 relies on, and what role they play. NSIs can use it to map the value stream to their own organisation.

| Capability group | Capabilities | Role in VS-03 |
|---|---|---|
| 1.1 Statistical design and build | 1.1.2 Design statistics product, 1.1.3 Build statistics product | Design the editing and imputation methodology and the derivation specifications, and build the editing pipeline |
| 1.3 Processing | 1.3.2 Deriving variables and units, 1.3.3 Check content, 1.3.4 Adjusting and imputing | Detect errors, correct and impute values, and derive new variables |
| 2.1 Data management | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management, 2.1.4 Statistical register management | Manage data, edit metadata, and quality versions; assess quality improvement; integrate with statistical registers |
| 3.2 Computerisation and automation | 3.2.1 Application development, 3.2.2 Functional management | Build and maintain the editing, imputation, derivation, and integration engines |
| 3.3 Security and privacy | 3.3.1 Privacy management, 3.3.2 Security planning | Manage disclosure risk in enrichment and linkage, and secure the edit audit trail |
| 4.1 Governance | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improvement management, 4.1.5 Accountability | Govern the domain, steward the editing methodology, plan improvements, report on auditability and compliance |

#### Stages, processes, and functions

The table shows which SAF business processes realise each stage of VS-03 and which business functions they mainly use.

| Stage | Realised by processes | Main functions |
|---|---|---|
| VS-03.1 Conduct Error Detection and Quality Diagnostics | PRD-5.3 Review and validate | FUN-3.3 Process statistical data |
| VS-03.2 Perform Data Editing and Correction | PRD-5.2 Classify and code; PRD-5.4 Edit and impute | FUN-3.3 Process statistical data |
| VS-03.3 Impute Missing or Non-Response Data | PRD-5.4 Edit and impute | FUN-3.3 Process statistical data; FUN-4.1 Manage statistical and analytical methodology |
| VS-03.4 Derive Additional Variables and Indicators | PRD-5.1 Integrate data; PRD-5.5 Derive new variables and units | FUN-3.3 Process statistical data |
| VS-03.5 Perform Quality Evaluation and Versioning | PRD-5.8 Finalise data files; DLM-2 Promote data through a quality gate; DLM-3 Register and catalogue data | FUN-3.3 Process statistical data; FUN-5.2 Assure and review quality; FUN-7.3 Manage data lifecycle and storage |

|**PLACEHOLDER: ArchiMate view VS-03 (b) stages realised by processes and functions**|
|---|

#### Framework mappings

This reference table maps each process type of VS-03 to the SAF business processes, the international frameworks (GSBPM, GAMSO, CSDA), and the SAF capability model. It is intended for architects and auditors; the rest of this section does not depend on it.

| Process type | SAF business processes | GSBPM | GAMSO | CSDA | SAF capabilities |
|---|---|---|---|---|---|
| Design | PRD-2.2, PRD-2.5, DLM-1, DLM-4, DLM-9, OVA-1, OVA-4 | Phase 2 Design (2.2, 2.5) | Production (design activities), Capability Management | Data Governance, Metadata Management, Data Quality | 1.1.2 Design statistics product, 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| Implementation | PRD-3.2, PRD-3.4 to PRD-3.7, DLM-3, DLM-5 | Phase 3 Build (3.2, 3.4 to 3.7) | Capability Management | Data Processing (set-up), Data Governance (configuration) | 1.1.3 Build statistics product, 3.2.1 Application development, 3.2.2 Functional management |
| Execution | PRD-5.1 to PRD-5.5, PRD-5.8, DLM-2 to DLM-5, OVA-2, OVA-4 | Phase 5 Process (5.1 Integrate data, 5.2 Classify and code, 5.3 Review and validate, 5.4 Edit and impute, 5.5 Derive new variables and units, 5.8 Finalise data files) | Production (execution) | Data Processing (execution) | 1.3.2 Deriving variables and units, 1.3.3 Check content, 1.3.4 Adjusting and imputing, 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| Management | OVA-1, OVA-2, OVA-4, OVA-5, DLM-5, DLM-8, PRD-8.1 to PRD-8.3 | Phase 8 Evaluate; overarching Quality Management and Metadata Management | Corporate Support (Quality, Data, and Metadata Management), Capability Management (improvement) | Data Quality, Data Governance, Traceability | 2.1.3 Statistical quality management, 4.1.4 Improvement management, 4.1.5 Accountability |

### 7. Principles

The following principles govern VS-03 most directly.

| Principle | Statement | Application in VS-03 |
|---|---|---|
| SAF-P01 | Actively participate in open-source communities to maintain collective control over statistical processes | Editing, imputation, and coding tooling, such as selective-editing engines and imputation libraries, is developed and shared in open-source communities with other NSIs. This keeps collective control over critical methodological capabilities instead of depending on vendors. |
| SAF-P07 | Implement loosely coupled processes and systems | Editing is independent from upstream standardisation and downstream estimation. Processed Data (State #3) is the decoupling interface: downstream consumers use edited, enriched microdata without knowing how it was corrected or imputed. |
| SAF-P08 | Data is shared property | Processed data, once versioned, is available to all authorised consumers. Editing and enrichment are not duplicated across statistical products when the same processed asset can serve several purposes. |
| SAF-P09 | No data without metadata and classification | Every edit, imputation, and derived variable carries metadata: the rule applied, the original value, the imputation method and flag, the derivation formula, and a classification for derived variables. This makes the changes transparent and reproducible. |
| SAF-P10 | Security by design | Access controls, integrity verification, and a tamper-evident edit audit trail are built into the editing pipeline from the start, so that every change to a value stays attributable and traceable. |
| SAF-P11 | Privacy by design | VS-03 works on pseudonymised microdata. Enrichment and integration with other datasets raise the risk of re-identification, so linkage is assessed for disclosure risk and minimisation by design, not afterwards. |

::: {.callout-note title="Principles that apply across the process types"}
SAF-P09 is the backbone of the editing discipline: Design defines the rules and the required edit metadata, Execution captures the original value, rule, and reason for every change, and Management assesses edit quality and closes gaps. SAF-P10 governs the tamper-evident edit audit trail across all stages, VS-03.1 to VS-03.5. SAF-P11 applies especially to *Design Integration and Linkage Rules* and to VS-03.4, where linkage can raise the risk of re-identification. SAF-P07 governs both the intake of State #2 from VS-02 and the handover of State #3 to VS-04.
:::

### 8. Interfaces, services, and events

**Boundary interfaces**

VS-03 has two boundary interfaces: intake from VS-02, and handover to VS-04.

| Boundary | Handed over | Required metadata | Trigger | Responsibility transfer |
|---|---|---|---|---|
| VS-02 (or VS-01 where #2 is skipped) → VS-03 (intake) | Registered standardised data version (#2) | Source-to-target mapping lineage, applied classification versions, recorded unit, currency, and reference-period bases, list of unmapped or uncoded values for coding, records of definition differences, classification | *Standardized Data Registered* | VS-02 keeps custody of the standardised artefact; VS-03 takes responsibility for editing, imputation, derivation, interpretive coding, and value conversion on receipt of the event |
| VS-03 → VS-04 (handover) | Registered Processed Data quality version (#3) | Edit lineage (original value, rule, reason), imputation flags and methods, derived-variable formulas and classification, integration and linkage lineage, quality-improvement assessment, quality-version identifier, classification | *Processed Data Registered* | VS-03 keeps custody of the processed version; VS-04 takes responsibility for estimation, weighting, and analysis on receipt of the event |

**Business services**

| Service | Offered to | Realised in | Interfaces |
|---|---|---|---|
| Error-detection service | Consumers of standardised data, editing teams | VS-03.1 Conduct Error Detection and Quality Diagnostics | Diagnostic reports |
| Editing and correction service | Editing teams, subject-matter statisticians | VS-03.2 Perform Data Editing and Correction | Review and adjudication workbench for analysts, edit-audit query interface |
| Imputation service | Editing teams, methodologists | VS-03.3 Impute Missing or Non-Response Data | Imputation flags and records |
| Derivation and integration service | Editing teams, downstream analysts | VS-03.4 Derive Additional Variables and Indicators | Derived-variable catalogue |
| Processed data provisioning service | VS-04 Estimation, Analysis and Statistical Modeling, other statistical products | VS-03.5 Perform Quality Evaluation and Versioning | Event notification (*Processed Data Registered*) and a catalogue query interface to find and access processed quality versions and their edit lineage |
| Quality-version catalogue service | All data consumers in the NSI | Management sub-process *Manage Methodology and Version Lifecycle* | Search and browse interface for quality versions, edit lineage, imputation flags, and derived-variable metadata |
| Design and methodology service | Methodologists, editing and imputation designers | All Design sub-processes of VS-03 | Design documents, methodology advice |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Design artefacts published* | Start of Implementation after a design change |
| *Pipeline production-ready* | End of Implementation; Execution can start |
| *Standardized Data Registered* | Start of VS-03.1 for that version |
| *Quality version accepted* / *Quality insufficient* | Outcome of VS-03.5; insufficient quality starts re-editing or re-imputation after review |
| *Processed Data Registered* | Completion of VS-03.5; triggers VS-04 |
| *Improvement recommendations issued* | Input for Design from *Continuous Improvement* |

|**PLACEHOLDER: VS-03 event choreography between the upstream value stream (VS-02), NSI teams, and process management across Design, Implementation, Execution (detect, edit, code and reconcile, impute, derive, convert and integrate, then quality version accepted or re-edit), and Management (edit and imputation rates, quality improvement, audit reports, improvement recommendations)**|
|---|

**Interaction with the supporting value streams**

| Value stream | Provides to VS-03 | Receives from VS-03 |
|---|---|---|
| VS-07 Governance and Compliance | Editing and privacy policy, audit of edit lineage, methodology compliance, and disclosure risk | Edit audit summaries, methodology and disclosure-risk compliance reports |
| VS-08 Innovation and Methodological Development | Improved imputation and outlier-detection methods, coding tools | Improvement needs; processed data for testing new editing, imputation, or coding methods |
| VS-09 Infrastructure and Platform Enablement | Computing and orchestration for editing, imputation, and coding at scale; version store | Capacity and processing-window requirements |

### 9. Key performance indicators

The key performance indicators are collected per production cycle in *Monitor Process Performance*. They feed the dashboard that the process owner reviews.

| KPI | Description | Measurement |
|---|---|---|
| Edit rate | Share of values changed by editing | Per variable, per cycle |
| Imputation rate | Share of values imputed | Per variable, per cycle |
| Manual-review rate | Share of records routed to manual adjudication | Per source, per cycle |
| Over-editing indicator | Share of edits with negligible impact on results | Per cycle |
| Coding completion rate | Share of free-text values successfully coded | Per classification, per cycle |
| Processing time | Time from standardised intake to versioned registration | Per dataset, per cycle |

### 10. Examples

**Structural Business Statistics.** The design sets consistency rules (turnover ≥ 0, employees ≥ 0, turnover per employee within a plausible band by NACE class), outlier rules based on a Hidiroglou–Berthelot test on year-on-year ratios, and a selective-editing score that flags only units whose potential error would move a published aggregate by more than a set threshold. Everything else is accepted without manual work. In a cycle, the standardised SBS file is diagnosed: 312 units fail the turnover-per-employee band, 47 are duplicates, and 1,204 have missing employee counts. The selective-editing scores prioritise 89 units whose potential error would materially affect a published aggregate; the remaining low-impact flags are scheduled for automatic treatment.

**Labour Force Survey imputation.** For item non-response on income, about 9% of records, the design specifies regression imputation with age, education (ISCED), occupation (ISCO), and region as predictors, and a constraint that imputed income stays within the valid range of the respondent's earnings bracket. Each imputed income carries the flag `imputed=true` and the method code `REG-01`, and the predictor values used are recorded. Analysts can exclude or down-weight imputed values, and the imputation can be reproduced or revised.

**Labour Force Survey coding.** The 42,000 free-text occupation answers handed over from VS-02 are coded to ISCO-08. 88% are coded automatically at or above the confidence threshold of 0.85, 5,040 go to computer-assisted coding, and 1,200 ambiguous cases go to expert manual coding. Each coded value records the source text, the assigned code, the method, and the confidence, so it is auditable as an editing decision.

**Price statistics.** The implementation team builds an outlier detector for daily price changes, an editing engine that applies designed corrections such as decimal-point fixes, and a review queue for flagged price jumps. Every correction stores the original scraped price, the rule, and the analyst's adjudication, so the edit can be audited and reversed.

**Tax register to business statistics.** Turnover, recorded by VS-02 in thousands of euro on a fiscal-year basis, is converted to units on a calendar-year basis with the designed conversion and apportionment rules. The conversion factor and the original value are stored in the lineage. Turnover per employee is then derived as a new indicator, with its formula and inputs recorded.

| **Toolkit:** SAF-TK-V03 VS-03 maturity checklist and scenarios |
|---|



## VS-04 Estimation, Analysis, and Statistical Modeling

### 1. Purpose and value created

VS-04 turns clean microdata into statistics. Up to this point the chain has improved the data itself. Here the focus shifts to producing numbers that describe a population: estimates, weighted aggregates, indices, time series, and model results. VS-04 does not change microdata values; it computes statistics from them. The output is a new kind of object, and each result carries a measure of how accurate it is. The value created is **analytical insight and statistical credibility**: data becomes information about a population that policymakers, researchers, and society can trust. Every decision in this value stream balances methodological detail with transparency and reproducibility.

VS-04 produces validated statistics with initial confidentiality protection. It does not compose products and does not publish them. Combining several analyses into integrated and composite statistical products belongs to VS-05 Statistical Product Composition. Final disclosure control for publication belongs to VS-06 Dissemination and Service Delivery.

::: {.callout-note title="Signature discipline: methodological transparency"}
Every estimate carries the method, parameters, weights, and accuracy measure (sampling error, confidence interval, or model diagnostic) that produced it, and its lineage to its inputs. Any published figure can therefore be regenerated and defended. Imputation uncertainty from VS-03 is reflected in the variance. Fitness for purpose and coherence with related statistics are explicit acceptance criteria. Initial statistical disclosure control is applied, so the output can potentially be released.
:::

VS-04 corresponds to the business domain **Estimation and balancing** (see *Steady-State Architecture, Business domains*). This section describes the business layer of that domain for all four process types: Design, Implementation, Execution, and Management.

|**PLACEHOLDER: ArchiMate view VS-04 (a) value stream and capabilities**|
|---|

<br>

### 2. Position and state transition

VS-04 is the fourth primary value stream. It receives Processed Data from VS-03 and applies statistical methods, estimation techniques, and analytical models to turn it into representative results. It is the stage where data becomes statistical information.

VS-04 takes data from State #3 to State #4, analytical version. Before VS-04, the data is edited, complete, and enriched microdata. After VS-04, it is a registered, immutable analytical version of statistics: estimates and aggregates calculated, accuracy and quality indicators produced, lineage documented, internal review completed, and initial disclosure control applied. The quality gate, the minimum metadata set, and the protection of State #4 are described in *State #4: Statistics* and are not repeated here. State #4 has two gate moments; VS-04 passes the analytical gate, and VS-05 later creates the approved version.

VS-04 receives Processed Data together with the metadata VS-03 attached: edit lineage, derived-variable definitions, and imputation flags. The imputation flags matter most. Estimation must reflect the extra uncertainty that imputed values introduce, for example through variance estimation that accounts for imputation. The edit and derivation lineage is carried through, so every estimate stays traceable to its observed and imputed inputs.

| From | To | Gate | Event out |
|---|---|---|---|
| #3 Processed Data | #4 Statistics (analytical) | Analytical gate of State #4 (approved method, weights, accuracy, model diagnostics, soundness and coherence, initial disclosure control, reproducibility, metadata) | *Output Data Registered* |

|**PLACEHOLDER: ArchiMate view VS-04 (c) state handover and events: Processed Data (#3) from VS-03, the estimation and analysis service at the boundary (weighting, estimation, aggregation, modelling, validation, disclosure control), Statistics (#4, analytical) shared with VS-05**|
|---|

<br>

### 3. Stages

The stages describe the value that VS-04 adds in every production cycle. Together they form the execution process type of VS-04. In a mature steady state, the methods have been designed and the engines built in advance (see attribute 4). Execution then focuses on computing weights, estimates, and models, and on capturing the methodology, parameters, and accuracy measures, so that every output is reproducible and defensible.

| Stage | Name | Value added |
|---|---|---|
| VS-04.1 | Confirm Estimation and Analytical Approach | The method fits the design and the purpose |
| VS-04.2 | Apply Weighting and Calibration | Bias from sampling, non-response, and coverage is reduced |
| VS-04.3 | Estimate and Aggregate Data | Statistics and indicators are available, each with its accuracy |
| VS-04.4 | Perform Model-Based Analysis | Model-based results complement direct estimates |
| VS-04.5 | Validate and Document Results | Results are sound and documented (State #4) |

Each stage below is described with its activities. The column *SAF process* shows the business process from *Business Processes* that the activity belongs to. The column *Other reference* shows the principles, capabilities, or external frameworks that the activity applies.

<br>

#### VS-04.1 Confirm Estimation and Analytical Approach

**Value created:** *The right, pre-approved method selected for this cycle's data and objective.*

Execution starts when the *Processed Data Registered* event arrives from VS-03. In a mature steady state the methodology has already been designed, so each cycle confirms or selects the pre-approved approach for the data at hand. The team verifies that the calibration totals and reference sources are current, and confirms that the target parameters and domains of estimation still apply. A significant change, such as a new domain or a methodology revision, goes back to Design instead of being adapted during the cycle.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Confirm or select the pre-approved estimation and analytical approach for the cycle | Confirmed approach for the cycle | PRD-2.5 Design processing and analysis | |
| Verify that calibration totals and reference sources are current | Reference source confirmation | DLM-9 Manage reference and master data | CSDA Reference Data; 2.1.4 Statistical register management |
| Confirm target parameters, reference populations, and domains of estimation | Confirmed estimation scope | PRD-2.4 Design frame and sample | |
| Flag methodology changes for design review | Methodology change exception (if any) | PRD-2.5 Design processing and analysis | GAMSO Quality Management |

<br>

#### VS-04.2 Apply Weighting and Calibration

**Value created:** *Bias from sampling, non-response, and coverage corrected, so results represent the population.*

The weighting engine applies the design weights and the non-response adjustment. The calibration engine then calibrates to the confirmed population totals, using the designed auxiliary variables and enforcing the weight bounds. Calibration convergence and the resulting weight distribution are checked against the designed constraints. The calibration totals, auxiliary variables, and convergence diagnostics are recorded, so the weighting can be reproduced.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Compute design weights and the non-response adjustment | Adjusted weights | PRD-5.6 Calculate weights | 1.3.5 Estimating population parameters |
| Calibrate to the confirmed population totals with the designed auxiliary variables | Calibrated weights | PRD-5.6 Calculate weights | 1.3.5 Estimating population parameters |
| Check convergence and weight distribution against the bounds | Weight diagnostics | PRD-5.6 Calculate weights | |
| Record calibration totals, auxiliary variables, and diagnostics as lineage | Weighting lineage | PRD-5.6 Calculate weights; OVA-4 Process Data Management | SAF-P09 |

<br>

#### VS-04.3 Estimate and Aggregate Data

**Value created:** *Representative statistics and aggregates, each carrying its accuracy.*

The estimation engine computes the target parameters with the calibrated weights. The aggregation pipeline computes the specified aggregates across the designed domains, with the agreed units and rounding conventions. The variance estimation component computes sampling errors and confidence intervals. These reflect both the survey design and the imputation uncertainty signaled by the VS-03 imputation flags. Every estimate is produced with its methodology, weights, and accuracy measure attached.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Compute target estimates with the calibrated weights | Point estimates | PRD-5.7 Calculate aggregates | 1.3.5 Estimating population parameters |
| Compute aggregates across the designed domains (units, rounding) | Output aggregates | PRD-5.7 Calculate aggregates | |
| Compute sampling errors and confidence intervals (design and imputation uncertainty) | Accuracy measures | PRD-5.7 Calculate aggregates | |
| Attach methodology, weights, and accuracy to every estimate | Estimate metadata | PRD-5.7 Calculate aggregates; OVA-2 Metadata Management | SAF-P09 |

<br>

|**PLACEHOLDER: VS-04 estimation and aggregation architecture: imputation-flagged microdata (#3) and calibrated weights feeding point estimation and aggregation by domain; variance estimation reflecting both the survey design and the imputation flags; every output carrying its accuracy and methodology**|
|---|

<br>

#### VS-04.4 Perform Model-Based Analysis

**Value created:** *Deeper insight: relationships, trends, and small-domain estimates that direct counts cannot give.*

This stage runs the model-based analyses specified in Design: analytical and regression models, time-series and forecasting models, and small-area models. Their diagnostics are computed and checked against the designed bounds, and seasonal adjustment is applied where applicable. Results are interpreted in context, and assumptions and limitations are documented. As with direct estimates, every model output carries its specification, parameters, diagnostics, and uncertainty. Model-based results are flagged distinctly from direct estimates.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Run the designed analytical, forecasting, and small-area models | Model outputs | PRD-6.1 Prepare draft outputs | 1.4.1 Statistical (output) analysis |
| Compute and check model diagnostics against the designed bounds | Model diagnostics | PRD-6.2 Validate outputs | |
| Apply seasonal adjustment and time-series treatment where applicable | Adjusted series | PRD-6.1 Prepare draft outputs | |
| Interpret results; document assumptions and limitations | Analytical commentary | PRD-6.3 Interpret and explain outputs | 1.4.1 Statistical (output) analysis |

<br>

#### VS-04.5 Validate and Document Results

**Value created:** *Statistically sound, coherent, documented, and disclosure-safe statistics, ready for handover.*

Results are checked for statistical soundness and consistency, and for coherence with prior periods and related statistics. Significant movements are explained, and revisions are handled according to the revision policy. Initial statistical disclosure control is applied according to the designed policy: the disclosure risk is assessed, and protection methods such as suppression, rounding, or perturbation are applied, so the output can potentially be released. The methodology and quality indicators are documented. A persistent, immutable output version is created with a unique identifier and full lineage, registered in line with SAF-P09, and access permissions are applied in line with SAF-P10. The stage ends by publishing the *Output Data Registered* event, which tells VS-05 that new validated statistics are available for composition. If validation fails, the results are re-estimated or revised after review.

**Output:** **Statistics (State #4), analytical version**, the official handover artefact to VS-05. Its structure and minimum metadata set are described in *State #4: Statistics*.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Validate soundness and coherence; explain movements; handle revisions | Validation report | PRD-6.2 Validate outputs; DLM-7 Revise data | 1.4.1 Statistical (output) analysis |
| Apply initial statistical disclosure control according to the designed policy | Disclosure-controlled outputs | PRD-6.4 Apply disclosure control | SAF-P11; 1.3.7 Statistical disclosure |
| Document methodology and quality indicators | Methodology and quality documentation | OVA-2 Metadata Management | SAF-P09 |
| Pass the analytical gate and create an immutable, identified output version with full lineage | Versioned output data | DLM-2 Promote data through a quality gate; DLM-5 Store and version data | CSDA Traceability |
| Register metadata, apply access permissions, and publish the *Output Data Registered* event to notify VS-05 | Catalogue registration, event | DLM-3 Register and catalogue data; DLM-4 Classify and protect data | SAF-P07, SAF-P10 |

### 4. The four process types

The sub-processes below are specific to VS-04. Each refines one or more SAF business processes, listed as *Refines*, which keeps it traceable to *Business Processes*. Sub-processes marked *(standard)* work as described in [Standard activities in every value stream](#standard-vs-activities); only the VS-04 specifics are listed.

#### Design: provides metadata

Without well-designed methods, estimation becomes ad hoc and indefensible, and management has no baseline to measure accuracy and coherence against.

| Design sub-process | Refines | Main outputs |
|---|---|---|
| Design Estimation Strategy and Accuracy Approach | PRD-2.4 Design frame and sample; PRD-2.5 Design processing and analysis; OVA-1 Quality Management | Estimation strategy, estimation specification, accuracy measurement plan, coherence criteria |
| Design Weighting and Calibration Methodology | PRD-2.5 Design processing and analysis; DLM-9 Manage reference and master data | Weighting specification, calibration specification, weight constraint policy, calibration total source register |
| Design Aggregation and Model Specifications | PRD-2.1 Design outputs and dissemination; PRD-2.5 Design processing and analysis; OVA-2 Metadata Management | Aggregation specification, model specification, output statistic metadata standard, time-series treatment specification |
| Design Validation and Disclosure-Control Policy | PRD-2.5 Design processing and analysis; OVA-1 Quality Management; OVA-2 Metadata Management | Validation policy, disclosure-control policy, output documentation standard, reproducibility design |
| Design Quality-Measurement and Versioning Framework | OVA-1 Quality Management; DLM-1 Plan and design data assets; DLM-4 Classify and protect data | Quality indicator set, versioning policy, lineage specification, access control design |

##### Design Estimation Strategy and Accuracy Approach

*Refines:* PRD-2.4 Design frame and sample; PRD-2.5 Design processing and analysis; OVA-1 Quality Management.

The starting point is choosing how the statistics will be estimated. This sub-process selects the estimation strategy that fits the source and the analytical objective: design-based estimation for sample surveys, register-based aggregation, or model-assisted and model-based estimation for small domains. It defines the target parameters, the reference populations, and the domains of estimation. It also defines the accuracy measurement approach: how sampling errors and confidence intervals are computed, including how the uncertainty introduced by VS-03 imputation is reflected in variance estimation. Coherence criteria with related and prior statistics complete the design.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Select the estimation strategy per source and objective (design-based, register-based, model-based) | Estimation strategy document | PRD-2.5 Design processing and analysis | 1.1.2 Design statistics product |
| Define target parameters, reference populations, and domains of estimation | Estimation specification | PRD-2.4 Design frame and sample; PRD-2.5 Design processing and analysis | |
| Define the accuracy measurement approach (sampling error, confidence interval), reflecting imputation uncertainty | Accuracy measurement plan | PRD-2.5 Design processing and analysis | |
| Define coherence criteria with related and prior statistics | Coherence criteria | OVA-1 Quality Management | GAMSO Quality Management |

##### Design Weighting and Calibration Methodology

*Refines:* PRD-2.5 Design processing and analysis; DLM-9 Manage reference and master data.

This sub-process designs how sampling bias, non-response, and coverage errors are corrected through weighting. The team specifies the design weights, the non-response adjustment model, and the calibration method, for example calibration to known population totals from registers. It sets the auxiliary variables and calibration totals to use, and the authoritative source and version of those totals. Bounds and acceptance constraints on the weights prevent extreme weights.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Specify design weights and the non-response adjustment | Weighting specification | PRD-2.5 Design processing and analysis | 1.3.5 Estimating population parameters |
| Specify the calibration method, auxiliary variables, and calibration totals with their sources | Calibration specification | PRD-2.5 Design processing and analysis | |
| Define weight bounds and acceptance constraints | Weight constraint policy | PRD-2.5 Design processing and analysis | |
| Define the authoritative source and version of the calibration totals | Calibration total source register | DLM-9 Manage reference and master data | CSDA Reference Data; 2.1.4 Statistical register management |

##### Design Aggregation and Model Specifications

*Refines:* PRD-2.1 Design outputs and dissemination; PRD-2.5 Design processing and analysis; OVA-2 Metadata Management.

This sub-process specifies what is computed. For aggregation, each output statistic is defined by its formula, its domains and breakdowns, and its units and rounding conventions. For analysis, model-based methods (regression, time-series and forecasting, small-area models) are specified with their inputs, their assumptions, and the diagnostics that must be produced and checked. Seasonal adjustment and time-series treatment are specified where applicable. Each output statistic receives its metadata and classification, in line with SAF-P09.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Specify output aggregates: formulas, domains and breakdowns, units, rounding | Aggregation specification | PRD-2.1 Design outputs and dissemination; PRD-2.5 Design processing and analysis | |
| Specify analytical and forecasting models: inputs, assumptions, diagnostics | Model specification | PRD-2.5 Design processing and analysis | |
| Define metadata and classification for every output statistic | Output statistic metadata standard | OVA-2 Metadata Management | SAF-P09 |
| Define seasonal adjustment and time-series treatment where applicable | Time-series treatment specification | PRD-2.5 Design processing and analysis | |

##### Design Validation and Disclosure-Control Policy

*Refines:* PRD-2.5 Design processing and analysis; OVA-1 Quality Management; OVA-2 Metadata Management.

This sub-process designs how results are validated and protected before handover. Validation criteria cover statistical soundness (plausibility, consistency, model diagnostics within bounds), coherence with related and prior statistics, and the revision policy. The statistical disclosure control policy sets the disclosure-risk criteria for tables and any output microdata, and the protection methods: suppression, rounding, and perturbation. The aim is an output that can potentially be released, in line with SAF-P11. Reproducibility is designed in: an output must be regenerable from the processed input plus the recorded methodology and parameters.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define validation criteria: soundness, coherence, model diagnostics, revision policy | Validation policy | OVA-1 Quality Management | GAMSO Quality Management |
| Define disclosure-risk criteria and protection methods | Disclosure-control policy | PRD-2.5 Design processing and analysis | SAF-P11; 1.3.7 Statistical disclosure |
| Define output metadata and methodology documentation requirements | Output documentation standard | OVA-2 Metadata Management | SAF-P09 |
| Design reproducibility: regenerate outputs from inputs, methodology, and parameters | Reproducibility design | PRD-2.5 Design processing and analysis | SAF-P10 |

##### Design Quality-Measurement and Versioning Framework

*Refines:* OVA-1 Quality Management; DLM-1 Plan and design data assets; DLM-4 Classify and protect data.

This last design sub-process makes sure that accuracy is measured and outputs are traceable. It defines the quality indicators to produce: sampling error, coefficient of variation, response and coverage rates, and model fit. It sets the output versioning policy: how versions are identified, what triggers a revision, immutability, and retention. It defines the lineage requirements from each statistic back to its processed inputs and the method applied, and the role-based access control for outputs, in line with SAF-P10.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define quality indicators (sampling error, coefficient of variation, response and coverage rates, model fit) | Quality indicator set | OVA-1 Quality Management | GAMSO Quality Management |
| Define the output versioning and revision policy | Versioning policy | DLM-1 Plan and design data assets | CSDA Traceability |
| Define lineage from each statistic to its processed inputs and method | Lineage specification | DLM-1 Plan and design data assets | CSDA Traceability |
| Design role-based access control for outputs | Access control design | DLM-4 Classify and protect data | SAF-P10; 3.3.4 Logical identity and access control |

|**PLACEHOLDER: VS-04 design process decomposition: inputs (processed data model with imputation flags, methodology set, calibration totals from registers, framework standards), the five design sub-processes in order, and the design document each produces, which together govern Implementation, Execution, and Management**|
|---|

#### Implementation: provides the execution process

| Implementation sub-process | Refines | Main outputs |
|---|---|---|
| Build Weighting and Calibration Engines | PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows; DLM-9 Manage reference and master data | Configured weighting and calibration engines, calibration total integration, versioned methodology repository |
| Build Estimation and Aggregation Pipelines | PRD-3.2 Reuse or build processing and analysis components; OVA-2 Metadata Management | Estimation pipeline, variance component, aggregation pipeline, output metadata binding |
| Build Modelling Environment, Validation, and Disclosure-Control Tooling | PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows; DLM-5 Store and version data | Modelling environment, validation tooling, disclosure-control tooling, versioning store, events |
| Test and Validate the Pipeline *(standard)* | PRD-3.5 Test production systems; PRD-3.6 Test statistical business process; PRD-3.7 Finalise production systems | Test reports for weighting, calibration, estimation, variance, aggregation, modelling, validation, disclosure control, and versioning store; reproducibility test (an output regenerated identically from the processed input plus the recorded methodology and parameters); benchmark or back-series test against known or prior-period results; accuracy measures and model diagnostics checked against expectations |

##### Build Weighting and Calibration Engines

*Refines:* PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows; DLM-9 Manage reference and master data.

This sub-process turns the weighting and calibration designs into operational tools. The weighting engine computes design weights and non-response adjustments. The calibration engine calibrates to the designed totals with the specified auxiliary variables and enforces the weight bounds. The connections to the authoritative register and reference sources are configured with version pinning, so the totals used are recorded and reproducible. All weighting logic is version-controlled, in line with SAF-P10.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Build or configure the weighting engine (design weights, non-response adjustment) | Configured weighting engine | PRD-3.2 Reuse or build processing and analysis components | SAF-P01 |
| Build or configure the calibration engine with auxiliary variables and bounds | Configured calibration engine | PRD-3.2 Reuse or build processing and analysis components | |
| Configure calibration total connections to versioned register sources | Calibration total integration | PRD-3.4 Configure workflows; DLM-9 Manage reference and master data | CSDA Reference Data |
| Version-control all weighting and calibration logic | Versioned methodology repository | PRD-3.4 Configure workflows | SAF-P10 |

##### Build Estimation and Aggregation Pipelines

*Refines:* PRD-3.2 Reuse or build processing and analysis components; OVA-2 Metadata Management.

The designed estimation and aggregation specifications are implemented as automated services. The estimation engine computes the target parameters with the designed accuracy measures. The variance estimation component computes sampling errors and confidence intervals, accounting for the survey design and, through the VS-03 imputation flags, for imputation uncertainty. The aggregation pipeline computes the specified aggregates across the designed domains with the units and rounding conventions. Every output is produced with its methodology, parameters, weights, and accuracy measure attached.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Build the estimation engine for the designed target parameters | Estimation pipeline | PRD-3.2 Reuse or build processing and analysis components | 1.1.3 Build statistics product |
| Build the variance estimation component (design and imputation uncertainty) | Variance and accuracy component | PRD-3.2 Reuse or build processing and analysis components | |
| Build the aggregation pipeline (domains, units, rounding) | Aggregation pipeline | PRD-3.2 Reuse or build processing and analysis components | |
| Attach methodology, weights, and accuracy measure to every output | Output metadata binding | OVA-2 Metadata Management | SAF-P09 |

##### Build Modelling Environment, Validation, and Disclosure-Control Tooling

*Refines:* PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows; DLM-5 Store and version data.

This sub-process implements model-based analysis, validation, and disclosure control. The modelling environment runs the specified analytical, forecasting, and small-area models with their diagnostics and, where applicable, seasonal adjustment. Validation tooling implements the designed soundness and coherence checks, including comparison with prior periods and related statistics. Disclosure-control tooling implements the designed risk checks and protection methods: suppression, rounding, and perturbation. The output versioning store keeps each accepted output version immutable, identified, reproducible from inputs plus methodology, and linked to its lineage. Event notifications alert VS-05 when an output version is registered.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Build or configure the modelling environment (models, diagnostics, seasonal adjustment) | Modelling environment | PRD-3.2 Reuse or build processing and analysis components | |
| Implement validation tooling (soundness, coherence, prior-period comparison) | Validation tooling | PRD-3.2 Reuse or build processing and analysis components | |
| Implement disclosure-control tooling (risk checks, suppression, rounding, perturbation) | Disclosure-control tooling | PRD-3.2 Reuse or build processing and analysis components | SAF-P11; 1.3.7 Statistical disclosure |
| Build the output versioning store (immutable, identified, reproducible) | Versioning store | DLM-5 Store and version data | CSDA Traceability |
| Configure the *Output Data Registered* event for downstream consumers | Event publication | PRD-3.4 Configure workflows | SAF-P07 |

|**PLACEHOLDER: VS-04 implementation pipeline: the five design artefacts feeding the three build sub-processes, followed by technical testing, reproducibility and benchmark testing, and accuracy verification, resulting in a production-ready estimation pipeline and operational procedures**|
|---|

#### Execution: provides the statistical data

Execution runs the stages of VS-04 in every production cycle. The stages and their activities are described in attribute 3. A cycle starts when a new Processed Data version is registered. The stages then run in order; VS-04.4 runs only where the design specifies model-based results. Execution applies the designed methods and the built engines as they are; a new domain or a methodology revision goes back to Design. Each run produces a new analytical version; preliminary, revised, and final figures are separate versions.

| Aspect | VS-04 |
|---|---|
| Trigger | *Processed Data Registered* |
| Cadence | Per production cycle, following the release calendar; additional runs for revisions according to the revision policy |
| Performed by | ROL-15 Subject-matter statistician (survey statistician, analyst or modeler, subject-matter reviewer), ROL-16 Disclosure control specialist, ROL-03 Data steward |
| Input | Processed Data (#3) with imputation flags and edit lineage, confirmed calibration totals, production-ready pipeline |
| Output | Registered analytical version of Statistics (#4) with methodology, accuracy, and lineage |
| Control point | Weight diagnostics in VS-04.2; analytical gate of State #4 in VS-04.5 |
| Exception path | Validation failed: re-estimate or revise after review; methodology change back to Design; an error in the microdata back to VS-03 as a new #3 version |

#### Management: provides quality reports

| Management sub-process | Refines | Main outputs |
|---|---|---|
| Monitor Process Performance *(standard)* | OVA-4 Process Data Management; PRD-8.1 Gather evaluation inputs | Process performance dashboard; throughput report against the release calendar; paradata on methods, parameter and software versions run, and number of manual interventions |
| Assess Output Quality | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use | Accuracy report, coherence report, revision analysis, quality trend analysis |
| Manage Methodology and Output-Version Lifecycle | OVA-2 Metadata Management; OVA-5 Knowledge Management; DLM-5 Store and version data; DLM-8 Monitor data quality, lineage and use | Methodology version register, metadata quality report, version store audit, metadata lineage audit |
| Audit and Compliance Reporting *(standard)* | OVA-1 Quality Management; OVA-4 Process Data Management; DLM-8 Monitor data quality, lineage and use | Reproducibility audit showing that every published figure can be regenerated from the processed input plus the recorded methodology and parameters; disclosure-control report on the control applied and the risk outcomes (SAF-P11); methodology compliance report confirming that approved estimation and analytical methods were applied (4.1.5 Accountability); security compliance report including the integrity of the tamper-evident methodology record (SAF-P10) |
| Continuous Improvement *(standard)* | PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan | Improvement recommendations, for example refining the calibration specification to reduce variance, recalibrating or replacing models, improving the non-response adjustment, adopting better variance estimators, and tuning the release process to improve timeliness; trends watched: sampling errors, revisions, coherence, model performance |

##### Assess Output Quality

*Refines:* OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use.

Beyond process performance, the quality of the outputs themselves is evaluated against the criteria set in *Design Quality-Measurement and Versioning Framework*. Each output is assessed on several dimensions. Accuracy covers sampling error, coefficient of variation, and model fit. Coherence covers consistency with related and prior statistics. Timeliness is measured against the release calendar. Reliability is assessed through revision analysis that compares preliminary and final figures. Quality indicators are produced per statistic, per output, and per cycle. Trends are tracked to detect deteriorating accuracy, growing revisions, or models that need recalibration. This follows the Data Quality capability of CSDA and SAF capability 2.1.3 *Statistical quality management*.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Evaluate accuracy (sampling error, coefficient of variation, model fit) | Accuracy report (per cycle) | OVA-1 Quality Management | 2.1.3 Statistical quality management |
| Assess coherence with related and prior statistics | Coherence report | OVA-1 Quality Management | CSDA Data Quality |
| Conduct revision analysis (preliminary compared with final figures) | Revision analysis | DLM-8 Monitor data quality, lineage and use | 2.1.3 Statistical quality management |
| Identify quality trends across statistics and cycles | Quality trend analysis | DLM-8 Monitor data quality, lineage and use | 2.1.3 Statistical quality management |

##### Manage Methodology and Output-Version Lifecycle

*Refines:* OVA-2 Metadata Management; OVA-5 Knowledge Management; DLM-5 Store and version data; DLM-8 Monitor data quality, lineage and use.

The estimation methods and the output versions they produce must stay current, complete, and well governed. This sub-process governs the life cycle of estimation methods, weighting and calibration specifications, and models. It versions them, manages transitions, such as a methodology change with back-series implications, and retires obsolete methods. It verifies that every output carries its full methodology, weights, accuracy measures, and lineage, as a compliance check on SAF-P09. It governs the output versioning store: retention, immutability, and reconciliation of catalogue entries with stored versions. Lineage from the processed state through estimation to the output state is tracked.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Govern the life cycle and versions of estimation methods, weighting specifications, and models | Methodology version register | OVA-5 Knowledge Management; OVA-2 Metadata Management | SAF-P03 |
| Verify metadata completeness (methodology, weights, accuracy, lineage) | Metadata quality report | OVA-2 Metadata Management | SAF-P09 |
| Govern the output versioning store: retention, immutability, reconciliation | Version store audit | DLM-5 Store and version data | CSDA Traceability |
| Track metadata lineage from processed to output state | Metadata lineage audit | DLM-8 Monitor data quality, lineage and use | CSDA Traceability |

|**PLACEHOLDER: VS-04 management feedback loop: data and paradata from Execution flowing through the five management sub-processes, with accuracy and timeliness dashboards to the process owner, accuracy, coherence, and revision reports to the quality manager, reproducibility and disclosure-control reports to VS-07, and updated methods and models back to Design**|
|---|

#### Metadata per process type

Metadata is produced in every process type, not only in Design. In this value stream, metadata is what makes a published figure defensible. The table shows the data metadata each process type of VS-04 contributes; the paradata are listed in [Standard activities in every value stream](#standard-vs-activities). In Implementation, VS-04 also records the outcomes of reproducibility tests, and in Execution the parameter values and run identifiers of every run.

| Process type | Data metadata produced |
|---|---|
| Design | Estimation and weighting methodology, calibration totals and their sources, aggregation specifications, model specifications, validation and disclosure-control policy |
| Implementation | Engine configurations, weighting and estimation parameters, model parameters, variance estimation settings, disclosure-control parameters |
| Execution | Per estimate: methodology, weights, accuracy measures (sampling error, confidence interval), model diagnostics, reference population, record of the disclosure control applied |
| Management | Accuracy and coherence assessments, revision analyses, lineage assessments, trend analyses |

|**PLACEHOLDER: VS-04 business object lifecycle: design artefacts (estimation strategy, weighting and calibration specification, aggregation and model specifications, validation and disclosure-control policy) govern implementation assets (weighting and estimation engines, modelling environment, variance and disclosure-control tooling, versioning store), which turn Processed Data (#3) into Statistics (#4), generating methodology, weights, accuracy, and output versions that management assesses and feeds back to design**|
|---|

### 5. Actors and roles

The table shows the actors and the reference roles involved in VS-04. Specialised role names used in an NSI map onto these reference roles (see *Role names in the value streams*). For example, the estimation methodologist in the original VS-04 description is ROL-07 Methodologist, the model designer is ROL-06 Statistical designer, and the survey statistician, the analyst or modeler, and the subject-matter reviewer are all forms of ROL-15 Subject-matter statistician.

| Actor or role | ID | Process type | Responsibility in VS-04 |
|---|---|---|---|
| International statistical organisation (methodology authority) | ACT-07 | External | Sets estimation, weighting, and analytical methods the NSI conforms to, for example Eurostat guidance |
| Process owner | ROL-01 | Management | Accountable for the end-to-end performance of VS-04 |
| Data owner | ROL-02 | Management | Accountable for the analytical version of State #4: methodological soundness and accuracy |
| Data steward | ROL-03 | Execution | Registers output datasets and versions, manages metadata entries, applies access controls |
| Data custodian | ROL-04 | Execution | Operates the output versioning store, access control, and retention |
| Statistical designer (model designer) | ROL-06 | Design | Specifies analytical and forecasting models, their inputs, assumptions, and diagnostics |
| Methodologist (estimation methodologist) | ROL-07 | Design | Designs the estimation strategy, the weighting and calibration methodology, and the accuracy measurement approach; owns the estimation, weighting, and model methods |
| Data engineer | ROL-10 | Implementation | Builds and configures weighting, estimation, aggregation, and modelling engines and the pipeline |
| Platform engineer | ROL-11 | Implementation | Configures estimation services, calibration total sources, and access controls |
| Test manager | ROL-12 | Implementation | Plans and carries out testing of the estimation pipeline: technical, reproducibility, and benchmark tests |
| Subject-matter statistician (survey statistician) | ROL-15 | Execution | Applies the designed weighting and calibration and computes estimates with accuracy measures |
| Subject-matter statistician (analyst or modeler) | ROL-15 | Execution | Carries out model-based analysis, regression, and forecasting, and documents diagnostics |
| Subject-matter statistician (subject-matter reviewer) | ROL-15 | Execution | Reviews results for plausibility, coherence, and fitness for purpose, and signs off |
| Disclosure control specialist | ROL-16 | Design, Execution | Designs the disclosure-control rules and disclosure-risk criteria for outputs, and applies initial disclosure control |
| Quality manager | ROL-18 | Management | Monitors accuracy and coherence indicators, produces quality reports, and drives continuous improvement |
| Compliance officer | ROL-19 | Management | Ensures reproducibility and disclosure-risk compliance, and produces audit reports |

### 6. Capabilities, processes, and functions

#### Capability foundations

The table shows which capabilities from the SAF capability model VS-04 relies on, and what role they play. NSIs can use it to map the value stream to their own organisation.

| Capability group | Capabilities | Role in VS-04 |
|---|---|---|
| 1.1 Statistical design and build | 1.1.2 Design statistics product, 1.1.3 Build statistics product | Design the estimation and weighting methodology and the analytical models, and build the estimation pipeline |
| 1.3 Processing | 1.3.5 Estimating population parameters, 1.3.7 Statistical disclosure | Compute weights, estimates, and aggregates; apply initial disclosure control |
| 1.4 Analysis | 1.4.1 Statistical (output) analysis | Validate, interpret, and explain the results |
| 2.1 Data management | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management, 2.1.4 Statistical register management | Manage data, methodology metadata, and quality; assess accuracy and coherence; use registers for calibration totals |
| 3.2 Computerisation and automation | 3.2.1 Application development, 3.2.2 Functional management | Build and maintain weighting, estimation, aggregation, and modelling engines |
| 3.3 Security and privacy | 3.3.1 Privacy management, 3.3.2 Security planning | Apply statistical disclosure control and assess output disclosure risk |
| 4.1 Governance | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improvement management, 4.1.5 Accountability | Govern the domain, steward estimation methodology, plan improvements, report on reproducibility and compliance |

#### Stages, processes, and functions

The table shows which SAF business processes realise each stage of VS-04 and which business functions they mainly use.

| Stage | Realised by processes | Main functions |
|---|---|---|
| VS-04.1 Confirm Estimation and Analytical Approach | PRD-2.4 Design frame and sample; PRD-2.5 Design processing and analysis | FUN-3.1 Design and build statistical products; FUN-4.1 Manage statistical and analytical methodology |
| VS-04.2 Apply Weighting and Calibration | PRD-5.6 Calculate weights | FUN-3.4 Estimate and analyse |
| VS-04.3 Estimate and Aggregate Data | PRD-5.7 Calculate aggregates | FUN-3.4 Estimate and analyse |
| VS-04.4 Perform Model-Based Analysis | PRD-6.1 Prepare draft outputs; PRD-6.3 Interpret and explain outputs | FUN-3.4 Estimate and analyse |
| VS-04.5 Validate and Document Results | PRD-6.2 Validate outputs; PRD-6.4 Apply disclosure control; OVA-2 Metadata Management | FUN-3.4 Estimate and analyse; FUN-3.5 Protect statistical confidentiality; FUN-7.2 Manage metadata |

|**PLACEHOLDER: ArchiMate view VS-04 (b) stages realised by processes and functions**|
|---|

#### Framework mappings

This reference table maps each process type of VS-04 to the SAF business processes, the international frameworks (GSBPM, GAMSO, CSDA), and the SAF capability model. It is intended for architects and auditors; the rest of this section does not depend on it.

| Process type | SAF business processes | GSBPM | GAMSO | CSDA | SAF capabilities |
|---|---|---|---|---|---|
| Design | PRD-2.1, PRD-2.4, PRD-2.5, DLM-1, DLM-4, DLM-9, OVA-1, OVA-2 | Phase 2 Design (2.1, 2.4, 2.5) | Production (design activities), Capability Management | Data Governance, Metadata Management, Data Quality, Reference Data | 1.1.2 Design statistics product, 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| Implementation | PRD-3.2, PRD-3.4 to PRD-3.7, DLM-5, DLM-9, OVA-2 | Phase 3 Build (3.2, 3.4 to 3.7) | Capability Management | Data Processing and Analysis (set-up), Data Governance (configuration) | 1.1.3 Build statistics product, 3.2.1 Application development, 3.2.2 Functional management |
| Execution | PRD-2.4, PRD-2.5, PRD-5.6, PRD-5.7, PRD-6.1 to PRD-6.4, DLM-2 to DLM-5, DLM-7, DLM-9, OVA-2, OVA-4 | Phase 5 Process (5.6 Calculate weights, 5.7 Calculate aggregates), Phase 6 Analyse (6.1 to 6.4); 2.4 and 2.5 in their recurrent form | Production (execution) | Data Analysis (execution) | 1.3.5 Estimating population parameters, 1.3.7 Statistical disclosure, 1.4.1 Statistical (output) analysis, 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| Management | OVA-1, OVA-2, OVA-4, OVA-5, DLM-5, DLM-8, PRD-8.1 to PRD-8.3 | Phase 8 Evaluate; overarching Quality Management and Metadata Management | Corporate Support (Quality, Data, and Metadata Management), Capability Management (improvement) | Data Quality, Data Governance, Traceability | 2.1.3 Statistical quality management, 4.1.4 Improvement management, 4.1.5 Accountability |

### 7. Principles

The following principles govern VS-04 most directly.

| Principle | Statement | Application in VS-04 |
|---|---|---|
| SAF-P01 | Actively participate in open-source communities to maintain collective control over statistical processes | Estimation, weighting, and modelling tooling, such as calibration and variance estimation libraries, is open source where possible, and the NSI contributes to the communities that maintain it. The NSI keeps collective control over critical methodological capabilities instead of depending on vendors. |
| SAF-P07 | Implement loosely coupled processes and systems | Estimation is independent from upstream editing and downstream composition. Statistics (State #4) is the decoupling interface: downstream consumers use validated statistics without knowing the estimation internals. |
| SAF-P08 | Data is shared property | Output statistics and output microdata, once validated, are available to all authorised consumers. Estimation is not duplicated across products when the same validated output can serve several purposes. |
| SAF-P09 | No data without metadata and classification | Every estimate carries metadata: the methodology and parameters applied, the weights used, accuracy measures (sampling error, confidence interval), the reference population, and a classification for derived statistics. This is what makes results transparent and reproducible. |
| SAF-P10 | Security by design | Access controls, integrity verification, and a tamper-evident record of methods and parameters are built into the estimation pipeline from the start, so that every published figure is attributable and reproducible. |
| SAF-P11 | Privacy by design | Initial statistical disclosure control is applied to outputs, and the disclosure risk of estimates and any output microdata is assessed by design, so the result can potentially be released. |

::: {.callout-note title="Principles that apply across the process types"}
SAF-P09 is the backbone of methodological transparency: Design defines the methodology and the required output metadata, Execution captures the method, parameters, weights, and accuracy measures for every estimate, and Management assesses output quality and coherence. SAF-P10 governs the tamper-evident record of methods and the reproducibility of outputs across the stages VS-04.1 to VS-04.5. SAF-P11 applies especially to VS-04.5, where the disclosure risk of the output is assessed before handover. SAF-P07 governs both the intake of State #3 from VS-03 and the handover of State #4 to VS-05.
:::

### 8. Interfaces, services, and events

**Boundary interfaces**

VS-04 has two boundary interfaces: intake from VS-03, and handover to VS-05.

| Boundary | Handed over | Required metadata | Trigger | Responsibility transfer |
|---|---|---|---|---|
| VS-03 → VS-04 (intake) | Registered Processed Data version (#3) | Minimum metadata set of State #3, in particular edit lineage, derived-variable definitions, imputation flags and methods, quality improvement assessment, quality version identifier, classification | *Processed Data Registered* | VS-03 keeps custody of the processed version; VS-04 takes responsibility for weighting, estimation, modelling, and validation on receipt of the event |
| VS-04 → VS-05 (handover) | Registered analytical version of Statistics (#4) | Minimum metadata set of State #4: methodology and parameters, weights, accuracy measures, model diagnostics, record of disclosure control applied, coherence results, quality indicators, output version identifier, lineage to the processed source, classification | *Output Data Registered* | VS-04 keeps custody of the output version; VS-05 takes responsibility for composing integrated and composite products on receipt of the event |

**Business services**

| Service | Offered to | Realised in | Interfaces |
|---|---|---|---|
| Weighting and calibration service | Estimation teams, consumers of processed data | VS-04.2 Apply Weighting and Calibration | Weighting and calibration engines |
| Estimation and aggregation service | Estimation teams, analysts | VS-04.3 Estimate and Aggregate Data | Estimation interface that returns estimates with accuracy measures; query interface for methodology and parameters |
| Modelling and analysis service | Analysts, methodologists | VS-04.4 Perform Model-Based Analysis | Modelling environment |
| Validation and disclosure-control service | Quality managers, disclosure control specialists | VS-04.5 Validate and Document Results | Validation and disclosure-control tooling |
| Output data provisioning service | VS-05 Statistical Product Composition, data analysts, other statistical processes | VS-04.5 Validate and Document Results | Event notification (*Output Data Registered*) and a catalogue query interface to find and access output versions, their accuracy measures, and methodology |
| Output version catalogue service | All data consumers in the NSI | Management sub-process *Manage Methodology and Output-Version Lifecycle* | Search and browse interface for output versions, accuracy measures, methodology documentation, and lineage |
| Design and methodology service | Methodologists, statistical designers | All Design sub-processes of VS-04 | Design documents, methodology advice |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Design artefacts published* | Start of Implementation after a design change |
| *Pipeline production-ready* | End of Implementation; Execution can start |
| *Processed Data Registered* | Start of VS-04.1 for a new cycle |
| *Output version accepted* / *Validation failed* | Outcome of VS-04.5; failure starts re-estimation or revision after review |
| *Output Data Registered* | Completion of VS-04.5; triggers VS-05 |
| *Improvement recommendations issued* | Input for Design from *Continuous Improvement* |

|**PLACEHOLDER: VS-04 event choreography between VS-03, NSI teams, and process management across Design, Implementation, Execution (Processed Data Registered, weighting, estimation, modelling, validation passed or failed, Output Data Registered), and Management (accuracy, timeliness, coherence, revisions, audit, improvement recommendations)**|
|---|

**Interaction with the supporting value streams**

| Value stream | Provides to VS-04 | Receives from VS-04 |
|---|---|---|
| VS-07 Governance and Compliance | Methodology, privacy, and security policy | Reproducibility audits, disclosure-control and methodology compliance reports |
| VS-08 Innovation and Methodological Development | New estimation, weighting, and modelling methods | Improvement needs, for example better variance estimators or replacement models |
| VS-09 Infrastructure and Platform Enablement | Estimation and modelling environments, versioning store, catalogue, event interfaces | Capacity and environment requirements |

### 9. Key performance indicators

The key performance indicators are collected per production cycle in *Monitor Process Performance*. They feed the dashboard that the process owner reviews.

| KPI | Description | Measurement |
|---|---|---|
| On-time output rate | Share of outputs produced within the release calendar window | Per output, per cycle |
| Average sampling error or coefficient of variation | Typical accuracy of key estimates | Per statistic, per cycle |
| Coherence check pass rate | Share of outputs that pass the coherence checks on the first run | Per cycle |
| Revision magnitude | Size of revisions compared with previously published figures | Per statistic, per cycle |
| Reproducibility rate | Share of outputs that regenerate identically from inputs plus methodology | Per cycle |
| Processing time | Time from processed intake to versioned registration | Per output, per cycle |

### 10. Examples

**Labour Force Survey.** The design-based estimation strategy for the employment rate calibrates to population totals by age, sex, and region, with a variance estimator (for example a linearisation or replication method) that accounts for the survey design and for the income and non-response imputation flagged in VS-03. Domains of estimation are national and NUTS-2. For cycle Q3-2026 the team confirms the strategy, the calibration totals from the latest population register extract, and the domains; no methodology change is needed, so the cycle does not return to Design. The employment rate is estimated at 71.4%, with a 95% confidence interval of ±0.5 percentage points at national level and wider intervals at NUTS-2. Each cell carries its estimate, coefficient of variation, and the method that produced it.

**Household survey.** The calibration is designed as a generalised regression (GREG) calibration to population totals by age, sex, and region from the population register, with weight bounds that cap the calibration factor. The engine pulls the totals from a pinned version of the register and records the totals and convergence diagnostics with every run. In production the calibration converges in 6 iterations, the weighted margins reproduce the register totals, and the calibration factor stays within the bounds.

**Tax register to business statistics.** For small NACE by region domains where the direct register aggregate is unstable, a small-area model borrows strength across domains to produce more reliable estimates. The model diagnostics (fit, prediction intervals) are recorded, and the model-based cells are flagged distinctly from direct aggregates.

| **Toolkit:** SAF-TK-V04 VS-04 maturity checklist and scenarios |
|---|



## VS-05 Statistical Product Composition

### 1. Purpose and value created

VS-05 turns the statistics that VS-04 produced into finished statistical products. A single estimate is not yet something a user reads. VS-05 brings results from different domains, surveys, and time periods together into coherent publications, time series, indices, and datasets, explains them, and approves them for release. It does not re-estimate anything: it selects, combines, checks, explains, and signs off. The value created is **coherence and interpretability**: the product is internally consistent, coherent with related and prior statistics, and accompanied by the metadata and interpretation that users need to understand it.

VS-05 corresponds to the business domain **Statistically composed and composite products** (see *Steady-State Architecture, Business domains*). This section describes the business layer of that domain for all four process types: Design, Implementation, Execution, and Management. Re-estimation, weighting, and model-based analysis are not part of VS-05; they belong to VS-04. Publishing, distribution, user services, and final disclosure control for release belong to VS-06.

::: {.callout-note title="Signature discipline: coherence and interpretability"}
VS-05 composes validated outputs; it does not re-estimate them. Every product is internally consistent, coherent with related and prior statistics, carries the accuracy metadata of its components, has lineage to its component outputs and the composition method, and is approved against dissemination and confidentiality standards before it is registered.
:::

|**PLACEHOLDER: ArchiMate view VS-05 (a) value stream and capabilities**|
|---|

<br>

### 2. Position and state transition

VS-05 is the fifth primary value stream. It receives validated statistics from VS-04 and delivers approved products to VS-06. It is the stage where separate analyses become finished statistical products.

VS-05 works within State #4. It consumes analytical versions of #4 and produces approved versions of #4. Approval does not change an analytical version: it creates a new, immutable version with the status *approved* that refers to the analytical versions it was composed from. The quality gate, the minimum metadata set, and the protection of State #4 are described in *State #4: Statistics* and are not repeated here.

VS-05 receives the analytical versions together with the metadata VS-04 attached: methodology, weights, accuracy measures such as sampling errors and confidence intervals, and the record of the disclosure control already applied. VS-05 propagates this accuracy and quality metadata into the product. It does not discard or recompute it. It uses it to weight or caveat the composed figures, and to run coherence checks across the combined outputs. Composition never silently changes a component estimate.

| From | To | Gate | Event out |
|---|---|---|---|
| #4 Statistics (analytical) | #4 Statistics (approved) | Approval gate of State #4 (component selection, composition, consistency and coherence, interpretive content, dissemination and confidentiality standards, sign-off) | *Statistical Product Registered* |

|**PLACEHOLDER: ArchiMate view VS-05 (c) state handover and events: analytical #4 versions from VS-04, the composition service at the boundary (integrate outputs, construct composites, coherence checks, interpret, approve and register), approved #4 product versions handed to VS-06**|
|---|

<br>

### 3. Stages

The stages describe the value that VS-05 adds in every production cycle. Together they form the execution process type of VS-05. In a mature steady state, the products, composites, checks, and templates have been designed and built in advance (see attribute 4). Execution then focuses on composing the product, checking its coherence, and capturing component lineage and approval, so that every product is coherent, interpretable, and reproducible.

| Stage | Name | Value added |
|---|---|---|
| VS-05.1 | Select and Integrate Source Datasets | Relevant results are brought together |
| VS-05.2 | Construct Composite Indicators or Indices | Indices, ratios, and aggregates are available |
| VS-05.3 | Perform Consistency and Coherence Checks | The product is internally consistent |
| VS-05.4 | Generate Analytical and Interpretive Outputs | Results are explained and visualised |
| VS-05.5 | Approve and Register Statistical Products | The product is approved for release (State #4, approved) |

Each stage below is described with its activities. The column *SAF process* shows the business process from *Business Processes* that the activity belongs to. The column *Other reference* shows the principles, capabilities, or external frameworks that the activity applies.

<br>

#### VS-05.1 Select and Integrate Source Datasets

**Value created:** *The right validated outputs brought together as the basis for a coherent product.*

Execution starts when VS-04 publishes the *Output Data Registered* event for the components of a product. The team applies the designed selection rules to pick the correct analytical #4 versions, by domain, period, and accuracy. The exact versions are pinned, so the product can always be traced to them. Components from several domains, surveys, or time periods are integrated into the product structure as specified. Their accuracy and methodology metadata is carried forward, and the component lineage is recorded. Registered outputs are reused; VS-05 does not repeat analysis that already exists, in line with SAF-P08.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Select and pin the correct component output versions according to the specification | Selected components | PRD-6.1 Prepare draft outputs; DLM-6 Provide data for reuse | SAF-P08 |
| Integrate the components into the product structure | Integrated product base | PRD-5.1 Integrate data; PRD-6.1 Prepare draft outputs | 1.3.6 Integrate statistics |
| Carry component accuracy and methodology metadata into the product | Propagated metadata | OVA-2 Metadata Management | SAF-P09 |
| Record the component lineage: which output versions were used | Component lineage | OVA-2 Metadata Management | CSDA Traceability |

<br>

#### VS-05.2 Construct Composite Indicators or Indices

**Value created:** *Derived measures, such as indices, ratios, and time series, that summarise the results and add meaning.*

This stage computes the designed composite indicators, indices, and time-series aggregates from the integrated components. Indicators and indices are calculated with the designed formulas and weighting. Time series are chained, linked, and benchmarked according to the specification. Each composite carries an uncertainty measure derived from the accuracy of its components. No component estimate is re-estimated: composites are built from the validated outputs as received.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Calculate composite indicators and indices with the designed formulas | Composite indicators | PRD-5.7 Calculate aggregates; PRD-5.5 Derive new variables and units | |
| Construct time series: chain, link, benchmark | Composite time series | PRD-5.7 Calculate aggregates | |
| Derive composite uncertainty from component accuracy | Composite accuracy measures | PRD-5.7 Calculate aggregates | SAF-P09 |
| Record the composition method and inputs as lineage | Composite lineage | OVA-2 Metadata Management | SAF-P09 |

<br>

#### VS-05.3 Perform Consistency and Coherence Checks

**Value created:** *Confidence that the product is internally consistent and fits the wider statistical picture.*

This stage runs the designed checks. Internal consistency checks confirm that totals reconcile to their components and that breakdowns sum to totals. Coherence checks compare the product with related statistics and with prior releases, within the designed tolerances. Each discrepancy is dispositioned according to the policy: accepted, flagged, or returned for review. A significant discrepancy is explained. Nothing is adjusted silently. If a component is wrong, it goes back to VS-04 and returns as a new analytical version. All check results are logged in the audit trail of the product.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Run internal consistency checks: totals and breakdowns reconcile | Consistency results | PRD-6.2 Validate outputs | |
| Run coherence checks against related statistics and prior releases | Coherence results | PRD-6.2 Validate outputs | 1.3.6 Integrate statistics |
| Disposition discrepancies (accept, flag, return to VS-04) and explain them | Discrepancy dispositions | PRD-6.2 Validate outputs; DLM-2 Promote data through a quality gate | |
| Log all check results in the audit trail of the product | Audit trail entries | OVA-4 Process Data Management | SAF-P10 |

|**PLACEHOLDER: VS-05 composition and coherence architecture: component outputs of several domains integrated and composed into indicators, then checked for internal consistency and for coherence, with prior-period products as comparison, resulting in a coherent product that carries its lineage and accuracy**|
|---|

<br>

#### VS-05.4 Generate Analytical and Interpretive Outputs

**Value created:** *Products that users can understand: narrative, key messages, and visualisations grounded in the data.*

This stage produces the content that makes the product understandable. The analytical narrative and commentary are written with the designed templates. Key messages are stated together with their supporting evidence. Tables and visualisations are produced. The content passes the editorial and quality review, which checks that it is accurate, in plain language, accessible, and consistent with the data and its caveats, including the accuracy carried from VS-04. The review makes sure that the text does not overstate a movement that is not statistically significant.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Write the analytical narrative and commentary with the templates | Product narrative | PRD-6.3 Interpret and explain outputs | 1.4.1 Statistical (output) analysis |
| State key messages with their supporting evidence | Key messages | PRD-6.3 Interpret and explain outputs | |
| Produce tables and visualisations | Tables and visualisations | PRD-7.2 Produce dissemination products | |
| Run the editorial and quality review of the content | Reviewed content | PRD-7.2 Produce dissemination products; OVA-1 Quality Management | GAMSO Quality Management |

<br>

#### VS-05.5 Approve and Register Statistical Products

**Value created:** *A validated, approved, and registered product, ready for dissemination.*

This stage validates, approves, and registers the product. The product is checked against the dissemination and confidentiality standards. This includes the disclosure risk that arises from combining outputs: two tables that are each safe can together reveal a value. The product is then submitted to the designated approval authority. On approval, a persistent, immutable product version is created with a unique identifier and full lineage: components, composition method, coherence results, and approval record. Its metadata is registered in line with SAF-P09, and access permissions are applied in line with SAF-P10. The stage ends by publishing the *Statistical Product Registered* event, which tells VS-06 that an approved product is available for dissemination. If the product is not approved, it is revised, or a component is returned to VS-04.

**Output:** **Approved statistical product (State #4, approved)**, the official handover artefact to the dissemination domain. Its minimum metadata set is described in *State #4: Statistics*.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Validate the product against dissemination and confidentiality standards, including the risk of combining outputs | Validation result | PRD-6.4 Apply disclosure control; PRD-6.5 Finalise outputs | SAF-P11; 1.3.7 Statistical disclosure |
| Submit the product to the approval authority and obtain sign-off | Approval record | PRD-6.5 Finalise outputs | 4.1.5 Accountability |
| Create an immutable, identified product version with full lineage | Versioned product | DLM-3 Register and catalogue data; DLM-5 Store and version data | CSDA Traceability |
| Apply access permissions to the approved version | Access-controlled product | DLM-4 Classify and protect data | SAF-P10 |
| Register metadata and publish the *Statistical Product Registered* event to notify VS-06 | Catalogue registration, event | DLM-3 Register and catalogue data | SAF-P07 |

Each product version is linked to four records, all traceable to the analytical #4 versions it was composed from.

| Product record | Content |
|---|---|
| Statistical product | Persistent identifier, immutable version, product type (publication, index, time series, dataset), reference period, registration timestamp |
| Component lineage (one per component) | Analytical #4 version used, domain or source, composition method, accuracy carried |
| Coherence result | Internally consistent, coherent with related statistics, coherent over time, number of flagged discrepancies |
| Interpretive content | Narrative reference, key messages with evidence, tables and charts, editorial review passed |
| Approval record | Approval authority, confidentiality cleared, approval timestamp, cleared for dissemination |

### 4. The four process types

The sub-processes below are specific to VS-05. Each refines one or more SAF business processes, listed as *Refines*, which keeps it traceable to *Business Processes*. Sub-processes marked *(standard)* work as described in [Standard activities in every value stream](#standard-vs-activities); only the VS-05 specifics are listed.

#### Design: provides metadata

| Design sub-process | Refines | Main outputs |
|---|---|---|
| Design the Statistical Product Portfolio | PRD-2.1 Design outputs and dissemination; PRD-2.5 Design processing and analysis; DLM-1 Plan and design data assets; OVA-2 Metadata Management | Product specification, component-selection specification, metadata-propagation rules, product metadata standard |
| Design Composite Indicators and Indices | PRD-2.5 Design processing and analysis; OVA-2 Metadata Management | Composite-indicator specification, time-series specification, uncertainty-representation rules |
| Design Consistency and Coherence Checks | PRD-2.5 Design processing and analysis; DLM-7 Revise data; OVA-1 Quality Management | Consistency and coherence check sets, coherence tolerance policy, revision policy |
| Design Analytical and Interpretive Content | PRD-2.1 Design outputs and dissemination; OVA-1 Quality Management | Content templates, visualisation specification, key-message guidelines, editorial review policy |
| Design Approval, Confidentiality, and Versioning Framework | PRD-2.5 Design processing and analysis; PRD-2.6 Design production systems and workflows; DLM-1 Plan and design data assets; DLM-4 Classify and protect data | Approval policy, confidentiality standard, versioning and lineage policy, access control design |

##### Design the Statistical Product Portfolio

*Refines:* PRD-2.1 Design outputs and dissemination; PRD-2.5 Design processing and analysis; DLM-1 Plan and design data assets; OVA-2 Metadata Management.

The starting point is deciding which products will be produced. This sub-process specifies each statistical product: its purpose, target users, content, structure, breakdowns, release frequency, and the analytical #4 outputs it draws on. The team designs how component outputs are selected and integrated (which estimates, which domains, which time periods) and how their accuracy metadata is carried into the product. Each product also gets its classification and versioning identity. Without product specifications, composition becomes ad hoc, and Management has no baseline to measure coherence and interpretability against.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Specify each product: purpose, users, content, structure, breakdowns, frequency | Product specification | PRD-2.1 Design outputs and dissemination | 1.1.2 Design statistics product |
| Define the component outputs each product draws on, and the selection rules | Component-selection specification | PRD-2.5 Design processing and analysis | SAF-P08 |
| Define how component accuracy and quality metadata is carried into the product | Metadata-propagation rules | OVA-2 Metadata Management | SAF-P09 |
| Define the product classification and versioning identity | Product metadata standard | DLM-1 Plan and design data assets; OVA-2 Metadata Management | SAF-P09 |

##### Design Composite Indicators and Indices

*Refines:* PRD-2.5 Design processing and analysis; OVA-2 Metadata Management.

This sub-process specifies the derived measures that the products present: composite indicators, indices, ratios, and time-series aggregates. Each is defined by its formula, component inputs, weighting or aggregation method, and base period. Time series get chaining, linking, and benchmarking rules. Each composite gets the metadata and classification it carries. Where a composite combines outputs of differing accuracy, the design specifies how its uncertainty is represented. International standards, such as index manuals, inform the specifications.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Specify composite indicators and indices: formula, inputs, weighting, base period | Composite-indicator specification | PRD-2.5 Design processing and analysis | Index manuals |
| Specify time-series construction: chaining, linking, benchmarking | Time-series specification | PRD-2.5 Design processing and analysis | |
| Define how component uncertainty is represented in composites | Uncertainty-representation rules | PRD-2.5 Design processing and analysis | SAF-P09 |
| Define the metadata and classification of each composite | Composite metadata standard | OVA-2 Metadata Management | SAF-P09 |

##### Design Consistency and Coherence Checks

*Refines:* PRD-2.5 Design processing and analysis; DLM-7 Revise data; OVA-1 Quality Management.

This sub-process designs the checks that make sure integrated products are sound. It specifies internal consistency checks: totals reconcile to components, and breakdowns sum to totals. It specifies coherence checks against related statistics, such as the national accounts and prior products, and across time. Tolerance thresholds and disposition rules (accept, flag, return for review) complete the check set. The revision policy for products is also designed here.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define internal consistency checks: totals and breakdowns reconcile | Consistency check set | PRD-2.5 Design processing and analysis | |
| Define coherence checks against related statistics and across time | Coherence check set | PRD-2.5 Design processing and analysis; OVA-1 Quality Management | GAMSO Quality Management |
| Define tolerance thresholds and disposition rules | Coherence tolerance policy | PRD-2.5 Design processing and analysis | |
| Define the product revision policy | Revision policy | DLM-7 Revise data; OVA-1 Quality Management | GAMSO Quality Management |

##### Design Analytical and Interpretive Content

*Refines:* PRD-2.1 Design outputs and dissemination; OVA-1 Quality Management.

This sub-process designs the content that makes products interpretable for people. It specifies the structure of the analytical narrative and commentary, the visualisations and tables, the key messages and the evidence they require, and the editorial and quality review of the content. Accessibility and plain-language standards are part of the design.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Specify the structure of the analytical narrative and commentary | Content template | PRD-2.1 Design outputs and dissemination | |
| Specify visualisations and tables | Visualisation specification | PRD-2.1 Design outputs and dissemination | |
| Define key messages and their evidence requirements | Key-message guidelines | PRD-2.1 Design outputs and dissemination | |
| Define the editorial and quality review of content | Editorial review policy | OVA-1 Quality Management | GAMSO Quality Management |

##### Design Approval, Confidentiality, and Versioning Framework

*Refines:* PRD-2.5 Design processing and analysis; PRD-2.6 Design production systems and workflows; DLM-1 Plan and design data assets; DLM-4 Classify and protect data.

The last design sub-process makes sure that products are properly approved, protected, and traceable. It defines the approval workflow and the approval authority. It defines the confidentiality and disclosure standards that a product must meet before registration, including the risk of combining outputs. It sets the product versioning policy (identity, revision triggers, immutability, retention) and the lineage required from each product to its component outputs. Role-based access control for products is designed in line with SAF-P10.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define the approval workflow and the approval authority | Approval policy | PRD-2.6 Design production systems and workflows | 4.1.5 Accountability |
| Define confidentiality and disclosure standards for products, including the risk of combining outputs | Confidentiality standard | PRD-2.5 Design processing and analysis | SAF-P11; 3.3.1 Privacy management |
| Define product versioning and lineage requirements | Versioning and lineage policy | DLM-1 Plan and design data assets | CSDA Traceability |
| Design role-based access control for products | Access control design | DLM-4 Classify and protect data | SAF-P10; 3.3.4 Logical identity and access control |

|**PLACEHOLDER: VS-05 design process decomposition: inputs (analytical #4 outputs with accuracy, user needs, framework standards, product and index standards such as SDMX and index manuals), the five design sub-processes in order, and the design artefact each produces, which together govern Implementation, Execution, and Management**|
|---|

#### Implementation: provides the execution process

| Implementation sub-process | Refines | Main outputs |
|---|---|---|
| Build Integration and Composition Engines | PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows | Configured integration and composition engines, pinned connections to the State #4 catalogue |
| Build Indicator-Construction and Time-Series Engines | PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows | Indicator-construction engine, time-series engine, composite-accuracy component |
| Build Coherence-Check, Content, and Approval Tooling | PRD-3.2 Reuse or build processing and analysis components; PRD-3.3 Reuse or build dissemination components; PRD-3.4 Configure workflows; DLM-5 Store and version data | Coherence tooling, content tooling, approval and versioning store, event publication |
| Test and Validate the Pipeline *(standard)* | PRD-3.5 Test production systems; PRD-3.6 Test statistical business process; PRD-3.7 Finalise production systems | Test reports; integration test from output intake through composition, coherence checks, content, and approval to registration; coherence test: composites reconcile to components and cohere with prior products; reproducibility test: a product regenerates identically from its component versions plus the composition method |

##### Build Integration and Composition Engines

*Refines:* PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows.

This sub-process turns the product and integration designs into operational tools. The integration engine selects and combines the designed component outputs into the product structure, with their accuracy and quality metadata. The composition engine assembles products from their components according to the specifications. Connections to the State #4 catalogue use version pinning, so the exact component versions used are recorded. All composition logic is version-controlled, in line with SAF-P10.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Build or configure the integration engine: select and combine component outputs | Configured integration engine | PRD-3.2 Reuse or build processing and analysis components | 1.1.3 Build statistics product |
| Build or configure the composition engine: assemble products from components | Configured composition engine | PRD-3.2 Reuse or build processing and analysis components | |
| Configure pinned connections to the State #4 output catalogue | Output-source integration | PRD-3.4 Configure workflows | CSDA Metadata Management |
| Put all composition logic under version control | Versioned composition repository | PRD-3.4 Configure workflows | SAF-P10 |

##### Build Indicator-Construction and Time-Series Engines

*Refines:* PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows.

The designed composite-indicator and time-series specifications are implemented. Indicator and index calculators are built from the designed formulas and weighting. Time-series engines are configured for chaining, linking, and benchmarking. Uncertainty representation is implemented, so that composites carry an appropriate accuracy measure. Every composite output is produced with its method and inputs attached.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Build indicator and index calculators from the designed formulas | Indicator-construction engine | PRD-3.2 Reuse or build processing and analysis components | |
| Configure time-series chaining, linking, and benchmarking | Time-series engine | PRD-3.2 Reuse or build processing and analysis components | |
| Implement uncertainty representation for composites | Composite-accuracy component | PRD-3.2 Reuse or build processing and analysis components | SAF-P09 |
| Attach the method and inputs to every composite | Composite metadata binding | PRD-3.4 Configure workflows | SAF-P09 |

##### Build Coherence-Check, Content, and Approval Tooling

*Refines:* PRD-3.2 Reuse or build processing and analysis components; PRD-3.3 Reuse or build dissemination components; PRD-3.4 Configure workflows; DLM-5 Store and version data.

This sub-process implements the coherence checks, the content tooling, and the approval and versioning store. Coherence tooling implements the designed internal consistency checks and the checks across sources and time, with their tolerances. Content tooling supports the analytical narrative, tables, and visualisations according to the templates, with the editorial review workflow. The approval and versioning store makes each approved product version immutable, identified, reproducible from its components plus method, and accompanied by its lineage and approval record. Event notifications are configured to alert VS-06 when a product is approved and registered.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Implement consistency and coherence checks with their tolerances | Coherence tooling | PRD-3.2 Reuse or build processing and analysis components | |
| Build content and visualisation tooling with the editorial workflow | Content tooling | PRD-3.3 Reuse or build dissemination components | |
| Build the approval and versioning store: immutable, identified, reproducible | Approval and versioning store | PRD-3.4 Configure workflows; DLM-5 Store and version data | CSDA Traceability |
| Configure the *Statistical Product Registered* event for downstream consumers | Event publication | PRD-3.4 Configure workflows | SAF-P07 |

|**PLACEHOLDER: VS-05 implementation pipeline: the five design artefacts feeding the three build sub-processes, followed by technical testing, coherence test, and reproducibility test, resulting in an operational composition pipeline and operational procedures**|
|---|

#### Execution: provides the statistical data

Execution runs the stages of VS-05 for every product release. The stages and their activities are described in attribute 3. A cycle starts when the analytical versions a product needs have been registered, and it is planned against the release calendar. Execution applies the designs and the solution as they are; a new composite, check, or template goes back to Design. A coherence problem is never solved inside VS-05 by changing a component: the component goes back to VS-04.

| Aspect | VS-05 |
|---|---|
| Trigger | *Output Data Registered* for the components of a product |
| Cadence | Per product release, according to the release calendar |
| Performed by | ROL-10 Data engineer (integration), ROL-15 Subject-matter statistician, ROL-17 Release manager (approval authority), ROL-03 Data steward |
| Input | Registered analytical #4 versions and their metadata |
| Output | Registered approved #4 version with composition record, coherence results, interpretive content, and approval record |
| Control point | Coherence checks in VS-05.3; approval gate of State #4 in VS-05.5 |
| Exception path | Component that fails the coherence check returned to VS-04 for a new analytical version; product not approved revised and resubmitted; need for a new composite or check back to Design |

#### Management: provides quality reports

| Management sub-process | Refines | Main outputs |
|---|---|---|
| Monitor Process Performance *(standard)* | OVA-4 Process Data Management; PRD-8.1 Gather evaluation inputs | Process performance dashboard; throughput report against the release calendar; paradata on component versions and methods used and on approval iterations |
| Assess Product Quality | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use | Coherence report, interpretability review, product completeness report, quality trend analysis |
| Manage Product and Version Lifecycle | OVA-2 Metadata Management; DLM-5 Store and version data; DLM-8 Monitor data quality, lineage and use | Product version register, metadata quality report, version store audit, metadata lineage audit |
| Audit and Compliance Reporting *(standard)* | OVA-1 Quality Management; OVA-4 Process Data Management; DLM-8 Monitor data quality, lineage and use | Reproducibility audit: every product regenerates from its component versions plus the composition method (4.1.5 Accountability); approval and confidentiality report confirming that every registered product was approved by the designated authority and meets the confidentiality standard, including the risk of combining outputs (SAF-P11); standards compliance report on product and exchange standards, such as SDMX; security compliance report on access controls and the integrity of the approval record (SAF-P10) |
| Continuous Improvement *(standard)* | PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan | Improvement recommendations, for example refined composite-indicator methods, coherence checks that produce fewer false alarms, a streamlined approval workflow, better visualisations, and more reuse of validated outputs; trends watched: coherence issues, approval iterations, component reuse, interpretability |

##### Assess Product Quality

*Refines:* OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use.

Beyond process performance, the quality of the products themselves is evaluated against the criteria set in Design. Each product is assessed on four dimensions. Coherence covers internal consistency and consistency with related and prior statistics. Interpretability covers the clarity and accuracy of narrative and visualisations. Completeness checks that all designed content is present. Accuracy propagation checks that component accuracy was carried correctly. Quality indicators are produced per product and per cycle, and trends are tracked to detect recurring coherence issues or interpretive weaknesses. This follows the Data Quality capability of CSDA and SAF capability 2.1.3 *Statistical quality management*.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Evaluate coherence: internal, and with related and prior statistics | Coherence report (per cycle) | OVA-1 Quality Management | 2.1.3 Statistical quality management |
| Assess the interpretability of narrative and visualisations | Interpretability review | OVA-1 Quality Management | CSDA Data Quality |
| Check completeness and correct accuracy propagation | Product completeness report | DLM-8 Monitor data quality, lineage and use | 2.1.3 Statistical quality management |
| Identify quality trends across products and cycles | Quality trend analysis | DLM-8 Monitor data quality, lineage and use | 2.1.3 Statistical quality management |

##### Manage Product and Version Lifecycle

*Refines:* OVA-2 Metadata Management; DLM-5 Store and version data; DLM-8 Monitor data quality, lineage and use.

The product portfolio and the versions it produces must stay current, complete, and well governed. This sub-process governs the life cycle of product specifications, composite-indicator definitions, and content templates. It versions them, manages transitions such as the rebasing of an index, and retires obsolete products. It verifies that every product carries full component lineage, composition method, coherence results, and approval record, as a compliance check on SAF-P09. It governs the product version store: retention, immutability, and reconciliation of catalogue entries with stored versions. Metadata lineage from outputs through composition to products is tracked.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Govern the life cycle and versions of products, indicators, and templates | Product version register | OVA-2 Metadata Management | SAF-P09 |
| Verify metadata completeness: component lineage, method, coherence results, approval | Metadata quality report | OVA-2 Metadata Management | SAF-P09 |
| Govern the product version store: retention, immutability, reconciliation | Version store audit | DLM-5 Store and version data | CSDA Traceability |
| Track metadata lineage from outputs to products | Metadata lineage audit | DLM-8 Monitor data quality, lineage and use | CSDA Traceability |

|**PLACEHOLDER: VS-05 management feedback loop: data and paradata from Execution flowing through the five management sub-processes (coherence pass rate and timeliness, coherence and interpretability, products and versions, reproducibility and approval), with dashboards to the process owner, quality reports to the quality manager, compliance reports to VS-07, and improvement recommendations back to Design**|
|---|

#### Metadata per process type

In this domain, metadata is what makes a composite product interpretable: each product must carry its components, methodology, coherence results, and approval. The table shows the data metadata each process type of VS-05 contributes; the paradata are listed in [Standard activities in every value stream](#standard-vs-activities). In Execution, VS-05 also records the approval workflow trail and the number of approval iterations as paradata, and in Implementation the outcomes of the coherence tests.

| Process type | Data metadata produced |
|---|---|
| Design | Product specifications, composite-indicator definitions, coherence criteria, approval and confidentiality policy |
| Implementation | Integration configurations, indicator-construction parameters, coherence-check parameters, product templates |
| Execution | Component lineage, composition and indicator method, coherence-check results, interpretive content, and approval record per product |
| Management | Coherence and interpretability assessments, product quality scores, lineage assessments, trend analyses |

|**PLACEHOLDER: VS-05 business object lifecycle: design artefacts govern implementation assets (integration and composition engines, indicator engines, coherence and content tooling, approval store), which produce the process that composes analytical #4 versions into approved statistical products, generating component lineage, coherence results, and approval records that management assesses and feeds back to design**|
|---|

### 5. Actors and roles

VS-05 is mostly internal: it receives its input from VS-04, and the process owner of VS-04 remains the data owner of the analytical versions. The table shows the actors and the reference roles involved. Specialised role names used in an NSI map onto these reference roles (see *Role names in the value streams*); for example, the product manager and the coherence designer in the original VS-05 description are ROL-06 Statistical designer, and the approval authority is ROL-17 Release manager. Design work is typically carried out by the collaboration COL-05 *Statistical product team*.

| Actor or role | ID | Process type | Responsibility in VS-05 |
|---|---|---|---|
| International statistical organisation (standards body) | ACT-07 | External | Maintains the product, indicator, and exchange standards the NSI conforms to, such as SDMX and index manuals |
| Process owner | ROL-01 | Management | Accountable for the end-to-end performance of VS-05 |
| Data owner | ROL-02 | Management | Process owner of Product Composition; accountable for the coherence and interpretability of approved #4 versions |
| Data steward | ROL-03 | Execution | Registers approved products and versions, manages metadata entries, applies access controls |
| Data custodian | ROL-04 | Execution | Operates the product version store and keeps the pre-release access log |
| Statistical designer | ROL-06 | Design | Designs the product portfolio, product specifications, and release content (product manager); designs the consistency and coherence checks (coherence designer) |
| Methodologist | ROL-07 | Design | Specifies composite indicators, indices, and time-series construction methods (indicator and index methodologist) |
| Data engineer | ROL-10 | Implementation, Execution | Builds and configures the integration, indicator-construction, and reporting engines; in each cycle, selects and integrates the component outputs into the product structure (integration specialist) |
| Platform engineer | ROL-11 | Implementation | Configures composition services, output-source connections, and access controls |
| Test manager | ROL-12 | Implementation | Plans and carries out testing of the composition pipeline: technical, coherence, and reproducibility tests |
| Subject-matter statistician | ROL-15 | Execution | Produces the analytical and interpretive content: commentary, key messages, and visualisations (subject-matter author) |
| Disclosure control specialist | ROL-16 | Design, Execution | Defines and checks the confidentiality standard for products, including the disclosure risk of combining outputs |
| Release manager (approval authority) | ROL-17 | Execution | Validates products against the dissemination and confidentiality standards and approves them for registration and release |
| Quality manager | ROL-18 | Management | Monitors coherence and interpretability indicators, produces quality reports, and drives continuous improvement |
| Compliance officer | ROL-19 | Management | Ensures confidentiality and standards compliance of products and produces audit reports |

### 6. Capabilities, processes, and functions

#### Capability foundations

The table shows which capabilities from the SAF capability model VS-05 relies on, and what role they play. NSIs can use it to map the value stream to their own organisation.

| Capability group | Capabilities | Role in VS-05 |
|---|---|---|
| 1.1 Statistical design and build | 1.1.2 Design statistics product, 1.1.3 Build statistics product | Design the statistical products and composite indicators, and build the composition pipeline |
| 1.3 Processing | 1.3.6 Integrate statistics, 1.3.7 Statistical disclosure | Integrate separate statistics into a coherent product, and check the disclosure risk of the combined product |
| 1.4 Analysis | 1.4.1 Statistical (output) analysis | Validate, interpret, and explain the product, and finalise it for dissemination |
| 2.1 Data management | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management, 2.1.4 Statistical register management | Manage products, metadata, and quality; assess coherence; integrate across registers and time |
| 3.2 Computerisation and automation | 3.2.1 Application development, 3.2.2 Functional management | Build and maintain the integration, indicator-construction, and reporting and visualisation engines |
| 3.3 Security and privacy | 3.3.1 Privacy management, 3.3.2 Security planning | Validate products against confidentiality standards and assess the disclosure risk of composite products |
| 4.1 Governance | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improvement management, 4.1.5 Accountability | Govern the domain, steward product approval, plan improvements, report on compliance |

#### Stages, processes, and functions

The table shows which SAF business processes realise each stage of VS-05 and which business functions they mainly use.

| Stage | Realised by processes | Main functions |
|---|---|---|
| VS-05.1 Select and Integrate Source Datasets | PRD-5.1 Integrate data; PRD-6.1 Prepare draft outputs | FUN-3.4 Estimate and analyse |
| VS-05.2 Construct Composite Indicators or Indices | PRD-5.5 Derive new variables and units; PRD-5.7 Calculate aggregates | FUN-3.3 Process statistical data; FUN-3.4 Estimate and analyse |
| VS-05.3 Perform Consistency and Coherence Checks | PRD-6.2 Validate outputs | FUN-3.4 Estimate and analyse; FUN-5.2 Assure and review quality |
| VS-05.4 Generate Analytical and Interpretive Outputs | PRD-6.3 Interpret and explain outputs; PRD-7.2 Produce dissemination products | FUN-3.4 Estimate and analyse; FUN-3.6 Disseminate statistics |
| VS-05.5 Approve and Register Statistical Products | PRD-6.4 Apply disclosure control; PRD-6.5 Finalise outputs; DLM-3 Register and catalogue data | FUN-3.4 Estimate and analyse; FUN-3.5 Protect statistical confidentiality; FUN-7.2 Manage metadata |

|**PLACEHOLDER: ArchiMate view VS-05 (b) stages realised by processes and functions**|
|---|

#### Framework mappings

This reference table maps each process type of VS-05 to the SAF business processes, the international frameworks (GSBPM, GAMSO, CSDA), and the SAF capability model. It is intended for architects and auditors; the rest of this section does not depend on it.

| Process type | SAF business processes | GSBPM | GAMSO | CSDA | SAF capabilities |
|---|---|---|---|---|---|
| Design | PRD-2.1, PRD-2.5, PRD-2.6, DLM-1, DLM-4, DLM-7, OVA-1, OVA-2 | Phase 2 Design (2.1, 2.5, 2.6) | Production (design activities), Capability Management | Data Governance, Metadata Management, Data Quality | 1.1.2 Design statistics product, 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| Implementation | PRD-3.2 to PRD-3.7, DLM-5 | Phase 3 Build (3.2 to 3.7) | Capability Management | Data Processing and Dissemination preparation (set-up), Data Governance (configuration) | 1.1.3 Build statistics product, 3.2.1 Application development, 3.2.2 Functional management |
| Execution | PRD-5.1, PRD-5.5, PRD-5.7, PRD-6.1 to PRD-6.5, PRD-7.2, DLM-2 to DLM-6, OVA-2, OVA-4 | Phase 6 Analyse (6.1 to 6.5), 7.2 Produce dissemination products; the business domain table also lists 7.1 Update output systems | Production (execution) | Data Analysis and Dissemination preparation (execution) | 1.3.6 Integrate statistics, 1.4.1 Statistical (output) analysis, 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| Management | OVA-1, OVA-2, OVA-4, DLM-5, DLM-8, PRD-8.1 to PRD-8.3 | Phase 8 Evaluate; overarching Quality Management and Metadata Management | Corporate Support (Quality, Data, and Metadata Management), Capability Management (improvement) | Data Quality, Data Governance, Traceability | 2.1.3 Statistical quality management, 4.1.4 Improvement management, 4.1.5 Accountability |

### 7. Principles

The following principles govern VS-05 most directly.

| Principle | Statement | Application in VS-05 |
|---|---|---|
| SAF-P01 | Actively participate in open-source communities to maintain collective control over statistical processes | Composition, indicator-construction, and reporting and visualisation tooling is reused and developed in open-source communities with other NSIs, so that the NSI keeps collective control over critical product capabilities instead of depending on vendors. |
| SAF-P07 | Implement loosely coupled processes and systems | Composition is independent from upstream estimation and downstream dissemination. The approved statistical product is the decoupling interface: VS-06 uses it without knowing how it was composed. |
| SAF-P08 | Data is shared property | Approved products and their components, once registered, are available to all authorised consumers. Composition reuses existing validated outputs instead of duplicating analysis. |
| SAF-P09 | No data without metadata and classification | Every product carries its component outputs and their accuracy, the composition and indicator method, the coherence results, its classification, and the approval record. This is what makes products interpretable and trustworthy. |
| SAF-P10 | Security By Design | Access controls, integrity verification, and a tamper-evident composition and approval record are built into the pipeline, so that every product is attributable and reproducible. |
| SAF-P11 | Privacy By Design | Products are validated against confidentiality standards. The disclosure risk of composite products, including the risk of combining outputs, is assessed by design before registration. |

::: {.callout-note title="Principles that apply across the process types"}
SAF-P09 underpins interpretability in all four process types: Design defines the product and its required metadata, Execution captures component lineage, composition method, and coherence results, and Management assesses product quality. SAF-P10 governs the tamper-evident composition and approval record across the stages VS-05.1 to VS-05.5. SAF-P11 applies especially to VS-05.5, where the confidentiality and disclosure risk of the composite product are confirmed before registration. SAF-P07 governs both the intake of analytical versions from VS-04 and the handover of approved versions to VS-06.
:::

### 8. Interfaces, services, and events

**Boundary interfaces**

VS-05 has two boundary interfaces, both within State #4: intake of analytical versions from VS-04, and handover of approved versions to VS-06.

| Boundary | Handed over | Required metadata | Trigger | Responsibility transfer |
|---|---|---|---|---|
| VS-04 → VS-05 (intake) | Registered analytical #4 version | Methodology and parameters, weights, accuracy measures, model diagnostics, applied disclosure control record, output version identifier, lineage to the processed source (#3), classification | *Output Data Registered* | VS-04 keeps custody of the analytical version; VS-05 takes responsibility for composition and approval on receipt of the event |
| VS-05 → VS-06 (handover) | Registered approved #4 version (statistical product) | Component lineage, composition and indicator method, propagated accuracy, coherence results, interpretive content, approval record, confidentiality status, product version identifier, classification | *Statistical Product Registered* | VS-05 keeps custody of the product version; VS-06 takes responsibility for final disclosure control, release, and user support on receipt of the event |

**Business services**

| Service | Offered to | Realised in | Interfaces |
|---|---|---|---|
| Integration and composition service | Composition teams, consumers of output data | VS-05.1 Select and Integrate Source Datasets | Pinned connections to the State #4 output catalogue |
| Indicator and index service | Composition teams, methodologists | VS-05.2 Construct Composite Indicators or Indices | Composite construction interface and a query interface for methodology and parameters |
| Coherence validation service | Quality managers, subject-matter statisticians | VS-05.3 Perform Consistency and Coherence Checks | Coherence results and discrepancy dispositions |
| Analytical content service | Authors, editors, VS-06 Dissemination and Service Delivery | VS-05.4 Generate Analytical and Interpretive Outputs | Content and visualisation tooling with editorial workflow |
| Product provisioning service | VS-06 Dissemination and Service Delivery | VS-05.5 Approve and Register Statistical Products | Event notification (*Statistical Product Registered*) and a catalogue query interface to find and access approved products, their lineage, and their accuracy |
| Product catalogue service | All data consumers in the NSI | Management sub-process *Manage Product and Version Lifecycle* | Search and browse interface for products, component lineage, coherence results, and approval records |
| Design and methodology service | Statistical designers, methodologists | All Design sub-processes of VS-05 | Design documents, methodology advice |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Design artefacts published* | Start of Implementation after a design change |
| *Pipeline production-ready* | End of Implementation; Execution can start |
| *Output Data Registered* | Start of VS-05.1 for the products that use that analytical version |
| *Statistical Product Registered* | Completion of VS-05.5 after approval; triggers VS-06. A product that is not approved is revised, or a component is returned to VS-04 |
| *Improvement recommendations issued* | Input for Design from *Continuous Improvement* |

|**PLACEHOLDER: VS-05 event choreography between VS-04, NSI teams, and process management across Design, Implementation, Execution (output data registered, integrate and compose, coherence checks and interpretive content, approval granted or refused), and Management (coherence and timeliness monitoring, product quality, audit reports, improvement recommendations)**|
|---|

**Interaction with the supporting value streams**

| Value stream | Provides to VS-05 | Receives from VS-05 |
|---|---|---|
| VS-07 Governance and Compliance | Confidentiality and approval policies, revision policy framework | Reproducibility audits, approval and confidentiality compliance reports |
| VS-08 Innovation and Methodological Development | New composite-indicator and time-series methods | Improvement needs |
| VS-09 Infrastructure and Platform Enablement | Composition and content tooling, version store, catalogue, event interfaces | Capacity and tooling requirements |
| VS-10 Customer and Stakeholder Engagement | User needs for products and content | Product portfolio, feedback on interpretability |

### 9. Key performance indicators

The key performance indicators are collected per production cycle in *Monitor Process Performance*. They feed the dashboard that the process owner reviews.

| KPI | Description | Measurement |
|---|---|---|
| On-time product rate | Products composed within the release-calendar window | Per product, per cycle |
| Coherence-check pass rate | Products passing the coherence checks on the first run | Per product, per cycle |
| Approval iteration count | Number of approval cycles before sign-off | Per product, per cycle |
| Component reuse rate | Share of products that reuse existing validated outputs | Per cycle |
| Reproducibility rate | Share of products that regenerate from components plus method | Per cycle |
| Processing time | Time from output intake to product registration | Per product, per cycle |

### 10. Examples

**Labour market publication.** The quarterly labour market publication is specified to combine the Labour Force Survey employment-rate estimates (national and NUTS-2), the unemployment series, and administrative job-vacancy figures into one coherent release, with the confidence interval of each component carried into the published tables. For Q3 2026, the team selects the validated `OD-LFS-2026Q3` employment and unemployment outputs and the latest administrative vacancy output, and pins their exact versions. The commentary explains a 0.3 percentage point rise in the employment rate, notes that it is within the confidence interval, and presents a regional map and a time-series chart. The editorial review confirms that the wording does not overstate a movement that is not statistically significant.

**Business statistics product.** The composite structural business statistics product integrates the register-based aggregates and the survey-based estimates for the same NACE by region domains. The engine pins the exact `OD-BUS` output versions and carries their accuracy metadata into the combined tables. In the coherence checks, NACE-class turnover sums to the published total, the survey-based and register-based components agree within tolerance for overlapping domains, and the series is coherent with the prior year. One domain exceeds the tolerance and is returned to VS-04 for review instead of being adjusted in the product.

**Consumer price index.** The headline consumer price index is composed from the validated item indices with the designed weighting and chaining. The all-items index and its main divisions are constructed, and each carries its method and the period weights used.

| **Toolkit:** SAF-TK-V05 VS-05 maturity checklist and scenarios |
|---|



## VS-06 Dissemination and Service Delivery

### 1. Purpose and value created

VS-06 is the exit point of the statistical value chain. It takes approved statistical products and makes them available to policy makers, researchers, journalists, businesses, and the public through trusted, secure channels: publications, open data, APIs, dashboards, deliveries to international organisations, data spaces, and secure access to microdata for research. It does not change the statistics. It protects them with final disclosure control, formats them for each channel, documents them, releases them at the same moment for everyone, and helps users interpret them correctly. The value created is **impact and accessibility**: statistics that users can find, trust, and use responsibly, which turns statistical output into societal value through informed decisions, evidence-based policy, and transparency.

Composing and approving statistical products is not part of VS-06; it belongs to VS-05. VS-06 only disseminates products that have already been approved and registered. The technical platforms for portals, APIs, dashboards, and secure research environments are provided by VS-09.

::: {.callout-note title="Signature discipline: accessibility, trust, and the release gate"}
Accurate, timely, and understandable delivery through secure channels, gated by **final statistical disclosure control**: no release without confidentiality clearance. Documentation and user services support responsible use. Equal access to released statistics, through managed release timing and embargo discipline, and accessibility, through formats, languages, and machine-readability, are explicit obligations.
:::

VS-06 corresponds to the business domain **Dissemination** (see *Steady-State Architecture, Business domains*). This section describes the business layer of that domain for all four process types: Design, Implementation, Execution, and Management.

|**PLACEHOLDER: ArchiMate view VS-06 (a) value stream and capabilities**|
|---|

<br>

### 2. Position and state transition

VS-06 is the sixth and last primary value stream. It receives approved statistical products from VS-05 and has no downstream primary value stream. Its handover is to users outside the NSI, and its feedback path runs to VS-10.

VS-06 takes data from State #4 (approved version) to State #5. Before VS-06, the product is an approved, registered version that is still restricted and usually market-sensitive. It carries the metadata that VS-05 attached: component lineage, composition method, propagated accuracy, coherence results, the approval record, and the confidentiality status. VS-06 applies the final disclosure control for release, beyond the initial disclosure control of VS-04 and the standards check of VS-05. After VS-06, the output is released data, documented for correct interpretation and available through the agreed channels. Once users take it into their own environment, it becomes consumed data (boundary position #6), outside the NSI's control. The quality gate, the minimum metadata set, and the protection of State #5 are described in *State #5: Released Data* and are not repeated here.

| From | To | Gate | Event out |
|---|---|---|---|
| #4 Statistics (approved) | #5 Released Data | Gate of State #5 (approved source, final disclosure control, de-identification, documentation, format and accessibility, release authorisation, timing and equal access, metadata) | *Statistics Released* |

|**PLACEHOLDER: ArchiMate view VS-06 (c) state handover and events: the approved product (#4) from VS-05, the dissemination service at the boundary (final disclosure control and formatting, publication, access, user support, monitoring), Released Data (#5) under NSI control, and Consumed Data (#6) with users outside the NSI, with usage and feedback flowing back to VS-06.5 and VS-10**|
|---|

<br>

### 3. Stages

The stages describe the value that VS-06 adds in every release cycle. Together they form the execution process type of VS-06. In a mature steady state, the strategy, the disclosure rules, and the channels have been designed and built in advance (see attribute 4). Execution then focuses on running the release, serving users, and monitoring use, with final disclosure control as the gate that must be passed before anything is published.

| Stage | Name | Value added |
|---|---|---|
| VS-06.1 | Plan Dissemination and Access Strategy | Target users, channels, formats, and release timing are set for the release |
| VS-06.2 | Prepare Data for Dissemination | The output is disclosure-safe and in the right format for each channel |
| VS-06.3 | Publish and Provide Access Services | Users can find and access the output, equally and on time (State #5) |
| VS-06.4 | Support and Engage Users | Users understand and use the output correctly |
| VS-06.5 | Monitor Usage and Feedback | The NSI knows how its output is used and valued |

Each stage below is described with its activities. The column *SAF process* shows the business process from *Business Processes* that the activity belongs to. The column *Other reference* shows the principles, capabilities, or external frameworks that the activity applies.

<br>

#### VS-06.1 Plan Dissemination and Access Strategy

**Value created:** *The right channels, formats, and timing confirmed for this release.*

Execution starts when the *Statistical Product Registered* event arrives from VS-05. In a mature steady state, the Design process *Design Dissemination and Access Strategy* has already set the strategy. Each cycle therefore confirms the plan for this release rather than creating it. The team confirms the channels, the formats, and the slot in the release calendar for the product. It verifies the embargo and equal-access arrangements, and confirms the target user groups and the communication plan. A significant change, such as a new channel or a policy change, goes back to design instead of being solved during the cycle.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Confirm channels, formats, and release calendar slot for the product | Confirmed release plan | PRD-2.1 Design outputs and dissemination | 1.5.1 Publication management |
| Verify embargo and equal-access arrangements | Confirmed access arrangements | PRD-2.1 Design outputs and dissemination | 4.1.5 Accountability |
| Confirm target user groups and the communication plan | Confirmed audience and communication plan | PRD-2.1 Design outputs and dissemination | 1.5.2 Promotion to use |
| Flag plan changes for design review | Plan change exception (if any) | PRD-2.1 Design outputs and dissemination | GAMSO Quality Management |

<br>

#### VS-06.2 Prepare Data for Dissemination

**Value created:** *Products made disclosure-safe and formatted for each channel.*

This stage prepares the product for release. Final disclosure control is applied: suppression, rounding, or perturbation for tables and dashboards, beyond the protection applied upstream, and de-identification for any released microdata. The release is then checked against the disclosure-risk criteria of the gate of State #5. Nothing proceeds if the criteria are not met: a release that fails is returned for additional protection, because confidentiality is not negotiable at the boundary to State #5. The product is then formatted for each channel (publication, API or dataset, dashboard) and loaded into the output systems, where it stays under embargo. The documentation, metadata, and methodology notes are assembled according to the documentation standard.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Apply final disclosure control to tables and dashboards | Disclosure-controlled outputs | PRD-6.4 Apply disclosure control | SAF-P11; 1.3.7 Statistical disclosure; GSBPM 6.4 |
| De-identify any released microdata to the designed standard | De-identified microdata | PRD-6.4 Apply disclosure control | SAF-P11 |
| Check the release against the disclosure-risk criteria | Disclosure clearance, or return for further protection | PRD-6.4 Apply disclosure control; DLM-2 Promote data through a quality gate | SAF-P11 |
| Format the product for each channel and load it into the output systems under embargo | Channel-ready products | PRD-7.1 Update output systems; PRD-7.2 Produce dissemination products | |
| Assemble documentation, metadata, and methodology notes | Release documentation package | PRD-7.2 Produce dissemination products; OVA-2 Metadata Management | SAF-P09 |

<br>

#### VS-06.3 Publish and Provide Access Services

**Value created:** *Statistics released to users through trusted, secure channels, equally and on time.*

This stage executes the release. The product and its metadata are published through the confirmed channels: portal or publication, API and open data, dashboards, deliveries to international organisations, and data offerings in data spaces where applicable. Release timing follows the calendar, with embargo and equal access enforced: no privileged early access outside policy. All channels come from the same released version, so a user gets the same figure everywhere. Access to microdata is mediated through a secure research environment: researchers are authorised, their project is assessed, a project-specific dataset is prepared, and every result is checked before it leaves the environment. The release is promoted according to the communication plan, together with VS-10. A persistent, identified release version is recorded with lineage to the approved product, and the *Statistics Released* event is published.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Publish products and metadata through the confirmed channels (portal, API, dashboards) | Published release | PRD-7.2 Produce dissemination products; PRD-7.3 Release dissemination products | 1.5.3 Facilitate data access |
| Manage release timing, embargo, and equal access | Managed release, embargo log | PRD-7.3 Release dissemination products | 1.5.1 Publication management; 4.1.5 Accountability |
| Publish data offerings in data spaces where applicable | Data space offering | DSP-2 Publish data offerings | |
| Authorise researchers and assess project applications | Research access authorisation | MDS-1 Authorise institutions and researchers; MDS-2 Assess access applications | 2.2.4 Data services; COL-04 |
| Provide mediated access in a secure research environment, or privacy-preserving analysis where data cannot be moved | Research dataset, research access provision | MDS-3 Prepare research datasets; MDS-4 Provide a secure processing environment; MDS-5 Facilitate privacy-preserving analysis | SAF-P10, SAF-P11 |
| Check research output before it leaves the environment | Released or returned research output | MDS-7 Check and release output | SAF-P11 |
| Promote the release according to the communication plan, with VS-10 | Promotion carried out | PRD-7.4 Promote dissemination products | 1.5.2 Promotion to use |
| Register the release version with lineage and publish the *Statistics Released* event | Release version, event notification | DLM-3 Register and catalogue data | SAF-P07 |

|**PLACEHOLDER: VS-06 release architecture: the approved product passes final disclosure control and formatting, then the disclosure-risk decision; on "yes" it is released through portal or publication, API and open data, dashboards, and the secure research environment to users (#6); on "no" it is returned for more protection**|
|---|

<br>

#### VS-06.4 Support and Engage Users

**Value created:** *Users helped to find, understand, and correctly use the statistics.*

This stage supports users after release. Documentation, metadata, and user guides are made available with the release. The helpdesk answers queries, and training or guidance is provided for correct interpretation and use. Researchers in the secure environment receive their own support, including help with output checking. Engagement activities, together with VS-10, gather questions and needs. Errata and clarifications are issued according to the correction policy. The aim is responsible use: helping users avoid misinterpreting estimates and their uncertainty.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Provide documentation, metadata, and user guides with the release | Published documentation | PRD-7.5 Provide user support; OVA-2 Metadata Management | SAF-P09 |
| Operate the helpdesk and respond to user queries | Query responses | PRD-7.5 Provide user support | 3.4.1 Services management |
| Provide training and guidance for correct interpretation | User guidance | PRD-7.5 Provide user support | |
| Support researchers with data, methods, and output checking | Researcher support | MDS-6 Support researchers | COL-04 |
| Gather questions and needs through engagement activities, with VS-10 | Engagement log | PRD-7.4 Promote dissemination products | |
| Issue errata and clarifications according to the correction policy | Corrections (if any) | PRD-7.3 Release dissemination products; DLM-7 Revise data | 4.1.5 Accountability |

<br>

#### VS-06.5 Monitor Usage and Feedback

**Value created:** *Insight into how statistics are used and valued, feeding continuous improvement.*

This last stage closes the loop with users. Usage is tracked across channels: downloads, API calls, dashboard views, and publication reads. User satisfaction and feedback are collected, and the insights are analysed to understand reach, value, and unmet needs. For research access, the use of the data against the conditions of use is monitored, and finished projects are closed, with their datasets and project-specific pseudonymisation keys disposed of. The insights go back to Design, to VS-10, and across the value chain. An example is demand for a new breakdown, which would have to start in earlier value streams.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Track usage across channels (downloads, API calls, views) | Usage statistics | PRD-8.1 Gather evaluation inputs; DLM-8 Monitor data quality, lineage and use | |
| Collect user satisfaction and feedback | Feedback log | PRD-8.1 Gather evaluation inputs | GSBPM 8 |
| Analyse reach, value, and unmet needs | Usage insight report | PRD-8.1 Gather evaluation inputs; PRD-8.2 Conduct evaluation | |
| Monitor research use against the conditions of use, and close finished projects | Research compliance record, project closure record | MDS-8 Monitor use and compliance; MDS-9 Close projects | SAF-P11 |
| Route insights to Design, VS-10, and the wider chain | Improvement and engagement inputs | PRD-8.1 Gather evaluation inputs | 4.1.4 Improvement management |

### 4. The four process types

The sub-processes below are specific to VS-06. Each refines one or more SAF business processes, listed as *Refines*, which keeps it traceable to *Business Processes*. Sub-processes marked *(standard)* work as described in [Standard activities in every value stream](#standard-vs-activities); only the VS-06 specifics are listed.

#### Design: provides metadata

Without a designed strategy and release policy, release becomes ad hoc, with a risk of confidentiality breaches or unequal access, and management has no baseline to measure accessibility and impact against.

| Design sub-process | Refines | Main outputs |
|---|---|---|
| Design Dissemination and Access Strategy | PRD-1.2 Consult and confirm needs; PRD-2.1 Design outputs and dissemination | User segmentation, channel and format strategy, release calendar and access policy, product-channel map |
| Design Disclosure Control and De-identification for Release | PRD-2.1 Design outputs and dissemination; PRD-2.5 Design processing and analysis; DLM-4 Classify and protect data | Release disclosure-control rules, de-identification standard, disclosure-risk criteria, channel protection design |
| Design Channels, Formats, and Documentation | PRD-2.1 Design outputs and dissemination; OVA-2 Metadata Management | Format and accessibility standard, API and dataset specification, service design, documentation standard |
| Design User Support, Promotion, and Feedback Model | PRD-2.1 Design outputs and dissemination; DLM-7 Revise data | User support model, communication plan, usage and feedback model, correction policy |
| Design Release Governance and Audit Framework | PRD-2.1 Design outputs and dissemination; DLM-1 Plan and design data assets; DLM-4 Classify and protect data | Release approval policy, equal-access controls, versioning and lineage policy, access control design |

##### Design Dissemination and Access Strategy

*Refines:* PRD-1.2 Consult and confirm needs; PRD-2.1 Design outputs and dissemination.

The starting point is deciding who the products are for and how they will be reached. This sub-process defines the target user groups and their needs, together with VS-10. It defines the access channels and release formats: open data, API, research access, publications, and dashboards. It sets the release calendar and the equal-access and embargo policy. Each product is mapped to its channels and formats.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define target user groups and their needs, with VS-10 | User segmentation | PRD-1.2 Consult and confirm needs; PRD-2.1 Design outputs and dissemination | 2.2.5 User research |
| Define access channels and release formats (open data, API, research access, publications, dashboards) | Channel and format strategy | PRD-2.1 Design outputs and dissemination | 1.5.3 Facilitate data access |
| Define the release calendar and the equal-access and embargo policy | Release calendar and access policy | PRD-2.1 Design outputs and dissemination | 1.5.1 Publication management; 4.1.5 Accountability |
| Map each product to its channels and formats | Product-channel map | PRD-2.1 Design outputs and dissemination | |

##### Design Disclosure Control and De-identification for Release

*Refines:* PRD-2.1 Design outputs and dissemination; PRD-2.5 Design processing and analysis; DLM-4 Classify and protect data.

This sub-process designs the final confidentiality protection applied before release. It specifies the disclosure-control rules for tables and dashboards (suppression, rounding, perturbation), over and above the protection already applied upstream. It sets the de-identification standard for any released microdata and the disclosure-risk criteria that a release must meet. Different channels get different treatment: more detailed microdata, for example, is only available in a secure research environment.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define final disclosure-control rules for tables and dashboards | Release disclosure-control rules | PRD-2.5 Design processing and analysis | SAF-P11; 1.3.7 Statistical disclosure |
| Define the de-identification standard for released microdata | De-identification standard | PRD-2.5 Design processing and analysis; DLM-4 Classify and protect data | SAF-P11; 3.3.1 Privacy management |
| Define the disclosure-risk criteria a release must meet | Disclosure-risk criteria | PRD-2.1 Design outputs and dissemination | SAF-P11 |
| Design differential treatment by channel (open access or secure research access) | Channel protection design | PRD-2.1 Design outputs and dissemination; DLM-4 Classify and protect data | SAF-P10; 2.2.4 Data services |

##### Design Channels, Formats, and Documentation

*Refines:* PRD-2.1 Design outputs and dissemination; OVA-2 Metadata Management.

This sub-process designs the delivery mechanics, using the platforms that VS-09 provides. It specifies the publication formats and accessibility standards: machine-readable formats, languages, and web accessibility. It specifies the API and dataset structures, for example in SDMX, the dashboards and visualisations, and the access model of the secure research environment. It also sets the documentation standard that every release must meet: methodology notes, metadata, and user guides.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Specify publication formats and accessibility standards | Format and accessibility standard | PRD-2.1 Design outputs and dissemination | |
| Specify API and dataset structures | API and dataset specification | PRD-2.1 Design outputs and dissemination; OVA-2 Metadata Management | SDMX; CSDA Dissemination |
| Specify dashboards, visualisations, and the research access model | Service design | PRD-2.1 Design outputs and dissemination | 2.2.4 Data services |
| Define the documentation standard for every release | Documentation standard | OVA-2 Metadata Management | SAF-P09 |

##### Design User Support, Promotion, and Feedback Model

*Refines:* PRD-2.1 Design outputs and dissemination; DLM-7 Revise data.

This sub-process designs how users are supported and heard. It specifies the user support model (documentation, helpdesk, training) and the approach to promoting and communicating releases, together with VS-10. It defines the usage and feedback model: what is measured, such as usage and satisfaction, how feedback is collected, and how it goes back into improvement. The correction and erratum policy completes the design.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define the user support model (documentation, helpdesk, training) | User support model | PRD-2.1 Design outputs and dissemination | 3.4.1 Services management |
| Define the promotion and communication approach for releases, with VS-10 | Communication plan | PRD-2.1 Design outputs and dissemination | 1.5.2 Promotion to use; 3.1.4 Communication management |
| Define the usage and feedback model | Usage and feedback model | PRD-2.1 Design outputs and dissemination | |
| Define the correction, erratum, and re-release policy | Correction policy | DLM-7 Revise data | 4.1.5 Accountability |

##### Design Release Governance and Audit Framework

*Refines:* PRD-2.1 Design outputs and dissemination; DLM-1 Plan and design data assets; DLM-4 Classify and protect data.

This last design sub-process makes sure that releases are governed, equitable, and auditable. It defines the release approval and sign-off workflow and the equal-access controls, so that nobody gets early access outside policy. It sets the release versioning policy (identity, revisions and corrections, retention) and the lineage requirements from each release back to its approved product. Role-based access control for the access services is designed in line with SAF-P10.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define the release approval and sign-off workflow | Release approval policy | PRD-2.1 Design outputs and dissemination | 4.1.5 Accountability |
| Define equal-access controls and embargo governance | Equal-access controls | PRD-2.1 Design outputs and dissemination | 1.5.1 Publication management; 4.1.5 Accountability |
| Define release versioning and lineage requirements | Versioning and lineage policy | DLM-1 Plan and design data assets | CSDA Traceability |
| Design role-based access control for the access services | Access control design | DLM-4 Classify and protect data | SAF-P10; 3.3.4 Logical identity and access control |

|**PLACEHOLDER: VS-06 design process decomposition: inputs (approved products from VS-05, user needs via VS-10, confidentiality and access law via VS-07, framework standards), the five design sub-processes in order, and the design document each produces (channel and format strategy, release disclosure-control rules, service and documentation specifications, support and feedback model, release governance policy)**|
|---|

#### Implementation: provides the execution process

Implementation builds, configures, and tests the dissemination and access pipeline on the platforms provided by VS-09. Nothing is published in production until this is complete.

| Implementation sub-process | Refines | Main outputs |
|---|---|---|
| Build Publication and Access Channels | PRD-3.3 Reuse or build dissemination components; MDS-4 Provide a secure processing environment | Configured publication, open-data, API, and dashboard services; research access service; standard exchange interfaces |
| Configure Disclosure Control and Release Tooling | PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows | Configured disclosure-control tooling, de-identification component, release disclosure gate, release management tooling |
| Build Documentation, Support, and Usage Monitoring Services | PRD-3.3 Reuse or build dissemination components; PRD-3.4 Configure workflows; DLM-3 Register and catalogue data | Documentation services, user support services, usage and feedback tooling, release version store, event publication |
| Test and Validate the Pipeline *(standard)* | PRD-3.5 Test production systems; PRD-3.6 Test statistical business process; PRD-3.7 Finalise production systems | Test reports; integration test from product intake through preparation, disclosure control, and release to access and support; accessibility test (formats, languages, machine-readability); security and disclosure test (access controls, no output breaches the disclosure-risk criteria); release rehearsal (managed timing, embargo, equal access) |

##### Build Publication and Access Channels

*Refines:* PRD-3.3 Reuse or build dissemination components; MDS-4 Provide a secure processing environment.

This sub-process turns the channel and format designs into operational services. The publication channels (website or publication system), the API and open-data services, the dashboards, and access to the secure research environment are built or configured on the VS-09 platforms, according to the designed formats and accessibility standards. Dataset and metadata exchange compliant with SDMX is configured, and access controls are applied according to the designed model.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Build or configure publication channels and the open-data and API services | Configured publication and API services | PRD-3.3 Reuse or build dissemination components | 1.1.3 Build statistics product |
| Build or configure dashboards and visualisation services | Configured dashboards | PRD-3.3 Reuse or build dissemination components | |
| Configure access to the secure research environment | Research access service | MDS-4 Provide a secure processing environment | SAF-P10 |
| Configure dataset and metadata exchange compliant with SDMX | Standard exchange interfaces | PRD-3.3 Reuse or build dissemination components | SDMX; CSDA Dissemination |

##### Configure Disclosure Control and Release Tooling

*Refines:* PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows.

The designed disclosure-control rules and release policy are implemented. Disclosure-control tooling is configured to apply the designed suppression, rounding, and perturbation to tables and dashboards, and to de-identify released microdata. Disclosure-risk checks are enforced before publication. Release tooling is configured for release at a managed time, embargo handling, and enforcement of equal access.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Configure final disclosure-control tooling (suppression, rounding, perturbation) | Configured disclosure-control tooling | PRD-3.2 Reuse or build processing and analysis components | SAF-P11 |
| Configure microdata de-identification to the designed standard | De-identification component | PRD-3.2 Reuse or build processing and analysis components | SAF-P11 |
| Enforce disclosure-risk checks before publication | Release disclosure gate | PRD-3.4 Configure workflows; DLM-2 Promote data through a quality gate | SAF-P11 |
| Configure release at a managed time, embargo handling, and equal-access enforcement | Release management tooling | PRD-3.4 Configure workflows | 1.5.1 Publication management; 4.1.5 Accountability |

##### Build Documentation, Support, and Usage Monitoring Services

*Refines:* PRD-3.3 Reuse or build dissemination components; PRD-3.4 Configure workflows; DLM-3 Register and catalogue data.

This sub-process implements the services for users and the feedback loop. Documentation and metadata services make sure that every release is accompanied by methodology notes, reference metadata, and user guides. Helpdesk and training support are set up according to the support model. Usage monitoring and feedback collection capture usage statistics, satisfaction, and feedback, and route them into the improvement loop and to VS-10. The release version store is built so that each release is identified, immutable, and traceable to its approved product, and event notifications are configured to signal a release.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Build documentation and metadata services for every release | Documentation services | PRD-3.3 Reuse or build dissemination components; OVA-2 Metadata Management | SAF-P09 |
| Set up helpdesk and training support | User support services | PRD-3.3 Reuse or build dissemination components | 3.4.1 Services management |
| Implement usage monitoring and feedback collection | Usage and feedback tooling | PRD-3.4 Configure workflows | |
| Build the release version store and configure the *Statistics Released* event | Release version store, event publication | PRD-3.4 Configure workflows; DLM-3 Register and catalogue data | SAF-P07; CSDA Traceability |

|**PLACEHOLDER: VS-06 implementation pipeline: the five design artefacts feeding the three build sub-processes, followed by technical testing, accessibility and disclosure tests, and a release rehearsal, resulting in an operational dissemination pipeline and operational procedures**|
|---|

#### Execution: provides the statistical data

Execution runs the stages of VS-06 for every release. The stages and their activities are described in attribute 3. A cycle starts when an approved product is registered; the release itself takes place at the slot in the release calendar. Support and monitoring of usage continue after the release. Execution applies the designs and the solution as they are; a new channel or a policy change goes back to Design. Every release attempt ends in one of two outcomes: released at the planned moment, or returned for further protection. Unlike earlier gates, the disclosure criteria allow no conditional acceptance.

| Aspect | VS-06 |
|---|---|
| Trigger | *Statistical Product Registered* |
| Cadence | Per release, following the release calendar; support and monitoring are continuous |
| Performed by | ROL-17 Release manager, ROL-16 Disclosure control specialist, ROL-22 Dissemination and service manager, ROL-03 Data steward |
| Input | Approved #4 version with its metadata and approval record |
| Output | Released data version (#5) in its channel representations, user support, usage and feedback data |
| Control point | Gate of State #5: disclosure-risk criteria in VS-06.2; release authorisation and release slot before VS-06.3 |
| Exception path | Failed disclosure criteria: return for further protection; error in content: back to VS-05 or VS-04 as a new approved version, released again with an erratum; plan change: back to Design |

#### Management: provides quality reports

Management runs alongside and after execution. It also makes sure that every release is compliant and equitable, and it feeds recommendations to VS-10 as well as to Design.

| Management sub-process | Refines | Main outputs |
|---|---|---|
| Monitor Process Performance *(standard)* | OVA-4 Process Data Management; PRD-8.1 Gather evaluation inputs | Process performance dashboard; release calendar adherence report; paradata on channels used, the moment each release went live, embargo handling, and the number of support queries |
| Assess Dissemination Quality | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use | Accessibility report, punctuality report, reach and clarity report, quality trend analysis |
| Manage Release and Channel Lifecycle | OVA-2 Metadata Management; DLM-5 Store and version data; DLM-7 Revise data; DLM-8 Monitor data quality, lineage and use; DLM-10 Archive and preserve data | Channel version register, metadata quality report, release store audit, metadata lineage audit |
| Audit and Compliance Reporting *(standard)* | OVA-1 Quality Management; OVA-4 Process Data Management; MDS-8 Monitor use and compliance | Produced with VS-07: disclosure compliance summary (every release passed the gate; released microdata meets the de-identification standard); equal-access compliance report (release timing and embargo respected, no privileged early access); accessibility compliance report; security compliance report covering access controls and the integrity of the secure research environment |
| Continuous Improvement *(standard)* | PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan | Improvement recommendations, for example new or better channels and formats, clearer documentation where users misunderstand it, a leaner release process, better accessibility, and demand for new statistics or breakdowns; recommendations go to Design, to VS-10, and, where the need starts earlier, across the chain; trends watched: punctuality, reach, satisfaction, support queries |

##### Assess Dissemination Quality

*Refines:* OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use.

Beyond process performance, the quality of dissemination itself is evaluated against the criteria set in Design. Each release and the service as a whole are assessed on several dimensions. Accessibility covers formats, languages, machine-readability, and compliance with web accessibility standards. Timeliness and punctuality are measured against the release calendar. Reach and relevance compare usage with expectations and check the coverage of user groups. Clarity looks at whether users interpret the figures correctly, judged from queries and feedback. Quality indicators are produced per release and per cycle, and trends are tracked. This follows the Data Quality capability of CSDA and SAF capability 2.1.3 *Statistical quality management*.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Assess the accessibility compliance of releases | Accessibility report (per cycle) | OVA-1 Quality Management | 2.1.3 Statistical quality management |
| Assess timeliness and punctuality against the release calendar | Punctuality report | OVA-1 Quality Management | CSDA Data Quality |
| Assess reach, relevance, and clarity from usage and feedback | Reach and clarity report | DLM-8 Monitor data quality, lineage and use | 2.1.3 Statistical quality management |
| Identify quality trends across releases and cycles | Quality trend analysis | OVA-1 Quality Management | 2.1.3 Statistical quality management |

##### Manage Release and Channel Lifecycle

*Refines:* OVA-2 Metadata Management; DLM-5 Store and version data; DLM-7 Revise data; DLM-8 Monitor data quality, lineage and use; DLM-10 Archive and preserve data.

Dissemination channels, formats, and the releases they carry must stay current, complete, and well governed. This sub-process manages the life cycle of channels, formats, and documentation standards: it versions them, manages transitions such as an API version upgrade, and retires obsolete channels. It verifies that every release carries full documentation, its disclosure record, and its lineage, as a compliance check on SAF-P09. It governs the release version store: retention, immutability, handling of corrections, and reconciliation of catalogue entries with what is actually published. Lineage from approved product to released data is tracked.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Manage the life cycle and versions of channels, formats, and documentation standards | Channel version register | OVA-2 Metadata Management | 3.4.1 Services management |
| Verify metadata completeness: documentation, disclosure record, lineage | Metadata quality report | OVA-2 Metadata Management | SAF-P09 |
| Govern the release version store: retention, immutability, corrections, reconciliation with the catalogue | Release store audit | DLM-5 Store and version data; DLM-7 Revise data; DLM-10 Archive and preserve data | CSDA Traceability |
| Track metadata lineage from approved product to released data | Metadata lineage audit | DLM-8 Monitor data quality, lineage and use | CSDA Traceability |

|**PLACEHOLDER: VS-06 management feedback loop: releases and usage data from Execution flowing through the five management sub-processes, with dashboards to the process owner, quality reports to the quality manager, compliance reports to VS-07, and improvement recommendations back to Design and user insight to VS-10**|
|---|

#### Metadata per process type

Metadata is what enables responsible use: every released product carries the documentation, methodology, and reference metadata users need. The table shows the data metadata each process type of VS-06 contributes; the paradata are listed in [Standard activities in every value stream](#standard-vs-activities). VS-06 also records as paradata the accessibility test outcomes in Implementation, and the adherence to the release calendar, the embargo handling, and the publication run identifiers in Execution.

| Process type | Data metadata produced |
|---|---|
| Design | Dissemination and access strategy, channel and format specifications, release and disclosure policy, documentation standards |
| Implementation | Channel configurations, API and dataset templates, disclosure-control parameters, documentation templates |
| Execution | Documentation per release, record of the final disclosure control applied, channels and formats published, release timestamp, metadata of the access services |
| Management | Usage statistics, accessibility assessments, user satisfaction measures, release quality reports |

|**PLACEHOLDER: VS-06 business object lifecycle: design artefacts govern implementation assets, which produce the pipeline that releases the approved product (#4) as Released Data (#5), consumed as Consumed Data (#6), generating disclosure records, documentation, and usage data that management assesses and feeds back to design**|
|---|

### 5. Actors and roles

VS-06 is where the NSI meets the users of its statistics. The table shows the actors and the reference roles involved. Specialised role names used in an NSI map onto these reference roles (see *Role names in the value streams*); for example, the dissemination manager, the channel and service designer, the open-data and API product owner, and the user support lead in the original VS-06 description are all ROL-22 Dissemination and service manager. Access for researchers is organised in the collaboration COL-04 *Research access partnership*.

| Actor or role | ID | Process type | Responsibility in VS-06 |
|---|---|---|---|
| Data user | ACT-05 | External | Consumes released data: policy makers, researchers, journalists, businesses, the public |
| International statistical organisation | ACT-07 | External | Receives deliveries under agreed transmission programmes |
| Process owner | ROL-01 | Management | Accountable for the end-to-end performance of VS-06 |
| Data owner | ROL-02 | Management | Accountable for State #5: confidentiality, equal access, and the quality of the release |
| Data steward | ROL-03 | Execution | Maintains release documentation, catalogue entries, and errata |
| Data custodian | ROL-04 | Execution | Operates release channels, integrity protection, and the embargo log |
| Disclosure control specialist | ROL-16 | Design, Execution | Designs the final disclosure-control rules and de-identification standards, and applies and signs off the final disclosure control |
| Dissemination and service manager | ROL-22 | Design, Execution | Designs the dissemination and access strategy, the service portfolio, the channels, formats, APIs, dashboards, and secure research access; operates the open-data, API, and dashboard services; leads documentation, helpdesk, and training |
| Data engineer | ROL-10 | Implementation | Builds and configures publication channels, APIs, and access services on VS-09 platforms |
| Platform engineer | ROL-11 | Implementation | Configures release tooling, access controls, and disclosure-control tooling |
| Test manager | ROL-12 | Implementation | Plans and carries out testing of the release pipeline: technical, accessibility, and security tests |
| Release manager | ROL-17 | Execution | Manages the release: timing, embargo, equal access, and publication across channels |
| Quality manager | ROL-18 | Management | Monitors usage and accessibility indicators, produces quality reports, and drives continuous improvement |
| Compliance officer | ROL-19 | Management | Ensures data protection, confidentiality, and equal-access compliance with VS-07, and produces audit reports |
| Relationship manager | ROL-23 | Execution | Promotes releases and gathers user feedback, with VS-10 |

### 6. Capabilities, processes, and functions

#### Capability foundations

The table shows which capabilities from the SAF capability model VS-06 relies on, and what role they play. NSIs can use it to map the value stream to their own organisation.

| Capability group | Capabilities | Role in VS-06 |
|---|---|---|
| 1.1 Statistical design and build | 1.1.2 Design statistics product, 1.1.3 Build statistics product | Design dissemination products and services, and build the release and access pipeline |
| 1.3 Processing | 1.3.7 Statistical disclosure | Apply final disclosure control before release |
| 1.5 Dissemination | 1.5.1 Publication management, 1.5.2 Promotion to use, 1.5.3 Facilitate data access, 1.5.4 Statistical information management | Release according to the calendar with equal access, promote releases, and make data and metadata available through several channels |
| 2.1 Data management | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management | Manage released data and its metadata, and the quality of release and access |
| 2.2 Research | 2.2.4 Data services, 2.2.5 User research | Provide microdata for research, and understand user needs with VS-10 |
| 3.2 Computerisation and automation | 3.2.1 Application development, 3.2.2 Functional management | Build and maintain publication channels, APIs, and dashboards, with VS-09 platforms |
| 3.3 Security and privacy | 3.3.1 Privacy management, 3.3.2 Security planning, 3.3.4 Logical identity and access control | Apply final disclosure control and secure access to released data and microdata |
| 3.4 Customer and chain interaction | 3.4.1 Services management | Design and manage the dissemination services and their service levels |
| 4.1 Strategy and leadership | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improvement management, 4.1.5 Accountability | Govern release, manage the equal-access policy, plan improvements, report on compliance |

#### Stages, processes, and functions

The table shows which SAF business processes realise each stage of VS-06 and which business functions they mainly use.

| Stage | Realised by processes | Main functions |
|---|---|---|
| VS-06.1 Plan Dissemination and Access Strategy | PRD-2.1 Design outputs and dissemination | FUN-3.1 Design and build statistical products; FUN-3.6 Disseminate statistics |
| VS-06.2 Prepare Data for Dissemination | PRD-6.4 Apply disclosure control; PRD-7.1 Update output systems | FUN-3.5 Protect statistical confidentiality; FUN-3.6 Disseminate statistics |
| VS-06.3 Publish and Provide Access Services | PRD-7.2 Produce dissemination products; PRD-7.3 Release dissemination products; MDS-1 Authorise institutions and researchers; MDS-2 Assess access applications; MDS-3 Prepare research datasets; MDS-4 Provide a secure processing environment; MDS-5 Facilitate privacy-preserving analysis; MDS-7 Check and release output; DSP-2 Publish data offerings | FUN-3.6 Disseminate statistics; FUN-8.1 Manage research access; FUN-8.2 Prepare research data; FUN-8.3 Operate secure research environments; FUN-8.4 Control research output; FUN-8.5 Enable privacy-preserving analysis; FUN-9.1 Manage data space participation |
| VS-06.4 Support and Engage Users | PRD-7.4 Promote dissemination products; PRD-7.5 Provide user support; MDS-6 Support researchers | FUN-3.6 Disseminate statistics; FUN-8.3 Operate secure research environments; FUN-10.9 Manage users and services |
| VS-06.5 Monitor Usage and Feedback | PRD-8.1 Gather evaluation inputs; MDS-8 Monitor use and compliance; MDS-9 Close projects | FUN-8.1 Manage research access; FUN-8.3 Operate secure research environments; FUN-10.9 Manage users and services |

|**PLACEHOLDER: ArchiMate view VS-06 (b) stages realised by processes and functions**|
|---|

#### Framework mappings

This reference table maps each process type of VS-06 to the SAF business processes, the international frameworks (GSBPM, GAMSO, CSDA), and the SAF capability model. It is intended for architects and auditors; the rest of this section does not depend on it.

| Process type | SAF business processes | GSBPM | GAMSO | CSDA | SAF capabilities |
|---|---|---|---|---|---|
| Design | PRD-1.2, PRD-2.1, PRD-2.5, DLM-1, DLM-4, DLM-7, OVA-2 | Phase 1 Specify Needs (1.2), Phase 2 Design (2.1, 2.5) | Production (design activities), Capability Management | Data Governance, Metadata Management, Dissemination | 1.1.2 Design statistics product, 2.1.2 Metadata management, 3.3.1 Privacy management |
| Implementation | PRD-3.2 to PRD-3.7, DLM-2, DLM-3, OVA-2, MDS-4 | Phase 3 Build (3.2 to 3.7) | Capability Management | Dissemination (set-up), Data Governance (configuration) | 1.1.3 Build statistics product, 3.2.1 Application development, 3.2.2 Functional management |
| Execution | PRD-2.1, PRD-6.4, PRD-7.1 to PRD-7.5, PRD-8.1, PRD-8.2, DLM-2, DLM-3, DLM-7, DLM-8, OVA-2, MDS-1 to MDS-9, DSP-2 | 6.4 Apply disclosure control; Phase 7 Disseminate (7.1 to 7.5); Phase 8 Evaluate for usage monitoring; 2.1 in its recurrent form | Production (execution), Corporate Support (communication) | Dissemination (execution) | 1.3.7 Statistical disclosure, 1.5.1 to 1.5.4, 2.1.2 Metadata management, 2.2.4 Data services, 3.3.1 Privacy management |
| Management | OVA-1, OVA-2, OVA-4, DLM-5, DLM-7, DLM-8, DLM-10, MDS-8, PRD-8.1 to PRD-8.3 | Phase 8 Evaluate; overarching Quality Management and Metadata Management | Corporate Support (Quality Management, Communication), Capability Management (improvement) | Data Quality, Data Governance, Traceability | 2.1.3 Statistical quality management, 4.1.4 Improvement management, 4.1.5 Accountability |

### 7. Principles

The following principles govern VS-06 most directly.

| Principle | Statement | Application in VS-06 |
|---|---|---|
| SAF-P01 | Actively participate in open-source communities to maintain collective control over statistical processes | Dissemination platforms, APIs, and visualisation tooling are built with open-source communities, and the NSI contributes back, so that it keeps collective control over critical delivery capabilities instead of depending on vendors. |
| SAF-P07 | Implement loosely coupled processes and systems | VS-06 consumes approved products through the State #4 interface without knowledge of how they were composed, and exposes released data through stable, versioned access services. |
| SAF-P08 | Data is shared property | Released data is made broadly and equally available to all authorised users through open and standard channels, which maximises reuse while respecting confidentiality. |
| SAF-P09 | No data without metadata and classification | Every released product carries the metadata, methodology notes, and documentation users need to interpret it correctly. Released datasets come with structural and reference metadata, for example in SDMX. |
| SAF-P10 | Security by design | Access controls, secure channels, and integrity protection are built into the publication and access services from the start, including secure research environments for sensitive microdata. |
| SAF-P11 | Privacy by design | Final disclosure control and de-identification are applied before release. The disclosure risk of every released product and microdata file is assessed and cleared by design. |

::: {.callout-note title="Principles that apply across the process types"}
SAF-P11 is the release gate: disclosure control is designed in *Design Disclosure Control and De-identification for Release* and *Design Release Governance and Audit Framework*, implemented in *Configure Disclosure Control and Release Tooling*, and applied in VS-06.2 before anything is published. SAF-P08 and SAF-P09 drive open, well-documented release with equal access. SAF-P10 governs the access services and secure research environments in VS-06.3 and VS-06.4. SAF-P07 governs the State #4 intake interface from VS-05 and the access interface for released data to external users.
:::

### 8. Interfaces, services, and events

**Boundary interfaces**

VS-06 has two boundary interfaces: intake from VS-05, and release to users outside the NSI.

| Boundary | Handed over | Required metadata | Trigger | Responsibility transfer |
|---|---|---|---|---|
| VS-05 → VS-06 (intake) | Approved statistical product (#4, approved) | Component lineage, composition method, propagated accuracy, coherence results, approval record, confidentiality status, product version identifier, classification | *Statistical Product Registered* | VS-05 keeps custody of the product version; VS-06 takes responsibility for final disclosure control, release, and service delivery on receipt of the event |
| VS-06 → users and society (release) | Released data (#5): published statistics, de-identified microdata, access services | Final disclosure-control record, documentation and methodology notes, reference and structural metadata, channels and formats, release timestamp, release version identifier, lineage to the approved product | *Statistics Released* | The NSI publishes and serves; external users consume the data as #6, outside NSI control. Usage and feedback flow back to VS-06.5 and VS-10 |

**Business services**

| Service | Offered to | Realised in | Interfaces |
|---|---|---|---|
| Dissemination preparation service | Release teams, for approved products from VS-05 | VS-06.2 Prepare Data for Dissemination | Intake of the approved #4 version on *Statistical Product Registered* |
| Publication and open-data service | Data users, the public, businesses | VS-06.3 Publish and Provide Access Services | Web publication and bulk open-data download with machine-readable metadata; equal-access release timing enforced |
| API and dashboard service | Researchers, developers, analysts | VS-06.3 Publish and Provide Access Services | SDMX-compliant API to query released series, datasets, and metadata; interactive dashboards fed from the released datasets |
| Secure research access service | Accredited researchers | VS-06.3 Publish and Provide Access Services | Mediated access to de-identified microdata in a controlled environment, with output checking |
| User support service | All data users | VS-06.4 Support and Engage Users | Documentation, helpdesk, training |
| Usage and feedback service | Process owners, VS-10, the wider chain | VS-06.5 Monitor Usage and Feedback | Usage statistics, feedback log, usage insight reports |
| Design and strategy service | Dissemination and service managers, channel designers | All Design sub-processes of VS-06 | Design documents, release and disclosure policy |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Design artefacts published* | Start of Implementation after a design change |
| *Pipeline production-ready* | End of Implementation; Execution can start |
| *Statistical Product Registered* | Start of VS-06.1 for that product (received from VS-05) |
| Disclosure gate passed / failed | Outcome of the disclosure-risk check in VS-06.2; failure returns the product for further protection |
| *Statistics Released* | Completion of the release in VS-06.3; the data is available to users |
| Usage and feedback received | Input for VS-06.5 and VS-10 |
| *Improvement recommendations issued* | Input for Design and VS-10 from *Continuous Improvement* |

|**PLACEHOLDER: VS-06 event choreography between VS-05, NSI teams, users, and process management across Design, Implementation, Execution (product registered, final disclosure control, gate passed and release with managed timing or gate failed and return for protection, documentation and support, usage and feedback), and Management (usage and punctuality, accessibility, compliance reports, improvement recommendations to Design and VS-10)**|
|---|

**Interaction with the supporting value streams**

| Value stream | Provides to VS-06 | Receives from VS-06 |
|---|---|---|
| VS-07 Governance and Compliance | Data protection and confidentiality law compliance, release and equal-access policy oversight | Disclosure, equal-access, accessibility, and security compliance reports |
| VS-08 Innovation and Methodological Development | New methods and tools, for example for disclosure control and dissemination | Improvement needs |
| VS-09 Infrastructure and Platform Enablement | Portals, APIs, dashboards, secure research environments | Capacity and channel availability requirements |
| VS-10 Customer and Stakeholder Engagement | User needs and segmentation, communication with stakeholders | Usage data, feedback, and user insight |

### 9. Key performance indicators

The key performance indicators are collected per release cycle in *Monitor Process Performance*. They feed the dashboard that the process owner reviews.

| KPI | Description | Measurement |
|---|---|---|
| On-time release rate | Share of releases published exactly in their calendar slot | Per release, per cycle |
| Disclosure gate pass rate | Share of releases passing the disclosure-risk gate on the first run | Per release, per cycle |
| Channel availability | Uptime of API and access services | Per channel |
| Usage and reach | Downloads, API calls, and dashboard views per release | Per release, per channel |
| User satisfaction | Satisfaction measure from feedback | Per cycle |
| Support response time | Time to resolve user queries | Per cycle |

### 10. Examples

**Labour market statistics.** The dissemination strategy targets policy makers with a press release and commentary on the release date, researchers with an API and downloadable series, and the public with an interactive dashboard. The release calendar is published in advance. For the Q3-2026 release, the team confirms the date and slot, the press embargo for accredited media, and the channels, with no change to the strategy this cycle. At 09:00 on the release date, the figures go live at the same moment on the website, the API, and the dashboard. Accredited media that received the embargoed copy under agreement may publish at the same moment. No figure is available before the release time.

**Open data and API.** The team configures an SDMX-based API and a bulk open-data download for the labour market series on the NSI's VS-09 platform, with rate limiting and machine-readable metadata. A public dashboard is fed from the same released datasets, so every channel shows the same figures.

**Research microdata.** Researchers who access de-identified business microdata in the secure research environment receive the data dictionary, methodology notes, and an onboarding session. The helpdesk handles requests for output checking, so that the results researchers export also meet the disclosure rules.

| **Toolkit:** SAF-TK-V06 VS-06 maturity checklist and scenarios |
|---|



## VS-07 Governance and Compliance

### 1. Purpose and value created

VS-07 makes sure that every process, dataset, and product of the NSI operates under clear rules, standards, and accountability. It builds trust, inside and outside the NSI, by making sure that all data activities are ethical, transparent, and compliant with legal, methodological, and quality requirements. It aligns the NSI with standards such as the European Statistics Code of Practice, GDPR, GSBPM, GAMSO, and the ISO data quality principles. The value created is **integrity and accountability**: the NSI acts responsibly, protects privacy, and delivers products that users can trust.

VS-07 does not move data along the chain. It oversees the value streams that do. It sets the rules they must follow, collects the evidence that they follow them, and provides assurance to management, supervisory bodies, and society. VS-07 is the place where the data principles SAF-P09, SAF-P10, and SAF-P11 are enforced across the whole NSI. This section covers the governance capabilities, how they are established and operated, and how they interact with the rest of the value chain. The application and technology controls that implement them are provided with VS-09.

|**PLACEHOLDER: ArchiMate view VS-07 (a) value stream and capabilities**|
|---|

<br>

### 2. Relation to the value chain

VS-07 is not a stage in the production line. It runs horizontally and continuously across all value streams, primary and supporting. It interacts with them in two directions. Downward, it imposes governance frameworks, policies, roles, and controls. Upward, it receives compliance evidence, quality indicators, and audit findings. The *Audit and Compliance Reporting* sub-process of each primary value stream (see [Standard activities in every value stream](#standard-vs-activities)) feeds directly into VS-07. Outward, VS-07 issues certification and assurance to regulators, the public, and international peers.

| Primary value stream(s) | Provides | Receives |
|---|---|---|
| VS-01 to VS-06 | Governance frameworks and policies, legal register and compliance procedures, data governance role assignments, metadata and lineage rules, controls | Compliance evidence, quality indicators, audit trails, and audit findings from each stream's *Audit and Compliance Reporting* |

VS-07 maps to the GAMSO areas **Strategy and Leadership** and **Corporate Support**, and to Capability Management for the life cycle of standards, methods, and data assets (see *Framework mappings*). VS-07 has no state transition and no registration event. Its output is an enabling capability: governance frameworks, compliance mechanisms, assurance, and audit results.

|**PLACEHOLDER: ArchiMate view VS-07 (c) interactions with the value chain: VS-07 sets frameworks, policies, roles, and controls for all value streams (VS-01 to VS-10); the streams return compliance evidence, quality indicators, and audit findings; VS-07 provides certification and assurance to regulators, the public, and international peers**|
|---|

<br>

### 3. Stages

The stages form a continuous governance loop. VS-07.1 and VS-07.2 set the rules, VS-07.3 embeds them in the work of the value streams, VS-07.4 and VS-07.5 assure that they are followed, and VS-07.6 keeps them up to date. The loop never stops running.

| Stage | Name | Value added |
|---|---|---|
| VS-07.1 | Define Governance Frameworks and Policies | Rules for data, metadata, ethics, confidentiality, and quality are set |
| VS-07.2 | Establish Legal and Regulatory Compliance Mechanisms | Applicable rules are known and translated into procedures |
| VS-07.3 | Implement Data and Metadata Governance | Ownership, stewardship, and lineage are assigned |
| VS-07.4 | Monitor Quality and Compliance Indicators | Quality and compliance status is visible |
| VS-07.5 | Audit, Certify and Report Compliance | Compliance is demonstrated |
| VS-07.6 | Update and Improve Governance Mechanisms | Governance keeps up with new rules and lessons learned |

<br>

#### VS-07.1 Define Governance Frameworks and Policies

**Value created:** *A clear rule book that the whole organisation works under.*

This stage defines the overarching charters and principles that cover data, metadata, ethics, confidentiality, and statistical quality. Together they form the rule book of the NSI. The chief data officer sets the data policy and the governance framework, with the data governance board (COL-06). The quality manager sets the quality framework. Controls are aligned with organisational value and accountability, so that governance does not exist for its own sake (SAF-P04).

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define the governance charter and accountability structure | Governance charter | DLM-1 Plan and design data assets | 4.1.1 Strategy and governance; GAMSO Strategy and Leadership |
| Define the data and metadata policies, including classification obligations | Data policy, metadata policy | DLM-1 Plan and design data assets; OVA-2 Metadata Management | SAF-P09; 2.1.1 Data lifecycle management |
| Define the ethics and confidentiality policy, including disclosure control | Confidentiality policy | DLM-4 Classify and protect data | SAF-P11; 3.3.1 Privacy management |
| Define the quality framework: dimensions, indicators, reporting requirements | Quality framework | OVA-1 Quality Management | 2.1.3 Statistical quality management; European Statistics Code of Practice |
| Define the steady-state interface and event conventions that all streams follow | Interface and event conventions | DLM-1 Plan and design data assets | SAF-P07 |

<br>

#### VS-07.2 Establish Legal and Regulatory Compliance Mechanisms

**Value created:** *Every process stays within the law, and the NSI knows which rules apply.*

This stage identifies the regulations that apply to the NSI: GDPR, official statistics legislation, and data sharing agreements. Legal counsel interprets them, and the compliance officer translates them into procedures that keep every process within the law. The applicable provisions are kept in a legal register. The stage also sets the information security and access control framework (SAF-P10) and the privacy policy (SAF-P11) that the value streams and VS-09 must apply.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Identify the applicable regulations: GDPR, statistics law, data sharing agreements | Legal register | DLM-4 Classify and protect data | 3.1.7 Legal support |
| Interpret regulation and frame compliance procedures | Compliance procedures mapped to regulation | DLM-4 Classify and protect data | 3.1.7 Legal support |
| Set the information security and access control framework | Security policy | DLM-4 Classify and protect data | SAF-P10; 3.3.2 Security planning; 3.3.4 Logical identity and access control |
| Set the privacy policy, including purpose limitation and data minimisation | Privacy policy | DLM-4 Classify and protect data | SAF-P11; 3.3.1 Privacy management; GDPR |
| Define the compliance criteria that new processes and methods must meet before production | Compliance criteria | OVA-1 Quality Management | SAF-P03 |

<br>

#### VS-07.3 Implement Data and Metadata Governance

**Value created:** *Governance is wired into how the streams actually work, not only on paper.*

This stage makes the frameworks operational. The chief data officer assigns the data governance roles (data owner, data steward, data custodian) to people and units in every data domain. The processes for metadata creation, maintenance, and lineage tracking are put in place, so that each value stream captures metadata at the point each value is created or changed (SAF-P09). Access rules follow from the role assignments. The supporting tooling, such as catalogue functions and dashboards, is built with VS-09.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Assign data owner, data steward, and data custodian roles per data domain | Data governance role assignments | DLM-1 Plan and design data assets; OVA-3 Data Management | 2.1.1 Data lifecycle management |
| Set up the processes for metadata creation and maintenance | Metadata rules | OVA-2 Metadata Management | SAF-P09; 2.1.2 Metadata management |
| Set up lineage tracking rules across the steady states | Lineage rules | OVA-2 Metadata Management; OVA-3 Data Management | SAF-P09 |
| Set the access rules that follow from the role assignments | Access rules | DLM-6 Provide data for reuse | SAF-P10 |
| Build governance tooling and dashboards with VS-09 | Governance tooling, dashboards | OVA-3 Data Management | 3.2.2 Functional management |

<br>

#### VS-07.4 Monitor Quality and Compliance Indicators

**Value created:** *Quality and compliance status is visible at any time.*

With the controls in place, VS-07 measures process and output quality, such as accuracy, timeliness, and comparability. It tracks compliance status on formal scorecards and dashboards. The input is the compliance evidence and the quality indicators that the value streams report. Monitoring also covers the use of microdata by researchers and the NSI's own exchanges in data spaces. Metadata governance compliance is checked from the evidence of the streams: the share of registered datasets that meet the SAF-P09 obligations.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Measure process and output quality: accuracy, timeliness, comparability | Quality scorecard | OVA-1 Quality Management | 2.1.3 Statistical quality management |
| Consolidate the compliance evidence of all value streams | Compliance dashboard | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use | 4.1.5 Accountability |
| Monitor metadata and lineage compliance of registered datasets | Metadata governance compliance report | DLM-8 Monitor data quality, lineage and use | SAF-P09 |
| Monitor compliance with the conditions of microdata use | Microdata compliance report | MDS-8 Monitor use and compliance | SAF-P11 |
| Monitor compliance of data space exchanges | Data space compliance report | DSP-5 Monitor compliance and report | |

<br>

#### VS-07.5 Audit, Certify and Report Compliance

**Value created:** *Demonstrated assurance that the statistics can be trusted.*

Periodically, VS-07 conducts internal and external audits, performs quality reviews, and documents adherence to the frameworks. Auditors review evidence such as logs, quality reports, and lineage records. The quality manager prepares the NSI for peer reviews against the European Statistics Code of Practice. The results are audit reports, certifications, and assurance statements for management, supervisory authorities, and the public. Transparency reports meet the accountability commitments to stakeholders.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Conduct internal and external audits of processes and controls | Audit reports, audit findings | OVA-1 Quality Management; PRD-8.2 Conduct evaluation | 4.1.5 Accountability |
| Perform quality reviews and peer reviews | Quality review reports | PRD-8.2 Conduct evaluation | European Statistics Code of Practice |
| Obtain and maintain certifications | Certifications | OVA-1 Quality Management | ISO data quality principles |
| Document adherence and issue assurance statements | Assurance statements | OVA-1 Quality Management | 4.1.5 Accountability |
| Publish transparency reports | Transparency report | OVA-1 Quality Management | 4.1.5 Accountability |

<br>

#### VS-07.6 Update and Improve Governance Mechanisms

**Value created:** *Governance evolves with the organisation instead of becoming rigid.*

This stage closes the loop. It incorporates feedback, regulatory changes, and lessons learned from audits into the policies and control frameworks. Each policy and control is version-managed across its life cycle (SAF-P03): changes are tracked, prior versions remain identifiable, and obsolete policies and controls are formally retired. Changes to retention, archiving, and disposal rules are passed to the value streams that apply them.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Analyse feedback, audit findings, and regulatory changes | Policy change proposals | PRD-8.3 Agree an action plan | 4.1.4 Improvement management |
| Revise policies and controls, and track remediation of audit findings | Revised policies and controls | PRD-8.3 Agree an action plan | 4.1.2 Policy and planning |
| Version policies and formally retire obsolete ones | Policy version history | PRD-8.3 Agree an action plan | SAF-P03 |
| Update retention, archiving, and disposal rules | Revised retention rules | DLM-10 Archive and preserve data; DLM-11 Dispose of data | SAF-P03 |

### 4. Plan, build, operate, and improve

VS-07 is itself a capability that must be planned (its frameworks and operating model), built (roles, tooling, and dashboards, with VS-09), operated (continuous monitoring and periodic audit), and improved. Unlike a primary value stream, it runs continuously and organisation-wide, not as a production run per cycle, and it produces assurance rather than statistical data.

| Cycle step | What happens in VS-07 | Main outputs | SAF process |
|---|---|---|---|
| Plan | Define the governance frameworks and policies (VS-07.1) and the legal and regulatory compliance mechanisms (VS-07.2) | Governance charter, policies, legal register, compliance procedures | DLM-1 Plan and design data assets; DLM-4 Classify and protect data; OVA-1 Quality Management |
| Build | Implement data and metadata governance (VS-07.3): assign roles, set up metadata and lineage processes, build tooling and dashboards with VS-09 | Role assignments, metadata and lineage rules, governance tooling | OVA-2 Metadata Management; OVA-3 Data Management; DLM-6 Provide data for reuse |
| Operate | Monitor quality and compliance indicators continuously (VS-07.4); audit, certify, and report periodically (VS-07.5) | Dashboards, scorecards, audit reports, certifications, assurance statements | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use; MDS-8 Monitor use and compliance; DSP-5 Monitor compliance and report; PRD-8.2 Conduct evaluation |
| Improve | Update and improve the governance mechanisms (VS-07.6) | Revised policies and controls | PRD-8.3 Agree an action plan; DLM-10 Archive and preserve data; DLM-11 Dispose of data |

**Governance artefacts.** VS-07 manages enabling artefacts, not data states: the governance framework and policy set, the regulatory compliance register, the data governance role assignments with the metadata and lineage rules, the quality and compliance dashboards, and the audit and certification reports. Every value stream refers to them. Each artefact has a designated owner and is version-managed across its life cycle (SAF-P03).

VS-07 monitors itself with the same discipline it imposes on the chain (attribute 9).

### 5. Actors and roles

VS-07 defines and assigns the data governance roles for the whole NSI, and it relies on the assurance roles. Specialised role names map onto the reference roles (see *Role names in the value streams*): the Chief Data / Governance Officer is ROL-05 Chief data officer, Legal Counsel is a form of ROL-19 Compliance officer, and the Internal / External Auditor is ROL-21 Auditor. Data policy across domains is steered by the collaboration COL-06 *Data governance board*.

| Actor or role | ID | Process type | Responsibility in VS-07 |
|---|---|---|---|
| Supervisory and legal authority | ACT-08 | External | Sets regulatory requirements and changes; assesses compliance; receives certification and assurance |
| International statistical organisation | ACT-07 | External | Sets standards; takes part in peer reviews, for example against the Code of Practice |
| Chief data officer | ROL-05 | Plan, Build | Accountable for the governance framework and organisational data policy; assigns the data governance roles |
| Compliance officer (incl. legal counsel) | ROL-19 | Plan, Operate | Ensures legal and regulatory compliance (Code of Practice, GDPR, statistics law); interprets regulation and frames compliance procedures; keeps the legal register |
| Data owner, data steward, data custodian | ROL-02, ROL-03, ROL-04 | Build, Operate | The data governance roles that VS-07 defines and assigns across domains |
| Quality manager | ROL-18 | Plan, Operate | Defines quality indicators and monitors quality and compliance status |
| Security officer | ROL-20 | Plan, Operate | Defines the security and continuity policy that VS-09 enforces; reviews security posture and incidents |
| Auditor (internal or external) | ROL-21 | Operate | Conducts audits and certifications of adherence to the frameworks |
| Process owners (VS-01 to VS-10) | ROL-01 | Operate | Accountable, in their own streams, for operating within the controls of VS-07 and supplying evidence |

### 6. Capabilities, processes, and functions

#### Capability foundations

| Capability group | Capabilities | Role in VS-07 |
|---|---|---|
| 4.1 Strategy and leadership | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improvement management, 4.1.5 Accountability | Set governance strategy and accountability, translate it into policies, improve governance, report on compliance |
| 2.1 Data management | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management | Govern the life cycle of data assets, metadata, and quality across the chain |
| 3.1 Business operations | 3.1.7 Legal support | Interpret regulation and assess agreements |
| 3.3 Security and privacy | 3.3.1 Privacy management, 3.3.2 Security planning, 3.3.3 Security incident management | Set and assure the privacy and information security framework |

#### Stages, processes, and functions

| Stage | Realised by processes | Main functions |
|---|---|---|
| VS-07.1 Define Governance Frameworks and Policies | DLM-1 Plan and design data assets | FUN-1.2 Govern and steer the organisation; FUN-5.1 Manage the quality framework; FUN-7.1 Govern data |
| VS-07.2 Establish Legal and Regulatory Compliance Mechanisms | DLM-4 Classify and protect data | FUN-10.5 Manage legal affairs; FUN-10.8 Manage information security and privacy |
| VS-07.3 Implement Data and Metadata Governance | OVA-2 Metadata Management; OVA-3 Data Management; DLM-1 Plan and design data assets; DLM-6 Provide data for reuse | FUN-7.1 Govern data; FUN-7.2 Manage metadata |
| VS-07.4 Monitor Quality and Compliance Indicators | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use; MDS-8 Monitor use and compliance; DSP-5 Monitor compliance and report | FUN-5.2 Assure and review quality; FUN-7.1 Govern data |
| VS-07.5 Audit, Certify and Report Compliance | OVA-1 Quality Management; PRD-8.2 Conduct evaluation | FUN-1.2 Govern and steer the organisation; FUN-5.2 Assure and review quality |
| VS-07.6 Update and Improve Governance Mechanisms | PRD-8.3 Agree an action plan; DLM-10 Archive and preserve data; DLM-11 Dispose of data | FUN-2.1 Plan capability improvements; FUN-7.1 Govern data |

|**PLACEHOLDER: ArchiMate view VS-07 (b) stages realised by processes and functions**|
|---|

#### Framework mappings

Where the primary value streams map to GSBPM production phases, VS-07 maps to the GAMSO overarching activities.

| GAMSO area | Relevance to VS-07 | Stages |
|---|---|---|
| Strategy and Leadership | Set governance strategy, charters, and accountability; manage organisational and ethical frameworks | VS-07.1, VS-07.5 |
| Corporate Support | Manage the legal framework, quality management, and information security governance | VS-07.2, VS-07.4, VS-07.5 |
| Capability Management | Govern the life cycle of standards, methods, and data assets | VS-07.3, VS-07.6 |

External standards that VS-07 aligns the NSI with: European Statistics Code of Practice, GDPR, GSBPM, GAMSO, and the ISO data quality principles.

### 7. Principles

VS-07 foregrounds SAF-P03 and SAF-P04, and it enforces the data principles SAF-P09, SAF-P10, and SAF-P11 across the whole chain.

| Principle | Statement | Application in VS-07 |
|---|---|---|
| SAF-P09 | No data without metadata and classification | Governs metadata and classification obligations and audits them across every value stream |
| SAF-P10 | Security By Design | Sets and assures the information security and access control framework |
| SAF-P11 | Privacy By Design | Sets the privacy, confidentiality, and disclosure control policy and verifies compliance |
| SAF-P03 | Active Life Cycle management | Governs the life cycle of policies, standards, classifications, and data assets; versions governance artefacts and retires obsolete ones |
| SAF-P04 | Maximise the benefits for the organisation | Aligns controls to organisational value and accountability, avoiding governance for its own sake |
| SAF-P07 | Implement loosely coupled processes and systems | Defines the steady-state interface and event conventions that the value streams are governed by |

### 8. Interfaces, services, and events

**Business services**

VS-07 offers governance and assurance as a service to every other value stream.

| Service | Offered to | Realised in | Interfaces |
|---|---|---|---|
| Governance framework and policy service | All value streams | VS-07.1, VS-07.2, VS-07.3 | Policy set, legal register, role assignments, metadata and lineage rules |
| Compliance assessment service | VS-08, process owners | VS-07.2 | Compliance criteria; assessment of new methods and processes before production |
| Quality and compliance monitoring service | Management, process owners | VS-07.4 | Dashboards and scorecards |
| Audit and certification service | Management, supervisory authorities, the public, international peers | VS-07.5 | Audit reports, certifications, assurance statements, transparency reports |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Regulatory change* | Review of the legal register and policies in VS-07.2 and VS-07.6 |
| *Policy update issued* | The value streams adapt their designs and controls |
| *Compliance review* | Periodic review of a stream's compliance evidence in VS-07.4 |
| *Method compliance assessment* | Request from VS-08 to assess a new method before production |
| *Security/continuity review* | Review of the security posture and incident evidence of VS-09 |
| *Audit* | Start of an internal or external audit in VS-07.5 |
| *Certification* | Outcome of VS-07.5 towards external parties |
| *Transparency report* | Publication of accountability information, also used by VS-10 |

**Interaction with the primary value streams**

Each primary value stream supplies the evidence for the audit focus of the state it produces (see *Producing and consuming domains* in each state of the Steady-State Architecture).

| Value stream | Provides to VS-07 | Audit focus of VS-07 |
|---|---|---|
| VS-01 Data Acquisition and Ingestion | Audit trails, records of processing, agreement compliance | Provenance and legal basis (State #1) |
| VS-02 Data Standardization and Integration | Mapping lineage, privacy and standards compliance | Mapping lineage and pseudonymisation (State #2) |
| VS-03 Data Editing and Enrichment | Edit audit, disclosure risk and methodology compliance | Edit lineage, methodology compliance, disclosure risk (State #3) |
| VS-04 Estimation, Analysis and Statistical Modeling | Reproducibility audit, disclosure control reporting | Methodology, reproducibility, approval (State #4) |
| VS-05 Statistical Product Composition | Approval and confidentiality reporting | Methodology, reproducibility, approval (State #4 approved) |
| VS-06 Dissemination and Service Delivery | Disclosure, equal access, and accessibility compliance | Disclosure control, equal access, release authorisation (State #5) |

**Interaction with the other supporting value streams and external parties**

| Counterpart | VS-07 provides | VS-07 receives |
|---|---|---|
| VS-08 Innovation and Methodological Development | Compliance criteria a new method must meet | Requests to assess and approve new methods before production |
| VS-09 Infrastructure and Platform Enablement | Security and continuity policy to enforce | Security posture and incident evidence |
| VS-10 Customer and Stakeholder Engagement | Transparency and accountability commitments | Stakeholder trust signals and complaints |
| Regulators, the public, international peers | Certification, assurance, transparency reports | Regulatory requirements and changes |

### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| Policy coverage | Share of value streams and data domains operating under current, approved policies | Per policy domain, annually |
| Audit findings closed on time | Percentage of audit findings remediated within their agreed deadline | Per audit cycle |
| Compliance incidents | Number of confidentiality, security, or legal incidents | Per quarter (target: zero) |
| Certification status | Certifications and peer review assessments held and current (for example the Code of Practice) | Annually |
| Metadata governance compliance | Share of registered datasets meeting the SAF-P09 obligations | Per cycle, from the streams' *Audit and Compliance Reporting* |
| Regulatory response time | Time from detection of a regulatory change to an updated policy being issued | Per change |

### 10. Examples

**Regulatory change.** A change in data protection law is detected. Legal counsel interprets it, and the compliance officer updates the legal register and the privacy policy. The *Policy update issued* event reaches the process owners, who adapt their designs and controls. The regulatory response time KPI measures the time from detection to the updated policy.

**Peer review.** The quality manager prepares the NSI for a peer review against the European Statistics Code of Practice. The evidence comes from the dashboards of VS-07.4 and from the *Audit and Compliance Reporting* of each primary value stream. The findings are tracked to closure in VS-07.6.

| **Toolkit:** SAF-TK-V07 VS-07 maturity checklist and scenarios |
|---|



## VS-08 Innovation and Methodological Development

### 1. Purpose and value created

VS-08 makes sure the statistical organisation does not stand still. It discovers, tests, and introduces new ways of working: new data sources, methods, tools, and technologies. It moves the organisation from "we have always done it this way" to "we can do this better, faster, and smarter." It connects research, methodology, IT, and business users. The value created is **continuous improvement**: the SAF stays future-proof for new data (IoT, administrative data, data spaces), new techniques (machine learning, small-area estimation), and new operating models (secure processing environments, data sharing).

VS-08 does not transform data. It improves the methods and tools that the primary value streams use, and its output is an enabling capability: validated methods, documented tools, reference implementations, and trained staff.

::: {.callout-note title="Signature discipline: controlled innovation"}
Innovation in VS-08 is controlled. Only methods that are sound, documented, and compliant reach production. The evaluation gate in VS-08.3 stops attractive but unsound ideas, and the transfer gate in VS-08.5 moves a validated method into production only after VS-07 approval and on VS-09 platforms.
:::

VS-08 corresponds to the horizontal business domain **Innovation**. Its domain processes are mainly realised by the business function FUN-4 *Methodology and Research*.

|**PLACEHOLDER: ArchiMate view VS-08 (a) value stream and capabilities**|
|---|

<br>

### 2. Relation to the value chain

VS-08 is not a stage in the production line. It runs alongside the chain as a continuous research and development pipeline. It draws its agenda from the needs of the primary value streams and feeds validated improvements back into them. It has no state transition, no quality gate of its own, and no registration event. It aligns to the GAMSO area **Capability Management**, with the innovation agenda set under **Strategy and Leadership**.

The improvement recommendations that every primary value stream produces in its *Continuous Improvement* sub-process (see [Standard activities in every value stream](#standard-vs-activities)), together with user needs surfaced by VS-10 and an external scan of technology, form the **innovation backlog** of VS-08. VS-08 is also an occasional consumer of States #1, #2, and #3, for the exploration of sources and the testing of new methods, always under specific authorisation.

| Primary value stream | Provides | Receives |
|---|---|---|
| VS-01 Data Acquisition and Ingestion | New ways to connect to data spaces and new sources; new collection methods | Improvement needs; authorised access to #1 for source exploration |
| VS-02 Data Standardization and Integration | New mapping or classification techniques | Improvement needs; authorised access to #2 for exploration of sources and methods |
| VS-03 Data Editing and Enrichment | Smarter imputation and outlier detection; new editing and coding methods | Improvement needs; authorised access to #3 for testing new editing, imputation, or coding methods |
| VS-04 Estimation, Analysis and Statistical Modeling | New models and methods based on machine learning; small-area estimation | Improvement needs; fitness-for-purpose validation |
| VS-05 Statistical Product Composition | Validated methods and tools transferred to production | Improvement needs; fitness-for-purpose validation |
| VS-06 Dissemination and Service Delivery | New channels: APIs, linked data, interactive views | Improvement needs; fitness-for-purpose validation |

|**PLACEHOLDER: ArchiMate view VS-08 (c) interactions with the value chain: improvement needs from VS-01 to VS-06, user needs from VS-10, and the external scan entering VS-08; validated methods and tools leaving through the VS-08.5 transfer gate to the target production stream (for example VS-03 or VS-04); compliance approval from VS-07 and sandbox and production platforms from VS-09**|
|---|

<br>

### 3. Stages

The stages form a continuous innovation pipeline: identify, research, evaluate, develop, integrate, and share. The last stage surfaces the next round of needs. The cadence is project or pipeline based, not per production cycle.

| Stage | Name | Value added |
|---|---|---|
| VS-08.1 | Identify Innovation Needs and Opportunities | Promising developments are known |
| VS-08.2 | Conduct Research and Proof-of-Concepts | Ideas are tested in a limited scope |
| VS-08.3 | Evaluate Methodological Soundness and Feasibility | Only sound and feasible innovations proceed |
| VS-08.4 | Develop and Document New Methodologies or Tools | Innovations are ready for reuse |
| VS-08.5 | Integrate Innovation into Production Environments | Innovations run in production under governance |
| VS-08.6 | Promote Knowledge Sharing and Capability Building | Staff can apply the new methods |

<br>

#### VS-08.1 Identify Innovation Needs and Opportunities

**Value created:** *A prioritised view of the developments worth pursuing.*

The pipeline starts by scanning technological, methodological, and policy developments, such as AI, machine learning, new data sources, and cloud. It also takes in the improvement backlog of the chain: the recommendations of the primary value streams and the user-driven needs from VS-10. Candidates are prioritised by organisation-wide value and scalability, not by novelty (SAF-P04). The result is the prioritised innovation backlog.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Scan technological, methodological, and policy developments (AI, machine learning, new sources, cloud) | Scan results | No reference process (NSI-specific) | 2.2.1 Data source exploration; 2.2.3 Methodology |
| Collect improvement recommendations from the primary value streams | Backlog entries (*Innovation need raised*) | PRD-8.3 Agree an action plan | 4.1.4 Improvement management |
| Collect user needs that imply new methods, from VS-10 | Backlog entries (*User-driven innovation need*) | PRD-1.1 Identify needs | 2.2.5 User research |
| Check whether new or existing data sources can meet the need | Source assessment | PRD-1.5 Check data availability and suitability | SAF-P08 |
| Prioritise candidates by organisation-wide value and scalability | Prioritised innovation backlog | PRD-1.6 Prepare and submit business case | SAF-P04 |

<br>

#### VS-08.2 Conduct Research and Proof-of-Concepts

**Value created:** *Evidence on whether an idea works, before any commitment.*

Candidates from the backlog enter controlled experiments and pilots. Each tests a new method or technology in a limited scope before any commitment is made. Experiments run in research or sandbox environments that VS-09 provides. Where they need production data, they use registered versions of States #1, #2, or #3 under specific authorisation, never the working environment of a producing domain. Subject-matter experts from the production streams bring the real problem.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define the scope and success criteria of the experiment | Experiment plan | No reference process (NSI-specific) | 2.2.3 Methodology |
| Request a sandbox environment from VS-09 | Research environment (*Platform request*) | No reference process (NSI-specific) | VS-09 |
| Obtain authorised access to registered data of #1, #2, or #3 | Access granted for a stated purpose and period | DLM-6 Provide data for reuse | SAF-P10, SAF-P11 |
| Run the proof-of-concept or pilot in limited scope | Experiment and pilot results | No reference process (NSI-specific) | 2.2.1 Data source exploration; 2.2.2 Product innovation |
| Record research findings | Research findings | OVA-5 Knowledge Management | SAF-P03 |

<br>

#### VS-08.3 Evaluate Methodological Soundness and Feasibility

**Value created:** *Only sound and feasible innovations proceed.*

Promising results are evaluated for accuracy, scalability, and alignment with the quality and ethical frameworks of the NSI. This stage is the gate that stops attractive but unsound ideas. A healthy gate stops some proofs-of-concept, and every stop has a documented rationale. Subject-matter experts confirm fitness for purpose.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Assess accuracy against the intended use | Soundness assessment | PRD-3.6 Test statistical business process | 2.1.3 Statistical quality management |
| Assess scalability and feasibility in production conditions | Feasibility assessment | PRD-3.6 Test statistical business process | |
| Check alignment with the quality and ethical frameworks | Soundness and feasibility assessment | OVA-1 Quality Management | |
| Validate fitness for purpose with subject-matter experts | Fitness-for-purpose validation | PRD-3.6 Test statistical business process | |
| Decide to proceed or stop, with a documented rationale | Gate decision record | PRD-3.6 Test statistical business process | SAF-P03 |

<br>

#### VS-08.4 Develop and Document New Methodologies or Tools

**Value created:** *Innovations that are reproducible and ready for reuse.*

What passes the gate is developed into standardised procedures, algorithms, or reference implementations. It is documented so that it is reproducible and ready to hand over, rather than living in a researcher's notebook. Shared and open tooling comes first, and the NSI contributes back (SAF-P01). Each artefact has a designated owner and a version.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Formalise the validated method as a standardised procedure or algorithm | Standardised method | OVA-5 Knowledge Management | 2.2.3 Methodology |
| Build the reference implementation, documented and version-controlled | Reference implementation | PRD-3.2 Reuse or build processing and analysis components | SAF-P01; 3.2.1 Application development |
| Document the method and tool for reproducibility | Method documentation | OVA-5 Knowledge Management | |
| Assign an owner and a version to each artefact | Versioned method and tool | OVA-5 Knowledge Management | SAF-P03 |

<br>

#### VS-08.5 Integrate Innovation into Production Environments

**Value created:** *Innovations run in production under governance.*

This is the defining stage of VS-08: the governed transfer of a validated method or tool from pilot to production in the relevant primary value stream. The method passes the compliance assessment of VS-07 before transfer and runs on VS-09 platforms. It must fit the steady-state interfaces, so that the production streams stay loosely coupled (SAF-P07). Once transferred, the method becomes part of the design metadata of the receiving stream. This is the GAMSO idea of transferring mature results of innovation into production.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Submit the method to VS-07 for compliance assessment before production | Compliance approval (*Method compliance assessment*) | PRD-3.7 Finalise production systems | VS-07 |
| Check interoperability with the steady-state interfaces of the target stream | Interoperability confirmation | PRD-3.4 Configure workflows | SAF-P07 |
| Onboard the method or tool on the VS-09 production platform | Production runtime (*Production onboarding*) | PRD-3.7 Finalise production systems | VS-09 |
| Hand over the method as design metadata to the receiving stream | Method live in a production stream (*Method transferred to production*) | PRD-3.7 Finalise production systems; OVA-2 Metadata Management | GAMSO Capability Management |
| Train the production staff and arrange support | Trained operating team | PRD-3.7 Finalise production systems | |

<br>

#### VS-08.6 Promote Knowledge Sharing and Capability Building

**Value created:** *Staff who can adopt and sustain the new methods.*

VS-08 disseminates results, best practices, and guidelines, and grows staff competency, so that the organisation can actually adopt and sustain the new way of working. Adoption in the target streams is followed up. This in turn surfaces the next round of needs for VS-08.1.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Disseminate results, best practices, and guidelines | Disseminated guidance | OVA-5 Knowledge Management | SAF-P05 |
| Train staff on new methods | Trained staff | OVA-5 Knowledge Management | 3.1.1 Personnel management (HR) |
| Share methods and tools with other NSIs and open-source communities | Shared methods and contributions | OVA-5 Knowledge Management | SAF-P01; 4.1.6 Collaboration |
| Follow up adoption in the target streams and collect new needs | Adoption measures, backlog input | PRD-8.1 Gather evaluation inputs | 4.1.4 Improvement management |

### 4. Plan, build, operate, and improve

VS-08 is itself a capability that is planned, built, operated, and improved. Unlike a primary value stream, it produces methods and capability, not statistical data. The stages group into the cycle: VS-08.1 and VS-08.2 find what is worth doing, VS-08.3 and VS-08.4 make it sound and real, VS-08.5 puts it to work, and VS-08.6 spreads it.

| Cycle step | What happens in VS-08 | Main outputs | SAF process |
|---|---|---|---|
| Plan | Set the innovation strategy, aligned to the organisational strategy, and the evaluation criteria of the VS-08.3 gate | Innovation strategy, evaluation criteria | PRD-1.6 Prepare and submit business case; OVA-1 Quality Management |
| Build | Build research and sandbox environments, with VS-09 | Research environments | No reference process (NSI-specific) |
| Operate | Run the innovation pipeline continuously, from backlog to transfer | Validated methods and tools in production | PRD-3.6 Test statistical business process; PRD-3.7 Finalise production systems |
| Improve | Learn from VS-08.6 and from retrospectives; review the key performance indicators (attribute 9) | Improvement actions for the pipeline | PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan |

| Aspect | VS-08 |
|---|---|
| Trigger | *Innovation need raised*; *User-driven innovation need*; results of the external scan |
| Cadence | Continuous pipeline; project based per innovation |
| Performed by | ROL-07 Methodologist, ROL-15 Subject-matter statistician (researcher or data scientist), ROL-10 Data engineer |
| Input | Innovation backlog; authorised access to #1, #2, #3; sandbox environments |
| Output | Validated methods and tools transferred to production; trained staff |
| Control point | Soundness and feasibility gate in VS-08.3; compliance approval by VS-07 before the transfer in VS-08.5 |
| Exception path | Stop at VS-08.3 with a documented rationale; return to research when the compliance assessment fails |

**Enabling artefacts.** VS-08 manages enabling artefacts, not statistical data. They are version-managed across their life cycle (SAF-P03). Each artefact has a designated owner, changes are tracked, prior versions remain identifiable, and superseded methods are formally retired. Once transferred, an artefact becomes part of the design metadata of a production stream.

| Artefact | Produced in |
|---|---|
| Innovation backlog | VS-08.1 |
| Research findings and proof-of-concept results | VS-08.2 |
| Soundness and feasibility assessments | VS-08.3 |
| Validated methods, algorithms, and reference implementations | VS-08.4 |
| Knowledge assets: guidelines, training | VS-08.6 |

### 5. Actors and roles

The table shows the reference roles involved in VS-08 (see *Role names in the value streams*).

| Actor or role | ID | Process type | Responsibility in VS-08 |
|---|---|---|---|
| Head of methodology or innovation | ROL-01, ROL-07 | Management | Process owner of VS-08; owns the innovation agenda and the methodological standards |
| Methodologist | ROL-07 | Design | Evaluates soundness and feasibility; formalises validated methods |
| Researcher or data scientist | ROL-15 | Execution | Conducts research and proofs-of-concept |
| Subject-matter expert from the production streams | ROL-15 | Execution | Brings the real problem and validates fitness for purpose |
| Tool or platform engineer | ROL-10 | Implementation | Builds reference implementations and prepares them for production, with VS-09 |
| Platform engineer | ROL-11 | Implementation | Provides sandbox and production platforms, anchored in VS-09 |
| Compliance officer | ROL-19 | Management | Approves a method against compliance criteria before transfer (VS-07) |
| Trainer or knowledge manager | Not in the reference set | Execution | Disseminates results and builds staff competency |

### 6. Capabilities, processes, and functions

#### Capability foundations

| Capability group | Capabilities | Role in VS-08 |
|---|---|---|
| 2.2 Research | 2.2.1 Data source exploration, 2.2.2 Product innovation, 2.2.3 Methodology | Explore new sources, products, and methods |
| 1.1 Statistical design and build | 1.1.2 Design statistics product, 1.1.3 Build statistics product | Develop validated methods into designs and reference implementations; supports all primary capabilities |
| 3.1 Business operations | 3.1.1 Personnel management (HR) | Build staff competency in new methods |
| 3.2 Computerisation and automation | 3.2.1 Application development | Build reference implementations |
| 4.1 Strategy and leadership | 4.1.3 Change management, 4.1.4 Improvement management, 4.1.6 Collaboration | Set the innovation agenda, take in improvement needs, manage the change into production, and cooperate with other NSIs |

#### Stages, processes, and functions

| Stage | Realised by processes | Main functions |
|---|---|---|
| VS-08.1 Identify Innovation Needs and Opportunities | PRD-1.5 Check data availability and suitability | FUN-4.2 Research and innovate |
| VS-08.2 Conduct Research and Proof-of-Concepts | No reference process (NSI-specific) | FUN-4.2 Research and innovate |
| VS-08.3 Evaluate Methodological Soundness and Feasibility | PRD-3.6 Test statistical business process | FUN-4.1 Manage statistical and analytical methodology; FUN-5.2 Assure and review quality |
| VS-08.4 Develop and Document New Methodologies or Tools | PRD-3.2 Reuse or build processing and analysis components; OVA-5 Knowledge Management | FUN-4.1 Manage statistical and analytical methodology; FUN-10.4 Manage information and records |
| VS-08.5 Integrate Innovation into Production Environments | PRD-3.7 Finalise production systems | FUN-2.4 Transfer capability improvements to operations; FUN-3.1 Design and build statistical products |
| VS-08.6 Promote Knowledge Sharing and Capability Building | OVA-5 Knowledge Management | FUN-10.1 Manage human resources; FUN-10.4 Manage information and records |

|**PLACEHOLDER: ArchiMate view VS-08 (b) stages realised by processes and functions**|
|---|

#### Framework mappings

| Cycle step | SAF business processes | GAMSO | SAF capabilities |
|---|---|---|---|
| Plan | PRD-1.1, PRD-1.5, PRD-1.6, PRD-8.3, OVA-1 | Strategy and Leadership (set the innovation agenda aligned to the organisational strategy) | 2.2.1 Data source exploration, 2.2.5 User research, 4.1.4 Improvement management |
| Build | PRD-3.2, PRD-3.6, OVA-5, DLM-6 | Capability Management (manage research and innovation, develop methodology) | 2.2.2 Product innovation, 2.2.3 Methodology, 3.2.1 Application development |
| Operate | PRD-3.4, PRD-3.7, OVA-2 | Capability Management (manage change, transfer to production) | 1.1.3 Build statistics product, 4.1.3 Change management |
| Improve | OVA-5, PRD-8.1 to PRD-8.3 | Capability Management (build staff capability) | 3.1.1 Personnel management (HR), 4.1.6 Collaboration |

### 7. Principles

| Principle | Statement | Application in VS-08 |
|---|---|---|
| SAF-P01 | Actively participate in open-source communities to maintain collective control over statistical processes | Innovate on and contribute to shared, open methods and tools rather than vendor black boxes. |
| SAF-P05 | IT and technology is everyone's business | Connect research, methodology, IT, and business users; build broad capability to adopt new methods. |
| SAF-P03 | Active Life Cycle management | Manage methods and tools across their life cycle, from proof-of-concept to production to retirement. |
| SAF-P04 | Maximise the benefits for the organisation | Prioritise innovations by organisation-wide value and scalability, not novelty. |
| SAF-P07 | Implement loosely coupled processes and systems | Transfer methods that fit the steady-state interfaces, so that the production streams stay decoupled. |

### 8. Interfaces, services, and events

**Business services**

| Service | Offered to | Realised in | Interfaces |
|---|---|---|---|
| Innovation intake service | VS-01 to VS-06, VS-10 | VS-08.1 Identify Innovation Needs and Opportunities | Innovation backlog |
| Method and tool transfer service | VS-01 to VS-06 | VS-08.5 Integrate Innovation into Production Environments | Validated method, reference implementation, design metadata |
| Knowledge and training service | All staff of the NSI | VS-08.6 Promote Knowledge Sharing and Capability Building | Guidelines, training |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Innovation need raised* | A primary value stream adds an improvement need to the backlog (VS-08.1) |
| *User-driven innovation need* | VS-10 adds a user need that implies a new method (VS-08.1) |
| *Platform request* | VS-08 asks VS-09 for a sandbox or production platform |
| *Method compliance assessment* | VS-08 submits a method to VS-07 before transfer (VS-08.5) |
| *Production onboarding* | The method or tool is onboarded on the VS-09 production runtime |
| *Method transferred to production* | Completion of VS-08.5; the method is live in the receiving stream |

**Interaction with the primary value streams**

| Counterpart | VS-08 provides | VS-08 receives | Event |
|---|---|---|---|
| All primary streams (VS-01 to VS-06) | Validated methods and tools transferred to production | Improvement recommendations from their *Continuous Improvement* sub-process; fitness-for-purpose validation | *Innovation need raised*, *Method transferred to production* |
| VS-10 Customer and Stakeholder Engagement | New service and product possibilities | User needs that imply new methods | *User-driven innovation need* |
| VS-07 Governance and Compliance | Methods for pre-production approval | Compliance criteria and approval | *Method compliance assessment* |
| VS-09 Infrastructure and Platform Enablement | Requirements for sandbox and production platforms | Research environments and production runtime | *Platform request*, *Production onboarding* |

### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| Idea-to-production lead time | Median time from a backlog item (VS-08.1) to a completed transfer (VS-08.5) | Per transferred innovation |
| Transfer rate and durability | Methods and tools transferred to production per year, and the share still in use after 12 months | Annually |
| Gate effectiveness | Share of proofs-of-concept stopped at the VS-08.3 gate with a documented rationale (a healthy gate stops some) | Per evaluation |
| Backlog responsiveness | Share of prioritised backlog items reaching a proof-of-concept within the agreed time | Per planning period |
| Capability building | Staff trained on new methods, and adoption rate in the target streams | Per year, per transfer |

### 10. Examples

**Smarter imputation.** VS-03 reports through its *Continuous Improvement* sub-process that manual follow-up of missing values is too costly. VS-08 tests an imputation method based on machine learning on an authorised copy of State #3, evaluates its accuracy at the VS-08.3 gate, and documents it with a reference implementation. After VS-07 approval it is transferred into the design of VS-03.

**New data source.** A data space offers a new source for an existing statistic. VS-08 explores the source under specific authorisation, tests whether it can replace part of a survey, and hands the validated connection and method over to VS-01, which then acquires the source in production.

| **Toolkit:** SAF-TK-V08 VS-08 maturity checklist and scenarios |
|---|



## VS-09 Infrastructure and Platform Enablement

### 1. Purpose and value created

VS-09 provides the technical and digital foundation of the statistical organisation. The other value streams work on data, methods, governance, or relationships. VS-09 makes sure that all of this work can actually run: safely, efficiently, and at scale. It delivers the IT environments, data platforms, tools, and integration services that statistical production needs, from data collection to dissemination. It keeps them secure, resilient, and compliant, and flexible enough to adopt new technologies and new data sources as the NSI modernises. The value created is **reliable enablement**, or operational capability and continuity: a stable, modern, and adaptive foundation that turns infrastructure from a background function into an active enabler of the statistical mission.

VS-09 corresponds to the horizontal domain **Infrastructure**. Its signature discipline is that platforms are run as supported, monitored, and recoverable services, with security built in from the start, never as one-off builds. This section describes the business layer of that enablement: the capability of providing platforms and services. The application and technology architecture of the platforms themselves is described in the application and technology layers of the SAF, not here.

|**PLACEHOLDER: ArchiMate view VS-09 (a) value stream and capabilities**|
|---|

<br>

### 2. Relation to the value chain

VS-09 is not a stage in the production line. It is the foundation underneath it: every primary and supporting value stream runs on the platforms that VS-09 provides. VS-09 does not take data from one state to the next and has no registration event. It provides the environments in which the states are stored, the gates are run, and the handover events are delivered. It runs continuously, as an always-on service, not per production cycle. Its output is an enabling capability, not a data artefact: platforms, environments, integration services, and assured availability.

VS-09 receives requirements from business capabilities, data volumes, and the other value streams, in particular VS-08 for new technology and VS-06 for dissemination platforms. Its security and continuity posture is governed by VS-07.

| Primary value stream(s) | Provides | Receives |
|---|---|---|
| VS-01 Data Acquisition and Ingestion | Secure collection and transfer channels, storage, catalogue, event interfaces | Capacity and channel requirements |
| VS-02 to VS-05 (standardisation, editing, analysis, composition) | Computing and orchestration to process large datasets efficiently; storage and versioning of the states | Capacity demand, processing requirements |
| VS-06 Dissemination and Service Delivery | Portals, APIs, dashboards, secure research environments | Channel and scaling requirements |
| All primary value streams | Steady-state event interfaces, assured availability, recovery | Incidents, capacity demand |

VS-09 aligns to GAMSO, not to the production phases of GSBPM, and to the supporting business capabilities of the SAF.

| GAMSO area or SAF domain | Relevance to VS-09 |
|---|---|
| Capability Management | Manage the IT capability; introduce and modernise technology |
| Corporate Support | Manage IT services and operations, security, and business continuity |
| SAF capability domain 3, Supporting business capabilities | 3.2 Computerisation and automation (application development, functional management, technical management, IT infrastructure); 3.3 Security and privacy (technical) |

|**PLACEHOLDER: ArchiMate view VS-09 (c) interactions with the value chain: requirements from business capabilities, data volumes, VS-08 (new technology) and VS-06 (channels) flowing into VS-09; environments, platforms, integration, and availability flowing to all value streams VS-01 to VS-10; security and continuity policy from VS-07; incidents and capacity demand flowing back from all streams**|
|---|

<br>

### 3. Stages

The stages form a continuous enablement cycle: define, design, provision, integrate, assure, and evolve. The first two stages plan the foundation, the next two build it, VS-09.5 operates it, and VS-09.6 improves it (see attribute 4).

| Stage | Name | Value added |
|---|---|---|
| VS-09.1 | Define Digital and Technical Requirements | Infrastructure needs follow from business needs |
| VS-09.2 | Design Platform and Infrastructure Architecture | Platforms are designed for storage, processing, integration, and secure access |
| VS-09.3 | Provision and Configure Platforms | Environments are available with the required controls |
| VS-09.4 | Enable Integration and Orchestration Services | Processes and services are connected |
| VS-09.5 | Ensure Performance, Security and Continuity | Platforms are reliable and protected |
| VS-09.6 | Evolve and Modernise the Technical Ecosystem | The technical landscape stays current |

<br>

#### VS-09.1 Define Digital and Technical Requirements

**Value created:** *Infrastructure needs follow from business needs.*

The cycle starts from the business, not from technology. The team identifies the infrastructure needs that arise from the business capabilities, the data volumes, and the analytical complexity of the work across the value streams. Requirements come from the consuming value streams: capacity and channel requirements from VS-01, processing demand from VS-02 to VS-05, channel and scaling requirements from VS-06, and new-technology adoption requests from VS-08. The result is a set of infrastructure requirements derived from business needs.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Collect requirements from the consuming value streams | Requirements backlog | PRD-2.6 Design production systems and workflows | SAF-P05 |
| Derive infrastructure needs from business capabilities, data volumes, and analytical complexity | Infrastructure requirements | PRD-2.6 Design production systems and workflows | 3.2.2 Functional management |
| Assess requests to adopt new technology from VS-08 | Technology onboarding assessment | PRD-2.6 Design production systems and workflows | GAMSO Capability Management |

<br>

#### VS-09.2 Design Platform and Infrastructure Architecture

**Value created:** *Platforms are designed for storage, processing, integration, and secure access.*

The requirements feed the design of the platform and infrastructure architecture. The team produces blueprints for data storage, processing, integration, and secure access, for example a data fabric, a data market, and compute platforms. Reuse of shared and open platform components comes first, in line with SAF-P01. Security and access control are part of the blueprint from the start, in line with SAF-P10.

::: {.callout-note title="On the Medallion architecture"}
A platform team may use Bronze, Silver, and Gold to organise storage, staging, and table optimisation inside the platform. That is an engineering pattern, not a governance model: it describes how data has been refined, not what the data means, what methodological state it is in, or what another statistical process may rely on. The steady states remain the governance model. Medallion, if used at all, sits underneath it as a storage convention (see *Combining the models*).
:::

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Design blueprints for storage, processing, integration, and secure access | Architecture blueprints | PRD-2.6 Design production systems and workflows | 4.1.7 Architecture Management |
| Select shared and open platform components before building new ones | Sourcing decision | PRD-2.6 Design production systems and workflows | SAF-P01 |
| Design security and access control into the platforms | Security design | PRD-2.6 Design production systems and workflows | SAF-P10; 3.3.2 Security planning |
| Map platform storage conventions (such as Medallion layers) onto the steady states | Storage convention | PRD-2.6 Design production systems and workflows | |

<br>

#### VS-09.3 Provision and Configure Platforms

**Value created:** *Environments are available with the required controls.*

The architecture is realised by deploying environments, on-premise, hybrid, or in the cloud, with the necessary governance, monitoring, and security controls. This covers the production environments of the primary value streams, the portals, APIs, and dashboards of VS-06, the secure research environments for microdata access, and the sandbox and production runtime that VS-08 needs for new technology. Platforms are self-service and well documented, so that technology serves all teams (SAF-P05).

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Deploy environments (on-premise, hybrid, cloud) | Deployed environments | PRD-3.4 Configure workflows | 3.2.5 IT infrastructure |
| Configure governance, monitoring, and security controls | Controlled environments | PRD-3.4 Configure workflows | SAF-P10; 3.3.4 Logical identity and access control |
| Provide secure research environments for microdata access | Secure processing environment | MDS-4 Provide a secure processing environment | |
| Provide sandbox and production runtime for VS-08 | Research and production environments | PRD-3.4 Configure workflows | |
| Document platforms for self-service use | Platform documentation | PRD-3.4 Configure workflows | SAF-P05 |

<br>

#### VS-09.4 Enable Integration and Orchestration Services

**Value created:** *Processes and services are connected.*

This stage provides the APIs, workflow engines, and automation that connect the business services and processes. It includes the steady-state event interfaces that the primary value streams rely on: the registration events, such as *Raw Data Registered*, that trigger the next value stream. It also includes the connectivity to data spaces.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Provide APIs and workflow engines | Integration and orchestration services | PRD-3.4 Configure workflows | 3.2.1 Application development |
| Provide the steady-state event interfaces | Event interfaces | PRD-3.4 Configure workflows | SAF-P07 |
| Operate data space connectivity | Data space connectors | DSP-4 Exchange data under usage control | |

<br>

#### VS-09.5 Ensure Performance, Security and Continuity

**Value created:** *Platforms are reliable and protected.*

Day to day, VS-09 monitors platform performance, implements data protection, manages incidents, and guarantees availability and disaster recovery. This is the assurance that the whole chain can run reliably (SAF-P06). Platforms are run as actively supported, monitored services (SAF-P02). Security controls and continuity are assessed with VS-07, which sets the security and continuity policy.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Monitor platform performance and capacity | Performance monitoring | PRD-3.5 Test production systems | SAF-P02; 3.2.3 Technical management |
| Implement data protection: backup and recovery of stored versions | Backups, recovery procedures | DLM-5 Store and version data | 3.3.6 IT security services |
| Manage incidents and restore service | Incident records | PRD-3.5 Test production systems | 3.3.3 Security incident management |
| Guarantee availability and disaster recovery | Availability and disaster recovery plans | DLM-5 Store and version data | SAF-P06 |
| Assess the security posture with VS-07 | Security and continuity evidence | PRD-3.5 Test production systems | SAF-P10 |

<br>

#### VS-09.6 Evolve and Modernise the Technical Ecosystem

**Value created:** *The technical landscape stays current.*

The cycle ends by evolving the technical ecosystem. New technologies are introduced, often transferred from VS-08. Obsolete components are retired. The foundation stays flexible for new data sources and operating models. The result is a modernisation roadmap and adopted technologies, which feed the next round of requirements.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Introduce new technologies, often transferred from VS-08 | Adopted technologies | No reference process (NSI-specific) | FUN-2.2 Develop capability improvements |
| Retire obsolete components | Retirement records | No reference process (NSI-specific) | SAF-P03 |
| Maintain the modernisation roadmap | Modernisation roadmap | No reference process (NSI-specific) | 4.1.3 Change management |

### 4. Plan, build, operate, and improve

VS-09 is itself a capability that is designed, built, operated, and improved. Unlike a primary value stream it produces platforms and assured availability, not statistical data, and it runs as an always-on service rather than a per-cycle production run. Its security and continuity are governed by VS-07.

| Cycle step | What happens in VS-09 | Main outputs | SAF process |
|---|---|---|---|
| Plan | Define requirements and design the architecture and operating model (VS-09.1, VS-09.2) | Infrastructure requirements, architecture blueprints | PRD-2.6 Design production systems and workflows |
| Build | Provision platforms and enable integration (VS-09.3, VS-09.4) | Deployed environments, integration services, event interfaces | PRD-3.4 Configure workflows; MDS-4 Provide a secure processing environment; DSP-4 Exchange data under usage control |
| Operate | Continuous monitoring, security, and incident management (VS-09.5) | Monitoring, security, availability, disaster recovery | PRD-3.5 Test production systems; DLM-5 Store and version data |
| Improve | Evolve and modernise the technical ecosystem (VS-09.6) | Modernisation roadmap, adopted technologies | No reference process (NSI-specific) |

VS-09 manages enabling artefacts: technical requirements, architecture blueprints, provisioned environments and platforms, integration and orchestration services and event interfaces, monitoring, security, and continuity controls, and the modernisation roadmap. These artefacts underpin every value stream and are managed across their life cycle (SAF-P03), with security (SAF-P10) and continuity (SAF-P06) built in. Each artefact has a designated owner. Changes are tracked, prior versions remain identifiable, and obsolete components are formally retired.

### 5. Actors and roles

Specialised role names used in VS-09 map onto the reference roles (see *Role names in the value streams*). The platform engineer role is anchored in VS-09.

| Actor or role | ID | Process type | Responsibility in VS-09 |
|---|---|---|---|
| Chief technology or infrastructure officer | ACT-01; member of COL-07 | Management | Accountable for the technical foundation and its strategy |
| Supplier and service provider | ACT-09 | External | Cloud and hosting providers and software vendors that deliver platform services under contracts with security, confidentiality, and continuity requirements |
| Process owners of VS-01 to VS-10 | ROL-01 | Management | Define requirements as consuming teams and run their processes on the platforms |
| Data custodian | ROL-04 | Execution | Runs storage, backup, and access control according to the decisions of the data owner |
| Data engineer (integration engineer) | ROL-10 | Implementation | Builds APIs, workflow engines, and orchestration |
| Platform engineer (platform or cloud architect) | ROL-11 | Design | Designs the platform and infrastructure architecture |
| Platform engineer (DevOps or platform engineer) | ROL-11 | Implementation | Provisions, configures, and operates environments |
| Platform engineer (service desk or operations) | ROL-11 | Execution | Runs incident management and keeps services available |
| Security officer (security and continuity officer) | ROL-20 | Management | Implements security controls, monitoring, and disaster recovery, with VS-07 |
| Enterprise architect | ROL-24 | Design, Management | Reviews the platform architecture against the architecture principles in COL-07 Architecture board |

### 6. Capabilities, processes, and functions

#### Capability foundations

| Capability group | Capabilities | Role in VS-09 |
|---|---|---|
| 2.1 Data management | 2.1.1 Data lifecycle management | Store, version, back up, and recover the states |
| 3.2 Computerisation and automation | 3.2.1 Application development, 3.2.2 Functional management, 3.2.3 Technical management, 3.2.5 IT infrastructure | Develop, configure, and manage platforms and integration services |
| 3.3 Security and privacy | 3.3.2 Security planning, 3.3.3 Security incident management, 3.3.4 Logical identity and access control, 3.3.6 IT security services | Build technical security into every platform and respond to incidents |
| 4.1 Strategy and leadership | 4.1.3 Change management, 4.1.7 Architecture Management | Govern the platform architecture and its modernisation |

#### Stages, processes, and functions

| Stage | Realised by processes | Main functions |
|---|---|---|
| VS-09.1 Define Digital and Technical Requirements | PRD-2.6 Design production systems and workflows | FUN-2.5 Manage enterprise architecture; FUN-3.1 Design and build statistical products |
| VS-09.2 Design Platform and Infrastructure Architecture | PRD-2.6 Design production systems and workflows | FUN-2.5 Manage enterprise architecture; FUN-10.3 Manage information technology |
| VS-09.3 Provision and Configure Platforms | PRD-3.4 Configure workflows; MDS-4 Provide a secure processing environment | FUN-8.3 Operate secure research environments; FUN-10.3 Manage information technology |
| VS-09.4 Enable Integration and Orchestration Services | PRD-3.4 Configure workflows; DSP-4 Exchange data under usage control | FUN-9.2 Operate data space connectivity; FUN-10.3 Manage information technology |
| VS-09.5 Ensure Performance, Security and Continuity | PRD-3.5 Test production systems; DLM-5 Store and version data | FUN-10.3 Manage information technology; FUN-10.8 Manage information security and privacy |
| VS-09.6 Evolve and Modernise the Technical Ecosystem | No reference process (NSI-specific) | FUN-2.2 Develop capability improvements; FUN-10.3 Manage information technology |

|**PLACEHOLDER: ArchiMate view VS-09 (b) stages realised by processes and functions**|
|---|

#### Framework mappings

| Cycle step | SAF business processes | GSBPM | GAMSO | SAF capabilities |
|---|---|---|---|---|
| Plan | PRD-2.6 | 2.6 Design production systems and workflow | Capability Management | 4.1.7 Architecture Management, 3.2.2 Functional management |
| Build | PRD-3.4, MDS-4, DSP-4 | 3.4 Configure workflows | Capability Management | 3.2.1 Application development, 3.2.5 IT infrastructure |
| Operate | PRD-3.5, DLM-5 | 3.5 Test production system | Corporate Support (IT services, security, continuity) | 3.2.3 Technical management, 3.3.3 Security incident management, 3.3.6 IT security services |
| Improve | None (NSI-specific) | | Capability Management | 4.1.3 Change management |

### 7. Principles

VS-09 foregrounds SAF-P10, SAF-P06, SAF-P02, and SAF-P05.

| Principle | Statement | Application in VS-09 |
|---|---|---|
| SAF-P10 | Security By Design | Security and access control are built into every platform and environment from the start. |
| SAF-P06 | Business Continuity | VS-09 guarantees availability, resilience, and disaster recovery for the whole chain. |
| SAF-P02 | Active support | Platforms are run as actively supported, monitored services, not one-off builds. |
| SAF-P05 | IT and technology is everyone's business | Platforms are self-service and well documented, so that technology serves all teams. |
| SAF-P01 | Actively participate in open-source communities to maintain collective control over statistical processes | Open, shared platform components are preferred, so that the NSI keeps collective control. |
| SAF-P03 | Active Life Cycle management | Enabling artefacts have an owner and a version history; obsolete components are formally retired. |

### 8. Interfaces, services, and events

**Business services**

| Service | Offered to | Realised in | Interfaces |
|---|---|---|---|
| Platform and environment provisioning service | All value streams VS-01 to VS-10 | VS-09.3 Provision and Configure Platforms | Platform or service request |
| Integration and orchestration service | All primary value streams | VS-09.4 Enable Integration and Orchestration Services | APIs, workflow engines, steady-state event interfaces, data space connectors |
| Dissemination platform service | VS-06 Dissemination and Service Delivery | VS-09.3 Provision and Configure Platforms | Portals, APIs, dashboards, secure research environments |
| Research and innovation runtime service | VS-08 Innovation and Methodological Development | VS-09.3 Provision and Configure Platforms | Sandbox and production runtime for new technology |
| Platform operations and continuity service | All value streams | VS-09.5 Ensure Performance, Security and Continuity | Service desk, incident management, monitoring |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Platform or service request* | A consuming value stream asks for an environment or service; input to VS-09.1 |
| *Capacity change* | A change in capacity demand; review of capacity in VS-09.1 and VS-09.5 |
| *Incident* | Start of incident management in VS-09.5 |
| *Dissemination platform request* | VS-06 asks for a new or scaled channel |
| *Technology onboarding* | VS-08 asks to adopt a new technology; input to VS-09.1 and VS-09.6 |
| *Security or continuity review* | Periodic or triggered review of the security and continuity posture with VS-07 |

**Interaction with the primary value streams**

VS-09 interacts with all primary value streams at once (see attribute 2). The interaction runs through *Platform or service request*, *Incident*, and *Capacity change*; VS-06 also uses *Dissemination platform request*.

**Interaction with the supporting value streams**

| Value stream | Provides to VS-09 | Receives from VS-09 | Event |
|---|---|---|---|
| VS-07 Governance and Compliance | Security and continuity policy to enforce | Security posture, continuity and incident evidence | *Security or continuity review* |
| VS-08 Innovation and Methodological Development | New-technology adoption requests; requirements for sandbox and production platforms | Sandbox and production runtime for new technology | *Technology onboarding*; *Platform or service request* |

### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| Platform availability | Measured availability against the agreed service level, per platform | Monthly |
| Incident response | Mean time to restore service after an incident, per severity class | Per incident, trended quarterly |
| Event-interface reliability | Delivery rate of the steady-state handover events the chain depends on | Per interface, monthly |
| Capacity headroom | Share of platforms operating within their planned capacity envelope | Monthly, ahead of known peaks |
| Security posture | Open critical vulnerabilities and patch latency, assessed with VS-07 | Continuous, reported quarterly |
| Modernisation progress | Components retired or replaced according to the roadmap | Annually |

### 10. Examples

|**PLACEHOLDER: VS-09 examples to be added, for example provisioning a secure research environment, an outage of the event interface and its recovery, and the transfer of a new technology from VS-08 into production**|
|---|

| **Toolkit:** SAF-TK-V09 VS-09 maturity checklist and scenarios |
|---|



## VS-10 Customer and Stakeholder Engagement

### 1. Purpose and value created

VS-10 keeps the NSI connected, relevant, and responsive to the needs of those it serves. It builds and maintains mutual understanding and trust between the NSI and its users, data providers, partners, and policymakers. Official statistics exist to create public value. To create it, the NSI must understand what stakeholders need, communicate transparently, and keep its products, services, and policies aligned with real-world demand. VS-10 is the voice and the mirror of the NSI: it connects external expectations with internal capabilities and closes the feedback loop across the chain. The value created is **relevance and public value**: the work of the NSI is understood, used, and appreciated by its users, partners, and society, so that the NSI does not just produce data but produces public value.

VS-10 is not a one-way process. It is a continuous two-way dialogue that turns stakeholder insight into better products, improved services, and stronger relationships. It does not move data along the chain; it moves understanding: needs come in, communication and services go out. Producing, approving, and releasing statistical data is outside its scope.

VS-10 corresponds to the horizontal business domain **Engagement**. Its output is an enabling capability, not a data artefact: understood needs, a managed service portfolio, relationships, and impact insight.

|**PLACEHOLDER: ArchiMate view VS-10 (a) value stream and capabilities**|
|---|

<br>

### 2. Relation to the value chain

VS-10 is not a stage in the production line. It sits at the edges of the chain. On one side it faces the data providers and respondents who feed VS-01; on the other, the users who consume the output of VS-06. It channels what it learns inward to shape the whole chain. It has no state transition and no quality gate. It is a secondary consumer of Released Data (State #5): it uses usage and feedback data for needs analysis and impact measurement (see *State #5: Released Data*). What the NSI learns about consumed data (#6) comes back through VS-06.5 and VS-10.

| Primary value stream(s) | Provides | Receives |
|---|---|---|
| VS-01 Data Acquisition and Ingestion | Relationship management and transparency toward data providers; insight into which data sources and topics matter most to users | Provider needs, feedback, and issues; willingness to provide data |
| VS-05 Statistical Product Composition, VS-06 Dissemination and Service Delivery | Service requirements and user expectations; the outputs and formats users prefer | Usage and satisfaction data (VS-06.5 Monitor Usage and Feedback) |
| Design across VS-01 to VS-06 | User needs and service requirements | New and improved products and services |

VS-10 aligns to GAMSO rather than to GSBPM production phases.

| GAMSO area | Relevance to VS-10 |
|---|---|
| Strategy and Leadership | Manage stakeholder and customer relationships; align the service portfolio to the strategy |
| Corporate Support | Manage communications, marketing, user support, and service management |

|**PLACEHOLDER: ArchiMate view VS-10 (c) interactions with the value chain: data providers and respondents engaged two-way at the entry of VS-01, users and society engaged two-way after VS-06, usage and feedback from VS-06.5 into VS-10, and user needs routed into design across VS-01 to VS-06 and into the VS-08 innovation backlog**|
|---|

<br>

### 3. Stages

The six stages form a continuous engagement cycle: understand (VS-10.1, VS-10.2), offer (VS-10.3), deliver (VS-10.4, VS-10.5), and measure (VS-10.6). The insight from VS-10.6 feeds the next cycle, so that the next round of needs is better understood.

| Stage | Name | Value added |
|---|---|---|
| VS-10.1 | Identify and Segment Stakeholders | The NSI knows its users, providers and partners |
| VS-10.2 | Collect and Analyse User Needs | Needs are translated into requirements |
| VS-10.3 | Define and Manage Service Portfolios | Services and products match the needs |
| VS-10.4 | Deliver Services and Manage Relationships | Users and partners are served |
| VS-10.5 | Engage and Communicate with Stakeholders | Stakeholders understand the output |
| VS-10.6 | Monitor Impact and Satisfaction | The NSI knows its impact and acts on it |

Each stage below is described with its activities. The column *SAF process* shows the business process from *Business Processes* that the activity belongs to. The column *Other reference* shows the principles, capabilities, or external frameworks that the activity applies.

<br>

#### VS-10.1 Identify and Segment Stakeholders

**Value created:** *The NSI knows who its users, data providers, and partners are, and what they expect.*

The cycle begins by mapping the ecosystem of stakeholders: users, data providers, partners, and policymakers. For each group, the team describes its role and its expectations of the NSI. Users are grouped into segments, because their needs differ widely, so that services and channels can be designed per segment. Partners include other producers of official statistics, international statistical organisations, and the participants of the data spaces in which the NSI takes part.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Map the stakeholder ecosystem: users, data providers, partners, policymakers | Stakeholder map | PRD-1.2 Consult and confirm needs | 3.4.2 Contact management |
| Understand the roles and expectations of each stakeholder group | Stakeholder map | PRD-1.2 Consult and confirm needs | |
| Segment users by need and use | User segments | PRD-1.2 Consult and confirm needs | GAMSO Manage Consumers |
| Identify partners in the statistical system and in data spaces | Partner overview | DSP-6 Participate in data space governance | 4.1.6 Collaboration; COL-02, COL-03 |

<br>

#### VS-10.2 Collect and Analyse User Needs

**Value created:** *Stakeholder needs are understood and translated into concrete data or service requirements.*

VS-10 gathers feedback and runs consultations with the segments identified in VS-10.1. It analyses what it hears and records the needs in a needs register. Each need is translated into a concrete data or service requirement. Requirements are routed to the design of the primary value streams that can meet them. A need that calls for a new method, source, or tool goes to the innovation backlog of VS-08. VS-10 also tells VS-01 which data sources and topics matter most to users.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Gather feedback and run consultations | Consultation results | PRD-1.2 Consult and confirm needs | 2.2.5 User research |
| Analyse needs and record them in the needs register | User-needs register | PRD-1.1 Identify needs | 1.1.1 Needs inventory |
| Translate needs into data or service requirements | Service requirements | PRD-1.1 Identify needs | 1.1.1 Needs inventory |
| Route requirements to design across VS-01 to VS-06, and user-driven innovation needs to VS-08 | *Need routed to design/innovation* | PRD-1.1 Identify needs | VS-08.1 Identify Innovation Needs and Opportunities |

<br>

#### VS-10.3 Define and Manage Service Portfolios

**Value created:** *A portfolio of services and products that addresses stakeholder needs and serves the strategy.*

The needs shape the portfolio: the catalogue of business services and data products that address stakeholder needs and align with the strategic goals of the NSI. The portfolio is the bridge between what users want and what the chain produces. It shows which outputs and formats users prefer, which guides VS-05 and VS-06. Each service has a service standard against which its performance is measured in VS-10.4.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Define the catalogue of services and data products per segment | Service and product portfolio | PRD-2.1 Design outputs and dissemination | 3.4.1 Services management |
| Align the portfolio with the strategic goals | Service and product portfolio | PRD-2.1 Design outputs and dissemination | 4.1.2 Policy and planning; GAMSO Strategy and Leadership |
| Set the service standard for each service | Service standards | PRD-2.1 Design outputs and dissemination | 3.4.3 Service agreement |
| Specify the outputs and formats users prefer, for VS-05 and VS-06 | Service requirements | PRD-2.1 Design outputs and dissemination | |

<br>

#### VS-10.4 Deliver Services and Manage Relationships

**Value created:** *Users and partners are served, and relationships are actively maintained.*

Services reach users through customer support, service desks, and account management. Key data providers, partners, and policy users have an account or relationship manager, so that the NSI speaks with one voice to each of them. With data providers, VS-10 is transparent about how their data is used and protected, and it passes provider needs and issues to VS-01. Researchers who use microdata services get support with content, metadata, and the rules of use. Satisfaction and service performance are monitored against the service standard.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Operate the service desk and user support | Support records | PRD-7.5 Provide user support | 3.4.4 Self-service |
| Manage relationships with key users, partners, and policy users | Relationship records | PRD-7.5 Provide user support | 3.4.2 Contact management |
| Manage relationships with data providers, with transparency on data use and protection | Relationship records, provider needs | OVA-6 Data Supplier Management | COL-01; SAF-P11 |
| Support researchers in the use of microdata services | Researcher support records | MDS-6 Support researchers | COL-04 |
| Monitor service performance and satisfaction against the service standard | Service performance report | PRD-7.5 Provide user support | 3.4.3 Service agreement |

<br>

#### VS-10.5 Engage and Communicate with Stakeholders

**Value created:** *Stakeholders are aware of the statistics and understand them correctly.*

Alongside delivery, VS-10 engages with stakeholders through outreach, workshops, and knowledge-sharing events. The aim is awareness and correct understanding of statistical outputs. Transparent communication about data ethics, confidentiality, and quality also builds trust and strengthens VS-07.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Run outreach to user segments | Outreach campaigns | PRD-7.4 Promote dissemination products | 1.5.2 Promotion to use |
| Hold workshops and knowledge-sharing events | Events, participation records | PRD-7.4 Promote dissemination products | 3.1.4 Communication management |
| Communicate transparently about data ethics, confidentiality, and quality | Public communication | PRD-7.4 Promote dissemination products | 4.1.5 Accountability; SAF-P11 |

<br>

#### VS-10.6 Monitor Impact and Satisfaction

**Value created:** *The NSI knows how its data and services are used and what impact they have, and acts on it.*

VS-10 measures how data and services are used and assesses their societal impact. It receives usage and satisfaction data from VS-06.5 and runs its own satisfaction surveys. It documents uses of official statistics in policy, research, and media. The insight goes back into planning and innovation, which closes the loop: the next cycle of needs starts from it.

| Activity | Key outputs | SAF process | Other reference |
|---|---|---|---|
| Collect usage and satisfaction data from VS-06.5 | Usage insight | PRD-8.1 Gather evaluation inputs | |
| Measure satisfaction across user segments and services | Satisfaction scores | PRD-8.1 Gather evaluation inputs | |
| Document uses of official statistics in policy, research, and media | Impact evidence | PRD-8.2 Conduct evaluation | 4.1.5 Accountability |
| Assess societal impact and feed the insight into planning (VS-10.1, VS-10.2) and innovation (VS-08) | Impact and satisfaction insight | PRD-8.2 Conduct evaluation | 4.1.4 Improvement management |

### 4. Plan, build, operate, and improve

VS-10 is itself a capability that is planned, built, operated, and improved. Unlike a primary value stream, it produces relevance, relationships, and insight, not statistical data, and it runs as a continuous dialogue rather than a production run per cycle.

| Cycle step | What happens in VS-10 | Main outputs | SAF process |
|---|---|---|---|
| Plan | Design the engagement strategy and the portfolio model | Engagement strategy, portfolio model | PRD-1.2 Consult and confirm needs; PRD-2.1 Design outputs and dissemination |
| Build | Build support and feedback channels, with VS-09 | Service desk, consultation, and feedback channels | PRD-3.3 Reuse or build dissemination components |
| Operate | Run the continuous dialogue, user support, and communication (VS-10.1 to VS-10.5) | Needs register, managed relationships, communication | PRD-7.4 Promote dissemination products; PRD-7.5 Provide user support |
| Improve | Use the insight of VS-10.6 to improve engagement and the portfolio; retire services that no longer meet a need | Impact and satisfaction insight, portfolio changes | PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan |

#### Business objects

VS-10 manages enabling artefacts that carry user insight into the rest of the chain. They are maintained continuously rather than versioned per production cycle. Each artefact nevertheless has a designated owner and a managed life cycle (SAF-P03): changes are tracked and outdated entries are retired.

| Business object | Produced in |
|---|---|
| Stakeholder map and segments | VS-10.1 |
| User-needs register and service requirements | VS-10.2 |
| Service and product portfolio | VS-10.3 |
| Relationship and support records | VS-10.4 |
| Impact and satisfaction metrics | VS-10.6 |

### 5. Actors and roles

The roles below are indicative, not a mandated organisational structure. The SAF leaves organisation design to each NSI, which assigns these responsibilities to fit its own size, culture, and operating model. The specialised role names used in VS-10 map onto reference roles (see *Role names in the value streams*).

| Actor or role | ID | Process type | Responsibility in VS-10 |
|---|---|---|---|
| Data user | ACT-05 | External | Policy makers, researchers, media, businesses, and the public; express needs, give feedback, use services |
| Data provider | ACT-03 | External | Engaged on its needs and on how its data is used and protected |
| Respondent | ACT-04 | External | Engaged on burden and on why the NSI needs the data |
| Other producer of official statistics | ACT-06 | External | Partner in the national statistical system (COL-02) |
| International statistical organisation | ACT-07 | External | User and partner in international cooperation (COL-03) |
| Process owner | ROL-01 | Management | Accountable for the end-to-end performance of VS-10 |
| Head of Communication / Engagement | ROL-23 Relationship manager | Plan | Owns the stakeholder strategy and the external relationship |
| User Researcher | ROL-23 Relationship manager | Operate | Collects and analyses user needs and satisfaction |
| Account / Relationship Manager | ROL-23 Relationship manager | Operate | Manages relationships with key providers, partners, and policy users |
| Communications / Outreach Officer | ROL-23 Relationship manager | Operate | Runs outreach, workshops, and knowledge-sharing events |
| Impact Analyst | ROL-23 Relationship manager | Improve | Measures use, societal impact, and satisfaction |
| Service / Product Portfolio Manager | ROL-22 Dissemination and service manager | Plan | Defines and manages the catalogue of services and data products |
| Service Desk / User Support | ROL-22 Dissemination and service manager | Operate | Operates day-to-day user support |
| Statistical designer | ROL-06 | Design (primary streams) | Receives the requirements routed from VS-10.2 into the design of products |

### 6. Capabilities, processes, and functions

#### Capability foundations

| Capability group | Capabilities | Role in VS-10 |
|---|---|---|
| 1.1 Statistical design and build | 1.1.1 Needs inventory | Identify the demand for statistical information through relationships with users and stakeholders |
| 1.5 Dissemination | 1.5.2 Promotion to use | Promote statistical output to users |
| 2.2 Research | 2.2.5 User research | Collect and assess user needs and translate them into statistical output |
| 3.1 Business operations | 3.1.4 Communication management | Communicate with internal and external parties |
| 3.4 Customer and chain interaction | 3.4.1 Services management, 3.4.2 Contact management, 3.4.3 Service agreement, 3.4.4 Self-service | Manage the service portfolio, relationships, service standards, and self-service |
| 4.1 Strategy and leadership | 4.1.4 Improvement management, 4.1.5 Accountability, 4.1.6 Collaboration | Feed insight into improvement, report on impact, maintain strategic relationships |

#### Stages, processes, and functions

| Stage | Realised by processes | Main functions |
|---|---|---|
| VS-10.1 Identify and Segment Stakeholders | PRD-1.2 Consult and confirm needs; DSP-6 Participate in data space governance | FUN-1.3 Manage strategic collaboration; FUN-10.9 Manage users and services |
| VS-10.2 Collect and Analyse User Needs | PRD-1.1 Identify needs; PRD-1.2 Consult and confirm needs | FUN-3.1 Design and build statistical products; FUN-10.9 Manage users and services |
| VS-10.3 Define and Manage Service Portfolios | PRD-2.1 Design outputs and dissemination | FUN-10.9 Manage users and services |
| VS-10.4 Deliver Services and Manage Relationships | PRD-7.5 Provide user support; MDS-6 Support researchers; OVA-6 Data Supplier Management | FUN-6.1 Manage data supplier relationships; FUN-10.9 Manage users and services |
| VS-10.5 Engage and Communicate with Stakeholders | PRD-7.4 Promote dissemination products | FUN-1.4 Build public confidence; FUN-10.6 Manage communication |
| VS-10.6 Monitor Impact and Satisfaction | PRD-8.1 Gather evaluation inputs; PRD-8.2 Conduct evaluation | FUN-5.2 Assure and review quality; FUN-10.9 Manage users and services |

|**PLACEHOLDER: ArchiMate view VS-10 (b) stages realised by processes and functions**|
|---|

#### Framework mappings

| Cycle step | SAF business processes | GSBPM | GAMSO | SAF capabilities |
|---|---|---|---|---|
| Plan | PRD-1.1, PRD-1.2, PRD-2.1 | 1.1, 1.2, 2.1 | Strategy and Leadership | 1.1.1 Needs inventory, 3.4.1 Services management |
| Build | PRD-3.3 | 3.3 | Capability Management | 3.4.4 Self-service |
| Operate | PRD-7.4, PRD-7.5, MDS-6, OVA-6, DSP-6 | 7.4, 7.5 | Corporate Support (Manage Consumers, communication) | 1.5.2 Promotion to use, 3.1.4 Communication management, 3.4.2 Contact management, 4.1.6 Collaboration |
| Improve | PRD-8.1, PRD-8.2, PRD-8.3 | 8.1 to 8.3 | Strategy and Leadership; Capability Management | 2.2.5 User research, 4.1.4 Improvement management, 4.1.5 Accountability |

### 7. Principles

VS-10 foregrounds SAF-P04, SAF-P08, and SAF-P02. It also applies SAF-P11 in its dialogue with providers and users.

| Principle | Statement | Application in VS-10 |
|---|---|---|
| SAF-P04 | Maximise the benefits for the organisation | Keeps the whole chain aligned to real stakeholder value and public benefit |
| SAF-P08 | Data is shared property | Promotes broad, equitable access to and reuse of statistics and services |
| SAF-P02 | Active support | Runs user support and service management as actively managed services |
| SAF-P11 | Privacy By Design | Engages data providers and users with transparency about how their data is used and protected |

### 8. Interfaces, services, and events

**Business services**

| Service | Offered to | Realised in | Interfaces |
|---|---|---|---|
| Needs analysis service | Design across VS-01 to VS-06, VS-08 | VS-10.2 Collect and Analyse User Needs | Consultations, user-needs register, service requirements |
| Service and product portfolio | Users, primary value streams | VS-10.3 Define and Manage Service Portfolios | Service catalogue, service standards |
| User support service | Users, researchers | VS-10.4 Deliver Services and Manage Relationships | Service desk, self-service, account management |
| Provider relationship service | Data providers (via VS-01) | VS-10.4 Deliver Services and Manage Relationships | Relationship manager |
| Communication and outreach service | Users and society | VS-10.5 Engage and Communicate with Stakeholders | Outreach campaigns, workshops, knowledge-sharing events |
| Impact and satisfaction insight | Process owners, planning, VS-08 | VS-10.6 Monitor Impact and Satisfaction | Satisfaction and impact reports |

**Business events**

| Event | Counterpart | Triggers or marks |
|---|---|---|
| *User need captured* | Users and society | Entry of a need in the needs register (VS-10.2) |
| *Consultation* | Users and society | A structured gathering of needs and feedback (VS-10.2) |
| *Service request* | Users and society | Start of user support (VS-10.4) |
| *Provider engagement* | Data providers (via VS-01) | Contact on provider needs, burden, or data use (VS-10.4) |
| *Feedback received* | VS-06 Dissemination and Service Delivery | Arrival of usage and satisfaction data from VS-06.5 (VS-10.6) |
| *Need routed to design/innovation* | Design across VS-01 to VS-06, VS-08 | Handover of a requirement to design or to the innovation backlog (VS-10.2) |

**Interaction with the primary value streams**

| Value stream | Interaction | Event |
|---|---|---|
| VS-01 Data Acquisition and Ingestion | VS-10 manages the relationship with data providers and passes their needs and issues; VS-01 reports provider feedback and rejected deliveries | *Provider engagement* |
| VS-05 Statistical Product Composition | VS-10 passes the outputs and formats users prefer | *Need routed to design/innovation* |
| VS-06 Dissemination and Service Delivery | VS-10 passes service requirements and user expectations; VS-06.5 sends usage and satisfaction data | *Feedback received* |
| Design across VS-01 to VS-06 | VS-10 routes user needs and service requirements; it receives new and improved products and services | *Need routed to design/innovation* |

**Interaction with the other supporting value streams**

| Value stream | Provides to VS-10 | Receives from VS-10 |
|---|---|---|
| VS-07 Governance and Compliance | Policies on data ethics, confidentiality, and quality | Transparent communication about data ethics, confidentiality, and quality; impact evidence for accountability |
| VS-08 Innovation and Methodological Development | New and improved products and services | User-driven innovation needs, ideas and feedback from users and partners |
| VS-09 Infrastructure and Platform Enablement | Support and feedback channels | Requirements for channels and portals |

### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| User satisfaction | Satisfaction score across user segments and services | Per survey wave, per segment |
| Needs conversion | Share of captured needs converted into requirements routed to design or innovation | Per planning period |
| Service performance | Support response and resolution times against the service standard | Monthly |
| Reach and engagement | Participation in consultations and outreach; channel reach across segments | Per campaign, annually |
| Impact evidence | Documented uses of official statistics in policy, research, and media | Annually |

### 10. Examples

|**PLACEHOLDER: VS-10 examples to be added, for example a user consultation that leads to a new product, a provider engagement that reduces burden, and an impact report built from VS-06.5 usage data**|
|---|

| **Toolkit:** SAF-TK-V10 VS-10 maturity checklist and scenarios |
|---|
