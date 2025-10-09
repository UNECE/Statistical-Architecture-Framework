# SAF Architecture Framework
Created on: 07-07-2025
Contributers: Pascal Fransen (CBS), Trygve Falch (Statistics Norway), Jakob Engdahl (Statistics Sweden), Stephane Crete (Statistics Canada), Cedric Couralet (Insee), Daan Swinkels (CBS)
Version 0.1


## Content

Introduction
Activity Proposal
Definition of Scope
Target Audience
Constraints & Assumptions
Goals and Drivers
Architecture Principles
Stakeholders, Roles and Collaborations
Capability Model
Business Architecture


## Introduction


## Activity Proposal


## Definition of Scope


## Target Audience


## Constraints & Assumptions


## Goals and Drivers


## Architecture Principles


## Stakeholders, Roles and Collaborations


## Capability Model


## Business Architecture

### Overview 

The statistical process is divided into three main business domains (observation, processing/analysis, and dissemination), with processing/analysis further divided into four subdomains. This results in a total of six business domains:

* Observation/Collection
* Processing/analysis
    * Standardization without loss of content
    * Editing, derivation, and non-response correction
    * Estimation and closed-loop
    * Statistically composed and composite statistical products
* Dissemination

Each of the business domains use the following processes :

* Design of the execution processes; provides metadata
* Implementation of the execution processes; provides the execution process
* Execution of the execution processes; provides the statistical data
* Management of the execution processes; provides quality reports

Each domain focuses on adding a specific statistical value to some data. Once sufficient value has been added, a so-called quality version is versioned that must be kept and potentially shared to some consumers. This careful approach is crucial due to the growing interest in our microdata, combined with the increasing focus on privacy. If we combine the added values of the six business domains, a value chain of statistical data is created.

To realize statistical value within a business domain, execution processes (including governance) have been designed and implemented. How an execution process adds statistical value, and is therefore designed and implemented, falls outside the scope of the B&I architecture. This framework must stem from, among other things, the methodology set.

![Generic Business Architecture](images/Business%20Architecture_GSBPM_Data%20Steady%20State_visual_v0.1.png)

The execution processes between the business domains are loosely coupled. Each has its own design and implementation. For the mutual exchange of data, they are loosely linked via steady state interfaces. To this end, five steady state phases are recognized that exist between the business domains: [1] raw data, [2] standardized data without loss of content, [3] processed data, [4] statistics, and [5] released data. An steady state phase is therefore an environment where high-quality versions of data are brought together for exchange, but it also represents a value in the value chain of this data.

Each of the mentioned business domain can be linked to a GSBPM phase.


### Steady States of Data and Their Business Process Links


The business architecture leverages a data value chain approach where data progresses through predefined steady states, each representing a stage where data meets specific quality criteria and is ready for exchange between business domains. These steady states serve as handover points in the statistical production process, ensuring consistency, reusability, and quality control as well as interoperability across other ONS.

#### State #1: Raw Data

**Business Domain Link:** Observation/Collection

**Description:** Raw data represents the initial entry point where data has been received from external data holders and checked for basic safety and validation. At this stage, data has entered the NSO system in its original form as received from the data provider.

**Quality Requirements:**
- File integrity checks completed
- Virus and security scans performed
- SLA requirements verified with the data provider (e.g., completeness, delivery time)
- Data stored in its original format or equivalent

**ONS Use:** Raw data for the raw source data in its original form as received from the data holder. The ONS does not have access to the data at the source; this is the first point of possession.

**Key Characteristics:**
- Data has not been further validated for content
- Sender verification completed
- Technical checks and transformations on the technical level only (not content level)
- Forms the baseline for all subsequent processing

#### State #2: Standardized Data

**Business Domain Links:** Standardization without loss of content

**Description:** Standardized data has been transformed, formatted, and structured according to defined standards. This is the first point at which interoperability between domains is enabled through common classifications and standardized formats.

**Quality Requirements:**
- Format and structure standardized (e.g., converted from CSV to XML)
- Common classifications and code lists applied (e.g., geocoding, economic activity classifications)
- Variables mapped to enterprise standards
- Reference periods harmonized
- Confidentiality measures applied (e.g., pseudonymisation, data minimization)
- Data must not contain personally identifiable information

**ONS Use:** Standardized data based on the received raw data, enabling data integration and interoperability across the organization.

**Key Processing Activities:**
- Application of reference data and master data
- Restructuring and reformatting to NSO's standard storage format
- Recoding of variables to align with enterprise standards
- Pseudonymisation and encryption where required
- Value sets adapted to organizational standards

**Interoperability Benefit:** This state enables data from different sources to be combined and used across multiple statistical products, reducing duplication and increasing efficiency.

#### State #3: Processed Data

**Business domain Links:** Editing, derivation, and non-response correction

**Description:** Processed data has undergone content-related validation, editing, and enrichment. Data accuracy has been improved through validation checks and corrective measures. This data is ready to be integrated with other datasets.

**Quality Requirements:**
- Completeness and accuracy improved through validation and editing
- Data integrity checks completed
- Filtering, editing, or imputation applied as needed
- Data lineage documented
- Integration with other datasets completed where applicable
- New derived variables calculated

**ONS Use:** Processed data for the processed statistical microdata, ready for statistical analysis and production.

**Key Processing Activities:**
- Data cleansing and editing (content-related standardization)
- Integration with other datasets
- Validity checking and error correction
- Imputation of missing values
- Creation of new variables through calculation or derivation
- Flagging of problematic values

**Domain Responsibility:** While this processing is primarily driven by individual statistical domains, depending on the data type, it may be performed by a central unit for efficiency and consistency.

**Reusability Focus:** Processed data aims to be as reusable as possible for other processes or units, reducing duplication of data and processing effort while increasing transparency.

#### State #4: Output Data (Statistics)

**Business Domain Links:** Estimation and closed-loop + Statistically composed and composite statistical products

**Description:** Output data represents statistics that have been aggregated and analyzed, or microdata that has been prepared for specific purposes. Confidentiality measures have been applied to allow potential release.

**Quality Requirements:**
- Data lineage fully documented
- Aggregation and analysis completed
- Confidentiality measures applied
- Statistical estimates calculated
- Quality indicators produced
- Internal review completed

**ONS Use:** Statistics for basic statistics and integrated macrostatistics. These may be used internally by other statistical processes or prepared for dissemination.

**Key Characteristics:**
- Statistics will usually be aggregated data or estimated sizes
- May contain confidential and detailed data not yet suitable for publication
- Can be shared internally for use as input data in other statistical processes, especially macro statistics
- Estimated statistical target quantities produced
- Different confidentiality thresholds may apply depending on intended use

**Domain-Driven Production:** The type of outputs and specific processing methods vary significantly by statistical domain and product requirements.

#### State #5: Published Output Data (Released Data)

**Business Process Links:** Disseminate

**Description:** Published output data has been fully vetted, confidentiality requirements have been satisfied, and the data has been released or published for external use.

**Quality Requirements:**
- Higher confidentiality criteria applied
- Stronger documentation requirements met
- Data lineage fully traceable
- Quality reports completed
- Release authorization obtained
- Metadata and documentation suitable for external users

**ONS Use:** Released data for all data to be disseminated publicly or delivered to authorized external parties.

**Key Characteristics:**
- All requirements for confidentiality taken care of
- May be further processed compared to State #4 for additional confidentiality protection
- Published by the NSO or delivered to external parties
- Includes both published statistical values and delivered microdata (de-identified)
- Strict documentation requirements to support user understanding and data reuse

**External Consumption:** This is the final state in the value chain where statistical information fulfills the core mission of the NSO—delivering trusted statistics to society.

#### State #6: Consumed Data

**Description:** Data that has been used by external parties for their own purposes. This represents data outside the direct control of the ONS.

**ONS Use:** None - Consumed data is data used by external data consumers for their analyses and decision-making.

**Key Characteristic:** This state recognizes that once data is published, it enters the public domain and is used in ways that may be beyond the NSO's direct oversight, though the quality and documentation provided in State #5 support appropriate use.


