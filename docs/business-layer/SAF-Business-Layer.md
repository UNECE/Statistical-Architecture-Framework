---
title: SAF Business Layer — Primary and Supporting Value Streams (VS-01 to VS-10)
abstract: "This document consolidates the business layer of the Statistical Architecture Framework (SAF) into a single, readable overview. It covers the six **primary** value streams that form the statistical production chain (VS-01 Data Acquisition through VS-06 Dissemination) and the four **supporting** value streams that enable them (VS-07 Governance, VS-08 Innovation, VS-09 Infrastructure, VS-10 Stakeholder Engagement). It explains, once, the shared concepts the primary domains reuse — the data value chain and its steady states, the four-process governance pattern, and the principles to apply — then summarizes each primary stream, and finally the supporting streams, which work differently: they run continuously across the whole chain and produce enabling capabilities rather than transforming data. It is a reading companion to the detailed per-stream documents; the per-stream 'Applying This to Your NSO' guidance is omitted here."

---

## Introduction — The Statistical Data Value Chain

The SAF business layer describes how a National Statistical Office (NSO) turns externally-held data into trusted statistics that serve society. Six **primary** value streams form a linear production chain, each adding a specific kind of statistical value, and four **supporting** value streams enable them across the board.

{{< include _includes/_key-concepts.qmd >}}

This document is the consolidated, easier-to-read view of all ten streams. The shared concepts the primary streams rely on — the chain itself, the steady states of data, the four-process governance pattern, and the principles — are explained once below; each **primary** stream is then summarized compactly, keeping its execution detail. The four **supporting** streams follow at the end, in a section that first explains how a supporting stream differs from a production stream. For the full design, implementation, and management detail, and for NSO-application guidance, see the individual `VS-0x` business-layer documents.

*A note on numbering:* each `VS-0x.y` you see below is both a value stream stage (*what value* is added) and a business process (*how* it is done). The numbering maps one-to-one; this document uses the business-process view. See the key-concepts box above for the distinction.

The diagram below shows the whole business layer in one picture: data enters from external providers on the left, gains value through the six primary streams, and reaches users and society on the right — with the four supporting streams enabling every step.

```{mermaid}
%%| label: fig-overview
%%| fig-cap: "The six primary value streams as a production chain, delivering to users and society. Purple = the four supporting streams (they enable the chain, dashed arrow); dark green = parties outside the NSO."
flowchart TB
    EXT["External data providers"]:::ext --> chain
    subgraph chain["Primary value streams — the production chain"]
        direction LR
        VS01["VS-01<br/>Acquisition &<br/>Ingestion"] --> VS02["VS-02<br/>Standardization &<br/>Integration"] --> VS03["VS-03<br/>Editing &<br/>Enrichment"] --> VS04["VS-04<br/>Estimation &<br/>Modeling"] --> VS05["VS-05<br/>Product<br/>Composition"] --> VS06["VS-06<br/>Dissemination &<br/>Service Delivery"]
    end
    chain --> USERS["Users & society"]:::ext
    subgraph sup["Supporting value streams"]
        direction LR
        VS07["VS-07<br/>Governance &<br/>Compliance"]:::s
        VS08["VS-08<br/>Innovation &<br/>Methodology"]:::s
        VS09["VS-09<br/>Infrastructure &<br/>Platforms"]:::s
        VS10["VS-10<br/>Customer &<br/>Stakeholder Engagement"]:::s
    end
    sup -.->|"enable"| chain

    classDef ext fill:#0f766e,color:#fff,stroke:#0f766e
    classDef s fill:#7c3aed,color:#fff,stroke:#6d28d9
```

## Steady States of Data

The streams work independently of each other (in architecture terms: they are **loosely coupled**). They exchange data only at defined **steady states** — points where a high-quality, versioned dataset is handed over. Each primary stream consumes one steady state and produces the next, so a stream needs no knowledge of its neighbors' internals (SAF-P07). The handover works through events: when a stream registers a finished dataset, a notification tells the next stream that new data is ready.

The table lists the steady states in the order data passes through them — from data still at the provider (#0) to data in users' hands (#6):

| State | Name | Produced by | Meaning |
|---|---|---|---|
| (#0) | Source Data | *external providers* | Data at the external holder, before it enters the NSO (pre-ingestion; not a numbered SAF state) |
| #1 | Raw Data | VS-01 | Received into NSO custody in original form, with provenance (a record of where it came from and how) and basic validation |
| #2 | Standardized Data | VS-02 | Aligned to common structure, format, and classifications — **values unchanged** |
| #3 | Processed Data | VS-03 | Content validated, edited, imputed, enriched, integrated; derived variables added |
| #4 | Statistics (Output Data) | VS-04 → VS-05 | Estimated/aggregated statistics (VS-04), composed into approved products (VS-05) |
| #5 | Released Data | VS-06 | Disclosure-controlled, documented, published/delivered to external parties |
| #6 | Consumed Data | *external users* | Data in use outside the NSO's direct control |
: Steady States of data {tbl-colwidths="[10,20,20,50]"}

```{mermaid}
%%| label: fig-1
%%| fig-cap: "Steady-state handover across the chain. Each arrow is a handover between streams, triggered by a registration event. Blue = data states inside the NSO; yellow = statistics; light green = released; dark green = outside the NSO's control."
%%| fig-width: 10
flowchart TD
    S0["Source Data"]:::ext -->|VS-01| S1["#1 Raw"]
    S1 -->|VS-02| S2["#2 Standardized"]
    S2 -->|VS-03| S3["#3 Processed"]
    S3 -->|VS-04| S4["#4 Statistics"]
    S4 -->|VS-05| S4b["#4 Approved products"]
    S4b -->|VS-06| S5["#5 Released"]
    S5 --> S6["#6 Consumed"]:::ext

    classDef ext fill:#0f766e,color:#fff,stroke:#0f766e
    style S1 fill:#dbeafe,stroke:#2563eb
    style S2 fill:#dbeafe,stroke:#2563eb
    style S3 fill:#dbeafe,stroke:#2563eb
    style S4 fill:#fef9c3,stroke:#b45309
    style S4b fill:#fef9c3,stroke:#b45309
    style S5 fill:#dcfce7,stroke:#16a34a
```

## The Four-Process Governance Pattern

Every stream is described through the same **four process types**. This is not a one-off sequence but a repeating cycle that keeps quality improving, and each of the four produces a distinct kind of result:

- **Design** — decide how the work should be done: rules, methodology, specifications, policies.
- **Implementation** — build, configure, and test the systems that will do it.
- **Execution** — run the work each production cycle; this is what produces the statistical data.
- **Management** — check quality, monitor performance, and feed improvements back to Design.

The cycle looks like this — note the feedback arrow that closes the loop:

```{mermaid}
%%| label: fig-2
%%| fig-cap: "The four-process governance pattern. Each of the six streams runs this full cycle; the per-stream sections below summarize Design/Implementation/Management and keep the Execution detail."
%%| fig-width: 6
flowchart LR
    D["**Design**
    _metadata_"] -->|"guides building"| I["**Implement**
    _execution process_"]
    I -->|"production-ready"| E["**Execute**
    _statistical data_"]
    E -->|"data & process logs"| M["**Manage**
    _quality reports_"]
    M -->|"improvement feedback"| D

    style D fill:#7c3aed,color:#fff,stroke:#6d28d9
    style I fill:#2563eb,color:#fff,stroke:#1d4ed8
    style E fill:#059669,color:#fff,stroke:#047857
    style M fill:#d97706,color:#fff,stroke:#b45309
```

::: {.callout-note}
In the sections that follow, GSBPM phases are mapped per process type:

- **Design → Phase 2**,
- **Implementation → Phase 3**,
- **Execution → the later GSBPM phases** appropriate to the domain (Phase 4 for collection, Phase 5 for processing, Phase 6 for analysis, Phase 7 for dissemination),
- **Management → overarching Quality Management / Phase 8**.

The four **supporting** streams (VS-07–VS-10) do not follow this production cadence: they run a **continuous plan → build → operate → improve** cycle and align to **GAMSO** rather than GSBPM (see the supporting-streams section).
:::

## Principles to Apply

The SAF defines eleven architecture principles, labeled SAF-P01 to SAF-P11. The six **primary** streams actively apply six of them (marked ★ below); the four **supporting** streams foreground the other five (marked †). The table shows each principle with practical guidance on how to apply it; VS-07 in particular **enforces** the data principles (P09/P10/P11) across the whole chain.

| Principle | Statement | How to apply across the value chain |
|---|---|---|
| **SAF-P01** ★ | Actively participate in open source to maintain collective control over statistical processes | Build statistical capabilities on shared, open tooling; contribute back, so NSOs keep collective control of critical methods rather than depending on vendors. |
| **SAF-P07** ★ | Implement loosely coupled processes and systems | Exchange data only at steady-state interfaces; each stream consumes one state and produces the next without knowing the others' internals. |
| **SAF-P08** ★ | Data is shared property | Once an artefact is registered at a steady state, make it available to all authorized consumers; avoid duplicating collection, processing, or analysis. |
| **SAF-P09** ★ | No data without metadata and classification | Every artefact carries provenance (origin), methodology, accuracy, classification, and lineage (the trace back to its inputs) — captured at the point each value is created or changed. |
| **SAF-P10** ★ | Security By Design | Embed access control, integrity verification, and tamper-evident audit trails in every pipeline from the start. |
| **SAF-P11** ★ | Privacy By Design | Remove/pseudonymize identifiers during standardization; assess disclosure risk on enrichment and apply statistical disclosure control before release. |
| **SAF-P02** † | Active support | Operate and support capabilities as living services, not one-off builds (VS-09 platforms, VS-10 services). |
| **SAF-P03** † | Active Life Cycle management | Version and govern rules, methods, models, and products across their life cycle; retire what is obsolete (VS-07, VS-08). |
| **SAF-P04** † | Maximize the benefits for the organization | Prefer solutions that serve the whole organization and real user value over local optimizations (VS-10, VS-07). |
| **SAF-P05** † | IT and technology is everyone's business | Treat methodology, data, and technology as a shared responsibility across business and IT (VS-08, VS-09). |
| **SAF-P06** † | Business Continuity | Keep the chain running reliably and able to recover from disruption (VS-09). |
: SAF Principles {tbl-colwidths="[10,30,60]"}

★ = actively applied by the six primary value streams. † = foregrounded by the four supporting value streams (VS-07–VS-10).

::: {.callout-important title="Two cross-chain disciplines"}
**Metadata everywhere (SAF-P09):** value is only added once its context is captured — what was done, by which rule/method, with what accuracy, and traceable to its inputs.

**Confidentiality progressively applied (SAF-P11):** identifiers are removed/pseudonymized at standardization (#2), disclosure risk is assessed on enrichment (#3), initial disclosure control is applied to outputs (#4), and final disclosure control gates release (#5).
:::

## VS-01.0 — Data Acquisition and Ingestion

**Domain:** Observation/Collection · **State transition:** Source Data → **#1 Raw Data** · **Value:** all data enters NSO custody, verifiably and with provenance.

VS-01 is the front door of the statistical system. Its job is to bring data from the outside world — survey respondents, administrative registers, and emerging sources such as web or sensor data — into the NSO safely and with a complete record of where it came from. Nothing about the data's content is changed here; the point is to receive it, prove it is what it claims to be, and register it so the rest of the chain can find and trust it. The output is **Raw Data**: the data in its original form, under NSO custody, accompanied by provenance.

**Business processes**

- VS-01.1 Identify Data Needs and Sources
- VS-01.2 Establish Data Agreement and Access Right
- VS-01.3 Collect, Receive, or Extract Data
- VS-01.4 Validate and Log Data Intake
- VS-01.5 Store and Register Raw Data Artefacts

**How the business processes work.** The cycle starts by **identifying the data needs and sources** for the round — confirming what variables and populations are required and that the chosen sources are available and accessible. Once the source is settled, the team **establishes the data agreement and access rights**: activating or renewing the legal basis (a data-sharing agreement, or the relevant GDPR ground) and checking that credentials are valid, so collection is lawful and controlled. Data is then **collected, received, or extracted** through the appropriate channel — a survey instrument, an administrative file transfer, or an API/scraping job — and at the moment of receipt the ingestion metadata (source, method, timestamp, file hash, volume) is captured. Each delivery is **validated and logged**: completeness, structure, and integrity are checked and every result written to an audit trail, so the NSO can be confident the intake is whole and traceable. Finally the dataset is **stored and registered as a raw-data artefact** — given a persistent identifier, kept in its original form, and cataloged with its provenance — and a "Raw Data Registered" event tells VS-02 that new data is ready.

::: {.callout-note title="Signature discipline — no data without metadata"}
Every dataset is enriched at ingestion with provenance, source, method, timestamp, and a quality and BIV classification — availability, integrity, confidentiality — per SAF-P09, with security and privacy applied by design (SAF-P10/P11).
:::

Around this per-cycle run, **Design** prepares the data requirements, collection methodology, raw-data schema, validation rules, and access/privacy framework; **Implementation** builds the collection instruments and ingestion/validation workflows and tests them; and **Management** monitors response, timeliness, and rejection rates, assesses intake quality, and feeds improvements back to design.

| Business process | What it produces |
|---|---|
| VS-01.1 Identify Data Needs and Sources | Confirmed requirements and available sources for the cycle |
| VS-01.2 Establish Data Agreement and Access Right | Active, lawful access (agreements, GDPR basis, credentials) |
| VS-01.3 Collect, Receive, or Extract Data | Data in NSO custody + captured ingestion metadata |
| VS-01.4 Validate and Log Data Intake | Validated intake + audit trail |
| VS-01.5 Store and Register Raw Data Artefacts | Registered Raw Data artefact + "Raw Data Registered" event |

**Boundaries:** in — Source Data from external providers; out — **Raw Data** on *"Raw Data Registered"* → VS-02.

## VS-02.0 — Data Standardization and Integration

**Domain:** Standardization without loss of content · **State transition:** #1 Raw → **#2 Standardized** · **Value:** coherence and comparability across sources.

VS-02 makes data from different sources speak the same language. After raw data is in custody, this stream aligns its structure, format, and codes to the NSO's agreed standards so that datasets which looked different at the source can be compared and combined. Crucially it does this **without changing any value** — it re-expresses and annotates, it does not transform. The output is **Standardized Data**: the same information, now in a common shape, expressed in standard classifications, and carrying rich metadata.

**Business processes**

- VS-02.1 Profile and Assess Data Structure
- VS-02.2 Apply Standard Classifications and Formats
- VS-02.3 Align Metadata and Semantics
- VS-02.4 Validate Structural and Semantic Conformance
- VS-02.5 Register Standardized Artefacts

**How the business processes work.** The stream first **profiles and assesses the incoming structure**, comparing it against the target data model to see which fields map directly, which simply need reformatting, which source codes have a standard correspondence, and which values are uncoded. It then **applies standard classifications and formats**: source codes are mapped one-to-one to standards (for example a source activity code to NACE, the European industry classification) through maintained correspondence tables, and the layout is coerced into the common format (renaming, restructuring, type-casting, e.g. CSV→XML). The original values are preserved, and anything that has no deterministic correspondence — or is free text needing interpretation — is flagged and passed downstream to VS-03. Next it **aligns metadata and semantics**: variables are linked to canonical concepts, and each variable's unit, currency, and reference-period basis (and any differing cross-source definitions) are *recorded as metadata* rather than converted. The result is **checked for structural and semantic conformance**, including a no-loss-of-content check confirming that record counts and key measures are unchanged. Conformant data is then **registered as a standardized artefact** with its mapping lineage, and a "Standardized Data Registered" event notifies VS-03.

::: {.callout-note title="Signature discipline — standardization without loss of content"}
VS-02 only maps codes 1-to-1, coerces format/structure, and annotates metadata. It **never changes a value**; unit/currency conversion, reference-period alignment, value reconciliation, and interpretive free-text coding are deliberately deferred to VS-03.
:::

Around this, **Design** defines the target data model, the deterministic classification correspondences, the harmonization and conformance rules, and the privacy framework; **Implementation** builds the mapping & format-coercion component, the classification-mapping services, the conformance pipeline, and identifier pseudonymization; **Management** tracks mapping coverage and the unmapped-value rate, governs classification versions, and improves the correspondences.

| Business process | What it produces |
|---|---|
| VS-02.1 Profile and Assess Data Structure | A structure-gap assessment against the target model |
| VS-02.2 Apply Standard Classifications and Formats | Standard-coded, common-format data (values unchanged); unmapped values flagged for VS-03 |
| VS-02.3 Align Metadata and Semantics | Canonical-concept links + unit/period/definition metadata |
| VS-02.4 Validate Structural and Semantic Conformance | Conformance result + no-loss-of-content confirmation |
| VS-02.5 Register Standardized Artefacts | Registered Standardized Data + "Standardized Data Registered" event |

**Boundaries:** in — Raw Data on *"Raw Data Registered"*; out — **Standardized Data** on *"Standardized Data Registered"* → VS-03.

## VS-03.0 — Data Editing and Enrichment

**Domain:** Editing, derivation, and non-response correction · **State transition:** #2 Standardized → **#3 Processed** · **Value:** data reliability and analytical readiness.

VS-03 is where data quality is actively improved. Standardized data is rarely clean — it contains errors, inconsistencies, gaps, and not-yet-coded values. This stream detects those problems, corrects them, fills the gaps, and derives the extra variables analysis needs. Uniquely in the chain, it **deliberately changes values to do so**. What makes that safe is total traceability: every change is recorded against its original value and a reproducible, versioned dataset is produced. The output is **Processed Data**: reliable, complete, analytically ready microdata.

**Business processes**

- VS-03.1 Conduct Error Detection / Quality Diagnostics
- VS-03.2 Perform Data Editing and Correction
- VS-03.3 Impute Missing or Non-Response Data
- VS-03.4 Derive Additional Variables and Indicators
- VS-03.5 Perform Quality Evaluation and Versioning

**How the business processes work.** The stream begins by **detecting errors and running quality diagnostics** — consistency, range, outlier, and duplicate checks — and uses selective-editing scores to prioritize the problems that actually matter for the results. It then **performs editing and correction**: low-impact issues are auto-corrected by rule while high-impact records are reviewed by subject-matter analysts, and this is where the interpretive work VS-02 deferred is carried out (coding free-text values such as occupation to ISCO, the international occupation classification, and reconciling values where integrated sources disagree). Every change logs the original value, the rule or decision, the reason, the actor, and the time. Genuine gaps are then closed by **imputing missing or non-response data** using approved methods, with each imputed value clearly flagged so it stays distinguishable from observed data. The dataset is **enriched by deriving additional variables and indicators** — and this is also where unit/currency conversion and reference-period alignment are computed from the bases VS-02 recorded, and where datasets are integrated on common keys. Finally the stream **evaluates quality and versions the result**: it measures the improvement against the incoming baseline, verifies the edit lineage is complete and reversible, and creates an immutable Processed Data version, signaled to VS-04 by a "Processed Data Registered" event.

::: {.callout-note title="Signature discipline — full traceability"}
VS-03 is the domain that changes values, under the guarantee of *no undocumented or irreversible change*: original values are preserved beside edited ones, imputations are flagged, and every version is reproducible.
:::

Around this, **Design** sets the error-detection and editing rules (with a selective-editing strategy), the imputation methodology, the derivation and coding specs, the integration rules, and the versioning policy; **Implementation** builds the editing, imputation, coding, derivation, and integration engines and the version store; **Management** watches edit, imputation, and over-editing rates, assesses quality improvement, and audits the edit lineage.

| Business process | What it produces |
|---|---|
| VS-03.1 Conduct Error Detection / Quality Diagnostics | A prioritized diagnosis of errors and gaps |
| VS-03.2 Perform Data Editing and Correction | Corrected values + interpretive coding + full edit lineage |
| VS-03.3 Impute Missing or Non-Response Data | Completed data with imputation flags |
| VS-03.4 Derive Additional Variables and Indicators | Derived variables + unit/currency/period conversions + integrated data |
| VS-03.5 Perform Quality Evaluation and Versioning | Versioned Processed Data + "Processed Data Registered" event |

**Boundaries:** in — Standardized Data on *"Standardized Data Registered"*; out — **Processed Data** on *"Processed Data Registered"* → VS-04.

## VS-04.0 — Estimation, Analysis, and Statistical Modeling

**Domain:** Estimation and closed-loop · **State transition:** #3 Processed → **#4 Statistics** · **Value:** analytical insight and statistical credibility.

VS-04 turns clean microdata into statistics. Up to now the chain has improved the data itself; here the focus shifts to producing numbers that describe a population — estimates, weighted aggregates, indices, and model results. The microdata is not edited further; instead statistics are computed *from* it, each accompanied by a measure of how accurate it is. The output is **Output Data / Statistics**: validated figures with their methodology and accuracy attached, and an initial layer of confidentiality protection applied.

**Business processes**

- VS-04.1 Confirm Estimation and Analytical Approach
- VS-04.2 Apply Weighting and Calibration
- VS-04.3 Estimate and Aggregate Data
- VS-04.4 Perform Model-Based Analysis
- VS-04.5 Validate and Document Results

**How the business processes work.** Each round starts by **confirming the estimation and analytical approach** — selecting the pre-approved method for this cycle's data and checking that the calibration totals and domains are current. The stream then **applies weighting and calibration** to correct for sampling, non-response, and coverage, so the sample represents the population. With weights in place it **estimates and aggregates the data**, producing the target statistics together with their accuracy (standard errors and confidence intervals) — and because VS-03 flagged which values were imputed, that added uncertainty is reflected in the variance. Where direct figures are not enough, it **performs model-based analysis** (regression, time-series/forecasting, small-area models) to reveal relationships and produce reliable estimates for thin domains, recording the model diagnostics. Finally it **validates and documents the results**: checking statistical soundness and coherence with related and prior statistics, applying an initial layer of statistical disclosure control so the figures can potentially be released, documenting the methodology, and versioning the output — announced to VS-05 by an "Output Data Registered" event.

::: {.callout-note title="Signature discipline — methodological transparency"}
Every estimate carries the method, parameters, and accuracy measure that produced it and can be regenerated; imputation uncertainty from VS-03 is reflected in the variance, and initial statistical disclosure control is applied so output can potentially be released.
:::

Around this, **Design** fixes the estimation strategy and accuracy approach, the weighting/calibration methodology, the aggregation and model specifications, and the validation and disclosure-control policy; **Implementation** builds the weighting, estimation, variance, and modeling engines and the disclosure-control and version tooling; **Management** tracks accuracy, timeliness, and revisions, assesses coherence, and audits reproducibility.

| Business process | What it produces |
|---|---|
| VS-04.1 Confirm Estimation and Analytical Approach | The pre-approved method confirmed for the cycle |
| VS-04.2 Apply Weighting and Calibration | Weights that make the sample represent the population |
| VS-04.3 Estimate and Aggregate Data | Estimates and aggregates, each with an accuracy measure |
| VS-04.4 Perform Model-Based Analysis | Model/forecast/small-area results with diagnostics |
| VS-04.5 Validate and Document Results | Validated, disclosure-controlled, versioned statistics + "Output Data Registered" event |

**Boundaries:** in — Processed Data on *"Processed Data Registered"*; out — **Output Data** on *"Output Data Registered"* → VS-05.

## VS-05.0 — Statistical Product Composition

**Domain:** Statistically composed and composite products · **State transition:** within **#4 Statistics** (analytical outputs → approved products) · **Value:** coherence and interpretability.

VS-05 assembles finished products from the statistics VS-04 produced. Individual estimates are not yet something a user reads; this stream brings results from different domains, surveys, and time periods together into coherent publications, time series, indices, and datasets — and approves them for release. It does not re-estimate anything; it selects, combines, checks, explains, and signs off. The output is an **approved, registered statistical product** ready for dissemination.

**Business processes**

- VS-05.1 Select and Integrate Source Datasets
- VS-05.2 Construct Composite Indicators or Indices
- VS-05.3 Perform Consistency and Coherence Checks
- VS-05.4 Generate Analytical and Interpretive Outputs
- VS-05.5 Approve and Register Statistical Products

**How the business processes work.** The stream first **selects and integrates the source datasets** — picking the exact validated output versions a product needs and combining them, carrying their accuracy metadata along. It then **constructs the composite indicators or indices** the product presents (ratios, indices, chained time series), deriving each composite's uncertainty from its components. The assembled product is put through **consistency and coherence checks**: totals must reconcile to their parts, and the figures must agree with related statistics and with prior releases — discrepancies are explained or sent back, never quietly adjusted. Next the stream **generates the analytical and interpretive outputs** — the commentary, key messages, tables, and visualizations that make the product understandable — and runs them through editorial review. Finally it **approves and registers the product**: validating it against dissemination and confidentiality standards, obtaining sign-off from the designated authority, and registering an immutable version with full lineage, which a "Statistical Product Registered" event passes to VS-06.

::: {.callout-note title="Signature discipline — coherence and interpretability"}
VS-05 **composes** validated outputs (it does not re-estimate). Products are internally consistent, coherent with related and prior statistics, carry their components' accuracy metadata, and are **approved against dissemination and confidentiality standards** before being registered.
:::

Around this, **Design** defines the product portfolio, the composite-indicator specs, the coherence checks, the content templates, and the approval/confidentiality/versioning framework; **Implementation** builds the integration and composition engines, the indicator/time-series engines, the coherence and content tooling, and the approval/version store; **Management** tracks coherence-check pass rates and approval iterations, assesses product quality, and audits reproducibility and approval.

| Business process | What it produces |
|---|---|
| VS-05.1 Select and Integrate Source Datasets | Integrated components with accuracy carried forward |
| VS-05.2 Construct Composite Indicators or Indices | Composite measures and time series |
| VS-05.3 Perform Consistency and Coherence Checks | Confirmed internal consistency and coherence |
| VS-05.4 Generate Analytical and Interpretive Outputs | Reviewed narrative, tables, and visualizations |
| VS-05.5 Approve and Register Statistical Products | Approved, versioned product + "Statistical Product Registered" event |

**Boundaries:** in — Output Data on *"Output Data Registered"*; out — **Approved Statistical Product** on *"Statistical Product Registered"* → VS-06.

## VS-06.0 — Dissemination and Service Delivery

**Domain:** Dissemination (final stage) · **State transition:** #4 Approved products → **#5 Released** → #6 Consumed · **Value:** impact and accessibility.

VS-06 is the chain's exit point — where approved products become public value. It publishes and delivers statistics to policymakers, researchers, journalists, businesses, and the public through trusted, secure channels, and supports users in interpreting them correctly. The decisive control here is confidentiality: a final disclosure-control gate stands between an approved product and release. The output is **Released Data** (State #5); once in users' hands it becomes **Consumed Data** (State #6), beyond the NSO's direct control.

**Business processes**

- VS-06.1 Plan Dissemination and Access Strategy
- VS-06.2 Prepare Data for Dissemination
- VS-06.3 Publish and Provide Access Services
- VS-06.4 Support and Engage Users
- VS-06.5 Monitor Usage and Feedback

**How the business processes work.** Each release begins by **confirming the dissemination and access plan** — the channels (publication, API/open data, dashboards, secure research access), the formats, the release-calendar slot, and the embargo/equal-access arrangements. The product is then **prepared for dissemination**: final statistical disclosure control is applied (suppression, rounding, perturbation; de-identification of any microdata) and the release must clear the disclosure-risk criteria — *nothing proceeds if it does not* — after which it is formatted for each channel and packaged with its documentation and metadata. The stream then **publishes and provides access services**, releasing the product and its metadata across the confirmed channels with timing managed so that access is equal (no privileged early sight outside policy). It **supports and engages users** with documentation, a helpdesk, training, and errata, so the statistics are interpreted responsibly. Finally it **monitors usage and feedback** — tracking downloads, API calls, and dashboard views, and collecting satisfaction and questions — and routes those insights back to design, to VS-10, and across the chain. The release is signaled by a "Statistics Released" event.

::: {.callout-note title="Signature discipline — accessibility, trust, and the release gate"}
Accurate, timely, understandable delivery through secure channels, gated by **final statistical disclosure control** (no release without confidentiality clearance) and supported by documentation that enables responsible, equal-access use. VS-06 relies on the supporting streams VS-07 (compliance), VS-09 (platforms), and VS-10 (user needs).
:::

Around this, **Design** sets the dissemination and access strategy, the final disclosure-control and de-identification rules, the channels/formats/documentation standards, and the release governance; **Implementation** builds the publication, API, dashboard, and secure-research-access services (on VS-09 platforms) and the disclosure-control and release tooling; **Management** monitors punctuality, usage, and satisfaction, assesses accessibility, and audits disclosure and equal-access compliance with VS-07.

| Business process | What it produces |
|---|---|
| VS-06.1 Plan Dissemination and Access Strategy | Confirmed channels, formats, and release timing |
| VS-06.2 Prepare Data for Dissemination | Disclosure-safe, channel-ready products + documentation |
| VS-06.3 Publish and Provide Access Services | Released statistics across channels, equally and on time |
| VS-06.4 Support and Engage Users | User documentation, helpdesk, training, errata |
| VS-06.5 Monitor Usage and Feedback | Usage insight + feedback routed to design and VS-10 |

**Boundaries:** in — Approved Statistical Product on *"Statistical Product Registered"*; out — **Released Data** on *"Statistics Released"* → users/society (consumed as State #6). No downstream primary stream; feedback returns to VS-10.

## Supporting Value Streams (VS-07 to VS-10)

The four supporting streams are not stages in the production line — they work **across the whole chain**, enabling and constraining all six primary streams continuously. Reading their sections requires a small shift of mindset from the six above.

::: {.callout-important title="How a supporting value stream differs from a production stream"}
- **No steady-state data transition.** A supporting stream does not take data from one state to the next; it does not appear in the #1→#6 chain. There is no "Data Registered" handover event and no "Boundaries: in→out" — instead each interacts with the whole chain at once.
- **It runs continuously**, as a plan → build → operate → improve cycle, not per production cycle.
- **Its output is an enabling capability, not data:** governance & assurance (07), validated methods (08), platforms (09), understood needs & relationships (10).
- **It aligns to GAMSO** — the standard model of management and support activities (Strategy & Leadership, Capability Management, Corporate Support) — rather than to GSBPM production phases, and it foregrounds principles **P02–P06**.
:::

The diagram shows the two directions of that interaction: the supporting streams provide capabilities to the chain (arrows in), and the chain sends back evidence, needs, and usage (arrow out):

```{mermaid}
%%| label: fig-3
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

## VS-07.0 — Governance and Compliance

**Domain:** Governance (horizontal) · **GAMSO:** Strategy & Leadership + Corporate Support · **Value:** integrity and accountability.

VS-07 makes sure every process, dataset, and product operates under clear rules, standards, and accountability. It builds trust by ensuring all data activities are ethical, transparent, and compliant with legal, methodological, and quality requirements (Code of Practice, GDPR, ISO). It does not move data along the chain — it **oversees** the streams that do, and is the place where the data principles (P09/P10/P11) are enforced organization-wide.

**Business processes**

- VS-07.1 Define Governance Frameworks and Policies
- VS-07.2 Establish Legal and Regulatory Compliance Mechanisms
- VS-07.3 Implement Data and Metadata Governance
- VS-07.4 Monitor Quality and Compliance Indicators
- VS-07.5 Audit, Certify, and Report Compliance
- VS-07.6 Update and Improve Governance Mechanisms

**How the business processes work.** Governance runs as a continuous loop. It first **defines governance frameworks and policies** (07.1) — the charters and principles covering data, metadata, ethics, confidentiality, and quality — and **establishes legal and regulatory compliance mechanisms** (07.2), mapping applicable regulation to concrete procedures. These are made operational by **implementing data and metadata governance** (07.3): assigning the owner/steward/custodian roles and the metadata and lineage processes that wire governance into how the streams work. It then **monitors quality and compliance indicators** (07.4) on dashboards and periodically **audits, certifies, and reports compliance** (07.5), producing the assurance that the statistics can be trusted. Finally it **updates and improves the governance mechanisms** (07.6), folding regulatory change and lessons learned back into the policies. *(The strategy model labels two steps `VS-07.5`; the second is treated here as VS-07.6.)*

**Interaction with the chain:** provides frameworks, roles, and controls to all streams and receives their compliance evidence, quality indicators, and audit findings (each primary stream's audit-and-compliance reporting feeds here); issues certification and assurance to regulators and the public.

| Business process | What it produces |
|---|---|
| VS-07.1 Define Governance Frameworks and Policies | Governance charters and policies |
| VS-07.2 Establish Legal and Regulatory Compliance Mechanisms | Compliance procedures mapped to regulation |
| VS-07.3 Implement Data and Metadata Governance | Assigned roles + metadata/lineage processes |
| VS-07.4 Monitor Quality and Compliance Indicators | Quality & compliance dashboards |
| VS-07.5 Audit, Certify, and Report Compliance | Audit reports, certifications, assurance |
| VS-07.6 Update and Improve Governance Mechanisms | Revised policies and controls |

## VS-08.0 — Innovation and Methodological Development

**Domain:** Innovation (horizontal) · **GAMSO:** Capability Management · **Value:** continuous improvement / future-proofing.

VS-08 keeps the organization from standing still: it discovers, tests, and introduces new data sources, methods, tools, and technologies, connecting research, methodology, IT, and business users. It keeps innovation **controlled** so that only sound, documented, compliant methods reach production. It does not transform data — it improves the methods and tools the production streams use.

**Business processes**

- VS-08.1 Identify Innovation Needs and Opportunities
- VS-08.2 Conduct Research and Proof-of-Concepts
- VS-08.3 Evaluate Methodological Soundness and Feasibility
- VS-08.4 Develop / Document New Methodologies or Tools
- VS-08.5 Integrate Innovation into Production Environments
- VS-08.6 Promote Knowledge Sharing and Capability Building

**How the business processes work.** The pipeline begins by **identifying innovation needs and opportunities** (08.1) — scanning technology and methodology (AI, ML, new sources) and the chain's own improvement backlog — then runs **research and proofs-of-concept** (08.2) in limited scope. Promising results pass through **evaluation of methodological soundness and feasibility** (08.3), the gate that stops attractive-but-unsound ideas, and are then **developed and documented into methods or tools** (08.4) — standardized procedures and reference implementations ready to hand over. The defining step is **integrating innovation into production** (08.5): the governed transfer of a validated method into the relevant primary stream (after VS-07 approval, on VS-09 platforms). Finally it **promotes knowledge sharing and capability building** (08.6), disseminating guidance and growing staff competency — which surfaces the next round of needs.

**Interaction with the chain:** receives improvement needs from every primary stream (their continuous-improvement loops) and user-driven needs from VS-10; **delivers validated methods and tools into production** through the 08.5 transfer gate.

| Business process | What it produces |
|---|---|
| VS-08.1 Identify Innovation Needs and Opportunities | Prioritized innovation backlog |
| VS-08.2 Conduct Research and Proof-of-Concepts | Experiment / pilot results |
| VS-08.3 Evaluate Methodological Soundness and Feasibility | Soundness & feasibility assessment |
| VS-08.4 Develop / Document New Methodologies or Tools | Standardized method + reference implementation |
| VS-08.5 Integrate Innovation into Production Environments | Method/tool live in a production stream (governed transfer) |
| VS-08.6 Promote Knowledge Sharing and Capability Building | Disseminated guidance + trained staff |

## VS-09.0 — Infrastructure and Platform Enablement

**Domain:** Infrastructure (horizontal) · **GAMSO:** Capability Management + Corporate Support · **Value:** reliable enablement at scale.

VS-09 provides the technical and digital foundation every other stream runs on — environments, data platforms, tools, and integration services — keeping them secure, resilient, and compliant while flexible enough to adopt new technology. It is the business-layer view of providing the application and technology enablement the primary documents scoped out.

**Business processes**

- VS-09.1 Define Digital and Technical Requirements
- VS-09.2 Design Platform and Infrastructure Architecture
- VS-09.3 Provision and Configure Platforms
- VS-09.4 Enable Integration and Orchestration Services
- VS-09.5 Ensure Performance, Security, and Continuity
- VS-09.6 Evolve and Modernize the Technical Ecosystem

**How the business processes work.** The lifecycle begins by **defining digital and technical requirements** (09.1) from business capabilities and data volumes, feeding the **design of the platform and infrastructure architecture** (09.2) — blueprints for storage, processing, integration, and secure access. The architecture is realized by **provisioning and configuring platforms** (09.3) with governance, monitoring, and security controls, and by **enabling integration and orchestration services** (09.4) — the APIs, workflow engines, and the event interfaces the steady-state handovers rely on. Day to day it **ensures performance, security, and continuity** (09.5): monitoring, data protection, incident management, and disaster recovery. Finally it **evolves and modernizes the technical ecosystem** (09.6), adopting new technology (often from VS-08) and retiring the obsolete.

**Interaction with the chain:** provides environments, platforms, integration, and assured availability to all streams (including VS-06's portals/APIs and VS-08's sandboxes); receives requirements, capacity demand, and incidents; its security and continuity posture is governed by VS-07.

| Business process | What it produces |
|---|---|
| VS-09.1 Define Digital and Technical Requirements | Infrastructure requirements from business needs |
| VS-09.2 Design Platform and Infrastructure Architecture | Architecture blueprints |
| VS-09.3 Provision and Configure Platforms | Deployed, controlled environments |
| VS-09.4 Enable Integration and Orchestration Services | APIs, workflow/automation, event interfaces |
| VS-09.5 Ensure Performance, Security, and Continuity | Monitoring, security, availability, DR |
| VS-09.6 Evolve and Modernize the Technical Ecosystem | Modernization roadmap and adopted technology |

## VS-10.0 — Customer and Stakeholder Engagement

**Domain:** Engagement (horizontal) · **GAMSO:** Strategy & Leadership + Corporate Support · **Value:** relevance and public value.

VS-10 keeps the organization connected, relevant, and responsive — building mutual understanding and trust with users, data providers, partners, and policymakers. It is a continuous two-way dialogue: it does not move data, it moves **understanding** — needs in, communication and services out.

**Business processes**

- VS-10.1 Identify and Segment Stakeholders
- VS-10.2 Collect and Analyze User Needs
- VS-10.3 Define and Manage Service Portfolios
- VS-10.4 Deliver Services and Manage Relationships
- VS-10.5 Engage and Communicate with Stakeholders
- VS-10.6 Monitor Impact and Satisfaction

**How the business processes work.** The cycle begins by **identifying and segmenting stakeholders** (10.1) and **collecting and analyzing user needs** (10.2), translating them into data or service requirements. Those needs shape the **definition and management of service portfolios** (10.3) — catalogs of services and products aligned to strategy. Services reach users through **delivering services and managing relationships** (10.4) — support desks, account management, satisfaction monitoring — alongside **engaging and communicating with stakeholders** (10.5) via outreach and knowledge-sharing. Finally it **monitors impact and satisfaction** (10.6), measuring use and societal impact and feeding insight back into planning and innovation.

**Interaction with the chain:** bidirectional with VS-01 (the data providers it engages) and VS-06 (whose usage and feedback it receives); it routes user needs into design across the primary streams and into VS-08's innovation backlog.

| Business process | What it produces |
|---|---|
| VS-10.1 Identify and Segment Stakeholders | Stakeholder map and segments |
| VS-10.2 Collect and Analyze User Needs | Needs register / service requirements |
| VS-10.3 Define and Manage Service Portfolios | Service & product portfolio |
| VS-10.4 Deliver Services and Manage Relationships | Operating support & managed relationships |
| VS-10.5 Engage and Communicate with Stakeholders | Outreach, communication, awareness |
| VS-10.6 Monitor Impact and Satisfaction | Impact & satisfaction insight (fed back to the chain) |

## The Value Chain at a Glance

Use these two tables as a quick reference: the first summarizes the six production streams, the second the four supporting streams.

| VS | Domain | State in → out | Trigger out | Signature discipline |
|---|---|---|---|---|
| **01** | Acquisition & Ingestion | Source → #1 Raw | Raw Data Registered | Metadata & validation at ingestion |
| **02** | Standardization & Integration | #1 → #2 Standardized | Standardized Data Registered | No loss of content — map, coerce, annotate |
| **03** | Editing & Enrichment | #2 → #3 Processed | Processed Data Registered | Full traceability of every value change |
| **04** | Estimation & Modeling | #3 → #4 Statistics | Output Data Registered | Methodological transparency + accuracy + initial disclosure control |
| **05** | Product Composition | within #4 (→ approved) | Statistical Product Registered | Coherence & interpretability; approval before registration |
| **06** | Dissemination & Service Delivery | #4 → #5 Released → #6 | Statistics Released | Accessibility & trust; final disclosure-control gate |

The four supporting streams work differently — they have no state transition; they run horizontally and continuously:

| VS | Domain | GAMSO area | What it provides to the chain | Principles foregrounded |
|---|---|---|---|---|
| **07** | Governance & Compliance | Strategy & Leadership; Corporate Support | Frameworks, controls, assurance; enforces the data principles | P03, P04 (+ enforces P09/P10/P11) |
| **08** | Innovation & Methodological Development | Capability Management | Validated methods & tools transferred into production | P01, P05, P03, P04 |
| **09** | Infrastructure & Platform Enablement | Capability Management; Corporate Support | Platforms, environments, integration, continuity | P10, P06, P02, P05 |
| **10** | Customer & Stakeholder Engagement | Strategy & Leadership; Corporate Support | Understood needs, service portfolio, relationships, impact | P04, P08, P02 |

::: {.callout-note}
This consolidated view omits the per-stream **"Applying This to Your NSO"** maturity checklists and scenarios. For those, and for the full Design / Implementation / Management detail, diagrams, and boundary-interface tables, see the individual documents `VS-01.0` … `VS-10.0` in this folder.
:::
