SAF Architecture Framework
============================

Created on: 07-07-2025
Workgroup SAF: Trygve Falch (Statistics Norway, SSB), Jakob Engdahl (Statistics Sweden, SCB), Cedric Couralet (Statistics France, Insee), Pascal Fransen (Statistics Netherlands, CBS) and Daan Swinkels (Statistics Netherlands, CBS)

Current version: 0.5

| Version | Date | Contributor/Secretary |
|---|---|---|
|0.1|2025-07-07|Initial version|
|0.2|2026-06-01|Review processed|
|0.3|2026-07-31|Restructuring, Start with Business Architecture|
|0.4|2026-09-01|Merging Business Architecture content|
|0.5|2026-10-10|Restructured motivation section, TOGAF and ArchiMate context added|
|0.6|2026-11-10|Restructured strategy section|
|0.7|2026-12-10|Restructured business section, added business actors, roles and collaborations|
|0.8|2026-31-10|Concolidated and structured Steady State detail content|

## Content
[Preface](#preface)

-   [Acknowledgements](#acknowledgements)

[Introduction](#introduction)

-   [Purpose](#purpose)
-   [Definition of Scope](#definition-of-scope)
-   [Target Audience](#target-audience)
-   [Expected value](#expected-value)
-   [Constraints & Assumptions](#constraints-assumptions)
    -   [Use of TOGAF and ArchiMate in SAF](#use-of-togaf-and-archimate-in-saf)
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
-   [Assessment](#assessment)
-   [Requirements](#requirements)
-   [Constraints](#constraints)
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
    -   [A. Statistical production processes](#a.-statistical-production-processes)
    -   [B. Overarching processes](#b.-overarching-processes)
    -   [C. Data management and lifecycle processes](#c.-data-management-and-lifecycle-processes)
    -   [D. Microdata services processes](#d.-microdata-services-processes)
    -   [E. Data space processes](#e.-data-space-processes)
-   [Business Functions](#business-functions)
    -   [Process and function mapping](#process-and-function-mapping)
    -   [Mapping to value stream stages](#mapping-to-value-stream-stages)
-   [Business Services and Business Interfaces](#business-services-and-business-interfaces)
-   [Business Events](#business-events)
-   [Business Objects, Contracts, Representations and Products](#business-objects-contracts-representations-and-products)
-   [Reference Models for the Statistical Data Value Chain](#reference-models-for-the-statistical-data-value-chain)
    -   [Comparison](#comparison)
    -   [Selection criteria](#selection-criteria)
    -   [Combining the models](#combining-the-models)

[Steady-State Architecture](#steady-state-architecture)

-   [Overview](#overview)
    -   [Business domains](#business-domains)
    -   [The four process types](#the-four-process-types)
    -   [Design rules of the steady-state model](#design-rules-of-the-steady-state-model)
    -   [Steady states at a glance](#steady-states-at-a-glance)
    -   [State lifecycle](#state-lifecycle)
    -   [How each state is described](#how-each-state-is-described)
-   [Boundary Position #0: Source Data](#boundary-position-0-source-data)
-   [State #1: Raw Data](#state-1-raw-data)
-   [State #2: Standardized Data](#state-2-standardized-data)
-   [State #3: Processed Data](#state-3-processed-data)
-   [State #4: Output Data (Statistics)](#state-4-output-data-statistics)
-   [State #5: Published Output Data (Released Data)](#state-5-published-output-data-released-data)
-   [State #6: Consumed Data](#state-6-consumed-data)




# Preface

The Statistical Architecture Framework (SAF) was developed to support the modernisation of official statistics. This framework responds to the need of national statistical institutes and their partners for shared guidelines and standards. Producing statistics must remain credible, secure, and efficient. At the same time, organisations must adapt quickly to new data sources, higher user expectations, and tighter regulations and budgets. The SAF provides a solid foundation for this and help organisations guide these changes in a controlled and structured way.

This new framework replaces the older CSPA and CSDA standards, but it reuses the elements that are still current and valuable. The SAF combines the core ideas from these previous framework into a single, logical, and coherent model. While the framework continues to focus on cooperation, reuse, and standards, the focus has shifted heavily toward a practical application of the framework in an organization. It is specifically designed to be used directly within ongoing programmes and projects. This helps teams make concrete choices when designing and implementing new processes and solutions.

The fundamental principle of the framework is that data and its descriptions are the most important assets of a statistical organisation. Information is not just a tool to run processes, but the core of the organisation. The SAF therefore treats this information as an NSIs most valuable asset that must be professionally managed throughout its entire lifecycle. It must support systems that can work with both traditional and modern, new data sources and information flows. In addition, it offers a practical guide for collecting, combining, and publishing data.

The SAF builds on a modular approach where systems are constructed from loose, flexible components. It promotes the reuse of these digital building blocks, both within an organisation and between different organisations. This prevents projects from independently building the same tools, which reduces duplication and lowers costs. Furthermore, it ensures a clear separation between business methods, data, and the underlying technology. This separation is essential for keeping complex IT landscapes manageable and successfully scaling them up. The framework is designed to be used at multiple levels at the same time. It helps with strategic planning, designing specific IT solutions, and monitoring how different projects align with one another. 

The SAF does not replace existing statistical models, but rather works closely alongside them. It forms the connecting link between organisational strategy, business processes, and technology. This connection helps organisations make consistent decisions and makes sure that organization policy is translated into practice. To improve communication between teams, the SAF uses different visual models. By using a standard notation style, organisations can easily compare and reuse each other's designs. Finally, the SAF is a living framework that will continuously evolve based on practical experience, community feedback, and new technological developments.

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

The structures of the two standards correspond. The TOGAF Preliminary Phase, Phase A, and Requirements Management correspond to the ArchiMate motivation and strategy elements. TOGAF Phases B, C, and D correspond to the ArchiMate business, application, and technology layers. TOGAF Phases E to H correspond to the ArchiMate implementation and migration elements. This correspondence is the basis for the position of each SAF chapter (see *Position in the framework* in the Motivation chapter).

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

1. **Adopt, adapt or extend.** For each SAF element, the NSI decides whether to adopt it as it is, adapt it to the national context, or add NSI-specific elements (see *How NSIs use this chapter* in the Motivation chapter).
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

|**PLACEHOLDER: Mapping templates for SAF and national reference models to be added to the toolkit**|
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

|**PLACEHOLDER: Legal register template to be added to the toolkit**|
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
| PLACEHOLDER | Content that will be added, such as an ArchiMate view or a toolkit reference |
| Toolkit | The SAF toolkit, a separate set of templates and instruments for applying the framework |

Terms are defined in the SAF glossary, which takes precedence over definitions in this document (SAF-A4). The SAF uses British English spelling.

# Motivation

## Purpose of this chapter

The Motivation chapter explains why the SAF exists. It also explains why architecture decisions in an NSI are taken the way they are. It records the forces that act on statistical organisations, the results they want to achieve, the rules that guide their decisions, and the parties whose concerns must be addressed.

Without an explicit motivation, architecture is a set of models without a reason. With it, every capability, process, data state, application or platform choice can be traced back to a need and a result. That traceability makes architecture defensible, whether in a governance board, a budget discussion or an international review.

## Position in the framework

Motivation is the first layer of the SAF and the foundation for the other layers. The Strategy layer translates motivation into capabilities and value streams. The architecture domains (business, data, application and technology) then translate strategy into design.

The SAF is structured according to TOGAF and modelled in ArchiMate. The figure below shows how the phases of the TOGAF Architecture Development Method (ADM) relate to the ArchiMate layers. The figure has three areas:

- **Strategy & Motivation:** the Preliminary Phase, Phase A (Architecture Vision), and Requirements Management.
- **Core layers:** Phases B, C, and D, which produce the Business, Application (Information Systems), and Technology architectures.
- **Implementation & Migration:** Phases E to H, which plan, govern, and change the realisation of the architecture.

|**PLACEHOLDER: Logical model of the different layers to be added**|
|---|

The Motivation layer sits in the Strategy & Motivation area, at the start of the ADM cycle. It holds the content that TOGAF produces before any architecture domain is designed. That content keeps steering the architecture in all later phases.

| ADM phase | Role of motivation in this phase | SAF sections |
|---|---|---|
| Preliminary | Establish the architecture capability: who the architecture serves and which rules guide decisions | Stakeholders, Architecture Principles |
| A. Architecture Vision | Explain why change is needed, what must be achieved and what value it brings | Drivers, Goals, Outcomes, Meaning, Value |
| Requirements Management | Turn goals into requirements and constraints, and keep them traceable through every phase | Requirements, Constraints |
| B, C, D. Core architectures | Justify design choices in business, application and technology architecture | Traceability from each design decision back to a goal and a driver |
| E to H. Implementation & Migration | Prioritise solutions and work packages; reassess when drivers change | Drivers and goals as criteria for prioritisation and change requests |

Three consequences follow from this position.

- **Motivation comes first.** In TOGAF, no architecture domain is designed until stakeholders, drivers, goals and principles are agreed. The SAF follows the same order. Every later element must be traceable to the motivation.
- **Motivation stays active throughout the cycle.** Requirements Management sits at the centre of the ADM. Goals are refined into requirements there, and those requirements are checked in every phase. Motivation is the reference against which each architecture decision is tested, not a one-off introduction.
- **Motivation closes the loop.** In Phase H (Architecture Change Management), a new or changed driver triggers a change request. Examples are a new regulation or a new data source. The cycle then returns to the Preliminary Phase or Phase A, and the motivation elements become the starting point of the next iteration.

The Strategy layer shares the Strategy & Motivation area with the Motivation layer. Motivation explains *why*. Strategy describes *what* the NSI must be able to do (capabilities) and *how* it creates value (value streams). Strategy is the bridge to Phase B, Business Architecture.

## How NSIs use this chapter

The motivation elements in this chapter are a reference set. They describe internal and external forces and intentions that most NSIs share. Modelling the motivation layer is not mandatory, but the SAF strongly recommends it.

Most NSIs have a motivation, but it is implicit. It lives in strategy documents, board decisions and the experience of staff. It is rarely written down in a way that connects it to architecture decisions. Making it explicit, in SAF terms, helps an NSI in four ways.

First, it justifies investment. If every programme can be traced to a driver and a goal, an investment proposal rests on shared reasoning, not on individual preference. Boards and ministries can see what a proposal responds to, and what is at stake if it is not funded. The same links help to set priorities. Work that addresses several drivers, or contributes to a key outcome, comes before work that addresses none.

Second, it makes decisions consistent. Principles are derived from the motivation and turn intentions into decision rules. Similar questions then get similar answers, whichever team or architect is involved. When circumstances change, for example through new legislation, the documented links show which goals, principles and capabilities are affected. The NSI can review those specific decisions instead of starting over.

Third, it preserves knowledge. Staff move on and projects end. A documented motivation keeps the reasoning behind past decisions available. New statisticians and IT specialists can see why the architecture looks the way it does.

Fourth, it supports collaboration between NSIs. When NSIs use the same concepts and identifiers, they can quickly see where their interests overlap. That makes it easier to start joint projects, share components and compare approaches. A documented motivation is also useful evidence in external assessments, such as peer reviews.

An NSI can use each SAF motivation element in one of three ways:
1. **Adopt.** Use an SAF element as is, when it matches the national situation.
2. **Adapt.** Refine an SAF element with national specifics, such as a national statistics act or a government-wide digital strategy.
3. **Extend.** Add elements that are specific to the NSI, while keeping a reference to the closest SAF element where one exists.


|**PLACEHOLDER: Maturity Assessement to be added to the toolkit**|
|---|

## Motivation concepts in the SAF

| SAF section | ArchiMate element | Question it answers | Identifier |
|---|---|---|---|
| Drivers | Driver | Which forces make change necessary? | SAF-D |
| Goals | Goal | What does the NSI intend to achieve? | SAF-G |
| Meaning | Meaning | What does the framework signify to its users? | SAF-M |
| Outcomes | Outcome | Which concrete results show that a goal is achieved? | SAF-O |
| Architecture Principles | Principle | Which rules guide architecture decisions? | SAF-P |
| Value | Value | What is the framework worth, and to whom? | SAF-V |
| Assessment | Assessment | What does a driver mean for this NSI? | *TBD by NSI* |
| Requirements | Requirement | What must a solution do or provide to realise a goal? | *TBD by NSI* |
| Constraints | Constraint | Which limits apply to the design or its realisation? | *TBD by NSI* |
| Stakeholders | Stakeholder | Whose concerns must the architecture address? | SAF-ST |

The concepts form a chain. Stakeholders have concerns about drivers. An assessment records what a driver means for one NSI. Drivers motivate goals. Outcomes make goals measurable. Principles guide how goals are pursued, and requirements and constraints make them concrete for a solution. Meaning and value express why the result matters to stakeholders.

## Drivers

### The concept

A **driver** is an external or internal condition that motivates an organisation to set goals and to change. A driver is a force, not a problem and not a solution. "Rapid technological change" is a driver. "Our methods cannot use administrative data" is an assessment of that driver for one NSI. "Integrate new data sources into production" is a goal.

Three characteristics set drivers apart from other motivation elements:

- **They exist independently of the NSI.** An NSI can respond to a driver, but cannot decide whether it exists.
- **They are external or internal.** External drivers come from the environment: technology, legislation, society, politics or the economy. Internal drivers come from within: legacy systems, skills or organisational structure.
- **They are relatively stable.** A driver usually stays relevant for several years. Short-lived events, such as an incident or a budget round, are better recorded as assessments.

### How the SAF applies drivers

**Why the SAF records drivers**

Drivers make the SAF a response to real pressures instead of an abstract ideal. With them, an NSI can explain to its board, its ministry or a peer review why change is needed, and what happens without it. Drivers also help to set priorities. An investment that responds to several drivers deserves more attention than one that responds to none.

**How drivers fit into an NSI's own architecture**

The SAF drivers are common to the UNECE statistical community. An NSI applies them in four steps:

1. **Recognise.** Decide which SAF drivers apply to the national situation, and add national drivers where needed.
2. **Assess.** Analyse what each driver means for the NSI: strengths, weaknesses, risks and opportunities.
3. **Respond.** Derive or confirm the goals that answer the assessed drivers.
4. **Trace.** Link capabilities, programmes and architecture decisions to the drivers they address.

**Relationships with other concepts**

| Related concept | Relationship | Example in the SAF |
|---|---|---|
| Stakeholders (SAF-ST) | Stakeholders have concerns about drivers and often raise them | CIOs and CTOs (SAF-ST01) raise resource constraints (SAF-D5) |
| Assessment | An assessment records what a driver means for one NSI | "Two thirds of our processing runs on platforms out of vendor support" assesses SAF-D5 |
| Goals (SAF-G) | Drivers motivate goals | Resource constraints (SAF-D5) motivate cost efficiency (SAF-G1) |
| Principles (SAF-P) | Drivers explain why a principle exists | Trust and data protection (SAF-D3) explain privacy by design (SAF-P11) |
| Capabilities (Strategy) | Capabilities are developed in response to drivers, through goals | AI and technological acceleration (SAF-D2) drives investment in methodology (capability 2.2.3) |
| Value streams (Strategy) | Value streams show where a driver affects the production chain | Evolving data ecosystems (SAF-D1) affect data acquisition (VS-01) |

### SAF drivers

| ID | Driver | Type | Description | Architectural response in the SAF |
|---|---|---|---|---|
| **SAF-D1** | Evolving data ecosystems and partnerships | External | Statistics no longer rely on surveys alone. They draw on administrative, commercial, platform and community data. This creates opportunities, but also dependencies on actors outside the NSI's control. | Secure data sharing, standard interfaces, open-source collaboration and transparent governance, so that NSIs can take part in national data platforms and European data spaces. |
| **SAF-D2** | Artificial intelligence and technological acceleration | External | AI, automation and fast technological change alter how data is created, processed and used. NSIs must adopt these technologies and make their own outputs AI-ready. | A risk-based approach: tight control of methodologically critical processes, more automation where risk is lower. Modular, standards-based design to adopt new technology at a controlled pace. |
| **SAF-D3** | Trust, scientific rigour and data protection | External | Misinformation, privacy concerns and unregulated data providers put public confidence under pressure. Trust needs more than compliance. It needs rigour, transparency and accountability. | Protection built into the design: confidentiality controls, methodological integrity, traceability, and oversight in proportion to sensitivity. |
| **SAF-D4** | Uncertain and polarised global environment | External | Global tensions and political polarisation affect how official statistics are demanded and perceived. Cross-border data flows require openness and interoperability. | Interoperable architectures based on shared standards. Design principles that protect independence, comparability and credibility. |
| **SAF-D5** | Resource constraints and organisational agility | Internal and external | Budgets are tight, systems are ageing and specialist skills are scarce. Demand for timely and detailed output keeps growing. | Modular design, shared services, reuse and step-by-step modernisation, so that capacity can be shifted without large reinvestment. |

### Driver details

**SAF-D1 Evolving data ecosystems and partnerships**

Official statistics are moving from isolated data collection to a wider data ecosystem. Surveys used to be the main source. Now they sit next to administrative, commercial, platform and community data. This opens up new forms of collaboration. It also makes NSIs dependent on actors, technologies and infrastructures they do not control.

Open source is part of this ecosystem. It gives NSIs a shared base for innovation, transparency and lower costs. NSIs can develop tools and methods together with peers, academia and private partners.

The SAF responds with architectures for secure data sharing, standard interfaces and transparent governance. These let NSIs take part in national data platforms and European data spaces, where production may span several environments and jurisdictions. Openness is combined with strong governance and clear accountability, so that collaboration does not compromise the integrity of official statistics.

**SAF-D2 Artificial intelligence and technological acceleration**

AI, automation and rapid technological progress are changing how data is created, processed and used. New tools can automate routine tasks, improve analysis and strengthen quality assurance. They also raise the question of what relevant and trusted statistics mean when users rely on intelligent systems.

NSIs must both use AI and make their outputs usable by AI. Internally, that requires architectures and skills for automation, machine learning and advanced analytics, within secure and transparent limits. Externally, statistics must be machine-readable, machine-understandable and interoperable with the platforms that policy makers, researchers and citizens use.

The SAF takes a risk-based approach. Processes that demand methodological rigour and control stay tightly governed. Less sensitive areas can be automated further. Modular, standards-based design lets an NSI adopt new technology at its own pace, while it stays fully accountable for quality, data protection and independence.

**SAF-D3 Trust, scientific rigour and data protection**

Trust is the basis of official statistics. Misinformation, privacy concerns and unregulated data providers put it under pressure. Compliance alone does not maintain public confidence. Scientific rigour, transparency and clear accountability for the handling of data are also needed.

The SAF builds trust and protection into the architecture. It promotes governance and technical controls that protect confidentiality, keep methods sound and make processes traceable. Oversight is strict where sensitivity and quality demands are high. Where risks are lower, more automation and shared solutions are possible.

**SAF-D4 Uncertain and polarised global environment**

Global tensions, political polarisation and shifting power relations affect how official statistics are demanded and perceived. At the same time, cross-border data flows require statistical systems to stay open and interoperable, without giving up national and institutional integrity.

The SAF offers a stable base for cooperation. Interoperable architectures based on shared standards let NSIs exchange data and methods securely. Design principles that protect independence and transparency help NSIs stay credible and comparable, even when facts themselves are contested.

**SAF-D5 Resource constraints and organisational agility**

Many NSIs must do more with limited budgets, ageing systems and a shortage of specialist staff. Demand for timely, detailed and cross-domain output keeps growing. Meeting that demand requires efficiency and the ability to adapt quickly.

The SAF makes flexibility and reuse core principles. It supports modular design, shared services and scalable solutions that reduce duplication. Clear governance of priorities lets NSIs shift capacity, modernise step by step and keep delivering quality output under financial and staffing pressure.

|**PLACEHOLDER: Drivers Template and Application of Drivers to be added to the toolkit**|
|---|

## Goals

### The concept

A goal is a statement of intent. It is the direction or end state an organisation wants to achieve. A goal says *what* the organisation wants to achieve. It does not say *how*, or *how much*.

Three characteristics set goals apart:

- **They are qualitative and directional.** "Modernise statistical systems" sets a direction. A measurable result, such as "retire all platforms out of vendor support by 2029", is an outcome.
- **They are long-term.** A goal usually spans several planning cycles and outlives individual programmes and projects.
- **They are owned by stakeholders.** A goal only has meaning if a stakeholder recognises it as their intention.

The SAF goals cover operational and strategic needs. Some focus on efficiency, modernisation and compliance, which keep an NSI sustainable. Others support innovation and collaboration, such as the use of new data sources or advanced analytics. Together these goals make sure that modernisation does not weaken the core values of official statistics: neutrality, accuracy and reliability.

### How the SAF applies goals

**Why the SAF records goals**

Goals define what success looks like, for the SAF and for the NSIs that apply it. They give direction to the Strategy layer: capabilities and value streams are developed because they contribute to a goal. Without explicit goals, modernisation can turn into a series of technical upgrades that nobody can explain.

**How goals fit into an NSI's own architecture**

The SAF goals are shared by the UNECE statistical community. An NSI relates them to its own strategic plan. It then translates each relevant goal into measurable outcomes and, where needed, into objectives for programmes and projects. Goals that matter nationally but have no SAF counterpart are added as national goals. Each NSI can follow this path at its own pace, while working towards the same shared direction.

**Relationships with other concepts**

| Related concept | Relationship | Example in the SAF |
|---|---|---|
| Drivers (SAF-D) | Drivers motivate goals | Resource constraints (SAF-D5) motivate cost efficiency (SAF-G1) |
| Outcomes (SAF-O) | Outcomes make goals measurable | Increased efficiency (SAF-O5) shows progress on cost efficiency (SAF-G1) |
| Principles (SAF-P) | Principles guide how goals are pursued | Reuse before buying (SAF-P01) guides how cost efficiency is achieved |
| Stakeholders (SAF-ST) | Stakeholders own goals | CIOs and CTOs (SAF-ST01) own modernisation (SAF-G3) |
| Capabilities (Strategy) | Capabilities are developed to realise goals | Methodology (capability 2.2.3) supports data innovation (SAF-G4) |
| Value streams (Strategy) | Value streams show where a goal changes the production chain | Sustainable compliance (SAF-G5) is put into practice in VS-07 |

### SAF goals

| ID | Goal | Description | Architectural direction in the SAF |
|---|---|---|---|
| **SAF-G1** | Cost efficiency and resource sharing | Work as efficiently as possible with limited budgets and growing demand, by sharing services, reusing solutions and pooling resources. | Shared services, reusable and open-source components, modular architectures and step-by-step modernisation. |
| **SAF-G2** | Harmonised reference framework | Provide shared standards, patterns and practices that NSIs adapt locally while staying interoperable. | Common reference models, consistent design principles, and harmonisation as a condition for shared infrastructures and data spaces. |
| **SAF-G3** | Modernisation of statistical systems | Move from fragmented legacy environments to modular, service-based architectures that are secure, scalable and maintainable. | Service-based design, risk-based automation, and principles for access control, data protection and accountability where several parties work together. |
| **SAF-G4** | Support for data innovation | Bring new data sources, methods and products into production without loss of quality or consistency. | Controlled integration (versioning, validation, automated testing), shared platforms that link innovation and production, and safe reuse of open components. |
| **SAF-G5** | Sustainable compliance | Align modernisation with legal, security, quality and ethical frameworks, inside and outside the statistical domain. | Statistical standards (GSBPM, GSIM, SDMX) combined with standards for data management, AI and cloud. Compliance is designed in from the start. |

### Goal details

**SAF-G1 Cost efficiency and resource sharing**

Budgets are limited and demand keeps growing. NSIs must therefore work as efficiently as possible. The SAF promotes shared services, reuse of solutions and better interoperability. By pooling resources and using common components, NSIs gain capabilities they could not build alone, and they avoid duplicate work.

The SAF also encourages open-source components and community platforms where they improve transparency, collaboration and cost. Modular architectures and clear governance let NSIs adapt to new needs, shift capacity and modernise step by step, without large reinvestments. Efficiency then supports quality and long-term sustainability instead of competing with them.

**SAF-G2 Harmonised reference framework**

Without a shared architectural reference, NSIs build isolated solutions. These reduce comparability and raise long-term costs. The SAF offers a common base of standards, patterns and practices. NSIs adapt it to their own context and stay interoperable across borders and domains.

More and more collaboration takes place on shared infrastructures, such as national data platforms and international data spaces. Harmonisation is a condition for taking part. Consistent design principles help NSIs protect the integrity of official statistics, and reuse shared and open solutions safely.

**SAF-G3 Modernisation of statistical systems**

Many NSIs still depend on fragmented legacy IT that slows down innovation and response. The SAF guides the move to modular, service-based architectures that are secure, scalable and easier to maintain. Modernisation reduces technical debt, improves reliability and speeds up the delivery of new and better statistics.

Modernisation more often happens in settings with several parties, from national infrastructures to cross-border data spaces. The SAF sets principles for access control, data protection and accountability in those settings. It also takes a risk-based approach to automation and new technology. Critical processes stay tightly governed to protect methodological rigour. Less sensitive steps can be automated or shared.

**SAF-G4 Support for data innovation**

New data and methods are central to the future of official statistics. Yet many NSIs struggle to introduce a new data source or product. Their production systems are built for predictability and stability. Those qualities are necessary, but they slow down change.

The SAF supports architectures that combine robustness with flexibility. New components, data and workflows can then enter production faster, while quality and compliance stay under control. Versioning, validation and automated testing keep production reliable as it changes. Shared platforms and processes help prototypes move into operational use.

Open source matters here too. NSIs can build on each other's work, which increases transparency and the collective capacity of the community. The SAF supports this with patterns for the safe reuse of open components.

**SAF-G5 Sustainable compliance**

Compliance with laws, standards and ethical principles underpins the trust in and legitimacy of official statistics. Within the statistical domain, GSBPM, GSIM and SDMX remain the basis for consistent processes, metadata management and data exchange.

Statistical production is now part of a wider data and technology ecosystem. Compliance must therefore extend beyond statistical standards. The SAF encourages the use of relevant standards from data management, artificial intelligence and cloud computing. NSIs then stay interoperable with modern platforms and benefit from progress made elsewhere.

With consistent governance and open, verifiable technology, compliance becomes an enabler instead of a brake. Innovation, data sharing and collaboration take place in controlled and auditable environments. Transparency, scientific rigour and privacy by design are part of every process.

|**PLACEHOLDER: Goals Template and Application of Goals to be added to the toolkit**|
|---|

## Meaning

### The concept

Meaning is the knowledge or interpretation that a concept has in a given context. Meaning answers the question *what does this signify?* Value answers a different question: *what is it worth, and to whom?*

The SAF uses meaning at the level of the framework itself. The meaning elements describe how the statistical community should understand the SAF. Two interpretations matter most. First, the SAF connects strategy and technology. Every technology decision, from a new platform to a redesigned process, can be traced to a strategic objective. Next, the SAF is a common language for the UNECE statistical community. Shared models, practices and principles reduce duplicate work and make collaboration easier. This makes the SAF relevant beyond IT, to statisticians, policy makers and the citizens who depend on reliable statistics and information.

### How the SAF applies meaning

**Why the SAF records meaning**

Architecture frameworks are easily misread. IT staff may see a technical blueprint. Managers may see administrative overhead. Explicit meaning elements set the intended interpretation, so that all stakeholders read the framework in the same way.

**How meaning fits into an NSI's own architecture**

An NSI uses the meaning elements when it introduces the SAF internally, for example in an architecture charter, an onboarding programme or a management briefing. An NSI may also record what its own core concepts mean, such as "statistical product" or "steady state". That use belongs in the glossary.

**Relationships with other concepts**

| Related concept | Relationship | Example in the SAF |
|---|---|---|
| Value (SAF-V) | Meaning explains how value is interpreted | The SAF as common language (SAF-M4) explains why cross-border comparability (SAF-V1) is achievable |
| Stakeholders (SAF-ST) | Meaning is shaped for and by stakeholders | IT and data professionals (SAF-ST04) read the SAF through its notation (SAF-M4) |
| Goals (SAF-G) | Meaning frames how goals are understood | The SAF as a foundation for transformation (SAF-M3) frames modernisation (SAF-G3) |
| Glossary | The meaning of individual terms is recorded in the glossary | The definition of "steady state" |

### SAF meaning elements

| ID | Meaning | Description |
|---|---|---|
| **SAF-M1** | Bridge between strategy and technology | The SAF links strategic objectives, such as relevance and efficiency, to technology choices. IT investments are justified by what they contribute to the mission. |
| **SAF-M2** | Catalyst for collaboration | The SAF is a common framework for the statistical community. It makes joint platforms, interoperable systems and harmonised standards possible, and strengthens what UNECE members can do together. |
| **SAF-M3** | Foundation for digital transformation | The SAF is more than a set of technical models. It is the basis for digital transformation in official statistics, without loss of methodological rigour or institutional trust. |
| **SAF-M4** | Common language and notation | Through TOGAF and ArchiMate, stakeholders share one language and notation. This reduces misunderstanding and raises architectural maturity across the community. |

|**PLACEHOLDER: Meaning Template and Application of Meaning to be added to the toolkit**|
|---|

## Outcomes

### The concept

An outcome is an end result that has been, or is intended to be, achieved. Outcomes are more concrete than goals. A goal sets a direction. An outcome describes what will be different once that direction has been followed.

Three characteristics set outcomes apart:

- **They are results, not activities.** "Introduce a metadata catalogue" is an activity. "Every registered dataset has complete metadata and lineage" is an outcome.
- **They are measurable, or at least observable.** An outcome without an indicator cannot be used to steer.
- **They are realised by the strategy and architecture layers.** Capabilities, value streams and solutions exist to produce outcomes.

SAF outcomes are technical as well as societal. On the technical side, NSIs gain simpler processes, better metadata management and faster system development. On the societal side, the SAF supports trust, transparency and comparability, which informed policy and public accountability depend on. Outcomes also change over time. As an NSI matures, it sets new targets and adjusts its course.

### How the SAF applies outcomes

**Why the SAF records outcomes**

Outcomes show stakeholders what adopting the framework returns. They connect long-term goals to concrete changes in capabilities, processes and systems. They also make progress measurable, for one NSI and across the community.

**How outcomes fit into an NSI's own architecture**

An NSI selects the SAF outcomes that match its goals. It defines indicators and target values for its own context, and monitors them in its planning and control cycle. The indicative measures below are examples. The SAF toolkit will offer them as a starting point in SAF-TK-M05.

**Relationships with other concepts**

| Related concept | Relationship | Example in the SAF |
|---|---|---|
| Goals (SAF-G) | Outcomes make goals measurable | Improved interoperability (SAF-O3) shows progress on the harmonised reference framework (SAF-G2) |
| Value (SAF-V) | Outcomes deliver value to stakeholders | Enhanced data quality (SAF-O2) delivers trust and legitimacy (SAF-V6) |
| Capabilities (Strategy) | Capabilities realise outcomes | Metadata management (capability 2.1.2) realises enhanced data quality (SAF-O2) |
| Value streams (Strategy) | Value streams produce outcomes in the production chain | The steady-state handovers in VS-01 to VS-06 contribute to improved interoperability (SAF-O3) |
| Steady states (Business Architecture) | Quality gates make outcomes observable per state | Lineage and metadata requirements per state provide evidence for SAF-O2 |

### SAF outcomes

| ID | Outcome | Description | Indicative measures (illustrative) |
|---|---|---|---|
| **SAF-O1** | Accelerated modernisation | NSIs modernise faster and with less rework, because they start from shared reference models, patterns and building blocks instead of designing from scratch. | Lead time from decision to production for a new statistical product; share of solution designs that reuse SAF building blocks |
| **SAF-O2** | Enhanced data quality | Governance, metadata and lineage are part of the architecture. Statistical output therefore meets high standards of quality and reliability. Quality is designed in, not checked afterwards. | Share of datasets with complete metadata and lineage; revision rate of published figures |
| **SAF-O3** | Improved interoperability | NSIs reach higher interoperability across systems, domains and borders. This makes international collaboration easier, improves comparability and simplifies the use of external data sources. | Share of data exchanges using standard interfaces (e.g. SDMX); number of components shared between NSIs |
| **SAF-O4** | Improved trust and transparency | Openness, security and transparency in the architecture help to build and keep public trust. This strengthens the reputation of NSIs and the legitimacy of their output. | Results of public trust surveys; number of confidentiality or security incidents |
| **SAF-O5** | Increased efficiency | Reuse, harmonisation and standardisation reduce duplicate work. The result is lower IT costs, shorter development cycles and more efficient processing. | Number of redundant systems retired; processing time per production cycle; IT cost per statistical product |
| **SAF-O6** | Shared knowledge base | A community of practice across UNECE members exchanges lessons learned, reusable components and knowledge. This leads to continuous improvement at lower cost. | Number of reusable components and patterns published; number of NSIs contributing |

|**PLACEHOLDER: Outcome Template and the application of Outcomes to be added to the toolkit**|
|---|

## Architecture Principles

### The concept

An **architecture principle** is a general rule that guides how an organisation designs, builds and changes its information provision. Principles are durable and rarely change. They apply to all architecture decisions within their scope, not to one project only.

Principles matter in official statistics because production runs in a closely connected environment. A choice in one place affects many others. Principles keep such choices consistent. They also prevent short-term convenience from undermining long-term sustainability, a real risk for NSIs with legacy systems and tight budgets. Finally, principles create accountability. When stakeholders know the principles behind a decision, investments and trade-offs are easier to explain.

TOGAF recommends describing each principle in four parts:

- **Name**: a short, memorable label.
- **Statement**: the rule itself, in one or two sentences.
- **Rationale**: why the rule exists and what it brings.
- **Implications**: what following the rule requires in cost, resources and activities.

The SAF follows this template. A principle is only useful if it is applied. A principle that never changes a decision is a slogan.

### How the SAF applies principles

**Why the SAF records principles**

Principles turn goals into decision rules. When an NSI chooses between technologies, solutions or designs, principles make the choice consistent and explainable. They also give an architecture board a shared basis for reviewing projects.

**How principles fit into an NSI's own architecture**

An NSI takes the SAF principles into its own principle set, adapts the wording to national policy where needed, and adds national principles. Principles only take effect when they are part of governance. Architecture reviews test compliance, and deviations follow a documented dispensation process. The business layer of the SAF shows how each value stream applies the principles.

**Relationships with other concepts**

| Related concept | Relationship | Example in the SAF |
|---|---|---|
| Goals (SAF-G) | Principles guide how goals are pursued | Loose coupling (SAF-P07) guides modernisation (SAF-G3) |
| Drivers (SAF-D) | Drivers explain why a principle exists | Trust and data protection (SAF-D3) explain privacy by design (SAF-P11) |
| Requirements (SAF-REQ) **[R5]** | Principles are refined into concrete requirements | SAF-P09 becomes the minimum metadata set of each steady state |
| Steady states (Business Architecture) | Principles shape the design rules of the steady-state model | SAF-P07, P08, P09 and P11 underpin the six design rules |
| Value streams (Business Architecture) | Each value stream applies a subset of the principles | VS-07 enforces SAF-P09, P10 and P11 across the chain |

### SAF architecture principles

| ID | Principle | Statement |
|---|---|---|
| **SAF-P01** | Reuse before open source, open source before buying, buying before building | When options are equally suitable, reuse comes before open source, open source before purchase, and purchase before own development. |
| **SAF-P02** | Active support | Systems have an active user community or vendor support. As a rule of thumb, the latest or second-to-last major version is used. |
| **SAF-P03** | Active life cycle management | Systems and components are kept up to date according to an agreed life cycle management policy. |
| **SAF-P04** | Maximise the benefits for the organisation | IT decisions maximise the benefit for the organisation as a whole. |
| **SAF-P05** | IT and technology is everyone's business | All parts of the organisation take part in the IT decisions needed to reach organisational goals. |
| **SAF-P06** | Business continuity | Work continues despite system or staff outages. |
| **SAF-P07** | Implement loosely coupled processes and systems | Processes and systems are built as independently as possible and share functionality through standard interfaces. |
| **SAF-P08** | Data is shared property | Statistical data that adds value for internal or external users is shared. |
| **SAF-P09** | No data without metadata and classification | All shared data has metadata describing its content and meaning. |
| **SAF-P10** | Security by design | Security is an integral part of solutions across all layers of the architecture. |
| **SAF-P11** | Privacy by design | Privacy is an integral part of system architecture and business processes. |

### Principle details

**SAF-P01 Reuse before open source, open source before buying, buying before building**

- *Statement.* When options are equally suitable according to the business case, reuse of (parts of) existing applications comes first. Open-source software comes before purchase, and purchase comes before own development. Non-statistical processes use standard applications only.
- *Rationale.* Reuse is sustainable and cost-efficient, and it leads to standardisation of services and information provision. Open source increases transparency and avoids vendor lock-in.
- *Implications.* Each solution choice records the options considered, in this order. Own development requires explicit justification. Reusable components must be easy to find, for example in a shared catalogue.

**SAF-P02 Active support**

- *Statement.* Hardware and software have an active user community or vendor support. As a rule of thumb, the latest or second-to-last major version is used.
- *Rationale.* Business continuity requires fast and competent support when something breaks. Security requires that known vulnerabilities are fixed in time.
- *Implications.* Support status is a selection criterion for every component. Components that approach end of support are flagged in the life cycle plan.

**SAF-P03 Active life cycle management**

- *Statement.* Systems and components are kept up to date according to an agreed life cycle management (LCM) policy.
- *Rationale.* Without LCM, systems become outdated and vulnerable, and technical debt builds up. Paying off that debt later takes disproportionate effort and creates continuity risks.
- *Implications.* Every component has an owner and a life cycle plan. LCM has a structural budget, not only when problems arise.

**SAF-P04 Maximise the benefits for the organisation**

- *Statement.* IT decisions maximise the benefit for the organisation as a whole.
- *Rationale.* Decisions taken from an organisation-wide view have more long-term value than decisions taken from a departmental view. The principle stands for "service above self".
- *Implications.* Local optimisations need justification against organisation-wide priorities. Shared solutions are preferred over departmental ones, even when they fit one department less well.

**SAF-P05 IT and technology is everyone's business**

- *Statement.* All parts of the organisation take part in the IT decisions needed to reach organisational goals.
- *Rationale.* The users of IT are its main stakeholders. IT only fits the business when business experts and technical staff set goals and objectives together.
- *Implications.* Business ownership of each information system is assigned explicitly. Architecture and change decisions are taken in joint business and IT forums.

**SAF-P06 Business continuity**

- *Statement.* Work continues despite system or staff outages.
- *Rationale.* The more an NSI depends on its systems, the more their reliability matters. Hardware failures, disasters and data corruption must not stop statistical production or release.
- *Implications.* Continuity requirements are part of every design. Critical processes have fallback arrangements, and recovery is tested regularly.

**SAF-P07 Implement loosely coupled processes and systems**

- *Statement.* Processes and systems are built as independently as possible. They share functionality and logic through standard interfaces.
- *Rationale.* Loose coupling makes it easier to change or replace a single process or system. It also improves scalability and robustness, and it makes different security and privacy requirements easier to enforce.
- *Implications.* Domains exchange data through defined interfaces, such as the steady-state handovers in the business architecture. Direct dependencies on another domain's internal data or logic are avoided.

**SAF-P08 Data is shared property**

- *Statement.* Statistical data that adds value for internal or external users is shared.
- *Rationale.* Sharing enables reuse. In data collection, reuse reduces response burden. In processing, it avoids duplicate work on cleaning and analysing data.
- *Implications.* Data is registered and findable in a catalogue. Before new data is collected, reuse of existing data is checked. Access is governed, not withheld by default.

**SAF-P09 No data without metadata and classification**

- *Statement.* All shared data has metadata that describes its content and meaning as well as possible, and an AIC classification (availability, integrity, confidentiality).
- *Rationale.* Metadata makes data FAIR. An AIC classification sets the technical and organisational measures that laws, regulations and security standards require.
- *Implications.* Metadata and classification are recorded when data is registered, not afterwards. Data without the required metadata is not handed over.

**SAF-P10 Security by design**

- *Statement.* Security is an integral part of every solution. Security mechanisms are consistent across all layers of the architecture and scale from small to large objects.
- *Rationale.* Security added afterwards costs more, works less well and leaves gaps between layers.
- *Implications.* Security requirements are set in the design phase of every solution and tested before production.

**SAF-P11 Privacy by design**

- *Statement.* Privacy is an integral part of system architecture and business processes.
- *Rationale.* Privacy added afterwards conflicts with functionality and leaves risks. Built in from the start, it becomes part of the core functionality without limiting it.
- *Implications.* Privacy impact is assessed in the design phase. Measures such as pseudonymisation, data minimisation and disclosure control are placed at defined points in the value chain.

|**PLACEHOLDER: Principles Template and the application of Principles to be added to the toolkit**|
|---|

## Value

### The concept

**Value** is the worth, usefulness or importance of something to a stakeholder. Value is always value *for someone*. The same outcome can be worth a lot to one stakeholder and little to another.

Value differs from the other motivation elements:

- An outcome is a result. Value is what that result is worth to a stakeholder.
- A goal is an intention of the organisation. Value is the reason a stakeholder cares whether the goal is reached.
- Meaning is how something is interpreted. Value is how much it is worth.

The SAF creates value at several levels. For NSIs, it means lower risk, more agility and better alignment between IT and business. For international organisations, it means harmonisation and comparability. For citizens and policy makers, it means statistics they can rely on. Value also has a time dimension. Without a framework, modernisation tends to be fragmented, costly and short-lived. The SAF gives a stable base that reduces technical debt and makes investments last.

### How the SAF applies value

**Why the SAF records value**

Value makes the case for architecture in terms that stakeholders recognise. Architecture competes with other priorities for money and attention. It only gets support when its long-term worth is clear.

**How value fits into an NSI's own architecture**

An NSI uses the SAF value elements to build the business case for architecture work: in investment proposals, annual reports and briefings for its ministry or board. It selects the values that matter to its key stakeholders and links them to the outcomes it measures.

**Relationships with other concepts**

| Related concept | Relationship | Example in the SAF |
|---|---|---|
| Stakeholders (SAF-ST) | Stakeholders perceive value | Policy makers (SAF-ST03) value trust and legitimacy (SAF-V6) |
| Outcomes (SAF-O) | Outcomes deliver value | Improved interoperability (SAF-O3) delivers cross-border comparability (SAF-V1) |
| Meaning (SAF-M) | Meaning explains how value is interpreted | The SAF as bridge between strategy and technology (SAF-M1) underpins strategic alignment (SAF-V4) |
| Value streams (Strategy) | Value streams create value for stakeholders, stage by stage | VS-06 delivers released statistics to users and society |

### SAF value elements

| ID | Value | Description |
|---|---|---|
| **SAF-V1** | Cross-border comparability | Statistics are worth more when they can be compared across borders. Common standards, models and processes make that comparison meaningful. |
| **SAF-V2** | Innovation enablement | The SAF lowers the barriers for AI, machine learning, real-time analytics and big data. NSIs can experiment safely and keep their methods sound. |
| **SAF-V3** | Risk reduction | Compliance, security and governance are built into the architecture. This reduces the risk of system failures, data breaches and regulatory non-compliance, and protects the trust of citizens and stakeholders. |
| **SAF-V4** | Strategic alignment | IT initiatives contribute directly to the mission of producing official statistics. This improves governance, prioritisation and the impact of IT investments. |
| **SAF-V5** | Sustainability | Efficient, modern architectures with less technical debt give NSIs a clear path forward, without repeated and costly overhauls. |
| **SAF-V6** | Trust and legitimacy | Transparency, ethical practice and robust security strengthen the position of NSIs as authoritative providers of public data. |

|**PLACEHOLDER: Value Template and the application of Values to be added to the toolkit**|
|---|

## Assessment

### The concept

An assessment is the result of analysing a driver for one specific organisation. It records what the driver means for that organisation: a strength, a weakness, an opportunity or a threat. A driver describes a force. An assessment describes how that force affects this NSI, today.

Three characteristics set assessments apart:

- **They are specific to one organisation.** "Resource constraints" is a driver for many NSIs. "Two thirds of our processing runs on platforms out of vendor support" is an assessment for one NSI.
- **They are based on evidence.** An assessment rests on facts, such as an application portfolio scan, an audit finding, a maturity assessment or a staff survey. An opinion without evidence is not an assessment.
- **They change over time.** A driver often stays the same for years. An assessment changes as the NSI acts on it. It is therefore reviewed regularly, for example once a year.

The SAF does not define assessments. A generic assessment would contradict the concept itself. This section explains how assessments are used, and the toolkit provides a template to record them.

### How the SAF applies assessments

**Why the SAF uses assessments**

Assessments are the link between the generic SAF drivers and the goals of an NSI. Without them, an NSI jumps from "the world is changing" straight to "we must modernise", and nobody can see why this particular goal has priority. An assessment makes that step explicit. It also gives a baseline: if the next assessment of the same driver is better, the NSI can show progress.

**How assessments fit into an NSI's own architecture**

An NSI writes one or more assessments for each driver it recognises. The second step of applying drivers, *Assess*, produces them (see *Drivers*). A SWOT analysis is a common format: each finding is recorded as a strength, weakness, opportunity or threat. Assessments then feed the third step, *Respond*, in which the NSI derives or confirms its goals. In TOGAF terms, assessments are part of Phase A, Architecture Vision, and of the baseline description of each architecture domain.

**Relationships with other concepts**

| Related concept | Relationship | Example |
|---|---|---|
| Drivers (SAF-D) | An assessment analyses a driver for one NSI | An assessment of SAF-D5 records the share of platforms out of vendor support |
| Stakeholders (SAF-ST) | Stakeholders contribute evidence and recognise the findings | CIOs and CTOs (SAF-ST01) own the assessment of the application portfolio |
| Goals (SAF-G) | Assessments influence which goals an NSI sets and how it prioritises them | A weakness on SAF-D5 makes modernisation (SAF-G3) a priority |
| Outcomes (SAF-O) | A new assessment shows whether outcomes have been reached | The share of unsupported platforms falls after a modernisation programme (SAF-O1) |
| Capability Model (Strategy) | A capability maturity assessment is a structured form of assessment | A low score on metadata management (capability 2.1.2) |

### Examples (illustrative)

The examples show the form of an assessment and its links. They are not SAF assessments and do not apply to every NSI.

| Driver | Assessment | Type | Evidence | Leads to |
|---|---|---|---|---|
| SAF-D5 Resource constraints and organisational agility | Two thirds of our processing runs on platforms that are out of vendor support | Weakness | Application portfolio scan | Priority for SAF-G3 Modernisation of statistical systems |
| SAF-D1 Evolving data ecosystems and partnerships | A national data space is being set up, and our NSI is invited to join as a participant | Opportunity | Government programme plan | Priority for SAF-G2 Harmonised reference framework |
| SAF-D3 Trust, scientific rigour and data protection | We cannot show, for each published figure, which source data version it is based on | Weakness | Internal audit finding | Priority for SAF-O2 Enhanced data quality (lineage) |

|**PLACEHOLDER: Assessment Template and the application of Assessments to be added to the toolkit**|
|---|

## Requirements

### The concept

A requirement is a statement of need that a solution must meet. A goal says what the NSI wants to achieve. A requirement says what a specific solution, process or platform must do or provide to contribute to that goal.

Three characteristics set requirements apart:

- **They apply to a specific solution.** "Modernise statistical systems" is a goal. "The new processing platform records the lineage of every registered dataset" is a requirement.
- **They are testable.** It must be possible to check whether a solution meets the requirement, for example in an architecture review or an acceptance test.
- **They are derived, not invented.** A good requirement can be traced to a goal, an outcome or a principle. A requirement without that trace needs a justification.

The SAF does not define requirements for NSIs. Requirements depend on the solution, the context and the maturity of each NSI. This section explains how requirements relate to the other motivation elements. The toolkit provides a template to derive and record them.

### How the SAF applies requirements

**Why the SAF uses requirements**

Principles and goals are deliberately general. They only change a design when they are made concrete. Requirements are that concrete form. They connect the motivation layer to the architecture domains, and they let an architecture board test whether a solution really contributes to the goals it claims to serve.

**How requirements fit into an NSI's own architecture**

In TOGAF, requirements are managed in Requirements Management, at the centre of the ADM. They are identified in every phase and checked against each architecture decision. An NSI derives its requirements from three sources:

1. **Goals and outcomes.** What must the solution provide to contribute to a goal, and how will the outcome be measured?
2. **Principles.** What does each relevant SAF principle mean for this solution?
3. **SAF reference content.** Which SAF building blocks apply, and what do they require?

The SAF already contains content that works as a set of requirements. The steady states in the business architecture each have quality criteria and a minimum metadata set. An NSI that adopts the steady-state model can use these directly as requirements for the processes and platforms that produce and store each state. The same applies to the principle tables in each value stream. They show which principles apply at which stage of the production chain.

**Relationships with other concepts**

| Related concept | Relationship | Example |
|---|---|---|
| Goals (SAF-G) | Requirements make goals concrete for a solution | SAF-G4 Support for data innovation leads to a requirement for automated testing in the production pipeline |
| Outcomes (SAF-O) | Requirements contribute to outcomes and make them measurable in a solution | Lineage recording contributes to SAF-O2 Enhanced data quality |
| Principles (SAF-P) | Requirements apply principles to a specific solution | SAF-P09 becomes the requirement that no dataset is handed over without its minimum metadata |
| Constraints | Requirements describe what a solution must do; constraints limit how it may be done | A requirement for scalable processing within the constraint that data stays on premises |
| Steady states (Business Architecture) | Quality criteria and minimum metadata per state work as reusable requirements | The criteria for registering data in State #1 Raw Data |

### Examples (illustrative)

The examples show how a requirement is derived and traced. They are not SAF requirements.

| Source | Requirement | Applies to | How to verify |
|---|---|---|---|
| SAF-P09 No data without metadata and classification | No dataset is registered in a steady state without its minimum metadata set and an AIC classification | Data catalogue and registration process | Registration is refused when mandatory metadata is missing |
| SAF-G4 Support for data innovation | A new method can move from the innovation environment to production without manual re-implementation | Analytical platform and deployment pipeline | Time and effort for one pilot method to reach production |
| SAF-P07 Implement loosely coupled processes and systems | Business domains exchange data only through registered steady states, not through each other's internal data | All production processes | Architecture review of data flows between domains |

|**PLACEHOLDER: Requirements Template and the application of Requirements to be added to the toolkit**|
|---|

## Constraints

### The concept

A constraint is a factor that limits how goals can be realised. A requirement describes what a solution must do. A constraint describes the boundaries within which it must be done. Constraints are usually not chosen by the architect. They are given by law, policy, budget, existing contracts or the current landscape.

Three characteristics set constraints apart:

- **They limit the solution space.** A constraint rules out options. "Personal data may not be processed outside the EU" excludes certain cloud services, whatever their other merits.
- **They come from outside the design.** Typical sources are legislation, government policy, budget, staffing, existing contracts and technical dependencies.
- **They differ in how fixed they are.** A legal constraint cannot be negotiated. A budget or policy constraint may change. Recording the source of a constraint shows which ones can be challenged.

This section is about constraints on an NSI's own architecture. It is different from the *Constraints & Assumptions* in the Introduction, which describe the boundaries of the SAF itself (for example SAF-C1 and SAF-C2).

The SAF does not define constraints for NSIs, because legal and organisational contexts differ. Some constraints, however, apply to almost every NSI, such as data protection law and the statistical confidentiality required by national statistical law. They are used below as examples.

### How the SAF applies constraints

**Why the SAF uses constraints**

Constraints that stay implicit cause late surprises. A design that looks right fails in a procurement, a privacy assessment or a security review, because a limit was not known in time. Recording constraints early, and linking them to the goals they affect, keeps the architecture realistic. It also makes trade-offs visible: when a constraint blocks a goal, the board can decide whether to accept that or to challenge the constraint.

**How constraints fit into an NSI's own architecture**

In TOGAF, constraints are identified in Phase A, Architecture Vision, and managed together with requirements in Requirements Management. An NSI records its constraints with their source and whether they are fixed or negotiable. Each constraint is linked to the goals, requirements or solutions it affects. Constraints are reviewed when their source changes, for example after new legislation or a new government policy on cloud use.

Several parts of the SAF help to identify constraints. *Definition of Scope* states that the SAF does not prescribe a technology stack or organisational design, so those choices are left to the NSI and its constraints. The principles on security and privacy by design (SAF-P10 and SAF-P11) point to the legal and security frameworks that usually impose constraints.

**Relationships with other concepts**

| Related concept | Relationship | Example |
|---|---|---|
| Drivers (SAF-D) | Some drivers are the origin of constraints | SAF-D3 Trust, scientific rigour and data protection is the origin of data protection constraints |
| Goals (SAF-G) | Constraints limit how goals can be realised | A ban on public cloud for statistical microdata limits how SAF-G3 Modernisation is realised |
| Requirements | Constraints bound the solutions that can meet a requirement | A scalability requirement must be met within on-premises infrastructure |
| Principles (SAF-P) | Principles are applied within the limits that constraints set | SAF-P01 Reuse before buying applies within public procurement rules |
| Stakeholders (SAF-ST) | Stakeholders often own or impose constraints | A privacy officer applies data protection law; a ministry sets the budget |

### Examples (illustrative)

The examples show the form of a constraint. They are not SAF constraints, and their content differs per country.

| Constraint | Source | Fixed or negotiable | Affects |
|---|---|---|---|
| Statistical microdata is processed only within the NSI's own controlled environment | National statistical law and confidentiality policy | Fixed | Platform and hosting choices for SAF-G3; data sharing under SAF-G2 |
| Personal data is processed in line with the GDPR, including data minimisation and purpose limitation | EU legislation | Fixed | Design of data acquisition and standardisation; SAF-P11 Privacy by design |
| Public cloud services are used only for business support functions, not for statistical production | Government or NSI cloud policy | Negotiable | Technology choices for SAF-G3 and SAF-G4 |

|**PLACEHOLDER: Constraints Template and the application of Constraints to be added to the toolkit**|
|---|

## Stakeholders

### The concept

A **stakeholder** is an individual, group or organisation with an interest in the effects of the architecture **[R8]**. Stakeholders have *concerns*: questions or interests they want the architecture to address, such as cost, risk, quality or compliance.

A stakeholder is not the same as a business actor or role. An actor or role performs work in the architecture, for example a data steward who registers datasets. A stakeholder has an interest in the architecture, whether or not it performs work in it. The same person or organisation can be both.

SAF stakeholders range from CIOs and technical experts within NSIs to international organisations, policy makers, researchers and society as a whole. Their interests differ, and the framework has to balance them. IT professionals turn SAF principles into systems. Policy makers care about the results those systems make possible. UNECE keeps the SAF harmonised and relevant across countries.

### How the SAF applies stakeholders

**Why the SAF records stakeholders**

Architecture is never developed in isolation. Knowing the stakeholders makes clear whose concerns the architecture must address, who should take part in governance and decisions, and which views each audience needs. Involvement also builds support. People who take part in architecture decisions are more likely to back them.

**How stakeholders fit into an NSI's own architecture**

An NSI maps the SAF stakeholders onto its own stakeholder landscape. It identifies who represents each stakeholder and records their concerns. The concerns determine which views the NSI produces. A CIO needs a capability and investment view. A privacy officer needs a view of data flows and protection measures. The stakeholder map is reviewed at the start of each architecture cycle.

**Relationships with other concepts**

| Related concept | Relationship | Example in the SAF |
|---|---|---|
| Drivers (SAF-D) | Stakeholders have concerns about drivers and raise them | CIOs and CTOs (SAF-ST01) raise resource constraints (SAF-D5) |
| Goals (SAF-G) | Stakeholders own goals | NSIs (SAF-ST05) own modernisation (SAF-G3) |
| Value (SAF-V) | Stakeholders perceive value | Researchers and academia (SAF-ST06) value innovation enablement (SAF-V2) |
| Viewpoints | Stakeholder concerns determine which views are produced | Privacy officers need data-flow and protection views |
| Business actors and roles (Business Architecture) | A stakeholder may also act in the architecture | Data providers are stakeholders and actors in VS-01 |

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

# Strategy

## Purpose of this chapter

The Strategy chapter translates motivation into what an NSI must be able to do and how it creates value. Motivation explains *why* change is needed. Strategy describes *what* the organisation needs: its capabilities, the resources behind them, the value streams they support and the courses of action that develop them.

These elements are deliberately independent of organisation structure, processes and systems. Departments, processes and applications change often. Capabilities and value streams change slowly. Anchoring architecture work in this layer lets an NSI compare itself with peers, plan investments over several years, and reorganise or replace technology without losing sight of what it must deliver.

## Position in the framework

The Strategy layer shares the Strategy & Motivation area of the TOGAF ADM with the Motivation layer (see *Position in the framework* in the Motivation chapter). It receives direction from goals and outcomes. It gives direction to the business architecture: value stream stages are realised by business processes, and capabilities are realised by people, processes, information and technology in the lower layers.

|**PLACEHOLDER: Position of the Strategy layer between Motivation and the architecture domains**|
|---|

In TOGAF terms, the Strategy chapter supports capability-based planning. Capabilities and value streams are part of the Architecture Vision (Phase A) and of the baseline and target Business Architecture (Phase B). Courses of action and resources return in Phases E and F, where the NSI decides how and in which order capabilities are developed.

## How NSIs use this chapter

The capability model and the value streams in this chapter are a reference. Most NSIs perform the same core activities, so these elements are largely shared across the community. An NSI uses them in the same three ways as the motivation elements: adopt, adapt or extend.

The capability model is the most practical starting point. An NSI can assess the maturity of each capability, mark where its goals require improvement, and use the result to prioritise investment. Value streams show where in the production chain a capability creates value, and which stakeholders notice a weak capability first.

Resources and courses of action are specific to each NSI. The SAF explains these concepts and gives examples. The toolkit provides templates to record them.

|**PLACEHOLDER: Capability maturity assessment and capability heatmap to be added to the toolkit**|
|---|

## Strategy concepts in the SAF

| SAF section | ArchiMate element | Question it answers | Identifier |
|---|---|---|---|
| Capability Model | Capability | What must the NSI be able to do? | Capability number (e.g. 1.2.1) |
| Value Streams | Value Stream | Which sequence of stages creates value for a stakeholder? | VS-01 to VS-10 |
| Resources | Resource | Which assets does the NSI have or need to perform its capabilities? | Defined by the NSI |
| Courses of Action | Course of Action | Which approach will the NSI take to develop its capabilities and reach its goals? | Defined by the NSI |

The concepts form a chain. Capabilities are what the NSI can do. Resources are what it uses to do it: people, data, knowledge, technology and money. Value streams show where capabilities create value for a stakeholder. Courses of action describe how the NSI will strengthen its capabilities and resources to reach its goals.

## Capability Model

### The concept

Within the Statistical Architecture Framework (SAF), business capabilities define the fundamental abilities of a statistical organization to perform its mission , independent of processes, organizational structures, or technologies. A business capability represents what the organization must be able to do to deliver value and achieve its objectives, providing a stable and long-term view of the enterprise’s functional landscape.

Capabilities serve as the enabling building blocks of the statistical organization. They do not change frequently, even when the underlying processes, applications, or organizational units evolve. For example, the capability “Manage Statistical Data Quality” remains essential regardless of whether data validation is manual, automated, or AI-driven. This stability makes capabilities the preferred unit of analysis for strategic planning, transformation roadmaps, and architecture alignment within the SAF.

Three characteristics set capabilities apart:

- **They are stable.** Statistical quality management (2.1.3) remains essential whether quality checks are manual, automated or AI-supported. Processes and applications change; the capability stays.
- **They are independent of organisation.** A capability can be spread over several departments, or one department can hold several capabilities. The capability model does not follow the organisation chart.
- **They are hierarchical.** High-level capabilities are decomposed into more detailed ones. In the SAF, *Data management* (2.1) is decomposed into, among others, *Metadata management* (2.1.2).

Each capability describes a specific business purpose and outcome, which is realized through one or more business functions and operationalized by business processes. Capabilities therefore serve as the conceptual bridge between strategy and execution. They translate strategic goals into operational competence. Within the SAF, capabilities are often organized hierarchically, showing decomposition from high-level domains (such as Data Governance or Statistical Production) into more granular sub-capabilities (such as Metadata Management or Sampling Design).

### How the SAF applies capabilities

**Why the SAF uses a capability model**

Capabilities are the preferred unit for strategic planning in the SAF. Because they are stable, they make a reliable basis for multi-annual roadmaps. Because they are independent of organisation and technology, they let NSIs compare themselves with each other. A capability view also makes gaps visible: where a goal requires a capability that is weak or missing, investment is needed.

**How capabilities fit into an NSI's own architecture**

An NSI maps the SAF capability model onto its own organisation. It checks which capabilities it has, which it lacks and which are specific to its mandate. It then assesses the maturity of each relevant capability and links capabilities to its goals and outcomes. Capabilities with a low maturity and a high contribution to goals become candidates for investment. Each capability can then be traced to the processes, applications and platforms that realise it.

**Relationships with other concepts**

| Related concept | Relationship | Example in the SAF |
|---|---|---|
| Goals and outcomes (Motivation) | Capabilities realise goals and outcomes | Metadata management (2.1.2) realises enhanced data quality (SAF-O2) |
| Assessment (Motivation) | A capability maturity assessment is a structured form of assessment | A low maturity score for Statistical quality management (2.1.3) |
| Value Streams | Capabilities enable value stream stages | Primary data collection (1.2.1) enables stage *Collect or Receive Data* of VS-01 |
| Resources | Capabilities are performed with resources | Methodology (2.2.3) depends on staff with methodological expertise |
| Courses of Action | Courses of action develop capabilities | A shared platform with partner NSIs develops IT infrastructure (3.2.5) |
| Business functions and processes (Business Architecture) | Business functions and processes realise capabilities | Business function *Classify Data* realises Data standardisation (1.3.1) |
| Steady states (Business Architecture) | Capabilities produce or govern steady states | Data standardisation (1.3.1) produces State #2 Standardized Data |

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

|**PLACEHOLDER: Capability Model Template and the application of Capabilities to be added to the toolkit**|
|---|

## Value Streams **[T1]**

### The concept

A value stream is a sequence of stages that together create an overall result for a stakeholder. Each stage adds a specific piece of value. The value stream ends when the stakeholder receives the result.

Three characteristics set value streams apart:

- **They are seen from the stakeholder.** A value stream starts with a need and ends with value for someone. It does not follow the organisation chart or the order of systems.
- **They describe value, not work.** A stage says *what value* is added. *How* the work is done is described by business processes in the Business Architecture.
- **They are enabled by capabilities.** Each stage needs one or more capabilities. A weak capability shows up as a weak stage.

Value streams and capabilities are two views on the same organisation. Capabilities show *what* the NSI can do. Value streams show *where* that ability turns into value.

### How the SAF applies value streams

**Why the SAF uses value streams**

Value streams connect the capability model to the stakeholders. They make clear which capabilities matter for which result, and which stakeholders notice a weak capability first. They also give the Business Architecture its structure: each stage is realised by business processes, and the primary value streams follow the steady states of data.

**How value streams fit into an NSI's own architecture**

Most NSIs produce statistics in a similar sequence, so the SAF value streams fit most of them. An NSI checks whether the stages match its own production chain, adapts names where needed, and links its own capabilities to each stage. It can then use the value streams to assess where in the chain improvements create the most value for users.

**Relationships with other concepts**

| Related concept | Relationship | Example in the SAF |
|---|---|---|
| Stakeholders (Motivation) | A value stream creates value for a stakeholder | VS-06 creates value for users of statistics (SAF-ST02, SAF-ST03, SAF-ST06) |
| Value (Motivation) | A value stream delivers value elements | VS-06 contributes to trust and legitimacy (SAF-V6) |
| Capability Model | Capabilities enable value stream stages | Primary data collection (1.2.1) enables VS-01.3 *Collect or Receive Data* |
| Courses of Action | Courses of action improve value streams by developing capabilities | A web-first collection strategy improves VS-01 |
| Steady states (Business Architecture) | Each primary value stream produces one steady state | VS-02 produces State #2 Standardized Data |
| Business processes (Business Architecture) | Business processes realise value stream stages | The execution processes of the Standardization domain realise the stages of VS-02 |

The processes that realise each stage, and the steady states between them, are described in the Business Architecture chapter.

### Value stream overview **[T2]** **[T3]**

The SAF has ten value streams. Six primary value streams form the statistical value chain. Four supporting value streams run across the chain.

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

### Capabilities per value stream **[T4]**

|**PLACEHOLDER: ArchiMate view of capabilities serving value stream stages**|
|---|

### Primary Value Streams

**VS-01 Data Acquisition and Ingestion**

The Data Acquisition & Ingestion Value Stream is the first step in the statistical value chain. It focuses on bringing raw data into the statistical system in a secure, traceable, and compliant way. The purpose of this value stream is to make sure that data, no matter where the data comes from, enters the organization in a state that is authentic, well-documented, and ready for use. This value stream sets the foundation for everything that follows. It makes sure that the right data is collected, that legal requirements and ethical guidelines are observed, and that the data is safely stored and traceable from its source.

|**PLACEHOLDER: Add ArchiMate view of VS-01 **|
|---|

| Stage | Name | Value added |
|---|---|---|
| VS-01.1 | Identify Data Needs and Sources | The information need is clear, and suitable sources are known |
| VS-01.2 | Establish Data Agreements and Access Rights | Data can be obtained lawfully, under agreed conditions |
| VS-01.3 | Collect or Receive Data | Data and its metadata are in NSI custody |
| VS-01.4 | Validate and Log Data Intake | The delivery is complete, intact and traceable |
| VS-01.5 | Store and Register Raw Data Artefacts | Raw data is registered and available for reuse (State #1) |

The value created here lies in trust and readiness , trust that the data has been acquired correctly, and readiness for the data to move forward into later stages of the statistical process.

Once data has been safely acquired and registered, it is ready to move into the next phase - the Data Standardization & Integration Value Stream. Here, the focus shifts from collecting data to structuring it, ensuring that all incoming data can be compared, combined, and analyzed.

**VS-02 Data Standardization and Integration**

The Data Standardization & Integration Value Stream is the second step in the statistical value chain. After raw data has been collected and securely stored, it now needs to be standardized, harmonized, and prepared for further processing. In this value stream, the organization ensures that data from different sources - surveys, administrative registers, or external datasets - can work together seamlessly.
This is achieved through consistent structures, common formats, and shared definitions. The main goal is interoperability: data that looks different at the source must be aligned so it can be understood, compared, and reused across systems, domains, and time periods.

|**PLACEHOLDER: Add ArchiMate view of VS-02 **|
|---|

| Stage | Name | Value added |
|---|---|---|
| VS-02.1 | Profile and Assess Data Structure | Differences from the target model are known |
| VS-02.2 | Apply Standard Classifications and Formats | Data uses common codes, formats and identifiers |
| VS-02.3 | Align Metadata and Semantics | Definitions and descriptions are consistent |
| VS-02.4 | Validate Structural and Semantic Conformance | Conformance to standards is confirmed |
| VS-02.5 | Register Standardized Artefacts | Standardized data is registered and available for reuse (State #2) |

The value created here is coherence and comparability, transforming raw data into a structured and standardized asset that can flow smoothly into editing, analysis, and modeling.

Once data is standardized and validated, it can safely move to the Data Editing & Enrichment Value Stream. In that stage, attention shifts from structure and standards to quality and completeness. Here the organization begins improving data accuracy, filling gaps, and enriching datasets with derived or corrected information.

**VS-03 Data Editing and Enrichment**

The Data Editing & Enrichment Value Stream is the third step in the statistical value chain. After data has been standardized and aligned, the next task is to improve its quality, completeness, and usability. At this stage, the organization focuses on cleaning, correcting, and enriching data so that it becomes trustworthy and analytically sound. Errors are detected, inconsistencies are corrected, missing values are filled, and new variables are derived to add more meaning and analytical value. This is where raw, standardized data begins to transform into high-quality statistical input , ready for estimation, modeling, and analysis.

|**PLACEHOLDER: Add ArchiMate view of VS-03 **|
|---|

| Stage | Name | Value added |
|---|---|---|
| VS-03.1 | Conduct Error Detection and Quality Diagnostics | Errors, duplicates, gaps and outliers are known |
| VS-03.2 | Perform Data Editing and Correction | Incorrect values are corrected |
| VS-03.3 | Impute Missing or Non-Response Data | Missing values are filled with documented methods |
| VS-03.4 | Derive Additional Variables and Indicators | Data describes reality better than the source alone |
| VS-03.5 | Perform Quality Evaluation and Versioning | Quality is documented, and processed microdata is registered (State #3) |

The main value created here is data reliability and analytical readiness. By systematically improving data quality, the organization ensures that every subsequent result , every estimate, model, and publication, rests on a solid foundation.

**VS-04 Estimation, Analysis and Statistical Modeling**

The Estimation & Analysis Value Stream is the fourth stage of the statistical value chain. Here, the focus shifts from improving data quality to extracting insight and meaning. At this stage, the organization applies statistical methods, estimation techniques, and analytical models to transform edited and enriched data into representative results that describe real-world phenomena. This is where data becomes statistical information, summarized, interpreted, and validated to reflect populations, trends, and behaviors. Every decision taken in this stage must balance methodological detail with transparency and reproducibility.

|**PLACEHOLDER: Add ArchiMate view of VS-04 **|
|---|

| Stage | Name | Value added |
|---|---|---|
| VS-04.1 | Confirm Estimation and Analytical Approach | The method fits the design and the purpose |
| VS-04.2 | Apply Weighting and Calibration | Bias from sampling, non-response and coverage is reduced |
| VS-04.3 | Estimate and Aggregate Data | Statistics and indicators are available |
| VS-04.4 | Perform Model-Based Analysis | Model-based results complement direct estimates |
| VS-04.5 | Validate and Document Results | Results are sound and documented (State #4) |

The main value created here is analytical insight and statistical credibility. Through careful estimation and analysis, data is turned into knowledge that policymakers, researchers, and society can trust.

After estimation and analysis, the organization moves to the Statistical Product Composition Value Stream. Here, the focus shifts from individual analyses to building integrated and composite products. In that next stage, data from multiple sources and analyses are combined into coherent statistical publications, dashboards, and reports, turning analytical results into accessible products that provide a complete picture.

**VS-05 Statistical Product Composition**

The Statistical Product Composition Value Stream is the fifth stage in the statistical value chain. After estimation and analysis, the focus now shifts to bringing multiple analytical results together to create coherent, meaningful, and high-value statistical products. At this stage, data from different sources, domains, and analyses are combined, refined, and formatted into composite datasets, time series, and indicators that can be used for reporting, policymaking, and research. This value stream transforms intermediate analytical outputs into final statistical products , ready for validation, interpretation, and dissemination.

|**PLACEHOLDER: Add ArchiMate view of VS-05 **|
|---|

| Stage | Name | Value added |
|---|---|---|
| VS-05.1 | Select and Integrate Source Datasets | Relevant results are brought together |
| VS-05.2 | Construct Composite Indicators or Indices | Indices, ratios and aggregates are available |
| VS-05.3 | Perform Consistency and Coherence Checks | The product is internally consistent |
| VS-05.4 | Generate Analytical and Interpretive Outputs | Results are explained and visualised |
| VS-05.5 | Approve and Register Statistical Products | The product is approved for release (State #4, approved) |

The key value created here is coherence and interpretability. Through careful composition, integration, and quality control, statistical outputs become consistent, accessible, and ready to serve their intended purpose.

After products are approved and registered, they move into the Dissemination & Service Delivery Value Stream. Here, the focus shifts from producing statistics to sharing them, making them available through publications, APIs, dashboards, and data services. That next stage ensures that the work done throughout the entire value chain ultimately reaches users in a secure, accessible, and user-friendly way.

**VS-06 Dissemination and Service Delivery**

The Dissemination & Service Delivery Value Stream is the final stage in the statistical value chain. At this point, the statistical products created in the previous stages are published, distributed, and made accessible to users through trusted and secure channels. The main goal of this value stream is to ensure that information reaches users in a way that is accurate, timely, and easy to understand. This includes policymakers, researchers, journalists, businesses, and the general public. Dissemination is not only about releasing data, it is about providing services that help users access, interpret, and apply statistical information responsibly. This step transforms statistical outputs into societal value by enabling informed decision-making, evidence-based policy, and transparency.

|**PLACEHOLDER: Add ArchiMate view of VS-06 **|
|---|

| Stage | Name | Value added |
|---|---|---|
| VS-06.1 | Plan Dissemination and Access Strategy | Target users, channels and formats are set |
| VS-06.2 | Prepare Data for Dissemination | Output is disclosure-safe and in the right format |
| VS-06.3 | Publish and Provide Access Services | Users can find and access the output (State #5) |
| VS-06.4 | Support and Engage Users | Users understand and use the output correctly |
| VS-06.5 | Monitor Usage and Feedback | The NSI knows how its output is used |

The key value created here is impact and accessibility, ensuring that statistics and data services are usable, trusted, and beneficial to all. The Dissemination & Service Delivery Value Stream relies heavily on several cross-cutting value streams:

- Governance and Compliance ensures that all dissemination complies with data protection and confidentiality laws.
- Infrastructure and Platform Enablement provides the technical platforms for portals, Customer and Stakeholder Engagement ensures that dissemination services meet real user needs and expectations.

Together, these supporting streams ensure that dissemination is not just a technical process , but a strategic, user-centered activity that delivers societal value through trustworthy data.

### Supporting value streams

**VS-07 Governance and Compliance**

The Governance and Compliance Value Stream runs horizontally across all stages of the statistical value chain. Its purpose is to make sure that every process, dataset, and product within the organization operates under clear rules, standards, and accountability mechanisms. This value stream builds trust , both inside and outside the organization , by ensuring that all data activities are ethical, transparent, and compliant with legal, methodological, and quality requirements. It provides the framework of control and assurance that keeps the statistical system reliable, consistent, and aligned with national and international standards such as the European Statistics Code of Practice, GDPR, GSBPM, GAMSO and ISO data quality principles.

|**PLACEHOLDER: Add ArchiMate view of VS-07 **|
|---|

| Stage | Name | Value added |
|---|---|---|
| VS-07.1 | Define Governance Frameworks and Policies | Rules for data, metadata, ethics, confidentiality and quality are set |
| VS-07.2 | Establish Legal and Regulatory Compliance Mechanisms | Applicable rules are known and translated into procedures |
| VS-07.3 | Implement Data and Metadata Governance | Ownership, stewardship and lineage are assigned |
| VS-07.4 | Monitor Quality and Compliance Indicators | Quality and compliance status is visible |
| VS-07.5 | Audit, Certify and Report Compliance | Compliance is demonstrated |
| VS-07.6 | Update and Improve Governance Mechanisms | Governance keeps up with new rules and lessons learned |

The value created here is integrity and accountability making sure that the NSI acts responsibly, protects privacy, and delivers products users can trust.

The Governance and Compliance Value Stream supports all other value streams by acting as the foundation of trust and assurance. It ensures that Data Acquisition & Ingestion follows lawful and ethical standards. It guarantees that Editing, Estimation, and Dissemination meet quality benchmarks. It provides the governance structure for Infrastructure, Innovation, and Stakeholder Engagement. In short, it supports the entire SAF value chain, ensuring that every activity is compliant, transparent, and aligned with the mission of producing trustworthy statistics.

**VS-08 Innovation and Methodological Development**

The Innovation and Methodological Development Value Stream makes sure the statistical organization does not stand still. Its purpose is to discover, test, and introduce new ways of working , new data sources, new methods, new tools, and new technologies. This value stream helps the organization move from “we have always done it this way” to “we can do this better, faster, and smarter.”
It connects research, methodology, IT, and business users. It also makes sure that innovation is controlled , so that only methods that are sound, documented, and compliant end up in production.

|**PLACEHOLDER: Add ArchiMate view of VS-08 **|
|---|

| Stage | Name | Value added |
|---|---|---|
| VS-08.1 | Identify Innovation Needs and Opportunities | Promising developments are known |
| VS-08.2 | Conduct Research and Proof-of-Concepts | Ideas are tested in a limited scope |
| VS-08.3 | Evaluate Methodological Soundness and Feasibility | Only sound and feasible innovations proceed |
| VS-08.4 | Develop and Document New Methodologies or Tools | Innovations are ready for reuse |
| VS-08.5 | Integrate Innovation into Production Environments | Innovations run in production under governance |
| VS-08.6 | Promote Knowledge Sharing and Capability Building | Staff can apply the new methods |

The value created here is continuous improvement. Thanks to this stream, the SAF remains future-proof, able to work with new data (IoT, admin, data spaces), new techniques (ML, small-area estimation), and new operating models (secure processing environments, data sharing).
How This Supports the Other Value Streams.
- It gives Data Acquisition new ways to connect to data spaces and new sources.
- It gives Standardization & Integration new mapping or classification techniques.
- It gives Editing & Enrichment smarter imputation and outlier detection.
- It gives Estimation & Analysis new models and ML-based methods.
- It gives Dissemination new channels (APIs, linked data, interactive views).

So, this value stream keeps the entire SAF alive and evolving.

**VS-09 Infrastructure and Platform Enablement**

The Infrastructure and Platform Enablement Value Stream provides the technical and digital foundation that supports every part of the statistical organization. Where the other value streams focus on data, methods, or governance, this one ensures that all those activities can actually run safely, efficiently, and at scale. It delivers the IT environments, data platforms, tools, and integration services that make statistical production possible, from data collection to dissemination. It ensures that the systems are secure, resilient, and compliant, while also flexible enough to handle new technologies and data sources as the organization modernizes. This value stream enables the organization to work faster, smarter, and with confidence. It transforms infrastructure from a background function into an active enabler of the statistical mission, ensuring that every user, process, and dataset has the tools and environment it needs to perform reliably.

|**PLACEHOLDER: Add ArchiMate view of VS-09 **|
|---|

| Stage | Name | Value added |
|---|---|---|
| VS-09.1 | Define Digital and Technical Requirements | Infrastructure needs follow from business needs |
| VS-09.2 | Design Platform and Infrastructure Architecture | Platforms are designed for storage, processing, integration and secure access |
| VS-09.3 | Provision and Configure Platforms | Environments are available with the required controls |
| VS-09.4 | Enable Integration and Orchestration Services | Processes and services are connected |
| VS-09.5 | Ensure Performance, Security and Continuity | Platforms are reliable and protected |
| VS-09.6 | Evolve and Modernise the Technical Ecosystem | The technical landscape stays current |

The value created here is operational capability and continuity, a stable, modern, and adaptive foundation for the entire SAF ecosystem.

Connecting to Other Value Streams
The Infrastructure and Platform Enablement Value Stream supports every other part of the SAF. It underpins the business and data processes by providing the digital environment in which they operate.
- It gives Data Acquisition the secure pipelines and storage needed for data collection.
- It gives Standardization, Editing, and Analysis the computing and orchestration needed to process large datasets efficiently.
- It gives Dissemination the platforms, portals, and APIs through which users access results.
- It ensures Governance and Compliance have the tools to monitor security, quality, and data lineage, and
- It enables Innovation by offering scalable, modern platforms for experimentation and research.

**VS-10 Customer and Stakeholder Engagement**

The Customer and Stakeholder Engagement Value Stream ensures that the statistical organization remains connected, relevant, and responsive to the needs of those it serves. It focuses on building and maintaining mutual understanding and trust between the organization and its users, data providers, partners, and policy stakeholders. In the SAF, this value stream is essential because official statistics exist to create public value. To achieve that, the organization must understand what stakeholders need, communicate transparently, and ensure that products, data services, and policies remain aligned with real-world demands.

This value stream is not a one-way process. It is a continuous dialogue, listening to users, understanding their challenges, and translating those insights into better products, improved services, and stronger relationships.

|**PLACEHOLDER: Add ArchiMate view of VS-10 **|
|---|

| Stage | Name | Value added |
|---|---|---|
| VS-10.1 | Identify and Segment Stakeholders | The NSI knows its users, providers and partners |
| VS-10.2 | Collect and Analyse User Needs | Needs are translated into requirements |
| VS-10.3 | Define and Manage Service Portfolios | Services and products match the needs |
| VS-10.4 | Deliver Services and Manage Relationships | Users and partners are served |
| VS-10.5 | Engage and Communicate with Stakeholders | Stakeholders understand the output |
| VS-10.6 | Monitor Impact and Satisfaction | The NSI knows its impact and acts on it |

The value created here is relevance and trust, ensuring that the organization’s work is understood, used, and appreciated by its partners, users, and society at large.

Connecting to Other Value Streams
The Customer and Stakeholder Engagement Value Stream is the voice and mirror of the statistical organization.
- It connects external expectations with internal capabilities, closing the feedback loop across the SAF.
- It informs Data Acquisition by revealing what data sources or topics matter most to users.
- It influences Product Composition and Dissemination by identifying which outputs and formats users prefer.
- It strengthens Governance and Compliance through transparent communication about data ethics, confidentiality, and quality. It supports Innovation and Methodology by gathering ideas and feedback from real users and partners.

Through this value stream, the organization ensures that it doesn’t just produce data, it produces public value. It turns statistics into impact by aligning what the organization creates with what stakeholders need.

|**PLACEHOLDER: Value Stream Template and the application of Value Streams to be added to the toolkit**|
|---|

## Resources **[T6]**

### The concept

A **resource** is an asset that an organisation owns or controls. Resources are what the organisation uses to perform its capabilities. A capability without the right resources exists on paper only.

The SAF distinguishes six types of resources:

| Type | Examples in an NSI |
|---|---|
| People and skills | Methodologists, data engineers, subject-matter statisticians, architects |
| Data and information | Registers, survey data, administrative data deliveries, classifications, metadata |
| Knowledge | Statistical methods, process documentation, quality frameworks |
| Technology | Data platforms, processing tools, collection systems, secure processing environments |
| Financial | Structural budget, project funding, international grants |
| Relationships and agreements | Data sharing agreements, partnerships with other NSIs, supplier contracts |

Three characteristics set resources apart:

- **They are owned or controlled.** A resource is something the NSI has, or has secured through an agreement. Access to administrative data under a provision agreement is a resource.
- **They are limited.** People, money and data are scarce. Resources therefore force choices between capabilities.
- **They are shared.** The same resource often serves several capabilities. A data platform supports collection, processing and dissemination at the same time.

For an NSI, data is a resource in its own right. Registers, long time series and trusted relationships with data providers are often harder to replace than any system.

### How the SAF applies resources

**Why the SAF uses resources**

Resources make the capability model realistic. A maturity assessment that only looks at processes misses the most common bottleneck: not enough people with the right skills, or no access to a needed data source. Linking resources to capabilities shows where a capability depends on a single expert, an outdated platform or an agreement that expires.

**How resources fit into an NSI's own architecture**

Resources are specific to each NSI. The SAF does not list them. An NSI records the resources behind its key capabilities, notes where resources are missing or at risk, and uses this in its courses of action. Resources also link strategy to the lower layers: technology resources are described in more detail in the application and technology architecture, and data resources in the data architecture.

**Relationships with other concepts**

| Related concept | Relationship | Example |
|---|---|---|
| Capability Model | Resources are assigned to capabilities | Staff with methodological expertise are assigned to Methodology (2.2.3) |
| Courses of Action | Courses of action configure or develop resources | A workforce strategy trains data engineers |
| Assessment (Motivation) | An assessment can record a resource gap | "Two of our three methodologists for small area estimation retire within two years" |
| Constraints (Motivation) | Constraints limit which resources can be used | Public cloud may not be used for statistical microdata |
| Data and technology architecture | Data and technology resources are detailed there | The data platform as a technology resource |

### Examples (illustrative)

| Resource | Type | Supports capabilities | Note |
|---|---|---|---|
| Access to the national population register | Data and information; relationships and agreements | 1.2.2 Secondary data collection; 2.1.4 Statistical register management | Depends on a provision agreement that must be renewed |
| Team of methodologists for estimation | People and skills | 1.3.5 Estimating population parameters; 2.2.3 Methodology | Small team; knowledge concentrated in few people |
| Shared data processing platform | Technology | 1.3 Processing; 2.1.1 Data lifecycle management | Shared by several statistical domains |

|**PLACEHOLDER: Resource Template and the application of Resources to be added to the toolkit**|
|---|

## Courses of Action **[T6]** **[T7]**

### The concept

A **course of action** is an approach or plan for configuring capabilities and resources to reach a goal. It answers the question *how will we get there?*

Courses of action range from broad to specific. ArchiMate calls the broad, long-term ones **strategies** and the narrower, shorter-term ones **tactics**. There is no hard line between the two. A strategy is usually broken down into several tactics, and tactics are realised by developing capabilities and resources.

Three characteristics set courses of action apart:

- **They are choices.** A course of action chooses one approach over others. "Collect data web-first" rules out paper-first. A plan without a choice is not a course of action.
- **They serve goals.** Each course of action contributes to one or more goals and outcomes. A course of action that serves no goal needs a justification.
- **They change capabilities and resources.** A course of action builds, strengthens, shares or retires capabilities and resources.

Strategy, architecture and roadmap are related but different. A strategy sets the direction and the main choices. The architecture describes the structure that results. A roadmap sets the order and timing of the changes.

### How the SAF applies courses of action

**Why the SAF uses courses of action**

Goals say where the NSI wants to go. Capabilities say what it must be able to do. Courses of action connect the two: they describe the choices the NSI makes to close the gap. Recording them explicitly prevents a common problem: programmes that each make sense on their own, but pull the organisation in different directions.

**How courses of action fit into an NSI's own architecture**

Courses of action are specific to each NSI. The SAF does not define them. Most NSIs work with three levels:

1. **Organisation strategy.** The overall direction of the NSI, usually in a multi-annual plan approved by its board or ministry.
2. **Domain strategies.** Strategies for a specific area, such as data, metadata, IT, cloud, security or privacy. Each one refines the organisation strategy for its domain.
3. **Tactics and roadmaps.** Concrete approaches and their order in time, for example in a programme plan.

Each NSI names its own strategies. A small NSI may have one IT strategy that covers applications, infrastructure and cloud. A large NSI may have separate strategies for each. What matters is that the strategies are consistent with each other and traceable to the motivation.

The SAF elements help to make strategies consistent. A domain strategy can be described with the same building blocks used in this framework: the drivers and assessments that make it necessary, the goals and outcomes it serves, the principles it applies, the courses of action it chooses, the capabilities and resources it develops, and the roadmap that sets the order. When all strategies use these building blocks, overlaps and conflicts between them become visible. The toolkit offers templates for this.

Choosing a reference model for the data value chain, such as the Steady-State or the Medallion architecture (see Business Architecture), is itself a course of action.

**Relationships with other concepts**

| Related concept | Relationship | Example |
|---|---|---|
| Goals and outcomes (Motivation) | Courses of action serve goals and contribute to outcomes | A shared-platform strategy serves cost efficiency (SAF-G1) |
| Drivers and assessments (Motivation) | Assessments show why a course of action is needed | An assessment of SAF-D5 leads to a decision to retire legacy platforms |
| Principles (Motivation) | Courses of action apply principles | An application strategy applies SAF-P01 *Reuse before open source, open source before buying, buying before building* |
| Capability Model | Courses of action are realised by developing capabilities | A metadata strategy develops Metadata management (2.1.2) |
| Resources | Courses of action configure resources | A workforce strategy develops data engineering skills |
| Value Streams | Courses of action improve value streams | A web-first collection strategy improves VS-01 |
| Capability 4.1.2 *Policy and planning* | This capability produces the strategies | Translating the organisation strategy into domain strategies |

### Examples of strategies (illustrative)

The examples show which domain strategies NSIs often develop. They are not a required set. Each NSI decides which strategies it needs and how to combine them.

| Strategy | Typical question it answers | Mainly develops |
|---|---|---|
| Data strategy | How do we manage and use data as an asset? | 2.1 Data management; VS-01 to VS-06 |
| Metadata strategy | How do we make data findable, understandable and reusable? | 2.1.2 Metadata management |
| IT strategy | What do we reuse, buy or build, and on which platforms? | 3.2 Computerisation and automation; VS-09 |
| Cloud strategy | Which workloads may run where, and under which conditions? | 3.2.5 IT infrastructure; 3.3 Security and privacy |
| Information security strategy | How do we protect information and systems? | 3.3 Security and privacy; VS-07 |
| Privacy and confidentiality strategy | How do we protect respondents and keep statistical confidentiality? | 3.3.1 Privacy management; 1.3.7 Statistical disclosure |

Other strategies NSIs develop include strategies for data acquisition, dissemination and open data, artificial intelligence, innovation, workforce and skills, and sourcing and partnerships.

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

|**PLACEHOLDER: Strategy Template and the application of Courses of Action to be added to the toolkit**|
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
| From Strategy | Business processes realise value stream stages | The execution processes of the Standardization domain realise the stages of VS-02 |
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

|**PLACEHOLDER: Business architecture templates and mapping instruments to be added to the toolkit**|
|---|

## Relationship with the statistical standards

The SAF business architecture builds on two models that the statistical community already uses.

**GSBPM**, the Generic Statistical Business Process Model, describes statistical production in phases and sub-processes, from *Specify Needs* to *Evaluate*. The SAF process model is based on GSBPM.

**GAMSO**, the Generic Activity Model for Statistical Organisations, describes the activities of a statistical organisation as a whole: strategy and leadership, capability development, production, and the activities that support them. GAMSO places GSBPM in a wider context: GSBPM describes the production activities of GAMSO in detail. The SAF uses GAMSO as the frame of reference for its business functions. The functions are described in SAF terms, so that NSIs can apply them together with their own national function models. An NSI that already works with GAMSO will recognise the main areas.

**GSIM**, the Generic Statistical Information Model, describes the information objects used in statistical production. It is the reference for the SAF business objects.

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
| Integrating view 1 | Process and function architecture and value chain | *How* do processes, functions and value streams fit together? |
| Integrating view 2 | Steady-State and Medallion Architectures | *Where* is data handed over, and with which quality? |

### Functions and processes

Functions and processes are easily confused, but they are different.

A **business function** groups behaviour by the knowledge, skills and resources it needs. Functions are stable. They have no start or end, and they do not depend on the order of work. *Manage Quality* is a function: it exists as long as the NSI exists.

A **business process** is a sequence of activities that leads to a defined result. A process has a trigger, a start and an end. *Collect* is a process: it starts when a collection period opens and ends when the data is stored and checked.

The two cross each other. One process uses several functions, and one function contributes to several processes. In ArchiMate, functions and processes are connected through realisation and assignment relationships. Statistical production is the clearest example: the production function is realised by the production process, which the SAF describes in detail.

### Processes and the data value chain

The process view and the data value chain look at the same production from two angles. The process follows the life cycle of one statistical product, from need to evaluation. The data value chain follows the data, from source to release, across products.

In the Steady-State Architecture, each business domain uses four process types. They connect the two angles:

| Process type in a business domain | Provides | Corresponding GSBPM phases |
|---|---|---|
| Design | Metadata: designs, rules, specifications | 2 Design |
| Implementation | The execution process: instruments, components, configured workflows | 3 Build |
| Execution | Statistical data, registered in a steady state | 4 Collect, 5 Process, 6 Analyse, 7 Disseminate |
| Management | Quality reports and improvements | 8 Evaluate, and the overarching quality and metadata management |

The GSBPM phases 4 to 7 run across several business domains. *Process* (phase 5), for example, spans standardization, editing and part of estimation. The steady states mark where, within that flow, data is handed over with a defined quality.

### Generic and model-specific content

Actors, roles, processes, functions, services, events and objects are generic. They apply to every NSI, whatever reference model it chooses for its data value chain.

The data value chain is model-specific. The business domains, steady states and quality gates differ between the Steady-State and the Medallion Architecture. That is why the SAF describes them per reference model, at the end of this chapter.

## Structure of this chapter

| Section | Content | SAF content |
|---|---|---|
| Business Actors, Business Roles and Business Collaborations | Who is involved in statistical production, and with which responsibilities | Reference |
| Business Processes | The SAF process model, based on GSBPM | Reference |
| Business Functions | The SAF function model | Reference |
| Business Services and Business Interfaces | The services an NSI offers, and the channels through which it offers them | Reference |
| Business Events | Triggering events: what they are, how they are used, examples | Concept and examples |
| Business Objects, Contracts, Representations and Products | Information objects, agreements, forms of output and products: what they are, how they are used, examples | Concept and examples |
| Process and Function Architecture and Value Chain | How processes, functions and value streams fit together, per value stream | Reference |
| Steady-State and Medallion Architectures | Reference models for the data value chain: comparison, selection criteria, combination, and each model in detail | Reference |

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

|**PLACEHOLDER: Role mapping and RACI templates to be added to the toolkit**|
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
| PRD-3.2 | Reuse or build processing and analysis components | This sub-process builds or reuses the components for processing and analysis. Examples are validation rules, imputation routines and estimation programs. The components implement the methods designed in PRD-2.5. Shared components that other products already use are preferred. Each component is documented and version-controlled. |
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

|**PLACEHOLDER: Process templates and process mapping instruments to be added to the toolkit**|
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
| FUN-3.3 | Process statistical data | This function turns raw data into reliable microdata. It integrates, standardises, codes, validates, edits and imputes data. It also derives new variables and units. It applies the methods designed for each product. The function produces standardized and processed microdata. | 1.3.1, 1.3.2, 1.3.3, 1.3.4 |
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

|**PLACEHOLDER: Function templates and organisation-to-function mapping instruments to be added to the toolkit**|
|---|

## Business Services and Business Interfaces

## Business Events

## Business Objects, Contracts, Representations and Products

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
| Separation of standardization and editing | Explicit (#2 vs. #3) | Combined in Silver |
| Separation of internal statistics and released data | Explicit (#4 vs. #5) | Combined in Gold unless subdivided |
| Governance overhead | Higher: more states to own, register, and audit | Lower |
| Fit with platform tooling | Platform-neutral; mapping required | Native in lakehouse platforms |
| Typical adopters | Larger NSIs, many domains, high microdata reuse | Smaller NSIs, platform-led modernisation |

### Selection criteria

The criteria below help an NSI decide which model fits best. They are indicative. No single criterion is decisive, and the SAF toolkit will provide a structured assessment.

| Criterion | Points towards Steady-State | Points towards Medallion |
|---|---|---|
| Organisational size and number of statistical domains | Many domains, many teams handing over data | Few domains, small central data team |
| Reuse of intermediate microdata across domains | High; standardized and processed microdata reused by several products | Limited; most data flows within one product chain |
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
| — | Consumption (external) | Use of statistics by society | Data Consumption, Consumption Optimization | VS-10 (feedback) | 8 | #5 → (#6) |

The execution processes between the business domains are loosely coupled. Each has its own design and implementation. For the mutual exchange of data, they are loosely linked via steady state interfaces. To this end, five steady state phases are recognized as handover points at the business-domain boundaries described above. This means that the business domain "Observation" produces "Raw Data", business domain "Standardization without loss of content" produces "standardized data" etc.
1. raw data,
2. standardized data,
3. processed data,
4. statistics,
5. released data, and
6. Consumable data products.

A steady state phase is therefore an environment where high-quality versions of data are brought together for exchange, but it also represents a value in the value chain of this data.

### The four process types

Each business domain uses the same four process types:

1. **Design** of the execution processes, which provides metadata.
2. **Implementation** of the execution processes, which provides the execution process.
3. **Execution** of the execution processes, which provides the statistical data.
4. **Management** of the execution processes, which provides quality reports.

How an execution process adds statistical value, and therefore how it is designed and implemented, falls outside the scope of the SAF business architecture. That design follows from, among other things, the NSI's methodology.

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

### How each state is described

Each state below is described with the same ten attributes. NSIs can use this template to document their own implementation; the SAF toolkit will provide it as a fill-in form.

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
| Primary consumer | Standardization (VS-02) | Triggered by the *Raw Data Registered* event |
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

Conditional acceptance is a deliberate option. A late or slightly incomplete delivery may still be the best available data. The flag ensures every downstream user knows this.

### 4. Data and metadata characteristics

**Data.** Raw data is stored in its original format, or in a lossless technical equivalent. Permitted technical operations are those that change representation without changing content and that can be reversed: decryption, decompression, character-encoding normalisation, and container conversion. Operations that change values, codes, or record selection are not permitted at #1. The original byte stream, or a verifiable hash of it, is retained.

**Minimum metadata set.**

| Metadata element | Description |
|---|---|
| Persistent identifier and version | Unique identifier of this delivery version |
| Provider | Organisation or respondent group that supplied the data |
| Agreement reference and legal basis | Agreement identifier and the applicable legal ground |
| Channel and method | Transfer channel (file transfer, API, data space connector, survey mode) and instrument version |
| Receipt timestamp | Moment of receipt into NSI custody |
| Integrity proof | Checksum or signature value and algorithm |
| Volume | Record count and size |
| Reference period | Period the data describes, as stated by the provider |
| Structural description | Schema or technical specification the delivery conforms to |
| Gate outcome | Accepted or conditionally accepted, with quality flags |
| Classification | Availability, integrity, and confidentiality rating |

In GSIM terms, #1 typically instantiates a *Data Set* received from an *Information Provider* through an *Exchange Channel* under a *Provision Agreement*.

### 5. Security, privacy, and access

Raw data usually contains direct identifiers and therefore carries the highest confidentiality rating in the chain. Access is limited to the roles that operate the intake and the standardization process. Analysts and subject-matter staff do not work on #1.

Pseudonymisation is normally applied at the transition to #2. Some NSIs pseudonymise at the intake boundary, or receive data already pseudonymised by a trusted third party. Both variants are compatible with the model, provided the choice is documented and the key management is separated from the data. Data minimisation starts before #1: the agreement and the collection design determine that only necessary data is received.

### 6. Ownership and governance

| Role | Responsibility for #1 |
|---|---|
| Data owner | Process owner of Observation/Collection; accountable for lawful acquisition and fitness of the intake |
| Data steward | Maintains metadata and catalogue entries; resolves gate exceptions |
| Data custodian | Operates storage, access control, and retention |
| Relationship manager | Handles provider follow-up on rejected or flagged deliveries (with VS-10) |

### 7. Versioning, retention, and lineage

Every delivery, including a redelivery or correction by the provider, is a new immutable version. A redelivery never overwrites an earlier version, because statistics may already be built on it.

Retention of #1 is governed by two needs that pull in opposite directions. Reproducibility and audit favour keeping raw data; data minimisation and storage cost favour disposal. A common arrangement is to keep #1 until the dependent #3 version is verified and the audit period has passed, while #3 is the state subject to long-term archival requirements. The exact period is set by national law and NSI policy.

Lineage at #1 is the provenance record: the link from the registered version to the provider, the agreement, and the delivery event. Every downstream state must be able to trace back to a #1 version or, where a product starts from another domain's data, to the state it consumed.

### 8. Reuse and handover

Registration of #1 publishes the *Raw Data Registered* event and a catalogue entry. Consumers discover the delivery through the catalogue and access it through the handover interface, never through direct access to the intake system.

One delivery can serve several statistical products. The register-based census and the labour market statistics may both draw on the same population register delivery. Under SAF-P08, products reuse the registered delivery rather than requesting the same data again from the provider. This also reduces response burden.

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
| Value-stream stages | VS-01.3 Collect, Receive, or Extract Data; VS-01.4 Validate and Log Data Intake; VS-01.5 Store and Register Raw Data Artefacts |
| GSBPM | 4.3 Run collection, 4.4 Finalise collection |
| Principles | SAF-P07, SAF-P08, SAF-P09, SAF-P10, SAF-P11 |

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

Standardized data is raw data that has been brought into the common structure, format, and classifications of the NSI. Its values are unchanged. Only the representation changes: fields are renamed and restructured, types are cast, source codes are mapped one-to-one to standard codes, and descriptive metadata is attached. Direct identifiers are removed or replaced with pseudonymous keys. #2 is therefore the first state in which data from different sources can be compared and combined, and the first state without direct identifiers.

The value of #2 is **comparability without loss of content**. Data that looked different at the source now uses the same structure, the same codes, and documented definitions, units, and reference periods. Because no value has changed, the trace back to the authentic delivery in #1 stays simple and deterministic. Every interpretation, correction, or conversion is left to #3, where it is documented as an edit.

#2 is an optional state. A product can go directly from #1 to #3, for example when a source already arrives in the NSI's standard structure and coding. In that case the NSI records in the catalog that #2 was skipped, and why (see *Applying the steady states pragmatically*). **[SS1]**

### 2. Producing and consuming domains

| Role | Domain | Note |
|---|---|---|
| Producer | Standardization without loss of content (VS-02) | Functions: Transform Data, Anonymize Data, Classify Data |
| Primary consumer | Editing (VS-03) | Triggered by the *Standardized Data Registered* event |
| Secondary consumer | Other statistical products | Reuse of the same standardized source under SAF-P08, with authorization |
| Occasional consumer | Innovation and Methodology (VS-08) | Exploration of sources and methods, under specific authorization |
| Assurance | Governance and Compliance (VS-07) | Audit of mapping lineage and pseudonymization |

### 3. Quality gate

The gate for #2 checks conformance and preservation. It does not assess whether values are correct; that is the concern of #3. A value that cannot be mapped is not an error of standardization. It is a fact about the source, so it is flagged and handed to VS-03.

| Criterion | Check | Typical outcome on failure |
|---|---|---|
| Structural conformance | Fields, types, formats, and cardinalities match the target data model | Reject; re-map |
| Classification conformance | Every mapped code exists in the stated classification version; no orphan codes | Reject; correct the correspondence table |
| Mapping coverage | Share of source codes mapped one-to-one is above the agreed threshold | Conditionally accept with flag; unmapped values listed for VS-03 |
| Semantic metadata | Unit, currency, reference-period basis, and definition recorded for every variable | Hold until complete |
| No loss of content | Record counts and key measures identical to the #1 version; no value changed | Reject |
| Identifier protection | Direct identifiers removed or pseudonymized according to the privacy design | Reject; escalate to the privacy officer |
| Referential integrity | Linkage keys exist in the reference register (e.g., the statistical business register) | Conditionally accept with flag |
| Metadata and lineage | Minimum metadata set captured (see attribute 4); field-level lineage complete | Hold until complete |

Conditional acceptance is the normal outcome for many sources. Unmapped codes and unmatched keys are often caused by known lags, such as newly registered businesses. The flag ensures every downstream user knows exactly which values still need work.

### 4. Data and metadata characteristics

**Data.** Standardized data is stored in the canonical target data model. Standard codes are stored next to the original source values, so the original remains visible. Permitted operations are renaming, restructuring, type casting, reformatting (for example from CSV to a standard exchange format), key alignment, one-to-one code mapping through maintained correspondence tables, removal or pseudonymization of direct identifiers, and dropping variables that are not needed for the statistical purpose. Operations that change values are not permitted at #2: unit or currency conversion, reference-period alignment, reconciliation of differing definitions, derivation, interpretive coding of free text, editing, and imputation. These belong to #3. **[SS2]**

**Minimum metadata set.**

| Metadata element | Description |
|---|---|
| Persistent identifier and version | Unique identifier of this standardized version |
| Source reference | The #1 version or versions this dataset was produced from |
| Target model version | Version of the canonical data model applied |
| Mapping ruleset and engine version | Versions of the mapping rules and the tool that applied them |
| Classifications applied | Scheme and version per coded variable (e.g., NACE Rev. 2, ISCED 2011) |
| Mapping coverage and unmapped values | Coverage per variable and the list of values routed to VS-03 |
| Units, currency, and reference-period basis | Recorded per variable as received, not converted |
| Concept links and definition differences | Link to the canonical concept; recorded differences with other sources |
| Pseudonymization record | Identifiers removed or pseudonymized, method, key reference (never the key itself) |
| Conformance assessment | Structural, classification, and semantic results; no-loss-of-content confirmation |
| Gate outcome | Accepted or conditionally accepted, with quality flags |
| Classification | Availability, integrity, and confidentiality rating |

In GSIM terms, #2 typically instantiates a *Unit Data Set* that conforms to a *Data Structure*, whose *Represented Variables* take their values from *Statistical Classifications* and *Code Lists*.

### 5. Security, privacy, and access

#2 is the point where direct identifiers leave the working data. **Removal** deletes an identifier and ends the possibility to link on it. **Pseudonymization** replaces it with a key that still allows records to be linked. The privacy design decides per identifier which of the two applies, and the choice is recorded in the pseudonymization record.

Pseudonymization keys are managed by the data custodian, separately from the data and under separate access rights. Staff who work on #2 and later states never have access to the keys. Some NSIs pseudonymize at intake, or receive data already pseudonymized by a trusted third party. In that case #2 confirms and records the protection that is already in place.

Standardized data is still detailed microdata. Indirect identifiers, such as date of birth, place of residence, or occupation, remain, and combinations of them can identify a person or business. The confidentiality rating of #2 therefore stays high. Access is limited to the roles that standardize and edit the data, and to authorized reusers with a stated purpose. The formal assessment of disclosure risk starts at #3. **[SS3]**

### 6. Ownership and governance

| Role | Responsibility for #2 |
|---|---|
| Data owner | Process owner of Standardization; accountable for conformance and for applying the privacy design |
| Data steward | Registers versions, maintains catalog entries, and resolves gate exceptions |
| Data custodian | Operates storage, access control, and retention; manages pseudonymization keys separately from the data |
| Classification steward | Maintains the correspondence tables and the classification versions used in mapping |
| Metadata and data architect | Owns the target data model and the links to canonical concepts |

### 7. Versioning, retention, and lineage

Every standardization run produces a new immutable version. A new version also arises when the input stays the same but the rules change: a new correspondence table, a new classification version, or a revised target model. The earlier version is never overwritten, because #3 versions may already be built on it. Each #2 version records the exact #1 version and rule versions it was produced from.

Standardization is deterministic, so a #2 version can be regenerated from its #1 version and the recorded rule versions. Many NSIs therefore keep #2 only as long as the dependent #3 versions are produced and reviewed. This only works while #1 and the rule versions are themselves retained. If #1 is disposed of earlier, #2 must be kept for as long as reproducibility requires. The exact periods are set by national law and NSI policy.

Lineage at #2 is field-level. Each standardized value can be traced to the raw value it came from and to the mapping rule that was applied. The pseudonymization record shows which identifiers were replaced, without revealing the keys.

### 8. Reuse and handover

Registration of #2 publishes the *Standardized Data Registered* event and a catalog entry. Consumers discover the version through the catalog and access it through the handover interface, never through the standardization working environment.

One standardized source can serve many statistical products. A population register delivery is standardized once and is then used by the census, labour market statistics, and income statistics. Under SAF-P08, products reuse the registered version instead of standardizing the same source again. Repeating the work per product wastes effort and leads to inconsistent coding of the same source.

The list of unmapped values and the recorded units and periods travel with the handover. VS-03 then knows exactly which interpretive coding and conversions remain to be done.

| Handover element | Content |
|---|---|
| Artifact | Registered Standardized Data version |
| Required metadata | Minimum metadata set (attribute 4), including unmapped values and recorded units and periods |
| Trigger event | *Standardized Data Registered* |
| Responsibility transfer | VS-02 keeps custody; the consumer takes responsibility for editing, interpretive coding, and conversion on receipt of the event |

### 9. Traceability to the framework

| Framework element | References |
|---|---|
| Capabilities | 1.3.1 Data standardization, 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.4 Statistical register management, 3.3.1 Privacy management, 3.3.4 Logical identity and access control |
| Value-stream stages | VS-02.1 Profile and Assess Data Structure; VS-02.2 Apply Standard Classifications and Formats; VS-02.3 Align Metadata and Semantics; VS-02.4 Validate Structural and Semantic Conformance; VS-02.5 Register Standardized Artifacts |
| SAF processes **[SS4]** | PRD-5.2 Classify and code (deterministic mapping only), PRD-5.3 Review and validate (structural checks only), DLM-2 Promote data through a quality gate, DLM-3 Register and catalog data, DLM-4 Classify and protect data, DLM-9 Manage reference and master data |
| GSBPM | 5.1 Integrate data (key alignment only; record linkage takes place in #3), 5.2 Classify and code |
| Principles | SAF-P07, SAF-P08, SAF-P09, SAF-P10, SAF-P11 |
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
- Storing pseudonymization keys together with the data. The protection of #2 is then only on paper.
- Skipping #2 without recording the reason. Auditors can no longer see why the state is missing.

## State #3: Processed Data

### 1. Definition and value added

Processed data is microdata whose content has been checked, corrected, completed, and enriched. Errors, duplicates, outliers, and inconsistencies have been detected and resolved. Missing values have been imputed, free text has been coded, and units, currencies, and reference periods have been converted to a common basis. Records from different sources have been linked, and new variables have been derived. Unlike in #2, values do change here, but every change is documented, attributable, and reversible.

The value of #3 is **reliability and analytical readiness**. Every estimate, model, and publication downstream rests on this microdata. The guarantee is not that values stay the same, but that no value changes without a record of the original value, the rule or decision applied, the reason, the actor, and the time. That record makes it possible to explain, reproduce, or reverse any change.

#3 is the only steady state that is mandatory for all statistical production. It is the microdata on which everything downstream is verifiably built. It is also the state that national archival requirements usually apply to: without it, the statistics built on it cannot be re-verified. **[SS5]**

Processing is primarily driven by the individual statistical domains. Depending on the type of data, it may also be performed by a central unit for efficiency and consistency. Either way, the result is registered as #3 under the same quality gate.

### 2. Producing and consuming domains

| Role | Domain | Note |
|---|---|---|
| Producer | Editing, derivation, and non-response correction (VS-03) | Functions: Imputate Data, Integrate Data |
| Primary consumer | Estimation and Analysis (VS-04) | Triggered by the *Processed Data Registered* event |
| Secondary consumer | Other statistical products | Reuse of processed microdata under SAF-P08, with authorization |
| Secondary consumer | Microdata services (VS-06) | Research datasets are prepared from #3 and released as #5 **[SS6]** |
| Occasional consumer | Innovation and Methodology (VS-08) | Testing of new editing, imputation, or coding methods, under specific authorization |
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

**Minimum metadata set.**

| Metadata element | Description |
|---|---|
| Persistent identifier and version | Unique identifier of this quality version |
| Source reference | The #2 version or versions (or #1, where #2 was skipped) this dataset was produced from |
| Rule and model versions | Versions of the editing rules, imputation models, coding service, and derivation specifications applied |
| Edit lineage | Per changed value: original value, new value, rule or decision, reason code, actor, and time |
| Imputation record | Per imputed value: flag, method code, and the predictors or donors used |
| Coding record | Per coded value: source text, assigned code, method, and confidence |
| Conversion and reconciliation record | Rule, factor or rate, and original value for every conversion or reconciliation |
| Linkage record | Keys used, matching method, linkage rate, and match quality |
| Derived variables | Formula, inputs, unit, and classification per derived variable |
| Quality assessment | Edit rate, imputation rate, coding completion, and improvement against the baseline |
| Disclosure-risk assessment | Outcome of the re-identification risk assessment and the resulting access conditions |
| Gate outcome | Accepted or conditionally accepted, with quality flags |
| Classification | Availability, integrity, and confidentiality rating |

In GSIM terms, #3 typically instantiates a *Unit Data Set*, extended with derived *Represented Variables*. The edits are described as *Rules* applied in *Process Steps*, which gives the edit lineage its formal structure.

### 5. Security, privacy, and access

Processed data is pseudonymized microdata, but it is richer than #2. Linking sources and deriving variables adds detail, and more detail means a higher risk that a person or business can be recognized. #3 is therefore the point where the disclosure risk of microdata is formally assessed. The outcome sets the conditions for access and reuse.

Linkage uses the pseudonymous keys created at #2. The keys themselves remain with the data custodian, separately from the data. Access to #3 is limited to the roles that edit, estimate, and analyze the data, and to authorized reusers with a stated purpose. External researchers never access #3 directly. Their access runs through the microdata services in VS-06, which prepare a project-specific dataset with its own pseudonyms and release it as #5.

The edit audit trail is itself sensitive and must be tamper-evident. It shows who changed which value and why, which is essential evidence in an audit.

### 6. Ownership and governance

| Role | Responsibility for #3 |
|---|---|
| Data owner | Process owner of Editing; accountable for the quality version and for the correct application of approved methods |
| Data steward | Registers quality versions, maintains catalog entries, and resolves gate exceptions |
| Data custodian | Operates storage, access control, retention, and archival; keeps pseudonymization keys separate from the data |
| Methodologist | Owns the editing rules, imputation methodology, and derivation specifications |
| Subject-matter statistician | Adjudicates flagged records and signs off domain-specific corrections |

### 7. Versioning, retention, and lineage

Every completed editing cycle produces a new immutable quality version. A new version also arises when a source is redelivered, when a correction comes in, or when a rule or model changes. The earlier version is never overwritten, because estimates may already be built on it. Many NSIs distinguish preliminary and final versions; both are registered as separate quality versions of #3.

#3 is usually the state with the longest retention. It is the microdata that must be preserved to re-verify published statistics, and archival legislation often applies to it. When #3 is archived, its edit lineage, imputation flags, and derived-variable definitions are archived with it. Without that metadata, the archived values cannot be interpreted.

Lineage at #3 is value-level. Each processed value can be traced back to its original value in #2 or #1, the rule or decision that changed it, and the inputs of any imputation, conversion, or derivation. Linked records keep a reference to the source records they were built from.

### 8. Reuse and handover

Registration of #3 publishes the *Processed Data Registered* event and a catalog entry. Consumers discover the version through the catalog and access it through the handover interface, never through the editing working environment.

Processed microdata is the most valuable reusable asset in the chain. An integrated person-level dataset, edited and enriched once, can serve many statistics on labor, income, education, and health. Under SAF-P08, products reuse the registered quality version rather than editing the same data again. Editing the same data twice leads to different corrections of the same record, and therefore to statistics that do not agree.

The imputation flags travel with the handover. VS-04 needs them to reflect the extra uncertainty of imputed values in its accuracy measures.

| Handover element | Content |
|---|---|
| Artifact | Registered Processed Data quality version |
| Required metadata | Minimum metadata set (attribute 4), including edit lineage, imputation flags, and derived-variable definitions |
| Trigger event | *Processed Data Registered* |
| Responsibility transfer | VS-03 keeps custody; the consumer takes responsibility for weighting, estimation, and analysis on receipt of the event |

### 9. Traceability to the framework

| Framework element | References |
|---|---|
| Capabilities | 1.3.2 Deriving variables and units, 1.3.3 Check content, 1.3.4 Adjusting and imputing, 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management, 2.1.4 Statistical register management |
| Value-stream stages | VS-03.1 Conduct Error Detection and Quality Diagnostics; VS-03.2 Perform Data Editing and Correction; VS-03.3 Impute Missing or Non-Response Data; VS-03.4 Derive Additional Variables and Indicators; VS-03.5 Perform Quality Evaluation and Versioning |
| SAF processes | PRD-5.1 Integrate data, PRD-5.2 Classify and code (interpretive coding), PRD-5.3 Review and validate, PRD-5.4 Edit and impute, PRD-5.5 Derive new variables and units, PRD-5.8 Finalize data files, DLM-2, DLM-3, DLM-7 Revise data, DLM-10 Archive and preserve data |
| GSBPM | 5.1 Integrate data, 5.2 Classify and code, 5.3 Review and validate, 5.4 Edit and impute, 5.5 Derive new variables and units, 5.8 Finalize data files |
| Principles | SAF-P07, SAF-P08, SAF-P09, SAF-P10, SAF-P11 |
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

Both are versions of the same state. Approval does not change an analytical version; it creates a new, immutable version with the status *approved* that refers to the analytical versions it was composed from. #4 is mandatory for all statistical production.

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
| Interpretive content | Commentary and visualizations are reviewed and consistent with the data and its accuracy | Hold until complete |
| Dissemination and confidentiality standards | The product meets the standards, including the disclosure risk of combining outputs | Reject |
| Sign-off | The designated approval authority has approved the product | Hold until approved |

Coherence problems at the approval gate are never solved by adjusting a component estimate in VS-05. If a component is wrong, it goes back to VS-04 and returns as a new analytical version.

### 4. Data and metadata characteristics

**Data.** Statistics in #4 are mostly aggregated data: tables, data cubes, indicators, indices, and time series. They can also include weighted output microdata, prepared for a specific internal use. Permitted operations are weighting and calibration, estimation and aggregation, model-based analysis, seasonal adjustment, initial disclosure control, and, at the approval stage, composition of indicators, indices, and time series from analytical versions. Changing microdata values is not permitted at #4: corrections go back to #3. Final disclosure control for release is not part of #4 either; it belongs to the transition to #5. **[SS8]**

**Minimum metadata set.**

| Metadata element | Description |
|---|---|
| Persistent identifier and version | Unique identifier of this version |
| Status | *Analytical* or *approved* |
| Source reference | The #3 versions (for analytical versions) or the analytical #4 versions (for approved versions) used |
| Methodology | Estimation, weighting, and model methods, with their versions and parameters |
| Weights and calibration totals | Calibration method, auxiliary variables, and the source and version of the totals |
| Accuracy | Standard error, coefficient of variation, or confidence interval per estimate; whether imputation uncertainty is included |
| Model diagnostics | Fit and prediction intervals for model-based results |
| Disclosure control | Method applied and outcome of the risk assessment |
| Coherence results | Outcome of the coherence checks against related and prior statistics |
| Composition record | For approved versions: composition method and the component versions used |
| Interpretive content | For approved versions: reference to commentary, key messages, and visualizations |
| Approval record | For approved versions: approval authority, date, and confidentiality clearance |
| Classification | Availability, integrity, and confidentiality rating |

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
| Data steward | Registers versions, maintains catalog entries, and resolves gate exceptions |
| Data custodian | Operates storage, access control, retention, and the pre-release access log |
| Methodologist | Owns estimation, weighting, and model methods |
| Disclosure control specialist | Owns the disclosure-control rules for internal and potential external use |

### 7. Versioning, retention, and lineage

Every estimation run produces a new immutable analytical version. Every approval produces a new immutable approved version that refers to the analytical versions it was built from. Revisions follow the revision policy: a preliminary figure, a revised figure, and a final figure are three separate versions. Nothing is overwritten, because published figures and other statistics may depend on any of them.

Approved versions that were released are kept for as long as the released figures exist, because they are the direct basis of #5. Analytical versions that never led to a release can be kept for a shorter period, as long as revisions and reproducibility are covered. The exact periods are set by national law and NSI policy.

Lineage at #4 has two steps. An estimate traces back to the #3 version, the method, the parameters, and the weights that produced it. An approved product traces back to the analytical versions it was composed from, and through them to #3.

### 8. Reuse and handover

#4 has two handovers, one for each gate moment. The analytical version goes to VS-05 for composition; the approved version goes to VS-06 for release. Consumers access versions through the catalog and the handover interface, never through the estimation or composition working environment.

Statistics in #4 are also reused internally. Integration systems, such as the national accounts or labor accounts, use statistics from many domains as input. Under SAF-P08 they reuse the registered version instead of estimating the same figure again. This keeps internal use and later publication consistent.

| Handover element | Analytical version (VS-04 → VS-05) | Approved version (VS-05 → VS-06) |
|---|---|---|
| Artifact | Registered analytical #4 version | Registered approved #4 version |
| Required metadata | Methodology, weights, accuracy, model diagnostics, disclosure control, coherence results | Composition record, propagated accuracy, coherence results, interpretive content, approval record |
| Trigger event | *Output Data Registered* | *Statistical Product Registered* |
| Responsibility transfer | VS-04 keeps custody; VS-05 takes responsibility for composition and approval | VS-05 keeps custody; VS-06 takes responsibility for final disclosure control, release, and user support |

### 9. Traceability to the framework

| Framework element | References |
|---|---|
| Capabilities | 1.3.5 Estimating population parameters, 1.3.6 Integrate statistics, 1.3.7 Statistical disclosure, 1.4.1 Statistical (output) analysis, 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| Value-stream stages | VS-04.1 to VS-04.5 (analytical gate); VS-05.1 to VS-05.5 (approval gate) |
| SAF processes | PRD-5.6 Calculate weights, PRD-5.7 Calculate aggregates, PRD-6.1 Prepare draft outputs, PRD-6.2 Validate outputs, PRD-6.3 Interpret and explain outputs, PRD-6.4 Apply disclosure control (initial), PRD-6.5 Finalize outputs, PRD-7.2 Produce dissemination products (content), DLM-2, DLM-3, DLM-7 Revise data |
| GSBPM | 5.6 Calculate weights, 5.7 Calculate aggregates, 6.1 to 6.5 Analyze |
| Principles | SAF-P07, SAF-P08, SAF-P09, SAF-P10, SAF-P11 |
| Medallion layer | Gold, internal sub-layer; not yet released |

### 10. Examples and anti-patterns

**Examples**

- *Survey.* The Labor Force Survey estimates an employment rate of 71.4%, with a 95% confidence interval of ±0.5 percentage points at national level. The variance includes the uncertainty of imputed income from #3. This analytical version is then composed with unemployment and vacancy figures into the quarterly labor market product, which is approved and registered.
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

Released data is statistical output that the NSI has made available outside its own organization. It is based on an approved #4 version that has passed final disclosure control, has been documented for correct interpretation, and has been released through a trusted channel. Released data includes published tables and datasets, open data, data available through an API, deliveries to international organizations, data offered in a data space, and de-identified microdata made available to accredited researchers. #5 is the last point at which the NSI controls the data. Once users have it, it becomes consumed data, outside the NSI's control.

The value of #5 is **accessibility and trust**. Users get accurate, documented statistics through channels they can rely on, at a moment that is the same for everyone. The final disclosure check ensures that no respondent can be identified. The documentation ensures that users can interpret the figures correctly, including their accuracy and limitations.

#5 is mandatory whenever output is released. If nothing changes between the approved #4 version and the release, the same artifact can be marked as released instead of being registered again. The release steps still take place and are recorded: release authorization, the final disclosure check, and the release itself (see *Applying the steady states pragmatically*).

### 2. Producing and consuming domains

| Role | Domain | Note |
|---|---|---|
| Producer | Dissemination (VS-06) | Functions: Data Delivery, Data Publication |
| Primary consumer | External users | Policy makers, researchers, media, businesses, and the public; use turns #5 into #6 |
| Primary consumer | International organizations | Deliveries under agreed transmission programs, such as to Eurostat or the OECD |
| Primary consumer | Accredited researchers | Access to de-identified research datasets in a secure processing environment **[SS9]** |
| Secondary consumer | Customer and Stakeholder Engagement (VS-10) | Usage and feedback data for needs analysis and impact measurement |
| Assurance | Governance and Compliance (VS-07) | Audit of disclosure control, equal access, and release authorization |

### 3. Quality gate

The gate for #5 is the release gate. Confidentiality is not negotiable at this boundary. Unlike the earlier gates, the disclosure criteria allow no conditional acceptance: a release that fails them is returned for further protection. **[SS10]**

| Criterion | Check | Typical outcome on failure |
|---|---|---|
| Approved source | The release is based on an approved #4 version | Reject |
| Final disclosure control | Final protection applied and disclosure-risk criteria met for every table, dataset, and dashboard | Reject; apply further protection |
| De-identification | Released microdata meets the de-identification standard for its channel | Reject |
| Documentation | Methodology notes, metadata, and user guidance are complete | Hold until complete |
| Format and accessibility | Each channel format is valid, machine-readable where required, and meets the accessibility standard | Hold until corrected |
| Release authorization | The release has been signed off | Hold until authorized |
| Timing and equal access | Release time follows the release calendar; embargo arrangements are in place and logged | Hold until the release slot |
| Metadata | Minimum metadata set captured (see attribute 4) | Hold until complete |

### 4. Data and metadata characteristics

**Data.** One released version can have several representations, one per channel: a published table, an SDMX dataset behind an API, a dashboard, or a research dataset. All representations come from the same released version, so a user always gets the same figure through every channel. Permitted operations are final disclosure control, de-identification of microdata, formatting per channel, packaging, and adding documentation. Changing the statistical content is not permitted at #5. A correction to a released figure goes back to #4 as a new approved version and is released again with an erratum. **[SS11]**

**Minimum metadata set.**

| Metadata element | Description |
|---|---|
| Persistent identifier and version | Unique identifier of this release version |
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
| Classification | Availability, integrity, and confidentiality rating |

In GSIM terms, #5 is the disseminated form of a *Data Set* together with its *Referential Metadata*. SDMX defines the structure in which it is exchanged with users and international organizations.

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
| Data steward | Registers release versions, maintains documentation, and handles errata |
| Data custodian | Operates channels, access control, integrity protection, and the embargo log |

### 7. Versioning, retention, and lineage

Every release is an immutable version. A correction never silently replaces a released figure. It produces a new approved #4 version, a new release version, and a public erratum that explains what changed and why. Earlier releases remain identifiable, so users can see which figure was available at which moment.

Released statistics are usually kept permanently, as part of the public record. National archival legislation often prescribes this. Research datasets are the exception: they are disposed of when the research project closes, together with their project-specific pseudonymization keys. The approved code and outputs of the project are kept for reproducibility.

Lineage at #5 closes the chain. Each released figure traces back to its approved #4 version, and from there through the analytical versions, #3, and #2 to the authentic delivery in #1. This makes it possible to answer any question about a published figure, from source to release.

### 8. Reuse and handover

Release publishes the *Statistics Released* event and makes the data available through the agreed channels. #5 has no downstream production stream. Its handover is to users outside the NSI, where the data becomes consumed data (#6). Usage and feedback flow back to VS-06 and VS-10, and through them into the design of the whole chain.

Released data is the most widely reused form of NSI output. Under SAF-P08 it is offered as openly as confidentiality allows, in standard formats and with clear terms of use. Open, documented release reduces the number of individual data requests and lets users combine NSI data with other sources.

| Handover element | Content |
|---|---|
| Artifact | Released data version, in its channel-specific representations |
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
| Principles | SAF-P07, SAF-P08, SAF-P09, SAF-P10, SAF-P11 |
| Medallion layer | Gold, published sub-layer |

### 10. Examples and anti-patterns

**Examples**

- *Survey.* The quarterly labor market figures are released at 09:00 on the calendar date, at the same moment on the website, the API, and the dashboard. Two small regional cells are suppressed in the final disclosure check. Accredited media received an embargoed copy and publish at the same moment.
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

# Statistical Data Value Chain

## Overview

### Purpose of this chapter

This chapter describes how the statistical value chain works in practice. The Strategy chapter introduced the ten value streams, their stages, and the value they create. The Steady-State Architecture describes the results the chain hands over: the states, their quality gates, and their metadata. This chapter describes the work between those results: the stages, the processes that realize them, the roles that carry them out, and the events that connect them. Every value stream is described with the same structure, so that NSIs can compare them and map their own organization onto them. **[VC1]**

### Where to find what

| Question | Answered in |
|---|---|
| Which value streams exist, and what value do they create? | Strategy, *Value Streams* |
| What must data satisfy at each handover point? | Steady-State Architecture, per state |
| How is the work in each value stream organized? | This chapter |
| Which actors, roles, processes, and functions exist? | Business Architecture, reference content |
| How mature is an NSI, and how does it apply a value stream? | SAF Toolkit |

The division of work between states and value streams is deliberate. A state describes the **result**: what the data looks like, which gate it passed, and how it is protected. A value stream describes the **work**: who does what, in which order, and with which controls. Gate criteria and minimum metadata sets are therefore not repeated in this chapter. Each value stream refers to the state it produces.

### The chain at a glance

![Statistical data value chain overview](images/value-chain-overview.png)

|**PLACEHOLDER: ArchiMate view of the statistical data value chain: six primary and four supporting value streams, with the steady states between the primary streams**|
|---|

Six primary value streams form the production chain. Each one consumes a registered state version and produces the next. They are loosely coupled (SAF-P07): a value stream needs no knowledge of the internal work of its neighbors, only of the state it receives and the state it delivers. The handover is triggered by a registration event. Four supporting value streams run continuously across the whole chain. They set the rules, develop new methods, provide the platforms, and keep the chain connected to its users and data providers.

| VS | Value stream | Type | State in → out | Event out |
|---|---|---|---|---|
| VS-01 | Data Acquisition and Ingestion | Primary | #0 → #1 | *Raw Data Registered* |
| VS-02 | Data Standardization and Integration | Primary | #1 → #2 | *Standardized Data Registered* |
| VS-03 | Data Editing and Enrichment | Primary | #2 → #3 | *Processed Data Registered* |
| VS-04 | Estimation, Analysis and Statistical Modeling | Primary | #3 → #4 (analytical) | *Output Data Registered* |
| VS-05 | Statistical Product Composition | Primary | #4 (analytical) → #4 (approved) | *Statistical Product Registered* |
| VS-06 | Dissemination and Service Delivery | Primary | #4 (approved) → #5 | *Statistics Released* |
| VS-07 | Governance and Compliance | Supporting | Across the chain | n/a |
| VS-08 | Innovation and Methodological Development | Supporting | Across the chain | n/a |
| VS-09 | Infrastructure and Platform Enablement | Supporting | Across the chain | n/a |
| VS-10 | Customer and Stakeholder Engagement | Supporting | Across the chain; feedback from #5 and #6 | n/a |

Not every statistical product passes through every primary value stream. A macro statistic, for example, often starts from statistics another domain has already registered. Such a product enters the chain downstream and its lineage points to the state it consumed (see *Applying the steady states pragmatically*). Data that comes from outside the NSI always enters through VS-01.

### The four process types

Every business domain, and therefore every primary value stream, runs the same four process types. **Design** decides how the work is done and delivers metadata: designs, rules, and specifications. **Implementation** builds and tests the solution and delivers the execution process. **Execution** runs the work in each production cycle and delivers the statistical data; the stages of a value stream describe this execution. **Management** monitors the work, assesses quality, and feeds improvements back to design. Design and implementation only run when something changes, execution runs every cycle, and management runs continuously.

The supporting value streams do not follow a production cycle. They run the same pattern as a continuous cycle of plan, build, operate, and improve.

| Process type | Provides | GSBPM phases | Equivalent in supporting streams |
|---|---|---|---|
| Design | Metadata: designs, rules, specifications | 1 Specify Needs, 2 Design | Plan |
| Implementation | The execution process: instruments, components, configured workflows | 3 Build | Build |
| Execution | Statistical data, registered in a state | 4 Collect, 5 Process, 6 Analyze, 7 Disseminate | Operate |
| Management | Quality reports and improvements | 8 Evaluate; overarching quality and metadata management | Improve |

![The four process types](images/four-process-types.png)

|**PLACEHOLDER: ArchiMate view of the four process types (design, implementation, execution, management) and their outputs**|
|---|

### How each value stream is described

Each primary value stream is described with the same ten attributes. The supporting value streams use the same attributes, with two differences: attribute 2 describes the relation to the chain instead of a state transition, and attribute 4 follows the cycle of plan, build, operate, and improve.

| # | Attribute | Question it answers |
|---|---|---|
| 1 | Purpose and value created | Why does this value stream exist, and what value does it add? |
| 2 | Position and state transition | Which state does it consume, and which does it produce? |
| 3 | Stages | Which stages create the value, and what happens in each? |
| 4 | The four process types | How is the value stream designed, built, and managed? |
| 5 | Actors and roles | Who is involved, and with which responsibility? |
| 6 | Capabilities, processes, and functions | Which SAF capabilities, processes, and functions realize the stages? |
| 7 | Principles | Which architecture principles weigh most, and how are they applied? |
| 8 | Interfaces, services, and events | What does the value stream offer and exchange, and what triggers it? |
| 9 | Key performance indicators | How is the performance of the value stream measured? |
| 10 | Examples | What does the value stream look like in practice? |

Each value stream has three ArchiMate views: (a) the value stream with its stages and the capabilities that serve them, (b) the stages and the processes and functions that realize them, and (c) the state handover and its events. Maturity checklists and detailed end-to-end scenarios for each value stream are part of the SAF Toolkit. **[VC2]**

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

## Primary value streams

### VS-01 Data Acquisition and Ingestion

#### 1. Purpose and value created

VS-01 is the entry point of the statistical value chain. It brings data from outside the NSI under NSI custody: survey responses, administrative registers, exchanges in data spaces, and new sources such as web or sensor data. It does not change the content of the data. It makes sure the data is obtained lawfully, received securely, checked for integrity, and registered with its provenance. The value created is **trust and readiness**: trust that the data was acquired correctly, and readiness for use in the rest of the chain. Everything downstream depends on this. If the acquisition of a source cannot be traced, no statistic built on it can be fully defended.

![VS-01 value stream and capabilities](images/vs-01-value-stream.png)

|**PLACEHOLDER: ArchiMate view VS-01 (a) value stream and capabilities**|
|---|

#### 2. Position and state transition

VS-01 takes data from boundary position #0 to State #1. Before VS-01, the data is held by a provider or respondent, outside the NSI's control. After VS-01, it is a registered, immutable version of raw data, in NSI custody and with its provenance recorded. The quality gate, the minimum metadata set, and the protection of State #1 are described in *State #1: Raw Data* and are not repeated here. VS-01 is the only entrance for data from outside the NSI: there is no side door into the chain. A product that starts from data already registered by another domain does not pass VS-01; it enters the chain downstream.

| From | To | Gate | Event out |
|---|---|---|---|
| #0 Source Data | #1 Raw Data | Gate of State #1 (legal basis, authenticity, integrity, security, structure, completeness, timeliness, metadata) | *Raw Data Registered* |

![VS-01 state handover and events](images/vs-01-handover.png)

|**PLACEHOLDER: ArchiMate view VS-01 (c) state handover and events**|
|---|

#### 3. Stages

| Stage | Name | Value added |
|---|---|---|
| VS-01.1 | Identify Data Needs and Sources | The information need is clear, and suitable sources are known |
| VS-01.2 | Establish Data Agreements and Access Rights | Data can be obtained lawfully, under agreed conditions |
| VS-01.3 | Collect or Receive Data | Data and its metadata are in NSI custody |
| VS-01.4 | Validate and Log Data Intake | The delivery is complete, intact, and traceable |
| VS-01.5 | Store and Register Raw Data Artifacts | Raw data is registered and available for reuse (State #1) |

**VS-01.1 Identify Data Needs and Sources**

This stage starts from the information need set in the design of the statistical product. It determines which variables, populations, and reference periods are needed. Before any new collection, it checks whether the data already exists as a registered state version, in line with SAF-P08. Candidate sources are then assessed for quality, coverage, timeliness, legal availability, and cost. In recurring production, the stage confirms the requirements and the availability of the sources for the coming cycle. A significant change, such as a source that disappears, goes back to design instead of being solved during the cycle.

**VS-01.2 Establish Data Agreements and Access Rights**

This stage makes sure the NSI may obtain the data and knows under which conditions. For each source, it establishes the legal basis: a statutory obligation, a data provision agreement, or a usage policy in a data space. It records the purpose of use, the security requirements, and the delivery terms. It also arranges the technical access, such as credentials and certificates. In each cycle, the stage checks that agreements are still valid and credentials have not expired. The agreement reference is later linked to every delivery, so the legal basis of each version can be shown in an audit.

**VS-01.3 Collect or Receive Data**

This stage is where data enters NSI custody. For surveys, the frame and sample are created, the collection is set up, respondents are approached through one or more modes, and non-response is followed up. For administrative data, deliveries arrive through agreed channels, such as secure file transfer, an API, or a data space connector. Emerging sources, such as websites, are extracted according to their specification. At the moment of receipt, the metadata and paradata are captured: source, channel, time of receipt, integrity proof, volume, agreement reference, and for surveys the mode and instrument version. The data is now held by the NSI, but it has not yet been accepted.

**VS-01.4 Validate and Log Data Intake**

This stage applies the quality gate of State #1 to each delivery. It checks authenticity, integrity, security, structure, completeness against the agreement, and timeliness. It does not check or change the content of the data: values that look wrong are passed on, because content quality belongs to VS-03. The outcome is acceptance, conditional acceptance with quality flags, or rejection. A rejected delivery goes back to the provider with the reason, through the relationship manager. Every check, outcome, and decision is logged with the rule version and the actor.

**VS-01.5 Store and Register Raw Data Artifacts**

This stage turns an accepted delivery into State #1. The delivery receives a persistent identifier and is stored in its original form as an immutable version. Its metadata is registered in the catalog, its classification is set, and access rights are applied according to the decisions of the data owner. The stage then publishes the *Raw Data Registered* event, so consuming domains know a new version is available. A redelivery or correction by the provider always creates a new version; it never overwrites an earlier one.

#### 4. The four process types

The execution of VS-01 is described by its stages. This section describes the three other process types: how acquisition is designed, built, and managed.

**Design**

Design determines what data is needed, from which sources, and how it will be acquired. It assesses sources, chooses between primary collection, secondary collection, or a combination, and documents the reasons. It designs the collection instruments, the sample, and the communication with respondents and providers. It also defines the raw data structure, the intake checks, and the metadata to capture, in line with the gate of State #1. Finally, it decides on classification, access, data minimization, and the point in the chain where identifiers are pseudonymized.

| Design process | What it delivers | Main SAF processes |
|---|---|---|
| Design data requirements and source strategy | Data requirements, source assessment, collection strategy | PRD-1.1 Identify needs; PRD-1.2 Consult and confirm needs; PRD-1.3 Establish output objectives; PRD-1.4 Identify concepts; PRD-1.5 Check data availability and suitability; PRD-1.6 Prepare and submit business case |
| Design collection methodology and instruments | Collection modes, questionnaires, sample design, communication plan | PRD-2.3 Design collection; PRD-2.4 Design frame and sample |
| Design raw data structure and intake metadata | Raw data schema, intake metadata model | PRD-2.1 Design outputs and dissemination; DLM-1 Plan and design data assets |
| Design intake checks and exception handling | Check rules, delivery terms, exception policy | PRD-2.5 Design processing and analysis |
| Design classification, access, and privacy | Classification, access design, privacy impact assessment | DLM-1 Plan and design data assets; DLM-4 Classify and protect data |

**Implementation**

Implementation builds and tests the solution that the design describes. It builds or reuses collection instruments, such as web questionnaires and interviewer applications, and configures the receiving channels for deliveries. It automates the intake checks, the capture of metadata, the routing of exceptions, and the publication of the registration event. It sets up the catalog entries and the storage with the designed access rights. Before going live, it tests the components, the end-to-end flow, the security of the channels, and the process in a field test or pilot with real or synthetic data.

| Implementation process | What it delivers | Main SAF processes |
|---|---|---|
| Build collection instruments and channels | Instruments and configured channels | PRD-3.1 Reuse or build collection instruments |
| Configure intake workflows | Automated checks, metadata capture, exception routing, events | PRD-3.4 Configure workflows |
| Configure registration and catalog | Catalog entries, storage, access rights | PRD-3.4 Configure workflows; DLM-3 Register and catalog data |
| Test and finalize the solution | Test reports, field test, operational procedures | PRD-3.5 Test production systems; PRD-3.6 Test statistical business process; PRD-3.7 Finalize production systems |

**Management**

Management watches how acquisition performs and how good the received data is. It tracks response rates, delivery timeliness, rejection rates, and processing time per source and per mode. It assesses the completeness and conformance of deliveries over time, so that a declining source is noticed early. It checks that the catalog is complete and that registered versions match what is stored. It reports on audit and compliance to VS-07, and feeds improvements back to design or, where new methods are needed, to VS-08.

| Management process | What it delivers | Main SAF processes |
|---|---|---|
| Monitor process performance | Performance dashboard, compliance with delivery terms | OVA-4 Process Data Management; OVA-6 Data Supplier Management |
| Assess intake quality | Quality scorecards per source and per mode | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use |
| Manage intake metadata | Catalog completeness and reconciliation | OVA-2 Metadata Management |
| Report audit and compliance | Audit trail summary, compliance reports to VS-07 | OVA-1 Quality Management |
| Drive continuous improvement | Improvement actions fed back to design or VS-08 | PRD-8.1 Gather evaluation inputs; PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan |

#### 5. Actors and roles

VS-01 involves more external actors than any other value stream, because it is where the NSI meets its data providers. The table shows the actors and the reference roles involved. Specialized role names used in an NSI map onto these reference roles (see *Role names in the value streams*). The long-term relationship with each provider is organized in the collaboration COL-01 *Data provision partnership*.

| Actor or role | ID | Process type | Responsibility in VS-01 |
|---|---|---|---|
| Data provider | ACT-03 | External | Delivers administrative or other data under an agreement |
| Respondent | ACT-04 | External | Provides data directly, usually through a survey |
| Supervisory and legal authority | ACT-08 | External | Grants or oversees the legal basis for collection |
| Process owner | ROL-01 | Management | Accountable for the performance of VS-01 |
| Data owner | ROL-02 | Management | Accountable for State #1; decides on access and retention |
| Data steward | ROL-03 | Execution | Registers deliveries, maintains metadata, resolves gate exceptions |
| Data custodian | ROL-04 | Execution | Operates storage, access control, and retention |
| Statistical designer | ROL-06 | Design | Translates the information need into data requirements |
| Methodologist | ROL-07 | Design | Designs collection methods, sample, and questionnaire |
| Metadata and data architect | ROL-08 | Design | Designs the raw data structure and intake metadata |
| Data engineer | ROL-10 | Implementation | Builds instruments, channels, and intake workflows |
| Platform engineer | ROL-11 | Implementation | Configures platforms, endpoints, and access controls |
| Test manager | ROL-12 | Implementation | Plans and coordinates testing and field tests |
| Data collection manager | ROL-13 | Execution | Runs collection campaigns and monitors response |
| Data quality analyst | ROL-14 | Execution | Runs intake checks and logs exceptions |
| Quality manager | ROL-18 | Management | Monitors intake quality and leads improvements |
| Compliance officer | ROL-19 | Management | Checks the legal basis and compliance of acquisition |
| Relationship manager | ROL-23 | Execution | Maintains provider relationships and agreements |

#### 6. Capabilities, processes, and functions

VS-01 mainly draws on the capabilities 1.2.1 *Primary data collection*, 1.2.2 *Secondary data collection*, 2.1.1 *Data lifecycle management*, 2.1.2 *Metadata management*, 3.3.1 *Privacy management*, 3.3.4 *Logical identity and access control*, 3.4.2 *Contact management*, and 3.4.3 *Service agreement*. The table shows which processes realize each stage and which functions they mainly use.

| Stage | Realized by processes | Main functions |
|---|---|---|
| VS-01.1 Identify Data Needs and Sources | PRD-1.1 Identify needs; PRD-1.5 Check data availability and suitability; PRD-2.3 Design collection | FUN-3.1 Design and build statistical products; FUN-6.1 Manage data supplier relationships |
| VS-01.2 Establish Data Agreements and Access Rights | OVA-6 Data Supplier Management; DSP-1 Join a data space; DSP-3 Agree data use conditions | FUN-6.2 Manage data provision agreements; FUN-9.1 Manage data space participation; FUN-10.5 Manage legal affairs |
| VS-01.3 Collect or Receive Data | PRD-4.1 Create frame and select sample; PRD-4.2 Set up collection; PRD-4.3 Run collection; DSP-4 Exchange data under usage control | FUN-3.2 Collect and acquire data; FUN-9.2 Operate data space connectivity |
| VS-01.4 Validate and Log Data Intake | PRD-4.4 Finalize collection; DLM-2 Promote data through a quality gate | FUN-3.2 Collect and acquire data; FUN-7.3 Manage data lifecycle and storage |
| VS-01.5 Store and Register Raw Data Artifacts | DLM-3 Register and catalog data; DLM-4 Classify and protect data; DLM-5 Store and version data | FUN-7.2 Manage metadata; FUN-7.3 Manage data lifecycle and storage; FUN-7.5 Protect data |

![VS-01 stages, processes, and functions](images/vs-01-processes-functions.png)

|**PLACEHOLDER: ArchiMate view VS-01 (b) stages realized by processes and functions**|
|---|

#### 7. Principles

| Principle | Statement | Application in VS-01 |
|---|---|---|
| SAF-P01 | Reuse before open source, open source before buying, buying before building | Collection instruments, connectors, and intake tooling are reused across products; open-source solutions come before purchase **[VC3]** |
| SAF-P07 | Implement loosely coupled processes and systems | State #1 is the only interface to the rest of the chain; no domain reads directly from intake systems |
| SAF-P08 | Data is shared property | Existing registered data is reused before new collection; one delivery serves many products, which reduces response burden |
| SAF-P09 | No data without metadata and classification | Provenance, agreement reference, and classification are captured at receipt, not afterwards |
| SAF-P10 | Security by design | Channels are authenticated and encrypted; integrity proofs and security scans are part of every intake |
| SAF-P11 | Privacy by design | Agreements and collection design limit data to what is needed; the pseudonymization point is decided in design |

#### 8. Interfaces, services, and events

**Boundary interfaces**

| Boundary | Handed over | Trigger | Responsibility transfer |
|---|---|---|---|
| Provider or respondent → VS-01 | Delivery or survey response (#0) | Delivery received or response submitted | The provider is responsible up to receipt; VS-01 takes custody at the point of receipt |
| VS-01 → VS-02 (or VS-03) | Registered raw data version (#1) | *Raw Data Registered* | VS-01 keeps custody; the consumer takes responsibility for further processing on receipt of the event |

**Business services**

| Service | Offered to | Realized in | Interfaces |
|---|---|---|---|
| Data collection service | Respondents, data providers | VS-01.3 Collect or Receive Data | Web questionnaire, interviewer applications, telephone, paper, secure file transfer, API, data space connector |
| Data agreement service | Data providers, legal authorities | VS-01.2 Establish Data Agreements and Access Rights | Agreement management, relationship manager |
| Raw data provisioning service | VS-02 Data Standardization and Integration, VS-03 Data Editing and Enrichment, other domains | VS-01.5 Store and Register Raw Data Artifacts | Registration event, catalog query |
| Intake monitoring service | Process owner, quality manager | Management process type of VS-01 Data Acquisition and Ingestion | Dashboards and quality reports |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Collection period opened* | Start of VS-01.3 for a survey cycle (PRD-4.3) |
| *Agreement expired or changed* | A review in VS-01.2 before the next delivery |
| *Delivery received* | Start of VS-01.4 for that delivery |
| *Data Intake Validated* / *Data Intake Rejected* | Outcome of VS-01.4; rejection starts provider follow-up |
| *Raw Data Registered* | Completion of VS-01.5; triggers the consuming value stream |

**Interaction with the supporting value streams**

| Value stream | Provides to VS-01 | Receives from VS-01 |
|---|---|---|
| VS-07 Governance and Compliance | Legal register, privacy and security policy | Audit trails, compliance evidence |
| VS-08 Innovation and Methodological Development | New sources and collection methods | Improvement needs |
| VS-09 Infrastructure and Platform Enablement | Channels, storage, catalog, event interfaces | Capacity and channel requirements |
| VS-10 Customer and Stakeholder Engagement | Provider relationships and burden insight | Provider feedback and issues |

#### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| Response rate | Share of sampled units that provided data | Per survey, per mode, per cycle |
| Delivery timeliness | Share of deliveries received within the agreed window | Per source, per cycle |
| Rejection rate | Share of deliveries that failed the gate of State #1 | Per source, per cycle |
| Processing time | Time from receipt to registration | Per delivery, per cycle |
| Metadata completeness | Share of required metadata captured at registration | Per delivery |
| Exception rate | Frequency of exceptions per check rule | Per rule, per cycle |

#### 10. Examples

**Survey.** The Labor Force Survey uses a mixed-mode approach. Sampled persons first receive a web invitation; non-respondents are called after two weeks, and hard-to-reach groups are visited by an interviewer. Each mode records its own paradata, such as completion time or interviewer identifier. Responses are registered as one #1 version per collection batch, and the data collection manager follows the response rate per mode during the cycle.

**Administrative register.** The tax authority delivers its quarterly file by secure file transfer on day 38, within the agreed 45 days. The intake checks the checksum, the schema, and the record count, which is 99.2% of the expected volume. Fourteen unknown business identifiers are not an intake issue; they pass through with a flag. The file is registered as `RD-TAX-2026Q3-001`, and the *Raw Data Registered* event notifies VS-02.

**Web data.** Every night, 12,500 product pages of 25 retailers are scraped; on a typical day 95% succeed. Each scrape records the scraper version and a fingerprint of the page structure. When one retailer redesigns its website, the fingerprints change and the success rate drops. Management detects the trend and sends an improvement action to design, where the scraper is rebuilt.

|**PLACEHOLDER: VS-01 maturity checklist and end-to-end scenarios to be added to the toolkit**|
|---|

### VS-02 Data Standardization and Integration

#### 1. Purpose and value created

VS-02 makes data from different sources speak the same language. It takes registered raw data and brings it into the common structure, formats, and classifications of the NSI. It does this without changing any value. It re-expresses the representation, maps source codes one-to-one to standard codes, and records definitions, units, and reference periods as metadata. It is also the point where direct identifiers are removed or pseudonymized. The value created here is coherence and comparability. Data that looked different at the source can now be compared, combined, and reused across products, domains, and time. Because no value changes, the trace back to the authentic delivery stays simple and every interpretation is left to VS-03, where it is documented as an edit.

![VS-02 value stream and capabilities](images/vs-02-value-stream.png)

|**PLACEHOLDER: ArchiMate view VS-02 (a) value stream and capabilities**|
|---|

#### 2. Position and state transition

VS-02 takes data from State #1 to State #2. It starts when a raw data version is registered and ends when a standardized version passes the gate of State #2. The gate, the minimum metadata set, and the protection of State #2 are described in *State #2: Standardized Data* and are not repeated here. State #2 is optional: a product whose source already arrives in the NSI's standard structure and coding can go directly from #1 to VS-03, provided the choice is recorded in the catalog. When VS-02 does run, it is the only place where the standard representation of a source is created, so that all products reuse the same standardized version.

| From | To | Gate | Event out |
|---|---|---|---|
| #1 Raw Data | #2 Standardized Data | Gate of State #2 (structural, classification, and semantic conformance; no loss of content; identifier protection; metadata and lineage) | *Standardized Data Registered* |

![VS-02 state handover and events](images/vs-02-handover.png)

|**PLACEHOLDER: ArchiMate view VS-02 (c) state handover and events**|
|---|

#### 3. Stages

| Stage | Name | Value added |
|---|---|---|
| VS-02.1 | Profile and Assess Data Structure | Differences from the target model are known |
| VS-02.2 | Apply Standard Classifications and Formats | Data uses common codes, formats, and identifiers |
| VS-02.3 | Align Metadata and Semantics | Definitions and descriptions are consistent |
| VS-02.4 | Validate Structural and Semantic Conformance | Conformance to standards is confirmed |
| VS-02.5 | Register Standardized Artifacts | Standardized data is registered and available for reuse (State #2) |

**VS-02.1 Profile and Assess Data Structure**

This stage analyzes the structure of the incoming raw data. It infers types, counts values, measures how often fields are filled, and detects structural anomalies. It then compares the result with the target data model. The outcome is a structure-gap assessment: which fields map directly, which need reformatting, which source codes have a standard correspondence, and which values are uncoded. An unexpected structural change at the source, such as a new file layout, goes back to design instead of being solved during the cycle.

**VS-02.2 Apply Standard Classifications and Formats**

This stage brings the data into the target structure and the standard classifications. Fields are renamed and restructured, types are cast, formats are converted, and linkage keys are aligned. Values that already carry a source code are mapped one-to-one to the standard code through maintained correspondence tables, and the original value is kept next to it. Values without a correspondence, and free text that needs interpretation, are not coded here; they are listed and handed to VS-03. Every mapping applied, and every classification version used, is recorded as lineage.

**VS-02.3 Align Metadata and Semantics**

This stage makes sure the data is understood in the same way everywhere. Each variable is linked to its canonical concept in the concept system. Its unit, currency, and reference-period basis are recorded as metadata, exactly as received. Where sources define the same concept differently, the difference is recorded and flagged for VS-03; values are not adjusted to reconcile them. Quality descriptors, such as completeness and confidentiality flags, are attached in a standard form.

**VS-02.4 Validate Structural and Semantic Conformance**

This stage applies the gate of State #2. It checks the structure against the target model, the codes against the stated classification versions, and the metadata against the harmonized standards. It also checks that no content was lost: record counts and key measures must be identical to the #1 version, and no value may have changed. Unmapped values above the agreed threshold lead to conditional acceptance with a flag, not to rejection, because they describe the source rather than an error. Every check result and decision is logged with the rule version and the actor.

**VS-02.5 Register Standardized Artifacts**

This stage turns an accepted dataset into State #2. It confirms that direct identifiers were removed or pseudonymized according to the privacy design. The dataset receives a persistent identifier and is stored as an immutable version, with field-level lineage to the #1 version it came from. Its metadata, including the list of unmapped values and the recorded units and periods, is registered in the catalog. The stage then publishes the *Standardized Data Registered* event.

#### 4. The four process types

**Design**

Design defines the standard that all data must meet. It sets the canonical target data model, including the representation of dates, geography, currencies, and identifiers, and the key structure for linking sources. It selects the classifications the NSI conforms to, such as NACE, ISCO, COICOP, and NUTS, and defines which version applies and how transitions are handled. It designs the correspondence tables, the rules for recording units, periods, and definition differences, and the conformance checks, including the no-loss-of-content check. It also decides which identifiers are removed, which are pseudonymized, and how the keys are managed.

| Design process | What it delivers | Main SAF processes |
|---|---|---|
| Design target data model and schemas | Canonical data model, concept catalog, linkage key design | PRD-2.2 Design variables; DLM-1 Plan and design data assets |
| Design classification mapping strategy | Classification register, version policy, correspondence tables | PRD-2.5 Design processing and analysis; DLM-9 Manage reference and master data |
| Design metadata and semantic harmonization rules | Harmonized concepts, unit and period metadata rules, definition-difference policy | PRD-2.2 Design variables; OVA-2 Metadata Management |
| Design conformance checks | Structural, classification, semantic, and content-preservation rules | PRD-2.5 Design processing and analysis |
| Design registration, lineage, and privacy | Lineage model, classification, pseudonymization design | DLM-1 Plan and design data assets; DLM-4 Classify and protect data |

**Implementation**

Implementation builds the components that apply the standard. It builds or reuses profiling components and a mapping and format-conversion component that preserves every value. It loads the correspondence tables into mapping services and connects them to the authoritative classifications and registers, with version control. It automates the conformance checks, the pseudonymization, the capture of lineage, and the registration event. Before going live, it tests the components, verifies the correspondence tables against the source code lists, and confirms in a pilot that no content is lost.

| Implementation process | What it delivers | Main SAF processes |
|---|---|---|
| Build profiling and mapping components | Profiling module, value-preserving mapping component | PRD-3.2 Reuse or build processing and analysis components |
| Configure classification mapping services | Mapping services with version-controlled correspondence tables | PRD-3.2 Reuse or build processing and analysis components; DLM-9 Manage reference and master data |
| Configure conformance, pseudonymization, and registration | Automated checks, pseudonymization, lineage capture, events | PRD-3.4 Configure workflows; DLM-3 Register and catalog data |
| Test and finalize the solution | Test reports, mapping verification, operational procedures | PRD-3.5 Test production systems; PRD-3.6 Test statistical business process; PRD-3.7 Finalize production systems |

**Execution**

Execution runs the stages of VS-02 for every registered raw data version that a product needs in standardized form. It starts when a *Raw Data Registered* event arrives, or when a classification version changes and existing versions must be standardized again. The stages run in order and are largely automated; people step in for structural anomalies and gate exceptions. Execution applies the target model, correspondence tables, and rules as they are; a missing correspondence or a new source layout goes back to design. Every run ends with a registered version, a version with flags, or a return for re-mapping.

| Aspect | VS-02 |
|---|---|
| Trigger | *Raw Data Registered*; *Classification version changed* |
| Cadence | Per raw data version; repeated after a change of rules or classification version |
| Performed by | ROL-14 Data quality analyst, ROL-03 Data steward, ROL-09 Classification steward for exceptions |
| Input | Raw data version (#1), target model, correspondence tables, privacy design |
| Output | Registered standardized data version (#2), unmapped-value list, lineage |
| Control point | Gate of State #2 in VS-02.4 |
| Exception path | Re-mapping within VS-02; unmapped values to VS-03; structural change at the source back to design |

**Management**

Management watches the coverage and conformance of standardization. It tracks how many source codes are mapped, how many values are routed to VS-03, and how often a dataset passes the gate at the first attempt. It governs the life cycle of classification versions and correspondence tables, so that every domain uses the same version at the same time. It reports on lineage, pseudonymization, and standards compliance to VS-07. It feeds improvements back to design, such as extending a correspondence table when the same unmapped codes keep returning.

| Management process | What it delivers | Main SAF processes |
|---|---|---|
| Monitor process performance | Coverage, pass rate, and processing time dashboard | OVA-4 Process Data Management |
| Assess standardization quality | Mapping completeness, orphan codes, content-preservation reports | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use |
| Manage classification and metadata lifecycle | Version register, correspondence tables, catalog reconciliation | OVA-2 Metadata Management; DLM-9 Manage reference and master data |
| Report audit and compliance | Lineage audit, pseudonymization and standards compliance to VS-07 | OVA-1 Quality Management |
| Drive continuous improvement | Improvement actions fed back to design | PRD-8.1 Gather evaluation inputs; PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan |

#### 5. Actors and roles

VS-02 is mainly an internal value stream. Its key roles combine knowledge of data models, classifications, and metadata. Standards bodies are involved indirectly, through the classifications and exchange standards the NSI adopts. The table shows the reference roles involved; specialized names in an NSI map onto them (see *Role names in the value streams*).

| Actor or role | ID | Process type | Responsibility in VS-02 |
|---|---|---|---|
| International statistical organization | ACT-07 | External | Maintains classifications and exchange standards, such as NACE, ISCO, COICOP, and SDMX |
| Process owner | ROL-01 | Management | Accountable for the performance of VS-02 |
| Data owner | ROL-02 | Management | Accountable for State #2; decides on access and retention |
| Data steward | ROL-03 | Execution | Registers versions, maintains metadata, resolves gate exceptions |
| Data custodian | ROL-04 | Execution | Operates storage and access control; manages pseudonymization keys separately from the data |
| Methodologist | ROL-07 | Design | Designs the mapping method and the harmonization of definitions |
| Metadata and data architect | ROL-08 | Design | Designs the target data model, concepts, and lineage model |
| Classification steward | ROL-09 | Design | Owns classification versions and correspondence tables |
| Data engineer | ROL-10 | Implementation | Builds profiling, mapping, and conformance components |
| Platform engineer | ROL-11 | Implementation | Configures mapping services, reference-data connections, and access |
| Test manager | ROL-12 | Implementation | Plans and coordinates testing and mapping verification |
| Data quality analyst | ROL-14 | Execution | Runs profiling and conformance checks, logs exceptions |
| Quality manager | ROL-18 | Management | Monitors coverage and conformance, leads improvements |
| Compliance officer | ROL-19 | Management | Checks pseudonymization and standards compliance |

#### 6. Capabilities, processes, and functions

VS-02 mainly draws on the capabilities 1.3.1 *Data standardization*, 2.1.1 *Data lifecycle management*, 2.1.2 *Metadata management*, 2.1.4 *Statistical register management*, 3.3.1 *Privacy management*, and 3.3.4 *Logical identity and access control*.

| Stage | Realized by processes | Main functions |
|---|---|---|
| VS-02.1 Profile and Assess Data Structure | PRD-5.3 Review and validate (structural checks) | FUN-3.3 Process statistical data |
| VS-02.2 Apply Standard Classifications and Formats | PRD-5.2 Classify and code (deterministic mapping); DLM-9 Manage reference and master data | FUN-3.3 Process statistical data; FUN-7.4 Manage reference and master data |
| VS-02.3 Align Metadata and Semantics | OVA-2 Metadata Management | FUN-7.2 Manage metadata |
| VS-02.4 Validate Structural and Semantic Conformance | PRD-5.3 Review and validate (structural checks); DLM-2 Promote data through a quality gate | FUN-3.3 Process statistical data; FUN-7.3 Manage data lifecycle and storage |
| VS-02.5 Register Standardized Artifacts | DLM-3 Register and catalog data; DLM-4 Classify and protect data; DLM-5 Store and version data | FUN-7.2 Manage metadata; FUN-7.3 Manage data lifecycle and storage; FUN-7.5 Protect data |

![VS-02 stages, processes, and functions](images/vs-02-processes-functions.png)

|**PLACEHOLDER: ArchiMate view VS-02 (b) stages realized by processes and functions**|
|---|

#### 7. Principles

| Principle | Statement | Application in VS-02 |
|---|---|---|
| SAF-P01 | Reuse before open source, open source before buying, buying before building | Mapping services and correspondence tables are shared across products; open-source classification and SDMX tooling comes before purchase |
| SAF-P07 | Implement loosely coupled processes and systems | State #2 hides the source structure from consumers; they work with the standard model only |
| SAF-P08 | Data is shared property | A source is standardized once and the registered version serves all products |
| SAF-P09 | No data without metadata and classification | VS-02 is the main point where classifications are applied and harmonized metadata is attached |
| SAF-P10 | Security by design | Every mapping is logged and version-controlled, so the trail from #1 to #2 is tamper-evident |
| SAF-P11 | Privacy by design | Direct identifiers leave the working data at #2; keys are kept separate from the data |

#### 8. Interfaces, services, and events

**Boundary interfaces**

| Boundary | Handed over | Trigger | Responsibility transfer |
|---|---|---|---|
| VS-01 → VS-02 | Registered raw data version (#1) | *Raw Data Registered* | VS-01 keeps custody; VS-02 takes responsibility for standardization on receipt of the event |
| VS-02 → VS-03 | Registered standardized data version (#2), with unmapped values and recorded units and periods | *Standardized Data Registered* | VS-02 keeps custody; VS-03 takes responsibility for editing, interpretive coding, and conversion |

**Business services**

| Service | Offered to | Realized in | Interfaces |
|---|---|---|---|
| Standardization service | Statistical domains | VS-02.1 Profile and Assess Data Structure; VS-02.2 Apply Standard Classifications and Formats | Registration event, mapping specification |
| Classification mapping service | All domains that need code mapping | VS-02.2 Apply Standard Classifications and Formats | Mapping service, correspondence-table lookup, SDMX code lists |
| Standardized data provisioning service | VS-03 Data Editing and Enrichment, other domains | VS-02.5 Register Standardized Artifacts | Registration event, catalog query |
| Conformance monitoring service | Process owner, quality manager | Management process type of VS-02 Data Standardization and Integration | Dashboards and quality reports |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Raw Data Registered* | Start of VS-02 for that version |
| *Classification version changed* | Re-standardization of affected versions (from DLM-9) |
| *Source structure changed* | Return to design, raised in VS-02.1 |
| *Standardization Conformed* / *Standardization Non-Conformant* | Outcome of VS-02.4 |
| *Standardized Data Registered* | Completion of VS-02.5; triggers VS-03 |

**Interaction with the supporting value streams**

| Value stream | Provides to VS-02 | Receives from VS-02 |
|---|---|---|
| VS-07 Governance and Compliance | Classification and privacy policy | Lineage and pseudonymization evidence |
| VS-08 Innovation and Methodological Development | New mapping and classification techniques | Improvement needs, such as recurring unmapped codes |
| VS-09 Infrastructure and Platform Enablement | Mapping services, reference-data connections, key management | Platform and capacity requirements |

#### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| Mapping coverage | Share of source codes mapped one-to-one to a valid standard code | Per dataset, per classification |
| Unmapped-value rate | Share of values routed to VS-03 | Per source, per cycle |
| First-time pass rate | Share of datasets passing the gate of State #2 at the first attempt | Per source, per cycle |
| Content preservation | Share of runs with identical record counts and key measures | Per run |
| Processing time | Time from raw registration to standardized registration | Per dataset, per cycle |
| Re-mapping rate | Share of datasets returned for re-mapping or design change | Per source, per cycle |

#### 10. Examples

**Survey.** Labor Force Survey returns are restructured into the canonical person and household model. Source education codes are mapped to ISCED 2011 and region codes to NUTS-3. The free-text occupation answers are listed as unmapped and handed to VS-03. The personal identifier is replaced with a pseudonymous key, and the run confirms that all records are still present.

**Administrative register.** The tax authority's activity codes are mapped to NACE Rev. 2; 0.6% have no correspondence and are flagged. Turnover stays in thousands of euro on a fiscal-year basis, and this basis is recorded as metadata. The dataset is registered as `SD-BUS-2026Q3-001`, with lineage to `RD-TAX-2026Q3-001`. When the classification steward later publishes a new correspondence table, management schedules a re-standardization of the affected versions.

**Web data.** Scraped price records are reshaped into the canonical price record. Currency, unit, and scrape time are recorded as metadata, and prices stay exactly as received. Only products with a retailer category code that has a correspondence are mapped to COICOP; the rest go to VS-03 for classification. The high unmapped rate is expected for this source and is not treated as a failure.

|**PLACEHOLDER: VS-02 maturity checklist and end-to-end scenarios to be added to the toolkit**|
|---|

### VS-03 Data Editing and Enrichment

#### 1. Purpose and value created

VS-03 is where the quality of microdata is actively improved. Standardized data still contains errors, inconsistencies, gaps, and values that have not been coded yet. VS-03 detects these problems, corrects them, fills the gaps, links sources, and derives the variables that analysis needs. Unlike VS-02, it deliberately changes values, but never silently: every change is recorded with the original value, the rule or decision, the reason, the actor, and the time. The value created is **reliability and analytical readiness**. Every estimate and publication downstream rests on the microdata this value stream produces.

![VS-03 value stream and capabilities](images/vs-03-value-stream.png)

|**PLACEHOLDER: ArchiMate view VS-03 (a) value stream and capabilities**|
|---|

#### 2. Position and state transition

VS-03 takes data from State #2 to State #3. Where a product skipped State #2, it takes data directly from State #1. It ends when a quality version passes the gate of State #3. The gate, the minimum metadata set, and the protection of State #3 are described in *State #3: Processed Data* and are not repeated here. State #3 is mandatory for all statistical production, so VS-03 runs for every product that works with microdata. It also performs the value-changing work that VS-02 deliberately left open: interpretive coding, conversion of units, currencies, and reference periods, and reconciliation between sources.

| From | To | Gate | Event out |
|---|---|---|---|
| #2 Standardized Data (or #1 Raw Data) | #3 Processed Data | Gate of State #3 (rule conformance, edit lineage, imputation flags, coding, conversion, linkage quality, derived variables, disclosure risk, reproducibility) | *Processed Data Registered* |

![VS-03 state handover and events](images/vs-03-handover.png)

|**PLACEHOLDER: ArchiMate view VS-03 (c) state handover and events**|
|---|

#### 3. Stages

| Stage | Name | Value added |
|---|---|---|
| VS-03.1 | Conduct Error Detection and Quality Diagnostics | Errors, duplicates, gaps, and outliers are known |
| VS-03.2 | Perform Data Editing and Correction | Incorrect values are corrected |
| VS-03.3 | Impute Missing or Non-Response Data | Missing values are filled with documented methods |
| VS-03.4 | Derive Additional Variables and Indicators | Data describes reality better than the source alone |
| VS-03.5 | Perform Quality Evaluation and Versioning | Quality is documented, and processed microdata is registered (State #3) |

**VS-03.1 Conduct Error Detection and Quality Diagnostics**

This stage finds out where the data is wrong, incomplete, or inconsistent. It runs consistency, range, outlier, duplicate, and completeness checks. Selective editing scores each suspected error by its likely effect on the results. Each issue receives a disposition: correct automatically, refer to an expert, or accept. No value is changed in this stage; it only diagnoses, so that effort goes to the errors that matter.

**VS-03.2 Perform Data Editing and Correction**

This stage corrects the errors found in VS-03.1. Automatic rules handle low-impact issues, and subject-matter statisticians review and correct the records that were referred to them. The stage also codes free-text values, such as occupation, to standard classifications, with review of low-confidence cases. Where linked sources disagree on a value, it applies the agreed reconciliation rule. Every change records the original value, the rule or decision, the reason, the actor, and the time, so it can be explained and reversed.

**VS-03.3 Impute Missing or Non-Response Data**

This stage fills genuine gaps in the data. It applies the approved method for each variable and pattern of missingness, such as donor, regression, or rule-based imputation, or values from an external source. Imputed values must still satisfy the editing rules. Every imputed value carries a flag and a method code, so that it can always be told apart from an observed value. Imputation never overwrites an observed value.

**VS-03.4 Derive Additional Variables and Indicators**

This stage adds the variables that analysis needs but the sources do not provide. Derived variables are computed from documented formulas and receive their own metadata and classification. The stage also converts units, currencies, and reference periods from the bases that VS-02 recorded, and stores the conversion factor next to the original value. Where sources must be combined, records are linked on the agreed keys and the linkage quality is measured. Every derivation, conversion, and link is recorded in the lineage.

**VS-03.5 Perform Quality Evaluation and Versioning**

This stage decides whether the result can become State #3. It measures the improvement in completeness and accuracy against the incoming version. It verifies that the edit lineage is complete and that the version can be reproduced from its inputs and rules. It assesses the disclosure risk of the enriched and linked data. An accepted result is registered as an immutable quality version, and the *Processed Data Registered* event is published.

#### 4. The four process types

**Design**

Design defines how data is edited, imputed, and enriched. It sets the detection and editing rules, including a selective-editing strategy that concentrates effort where it affects results. It chooses the imputation methods per variable and requires a flag on every imputed value. It specifies derived variables, coding methods for free text, and conversion rules based on the metadata from VS-02. It also designs linkage and reconciliation rules, the disclosure-risk assessment, and the policy for quality versions and the edit audit trail.

| Design process | What it delivers | Main SAF processes |
|---|---|---|
| Design error detection and editing rules | Validation rules, selective-editing strategy, error dispositions | PRD-2.5 Design processing and analysis |
| Design imputation methodology | Imputation methods, donor specifications, flagging standard | PRD-2.5 Design processing and analysis |
| Design derivation, coding, and conversion | Derived-variable catalog, coding method, conversion rules | PRD-2.2 Design variables; PRD-2.5 Design processing and analysis |
| Design linkage and reconciliation | Linkage rules, reconciliation policy, disclosure-risk assessment | PRD-2.5 Design processing and analysis; DLM-4 Classify and protect data |
| Design quality versions and audit trail | Quality criteria, versioning policy, edit audit-trail specification | DLM-1 Plan and design data assets |

**Implementation**

Implementation builds the engines that carry out the designed methods. It builds detection components and an editing engine that applies automatic corrections and routes referred records to a review workbench. It configures the imputation services, the coding service with its review queue, and the conversion routines. It builds the derivation and linkage components and the store for quality versions. Before going live, it tests whether edits improve quality without over-editing, whether a version can be reproduced exactly, and how well imputation performs on known values.

| Implementation process | What it delivers | Main SAF processes |
|---|---|---|
| Build detection and editing engines | Detection module, editing engine, review workbench | PRD-3.2 Reuse or build processing and analysis components |
| Configure imputation, coding, and conversion services | Imputation services, coding service, conversion routines | PRD-3.2 Reuse or build processing and analysis components |
| Build derivation, linkage, and versioning | Derivation and linkage components, version store, events | PRD-3.4 Configure workflows; DLM-5 Store and version data |
| Test and finalize the solution | Edit-impact, reproducibility, and imputation tests; operational procedures | PRD-3.5 Test production systems; PRD-3.6 Test statistical business process; PRD-3.7 Finalize production systems |

**Execution**

Execution runs the stages of VS-03 for every incoming version that a product needs. It starts when a *Standardized Data Registered* event arrives, or a *Raw Data Registered* event where State #2 was skipped. It also restarts when a source is redelivered or a correction arrives. Automatic steps run first; subject-matter statisticians and coding specialists handle the referred records within the production window. Execution applies the approved rules and models; a new rule or a recalibrated model goes through design.

| Aspect | VS-03 |
|---|---|
| Trigger | *Standardized Data Registered*; *Raw Data Registered* where #2 is skipped; redelivery or correction |
| Cadence | Per production cycle; preliminary and final runs where the product has both |
| Performed by | ROL-14 Data quality analyst, ROL-15 Subject-matter statistician, ROL-09 Classification steward (coding), ROL-03 Data steward |
| Input | Standardized data version (#2), unmapped-value list, approved rules and models |
| Output | Registered processed data quality version (#3), edit lineage, imputation flags |
| Control point | Gate of State #3 in VS-03.5 |
| Exception path | Re-edit or re-impute within VS-03; source problems to VS-01 and the provider; method changes back to design |

**Management**

Management watches how much is changed and whether the changes improve quality. It tracks edit rates, imputation rates, manual-review rates, and signs of over-editing. It evaluates imputation against known values and checks that no rule violations remain. It governs the versions of rules, models, and coding services, and the store of quality versions, including archiving. It reports edit auditability, disclosure risk, and methodology compliance to VS-07, and feeds improvements back to design or VS-08.

| Management process | What it delivers | Main SAF processes |
|---|---|---|
| Monitor process performance | Edit, imputation, and review rate dashboard | OVA-4 Process Data Management |
| Assess quality improvement | Accuracy and completeness improvement, imputation quality, over-editing report | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use |
| Manage methods and quality versions | Method version register, revisions, archiving | OVA-5 Knowledge Management; DLM-7 Revise data; DLM-10 Archive and preserve data |
| Report audit and compliance | Edit audit, disclosure-risk, and methodology compliance reports to VS-07 | OVA-1 Quality Management |
| Drive continuous improvement | Improvement actions fed back to design or VS-08 | PRD-8.1 Gather evaluation inputs; PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan |

#### 5. Actors and roles

VS-03 combines methodological knowledge with subject-matter expertise. Subject-matter statisticians play a larger role here than in any other primary value stream, because they judge the plausibility of individual records. The table shows the reference roles involved; specialized names in an NSI map onto them (see *Role names in the value streams*).

| Actor or role | ID | Process type | Responsibility in VS-03 |
|---|---|---|---|
| International statistical organization | ACT-07 | External | Sets methodological guidance, for example on editing and imputation |
| Process owner | ROL-01 | Management | Accountable for the performance of VS-03 |
| Data owner | ROL-02 | Management | Accountable for State #3; decides on access, reuse, and retention |
| Data steward | ROL-03 | Execution | Registers quality versions, maintains metadata, resolves gate exceptions |
| Data custodian | ROL-04 | Execution | Operates storage, access control, archiving, and key separation |
| Statistical designer | ROL-06 | Design | Specifies derived variables and indicators |
| Methodologist | ROL-07 | Design | Designs editing rules, imputation methods, and linkage rules |
| Classification steward | ROL-09 | Design, Execution | Owns coding methods and handles low-confidence coding |
| Data engineer | ROL-10 | Implementation | Builds editing, imputation, derivation, and linkage components |
| Platform engineer | ROL-11 | Implementation | Configures services, donor and reference data, and access |
| Test manager | ROL-12 | Implementation | Plans edit-impact, reproducibility, and imputation tests |
| Data quality analyst | ROL-14 | Execution | Runs detection, evaluates quality improvement |
| Subject-matter statistician | ROL-15 | Execution | Reviews and corrects referred records |
| Quality manager | ROL-18 | Management | Monitors quality improvement, leads improvements |
| Compliance officer | ROL-19 | Management | Checks disclosure risk and edit auditability |

#### 6. Capabilities, processes, and functions

VS-03 mainly draws on the capabilities 1.3.2 *Deriving variables and units*, 1.3.3 *Check content*, 1.3.4 *Adjusting and imputing*, 2.1.1 *Data lifecycle management*, 2.1.2 *Metadata management*, 2.1.3 *Statistical quality management*, 2.1.4 *Statistical register management*, and 3.3.1 *Privacy management*.

| Stage | Realized by processes | Main functions |
|---|---|---|
| VS-03.1 Conduct Error Detection and Quality Diagnostics | PRD-5.3 Review and validate | FUN-3.3 Process statistical data |
| VS-03.2 Perform Data Editing and Correction | PRD-5.4 Edit and impute; PRD-5.2 Classify and code (interpretive coding) **[VC4]** | FUN-3.3 Process statistical data |
| VS-03.3 Impute Missing or Non-Response Data | PRD-5.4 Edit and impute | FUN-3.3 Process statistical data; FUN-4.1 Manage statistical and analytical methodology |
| VS-03.4 Derive Additional Variables and Indicators | PRD-5.1 Integrate data; PRD-5.5 Derive new variables and units | FUN-3.3 Process statistical data |
| VS-03.5 Perform Quality Evaluation and Versioning | PRD-5.8 Finalize data files; DLM-2 Promote data through a quality gate; DLM-3 Register and catalog data | FUN-3.3 Process statistical data; FUN-5.2 Assure and review quality; FUN-7.3 Manage data lifecycle and storage |

![VS-03 stages, processes, and functions](images/vs-03-processes-functions.png)

|**PLACEHOLDER: ArchiMate view VS-03 (b) stages realized by processes and functions**|
|---|

#### 7. Principles

| Principle | Statement | Application in VS-03 |
|---|---|---|
| SAF-P01 | Reuse before open source, open source before buying, buying before building | Editing, imputation, and coding components are shared across products; open-source method libraries come before purchase |
| SAF-P07 | Implement loosely coupled processes and systems | Consumers work with the registered quality version, not with the editing environment |
| SAF-P08 | Data is shared property | Microdata is edited once and reused; editing the same data twice leads to statistics that do not agree |
| SAF-P09 | No data without metadata and classification | Every edit, imputation, coding, and derivation carries its rule, method, and original value |
| SAF-P10 | Security by design | The edit audit trail is tamper-evident; every change is attributable |
| SAF-P11 | Privacy by design | Linkage and enrichment are checked for re-identification risk before registration |

#### 8. Interfaces, services, and events

**Boundary interfaces**

| Boundary | Handed over | Trigger | Responsibility transfer |
|---|---|---|---|
| VS-02 → VS-03 | Registered standardized data version (#2), with unmapped values and recorded units and periods | *Standardized Data Registered* | VS-02 keeps custody; VS-03 takes responsibility for editing, coding, conversion, and enrichment |
| VS-03 → VS-04 | Registered processed data quality version (#3), with edit lineage and imputation flags | *Processed Data Registered* | VS-03 keeps custody; VS-04 takes responsibility for weighting, estimation, and analysis |

**Business services**

| Service | Offered to | Realized in | Interfaces |
|---|---|---|---|
| Editing and correction service | Statistical domains | VS-03.2 Perform Data Editing and Correction | Review workbench, edit audit query |
| Imputation service | Statistical domains | VS-03.3 Impute Missing or Non-Response Data | Imputation service, method register |
| Derivation and integration service | Statistical domains | VS-03.4 Derive Additional Variables and Indicators | Derivation catalog, linkage service |
| Processed data provisioning service | VS-04 Estimation, Analysis and Statistical Modeling, other domains, microdata services in VS-06 Dissemination and Service Delivery | VS-03.5 Perform Quality Evaluation and Versioning | Registration event, catalog query |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Standardized Data Registered* | Start of VS-03 for that version |
| *Record referred for review* | Manual adjudication in VS-03.2 |
| *Revision registered* | A new run after a redelivery or correction (DLM-7) |
| *Quality version accepted* / *Quality version insufficient* | Outcome of VS-03.5 |
| *Processed Data Registered* | Completion of VS-03.5; triggers VS-04 |

**Interaction with the supporting value streams**

| Value stream | Provides to VS-03 | Receives from VS-03 |
|---|---|---|
| VS-07 Governance and Compliance | Methodology and disclosure-risk policy | Edit audit trails, disclosure-risk assessments |
| VS-08 Innovation and Methodological Development | New editing, imputation, and coding methods | Improvement needs, such as costly manual coding |
| VS-09 Infrastructure and Platform Enablement | Processing capacity, version store | Capacity requirements |

#### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| Edit rate | Share of values changed by editing | Per variable, per cycle |
| Imputation rate | Share of values imputed | Per variable, per cycle |
| Manual-review rate | Share of records referred to experts | Per source, per cycle |
| Over-editing indicator | Share of edits with negligible effect on the results | Per cycle |
| Coding completion rate | Share of free-text values coded | Per classification, per cycle |
| Processing time | Time from incoming registration to processed registration | Per dataset, per cycle |

#### 10. Examples

**Survey.** The 42,000 free-text occupation answers from the Labor Force Survey are coded to ISCO-08: 88% automatically, the rest computer-assisted or by experts. Inconsistencies between age and labor-market status are corrected by rule or by review. Item non-response on income is imputed by regression and flagged. The quality version is registered with full lineage and VS-04 is notified.

**Administrative register.** Outliers and duplicates in the tax data are detected and corrected. Turnover is converted to units on a calendar-year basis, with the conversion factor stored. The tax data is linked to the business survey on the statistical business register key, and a reconciliation rule resolves values where the sources disagree. The linkage is checked for disclosure risk before the version `PD-BUS-2026Q3-001` is registered.

**Web data.** Products with only a free-text name are classified to COICOP by a machine-learning classifier, and low-confidence cases are reviewed. Prices are converted to euro and standard units. Missing daily prices are filled by carry-forward and flagged with a staleness indicator. Management later sees one category being misclassified repeatedly and asks VS-08 to retrain the classifier.

|**PLACEHOLDER: VS-03 maturity checklist and end-to-end scenarios to be added to the toolkit**|
|---|

### VS-04 Estimation, Analysis and Statistical Modeling

#### 1. Purpose and value created

VS-04 turns processed microdata into statistics. Up to this point, the chain improved the data itself; here it produces figures that describe a population: estimates, aggregates, indices, and model results. VS-04 does not edit microdata; it computes from it. Each result carries the method and parameters that produced it and a measure of its accuracy, such as a standard error or confidence interval. The value created is **analytical insight and statistical credibility**: figures that are representative, coherent with related statistics, and reproducible, so that they can be defended in any discussion.

![VS-04 value stream and capabilities](images/vs-04-value-stream.png)

|**PLACEHOLDER: ArchiMate view VS-04 (a) value stream and capabilities**|
|---|

#### 2. Position and state transition

VS-04 takes data from State #3 to State #4 with the status *analytical*. It ends when the results pass the analytical gate of State #4. The analytical gate, the minimum metadata set, and the protection of State #4 are described in *State #4: Statistics* and are not repeated here. State #4 has a second gate moment, the approval gate, which belongs to VS-05. VS-04 also serves internal users directly: integration systems such as the national accounts reuse analytical versions as input.

| From | To | Gate | Event out |
|---|---|---|---|
| #3 Processed Data | #4 Statistics (analytical) | Analytical gate of State #4 (approved method, weights, accuracy, model diagnostics, soundness and coherence, initial disclosure control, reproducibility, metadata) | *Output Data Registered* |

![VS-04 state handover and events](images/vs-04-handover.png)

|**PLACEHOLDER: ArchiMate view VS-04 (c) state handover and events**|
|---|

#### 3. Stages

| Stage | Name | Value added |
|---|---|---|
| VS-04.1 | Confirm Estimation and Analytical Approach | The method fits the design and the purpose |
| VS-04.2 | Apply Weighting and Calibration | Bias from sampling, non-response, and coverage is reduced |
| VS-04.3 | Estimate and Aggregate Data | Statistics and indicators are available |
| VS-04.4 | Perform Model-Based Analysis | Model-based results complement direct estimates |
| VS-04.5 | Validate and Document Results | Results are sound and documented (State #4) |

**VS-04.1 Confirm Estimation and Analytical Approach**

This stage makes sure the right method is used for the data and the purpose of the cycle. The methods themselves are designed and approved in the design process; in each cycle, this stage confirms or selects the approved approach. It checks that the calibration totals and reference sources are current and that the target parameters and domains still apply. It takes the imputation flags of State #3 into account, because they affect the accuracy approach. A new domain or a change of method goes back to design instead of being decided during the cycle.

**VS-04.2 Apply Weighting and Calibration**

This stage computes the weights that make the data represent the population. It applies design weights and adjusts them for non-response. It calibrates them to known population totals, such as age, sex, and region from the population register. The convergence of the calibration and the distribution of the weights are checked against the agreed bounds. The totals used, their source and version, and the diagnostics are recorded so the weighting can be reproduced.

**VS-04.3 Estimate and Aggregate Data**

This stage produces the statistics. It computes the target estimates with the calibrated weights and aggregates them over the agreed domains, with the agreed units and rounding. It computes the accuracy of each estimate, including the extra uncertainty caused by imputed values. Every estimate is stored with its method, weights, and accuracy measure. The result is a first, unvalidated set of statistics.

**VS-04.4 Perform Model-Based Analysis**

This stage adds results that direct estimates cannot give. It runs the approved analytical, time-series, forecasting, or small-area models. It computes their diagnostics and checks them against the agreed limits, and applies seasonal adjustment where this is part of the design. Model-based results are flagged so that users can tell them apart from direct estimates. Assumptions and limitations are documented with the results.

**VS-04.5 Validate and Document Results**

This stage decides whether the results can become State #4. It checks plausibility, internal consistency, and coherence with earlier periods and related statistics, and explains large movements. It applies the initial disclosure control, so that the results could in principle be released. It documents the methodology and quality indicators and verifies that the results can be reproduced. An accepted result is registered as an analytical version, and the *Output Data Registered* event is published.

#### 4. The four process types

**Design**

Design defines how statistics are estimated and how their accuracy is measured. It chooses the estimation strategy per source and purpose: design-based, register-based, or model-based for small domains. It specifies the weighting and calibration, including the auxiliary variables, the totals, and their authoritative source. It specifies aggregates, models, diagnostics, and seasonal adjustment. It also sets the validation criteria, the revision policy, the initial disclosure-control rules, and the policy for analytical versions.

| Design process | What it delivers | Main SAF processes |
|---|---|---|
| Design estimation strategy and accuracy | Estimation strategy, target parameters and domains, accuracy approach | PRD-2.4 Design frame and sample; PRD-2.5 Design processing and analysis |
| Design weighting and calibration | Weighting and calibration specification, weight bounds, source of totals | PRD-2.5 Design processing and analysis; DLM-9 Manage reference and master data |
| Design aggregation and models | Aggregation specification, model specification, time-series treatment | PRD-2.1 Design outputs and dissemination; PRD-2.5 Design processing and analysis |
| Design validation and initial disclosure control | Validation criteria, revision policy, disclosure-control rules | PRD-2.5 Design processing and analysis |
| Design quality measurement and versioning | Quality indicators, versioning and lineage policy | DLM-1 Plan and design data assets |

**Implementation**

Implementation builds the engines that produce and check the statistics. It builds or configures the weighting and calibration engine, with versioned connections to the register totals. It builds the estimation, variance, and aggregation components, and the environment for models and seasonal adjustment. It implements the validation checks, the disclosure-control tooling, and the store for analytical versions. Before going live, it tests whether results can be reproduced exactly and compares them with a known benchmark or earlier series.

| Implementation process | What it delivers | Main SAF processes |
|---|---|---|
| Build weighting and calibration engines | Weighting and calibration engine, versioned totals | PRD-3.2 Reuse or build processing and analysis components |
| Build estimation, variance, and aggregation | Estimation engine, variance component, aggregation pipeline | PRD-3.2 Reuse or build processing and analysis components |
| Build modeling, validation, and disclosure-control tooling | Modeling environment, validation checks, disclosure-control tooling, version store | PRD-3.2 Reuse or build processing and analysis components; PRD-3.4 Configure workflows |
| Test and finalize the solution | Reproducibility, benchmark, and accuracy tests; operational procedures | PRD-3.5 Test production systems; PRD-3.6 Test statistical business process; PRD-3.7 Finalize production systems |

**Execution**

Execution runs the stages of VS-04 for every processed version that a statistic is based on. It starts when a *Processed Data Registered* event arrives, and runs again for revised figures according to the revision policy. Weighting, estimation, and models run largely automatically; statisticians and analysts review the results and explain movements. Execution uses the approved methods and parameters; a change of method goes through design and, where needed, VS-08. The production timetable is set by the release calendar of the products that use the results.

| Aspect | VS-04 |
|---|---|
| Trigger | *Processed Data Registered*; *Calibration totals updated*; revision according to the revision policy |
| Cadence | Per production cycle; preliminary, revised, and final runs |
| Performed by | ROL-15 Subject-matter statistician (survey statistician, analyst), ROL-16 Disclosure control specialist, ROL-03 Data steward |
| Input | Processed data quality version (#3), approved methods, current calibration totals |
| Output | Registered analytical version (#4) with methodology and accuracy |
| Control point | Analytical gate of State #4 in VS-04.5 |
| Exception path | Re-estimation within VS-04; data problems back to VS-03; method changes back to design |

**Management**

Management watches the accuracy, coherence, and stability of the statistics. It tracks standard errors and coefficients of variation, coherence pass rates, and the size of revisions between preliminary and final figures. It checks that results are produced on time for the release calendar. It governs the versions of methods, models, and analytical outputs. It reports reproducibility, disclosure control, and methodology compliance to VS-07, and feeds improvements back to design or VS-08.

| Management process | What it delivers | Main SAF processes |
|---|---|---|
| Monitor process performance | Timeliness, accuracy, and reproducibility dashboard | OVA-4 Process Data Management |
| Assess output quality | Accuracy, coherence, and revision analysis | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use |
| Manage methods and analytical versions | Method version register, revisions | OVA-5 Knowledge Management; DLM-7 Revise data |
| Report audit and compliance | Reproducibility, disclosure-control, and methodology compliance reports to VS-07 | OVA-1 Quality Management |
| Drive continuous improvement | Improvement actions fed back to design or VS-08 | PRD-8.1 Gather evaluation inputs; PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan |

#### 5. Actors and roles

VS-04 is the domain of methodologists and statisticians. Its results must be defensible, so the separation between those who design methods and those who run them matters. The table shows the reference roles involved; specialized names in an NSI map onto them (see *Role names in the value streams*).

| Actor or role | ID | Process type | Responsibility in VS-04 |
|---|---|---|---|
| International statistical organization | ACT-07 | External | Sets methodological standards and guidance |
| Process owner | ROL-01 | Management | Accountable for the performance of VS-04 |
| Data owner | ROL-02 | Management | Accountable for analytical versions of State #4 |
| Data steward | ROL-03 | Execution | Registers analytical versions, maintains metadata |
| Data custodian | ROL-04 | Execution | Operates storage and access control for results |
| Statistical designer | ROL-06 | Design | Specifies outputs, domains, and models |
| Methodologist | ROL-07 | Design | Designs estimation, weighting, variance, and models |
| Data engineer | ROL-10 | Implementation | Builds weighting, estimation, and modeling components |
| Platform engineer | ROL-11 | Implementation | Configures the processing environment and access |
| Test manager | ROL-12 | Implementation | Plans reproducibility and benchmark tests |
| Subject-matter statistician | ROL-15 | Execution | Runs estimation and analysis, reviews and explains results |
| Disclosure control specialist | ROL-16 | Design, Execution | Designs and applies initial disclosure control |
| Quality manager | ROL-18 | Management | Monitors accuracy and coherence, leads improvements |
| Compliance officer | ROL-19 | Management | Checks reproducibility and methodology compliance |

#### 6. Capabilities, processes, and functions

VS-04 mainly draws on the capabilities 1.3.5 *Estimating population parameters*, 1.3.7 *Statistical disclosure*, 1.4.1 *Statistical (output) analysis*, 2.1.2 *Metadata management*, 2.1.3 *Statistical quality management*, 2.1.4 *Statistical register management*, and 2.2.3 *Methodology*.

| Stage | Realized by processes | Main functions |
|---|---|---|
| VS-04.1 Confirm Estimation and Analytical Approach | PRD-2.4 Design frame and sample; PRD-2.5 Design processing and analysis | FUN-3.1 Design and build statistical products; FUN-4.1 Manage statistical and analytical methodology |
| VS-04.2 Apply Weighting and Calibration | PRD-5.6 Calculate weights | FUN-3.4 Estimate and analyze |
| VS-04.3 Estimate and Aggregate Data | PRD-5.7 Calculate aggregates | FUN-3.4 Estimate and analyze |
| VS-04.4 Perform Model-Based Analysis | PRD-6.1 Prepare draft outputs; PRD-6.3 Interpret and explain outputs | FUN-3.4 Estimate and analyze |
| VS-04.5 Validate and Document Results | PRD-6.2 Validate outputs; PRD-6.4 Apply disclosure control (initial) **[VC5]**; OVA-2 Metadata Management | FUN-3.4 Estimate and analyze; FUN-3.5 Protect statistical confidentiality **[VC5]**; FUN-7.2 Manage metadata |

![VS-04 stages, processes, and functions](images/vs-04-processes-functions.png)

|**PLACEHOLDER: ArchiMate view VS-04 (b) stages realized by processes and functions**|
|---|

#### 7. Principles

| Principle | Statement | Application in VS-04 |
|---|---|---|
| SAF-P01 | Reuse before open source, open source before buying, buying before building | Calibration, variance, and modeling libraries are shared; open-source statistical tooling comes before purchase |
| SAF-P07 | Implement loosely coupled processes and systems | Consumers use registered analytical versions, never the estimation environment |
| SAF-P08 | Data is shared property | Integration systems reuse registered figures instead of estimating them again |
| SAF-P09 | No data without metadata and classification | Every estimate carries its method, parameters, weights, and accuracy |
| SAF-P10 | Security by design | Methods and parameters are recorded tamper-evidently, so every figure can be regenerated |
| SAF-P11 | Privacy by design | Initial disclosure control is applied before any result leaves VS-04 |

#### 8. Interfaces, services, and events

**Boundary interfaces**

| Boundary | Handed over | Trigger | Responsibility transfer |
|---|---|---|---|
| VS-03 → VS-04 | Registered processed data quality version (#3), with imputation flags | *Processed Data Registered* | VS-03 keeps custody; VS-04 takes responsibility for weighting, estimation, and analysis |
| VS-04 → VS-05 | Registered analytical version (#4) with methodology and accuracy | *Output Data Registered* | VS-04 keeps custody; VS-05 takes responsibility for composition and approval |
| VS-04 → integration systems | Registered analytical version (#4) | *Output Data Registered* | VS-04 keeps custody; the integration system takes responsibility for its own use |

**Business services**

| Service | Offered to | Realized in | Interfaces |
|---|---|---|---|
| Weighting and calibration service | Statistical domains | VS-04.2 Apply Weighting and Calibration | Calibration service, register totals |
| Estimation and aggregation service | Statistical domains | VS-04.3 Estimate and Aggregate Data | Estimation service with accuracy measures |
| Modeling and analysis service | Statistical domains, methodologists | VS-04.4 Perform Model-Based Analysis | Modeling environment, diagnostics |
| Output data provisioning service | VS-05 Statistical Product Composition, integration systems | VS-04.5 Validate and Document Results | Registration event, catalog query |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Processed Data Registered* | Start of VS-04 for that version |
| *Calibration totals updated* | Check of the approach in VS-04.1 |
| *Validation failed* | Re-estimation, or return to VS-03 |
| *Output Data Registered* | Completion of VS-04.5; triggers VS-05 |
| *Revision required* | A new run according to the revision policy |

**Interaction with the supporting value streams**

| Value stream | Provides to VS-04 | Receives from VS-04 |
|---|---|---|
| VS-07 Governance and Compliance | Methodology, revision, and disclosure-control policy | Reproducibility and disclosure-control evidence |
| VS-08 Innovation and Methodological Development | New estimation and modeling methods | Improvement needs, such as unstable small domains |
| VS-09 Infrastructure and Platform Enablement | Computing capacity, modeling environment | Capacity requirements |

#### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| On-time output rate | Share of outputs produced within the agreed window | Per output, per cycle |
| Accuracy | Standard error or coefficient of variation of key estimates | Per statistic, per cycle |
| Coherence pass rate | Share of outputs passing coherence checks at the first attempt | Per cycle |
| Revision size | Difference between preliminary and final figures | Per statistic, per cycle |
| Reproducibility rate | Share of outputs that regenerate exactly from inputs and methods | Per cycle |
| Processing time | Time from processed registration to analytical registration | Per output, per cycle |

#### 10. Examples

**Survey.** The Labor Force Survey is calibrated to population totals by age, sex, and region from a fixed version of the population register. The employment rate is estimated at 71.4%, with a 95% confidence interval of ±0.5 percentage points at national level. The variance includes the uncertainty of imputed income. Small regional cells receive initial disclosure control, and the analytical version is registered.

**Administrative register.** Turnover is aggregated by industry and region. For small domains where the direct figure is unstable, a small-area model is used, and its results are flagged as model-based. Cells dominated by one business are protected by disclosure control. The coherence check against national-accounts inputs passes, and `OD-BUS-2026Q3-001` is registered.

**Web data.** A multilateral price index is calculated from the item prices in State #3, taking into account that some daily prices were carried forward. New products are chained in according to the approved rule. The index is checked against the movement of the official consumer price index. Management later asks VS-08 to evaluate a longer index window.

|**PLACEHOLDER: VS-04 maturity checklist and end-to-end scenarios to be added to the toolkit**|
|---|

### VS-05 Statistical Product Composition

#### 1. Purpose and value created

VS-05 turns separate statistics into finished products. A single estimate is not yet something a user reads. VS-05 brings results from different domains, sources, and periods together into publications, time series, indices, and datasets, and approves them for release. It does not estimate anything again: it selects, combines, checks, explains, and signs off. The value created is **coherence and interpretability**: products that are consistent internally and with related statistics, carry the accuracy of their components, and come with the explanation users need.

![VS-05 value stream and capabilities](images/vs-05-value-stream.png)

|**PLACEHOLDER: ArchiMate view VS-05 (a) value stream and capabilities**|
|---|

#### 2. Position and state transition

VS-05 works within State #4. It takes analytical versions and produces approved versions of the same state. It ends when a product passes the approval gate of State #4. The approval gate and the metadata of approved versions are described in *State #4: Statistics* and are not repeated here. Approval never changes an analytical version: it creates a new, immutable version with the status *approved* that refers to the components it was built from. A product that consists of a single analytical result still passes VS-05, because approval and explanation are always needed before release.

| From | To | Gate | Event out |
|---|---|---|---|
| #4 Statistics (analytical) | #4 Statistics (approved) | Approval gate of State #4 (component selection, composition, consistency and coherence, interpretive content, dissemination and confidentiality standards, sign-off) | *Statistical Product Registered* |

![VS-05 state handover and events](images/vs-05-handover.png)

|**PLACEHOLDER: ArchiMate view VS-05 (c) state handover and events**|
|---|

#### 3. Stages

| Stage | Name | Value added |
|---|---|---|
| VS-05.1 | Select and Integrate Source Datasets | Relevant results are brought together |
| VS-05.2 | Construct Composite Indicators or Indices | Indices, ratios, and aggregates are available |
| VS-05.3 | Perform Consistency and Coherence Checks | The product is internally consistent |
| VS-05.4 | Generate Analytical and Interpretive Outputs | Results are explained and visualized |
| VS-05.5 | Approve and Register Statistical Products | The product is approved for release (State #4, approved) |

**VS-05.1 Select and Integrate Source Datasets**

This stage brings together the results a product needs. It selects the exact analytical versions per domain, period, and breakdown, according to the product specification. It pins those versions, so the product can always be traced to the figures it used. It combines them into the structure of the product. The accuracy and methodology metadata of each component travels with it.

**VS-05.2 Construct Composite Indicators or Indices**

This stage computes the measures that the product presents. It calculates indicators, ratios, and indices according to their documented formulas and weights. It builds time series by chaining, linking, and benchmarking. Each composite receives an accuracy measure derived from its components. Components are used exactly as received; nothing is estimated again.

**VS-05.3 Perform Consistency and Coherence Checks**

This stage checks whether the product holds together. Totals must equal the sum of their parts, and breakdowns must add up. The product is compared with related statistics, such as the national accounts, and with earlier releases, within agreed tolerances. A discrepancy is accepted with an explanation, flagged, or returned to VS-04. A component estimate is never adjusted in VS-05 to make a check pass.

**VS-05.4 Generate Analytical and Interpretive Outputs**

This stage makes the product understandable. Subject-matter statisticians write the commentary and the key messages, supported by tables and visualizations. The text must be neutral and must not overstate movements that fall within the margin of error. Content follows the product templates and the accessibility and plain-language standards. An editorial review checks the content against the data and its accuracy.

**VS-05.5 Approve and Register Statistical Products**

This stage signs off the product. It checks the product against the dissemination and confidentiality standards, including the risk that combining results reveals information that each result alone does not. The designated approval authority decides. An approved product is registered as a new, immutable version with its components, method, coherence results, and approval record. The stage then publishes the *Statistical Product Registered* event.

#### 4. The four process types

**Design**

Design defines the products and how they are built. It specifies each product: purpose, users, content, structure, breakdowns, release frequency, and the components it uses. It specifies composite indicators, indices, and time series, including how uncertainty is shown. It designs the consistency and coherence checks with their tolerances, and the revision policy for products. It also designs the content templates, the editorial review, the approval workflow, and the confidentiality standards for combined results.

| Design process | What it delivers | Main SAF processes |
|---|---|---|
| Design the product portfolio | Product specifications, component selection rules | PRD-2.1 Design outputs and dissemination |
| Design composite indicators and indices | Indicator and index specifications, time-series rules | PRD-2.5 Design processing and analysis |
| Design consistency and coherence checks | Check set, tolerances, revision policy | PRD-2.5 Design processing and analysis |
| Design interpretive content | Content templates, visualization standards, editorial review | PRD-2.1 Design outputs and dissemination |
| Design approval, confidentiality, and versioning | Approval workflow, confidentiality standard, versioning policy | PRD-2.1 Design outputs and dissemination; DLM-1 Plan and design data assets |

**Implementation**

Implementation builds the tooling that assembles, checks, and approves products. It builds the composition components, with pinned connections to the registered analytical versions. It builds the calculators for indicators, indices, and time series. It implements the coherence checks, the content and visualization tooling, the approval workflow, and the store for approved versions. Before going live, it tests that composites reconcile to their components and that a product can be rebuilt exactly from its components and method.

| Implementation process | What it delivers | Main SAF processes |
|---|---|---|
| Build composition components | Composition engine, pinned component connections | PRD-3.2 Reuse or build processing and analysis components |
| Build indicator and time-series engines | Indicator, index, and time-series calculators | PRD-3.2 Reuse or build processing and analysis components |
| Build coherence, content, and approval tooling | Coherence checks, content tooling, approval workflow, version store | PRD-3.3 Reuse or build dissemination components; PRD-3.4 Configure workflows |
| Test and finalize the solution | Coherence and reproducibility tests, operational procedures | PRD-3.5 Test production systems; PRD-3.6 Test statistical business process; PRD-3.7 Finalize production systems |

**Execution**

Execution runs the stages of VS-05 for every product release. It starts when the analytical versions a product needs are registered, signaled by *Output Data Registered*. The timetable is set by the release calendar: approval must be complete before the release slot. Composition and checks run largely automatically; subject-matter statisticians write the content and the approval authority signs off. Execution follows the product specification; a new product or a change in a composite goes through design.

| Aspect | VS-05 |
|---|---|
| Trigger | *Output Data Registered* for the required components; the release calendar |
| Cadence | Per product release |
| Performed by | ROL-15 Subject-matter statistician (author), ROL-17 Release manager (approval authority), ROL-16 Disclosure control specialist, ROL-03 Data steward |
| Input | Analytical versions (#4), product specification, content templates |
| Output | Registered approved version (#4) with component lineage and approval record |
| Control point | Approval gate of State #4 in VS-05.5 |
| Exception path | Discrepant components back to VS-04; content revision within VS-05; product changes back to design |

**Management**

Management watches whether products are coherent, understandable, and on time. It tracks coherence pass rates, the number of approval rounds, and timeliness against the release calendar. It reviews the clarity of commentary and visualizations, partly based on user feedback from VS-06 and VS-10. It governs the versions of products, indicators, and templates, including rebasing of indices. It reports reproducibility, approval, and confidentiality compliance to VS-07, and feeds improvements back to design.

| Management process | What it delivers | Main SAF processes |
|---|---|---|
| Monitor process performance | Coherence, approval, and timeliness dashboard | OVA-4 Process Data Management |
| Assess product quality | Coherence and interpretability review | OVA-1 Quality Management |
| Manage products and approved versions | Product version register, rebasing, revisions | OVA-2 Metadata Management; DLM-7 Revise data |
| Report audit and compliance | Reproducibility, approval, and confidentiality reports to VS-07 | OVA-1 Quality Management |
| Drive continuous improvement | Improvement actions fed back to design | PRD-8.1 Gather evaluation inputs; PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan |

#### 5. Actors and roles

VS-05 brings together product owners, authors, and approvers. The work is often organized in the collaboration COL-05 *Statistical product team*, in which design, methodology, and subject-matter roles work together. The table shows the reference roles involved; specialized names in an NSI map onto them (see *Role names in the value streams*).

| Actor or role | ID | Process type | Responsibility in VS-05 |
|---|---|---|---|
| International statistical organization | ACT-07 | External | Sets product and index standards, such as SDMX and index manuals |
| Process owner | ROL-01 | Management | Accountable for the performance of VS-05 |
| Data owner | ROL-02 | Management | Accountable for approved versions of State #4 |
| Data steward | ROL-03 | Execution | Registers approved versions, maintains metadata |
| Data custodian | ROL-04 | Execution | Operates storage, access control, and the pre-release access log |
| Statistical designer | ROL-06 | Design | Designs products and coherence checks |
| Methodologist | ROL-07 | Design | Designs indicators, indices, and time-series methods |
| Data engineer | ROL-10 | Implementation | Builds composition, indicator, and content tooling |
| Platform engineer | ROL-11 | Implementation | Configures composition services and access |
| Test manager | ROL-12 | Implementation | Plans coherence and reproducibility tests |
| Subject-matter statistician | ROL-15 | Execution | Writes commentary, key messages, and visualizations |
| Disclosure control specialist | ROL-16 | Execution | Checks the confidentiality of the combined product |
| Release manager | ROL-17 | Execution | Acts as approval authority and plans approval against the release calendar |
| Quality manager | ROL-18 | Management | Monitors coherence and interpretability |
| Compliance officer | ROL-19 | Management | Checks approval and confidentiality compliance |

#### 6. Capabilities, processes, and functions

VS-05 mainly draws on the capabilities 1.3.6 *Integrate statistics*, 1.3.7 *Statistical disclosure*, 1.4.1 *Statistical (output) analysis*, 1.5.4 *Statistical information management*, 2.1.2 *Metadata management*, and 2.1.3 *Statistical quality management*.

| Stage | Realized by processes | Main functions |
|---|---|---|
| VS-05.1 Select and Integrate Source Datasets | PRD-5.1 Integrate data; PRD-6.1 Prepare draft outputs | FUN-3.4 Estimate and analyze |
| VS-05.2 Construct Composite Indicators or Indices | PRD-5.5 Derive new variables and units; PRD-5.7 Calculate aggregates | FUN-3.3 Process statistical data; FUN-3.4 Estimate and analyze |
| VS-05.3 Perform Consistency and Coherence Checks | PRD-6.2 Validate outputs | FUN-3.4 Estimate and analyze; FUN-5.2 Assure and review quality |
| VS-05.4 Generate Analytical and Interpretive Outputs | PRD-6.3 Interpret and explain outputs; PRD-7.2 Produce dissemination products | FUN-3.4 Estimate and analyze; FUN-3.6 Disseminate statistics |
| VS-05.5 Approve and Register Statistical Products | PRD-6.4 Apply disclosure control; PRD-6.5 Finalize outputs; DLM-3 Register and catalog data | FUN-3.4 Estimate and analyze; FUN-3.5 Protect statistical confidentiality; FUN-7.2 Manage metadata |

![VS-05 stages, processes, and functions](images/vs-05-processes-functions.png)

|**PLACEHOLDER: ArchiMate view VS-05 (b) stages realized by processes and functions**|
|---|

#### 7. Principles

| Principle | Statement | Application in VS-05 |
|---|---|---|
| SAF-P01 | Reuse before open source, open source before buying, buying before building | Templates, index calculators, and visualization tooling are shared across products |
| SAF-P07 | Implement loosely coupled processes and systems | VS-05 uses registered analytical versions only, and VS-06 uses registered approved versions only |
| SAF-P08 | Data is shared property | Products reuse validated results instead of producing their own variants |
| SAF-P09 | No data without metadata and classification | Every product carries its components, their accuracy, the composition method, and the approval record |
| SAF-P10 | Security by design | The approval record is tamper-evident; pre-release access is logged |
| SAF-P11 | Privacy by design | The confidentiality check covers the risk of combining results, not only each result alone |

#### 8. Interfaces, services, and events

**Boundary interfaces**

| Boundary | Handed over | Trigger | Responsibility transfer |
|---|---|---|---|
| VS-04 → VS-05 | Registered analytical versions (#4) | *Output Data Registered* | VS-04 keeps custody; VS-05 takes responsibility for composition and approval |
| VS-05 → VS-06 | Registered approved version (#4) | *Statistical Product Registered* | VS-05 keeps custody; VS-06 takes responsibility for final disclosure control, release, and user support |

**Business services**

| Service | Offered to | Realized in | Interfaces |
|---|---|---|---|
| Composition service | Product teams | VS-05.1 Select and Integrate Source Datasets; VS-05.2 Construct Composite Indicators or Indices | Composition engine, catalog query |
| Coherence validation service | Product teams, quality manager | VS-05.3 Perform Consistency and Coherence Checks | Coherence reports |
| Analytical content service | Product teams, VS-06 Dissemination and Service Delivery | VS-05.4 Generate Analytical and Interpretive Outputs | Content and visualization tooling |
| Product provisioning service | VS-06 Dissemination and Service Delivery | VS-05.5 Approve and Register Statistical Products | Registration event, catalog query |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Output Data Registered* | Availability of a component for VS-05.1 |
| *Coherence discrepancy found* | Explanation, flag, or return to VS-04 |
| *Product approved* / *Product not approved* | Outcome of VS-05.5 |
| *Statistical Product Registered* | Completion of VS-05.5; triggers VS-06 |

**Interaction with the supporting value streams**

| Value stream | Provides to VS-05 | Receives from VS-05 |
|---|---|---|
| VS-07 Governance and Compliance | Approval and confidentiality policy | Approval records, reproducibility evidence |
| VS-08 Innovation and Methodological Development | New indicator and visualization methods | Improvement needs |
| VS-10 Customer and Stakeholder Engagement | User needs for products and content | Product changes for communication |

#### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| On-time product rate | Share of products approved before their release slot | Per product, per cycle |
| Coherence pass rate | Share of products passing coherence checks at the first attempt | Per product, per cycle |
| Approval rounds | Number of approval rounds before sign-off | Per product, per cycle |
| Component reuse | Share of products built only from registered results | Per cycle |
| Reproducibility rate | Share of products that rebuild exactly from components and method | Per cycle |

#### 10. Examples

**Survey.** The quarterly labor market product combines the Labor Force Survey estimates with unemployment and vacancy figures. The confidence intervals of the components are carried into the tables. The commentary explains a rise of 0.3 percentage points in the employment rate and states that it falls within the margin of error. The product is approved in one round and registered.

**Administrative register.** The business statistics product combines register-based and survey-based figures for the same industries and regions. Industry totals reconcile with the published total. One domain exceeds the coherence tolerance and is returned to VS-04 instead of being adjusted. After the corrected analytical version arrives, the product is approved as `SP-BUS-2026Q3-001`.

**Web data.** The headline price index and its main divisions are composed from the item indices with the period weights. The product is checked against the previous month and year. The commentary explains the main contributions to the monthly change. Because the index is market-sensitive, access to the approved version is restricted and logged until release.

|**PLACEHOLDER: VS-05 maturity checklist and end-to-end scenarios to be added to the toolkit**|
|---|

### VS-06 Dissemination and Service Delivery

#### 1. Purpose and value created

VS-06 is the exit point of the statistical value chain. It takes approved products and makes them available to users through trusted channels: publications, open data, APIs, dashboards, deliveries to international organizations, and controlled access to microdata for researchers. Before anything is released, it applies the final disclosure check, which is the last line of protection for respondents. It also supports users in finding and interpreting the statistics, and learns from how they are used. The value created is **impact and accessibility**: statistics that reach every user at the same moment, can be trusted, and are used correctly.

![VS-06 value stream and capabilities](images/vs-06-value-stream.png)

|**PLACEHOLDER: ArchiMate view VS-06 (a) value stream and capabilities**|
|---|

#### 2. Position and state transition

VS-06 takes data from State #4 with the status *approved* to State #5. Once users have the data, it becomes consumed data, boundary position #6, outside the NSI's control. The release gate, the minimum metadata set, and the protection of State #5 are described in *State #5: Released Data* and are not repeated here. Unlike the earlier gates, the release gate allows no conditional acceptance on confidentiality. VS-06 has no downstream production stream; its feedback goes to VS-10 and, through VS-10, into the design of the whole chain.

| From | To | Gate | Event out |
|---|---|---|---|
| #4 Statistics (approved) | #5 Released Data | Release gate of State #5 (approved source, final disclosure control, de-identification, documentation, format and accessibility, release authorization, timing and equal access) | *Statistics Released* |

![VS-06 state handover and events](images/vs-06-handover.png)

|**PLACEHOLDER: ArchiMate view VS-06 (c) state handover and events**|
|---|

#### 3. Stages

| Stage | Name | Value added |
|---|---|---|
| VS-06.1 | Plan Dissemination and Access Strategy | Target users, channels, and formats are set |
| VS-06.2 | Prepare Data for Dissemination | Output is disclosure-safe and in the right format |
| VS-06.3 | Publish and Provide Access Services | Users can find and access the output (State #5) |
| VS-06.4 | Support and Engage Users | Users understand and use the output correctly |
| VS-06.5 | Monitor Usage and Feedback | The NSI knows how its output is used |

**VS-06.1 Plan Dissemination and Access Strategy**

This stage confirms how a product will reach its users. The dissemination strategy is designed in advance; in each cycle, this stage confirms the channels, formats, and release slot for the product. It checks the embargo arrangements, such as pre-release access for accredited media under agreement. It confirms the target users and the communication plan, together with VS-10. A new channel or a change of policy goes back to design instead of being decided during the release.

**VS-06.2 Prepare Data for Dissemination**

This stage makes the product safe and ready for each channel. It applies the final disclosure control to tables and dashboards, beyond the protection applied earlier in the chain. It de-identifies microdata that is released to researchers, according to the standard for that channel. The release must meet the disclosure-risk criteria; if it does not, it is returned for more protection and nothing is released. The product is then formatted for each channel and packaged with its documentation and metadata.

**VS-06.3 Publish and Provide Access Services**

This stage releases the product. It publishes through all agreed channels at the same moment: website, open data, API, and dashboard. It delivers data to international organizations under their transmission programs, publishes offerings in data spaces, and provides access for accredited researchers in a secure processing environment. No user gets the data before the release time, except under the embargo policy. Every release is recorded as an immutable version, and the *Statistics Released* event is published.

**VS-06.4 Support and Engage Users**

This stage helps users use the statistics correctly. Documentation, methodology notes, and user guidance are available with every release. A helpdesk answers questions and, for researchers, handles the checking of output that leaves the secure environment. Where a published figure turns out to be wrong, an erratum is issued according to the correction policy. Promotion and outreach take place together with VS-10.

**VS-06.5 Monitor Usage and Feedback**

This stage learns from how the statistics are used. It tracks use across channels, such as downloads, API calls, and dashboard views. It collects satisfaction and feedback from users. It analyzes reach, value, and unmet needs. The findings go to the design of VS-06, to VS-10, and through VS-10 to the rest of the chain.

#### 4. The four process types

**Design**

Design defines who is served, how, and under which protection. It sets the dissemination strategy per user group: channels, formats, release calendar, and embargo policy. It designs the final disclosure-control rules and the de-identification standard per channel, for example more detail only in a secure processing environment. It specifies formats, APIs, dashboards, accessibility standards, and the documentation that must accompany every release. It also designs user support, the feedback model, the correction policy, and the governance of releases.

| Design process | What it delivers | Main SAF processes |
|---|---|---|
| Design the dissemination and access strategy | User segments, channel and format strategy, release calendar, embargo policy | PRD-2.1 Design outputs and dissemination |
| Design final disclosure control and de-identification | Release disclosure rules, de-identification standard, disclosure-risk criteria | PRD-2.5 Design processing and analysis |
| Design channels, formats, and documentation | Format and accessibility standards, API and dataset specifications, documentation standard | PRD-2.1 Design outputs and dissemination; PRD-2.6 Design production systems and workflows |
| Design user support and feedback | Support model, communication plan, feedback model, correction policy | PRD-2.1 Design outputs and dissemination |
| Design release governance | Release authorization, equal-access controls, versioning policy | PRD-2.1 Design outputs and dissemination; DLM-1 Plan and design data assets |

**Implementation**

Implementation builds the channels and the release tooling, on the platforms provided by VS-09. It builds or configures the website, open-data and API services, dashboards, and the secure processing environment for researchers. It configures the disclosure-control tooling and the release tooling that enforces timing, embargo, and equal access. It builds the documentation, helpdesk, and usage-monitoring services, and the store for release versions. Before going live, it tests accessibility, security, and disclosure control, and rehearses the release itself.

| Implementation process | What it delivers | Main SAF processes |
|---|---|---|
| Build publication and access channels | Website, open data, API, dashboards, secure processing environment | PRD-3.3 Reuse or build dissemination components; MDS-4 Provide a secure processing environment |
| Configure disclosure-control and release tooling | Final disclosure-control tooling, release and embargo tooling | PRD-3.3 Reuse or build dissemination components; PRD-3.4 Configure workflows |
| Build documentation, support, and monitoring | Documentation services, helpdesk, usage monitoring, release store | PRD-3.3 Reuse or build dissemination components |
| Test and finalize the solution | Accessibility, security, and disclosure tests; release rehearsal; operational procedures | PRD-3.5 Test production systems; PRD-3.6 Test statistical business process; PRD-3.7 Finalize production systems |

**Execution**

Execution runs the stages of VS-06 for every release. It starts when a *Statistical Product Registered* event arrives, and the release itself takes place at the slot in the release calendar. Preparation and the final disclosure check must be complete before that slot. User support and usage monitoring continue after the release, for as long as the product is available. Execution follows the agreed strategy and policies; a new channel or a deviation from the calendar goes through design and VS-07.

| Aspect | VS-06 |
|---|---|
| Trigger | *Statistical Product Registered*; the release slot in the release calendar; research access requests |
| Cadence | Per release; continuous for user support and monitoring |
| Performed by | ROL-17 Release manager, ROL-16 Disclosure control specialist, ROL-22 Dissemination and service manager, ROL-03 Data steward |
| Input | Approved version (#4), release plan, channel templates |
| Output | Released data version (#5) in all channels, documentation, usage data |
| Control point | Release gate of State #5 in VS-06.2 and VS-06.3 |
| Exception path | Failed disclosure check: return for more protection; errors after release: erratum via a new approved version from VS-05 |

**Management**

Management watches whether releases are punctual, accessible, and safe, and whether they are used. It tracks release punctuality, the first-time pass rate of the disclosure check, channel availability, use, and user satisfaction. It assesses the accessibility and clarity of releases. It governs the life cycle of channels, formats, and release versions, including errata and archiving. It reports disclosure, equal-access, and accessibility compliance to VS-07, and feeds improvements back to design and to VS-10.

| Management process | What it delivers | Main SAF processes |
|---|---|---|
| Monitor process performance | Punctuality, availability, and use dashboard | OVA-4 Process Data Management |
| Assess dissemination quality | Accessibility, punctuality, reach, and clarity reports | OVA-1 Quality Management |
| Manage releases and channels | Channel version register, errata, archiving | DLM-7 Revise data; DLM-10 Archive and preserve data |
| Report audit and compliance | Disclosure, equal-access, and accessibility reports to VS-07 | OVA-1 Quality Management; MDS-8 Monitor use and compliance |
| Drive continuous improvement | Improvement actions fed back to design and VS-10 | PRD-8.1 Gather evaluation inputs; PRD-8.2 Conduct evaluation; PRD-8.3 Agree an action plan |

#### 5. Actors and roles

VS-06 is where the NSI meets its users. Research access is organized in the collaboration COL-04 *Research access partnership*. The table shows the actors and reference roles involved; specialized names in an NSI map onto them (see *Role names in the value streams*).

| Actor or role | ID | Process type | Responsibility in VS-06 |
|---|---|---|---|
| Data user | ACT-05 | External | Uses released statistics: policy makers, researchers, media, businesses, the public |
| International statistical organization | ACT-07 | External | Receives deliveries under transmission programs |
| Supervisory and legal authority | ACT-08 | External | Oversees confidentiality and equal access |
| Process owner | ROL-01 | Management | Accountable for the performance of VS-06 |
| Data owner | ROL-02 | Management | Accountable for State #5, including access for researchers |
| Data steward | ROL-03 | Execution | Registers release versions, maintains documentation, handles errata |
| Data custodian | ROL-04 | Execution | Operates channels, access control, integrity protection, and the embargo log |
| Data engineer | ROL-10 | Implementation | Builds publication, API, and dashboard services |
| Platform engineer | ROL-11 | Implementation | Configures channels and the secure processing environment |
| Test manager | ROL-12 | Implementation | Plans accessibility and security tests and release rehearsals |
| Disclosure control specialist | ROL-16 | Design, Execution | Designs and signs off the final disclosure control and output checking |
| Release manager | ROL-17 | Execution | Controls release timing, embargo, and equal access |
| Quality manager | ROL-18 | Management | Monitors punctuality, accessibility, and clarity |
| Compliance officer | ROL-19 | Management | Checks disclosure and equal-access compliance |
| Security officer | ROL-20 | Management | Assures the security of channels and research environments |
| Dissemination and service manager | ROL-22 | Design, Execution | Manages channels, formats, service levels, and research access |
| Relationship manager | ROL-23 | Execution | Handles user relationships, promotion, and feedback with VS-10 |

#### 6. Capabilities, processes, and functions

VS-06 mainly draws on the capabilities 1.3.7 *Statistical disclosure*, 1.5.1 *Publication management*, 1.5.2 *Promotion to use*, 1.5.3 *Facilitate data access*, 1.5.4 *Statistical information management*, 2.2.4 *Data services*, 3.4.1 *Services management*, and 3.4.4 *Self-service*.

| Stage | Realized by processes | Main functions |
|---|---|---|
| VS-06.1 Plan Dissemination and Access Strategy | PRD-2.1 Design outputs and dissemination | FUN-3.1 Design and build statistical products; FUN-3.6 Disseminate statistics |
| VS-06.2 Prepare Data for Dissemination | PRD-6.4 Apply disclosure control (final); PRD-7.1 Update output systems | FUN-3.5 Protect statistical confidentiality; FUN-3.6 Disseminate statistics |
| VS-06.3 Publish and Provide Access Services | PRD-7.2 Produce dissemination products; PRD-7.3 Release dissemination products; MDS-1 Authorize institutions and researchers; MDS-2 Assess access applications; MDS-3 Prepare research datasets; MDS-4 Provide a secure processing environment; MDS-5 Facilitate privacy-preserving analysis; MDS-7 Check and release output; DSP-2 Publish data offerings | FUN-3.6 Disseminate statistics; FUN-8.1 Manage research access; FUN-8.2 Prepare research data; FUN-8.3 Operate secure research environments; FUN-8.4 Control research output; FUN-8.5 Enable privacy-preserving analysis; FUN-9.1 Manage data space participation |
| VS-06.4 Support and Engage Users | PRD-7.4 Promote dissemination products; PRD-7.5 Provide user support; MDS-6 Support researchers | FUN-3.6 Disseminate statistics; FUN-8.3 Operate secure research environments; FUN-10.9 Manage users and services |
| VS-06.5 Monitor Usage and Feedback | PRD-8.1 Gather evaluation inputs; MDS-8 Monitor use and compliance; MDS-9 Close projects | FUN-8.1 Manage research access; FUN-8.3 Operate secure research environments; FUN-10.9 Manage users and services |

![VS-06 stages, processes, and functions](images/vs-06-processes-functions.png)

|**PLACEHOLDER: ArchiMate view VS-06 (b) stages realized by processes and functions**|
|---|

#### 7. Principles

| Principle | Statement | Application in VS-06 |
|---|---|---|
| SAF-P01 | Reuse before open source, open source before buying, buying before building | Channels, APIs, and dashboards are shared across products; open-source dissemination tooling comes before purchase |
| SAF-P07 | Implement loosely coupled processes and systems | VS-06 uses approved versions only and offers released data through stable, versioned services |
| SAF-P08 | Data is shared property | Released data is offered as openly as confidentiality allows, in standard formats with clear terms of use |
| SAF-P09 | No data without metadata and classification | Every release carries its documentation, methodology notes, and reference metadata |
| SAF-P10 | Security by design | Channels protect the integrity of released data; research environments control what enters and leaves |
| SAF-P11 | Privacy by design | Final disclosure control and de-identification are a hard gate before release |

#### 8. Interfaces, services, and events

**Boundary interfaces**

| Boundary | Handed over | Trigger | Responsibility transfer |
|---|---|---|---|
| VS-05 → VS-06 | Registered approved version (#4) | *Statistical Product Registered* | VS-05 keeps custody; VS-06 takes responsibility for final disclosure control, release, and user support |
| VS-06 → users and society | Released data version (#5) in its channels | *Statistics Released* | The NSI remains responsible for correctness, documentation, and errata; users are responsible for their own use (#6) |

**Business services**

| Service | Offered to | Realized in | Interfaces |
|---|---|---|---|
| Publication and open data service | The public, media, businesses, policy makers | VS-06.3 Publish and Provide Access Services | Website, open-data portal |
| API and dashboard service | Developers, analysts, researchers | VS-06.3 Publish and Provide Access Services | SDMX API, dashboards |
| International transmission service | International statistical organizations | VS-06.3 Publish and Provide Access Services | Agreed transmission channels and formats |
| Secure research access service | Accredited researchers | VS-06.3 Publish and Provide Access Services | Secure processing environment with output checking |
| User support service | All users | VS-06.4 Support and Engage Users | Helpdesk, documentation, training |
| Usage and feedback service | Process owners, VS-10 Customer and Stakeholder Engagement | VS-06.5 Monitor Usage and Feedback | Usage statistics, feedback channels |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Statistical Product Registered* | Start of VS-06 for that product |
| *Release slot reached* | Publication in VS-06.3 |
| *Disclosure check failed* | Return for more protection in VS-06.2 |
| *Statistics Released* | Completion of VS-06.3 |
| *Erratum issued* | Correction of a released figure, after a new approved version |
| *Feedback received* | Analysis in VS-06.5 and routing to VS-10 |

**Interaction with the supporting value streams**

| Value stream | Provides to VS-06 | Receives from VS-06 |
|---|---|---|
| VS-07 Governance and Compliance | Confidentiality, equal-access, and accessibility policy | Disclosure and equal-access evidence |
| VS-09 Infrastructure and Platform Enablement | Portals, APIs, dashboards, secure processing environments | Channel and capacity requirements |
| VS-10 Customer and Stakeholder Engagement | User needs, communication, relationships | Usage data, satisfaction, feedback |

#### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| Release punctuality | Share of releases published exactly at their calendar slot | Per release, per cycle |
| Disclosure first-time pass rate | Share of releases passing the final disclosure check at the first attempt | Per release, per cycle |
| Channel availability | Availability of APIs and access services | Per channel, per month |
| Use | Downloads, API calls, and dashboard views | Per release, per channel |
| User satisfaction | Satisfaction score from user feedback | Per cycle |
| Support response time | Time to resolve user questions | Per month |

#### 10. Examples

**Survey.** The quarterly labor market figures are released at 09:00 on the calendar date, at the same moment on the website, the API, and the dashboard. Two small regional cells are suppressed in the final disclosure check. Accredited media received an embargoed copy and publish at the same moment. User feedback shows confusion about the confidence interval, and a plain-language explanation is added for the next release.

**Administrative register.** Aggregated business statistics are published as open data. De-identified business microdata is made available to accredited researchers in the secure processing environment, with project-specific pseudonyms. Researchers receive the data dictionary and methodology notes. Their results leave the environment only after an output check.

**Web data.** The monthly price index is released at a fixed minute with strict equal access, because it is market-sensitive. The documentation explains the main contributions to the monthly change. Use on release day is monitored, and the dashboard reaches its highest number of views. Users ask for a breakdown by region, and VS-10 routes the request to design.

|**PLACEHOLDER: VS-06 maturity checklist and end-to-end scenarios to be added to the toolkit**|
|---|

## Supporting value streams

### VS-07 Governance and Compliance

#### 1. Purpose and value created

VS-07 makes sure that every process, dataset, and product in the NSI operates under clear rules and clear accountability. It sets the frameworks and policies for data, metadata, ethics, confidentiality, and quality. It translates legislation into procedures, assigns data-governance roles, and checks that the rules are followed. It provides assurance to management, supervisory authorities, and the public that official statistics can be trusted. The value created is **integrity and accountability**: the NSI can show, at any moment, that it acts lawfully, ethically, and with sound methods. Without VS-07, each value stream would interpret the rules on its own, and compliance would depend on individual judgment.

![VS-07 value stream and capabilities](images/vs-07-value-stream.png)

|**PLACEHOLDER: ArchiMate view VS-07 (a) value stream and capabilities**|
|---|

#### 2. Relation to the chain

VS-07 does not move data from one state to the next. It runs across the whole chain and governs the rules that every value stream and every state must follow. The quality gates of the states are its main instrument: VS-07 sets the policies behind them, and the primary value streams apply them. In return, every value stream delivers evidence to VS-07, such as audit trails, quality indicators, and compliance reports. VS-07 runs continuously, with periodic audits and reviews.

| Touch point | Where in the chain | What happens |
|---|---|---|
| Policies and rules | All value streams | VS-07 sets the frameworks that design processes must follow |
| Quality gates | Gates of States #1 to #5 | VS-07 sets the legal, confidentiality, and quality criteria behind each gate |
| Compliance evidence | Management process type of every value stream | Value streams report audit trails, indicators, and incidents to VS-07 |
| Method approval | Transfer gate of VS-08 (VS-08.5) | VS-07 assesses new methods against compliance criteria before production |
| External assurance | Supervisory authorities, peers, the public | VS-07 reports compliance and obtains certification |

![VS-07 relation to the value chain](images/vs-07-relation.png)

|**PLACEHOLDER: ArchiMate view VS-07 (c) relation to the value chain**|
|---|

#### 3. Stages

| Stage | Name | Value added |
|---|---|---|
| VS-07.1 | Define Governance Frameworks and Policies | Rules for data, metadata, ethics, confidentiality, and quality are set |
| VS-07.2 | Establish Legal and Regulatory Compliance Mechanisms | Applicable rules are known and translated into procedures |
| VS-07.3 | Implement Data and Metadata Governance | Ownership, stewardship, and lineage are assigned |
| VS-07.4 | Monitor Quality and Compliance Indicators | Quality and compliance status is visible |
| VS-07.5 | Audit, Certify and Report Compliance | Compliance is demonstrated |
| VS-07.6 | Update and Improve Governance Mechanisms | Governance keeps up with new rules and lessons learned |

**VS-07.1 Define Governance Frameworks and Policies**

This stage sets the rulebook of the NSI. It defines the policies for data, metadata, ethics, statistical confidentiality, and quality. It aligns them with international frameworks, such as the UN Fundamental Principles of Official Statistics and the European Statistics Code of Practice. It decides which policies apply to all value streams and which apply to specific states or processes. The result is a policy set that every design process can refer to.

**VS-07.2 Establish Legal and Regulatory Compliance Mechanisms**

This stage translates legislation into concrete procedures. It identifies the applicable laws, such as the national statistics act, the GDPR, and archives legislation, and records them in the legal register. For each provision, it records whether it leads to a driver, constraint, requirement, or principle (see *Legislation and regulation* in the Reading guide). It defines the procedures that keep processes within the law, such as privacy impact assessments and records of processing. It also tracks upcoming changes in legislation, so the NSI can prepare in time.

**VS-07.3 Implement Data and Metadata Governance**

This stage makes governance part of daily work. It assigns the data owner, data steward, and data custodian roles for each state and each important dataset. It sets the processes for metadata creation, maintenance, and lineage, so that SAF-P09 is met in practice. It sets up the data governance board, which resolves issues that cross domain boundaries. Governance that exists only on paper does not count; this stage makes sure it is embedded in how the value streams actually work.

**VS-07.4 Monitor Quality and Compliance Indicators**

This stage keeps track of whether the rules are followed. It collects quality indicators and compliance evidence from all value streams. It shows the status on dashboards and scorecards, per policy domain and per value stream. It detects deviations early, such as missing metadata, overdue audit actions, or a rise in incidents. Findings are passed to the responsible process owners and, where needed, to the data governance board.

**VS-07.5 Audit, Certify and Report Compliance**

This stage demonstrates compliance. It plans and carries out internal audits and supports external audits and peer reviews. It reviews evidence such as audit trails, lineage, approval records, and disclosure-control records. It reports the results to management and supervisory authorities, and publishes transparency reports where appropriate. A positive outcome leads to certification or a statement of assurance; findings lead to improvement actions.

**VS-07.6 Update and Improve Governance Mechanisms**

This stage keeps governance current. It processes audit findings, incidents, regulatory changes, and lessons learned. It updates policies, procedures, and controls, and retires those that are no longer needed. It informs the value streams of changes through a policy update. It also checks that retention and disposal of data follow the policies, so that data is neither kept too long nor removed too early.

#### 4. The four process types

For a supporting value stream, the four process types take the form of a continuous cycle: plan, build, operate, and improve. The stages of VS-07 follow this cycle.

| Cycle step | Corresponds to | Stages |
|---|---|---|
| Plan | Design | VS-07.1, VS-07.2 |
| Build | Implementation | VS-07.3 |
| Operate | Execution | VS-07.4, VS-07.5 |
| Improve | Management | VS-07.6 |

**Plan**

Planning sets the direction of governance. It decides which frameworks the NSI adopts, which policies it needs, and how strict each policy must be. It is driven by the strategy of the NSI, by legislation, and by the results of earlier audits. Planning takes place in an annual cycle and whenever a significant change occurs, such as new legislation. Its result is an approved policy set and a legal register, owned by the chief data officer and the compliance officer.

**Build**

Building puts governance into place. It assigns the governance roles and sets up the governance bodies, such as the data governance board. It defines the compliance checks that become part of the quality gates and the design processes. Together with VS-09, it provides the tooling for dashboards, catalogs, and audit trails. Building is complete when every state has an owner, a steward, and a custodian, and every policy has a check that tests it.

**Operate**

Operating runs the monitoring and the audits. It is continuous for monitoring and periodic for audits and certification. The compliance officer, quality manager, and auditors carry it out, using the evidence the value streams provide. Operating does not change policies; it shows whether they are followed. Deviations go to the process owners or to the improvement step.

| Aspect | VS-07 |
|---|---|
| Trigger | Audit plan; compliance indicators out of tolerance; incidents; external review |
| Cadence | Continuous monitoring; periodic audits and certification |
| Performed by | ROL-19 Compliance officer, ROL-18 Quality manager, ROL-21 Auditor |
| Input | Policies, legal register, compliance evidence from all value streams |
| Output | Dashboards, audit reports, certifications, transparency reports |
| Control point | Audit and certification in VS-07.5 |
| Exception path | Findings to process owners; structural gaps to VS-07.6 |

**Improve**

Improving closes the governance cycle. It combines audit findings, incidents, regulatory changes, and feedback from the value streams. It decides which policies or controls must change and in which order. It tracks whether improvement actions are carried out on time. Improvement keeps governance proportional: strict where risks are high, and simple where they are low.

#### 5. Actors and roles

VS-07 is led by the governance roles of the NSI, but involves every process owner. Data governance across domains is organized in the collaboration COL-06 *Data governance board*. The table shows the actors and reference roles involved; specialized names in an NSI map onto them (see *Role names in the value streams*).

| Actor or role | ID | Cycle step | Responsibility in VS-07 |
|---|---|---|---|
| Supervisory and legal authority | ACT-08 | External | Sets legal requirements and oversees compliance |
| International statistical organization | ACT-07 | External | Sets international frameworks and organizes peer reviews |
| Process owner | ROL-01 | Operate | Operates within the policies and supplies compliance evidence |
| Data owner | ROL-02 | Build, Operate | Is assigned ownership of states and datasets |
| Data steward | ROL-03 | Operate | Maintains metadata and lineage according to the policies |
| Data custodian | ROL-04 | Operate | Applies access, retention, and disposal decisions |
| Chief data officer | ROL-05 | Plan, Improve | Accountable for the governance framework and data policy |
| Quality manager | ROL-18 | Plan, Operate | Defines quality indicators and monitors them |
| Compliance officer | ROL-19 | Plan, Operate | Maintains the legal register and checks compliance |
| Security officer | ROL-20 | Plan, Operate | Sets security and continuity policy and monitors it |
| Auditor | ROL-21 | Operate | Audits processes and controls independently |

#### 6. Capabilities, processes, and functions

VS-07 mainly draws on the capabilities 4.1.1 *Strategy and governance*, 4.1.2 *Policy and planning*, 4.1.5 *Accountability*, 2.1.1 *Data lifecycle management*, 2.1.2 *Metadata management*, 2.1.3 *Statistical quality management*, 3.1.7 *Legal support*, 3.3.1 *Privacy management*, and 3.3.2 *Security planning*.

| Stage | Realized by processes | Main functions |
|---|---|---|
| VS-07.1 Define Governance Frameworks and Policies | DLM-1 Plan and design data assets | FUN-1.2 Govern and steer the organization; FUN-5.1 Manage the quality framework; FUN-7.1 Govern data |
| VS-07.2 Establish Legal and Regulatory Compliance Mechanisms | DLM-4 Classify and protect data | FUN-10.5 Manage legal affairs; FUN-10.8 Manage information security and privacy |
| VS-07.3 Implement Data and Metadata Governance | OVA-2 Metadata Management; OVA-3 Data Management; DLM-1 Plan and design data assets; DLM-6 Provide data for reuse | FUN-7.1 Govern data; FUN-7.2 Manage metadata |
| VS-07.4 Monitor Quality and Compliance Indicators | OVA-1 Quality Management; DLM-8 Monitor data quality, lineage and use; MDS-8 Monitor use and compliance; DSP-5 Monitor compliance and report | FUN-5.2 Assure and review quality; FUN-7.1 Govern data |
| VS-07.5 Audit, Certify and Report Compliance | OVA-1 Quality Management; PRD-8.2 Conduct evaluation | FUN-1.2 Govern and steer the organization; FUN-5.2 Assure and review quality |
| VS-07.6 Update and Improve Governance Mechanisms | PRD-8.3 Agree an action plan; DLM-10 Archive and preserve data; DLM-11 Dispose of data | FUN-2.1 Plan capability improvements; FUN-7.1 Govern data |

![VS-07 stages, processes, and functions](images/vs-07-processes-functions.png)

|**PLACEHOLDER: ArchiMate view VS-07 (b) stages realized by processes and functions**|
|---|

#### 7. Principles

VS-07 is the value stream that enforces the data principles across the whole chain.

| Principle | Statement | Application in VS-07 |
|---|---|---|
| SAF-P03 | Active life cycle management | Governance checks that every component has an owner and a life cycle plan, and that policies themselves are reviewed and retired |
| SAF-P04 | Maximize the benefits for the organization | Controls are proportional to risk and serve the organization as a whole, not governance for its own sake |
| SAF-P07 | Implement loosely coupled processes and systems | Governance sets the conventions for state interfaces and events that keep value streams decoupled |
| SAF-P09 | No data without metadata and classification | Governance sets the metadata and classification obligations and audits them in every state |
| SAF-P10 | Security by design | Governance sets the security policy and checks that it is built into every design |
| SAF-P11 | Privacy by design | Governance sets the privacy and confidentiality policy and checks its application at every gate |

#### 8. Interfaces, services, and events

**Business services**

| Service | Offered to | Realized in | Interfaces |
|---|---|---|---|
| Policy and framework service | All value streams | VS-07.1 Define Governance Frameworks and Policies | Policy register, policy updates |
| Legal compliance service | All value streams, VS-08 Innovation and Methodological Development | VS-07.2 Establish Legal and Regulatory Compliance Mechanisms | Legal register, privacy impact assessments |
| Data governance service | All value streams | VS-07.3 Implement Data and Metadata Governance | Role assignments, data governance board |
| Compliance monitoring service | Management, process owners | VS-07.4 Monitor Quality and Compliance Indicators | Dashboards and scorecards |
| Assurance service | Management, supervisory authorities, the public | VS-07.5 Audit, Certify and Report Compliance | Audit reports, certifications, transparency reports |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Regulatory change detected* | Review of the legal register and policies in VS-07.2 and VS-07.6 |
| *Compliance indicator out of tolerance* | Follow-up with the process owner |
| *Audit scheduled* / *Audit completed* | Start and end of an audit in VS-07.5 |
| *Method compliance assessment requested* | Assessment before the transfer gate VS-08.5 |
| *Policy update issued* | Adoption of the change by all value streams |

**Interaction with the other value streams**

| Value stream | VS-07 provides | VS-07 receives |
|---|---|---|
| VS-01 to VS-06 (primary) | Policies, gate criteria, governance roles | Audit trails, quality indicators, compliance reports |
| VS-08 Innovation and Methodological Development | Compliance criteria for new methods | Requests for method assessment |
| VS-09 Infrastructure and Platform Enablement | Security and continuity policy | Security posture and incident evidence |
| VS-10 Customer and Stakeholder Engagement | Transparency and accountability commitments | Trust signals and complaints |

#### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| Policy coverage | Share of value streams and data domains working under current, approved policies | Per policy domain, yearly |
| Audit findings closed on time | Share of audit findings resolved before their deadline | Per audit cycle |
| Compliance incidents | Number of confidentiality, security, or legal incidents | Per quarter |
| Certification status | Certifications and peer-review outcomes that are current | Yearly |
| Metadata compliance | Share of registered versions that meet SAF-P09 | Per cycle |
| Regulatory response time | Time from detecting a regulatory change to an updated policy | Per change |

#### 10. Examples **[VC6]**

**A new regulation.** An amendment to data protection law changes the rules for linking personal data. VS-07 records it in the legal register, assesses the impact on the gates of States #2 and #3, and updates the privacy policy. All value streams receive a policy update, and the next audit checks that VS-03 applies the new linkage rules. No value stream has to interpret the law on its own.

**Approval of a new method.** VS-08 proposes machine-learning coding of free-text occupations for the Labor Force Survey. VS-07 assesses the method against the criteria for privacy, transparency, and quality before the transfer to VS-03. It records the decision and the conditions, such as human review of low-confidence cases. Only then may the method enter production.

**A peer review.** Ahead of a peer review against the European Statistics Code of Practice, VS-07 collects the evidence from its dashboards and the compliance reports of the value streams. A self-assessment shows that the revision policy is outdated, and it is updated in VS-07.6 before the review. The outcome and recommendations enter the governance backlog.

|**PLACEHOLDER: VS-07 maturity checklist and detailed scenarios to be added to the toolkit**|
|---|

### VS-08 Innovation and Methodological Development

#### 1. Purpose and value created

VS-08 makes sure the NSI does not stand still. It discovers, tests, and introduces new data sources, methods, tools, and technologies. It connects research, methodology, IT, and the statistical domains, so that innovation answers real needs. It also keeps innovation controlled: only methods that are sound, documented, and compliant reach production. The value created is **continuous improvement**: the NSI can use new data, such as administrative data, web data, and data spaces, and new techniques, such as machine learning and small-area estimation. Without VS-08, improvements would either not happen or enter production without proper testing.

![VS-08 value stream and capabilities](images/vs-08-value-stream.png)

|**PLACEHOLDER: ArchiMate view VS-08 (a) value stream and capabilities**|
|---|

#### 2. Relation to the chain

VS-08 does not move data from one state to the next. It improves the methods and tools that the primary value streams use. Its agenda comes from the chain: the improvement actions of the primary value streams and the user needs collected by VS-10. Its results go back into the chain through a single, governed transfer: stage VS-08.5. VS-08 may use registered state versions for research, under specific authorization, but its experiments never produce registered states themselves.

| Touch point | Where in the chain | What happens |
|---|---|---|
| Innovation needs | Management process type of VS-01 to VS-06; VS-10 | Improvement needs and user needs enter the innovation backlog |
| Research data | Registered versions of States #1 to #4 | Used for research and proofs of concept under specific authorization |
| Transfer gate | VS-08.5, into the design of the target value stream | Validated methods and tools enter production after VS-07 approval |
| Platforms | VS-09 | Sandboxes for research and production platforms for transfer |

![VS-08 relation to the value chain](images/vs-08-relation.png)

|**PLACEHOLDER: ArchiMate view VS-08 (c) relation to the value chain**|
|---|

#### 3. Stages

| Stage | Name | Value added |
|---|---|---|
| VS-08.1 | Identify Innovation Needs and Opportunities | Promising developments are known |
| VS-08.2 | Conduct Research and Proof-of-Concepts | Ideas are tested in a limited scope |
| VS-08.3 | Evaluate Methodological Soundness and Feasibility | Only sound and feasible innovations proceed |
| VS-08.4 | Develop and Document New Methodologies or Tools | Innovations are ready for reuse |
| VS-08.5 | Integrate Innovation into Production Environments | Innovations run in production under governance |
| VS-08.6 | Promote Knowledge Sharing and Capability Building | Staff can apply the new methods |

**VS-08.1 Identify Innovation Needs and Opportunities**

This stage builds the innovation backlog. It collects the improvement needs from the primary value streams and the user needs from VS-10. It scans developments in methodology, technology, and data, including the work of other NSIs and international organizations. It prioritizes the candidates by their value for the organization as a whole and their feasibility. The result is a prioritized backlog, linked to the goals and drivers of the NSI.

**VS-08.2 Conduct Research and Proof-of-Concepts**

This stage tests ideas before any commitment is made. Researchers and methodologists run experiments and pilots in a limited scope and in a separate environment. They use registered data under specific authorization, or synthetic data where that is sufficient. The experiments are documented, including the ones that fail. The result is evidence on whether an idea works, not yet a decision to use it.

**VS-08.3 Evaluate Methodological Soundness and Feasibility**

This stage is the gate that stops attractive but unsound ideas. It assesses accuracy, bias, robustness, scalability, cost, and fit with the quality and ethical frameworks. It checks whether the method can be explained and reproduced. It asks VS-07 for an early view on compliance where privacy or transparency is at stake. A healthy gate sometimes says no, and records why.

**VS-08.4 Develop and Document New Methodologies or Tools**

This stage turns a promising result into something production can use. It writes the method as a standard procedure, with its assumptions, parameters, and limits. It builds a reference implementation, preferably on shared and open components. It prepares test cases, so that the target value stream can verify the method after transfer. A method that lives only in a researcher's notebook cannot be transferred.

**VS-08.5 Integrate Innovation into Production Environments**

This stage is the transfer gate into production. It hands the method or tool over to the design and implementation processes of the target value stream. It requires approval from VS-07 and a production platform from VS-09. The target value stream tests the method in its own environment before it goes live. After transfer, the method belongs to the target value stream, and VS-08 is no longer responsible for running it.

**VS-08.6 Promote Knowledge Sharing and Capability Building**

This stage makes sure people can use and sustain the new method. It provides guidelines, training, and support to the staff of the target value stream. It shares results, including negative ones, inside the NSI and with the international statistical community. It measures whether the method is actually adopted. What is learned here feeds the next round of needs in VS-08.1.

#### 4. The four process types

For a supporting value stream, the four process types take the form of a continuous cycle: plan, build, operate, and improve. The stages of VS-08 follow this cycle.

| Cycle step | Corresponds to | Stages |
|---|---|---|
| Plan | Design | VS-08.1 |
| Build | Implementation | VS-08.2, VS-08.3, VS-08.4 |
| Operate | Execution | VS-08.5 |
| Improve | Management | VS-08.6 |

**Plan**

Planning sets the innovation agenda. It is driven by the strategy of the NSI, the drivers in the Motivation layer, and the needs from the chain. It decides which candidates enter research and how much capacity they receive. Planning takes place in a regular cycle, for example per quarter, so that urgent needs are not blocked by a yearly plan. The head of methodology or innovation owns the agenda.

**Build**

Building covers research, evaluation, and development. It runs as a pipeline of projects, each with a clear question and a limited scope. Each project passes the evaluation gate before development starts. Building requires research environments from VS-09 and access to data under specific authorization. A project ends with a documented method or tool, or with a documented decision to stop.

**Operate**

Operating is the transfer into production. It takes place per innovation, when development is complete and VS-07 has approved the method. The target value stream receives the method, tests it, and puts it into production through its own design and implementation processes. VS-08 supports the transfer, but does not run the method afterwards. A transfer that fails returns the innovation to development.

| Aspect | VS-08 |
|---|---|
| Trigger | A developed method or tool that passed the evaluation gate |
| Cadence | Per innovation |
| Performed by | ROL-07 Methodologist, ROL-10 Data engineer, process owner of the target value stream (ROL-01) |
| Input | Documented method, reference implementation, test cases, VS-07 approval |
| Output | Method or tool in production in the target value stream |
| Control point | Transfer gate in VS-08.5 |
| Exception path | Failed tests in the target value stream: back to VS-08.4; compliance concerns: back to VS-08.3 |

**Improve**

Improving makes innovation stick and makes the pipeline better. It checks whether transferred methods are used and still work after a year. It shares knowledge and builds skills, so that the NSI does not depend on a few experts. It reviews the pipeline itself: lead times, the share of ideas stopped at the gate, and the reasons. It feeds the results into the next planning round.

#### 5. Actors and roles

VS-08 connects methodology, research, IT, and the statistical domains. International cooperation, organized in COL-03 *International statistical cooperation*, is an important source of methods and tools. The table shows the reference roles involved; specialized names in an NSI map onto them (see *Role names in the value streams*).

| Actor or role | ID | Cycle step | Responsibility in VS-08 |
|---|---|---|---|
| International statistical organization | ACT-07 | External | Shares methods, tools, and standards developed in the community |
| Process owner | ROL-01 | Plan, Operate | Brings needs from the production value streams and accepts transfers |
| Methodologist | ROL-07 | Plan, Build, Operate | Leads the innovation agenda, evaluates soundness, formalizes methods |
| Data engineer | ROL-10 | Build, Operate | Builds reference implementations and prepares them for production |
| Platform engineer | ROL-11 | Build | Provides research environments and production platforms with VS-09 |
| Subject-matter statistician | ROL-15 | Build | Brings the real problem, runs research, validates fitness for purpose |
| Compliance officer | ROL-19 | Build, Operate | Assesses new methods against compliance criteria |
| Enterprise architect | ROL-24 | Plan | Checks fit with the target architecture |
| Trainer or knowledge manager | Not in the reference set **[VC7]** | Improve | Provides training and shares knowledge |

#### 6. Capabilities, processes, and functions

VS-08 mainly draws on the capabilities 2.2.1 *Data source exploration*, 2.2.2 *Product innovation*, 2.2.3 *Methodology*, 4.1.3 *Change management*, 4.1.6 *Collaboration*, and 3.1.1 *Personnel management (HR)*.

| Stage | Realized by processes | Main functions |
|---|---|---|
| VS-08.1 Identify Innovation Needs and Opportunities | PRD-1.5 Check data availability and suitability | FUN-4.2 Research and innovate |
| VS-08.2 Conduct Research and Proof-of-Concepts | No reference process (NSI-specific) | FUN-4.2 Research and innovate |
| VS-08.3 Evaluate Methodological Soundness and Feasibility | PRD-3.6 Test statistical business process | FUN-4.1 Manage statistical and analytical methodology; FUN-5.2 Assure and review quality |
| VS-08.4 Develop and Document New Methodologies or Tools | PRD-3.2 Reuse or build processing and analysis components; OVA-5 Knowledge Management | FUN-4.1 Manage statistical and analytical methodology; FUN-10.4 Manage information and records |
| VS-08.5 Integrate Innovation into Production Environments | PRD-3.7 Finalize production systems | FUN-2.4 Transfer capability improvements to operations; FUN-3.1 Design and build statistical products |
| VS-08.6 Promote Knowledge Sharing and Capability Building | OVA-5 Knowledge Management | FUN-10.1 Manage human resources; FUN-10.4 Manage information and records |

![VS-08 stages, processes, and functions](images/vs-08-processes-functions.png)

|**PLACEHOLDER: ArchiMate view VS-08 (b) stages realized by processes and functions**|
|---|

#### 7. Principles

| Principle | Statement | Application in VS-08 |
|---|---|---|
| SAF-P01 | Reuse before open source, open source before buying, buying before building | Innovations build first on methods and tools of other NSIs and open-source communities |
| SAF-P03 | Active life cycle management | Methods and tools are managed from proof of concept through production to retirement |
| SAF-P04 | Maximize the benefits for the organization | Candidates are prioritized by value for the whole NSI, not by novelty |
| SAF-P05 | IT and technology is everyone's business | Research, methodology, IT, and the statistical domains decide together |
| SAF-P07 | Implement loosely coupled processes and systems | Transferred methods fit the state interfaces, so production value streams stay decoupled |

#### 8. Interfaces, services, and events

**Business services**

| Service | Offered to | Realized in | Interfaces |
|---|---|---|---|
| Innovation intake service | Process owners, VS-10 Customer and Stakeholder Engagement | VS-08.1 Identify Innovation Needs and Opportunities | Innovation backlog |
| Research and proof-of-concept service | Statistical domains | VS-08.2 Conduct Research and Proof-of-Concepts | Research environments, experiment reports |
| Methodology advisory service | Design processes of all value streams | VS-08.3 Evaluate Methodological Soundness and Feasibility; VS-08.4 Develop and Document New Methodologies or Tools | Method documentation, advice |
| Innovation transfer service | Primary value streams | VS-08.5 Integrate Innovation into Production Environments | Reference implementations, test cases |
| Knowledge and training service | Staff of all value streams | VS-08.6 Promote Knowledge Sharing and Capability Building | Guidelines, training |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Innovation need raised* | Entry into the backlog in VS-08.1 |
| *Proof of concept completed* | Start of evaluation in VS-08.3 |
| *Innovation stopped at the gate* | Documented decision not to proceed |
| *Method compliance assessment requested* | Assessment by VS-07 |
| *Method transferred to production* | Completion of VS-08.5 |

**Interaction with the other value streams**

| Value stream | VS-08 provides | VS-08 receives |
|---|---|---|
| VS-01 to VS-06 (primary) | Validated methods and tools | Improvement needs; fitness-for-purpose validation |
| VS-07 Governance and Compliance | Methods for assessment | Compliance criteria and approval |
| VS-09 Infrastructure and Platform Enablement | Requirements for research and production platforms | Sandboxes and production platforms |
| VS-10 Customer and Stakeholder Engagement | New service and product options | User needs that call for new methods |

#### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| Lead time from idea to production | Median time from backlog entry to completed transfer | Per transferred innovation |
| Transfer rate and durability | Transfers per year, and the share still in use after twelve months | Yearly |
| Gate effectiveness | Share of proofs of concept stopped at the gate, with a documented reason | Per evaluation |
| Backlog responsiveness | Share of prioritized candidates that reach a proof of concept within the agreed time | Per planning period |
| Capability building | Staff trained, and adoption rate in the target value streams | Per transfer, yearly |

#### 10. Examples **[VC6]**

**Machine-learning coding.** VS-03 reports that coding free-text occupations in the Labor Force Survey is costly. VS-08 pilots a machine-learning coder, evaluates its accuracy and bias, and builds a documented reference implementation. After approval by VS-07 and on a production platform from VS-09, the coder is transferred to VS-03. The coding team is trained, and adoption is measured after the first cycles.

**A new data source.** VS-10 reports demand for more timely price statistics. VS-08 investigates web scraping and multilateral index methods, compares the results with the official consumer price index, and documents the method. The method is transferred to VS-01 and VS-04, and the methodology is shared with other NSIs.

**The gate says no.** A domain wants a generative-AI assistant to draft commentary in VS-05. The proof of concept shows fluent text, but the evaluation finds results that vary between runs and cannot be explained. VS-07 agrees that the transparency requirement cannot be met. The idea is stopped with a documented reason, and a narrower option, template-based drafting with human sign-off, enters the backlog.

|**PLACEHOLDER: VS-08 maturity checklist and detailed scenarios to be added to the toolkit**|
|---|

### VS-09 Infrastructure and Platform Enablement

#### 1. Purpose and value created

VS-09 provides the technical foundation on which every other value stream runs. It delivers the environments, data platforms, tools, and integration services that statistical production needs, from collection to dissemination. It keeps them secure, available, and up to date, and flexible enough to adopt new technology. This chapter describes the business view: the ability to provide platforms and services. The platforms themselves are described in the application and technology architecture. The value created is **operational capability and continuity**: the chain can run reliably, at the required scale, and recover from disruption.

![VS-09 value stream and capabilities](images/vs-09-value-stream.png)

|**PLACEHOLDER: ArchiMate view VS-09 (a) value stream and capabilities**|
|---|

#### 2. Relation to the chain

VS-09 does not move data from one state to the next. It provides the environments in which the states are stored and the value streams run. It hosts the catalogs, the version stores, and the event interfaces that make the state handovers work. It receives requirements from all value streams and delivers platforms and services back to them. Its security and continuity are governed by VS-07.

| Touch point | Where in the chain | What happens |
|---|---|---|
| State storage | States #1 to #5 | VS-09 provides the storage, versioning, and access control for every state |
| Handover events | Between all primary value streams | VS-09 provides the event interfaces that trigger the next value stream |
| Channels | VS-01 intake and VS-06 release | VS-09 provides intake channels, portals, APIs, and secure processing environments |
| Research and transfer | VS-08 | VS-09 provides sandboxes and production platforms for transferred methods |
| Security and continuity | All value streams | VS-09 applies the policy set by VS-07 |

![VS-09 relation to the value chain](images/vs-09-relation.png)

|**PLACEHOLDER: ArchiMate view VS-09 (c) relation to the value chain**|
|---|

#### 3. Stages

| Stage | Name | Value added |
|---|---|---|
| VS-09.1 | Define Digital and Technical Requirements | Infrastructure needs follow from business needs |
| VS-09.2 | Design Platform and Infrastructure Architecture | Platforms are designed for storage, processing, integration, and secure access |
| VS-09.3 | Provision and Configure Platforms | Environments are available with the required controls |
| VS-09.4 | Enable Integration and Orchestration Services | Processes and services are connected |
| VS-09.5 | Ensure Performance, Security and Continuity | Platforms are reliable and protected |
| VS-09.6 | Evolve and Modernize the Technical Ecosystem | The technical landscape stays current |

**VS-09.1 Define Digital and Technical Requirements**

This stage derives technical requirements from business needs. It collects requirements from the value streams: data volumes, processing loads, retention per state, security classifications, and channel needs. It takes into account the constraints of the NSI, such as rules on where statistical microdata may be processed. It translates them into requirements for storage, processing, integration, and access. Requirements that come from the business are leading; technology that nobody needs is not built.

**VS-09.2 Design Platform and Infrastructure Architecture**

This stage designs the platforms that meet the requirements. It produces architecture blueprints for storage, processing, integration, and secure access, aligned with the target architecture of the NSI. It decides what is shared between value streams and what is specific. It applies the choice between reuse, open source, purchase, and own development. A platform team may organize storage internally in layers, for example Bronze, Silver, and Gold; that is an engineering convention, and the states remain the governance model. **[VC8]**

**VS-09.3 Provision and Configure Platforms**

This stage makes the designed platforms available. It deploys environments on premises, in a private cloud, or where policy allows in a public cloud. It configures them with the required monitoring, access control, and security measures. It provides separate environments for development, testing, research, and production. An environment is only handed over when its controls work.

**VS-09.4 Enable Integration and Orchestration Services**

This stage connects processes and services. It provides APIs, workflow engines, and the event interfaces that the state handovers rely on, such as *Raw Data Registered*. It provides the catalog and version services that make registered states findable and traceable. It makes sure that value streams connect through these services and not through direct access to each other's systems. This keeps the chain loosely coupled in practice, not only on paper.

**VS-09.5 Ensure Performance, Security and Continuity**

This stage keeps the platforms running and protected every day. It monitors performance and capacity, and manages incidents. It applies the security measures and handles security incidents together with the security officer. It guarantees availability and recovery according to the agreed service levels, and tests recovery regularly. This is the assurance that the chain can keep producing, even when something fails.

**VS-09.6 Evolve and Modernize the Technical Ecosystem**

This stage keeps the technical landscape current. It maintains a modernization roadmap, based on the life cycle plans of all components. It introduces new technology, often transferred from VS-08, and retires components that are out of support. It reduces technical debt step by step, without disrupting production. The roadmap is reviewed regularly against the strategy and the requirements of the value streams.

#### 4. The four process types

For a supporting value stream, the four process types take the form of a continuous cycle: plan, build, operate, and improve. The stages of VS-09 follow this cycle.

| Cycle step | Corresponds to | Stages |
|---|---|---|
| Plan | Design | VS-09.1, VS-09.2 |
| Build | Implementation | VS-09.3, VS-09.4 |
| Operate | Execution | VS-09.5 |
| Improve | Management | VS-09.6 |

**Plan**

Planning decides which platforms the NSI needs. It is driven by the requirements of the value streams, by the target architecture, and by the constraints set by VS-07. It takes place in the yearly planning cycle and whenever a value stream brings a significant new requirement. The enterprise architect and the platform engineers carry it out together. Its result is a set of requirements and blueprints, approved by the architecture board.

**Build**

Building puts the platforms and services in place. It provisions and configures environments and integration services according to the blueprints. It works in increments, so that value streams can start using parts of a platform early. It tests functionality, security, and performance before handover. Building is complete when the receiving value stream has accepted the platform for production use.

**Operate**

Operating runs the platforms as a continuous service. It covers monitoring, incident management, security operations, backup, and recovery. Platform engineers and operations staff carry it out, according to agreed service levels. Operating does not change the design; structural problems go to improvement. Capacity peaks, such as a census, are prepared in advance with the value streams concerned.

| Aspect | VS-09 |
|---|---|
| Trigger | Continuous service; incidents; capacity alerts; known peaks in production |
| Cadence | Continuous |
| Performed by | ROL-11 Platform engineer, ROL-20 Security officer, ROL-04 Data custodian |
| Input | Production platforms, service levels, security and continuity policy |
| Output | Available, secure platforms; incident and continuity reports |
| Control point | Service levels and recovery tests in VS-09.5 |
| Exception path | Incidents to incident management; structural problems to VS-09.6 |

**Improve**

Improving keeps the foundation fit for the future. It reviews incidents, capacity trends, and support status of components. It updates the modernization roadmap and plans the retirement of obsolete components. It introduces technology that VS-08 has validated. It also checks that platform costs stay in proportion to their use.

#### 5. Actors and roles

VS-09 is carried by the IT organization of the NSI, often together with suppliers. Architecture decisions are taken in COL-07 *Architecture board*. The table shows the actors and reference roles involved; specialized names in an NSI map onto them (see *Role names in the value streams*).

| Actor or role | ID | Cycle step | Responsibility in VS-09 |
|---|---|---|---|
| National Statistical Institute (management) | ACT-01 | Plan | The chief technology or infrastructure officer is accountable for the technical foundation |
| Supplier and service provider | ACT-09 | Build, Operate | Delivers hardware, software, hosting, or cloud services under contract |
| Process owner | ROL-01 | Plan | Brings the requirements of each value stream |
| Data custodian | ROL-04 | Operate | Operates storage, backup, access control, and retention |
| Data engineer | ROL-10 | Build | Builds integration and orchestration services |
| Platform engineer | ROL-11 | Plan, Build, Operate, Improve | Designs, provisions, and operates platforms |
| Test manager | ROL-12 | Build | Plans functional, security, and performance tests |
| Security officer | ROL-20 | Operate | Applies security measures and handles security incidents |
| Enterprise architect | ROL-24 | Plan, Improve | Aligns platforms with the target architecture and the roadmap |

#### 6. Capabilities, processes, and functions

VS-09 mainly draws on the capabilities 3.2.1 *Application development*, 3.2.2 *Functional management*, 3.2.3 *Technical management*, 3.2.5 *IT infrastructure*, 3.3.2 *Security planning*, 3.3.3 *Security incident management*, 3.3.6 *IT security services*, and 4.1.7 *Architecture Management*.

| Stage | Realized by processes | Main functions |
|---|---|---|
| VS-09.1 Define Digital and Technical Requirements | PRD-2.6 Design production systems and workflows | FUN-2.5 Manage enterprise architecture; FUN-3.1 Design and build statistical products |
| VS-09.2 Design Platform and Infrastructure Architecture | PRD-2.6 Design production systems and workflows | FUN-2.5 Manage enterprise architecture; FUN-10.3 Manage information technology |
| VS-09.3 Provision and Configure Platforms | PRD-3.4 Configure workflows; MDS-4 Provide a secure processing environment | FUN-8.3 Operate secure research environments; FUN-10.3 Manage information technology |
| VS-09.4 Enable Integration and Orchestration Services | PRD-3.4 Configure workflows; DSP-4 Exchange data under usage control | FUN-9.2 Operate data space connectivity; FUN-10.3 Manage information technology |
| VS-09.5 Ensure Performance, Security and Continuity | PRD-3.5 Test production systems; DLM-5 Store and version data | FUN-10.3 Manage information technology; FUN-10.8 Manage information security and privacy |
| VS-09.6 Evolve and Modernize the Technical Ecosystem | No reference process (NSI-specific) | FUN-2.2 Develop capability improvements; FUN-10.3 Manage information technology |

![VS-09 stages, processes, and functions](images/vs-09-processes-functions.png)

|**PLACEHOLDER: ArchiMate view VS-09 (b) stages realized by processes and functions**|
|---|

#### 7. Principles

| Principle | Statement | Application in VS-09 |
|---|---|---|
| SAF-P01 | Reuse before open source, open source before buying, buying before building | Platforms are shared across value streams; open-source components come before purchase |
| SAF-P02 | Active support | Every platform component has active vendor or community support |
| SAF-P03 | Active life cycle management | Every component has an owner and a life cycle plan in the modernization roadmap |
| SAF-P05 | IT and technology is everyone's business | Platform decisions are taken with the value streams that use them |
| SAF-P06 | Business continuity | Availability and recovery are designed in and tested regularly |
| SAF-P10 | Security by design | Security controls are part of every environment from the start |

#### 8. Interfaces, services, and events

**Business services**

| Service | Offered to | Realized in | Interfaces |
|---|---|---|---|
| Platform provisioning service | All value streams | VS-09.3 Provision and Configure Platforms | Service catalog, environment requests |
| Integration and event service | All primary value streams | VS-09.4 Enable Integration and Orchestration Services | APIs, workflow engines, event interfaces |
| Catalog and version service | All value streams | VS-09.4 Enable Integration and Orchestration Services | Data catalog, version store |
| Operations and continuity service | All value streams | VS-09.5 Ensure Performance, Security and Continuity | Service desk, monitoring, recovery |
| Research environment service | VS-06 Dissemination and Service Delivery, VS-08 Innovation and Methodological Development | VS-09.3 Provision and Configure Platforms | Secure processing environments, sandboxes |

**Business events**

| Event | Triggers or marks |
|---|---|
| *Platform requested* | Requirements analysis in VS-09.1 |
| *Platform accepted for production* | Completion of building |
| *Incident reported* | Incident management in VS-09.5 |
| *Capacity threshold reached* | Scaling or capacity planning |
| *Component end of support announced* | Update of the modernization roadmap in VS-09.6 |

**Interaction with the other value streams**

| Value stream | VS-09 provides | VS-09 receives |
|---|---|---|
| VS-01 to VS-06 (primary) | Platforms, storage, event interfaces, channels | Requirements, capacity demand, incidents |
| VS-07 Governance and Compliance | Security posture and continuity evidence | Security and continuity policy |
| VS-08 Innovation and Methodological Development | Sandboxes and production platforms | New technology to adopt |

#### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| Platform availability | Availability against the agreed service level | Per platform, per month |
| Time to restore | Mean time to restore service after an incident | Per severity, per quarter |
| Event reliability | Delivery rate of the state handover events | Per interface, per month |
| Capacity headroom | Share of platforms within their planned capacity | Per month |
| Security posture | Open critical vulnerabilities and time to patch | Continuous, reported per quarter |
| Modernization progress | Components retired or replaced according to the roadmap | Yearly |

#### 10. Examples **[VC6]**

**A secure processing environment.** VS-06 must give accredited researchers access to de-identified business microdata. VS-09 captures the requirements, designs the environment, and provisions it with access control and output checking. It operates the environment under the security policy of VS-07. VS-06 can then offer research access without building its own platform.

**A new processing platform.** VS-08 has validated a scalable processing technology. VS-09 designs and provisions the platform, connects it to the existing event interfaces, and tests performance and recovery. The platform is added to the modernization roadmap, and the old platform is planned for retirement.

**The census peak.** The census will multiply intake and processing volumes in VS-01 and VS-03 for three months. VS-09 plans the extra capacity with the census team, provisions it before the field period, and tests the event interfaces under full load. During the peak it monitors availability against the service levels. Afterwards the extra capacity is released, and the lessons enter the roadmap.

|**PLACEHOLDER: VS-09 maturity checklist and detailed scenarios to be added to the toolkit**|
|---|

### VS-10 Customer and Stakeholder Engagement

#### 1. Purpose and value created

VS-10 keeps the NSI connected to the people and organizations it serves and depends on. It maintains the relationships with users, data providers, partners, and policy makers. It finds out what they need, translates those needs into requirements, and manages the portfolio of products and services that meets them. It communicates openly about what the NSI does and how it protects the data it receives. The value created is **relevance and trust**: the NSI produces what society needs, and data providers and users trust it. VS-10 is not a one-way channel; it is a continuous dialogue that feeds the whole chain.

![VS-10 value stream and capabilities](images/vs-10-value-stream.png)

|**PLACEHOLDER: ArchiMate view VS-10 (a) value stream and capabilities**|
|---|

#### 2. Relation to the chain

VS-10 does not move data from one state to the next. It moves understanding: needs come in, and services and communication go out. It sits at both ends of the chain: at boundary position #0, where data providers and respondents deliver data, and at State #5 and boundary position #6, where users receive and use the statistics. It routes what it learns into the design of the primary value streams and into the innovation backlog of VS-08. It runs continuously.

| Touch point | Where in the chain | What happens |
|---|---|---|
| Data providers and respondents | Boundary position #0, VS-01 | VS-10 maintains relationships and monitors response burden |
| Users | State #5 and boundary position #6, VS-06 | VS-10 receives usage and feedback and engages users |
| Product design | Design process type of VS-01 to VS-06 | User needs become requirements for products and services |
| Innovation | VS-08.1 | Needs that require new methods enter the innovation backlog |

![VS-10 relation to the value chain](images/vs-10-relation.png)

|**PLACEHOLDER: ArchiMate view VS-10 (c) relation to the value chain**|
|---|

#### 3. Stages

| Stage | Name | Value added |
|---|---|---|
| VS-10.1 | Identify and Segment Stakeholders | The NSI knows its users, providers, and partners |
| VS-10.2 | Collect and Analyze User Needs | Needs are translated into requirements |
| VS-10.3 | Define and Manage Service Portfolios | Services and products match the needs |
| VS-10.4 | Deliver Services and Manage Relationships | Users and partners are served |
| VS-10.5 | Engage and Communicate with Stakeholders | Stakeholders understand the output |
| VS-10.6 | Monitor Impact and Satisfaction | The NSI knows its impact and acts on it |

**VS-10.1 Identify and Segment Stakeholders**

This stage maps who the NSI deals with. It identifies users, data providers, respondents, partners, and policy makers, and groups them into segments with similar needs. For each segment, it records expectations, preferred channels, and the relationship owner. It also recognizes new segments when they appear, such as data journalists or developers using the API. The stakeholder map is the basis for all other stages.

**VS-10.2 Collect and Analyze User Needs**

This stage finds out what stakeholders need. It runs consultations, surveys, user research, and advisory councils, and analyzes feedback from VS-06. It also collects the needs of data providers, such as lower burden or clearer delivery terms. It translates needs into concrete requirements for products, services, or data collection. Requirements are recorded in a needs register and routed to the design of the value streams or to VS-08.

**VS-10.3 Define and Manage Service Portfolios**

This stage decides what the NSI offers. It manages the portfolio of statistical products and services, such as publications, APIs, tailor-made data, and research access. It balances user needs against the mandate, the strategy, and the available resources. It sets service levels and decides on new, changed, or retired services. The portfolio is the bridge between what users want and what the chain produces.

**VS-10.4 Deliver Services and Manage Relationships**

This stage serves users and partners every day. It runs the service desk and account management for key users and partners. It maintains the relationships with data providers, together with the relationship managers in VS-01. It handles requests and complaints according to the service levels. It makes sure the NSI speaks with one voice to each partner.

**VS-10.5 Engage and Communicate with Stakeholders**

This stage explains the work of the NSI to the outside world. It organizes outreach, workshops, and knowledge sharing, and supports the promotion of releases with VS-06. It explains why the NSI needs data and how it protects confidentiality, which supports the willingness of providers and respondents to deliver. It helps users understand statistics and their uncertainty. Open communication builds the trust on which both data collection and use depend.

**VS-10.6 Monitor Impact and Satisfaction**

This stage measures whether the NSI makes a difference. It measures user satisfaction per segment and the quality of service. It collects evidence of how statistics are used in policy, research, and media. It analyzes the results and identifies gaps between needs and offer. The findings feed the next cycle and the planning of the NSI.

#### 4. The four process types

For a supporting value stream, the four process types take the form of a continuous cycle: plan, build, operate, and improve. The stages of VS-10 follow this cycle.

| Cycle step | Corresponds to | Stages |
|---|---|---|
| Plan | Design | VS-10.1, VS-10.2 |
| Build | Implementation | VS-10.3 |
| Operate | Execution | VS-10.4, VS-10.5 |
| Improve | Management | VS-10.6 |

**Plan**

Planning decides whom the NSI wants to reach and what they need. It is driven by the strategy, the mandate, and the results of earlier impact measurement. It sets the engagement strategy, the segments, and the consultation program. Planning takes place in the yearly cycle and when a new segment or a major change in needs appears. The head of communication and engagement owns it, together with the product owners.

**Build**

Building shapes the offer and the means to deliver it. It turns needs into changes in the portfolio, and sets service levels for new or changed services. It sets up the channels for support and feedback, together with VS-09. It routes requirements to the design processes of the value streams that must deliver them. Building is complete when a service is in the portfolio and the delivering value stream has accepted it.

**Operate**

Operating runs the daily dialogue with stakeholders. It covers the service desk, account management, provider relationships, outreach, and communication around releases. Relationship managers and service staff carry it out, according to the agreed service levels. Operating does not change the portfolio; new needs go back to planning. Complaints and incidents with providers or users are handled with the value stream concerned.

| Aspect | VS-10 |
|---|---|
| Trigger | User requests and complaints; release calendar; consultation program; provider issues |
| Cadence | Continuous; consultations and campaigns per plan |
| Performed by | ROL-23 Relationship manager, ROL-22 Dissemination and service manager |
| Input | Service portfolio, stakeholder map, service levels |
| Output | Served users and partners, communication, recorded needs and feedback |
| Control point | Service levels in VS-10.4 |
| Exception path | New needs to VS-10.2; service problems to the delivering value stream |

**Improve**

Improving closes the engagement cycle. It uses satisfaction measurements, impact evidence, and usage data from VS-06. It identifies services that no longer meet needs and needs that no service meets yet. It proposes changes to the portfolio, the channels, or the communication. Its findings also feed VS-08, when a need calls for a new method or source.

#### 5. Actors and roles

VS-10 involves more external actors than any other supporting value stream. Its relationships run through several collaborations: COL-01 *Data provision partnership*, COL-02 *National statistical system*, and COL-03 *International statistical cooperation*. The table shows the actors and reference roles involved; specialized names in an NSI map onto them (see *Role names in the value streams*).

| Actor or role | ID | Cycle step | Responsibility in VS-10 |
|---|---|---|---|
| Data provider | ACT-03 | External | Delivers data and gives feedback on burden and agreements |
| Respondent | ACT-04 | External | Provides data and expects clear communication |
| Data user | ACT-05 | External | Uses statistics and expresses needs and satisfaction |
| Other producer of official statistics | ACT-06 | External | Partner in the national statistical system |
| International statistical organization | ACT-07 | External | User of NSI data and partner in cooperation |
| Statistical designer | ROL-06 | Build | Turns needs into product designs |
| Data collection manager | ROL-13 | Operate | Handles respondent contact during collection |
| Dissemination and service manager | ROL-22 | Build, Operate | Manages the service portfolio, service levels, and the service desk |
| Relationship manager | ROL-23 | Plan, Operate, Improve | Maintains relationships, runs user research, communication, and impact measurement |

#### 6. Capabilities, processes, and functions

VS-10 mainly draws on the capabilities 1.1.1 *Needs inventory*, 1.5.2 *Promotion to use*, 2.2.5 *User research*, 3.4.1 *Services management*, 3.4.2 *Contact management*, 3.4.3 *Service agreement*, 3.4.4 *Self-service*, and 4.1.6 *Collaboration*.

| Stage | Realized by processes | Main functions |
|---|---|---|
| VS-10.1 Identify and Segment Stakeholders | PRD-1.2 Consult and confirm needs; DSP-6 Participate in data space governance | FUN-1.3 Manage strategic collaboration; FUN-10.9 Manage users and services |
| VS-10.2 Collect and Analyze User Needs | PRD-1.1 Identify needs; PRD-1.2 Consult and confirm needs | FUN-3.1 Design and build statistical products; FUN-10.9 Manage users and services |
| VS-10.3 Define and Manage Service Portfolios | PRD-2.1 Design outputs and dissemination | FUN-10.9 Manage users and services |
| VS-10.4 Deliver Services and Manage Relationships | PRD-7.5 Provide user support; MDS-6 Support researchers; OVA-6 Data Supplier Management | FUN-6.1 Manage data supplier relationships; FUN-10.9 Manage users and services |
| VS-10.5 Engage and Communicate with Stakeholders | PRD-7.4 Promote dissemination products | FUN-1.4 Build public confidence; FUN-10.6 Manage communication |
| VS-10.6 Monitor Impact and Satisfaction | PRD-8.1 Gather evaluation inputs; PRD-8.2 Conduct evaluation | FUN-5.2 Assure and review quality; FUN-10.9 Manage users and services |

![VS-10 stages, processes, and functions](images/vs-10-processes-functions.png)

|**PLACEHOLDER: ArchiMate view VS-10 (b) stages realized by processes and functions**|
|---|

#### 7. Principles

| Principle | Statement | Application in VS-10 |
|---|---|---|
| SAF-P02 | Active support | Services to users and partners are actively supported, with agreed service levels |
| SAF-P04 | Maximize the benefits for the organization | The portfolio serves public value and the whole NSI, not the wishes of one unit |
| SAF-P05 | IT and technology is everyone's business | User needs are brought into technology and product decisions |
| SAF-P08 | Data is shared property | Users get broad and equal access to statistics and services |
| SAF-P11 | Privacy by design | Providers and respondents are told openly how their data is used and protected |

#### 8. Interfaces, services, and events

**Business services**

| Service | Offered to | Realized in | Interfaces |
|---|---|---|---|
| Needs and consultation service | Users, partners, policy makers | VS-10.2 Collect and Analyze User Needs | Consultations, user research, advisory councils |
| Service portfolio | All users | VS-10.3 Define and Manage Service Portfolios | Product and service catalog |
| Service desk and account management | Users, partners | VS-10.4 Deliver Services and Manage Relationships | Service desk, account managers |
| Provider relationship service | Data providers, respondents | VS-10.4 Deliver Services and Manage Relationships | Relationship managers, provider portal |
| Outreach and communication service | The public, media, users | VS-10.5 Engage and Communicate with Stakeholders | Events, website, social media |

**Business events**

| Event | Triggers or marks |
|---|---|
| *User need captured* | Analysis and routing in VS-10.2 |
| *Feedback received* | Analysis in VS-10.2 and VS-10.6 |
| *Service request* / *Complaint received* | Handling in VS-10.4 |
| *Portfolio change approved* | Requirement to the delivering value stream |
| *Need routed to design or innovation* | Input for the design of VS-01 to VS-06 or for VS-08.1 |

**Interaction with the other value streams**

| Value stream | VS-10 provides | VS-10 receives |
|---|---|---|
| VS-01 Data Acquisition and Ingestion | Provider relationships and burden insight | Provider issues and feedback |
| VS-02 to VS-05 (primary) | User needs as requirements for design | Product changes to communicate |
| VS-06 Dissemination and Service Delivery | Service requirements and communication support | Usage data and user feedback |
| VS-07 Governance and Compliance | Trust signals and complaints | Transparency and accountability commitments |
| VS-08 Innovation and Methodological Development | User needs that call for new methods | New product and service options |

#### 9. Key performance indicators

| KPI | Description | Measurement |
|---|---|---|
| User satisfaction | Satisfaction score per user segment and service | Per survey round, per segment |
| Needs conversion | Share of recorded needs turned into requirements for design or innovation | Per planning period |
| Service performance | Response and resolution times against the service levels | Per month |
| Reach and engagement | Participation in consultations and outreach; reach per segment | Per campaign, yearly |
| Impact evidence | Documented uses of official statistics in policy, research, and media | Yearly |

#### 10. Examples **[VC6]**

**A new need becomes a product.** In a consultation, regional policy makers ask for labor market figures at a finer regional level. VS-10 records the need, adds a candidate product to the portfolio, and routes the requirement to VS-04 and VS-05. Because small-area estimation is needed, the request also enters the backlog of VS-08. After the first release by VS-06, VS-10 measures uptake and satisfaction.

**Closing the feedback loop.** VS-06 reports that users misread the confidence intervals in the labor market release. VS-10 analyzes the feedback, provides a plain-language explanation, and routes a documentation improvement to the design of VS-05 and VS-06. The next satisfaction survey shows whether the change helped.

**A new audience.** Journalists increasingly quote statistics from third-party websites, sometimes incorrectly. VS-10 recognizes data journalists as a segment, consults them, and adds a media service to the portfolio: machine-readable releases, ready-to-use visuals, and short methodology notes. The service is delivered through VS-06 under the equal-access policy of VS-07. The accuracy of citations in the press becomes an impact measure.

|**PLACEHOLDER: VS-10 maturity checklist and detailed scenarios to be added to the toolkit**|
|---|







