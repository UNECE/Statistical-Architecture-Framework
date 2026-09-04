SAF Architecture Framework
============================

Created on: 07-07-2025
Workgroup SAF: Trygve Falch (Statistics Norway, SSB), Jakob Engdahl (Statistics Sweden, SCB), Stephane Crete (Statistics Canada, StatCan), Cedric Couralet (Statistics France,Insee), Daan Swinkels (Statistics Netherlands,CBS), Pascal Fransen (Statistics Netherlands,CBS)
Version 0.3

| Version | Date | Contributor/Secretary |
|---|---|---|
|0.1|2025-07-07|Initial version|
|0.2|2026-06-01|Review processed|
|0.3|2026-07-31|Restructuring, Start with Business Architecture|
|0.4|2026-09-01|Merging Business Architecture content|

## Content
[Preface](#preface)

-   Acknowledgements [TODO]

[Introduction](#introduction)

-   Activity Proposal [TODO]
-   [Purpose](#purpose)
-   [Definition of Scope](#definition-of-scope)
-   [Target Audience](#target-audience)
-   Constraints & Assumptions [TODO]

[Motivation](#motivation)
-   [Drivers](#drivers)
-   [Goals](#goals)
-   [Meaning](#meaning)
-   [Outcome](#outcome)
-   [Architecture Principles](#architecture-principles)
-   [Value](#value)
-   [Stakeholders, Roles and Collaborations](#stakeholders-roles-and-collaborations)

[Strategy](#strategys)
-   [Capability Model](#capability-model)
-   [Valuestreams](#value-streams)

[Business Architecture](#business-architecture)
-   [Overview](#overview)
-   [Steady States](#steady-states-of-data-and-their-business-process-links)



# Preface

The Statistical Architecture Framework (SAF) is developed to support the modernisation of official statistics. It responds to a shared need across National Statistical Institutes (NSIs) and partner organisations. Statistical production must remain credible, secure, and efficient. At the same time, it must adapt to new data sources, new user expectations, and tighter constraints. SAF provides a common architectural foundation to help organisations make these changes in a controlled and coherent way.

This documentation is written for enterprise and data architects, IT architects, methodologists, and IT delivery teams. It is also intended for senior decision-makers such as CIOs and CTOs, and for privacy officers, policy makers, and managers who carry responsibility for compliance, traceability, and responsible data use.
SAF replaces the earlier Common Statistical Production Architecture (CSPA) and the Common Statistical Data Architecture (CSDA). It consolidates their core ideas into a single, coherent documentation set, and it retains their ambition of shared understanding across organisations. It also continues to promote interoperability, reuse, and standardised building blocks. However, SAF shifts the centre of gravity from reference descriptions towards practical applications. It is intended to be used directly in programmes and projects, and to guide concrete design and implementation choices.

The framework builds on the assumption that, in statistical organisations, data and metadata are central assets of the organisation, and not just enablers of processes. SAF therefore treats data and metadata as managed assets across the full statistical lifecycle. It supports architectures that can work with both traditional and newdata sources. It also provides practical guidance for designing capabilities for acquisition, integration, production, and dissemination, in a way that strengthens quality, transparency, and repeatability. SAF also carries forward the capability-centric, service-based and component-oriented direction introduced in CSDA and CSPA. It promotes modular design and reuse within and across organisations. This is intended to reduce duplication, improve maintainability, and make change more manageable. It also supports a clearer separation of concerns between business methods, data, applications, and technology, which is essential for scaling and for governing complex landscapes.
The framework is designed to support multiple types of use in parallel. It can be applied for strategic planning and capability development, for solution design and architecture governance, and for portfolio alignment and implementation guidance. It can be used at enterprise level, at programme level, and within specific initiatives. This includes initiatives focused on data sharing across organizations, secure processing environments, and regulated access workflows, where security, trust, and accountability are important requirements.
 
SAF is intended to work alongside established statistical standards and models. It does not replace statistical business and information models. Instead, it provides the architectural link between strategy, capabilities, processes, services, and technology. This “glue” helps organisations make consistent decisions, improve traceability from policy to implementation, and reduce fragmentation across projects and teams. To support communication and shared understanding, SAF uses a set of architecture viewpoints. Visual models are included to clarify scope, responsibilities, and dependencies. Where appropriate, a consistent modelling notation is used so that organisations can compare, reuse, and extend the content in a disciplined way.
SAF is a living framework. It is expected to evolve through implementation experience, community feedback, and changes in the external environment. Its value depends on active use and continuous improvement across the community it serves, so that the framework remains both credible and practical over time.

# Acknowledgements

TODO

# Introduction

The Statistical Architecture Framework (SAF) provides a common architectural basis for the design, delivery, and evolution of statistical production in National Statistical Institutes (NSIs) and related organisations. It brings together architectural concepts, reference structures, and practical guidance that support consistent decision-making across portfolios and programmes. SAF aims to help statistical organisations modernise with control, while preserving the institutional qualities that make official statistics credible: transparency, quality, impartiality, reproducibility, and public trust.

Statistical organisations are facing a period of accelerated change. Data ecosystems are evolving and increasingly depend on partnerships and shared infrastructures. Artificial intelligence and rapid technological advances are changing how data can be collected, processed, and interpreted, while also introducing new risks and new expectations. At the same time, trust, scientific rigor, and data protection requirements are becoming more prominent and more demanding. These changes occur in an uncertain and fragmented global environment, where information integrity and societal confidence cannot be taken for granted. All of this is happening under sustained resource constraints, requiring organisations to be more agile and deliberate in how they prioritise, reuse, and industrialise capabilities. SAF is intended to support organisations in quickly responding to these drivers without fragmenting their architecture, governance, and implementation landscape in the process.

SAF replaces earlier reference documentation by consolidating core architectural ideas into a single framework that is more usable in practice. It is not designed as a theoretical reference alone. It is designed to be applied. SAF supports the translation of strategy into capabilities, services, and implementation choices. It supports alignment across business, methodology, data, applications, and technology. It also supports collaboration between organisations by promoting common patterns, shared viewpoints, and comparable architectural descriptions.

# Activity Proposal
TODO

# Purpose

The purpose of SAF is to provide an authoritative, consistent, and actionable framework for developing and governing statistical architectures. It aims to support coherent modernisation across NSIs by providing shared structures for describing needs, designing solutions, and managing change. SAF helps ensure that investments in platforms, data management, methods, and delivery practices strengthen each other instead of competing. It also helps organisations to demonstrate traceability from policy and strategy to implemented solutions, including the controls required for confidentiality, integrity, accountability, and lawful processing.

SAF is intended to enable better outcomes in three areas. First, interoperability and reuse, both within an organisation and across organisational boundaries.

 Second, quality and robustness, by making architectural choices explicit and reviewable, and by promoting consistent handling of data, metadata, and methodological assets. Third, overall statistical production  effectiveness, by providing a common language and set of expectations that connects architects, methodologists, engineers, managers, and oversight functions.

# Definition of Scope

SAF covers the enterprise architecture concerns that are most relevant to statistical production and dissemination, including the supporting functions that enable them. It addresses the design and evolution of capabilities, information assets, applications and services, and underlying infrastructure and deployment arrangements. It also considers the cross-cutting concerns that are essential for official statistics, such as governance, security, privacy, auditability, reproducibility and the responsible use of data and advanced analytics.

To ensure consistency and practical applicability, SAF is organised according to a TOGAF-aligned structure. It addresses motivation and principles, strategic direction and target outcomes, and the architecture domains that connect intent to implementation. This includes business architecture, data architecture, application architecture, and technology and infrastructure considerations, as well as deployment and operationalisation aspects. SAF also includes viewpoints that are tailored to distinct roles and activities within an NSI, enabling the same underlying architecture to be communicated and assessed from multiple perspectives without losing coherence.

SAF does not prescribe a single operating model, a single technology stack, or a single organisational design. It recognises that NSIs differ in mandate, maturity, and context. Instead, it provides a shared architectural foundation that can be adapted to local realities while remaining comparable across organisations. It also assumes that terminology and detailed definitions are managed through a dedicated glossary, which is maintained alongside the framework.

# Target Audience

SAF is intended to be used as a reference and as a working instrument. It can be applied when shaping strategy and roadmaps, when designing new capabilities and platforms, and when assessing initiatives for alignment and risk. It can be used to structure architectural work in programmes and projects, and to support governance decisions by making assumptions, dependencies, and trade-offs explicit. It can also be used to support communication across disciplines by establishing shared architectural concepts and consistent viewpoints.

Different roles will use SAF in different ways, while relying on the same underlying content. Enterprise and data architects will use it to define target states, standards, patterns, and architecture decisions across the organisation. IT architects and delivery teams will use it to translate those decisions into solution designs, implementation plans, and operational controls. Methodologists will use it to connect methods and process design to the enabling data and technology arrangements, and to support repeatability and scientific rigor. CIOs, CTOs, managers, and policy makers will use it to understand the implications of strategic choices, to prioritise investment, and to oversee risk and compliance. Privacy officers and assurance functions will use it to assess whether designs incorporate adequate safeguards, traceability, and accountability.

SAF is most effective when it is used consistently across the lifecycle of change. It supports early-stage framing by clarifying drivers, objectives, and constraints. It supports design by providing reference structures and viewpoints that guide architecture development. It supports delivery by improving alignment between architecture and implementation decisions. It supports operation and evolution by making dependencies and responsibilities explicit, enabling controlled change and measurable improvement.

### Expected value

The expected value of SAF is a stronger and more coherent statistical architecture practice across NSIs. It supports faster and safer modernisation by reducing ambiguity and rework. It supports reuse by encouraging common building blocks and comparable solution descriptions. It supports trust by embedding governance and assurance concerns into architecture, rather than treating them as afterthoughts. It also supports collaboration across organisations, where shared approaches to interoperability, data governance, and service orientation reduce the effort required to work together.
In providing a common framework with practical orientation, SAF aims to help statistical organisations remain resilient and responsive. It supports them in delivering high-quality statistics under changing conditions, while maintaining the safeguards and institutional discipline that official statistics require.

# Constraints & Assumptions

TODO

# Motivation

## Drivers

Architecture drivers in many ocassions  are the same forces that make change necessary. They capture the pressures, trends, and constraints that statistical offices face and which the SAF is designed to address. Drivers can be external, such as technological advancements or new regulations, or internal, such as the need to replace legacy systems or respond to stakeholder demands. By documenting these drivers, SAF ensures that its architecture is not an abstract ideal but a practical response to real-world challenges.

For statistical organizations, these drivers are particularly intense. Rapid technological change requires continuous adaptation, while political and societal pressures demand timely, relevant, and transparent data. At the same time, many organizations face limited budgets and must balance modernization with cost control. 

Recognizing these drivers helps statistical offices prioritize investments and avoid the pitfalls of reactive decision-making, where short-term fixes can lead to long-term inefficiencies.

Including architecture drivers in the framework also strengthens communication with stakeholders. By clearly articulating the external and internal factors shaping architecture, CIOs, CTOs, and enterprise architects can build a stronger case for change, justify strategic initiatives, and ensure that all parties understand the urgency of modernization. In this way, SAF creates a shared understanding of why action is necessary and what risks are avoided by adopting a structured framework.
 
### SAF-D1 Evolving Data Ecosystems and Partnerships

The environment for producing official statistics is shifting from one of isolated data collection toward a complex and interdependent data ecosystem. Traditional surveys, once the cornerstone of statistical production, now coexist with administrative, commercial, platform, and community-driven data sources. This evolution expands opportunities for collaboration but also introduces dependencies on actors, technologies, and infrastructures outside the direct control of statistical organizations.

Open-source development has become a key element of this ecosystem. It provides a shared foundation for innovation, transparency, and cost efficiency, while fostering cooperation across institutional and national boundaries. As part of a wider collaboration model, open source allows NSIs to co-develop tools and methods with peers, academia, and private partners, ensuring that advances in technology benefit the entire statistical community. SAF addresses this driver by promoting architectures that support secure data sharing, standardized interfaces, and transparent governance models. It enables NSIs to participate confidently in broader ecosystems, from national data platforms to European data spaces, where production may take place across multiple environments and jurisdictions. By combining openness with strong governance and clear accountability, SAF ensures that collaboration and shared development strengthen rather than compromise the integrity of official statistics.
 
#### SAF-D2 Artificial Intelligence and Technological Acceleration

Artificial intelligence, automation, and rapid technological progress are transforming how data is created, processed, and consumed. For statistical organizations, these developments bring both opportunities and dependencies. Emerging tools can automate repetitive tasks, enhance analytical capabilities, and strengthen quality assurance. At the same time, they redefine what it means for official statistics to remain relevant and trusted in an environment increasingly shaped by intelligent systems.

The accelerating pace of innovation requires statistical offices to be both adopters and enablers of AI. Internally, this means developing architectures and competencies that support automation, machine learning, and advanced analytics within secure and transparent frameworks. Externally, it requires ensuring that official statistics are AI-ready - that is, machine-readable, machine-understandable, and interoperable with the digital platforms and applications used by policymakers, researchers, and citizens.

SAF addresses this driver by enabling NSIs to adopt a risk-based approach to modernization. It supports architectures where critical processes that demand methodological rigor, transparency, and control can be tightly governed, while areas that are less sensitive can be automated to a higher degree. This balance ensures that innovation strengthens quality and efficiency without compromising security, privacy, or trust.

Through modular and standards-based design, SAF provides the flexibility needed to integrate emerging technologies at an appropriate pace. It allows NSIs to benefit from automation and AI-driven tools while maintaining full accountability for statistical quality, data protection, and institutional independence.
 
### SAF-D3 Trust, Scientific Rigor, and Data Protection

Trust is the foundation of official statistics. In an environment increasingly challenged by misinformation, privacy concerns, and competition from unregulated data providers, maintaining public confidence requires more than compliance. It depends on scientific rigor, transparency, and clear accountability for how data is handled and communicated.

SAF addresses this driver by embedding trust and protection directly into architectural design. It promotes governance and technical controls that safeguard confidentiality, ensure methodological integrity, and make processes traceable and transparent. Through a risk-based approach, SAF allows NSIs to apply strict oversight where sensitivity and quality demands are high, while enabling greater automation and shared solutions where risks are lower. This balance ensures that modernization strengthens trust rather than compromising it.
 
### SAF-D4 Uncertain and Polarized Global Environment

Statistical organizations operate in an increasingly complex and uncertain world. Global tensions, political polarization, and shifting power dynamics influence both the demand for and the perception of official statistics. At the same time, digital interdependence and cross-border data flows require statistical systems to remain open and interoperable while safeguarding national and institutional integrity.

SAF addresses this driver by providing a stable and transparent foundation for cooperation and resilience. It promotes interoperable architectures based on shared standards, enabling NSIs to exchange data and methods securely even in times of uncertainty. By embedding governance and design principles that protect independence and transparency, SAF helps organizations maintain credibility, comparability, and trust in environments where facts themselves are often contested.
 
### SAF-D5 Resource Constraints and Organizational Agility

Many statistical organizations face increasing expectations with limited budgets, aging systems, and challenges in recruiting and retaining specialized skills. At the same time, the demand for more timely, detailed, and multidomain outputs continues to grow. Meeting these needs requires not only efficiency, but the ability to adapt rapidly to changing priorities and technologies.

SAF addresses this driver by promoting architectures that make flexibility and reuse a core principle. It supports modular designs, shared services, and scalable solutions that reduce duplication and enable more effective use of existing resources. By fostering an agile organizational mindset and clear governance around priorities, SAF allows NSIs to reallocate capacity, modernize incrementally, and continue to deliver high-quality outputs even under financial and staffing constraints.


### Goals

Architecture goals represent the outcomes an organization aims to achieve by adopting and implementing aframework. They define what success looks like and serve as the link between strategy and action. In the case of the SAF, these goals are not just about modernizing IT systems, but about ensuring that national statistical institutes can continue to provide trustworthy, relevant, and high-quality statistics in a rapidly changing environment.

The goals of SAF address both operational and strategic needs. On one hand, they focus on efficiency, modernization, and compliance, which are essential for ensuring sustainability. On the other hand, they support innovation, adaptability, and collaboration, enabling statistical offices to embrace new opportunities such as integrating alternative data sources or experimenting with advanced analytics. Together, these goals ensure that modernization efforts do not compromise the fundamental values of official statistics, neutrality, accuracy, and reliability.

By defining goals explicitly, SAF provides a roadmap that can be adapted by each statistical organization according to its maturity and context. This ensures that while each office may have unique challenges and resources, they are all working toward a shared vision that promotes harmonization, comparability, and global collaboration in official statistics.
 
### SAF-G1 Cost Efficiency and Resource Sharing
With limited budgets and growing demands, statistical organizations must operate as efficiently as possible. SAF promotes cost optimization and improved effectiveness through shared services, reuse of solutions, and stronger interoperability. By pooling resources and adopting common components, NSIs can access capabilities that would be difficult to develop individually while avoiding duplication of effort.
SAF also encourages the use of open-source components and community-driven platforms where this strengthens transparency, collaboration, and cost efficiency. Through modular architectures and clear governance, organizations can adapt to changing needs, reallocate capacity, and modernize incrementally without large-scale reinvestments. This approach ensures that efficiency is achieved in ways that reinforce both quality and long-term sustainability.
 
### SAF-G2 Harmonized Reference Framework

Without a shared architectural reference, statistical organizations risk developing isolated solutions that reduce comparability and increase long-term costs. SAF provides a harmonized foundation of standards, patterns, and best practices that can be adapted to local contexts while supporting interoperability across borders and domains. As collaboration increasingly takes place across shared infrastructures such as national data platforms and international data spaces, harmonization also becomes a prerequisite for participation. By promoting transparency and consistent design principles, SAF helps NSIs protect the integrity of official statistics and ensure that shared and open solutions can be reused safely and effectively. A common reference framework enables collaboration, strengthens trust, and supports coherence even as the data landscape evolves.
 
### SAF-G3 Modernization of Statistical Systems

Many statistical organizations continue to rely on fragmented and legacy IT environments that limit innovation and responsiveness. SAF provides guidance for transitioning toward modern, modular, and service-based architectures that are secure, scalable, and easier to maintain. Modernization reduces technical debt, improves reliability, and allows faster delivery of new and higher-quality statistical outputs.
Modernization increasingly takes place in environments where multiple actors operate, from national infrastructures to cross-border data spaces. SAF ensures that such settings can be used safely by defining principles for access control, data protection, and accountability. It also supports a risk-based approach to automation and integration of emerging technologies. Critical processes can remain tightly governed to preserve methodological rigor, while less sensitive stages can be automated or shared.
 
### SAF-G4 Support for Data Innovation

Innovation in data and methods is central to the future of official statistics. SAF promotes an environment where experimentation, collaboration, and reuse are encouraged within secure and well-governed boundaries. By providing a clear architectural foundation, SAF enables NSIs to incorporate new data sources, tools, and analytical methods without undermining consistency or quality.

Innovation is not only about creating new solutions but also about making change possible within production. Many statistical organizations find it difficult to introduce new data sources or develop new statistical products because their production systems are optimized for predictability and stability. While these are necessary principles, they can limit agility. SAF addresses this by supporting architectures that balance robustness with flexibility, allowing new components, data, or workflows to be integrated more rapidly while maintaining full control over quality and compliance.

To make this possible, the framework emphasizes mechanisms and guardrails that enable controlled integration of innovative methods into production chains. This includes versioning, validation, and automated testing approaches that preserve reliability even as systems evolve. SAF also seeks to narrow the gap between innovation and production by promoting shared platforms and processes that allow prototypes to transition smoothly into operational environments.

Open source plays a key role in this innovation process. It allows organizations to build on each other’s work, increase transparency, and strengthen the collective capacity of the statistical community. SAF supports this through architectural patterns that enable safe reuse of open components and integration with shared platforms. In doing so, it helps turn innovation into a structured, sustainable part of statistical production.
 
### SAF-G5 Sustainable Compliance

Compliance with regulations, standards, and ethical principles is fundamental to maintaining the trust and legitimacy of official statistics. SAF ensures that modernization aligns with legal, security, and quality frameworks while promoting transparency and accountability. Within the statistical domain, well-established standards such as GSBPM, GSIM, and SDMX continue to provide a foundation for consistent processes, metadata management, and data exchange. These remain essential for ensuring methodological rigor and comparability across the statistical system.

However, as the production of statistics becomes increasingly integrated into the broader data and technology ecosystem, compliance must also extend beyond traditional statistical standards. SAF encourages active engagement with and adoption of relevant standards from adjacent fields such as data management, artificial intelligence, and cloud computing. This outward-looking approach ensures that NSIs remain interoperable with modern data platforms and can benefit from technological progress developed outside the statistical community.

Through consistent governance and the use of open, verifiable technologies, SAF supports compliance as an enabler rather than a constraint. It provides the structures necessary to ensure that innovation, data sharing, and open collaboration occur within controlled and auditable environments. This approach reinforces public trust by embedding transparency, scientific rigor, and privacy-by-design across all processes.

## Meaning
Architecture meaning provides the “why” behind the framework. While goals and outcomes describe what SAF achieves, meaning explains why it matters. For statistical organizations, architecture is not just a technical exercise but a way of ensuring their continued relevance in a digital society. SAF’s meaning lies in its role as the foundation for modernization, trust, and international collaboration.

- One dimension of this meaning is its role as a bridge between strategy and technology. Without such a framework, investments in IT risk being disconnected from the mission of providing high-quality statistics. SAF ensures that every technological decision, from adopting a new platform to restructuring business processes, can be traced back to strategic objectives, creating a coherent organizational narrative. 
- Another dimension is collaboration. The meaning of SAF extends beyond individual organizations: it is a unifying language for the UNECE statistical community. By providing shared models, practices, and principles, SAF fosters international collaboration, reduces duplication, and amplifies collective impact. In this sense, SAF is not just meaningful to IT professionals but to the broader community of statisticians, policymakers, and citizens who depend on trustworthy statistics.
 
### SAF-M1 Bridge Between Strategy and Technology
SAF connects high-level strategic objectives, such as improving statistical relevance and efficiency, with concrete technology choices. It ensures that IT investments are always justified by their contribution to the organization’s mission.
 
### SAF-M2 Catalyst for Collaboration
SAF is a unifying framework for the statistical community. It enables organizations to work together on shared goals, whether through joint platforms, interoperable systems, or harmonized standards, thereby amplifying the collective capacity of UNECE members.
 
### SAF-M3 Foundation for Digital Transformation
SAF is not just a set of technical models; it is the foundation for digital transformation in official statistics. It enables NSIs to embrace innovation without sacrificing methodological rigor or institutional trust.

### SAF-M4 Unifying Language and Notation
By adopting TOGAF and ArchiMate, SAF ensures that diverse stakeholders can communicate using a consistent language and notation. This reduces misunderstandings, enables shared modelling practices, and promotes architectural maturity across the community.

# Outcome

Architecture outcomes describe the tangible benefits that organizations can expect when adopting SAF. They translate principles, goals, and drivers into measurable impacts such as improved interoperability, reduced costs, and enhanced data quality. Outcomes are critical for demonstrating the value of architecture to stakeholders, as they provide a clear “return on investment” for adopting the framework. In the SAF, outcomes are both technical and societal.

On the technical side, NSIs benefit from streamlined processes, better metadata management, and more efficient system development. On the societal side, SAF supports trust, transparency, and comparability of statistics, which are essential for informed policy-making and democratic accountability. This dual perspective ensures that SAF delivers benefits beyond IT, directly supporting the mission of statistical organizations.

By emphasizing outcomes, SAF also reinforces a culture of continuous improvement. Outcomes are not static; rather they evolve as organizations mature and as new challenges emerge. Making outcomes explicit allows NSIs to assess progress, measure success, and adjust their modernization strategies in line with both internal priorities and external demands.
 
## SAF-O1 Accelerated Modernization
Embedding governance, metadata, and lineage into architecture ensures that statistical outputs maintain the highest standards of quality and trustworthiness. SAF makes quality an architectural outcome rather than an afterthought.
 
## SAF-O2 Enhanced Data Quality
Embedding governance, metadata, and lineage into architecture ensures that statistical outputs maintain the highest standards of quality and trustworthiness. SAF makes quality an architectural outcome rather than an afterthought.
 
## SAF-O3 Improved Interoperability
By adopting SAF, NSIs will achieve higher levels of interoperability across systems, domains, and borders. This facilitates cross-country collaborations, enhances comparability of statistics, and simplifies the integration of external data sources into official workflows.
 
## SAF-O4 Improved Trust and Transparency
By embedding principles such as openness, security, and transparency, SAF helps to build and maintain public trust in statistics. This outcome strengthens the reputation of NSIs and the legitimacy of their outputs.
 
## SAF-O5 Increased Efficiency
SAF reduces duplication of effort by promoting reuse, harmonization, and standardization. This outcome means lower IT costs, faster system development cycles, and more efficient data processing pipelines across the statistical system.
 
## SAF-O6 Shared Knowledge Base
SAF fosters a community of practice across UNECE members. Through shared architectural frameworks, NSIs can exchange lessons learned, reusable components, and knowledge, leading to continuous improvement at lower cost.

# Architecture Principles
Architecture principles are the basis for any enterprise architecture framework. They provide the guiding rules and fundamental truths that define the way organizations design, implement, and manage their IT landscapes. In the context of official statistics, principles are particularly important because they ensure consistency across an interconnected environment.

For the SAF, architecture principles act as a compass for decision-making. They ensure that whenever there is a choice to be made between technologies, processes, or solutions, decisions are not taken in isolation but in accordance with the overarching vision of the statistical community. They also prevent short-term convenience from undermining long-term sustainability, a challenge that statistical offices often face given their reliance on legacy systems and resource constraints.

These principles also provide an element of accountability. When stakeholders understand the principles behind architectural decisions, it becomes easier to justify investments, explain trade-offs, and demonstrate that architecture is not a purely technical exercise but a strategic enabler of the organization’s mission. In this way, principles make architecture transparent, predictable, and anchored in trust.

## SAF-P01 Reuse before open source, open source, before buying, buying before making it yourself
In case of equal suitability (Business Case), reuse of (parts of) applications takes precedence. The use of open source software takes precedence over purchasing. Purchasing is then preferred over making it yourself. Non-statistical processes only use standard applications.

Reuse of an application or parts of that application is sustainable and cost-efficient, and also leads to standardization in service provision and information provision. If reuse is not possible, investigate whether an Open Source solution is available before considering a Closed Source (Commercial) solution.
 
## SAF-P02 Active support
Systems (hardware and software) have an active user community and/or vendor support. The rule of thumb is that we use the latest or the second-to-last major version. Among other things, for business continuity it is necessary to be able to get quick and good support in resolving a disruption in the event of a disruption. It is also important from a security perspective that identified security risks are resolved in a timely manner.
 
## SAF-P03 Active Life Cycle management
With active Life Cycle management we prevent overdue maintenance in the IV landscape so that continuity & security risks are mitigated, among other things. Without Life Cycle management, systems or parts thereof can become outdated and thus become vulnerable in terms of security. Without active Life Cycle management, a  technological debt is also built up that, when it eventually has to be repaid, will require disproportionate effort or introduce continuity risks. Keeping systems and components up-to-date in accordance with established LCM policy mitigates these risks.
 
## SAF-P04 Maximize the benefits for the organization
IT decisions are made to maximize the benefits of the organization as a whole. This principle embodies 'service above self'. Decisions made from an organization-wide perspective have greater long-term value than decisions made from a departmental perspective. To maximize the return on the investment, IV decisions must align with the organization-wide mission and priorities.
 
## SAF-P05 IT and technology is everyone's business
All departments in the organization participate in IV decisions that are necessary to achieve organizational goals. IT and technology users are the key stakeholders in the application of technology to meet an organization's needs. To ensure that IT and technology are aligned with business operations, all departments in the organization must be involved in all aspects of the IT and technology landscape. Business experts from across the organization and the technical staff responsible for developing and maintaining the IT and technology capabilities must work together as a team to jointly define the goals and objectives.
 
## SAF-P06 Business Continuity
Organizational activities are maintained despite system or employee outages. As systems and processes become increasingly important to operations, we become more dependent on them; therefore, we must consider the reliability of such systems and processes in their design and operation. Departments throughout the organization must have the ability to continue their activities, regardless of external events, within agreed lead times. Hardware failures, natural disasters, and data corruption must not disrupt or stop operations. The enterprise must be able to operate on the basis of alternative IV systems/processes.
 
## SAF-P07 Implement loosely coupled processes and systems
Processes and systems should be built as independently as possible. This means that processes and systems are designed in such a way that they are not intertwined and dependent on each other. Functionality and logic should be shared with the rest of the organization via standard interfaces. Loosely coupling processes and systems offers more flexibility to adapt or replace individual processes and systems in the future. In addition, there are advantages in terms of scalability and robustness. Differences in security and privacy requirements can also be better enforced.
 
## SAF-P08 Data is shared property
Statistical data that has been determined to add value for use by internal or external users is shared. This implies re-use of data, both in observation to reduce the burden and in further processing to prevent duplication of work in improving and analyzing data.
 
## SAF-P09 No data without metadata and classification
All data that needs to be shared, needs to be provided with metadata information that describes the content and meaning of the data as well as possible. In addition, the data also needs to be classified. Metadata makes it possible to make data FAIR and the BIV classification (Availability, Integrity and Confidentiality) provides direction for the necessary technical and organizational measures. This is to comply with various laws, requirements and security standards.
 
## SAF-P10 Security By Design
Security should not be an afterthought in IV solutions, but should be part of those solutions. Coherent security mechanisms should span all layers of the architecture and be scalable from small objects to large objects. Security should be designed as an integrated part of the system architecture.
 
## SAF-P11 Privacy By Design
Privacy by design should be designed as an integrated part of the system architecture and business processes. Privacy should not be an afterthought in IV solutions, but should be part of those solutions. The result is that privacy becomes an essential part of the core functionality that is delivered. Privacy is an integral part of the system without compromising functionality.

# Value
The value of architecture lies in the benefits it creates for stakeholders. While outcomes describe specific impacts, value captures the broader, long-term importance of SAF to statistical organizations and society. It is about demonstrating that investing in architecture is not merely a technical necessity but a strategic decision that creates trust, efficiency, and sustainability.
For NSIs, the value of SAF includes reduced risks, greater agility, and improved alignment between IT and business objectives. For international organizations, it provides harmonization and comparability, enabling more effective collaboration across borders. For citizens and policymakers, the value lies in the trustworthiness of the statistics produced, ensuring that public policy and democratic processes are grounded in reliable data.
Value is also about sustainability. Without a framework, modernization efforts can be fragmented, costly, and short-lived. SAF provides a stable foundation that reduces technical debt, improves governance, and ensures that investments yield long-term benefits. In doing so, it secures the role of statistical organizations as trusted institutions in the digital age.
 
## SAF-V1 Cross-Border Comparability
Statistics gain value when they are comparable across borders. SAF enables this by promoting common standards, models, and processes, ensuring that statistics from different countries can be meaningfully compared.

## SAF-V2 Innovation Enablement
SAF is designed to support the integration of advanced technologies such as AI/ML, real-time analytics, and big data. By lowering the barriers to innovation, it enables NSIs to experiment safely while maintaining methodological soundness.

## SAF-V3 Risk Reduction
By embedding compliance, security, and governance into the architecture, SAF reduces risks associated with system failures, data breaches, or regulatory non-compliance. This value is particularly critical in maintaining the trust of citizens and stakeholders.
 
## SAF-V4 Strategic Alignment
SAF ensures that all IT initiatives within NSIs directly contribute to their mission of producing official statistics. This alignment improves governance, prioritization, and the impact of IT investments.
 
## SAF-V5 Sustainability
SAF promotes efficiency and modernization while reducing technical debt. By providing clear pathways for evolution, it ensures that NSIs can sustain their IT landscapes without repeated costly overhauls.
 
## SAF-V6 Trust & Legitimacy
The value of SAF lies in enhancing trust in official statistics. By ensuring transparency, ethical practices, and robust security, SAF reinforces the legitimacy of NSIs as authoritative providers of public data.

# Stakeholders, Roles and Collaborations

### Stakeholders

Architecture is never developed in isolation. Stakeholders - , as individuals, groups, or organizations that influence or are influenced by architecture - are central to its success. In the SAF, stakeholders range from technical experts and CIOs within NSIs to international organizations, policymakers, researchers, and ultimately, society at large. Each of these stakeholders has unique interests, expectations, and contributions, and the framework must balance these to be effective.

Identifying stakeholders clarifies who should be involved in governance, decision-making, and implementation. For example, IT professionals are responsible for translating SAF principles into concrete systems, while policymakers are concerned with the outcomes those systems enable. International organizations such as UNECE play a custodial role, ensuring that SAF remains harmonized and relevant across countries. By mapping these roles, SAF ensures that no perspective is overlooked and that architecture decisions are inclusive and robust.

Engaging stakeholders also strengthens legitimacy. When those affected by architecture decisions are part of the conversation, they are more likely to support the outcomes. For statistical organizations, where public trust is essential, engaging stakeholders such as researchers, academia, and citizens indirectly ensures that the architecture remains aligned with societal expectations of transparency, security, and fairness.
 
#### SAF-ST01 CIOs & CTOs of NSIs
Technology leaders within NSIs need to make strategic IT investment decisions. SAF supports them by providing a clear framework to evaluate options, align IT with business goals, and ensure compliance with international standards.
 
#### SAF-ST02 Citizens & Society
Ultimately, society is the beneficiary of SAF, as it ensures that statistical organizations produce trustworthy, transparent, and modern statistics that support democratic accountability and informed public discourse.
 
#### SAF-ST03 Government Policy Makers
Policy makers rely on official statistics to design, implement, and evaluate policies. SAF indirectly benefits them by ensuring that NSIs deliver timely, accurate, and comparable data in formats that are accessible and actionable.
 
#### SAF-ST04 IT & Data Professionals
Architects, engineers, and data scientists will use SAF to guide their daily work in designing, implementing, and managing systems. SAF provides them with common patterns, tools, and practices that increase efficiency and reduce the learning curve when collaborating across institutions.
 
#### SAF-ST05 National Statistical Institutes (NSIs)
NSIs are the primary beneficiaries of SAF, as it provides them with structured guidance for their enterprise architecture. By using SAF, NSIs can align with international practices, improve efficiency, and strengthen their ability to deliver high-quality statistics to stakeholders.
 
#### SAF-ST06 Researchers & Academia
Research communities increasingly rely on official data for scientific inquiry and innovation. SAF supports them by ensuring that statistical systems are designed with openness, data sharing, and high-quality metadata in mind, facilitating advanced research use cases.
 
#### SAF-ST07 UNECE & Other International Bodies
UNECE acts as a custodian of SAF, ensuring that it remains relevant, comprehensive, and widely adopted. Other bodies, such as Eurostat or the UN Statistics Division, are also stakeholders, as SAF complements their work in statistical modernization.

### Roles
TODO

### Collaborations
TODO

# Strategy

## Capability Model

Within the Statistical Architecture Framework (SAF), business capabilities define the fundamental abilities of a statistical organization to perform its mission , independent of processes, organizational structures, or technologies. A business capability represents what the organization must be able to do to deliver value and achieve its objectives, providing a stable and long-term view of the enterprise’s functional landscape.

Capabilities serve as the enabling building blocks of the statistical enterprise. They do not change frequently, even when the underlying processes, applications, or organizational units evolve. For example, the capability “Manage Statistical Data Quality” remains essential regardless of whether data validation is manual, automated, or AI-driven. This stability makes capabilities the preferred unit of analysis for strategic planning, transformation roadmaps, and architecture alignment within the SAF.

Each capability encapsulates a specific business purpose and outcome, which is realized through one or more business functions and operationalized by business processes. Capabilities therefore serve as the conceptual bridge between strategy and execution: they translate strategic goals into operational competence. Within the SAF, capabilities are often organized hierarchically, showing decomposition from high-level domains (such as Data Governance or Statistical Production) into more granular sub-capabilities (such as Metadata Management or Sampling Design).

A capability-based view enables statistical organizations to assess maturity, identify gaps, and prioritize modernization efforts systematically. By mapping capabilities to the supporting processes, services, and technologies, the SAF facilitates a traceable and measurable link between strategic drivers and operational implementation. This approach supports architectural coherence across business, information, application, and technology layers, ensuring that investments in modernization or digitalization strengthen the organization’s ability to deliver trusted, high-quality statistical outputs.

In essence, business capabilities in the SAF define the functional DNA of the statistical system, the core abilities that enable it to collect, manage, analyze, and disseminate data in alignment with legal, ethical, and methodological standards. They provide the foundation upon which processes, roles, and value streams are built and integrated into a unified, resilient, and future-oriented architecture.
 
### Capability Model Main-level
The capability model provides a structured, visual overview of the organization’s core abilities required to achieve its mission of producing and disseminating official statistics. This map displays capabilities as stable, business-centric building blocks, grouped to align with strategic goals and is useful to highlight areas for development and investment. The capability model helps a statistical bureau assess and communicate its strengths, gaps, and areas needing improvement to support organizational objectives such as delivering high-quality, timely statistics, maintaining the trust of data providers, and promoting innovation in data processing.
On the highest level, four main capabilities are defined. The next paragraph will describe the more detailed capabilities.

1. Primary statistical capabilities
Description: Contains all capacities required to perform the legally required tasks of a Statistical Institute.Source: GAMSO
2. Supporting Data capabilities
Description: Includes additional statistical capabilities such as managing statistical data and conducting statistical research.
3. Supporting business capacities
Description: Includes the capabilities that ensure that the right people, information and resources are available to implement and support the statistical domains and the governing domain.
4. Governance capabilities
Description: Includes the capabilities that provide direction to the organization by determining the desired strategy and the framework within which changes must take place.
Source: GAMSO 1.2, Strategy and Leadership

### Capability Model Sub-levels

#### 1. Primary statistical capabilities

##### 1.1. Statistical design and build
The ability to map information needs and set up statistical processes for this purpose.
Source: GSBPM 5.2, Design
Link: https://unece.github.io/GSBPM-5.2/#design-phase
 
##### 1.1.1 Needs inventory      	
The ability to map out the information requirement (demand for information) and translate it into social tasks that we want to respond to (supply). 
Explanation: We often do this through strategic relationships, see the social tasks mentioned in the MJP and the process preceding it.
Source: GSBPM

##### 1.1.2. Design statistics product
The ability to translate information needs into concrete designs consisting of datasets, process and workflow models and rule sets/methodology. This for the datasets that are released
Explanation: This concerns both the statistical product itself and the process that produces this product. Components of the process are various process steps, rule sets for the various process steps, methodology used, the process flow, the designs of the required datasets and the designs for the shared connection points for reuse. If the required datasets are not available, an observation assignment can follow. For primary observation, designs can then follow regarding sampling, questionnaire, etc.
Source: GSBPM Design phase

##### 1.1.3. Build statistics product
Building, testing, and managing a statistical product to the point where the product lifecycle ends
Explanation: The output from the "Design" phase is assembled and configured in this phase to create the complete operational environment to execute the process.
Source: GSBPM

#### 1.2. Data collection
The ability to collect data for official statistics.
Source: GSBPM 5.2, Collect
Link : https://unece.github.io/GSBPM-5.2/#collect-phase 
 
##### 1.2.1. Primary data collection
Primary observation describes the ability to set up and manage surveys, through to completion and transfer for processing and analysis. Primary observation collects both the data and the associated metadata. 

Explanation: Primary observation is a domain within data collection and performs observations via one or more modes. The research population and the size of the sample are determined together with the client based on the needs. A distinction is made between personal surveys and company surveys. Components of surveys include samples, questionnaires, approach strategies. 
Source: ESS capability model

##### 1.2.2. Secondary data collection
Secondary observation is the activity that describes the work required to collect data and associated metadata from third parties for the production of statistics. 
Explanation: Within secondary observation, sources with data collected by third parties are used as much as possible. 
Source: ESS capability model

#### 1.3. Processing
The ability to process raw data into statistical microdata and statistics.Source : GSBPM Process Phase
 
##### 1.3.1. Data standardization	The ability to standardize data without loss of content.
Explanation: This includes standardization of data format, codes for categories, (link) keys, possible units of measurement (for weight, distance, time). Data standardization without loss of content takes place immediately after receipt of the raw data because we want this standardization as early as possible in the processing process for efficiency reasons.
 
##### 1.3.2. Deriving variables and units
The ability to create new units and values of new variables from existing units and values of existing variables. 
Explanation: We generally derive new variables with the aim of better describing reality; something the data source was not originally intended for.
 
##### 1.3.3. Check content
The ability to check datasets for irregularities, such as missing data, possible errors and outliers. 
Explanation: discovering possible errors can lead to adjustment, see also capacity "Adjust and impute", but can also lead to a quality indicator on the basis of which quality reports can be made. Discovering outliers leads to an 'outlier indicator' and is important for a good estimation method, see also capacity "Estimate population parameter". 
Source: GSBPM 
 
##### 1.3.4. Adjusting and imputing    	
The ability to adjust possible incorrect values and missing values. 
Explanation: together with the "Content check" capacity, this capacity is often called editing. The check is then carried out using editing rules. The adjustment is then often based on imputation. The imputed values do not yet have to comply with the editing rules. To this end, a final 'adjustment' often takes place with the editing rules as a restriction.
Source: GSBPM, ESS capability model

##### 1.3.5. Estimating population parameters
The ability to estimate population parameters from microdata.
Explanation: estimated population parameters often manifest themselves as observations (the cells) in a dimensional dataset (table). There are several estimation methods, including the traditional 'weight and aggregate'. There are several techniques to arrive at the weights. Sometimes weights are adjusted to give found outliers a smaller weight.

##### 1.3.6. Integrate statistics
The ability to integrate separate statistics into one consistent whole.
Explanation: We know integration systems for, for example, the national accounts, sector accounts and labour accounts

##### 1.3.7. Statistical disclosure
The ability to check datasets for privacy sensitivity and to adjust them in case of violation.
Source: GSBPM 6.4

#### 1.4. Analysis
The ability to examine and understand data before it is disseminated. 
Explanation: Within statistical institutes, statistical analysis is also known as statistical research in which certain connections or conclusions can be drawn on the basis of relationships (such as correlation).
Source: GSBPM 5.2, Analyse
 Link : https://unece.github.io/GSBPM-5.2/#analyse-phase

##### 1.4.1. Statistical (output) analysis
The ability to validate output, interpret and explain statistical data and finalize output for dissemination using shared methodologies and processes.
Source: ESS capability model

#### 1.5. Dissemination
The ability to manage the release of statistical products to users.
Explanation: This applies to both internal and external users.
Source: GSBPM 5.2, Disseminate
Link: https://unece.github.io/GSBPM-5.2/#disseminate-phase
 
##### 1.5.1. Publication management
The ability to manage the release of statistical output and associated content according to release schedules, so that users have predictable and equal access to data.
Source: ESS capability model

##### 1.5.2. Promotion to use
The ability to promote the statistical output to potential users and to inform the press and other interested parties about the statistical output.
Source: ESS capability model

##### 1.5.3. Facilitate data access
The ability to make statistical data and metadata available to humans and machines through multiple channels.
Source: ESS capability model

##### 1.5.4. Statistical information management
The ability to prepare and distribute publications related to statistical output. 
Explanation: This includes press releases, interpretations and reports. 
Source: ESS capability model
 
#### 2. Supporting Data capabilities
Includes additional statistical capabilities such as managing statistical data and conducting statistical research.
 
#### 2.1. Data management
The ability to manage data and metadata.

##### 2.1.1. Data lifecycle management
The ability to manage data throughout its entire lifecycle.
 
##### 2.1.2. Metadata management      	
The ability to manage metadata throughout the lifecycle.
Source: ESS Capabilities
 
##### 2.1.3. Statistical quality management   	
The ability to perform quality assessments, implement control mechanisms and initiate quality improvement mechanisms for the statistical value chain.
 
##### 2.1.4. Statistical register management
The ability to set up, maintain and make available "registry"-like services for collecting and integrating data.
Explanation: Master Data
Source: ESS capability model

#### 2.2. Research
Includes acquiring and recording knowledge in relation to statistical methods, products, sources and techniques.

##### 2.2.1. Data source exploration
Exploring new data sources
Source: ESS
 
##### 2.2.2. Product Innovation
The ability to innovate, i.e. create new statistical products based on existing data sources and explore new data sources that are useful and important to users.
Explanation: A design phase may be preceded by product innovation.
Source: ESS
 
##### 2.2.3. Methodology
The ability to investigate new methods for the statistical process.
 
##### 2.2.4. Data services
The ability to provide data for statistical or scientific research.
Explanation: This applies to both internal and external datasets. These services are realized with, among other things, Microdata services.
Source: local laws and regulations ?

##### 2.2.5. User research
The ability to collect, assess and translate user needs into statistical output

#### 3. Supporting business capacities 	
Includes the capabilities that ensure that the right people, information and resources are available to implement and support the statistical domains and the governing domain.

##### 3.1. Business operations
Contains all activities required for managing personnel, purchasing & contracts, finances and housing and the associated systems and communication.

##### 3.1.1. Personnel management (HR)
Ensuring that sufficient qualified employees are available to carry out all business processes.
 
##### 3.1.2. Purchasing & contract management
Acquiring goods and services and monitoring the agreements made with suppliers.
 
##### 3.1.3. Financial management
Includes the planning, organization, design, recording and control of the financial activities of the organization.
 
##### 3.1.4. Communication management
Ensuring that the organization communicates correctly to internal and external parties.
 
##### 3.1.5. Administrative support
Providing support with administrative tasks.
 
##### 3.1.6. Facility management
Organizational function that integrates people, place and process within the built environment.
Explanation: Description based on ISO 41011. The purpose of facility management is to improve the quality of life of people and the productivity of the core activity.
Source: ISO 41011
 
##### 3.1.7. Legal support
Handling requests and applications, assessing agreements and advising on relevant legislation and regulations.
 
##### 3.1.8. Information management and archive management
Includes the activities to bring, maintain and preserve the organization's information in a state of sustainable accessibility (FAIR).
Explanation: This concerns information created in the supporting and management processes, not statistical information from the primary statistical process.

#### 3.2. Computerization and automation
Ensuring that the information needs of the organization are translated into desired functionalities of the information provision and ensuring that the information systems are available to support the business processes.

##### 3.2.1. Application development
The ability to develop applications yourself.
Explanation: This skill is needed to fill gaps in functionality that are missing in the statistical process.
 
##### 3.2.2. Functional management
Performing management tasks so that applications optimally support business processes.
Explanation: For example, by collecting existing user requirements and translating them into new application functionality.

##### 3.2.3. Technical management
Performing management tasks regarding system software and applications.
Explanation: Installing and configuring hardware and software. Managing this hardware and software to ensure that it continues to function correctly, including all measures to help resolve disruptions in a timely manner.
 
##### 3.2.4. Digital workplace management
Management of the resources and services that the employee uses for his digital workplace.
Explanation: Examples are: (Develop) Laptop / Desktops, Mobile devices, Virtual desktops, Video / audio conferencing, Printing, VPN, proxy services, all for the benefit of the workplace.
 
##### 3.2.5. IT infrastructure     	
Developing, maintaining and managing IT infrastructure

#### 3.3. Security and Privacy
Contains all security and privacy related activities

##### 3.3.1. Privacy management
Developing, managing, applying and testing the privacy policy of Statistics Netherlands in order to comply with, among other things, legislation and regulations in the field of privacy protection.

##### 3.3.2. Security planning
Includes the activities of identifying, analyzing, and planning measures to ensure the security of a system, network, organization, and facility.

##### 3.3.3. Security incident management    	
Includes the activities of identifying, analyzing, responding to, and recovering from security incidents within an organization.

##### 3.3.4. Logical identity and access control
Includes all activities that ensure that a person, organization or IT facility can only use automated functions for which it has been granted access rights through an application process.

##### 3.3.5. Physical security & access control
Includes all activities that ensure controlled and safe access to buildings and spaces and that people and goods in these buildings and spaces are safe.

##### 3.3.6. IT Security services
IT services that serve to support information security. 
Explanation: Examples include:Endpoint protection, PKI, network security management,

#### 3.4. Customer and chain interaction
The ability to interact with the customer and chain partners, ensuring that they have the correct data and information and receiving notifications, requests and data.

##### 3.4.1. Services management
Includes the design, development, implementation and management of services that the organization (parts) provides to customers and chain partners.
 
##### 3.4.2. Contact management
Maintaining relationships with customers and chain partners.
Source: GSBPM 1.2
Link: https://statswiki.unece.org/spaces/GAMSO/pages/247302304/Corporate+Support#CorporateSupport-GAMSOv1.2ManageConsumersManageConsumers

##### 3.4.3. Service Agreement
Includes drawing up, managing and enforcing service agreements with clients and chain partners.
Explanation: These contracts apply to clients to whom NSO’s provide services such as access for external researchers or for additional statistical Services, but also to parties that supply information for primary or secondary observation. If these parties fail to comply, the NSO can take enforcement action.
 
##### 3.4.4. Self-service
Offers the opportunity to customers and chain partners to find solutions to questions about the services purchased themselves or to make justified adjustments to these services without the intervention of an employee.

#### 4. Governance capabilities
Includes the capabilities that provide direction to the organization by determining the desired strategy and the framework within which changes must take place.
Source: GAMSO 1.2, Strategy and Leadership"
 
##### 4.1.1. Strategy and governance
Developing a vision and setting up and monitoring the organization and its management.
 
##### 4.1.2. Policy and planning
Translating the strategy into more concrete objectives, principles and plans.
 
##### 4.1.3. Change management
Determining and managing major changes so that maximum contribution is made to the objectives.

##### 4.1.4. Improvement management
Managing the daily operation and working on identifying areas for improvement and implementing improvement measures based on daily operations.

##### 4.1.5. Accountability
Reporting to stakeholders inside and outside the organization on the extent to which obligations and agreements are met.

##### 4.1.6. Collaboration
The ability to maintain and consolidate strategic relationships with external stakeholders.
Explanation: These activities involve collaboration and coordination with other statistical organizations and other external stakeholders. They may involve coordination within a statistical system, which may be based on a geographical hierarchy of entities (local, regional, national, multinational), or a division of responsibilities between organizations based on activities. They include activities undertaken to identify new opportunities for data exchange or integration. They provide opportunities for the statistical community to exchange knowledge, improve statistical infrastructure and practices, and influence statistical standards.
 
Source: GAMSO 1.2, Manage Strategic Collaboration and Cooperation

## Value Streams

### Primary Value Streams

### VS-01.0 Data Acquisition and Ingestion Value Stream
 
The Data Acquisition & Ingestion Value Stream is the first step in the statistical value chain. It focuses on bringing raw data into the statistical system in a secure, traceable, and compliant way. The purpose of this value stream is to make sure that data, no matter where the data comes from, enters the organization in a state that is authentic, well-documented, and ready for use. This value stream sets the foundation for everything that follows. It makes sure that the right data is collected, that legal requirements and ethical guidelines are observed, and that the data is safely stored and traceable from its source.

This value chain identifies the following value steps:
- Identify Data Needs and Sources: Define the statistical or analytical requirement and identify potential data sources (surveys, registers, administrative systems, sensors, commercial or open data).
- Establish Data Agreements and Access Rights: Negotiate and formalize data-sharing agreements, define legal and ethical frameworks, and ensure privacy and compliance.
- Collect or Receive Data: Execute data collection through surveys, APIs, secure data transfers, or data space connectors. Capture metadata during ingestion.
- Validate and Log Data Intake: Verify completeness, structural integrity, and compliance with expected formats; log the ingestion process for traceability.
- Store and Register Raw Data Artefacts: Persist data in controlled repositories, assign identifiers, and register associated metadata, ownership, and provenance.

The value created here lies in trust and readiness , trust that the data has been acquired correctly, and readiness for the data to move forward into later stages of the statistical process.

Once data has been safely acquired and registered, it is ready to move into the next phase - the Data Standardization & Integration Value Stream. Here, the focus shifts from collecting data to structuring it, ensuring that all incoming data can be compared, combined, and analyzed.

### VS-02.0 Data Standardization and Integration Value Stream

The Data Standardization & Integration Value Stream is the second step in the statistical value chain. After raw data has been collected and securely stored, it now needs to be standardized, harmonized, and prepared for further processing. In this value stream, the organization ensures that data from different sources - surveys, administrative registers, or external datasets - can work together seamlessly.
This is achieved through consistent structures, common formats, and shared definitions. The main goal is interoperability: data that looks different at the source must be aligned so it can be understood, compared, and reused across systems, domains, and time periods.
This value chain identifies the following value steps:
- Profile and Assess Data Structure: Analyze data structure, identify inconsistencies, and align schema with target models.
- Apply Standard Classifications and Formats: Map variables, codes, and identifiers to standardized taxonomies and reference data (e.g., NACE, ISCO, SDMX, GSIM concepts).
- Align Metadata and Semantics: Harmonize descriptive metadata, ensuring coherence in definitions, classifications, and quality descriptors.
- Validate Structural and Semantic Conformance: Execute validation routines to ensure the data conforms to standards and classifications.
- Register Standardized Artefacts: Store the standardized dataset and update the metadata catalogue to reflect structural and semantic alignment.

The value created here is coherence and comparability, transforming raw data into a structured and standardized asset that can flow smoothly into editing, analysis, and modeling.

Once data is standardized and validated, it can safely move to the Data Editing & Enrichment Value Stream. In that stage, attention shifts from structure and standards to quality and completeness.

The organization begins improving data accuracy, filling gaps, and enriching datasets with derived or corrected information.

### VS-03.0 Data Editing and Enrichment Value Stream

The Data Editing & Enrichment Value Stream is the third step in the statistical value chain. After data has been standardized and aligned, the next task is to improve its quality, completeness, and usability. At this stage, the organization focuses on cleaning, correcting, and enriching data so that it becomes trustworthy and analytically sound. Errors are detected, inconsistencies are corrected, missing values are filled, and new variables are derived to add more meaning and analytical value. This is where raw, standardized data begins to transform into high-quality statistical input , ready for estimation, modeling, and analysis.

This value chain identifies the following value steps:
- Conduct Error Detection and Quality Diagnostics: Identify logical errors, duplicates, missing values, or outliers through rule-based or machine-learning validation.
- Perform Data Editing and Correction: Apply predefined rules and algorithms to correct errors or replace invalid entries.
- Impute Missing or Non-Response Data: Estimate missing values using statistical imputation techniques or external data sources.
- Derive Additional Variables and Indicators: Enrich datasets by calculating derived measures or additional analytical variables.
- Perform Quality Evaluation and Versioning: Assess improvement in data quality, document changes, and create traceable versions of edited datasets.

The main value created here is data reliability and analytical readiness. By systematically improving data quality, the organization ensures that every subsequent result , every estimate, model, and publication, rests on a solid foundation.

### VS-04.0 Estimation, Analysis, and Statistical Modeling Value Stream

The Estimation & Analysis Value Stream is the fourth stage of the statistical value chain. Here, the focus shifts from improving data quality to extracting insight and meaning. At this stage, the organization applies statistical methods, estimation techniques, and analytical models to transform edited and enriched data into representative results that describe real-world phenomena. This is where data becomes statistical information, summarized, interpreted, and validated to reflect populations, trends, and behaviors. Every decision taken in this stage must balance methodological detail with transparency and reproducibility.
This value chain identifies the following value steps:
- Design Estimation and Analytical Approach: Select methodology, model type, and parameters based on survey design and analytical objectives.
- Apply Weighting and Calibration: Adjust for sample bias, non-response, or coverage errors through statistical weighting or calibration methods.
- Estimate and Aggregate Data: Generate aggregated statistics, measures, and derived indicators.
- Perform Model-Based Analysis: Conduct modeling, regression, or forecasting analyses as applicable to the domain.
- Validate and Document Results: Review statistical soundness, check for consistency, document methodology and quality metrics.

The main value created here is analytical insight and statistical credibility. Through careful estimation and analysis, data is turned into knowledge that policymakers, researchers, and society can trust.

After estimation and analysis, the organization moves to the Statistical Product Composition Value Stream. Here, the focus shifts from individual analyses to building integrated and composite products. In that next stage, data from multiple sources and analyses are combined into coherent statistical publications, dashboards, and reports, turning analytical results into accessible products that provide a complete picture.

### VS-05.0 Statistical Product Composition Value Stream
 
The Statistical Product Composition Value Stream is the fifth stage in the statistical value chain. After estimation and analysis, the focus now shifts to bringing multiple analytical results together to create coherent, meaningful, and high-value statistical products. At this stage, data from different sources, domains, and analyses are combined, refined, and formatted into composite datasets, time series, and indicators that can be used for reporting, policymaking, and research. This value stream transforms intermediate analytical outputs into final statistical products , ready for validation, interpretation, and dissemination.
This value chain identifies the following value steps:
- Select and Integrate Source Datasets: Combine outputs from multiple domains, surveys, or time periods.
- Construct Composite Indicators or Indices: Create derived measures such as indices, ratios, or time-series aggregates.
- Perform Consistency and Coherence Checks: Ensure integrated datasets are internally consistent and methodologically sound.
- Generate Analytical and Interpretive Outputs: Produce thematic reports, visualizations, or analytical interpretations.
- Approve and Register Statistical Products: Validate products against dissemination and confidentiality standards and register them for publication.

The key value created here is coherence and interpretability. Through careful composition, integration, and quality control, statistical outputs become consistent, accessible, and ready to serve their intended purpose.

After products are approved and registered, they move into the Dissemination & Service Delivery Value Stream. Here, the focus shifts from producing statistics to sharing them, making them available through publications, APIs, dashboards, and data services. That next stage ensures that the work done throughout the entire value chain ultimately reaches users in a secure, accessible, and user-friendly way.
 
#### VS-06.0 Dissemination and Service Delivery Value Stream

The Dissemination & Service Delivery Value Stream is the final stage in the statistical value chain. At this point, the statistical products created in the previous stages are published, distributed, and made accessible to users through trusted and secure channels. The main goal of this value stream is to ensure that information reaches users in a way that is accurate, timely, and easy to understand. This includes policymakers, researchers, journalists, businesses, and the general public. Dissemination is not only about releasing data, it is about providing services that help users access, interpret, and apply statistical information responsibly. This step transforms statistical outputs into societal value by enabling informed decision-making, evidence-based policy, and transparency.
This value chain identifies the following value steps:
- Plan Dissemination and Access Strategy: Define target users, access channels, and release formats (open data, API, research access, publications).
- Prepare Data for Dissemination: Apply disclosure control, anonymization, and formatting for publication or access.
- Publish and Provide Access Services: Release data and metadata via portals, APIs, dashboards, or secure research environments.
- Support and Engage Users: Provide user documentation, helpdesk support, and training for correct interpretation and use.
- Monitor Usage and Feedback: Track user interactions, collect feedback, and feed insights into continuous improvement loops.

The key value created here is impact and accessibility, ensuring that statistics and data services are usable, trusted, and beneficial to all. The Dissemination & Service Delivery Value Stream relies heavily on several cross-cutting value streams:
- Governance and Compliance ensures that all dissemination complies with data protection and confidentiality laws.
- Infrastructure and Platform Enablement provides the technical platforms for portals, Customer and Stakeholder Engagement ensures that dissemination services meet real user needs and expectations.
Together, these supporting streams ensure that dissemination is not just a technical process , but a strategic, user-centered activity that delivers societal value through trustworthy data.
 

## Supporting Cross Domain Value-Streams
### VS-07.0 Governance and Compliance Value Stream

The Governance and Compliance Value Stream runs horizontally across all stages of the statistical value chain. Its purpose is to make sure that every process, dataset, and product within the organization operates under clear rules, standards, and accountability mechanisms. This value stream builds trust , both inside and outside the organization , by ensuring that all data activities are ethical, transparent, and compliant with legal, methodological, and quality requirements. It provides the framework of control and assurance that keeps the statistical system reliable, consistent, and aligned with national and international standards such as the European Statistics Code of Practice, GDPR, GSBPM, GAMSO and ISO data quality principles.
This value chain identifies the following value steps:
- Define Governance Frameworks and Policies: Establish overarching governance structures, charters, and principles covering data, metadata, ethics, confidentiality, and statistical quality.
- Establish Legal and Regulatory Compliance Mechanisms: Identify applicable regulations (GDPR, official statistics legislation, data-sharing agreements) and define procedures to ensure compliance across all processes.
- Implement Data and Metadata Governance: Define roles (data owner, steward, custodian) and processes for metadata creation, maintenance, and lineage tracking.
- Monitor Quality and Compliance Indicators: Measure process and output quality (accuracy, timeliness, comparability) and track compliance status using formal scorecards or dashboards.
- Audit, Certify, and Report Compliance: Conduct internal or external audits, perform quality reviews, and document adherence to governance frameworks.
- Update and Improve Governance Mechanisms: Incorporate feedback, regulatory changes, and lessons learned into policies and control frameworks.

The value created here is integrity and accountability making sure that the NSI acts responsibly, protects privacy, and delivers products users can trust.

The Governance and Compliance Value Stream supports all other value streams by acting as the foundation of trust and assurance. It ensures that Data Acquisition & Ingestion follows lawful and ethical standards. It guarantees that Editing, Estimation, and Dissemination meet quality benchmarks. It provides the governance structure for Infrastructure, Innovation, and Stakeholder Engagement. In short, it supports the entire SAF value chain, ensuring that every activity is compliant, transparent, and aligned with the mission of producing trustworthy statistics.

### VS-08.0 Innovation and Methodological Development Value Stream

The Innovation and Methodological Development Value Stream makes sure the statistical organization does not stand still. Its purpose is to discover, test, and introduce new ways of working , new data sources, new methods, new tools, and new technologies. This value stream helps the organization move from “we have always done it this way” to “we can do this better, faster, and smarter.”
It connects research, methodology, IT, and business users. It also makes sure that innovation is controlled , so that only methods that are sound, documented, and compliant end up in production. This value chain identifies the following value steps:
- Identify Innovation Needs and Opportunities: Scan technological, methodological, and policy developments (AI, ML, new data sources, cloud computing) for potential improvements in statistical production.
- Conduct Research and Proof-of-Concepts: Perform controlled experiments and pilot studies to test new methodologies or technologies in limited scope.
- Evaluate Methodological Soundness and Feasibility: Assess research outcomes for accuracy, scalability, and alignment with quality frameworks and ethical principles.
- Develop and Document New Methodologies or Tools: Formalize validated innovations into standardized procedures, algorithms, or reference implementations.
- Integrate Innovation into Production Environments: Transition successful methods or technologies from pilot to production, ensuring interoperability and governance compliance.
- Promote Knowledge Sharing and Capability Building: Disseminate results, best practices, and guidelines across teams; build staff competencies to adopt new methods.

The value created here is continuous improvement. Thanks to this stream, the SAF remains future-proof, able to work with new data (IoT, admin, data spaces), new techniques (ML, small-area estimation), and new operating models (secure processing environments, data sharing).
How This Supports the Other Value Streams.
- It gives Data Acquisition new ways to connect to data spaces and new sources.
- It gives Standardization & Integration new mapping or classification techniques.
- It gives Editing & Enrichment smarter imputation and outlier detection.
- It gives Estimation & Analysis new models and ML-based methods.
- It gives Dissemination new channels (APIs, linked data, interactive views).

So, this value stream keeps the entire SAF alive and evolving.

### VS-09.0 Infrastructure and Platform Enablement Value Stream
 
The Infrastructure and Platform Enablement Value Stream provides the technical and digital foundation that supports every part of the statistical organization. Where the other value streams focus on data, methods, or governance, this one ensures that all those activities can actually run safely, efficiently, and at scale. It delivers the IT environments, data platforms, tools, and integration services that make statistical production possible, from data collection to dissemination. It ensures that the systems are secure, resilient, and compliant, while also flexible enough to handle new technologies and data sources as the organization modernizes. This value stream enables the organization to work faster, smarter, and with confidence. It transforms infrastructure from a background function into an active enabler of the statistical mission, ensuring that every user, process, and dataset has the tools and environment it needs to perform reliably.
This value chain identifies the following value steps:
- Define Digital and Technical Requirements: Identify infrastructure needs arising from business capabilities, data volumes, and analytical complexity.
- Design Platform and Infrastructure Architecture: Develop architectural blueprints for data storage, processing, integration, and secure access (data fabric, data market, compute platforms).
- Provision and Configure Platforms: Deploy and configure environments (on-premise, hybrid, or cloud) with necessary governance, monitoring, and security controls.
- Enable Integration and Orchestration Services: Implement APIs, workflow engines, and automation frameworks to connect business services and processes.
- Ensure Performance, Security, and Continuity: Monitor platform performance, implement data protection, manage incidents, and guarantee availability and disaster recovery.
- Evolve and Modernize the Technical Ecosystem: Introduce new technologies, upgrade components, and decommission obsolete infrastructure in alignment with modernization strategy.
The value created here is operational capability and continuity, a stable, modern, and adaptive foundation for the entire SAF ecosystem.

Connecting to Other Value Streams
The Infrastructure and Platform Enablement Value Stream supports every other part of the SAF. It underpins the business and data processes by providing the digital environment in which they operate.
- It gives Data Acquisition the secure pipelines and storage needed for data collection.
- It gives Standardization, Editing, and Analysis the computing and orchestration needed to process large datasets efficiently.
- It gives Dissemination the platforms, portals, and APIs through which users access results.
- It ensures Governance and Compliance have the tools to monitor security, quality, and data lineage, and
- It enables Innovation by offering scalable, modern platforms for experimentation and research.

#### VS-10.0 Customer and Stakeholder Engagement Value Stream
 
The Customer and Stakeholder Engagement Value Stream ensures that the statistical organization remains connected, relevant, and responsive to the needs of those it serves. It focuses on building and maintaining mutual understanding and trust between the organization and its users, data providers, partners, and policy stakeholders. In the SAF, this value stream is essential because official statistics exist to create public value. To achieve that, the organization must understand what stakeholders need, communicate transparently, and ensure that products, data services, and policies remain aligned with real-world demands.

This value stream is not a one-way process. It is a continuous dialogue, listening to users, understanding their challenges, and translating those insights into better products, improved services, and stronger relationships. This value chain identifies the following value steps:
- Identify and Segment Stakeholders: Map the organization’s ecosystem of users, data providers, partners, and policymakers; understand their roles and expectations.
- Collect and Analyze User Needs: Gather feedback, conduct consultations, and translate stakeholder needs into data or service requirements.
- Define and Manage Service Portfolios: Develop catalogues of business services and data products that address stakeholder needs and align with strategic goals.
- Deliver Services and Manage Relationships: Operate customer support, service desks, and account management; monitor satisfaction and service performance.
- Engage and Communicate with Stakeholders: Conduct outreach, workshops, and knowledge-sharing events to promote awareness and understanding of statistical outputs.
- Monitor Impact and Satisfaction: Measure how data and services are used, assess societal impact, and feed insights back into planning and innovation.

The value created here is relevance and trust, ensuring that the organization’s work is understood, used, and appreciated by its partners, users, and society at large.

Connecting to Other Value Streams
The Customer and Stakeholder Engagement Value Stream is the voice and mirror of the statistical organization.
- It connects external expectations with internal capabilities, closing the feedback loop across the SAF.
- It informs Data Acquisition by revealing what data sources or topics matter most to users.
- It influences Product Composition and Dissemination by identifying which outputs and formats users prefer.
- It strengthens Governance and Compliance through transparent communication about data ethics, confidentiality, and quality. It supports Innovation and Methodology by gathering ideas and feedback from real users and partners.

Through this value stream, the organization ensures that it doesn’t just produce data, it produces public value. It turns statistics into impact by aligning what the organization creates with what stakeholders need.

Value Stream to Process Realization
TBD – this view shows the difference - but also the relationship - between the business processes that drive the steady-state architecture and the value that is being created.

# Business Architecture

## Overview 

The statistical process is divided into three main business domains (observation, processing/analysis, and dissemination), with processing/analysis further divided into four subdomains. This results in a total of six business domains:

- Observation/Collection
- Processing/analysis
    - Standardization without loss of content
    - Editing, derivation, and non-response correction
    - Estimation and closed-loop
    - Statistically composed and composite statistical products
- Dissemination

Each of the business domains use the following processes :

- Design of the execution processes; provides metadata
- Implementation of the execution processes; provides the execution process
- Execution of the execution processes; provides the statistical data
- Management of the execution processes; provides quality reports

Each domain focuses on adding a specific statistical value to some data. Once sufficient value has been added, a so-called quality version is versioned that must be kept and potentially shared to some consumers. This careful approach is crucial due to the growing interest in our microdata, combined with the increasing focus on privacy. If we combine the added values of the six business domains, a value chain of statistical data is created.

To realize statistical value within a business domain, execution processes (including governance) have been designed and implemented. How an execution process adds statistical value, and is therefore designed and implemented, falls outside the scope of the B&I architecture. This framework must stem from, among other things, the methodology set.

![Generic Business Architecture](images/Business%20Architecture_GSBPM_Data%20Steady%20State_visual_v0.1.png)

The execution processes between the business domains are loosely coupled. Each has its own design and implementation. For the mutual exchange of data, they are loosely linked via steady state interfaces. To this end, five steady state phases are recognized that exist between the business domains: 
1. raw data,
2. standardized data without loss of content, 
3. processed data, 
4. statistics, and 
5. released data. 
 
 A steady state phase is therefore an environment where high-quality versions of data are brought together for exchange, but it also represents a value in the value chain of this data.

Each of the mentioned business domains can be linked to a GSBPM phase.

## Steady States of Data and Their Business Process Links

The business architecture leverages a data value chain approach where data progresses through predefined steady states, each representing a stage where data meets specific quality criteria and is ready for exchange between business domains. These steady states serve as handover points in the statistical production process, ensuring consistency, reusability, and quality control as well as interoperability across other ONS.

### State #1: Raw Data

**Business Domain Link:** Observation/Collection

**Description:** Raw data represents the initial entry point where data has been received from external data holders and checked for basic safety and validation. At this stage, data has entered the NSO system in its original form as received from the data provider.

**Quality Requirements:**
- File integrity checks completed
- Virus and security scans performed
- SLA requirements verified with the data provider (e.g., completeness, delivery time)
- Data stored in its original format or equivalent

**Usage:** Raw data for the raw source data in its original form as received from the data holder. The ONS does not have access to the data at the source; this is the first point of possession.

**Key Characteristics:**
- Data has not been further validated for content
- Sender verification completed
- Technical checks and transformations on the technical level only (not content level)
- Forms the baseline for all subsequent processing

### State #2: Standardized Data

**Business Domain Links:** Standardization without loss of content

**Description:** Standardized data has been transformed, formatted, and structured according to defined standards. This is the first point at which interoperability between domains is enabled through common classifications and standardized formats.

**Quality Requirements:**
- Format and structure standardized (e.g., converted from CSV to XML)
- Common classifications and code lists applied (e.g., geocoding, economic activity classifications)
- Variables mapped to enterprise standards
- Reference periods harmonized
- Confidentiality measures applied (e.g., pseudonymisation, data minimization)
- Data must not contain personally identifiable information

**Usage:** Standardized data based on the received raw data, enabling data integration and interoperability across the organization.

**Key Processing Activities:**
- Application of reference data and master data
- Restructuring and reformatting to NSO's standard storage format
- Recoding of variables to align with enterprise standards
- Pseudonymisation and encryption where required
- Value sets adapted to organizational standards

**Interoperability Benefit:** This state enables data from different sources to be combined and used across multiple statistical products, reducing duplication and increasing efficiency.

### State #3: Processed Data

**Business domain Links:** Editing, derivation, and non-response correction

**Description:** Processed data has undergone content-related validation, editing, and enrichment. Data accuracy has been improved through validation checks and corrective measures. This data is ready to be integrated with other datasets.

**Quality Requirements:**
- Completeness and accuracy improved through validation and editing
- Data integrity checks completed
- Filtering, editing, or imputation applied as needed
- Data lineage documented
- Integration with other datasets completed where applicable
- New derived variables calculated

**Usage:** Processed data for the processed statistical microdata, ready for statistical analysis and production.

**Key Processing Activities:**
- Data cleansing and editing (content-related standardization)
- Integration with other datasets
- Validity checking and error correction
- Imputation of missing values
- Creation of new variables through calculation or derivation
- Flagging of problematic values

**Domain Responsibility:** While this processing is primarily driven by individual statistical domains, depending on the data type, it may be performed by a central unit for efficiency and consistency.

**Reusability Focus:** Processed data aims to be as reusable as possible for other processes or units, reducing duplication of data and processing effort while increasing transparency.

### State #4: Output Data (Statistics)

**Business Domain Links:** Estimation and closed-loop + Statistically composed and composite statistical products

**Description:** Output data represents statistics that have been aggregated and analyzed, or microdata that has been prepared for specific purposes. Confidentiality measures have been applied to allow potential release.

**Quality Requirements:**
- Data lineage fully documented
- Aggregation and analysis completed
- Confidentiality measures applied
- Statistical estimates calculated
- Quality indicators produced
- Internal review completed

**Usage:** Statistics for basic statistics and integrated macrostatistics. These may be used internally by other statistical processes or prepared for dissemination.

**Key Characteristics:**
- Statistics will usually be aggregated data or estimated sizes
- May contain confidential and detailed data not yet suitable for publication
- Can be shared internally for use as input data in other statistical processes, especially macro statistics
- Estimated statistical target quantities produced
- Different confidentiality thresholds may apply depending on intended use

**Domain-Driven Production:** The type of outputs and specific processing methods vary significantly by statistical domain and product requirements.

### State #5: Published Output Data (Released Data)

**Business Process Links:** Disseminate

**Description:** Published output data has been fully vetted, confidentiality requirements have been satisfied, and the data has been released or published for external use.

**Quality Requirements:**
- Higher confidentiality criteria applied
- Stronger documentation requirements met
- Data lineage fully traceable
- Quality reports completed
- Release authorization obtained
- Metadata and documentation suitable for external users

**Usage:** Released data for all data to be disseminated publicly or delivered to authorized external parties.

**Key Characteristics:**
- All requirements for confidentiality taken care of
- May be further processed compared to State #4 for additional confidentiality protection
- Published by the NSO or delivered to external parties
- Includes both published statistical values and delivered microdata (de-identified)
- Strict documentation requirements to support user understanding and data reuse

**External Consumption:** This is the final state in the value chain where statistical information fulfills the core mission of the NSO—delivering trusted statistics to society.

### State #6: Consumed Data

**Description:** Data that has been used by external parties for their own purposes. This represents data outside the direct control of the NSI.

**Usage:** - None - Consumed data is data used by external data consumers for their analyses and decision-making.

**Key Characteristic:** This state recognizes that once data is published, it enters the public domain and is used in ways that may be beyond the NSO's direct oversight, though the quality and documentation provided in State #5 support appropriate use.

## The Statistical Data Value Chain

The SAF business layer describes how a National Statistical Office (NSO) turns externally-held data into trusted statistics that serve society. Six **primary** value streams form a linear production chain, each adding a specific kind of statistical value, and four **supporting** value streams enable them across the board.

::: {.callout-note title="Key concepts — if you are new to architecture documents" collapse="true"}
This documentation uses a handful of architecture terms. Here is what they mean in plain language:

- **Value stream** — a sequence of steps that together create a statistical output. Think of it as a production line: VS-01 to VS-06 each add a specific kind of value to the data.
- **Value stream stage vs. business process** — the stage (`VS-0x.y`) says *what value* is added; the business process describes *how* your office actually does it. The numbering maps one-to-one.[^archimate]
- **Steady state** — a fixed handover point: a versioned, quality-assured dataset that one stream produces and the next one consumes. The six states are numbered #0 (source data, still at the provider) to #5 (published statistics).
- **The four process types** — every domain is described through the same four groups: **Design** (decide how it should work), **Implementation** (build and test it), **Execution** (run it each production cycle), **Management** (check quality and feed improvements back).
- **Business service / object / event** — what a domain offers to others / the data artefacts it works on / the signals streams send each other (e.g. *"Raw Data Registered"* tells the next stream new data is ready).
- **NSO** — National Statistical Office.
- **GSBPM** — the *Generic Statistical Business Process Model*: the standard, internationally agreed description of the phases of statistical production (specify needs, design, build, collect, process, analyse, disseminate, evaluate).
- **GAMSO** — the *Generic Activity Model for Statistical Organizations*: the companion standard describing management and support activities (strategy, capability development, corporate support).
- **SAF-P01 … SAF-P11** — the eleven SAF architecture **p**rinciples, defined in the SAF Framework document and referenced throughout.

[^archimate]: This split follows the ArchiMate 3.2 Specification (sec. 7.3.2): "value streams are typically realized by business processes", with the stages providing "a framework for organizing and defining business processes".
:::


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

## VS-01.0 Data Acquisition and Ingestion 

### Purpose and Scope

This document specifies the complete business layer for the **Observation/Collection** business domain, corresponding to the *VS-01.0 Data Acquisition and Ingestion Value Stream*. It also covers 4 governance process types:

- **Design** — how the acquisition pipeline is specified and planned (produces metadata)
- **Implementation** — how the pipeline is built, configured, and tested (produces the execution process)
- **Execution** — how data is operationally collected, validated, and stored (produces statistical data)
- **Management** — how the domain is monitored, quality-assessed, and improved (produces quality reports)

::: {.callout-warning title="Out of Scope"}
Application and Technology layer specifications are out of scope for this document.
:::



::: {.callout-tip title="How to read this document"}
You do not need to read this document cover to cover — go to the section that matches your role:

- **Data collection manager / operations staff** → the **Execution** processes (what happens each production cycle).
- **Quality or compliance manager** → the **Management** processes (monitoring, quality, audit, improvement).
- **Methodologist / statistical designer** → the **Design** processes (requirements, methodology, rules).
- **System builder / IT** → the **Implementation** processes (building and testing the pipeline).
- **Manager wanting the big picture** → read the *Introduction and Strategic Context*, then jump to the *End-to-End Scenarios* at the end.
:::


*A note on numbering:* each `VS-01.y` below is both a value stream stage (*what value* is added) and a business process (*how* it is done); the numbering maps one-to-one. See the key-concepts box above.



### Position in the Statistical Value Chain

VS-01.0 is the first primary value stream — the entry point through which all data enters the statistical system. It is the "Source & Ingest Information" orchestration stage that feeds all downstream processing.

```{mermaid}
%%| label: fig-1
%%| fig-cap: "Value Stream Context Map. VS-01.0 (highlighted) is the entry point: all data passes through it before any downstream processing. The four supporting streams below enable the whole chain."
%%| fig-width: 6


flowchart TD
    subgraph primary["Primary Value Streams"]
        direction LR
        VS01["**VS-01.0**
        Data Acquisition
        & Ingestion"]:::highlight
        VS02["VS-02.0
        Data Standardization
        & Integration"]
        VS03["VS-03.0
        Data Editing
        & Enrichment"]
        VS04["VS-04.0
        Estimation, Analysis
        & Modeling"]
        VS05["VS-05.0
        Statistical Product
        Composition"]
        VS06["VS-06.0
        Dissemination
        & Service Delivery"]
        VS01 --> VS02 --> VS03 --> VS04 --> VS05 --> VS06
    end

    subgraph supporting["Supporting Value Streams"]
        VS07["VS-07.0
        Governance &
        Compliance"]
        VS08["VS-08.0
        Innovation &
        Methodology"]
        VS09["VS-09.0
        Infrastructure &
        Platform Enablement"]
        VS10["VS-10.0
        Customer &
        Stakeholder Engagement"]
    end

    supporting -.->|"enables"| primary

    classDef highlight fill:#2563eb,color:#fff,stroke:#1d4ed8,stroke-width:3px
```

### Steady State Transition

VS-01.0 transitions data from **Steady State #0 (Source Data)** — data at the external provider — to **Steady State #1 (Raw Data)** — data under NSO custody in its original form, with provenance metadata and basic quality verification completed.

```{mermaid}
%%| label: fig-2
%%| fig-cap: "Steady State Transition. Source Data is external data in its original form; the ingestion service at the NSO boundary validates and documents it; Raw Data is the same data under NSO custody, ready for downstream use."
%%| fig-width: 6
flowchart LR
    subgraph external["External Domain"]
        SD["Source Data
        (State #0)"]
    end

    subgraph boundary["NSO Boundary"]
        QG["Ingestion Service
        (Metadata addition, Quality/Schema check)"]
    end

    subgraph internal["NSO Domain"]
        RD["Raw Data
        (State #1)"]
    end

    SD --> QG --> RD

    style internal fill:#2563eb,color:#fff,stroke:#1d4ed8,stroke-width:3px
    style external fill:#7d7d7d,color:#fff,stroke:#1d4ed8,stroke-width:1px
    style boundary fill:#FFF,stroke-dasharray:5,5

```

::: {.callout-tip title='Quality gate criteria (Examples)'}
- File integrity checks completed (checksum, digital signature)
- Virus and security scans performed
- Service-level agreement (SLA) requirements verified with the data provider (completeness, delivery timeliness)
- Sender verification completed
- Data stored in its original format — no content-level transformation has been applied
- Ingestion metadata captured (provenance, source, timestamp, method)
:::


### The Four-Process Governance Pattern

The Statistical Architecture Framework defines that each business domain operates through four distinct process types. This is not a linear sequence but a governance cycle where each process type produces a distinct output that feeds the others.


```{mermaid}
%%| label: fig-3
%%| fig-cap: "The Four-Process Governance Pattern. Each process type produces a distinct artefact class. The cycle closes when Management findings feed back into Design improvements."
%%| fig-width: 6
flowchart LR
    D["**Design**
    _provides metadata_

    Data models, validation rules,
    methodology, quality criteria"]
    I["**Implement**
    _provides the execution process_

    Configured pipelines, tested
    instruments, production-ready systems"]
    E["**Execute**
    _provides the statistical data_
    Collected datasets, ingestion
    metadata, audit trails"]
    M["**Manage**
    _provides quality reports_
    KPI dashboards, quality scorecards,
    improvement recommendations"]

    D -->|"design artefacts
    guide building"| I
    I -->|"production-ready
    process"| E
    E -->|"data & process logs
    for assessment"| M
    M -->|"improvement
    feedback"| D

    style D fill:#7c3aed,color:#fff,stroke:#6d28d9
    style I fill:#2563eb,color:#fff,stroke:#1d4ed8
    style E fill:#059669,color:#fff,stroke:#047857
    style M fill:#d97706,color:#fff,stroke:#b45309
```




### Governing Principles

The following principles directly govern the VS-01.0 business domain:

| Principle | Statement | Application to VS-01.0 |
|---|---|---|
| **SAF-P01** | Actively participate in open source to maintain collective control over statistical processes | NSOs should contribute to open source communities for collection and ingestion tooling, ensuring collective control over critical capabilities rather than vendor dependence. |
| **SAF-P07** | Implement loosely coupled processes and systems | The data acquisition domain must be independent from downstream processing. Raw Data (State #1) serves as a decoupling interface — downstream consumers access it without knowledge of how it was collected. |
| **SAF-P08** | Data is shared property | Raw data, once registered, is available to all authorized consumers. Collection efforts should not be duplicated across statistical products when the same source data can serve multiple purposes. |
| **SAF-P09** | No data without metadata and classification | At the point of ingestion, every dataset must be enriched with provenance (where it came from and how), source, method, timestamp, quality indicators, and a BIV classification (availability, integrity, confidentiality). This is not a precondition that blocks ingestion, but an obligation the NSO fulfills during acquisition. |
| **SAF-P10** | Security By Design | Security is embedded in the acquisition pipeline — encrypted transfer channels, virus scanning, checksum verification, access controls — not added as an afterthought. |
| **SAF-P11** | Privacy By Design | Privacy protection (pseudonymization timing, purpose limitation, GDPR lawful basis) is designed into the acquisition process from the start, not retrofitted after data enters the system. |

::: {.callout-note title="Cross-cutting principle application"}
Several principles cut across all four process types. SAF-P09 (no data without metadata) applies everywhere: Design defines the target metadata, Execute captures it at ingestion, Manage assesses and closes remaining gaps. SAF-P10 (Security By Design) applies to Design (Section 3.5), Implementation (Section 4.1), and Execution (Sections 5.3–5.5). SAF-P11 (Privacy By Design) applies to Design (Section 3.5) and propagates through all phases. SAF-P07 (loosely coupled) governs the State #1 handover interface to VS-02.0.
:::

### Capability Foundations

This table is reference material: it shows which abilities from the SAF capability model the domain relies on, so you can map them to your own organization. It is safe to skip on a first read.

VS-01.0 draws on the following SAF capabilities:

| Capability Group | Capabilities | Role in VS-01.0 |
|---|---|---|
| **1.1 Statistical design and build** | 1.1.1 Needs inventory, 1.1.2 Design statistics product, 1.1.3 Build statistics product | Design the data requirements, collection methodology, and build the acquisition pipeline |
| **1.2 Data collection** | 1.2.1 Primary data collection, 1.2.2 Secondary data collection | Execute the collection — surveys, administrative data intake, API extraction |
| **2.1 Data management** | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management, 2.1.4 Statistical register management | Manage the data and metadata throughout ingestion, assess quality, maintain registers |
| **3.1 Business operations** | 3.1.2 Purchasing & contract management | Manage data sharing agreements and provider contracts |
| **3.2 Computerization and automation** | 3.2.1 Application development, 3.2.2 Functional management | Build and maintain collection instruments and ingestion systems |
| **3.3 Security and Privacy** | 3.3.1 Privacy management, 3.3.2 Security planning | Ensure privacy and security by design in all acquisition processes |
| **4.1 Governance** | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improve management, 4.1.5 Accountability | Govern the domain, plan improvements, report on compliance |

### Metadata Perspective

Metadata is produced in every phase, not only in Design. The table below shows what each process type contributes — both data metadata (describing the datasets) and process metadata, also called *paradata* (describing how the process itself ran: who, when, with which tools).

| Process Type | Data Metadata Produced | Process Metadata (Paradata) Produced |
|---|---|---|
| **Design** | Data models, variable definitions, classification schemes, expected formats, quality thresholds | Design decisions log, methodology version, review and approval records |
| **Implement** | Schema configurations, validation rule parameters, catalog templates, instrument-to-metadata mappings | Build log, test results, configuration change records, deployment approvals |
| **Execute** | Per-dataset provenance, source, timestamp, file hash, volume, quality indicator values, agreement reference | Operator identity, timing, volumes, errors, collection mode, instrument version |
| **Manage** | Quality scores, lineage assessments, completeness reports, lifecycle status, trend analyses | KPI dashboards, quality trend analyses, improvement decisions, audit findings |


## Business Roles and Actors



| Role                        | Process Orientation | Description                                                                                       |
|-----------------------------|---------------------|---------------------------------------------------------------------------------------------------|
| **Data Provider**           | External            | Supplies data to the NSO under a data sharing agreement (government agency, business, individual) |
| **Survey Respondent**       | External            | Provides data through survey instruments — web (CAWI), face-to-face (CAPI), telephone (CATI), or paper |
| **Legal Authority**         | External            | Grants legal basis for data collection (e.g., statistics law, GDPR authorization)                 |
| **Metadata Architect**      | Design              | Designs data models, metadata schemas, and classification mappings                                |
| **Data Engineer**           | Implementation      | Builds and configures ingestion pipelines, collection instruments, and data channels              |
| **System Configurator**     | Implementation      | Configures platforms, SFTP endpoints, API connectors, and access controls                         |
| **Test Manager**            | Implementation      | Plans and executes testing of the acquisition pipeline (technical, field, integration)            |
| **Process Owner**           | Management          | Accountable for the end-to-end performance of the data acquisition domain                         |
| **Compliance Officer**      | Management          | Ensures legal and regulatory compliance, produces audit reports                                   |
| **Quality Manager**         | Management          | Monitors KPIs, produces quality reports, and drives continuous improvement                        |
| **Methodologist**           | Design              | Designs collection methodology, sampling strategies, and questionnaire content                    |
| **Statistical Designer**    | Design              | Translates statistical needs into data requirements and process specifications                    |
| **Data Collection Manager** | Execution           | Oversees operational data collection campaigns and coordinates collection teams                   |
| **Data Quality Analyst**    | Execution           | Performs validation checks, assesses data quality at intake, and logs exceptions                  |
| **Data Steward**            | Execution           | Registers datasets in the catalog, manages metadata entries, and applies access controls          |



## Design Processes — "provides metadata"

*Framework alignment: GSBPM Phases 1–2 — see [Framework Mappings](#framework-mappings).*

The design phase produces the **metadata artefacts** that govern all subsequent phases. Without a well-designed acquisition pipeline, execution becomes ad-hoc, implementation becomes inconsistent, and management has nothing to measure against.

### Design Data Requirements and Source Strategy

The starting point of any data acquisition effort is understanding what data is needed and where it can be obtained. This sub-process translates statistical objectives — target populations, required variables, reference periods, and quality expectations — into a concrete source strategy. The team inventories and evaluates potential data sources across the full spectrum: surveys, administrative registers, APIs, web sources, sensors, and commercial data. Each source is assessed for relevance, quality, accessibility, cost, timeliness, and legal availability. The outcome is a strategic decision on the collection approach: primary collection (run a survey), secondary collection (reuse administrative data), or a multi-source combination. The trade-offs behind that decision are documented (GSBPM phases 1.1–1.3 and 1.5–1.6).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define statistical needs: target population, variables, reference period, quality expectations | Data Requirements Specification | GSBPM 1.1–1.3 |
| Inventory and evaluate potential data sources across all types | Source Assessment Report | GSBPM 1.5 |
| Assess each source for relevance, quality, accessibility, cost, timeliness, legal availability | Source Assessment Report | GSBPM 1.5 |
| Decide collection strategy: primary vs. secondary vs. multi-source | Collection Strategy Decision Record | GSBPM 1.6 |
| Document trade-offs between source options | Collection Strategy Decision Record | GSBPM 1.6 |

::: {.callout-tip title="**NSO Example — Population Census:**"}
A national statistical organization designing its next census decides on a register-first approach: use the population register as the primary source, supplement with a sample survey for variables not available in registers (housing conditions, commuting patterns), and validate against municipal records. The design phase produces the variable mapping from registers to census variables, the sample design for the supplementary survey, and the quality criteria for register data acceptance.
:::


### Design Collection Methodology and Instruments

Once the source strategy is set, the methodology team designs how data will actually be collected. This involves selecting collection modes — web, face-to-face, or telephone interviewing (CAWI/CAPI/CATI), secure file transfer (SFTP), automated machine-to-machine interfaces (API), data space connectors, or web scraping — and defining how each mode operates within the overall design. For survey-based collection, this includes questionnaire design: variable definitions, question wording, skip logic, and code lists. The sampling frame and sample selection methodology are designed to ensure statistical representativeness. Where multiple modes are used, the team specifies which respondents receive which mode and the fallback sequence for non-response. A respondent communication strategy — invitation letters, reminders, and help desk scripts — rounds out the design, aligned with GSBPM phases 2.2–2.4.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Design collection modes (CAWI, CAPI, CATI, SFTP, API, web scraping, etc.) | Collection Methodology Document | GSBPM 2.3 |
| Design questionnaire content: variable definitions, question wording, skip logic, code lists | Questionnaire Design (per mode) | GSBPM 2.2 |
| Design sampling frame and sample selection methodology | Sample Design and Selection Criteria | GSBPM 2.4 |
| Define multi-mode strategy and fallback sequences | Collection Methodology Document | GSBPM 2.3 |
| Design respondent communication strategy | Respondent Communication Plan | GSBPM 2.3 |

::: {.callout-tip title="**NSO Example — Labour Force Survey:**"}
The LFS design team specifies a mixed-mode approach: first CAWI invitation by email, CATI follow-up after 2 weeks for non-respondents, CAPI for hard-to-reach populations. A rotation panel design (2-2-2) ensures longitudinal tracking. The questionnaire is designed with adaptive questioning to minimize response burden.
:::



### Design Data Model and Metadata Schema

This sub-process defines the target data structure for Raw Data (State #1) and the metadata that must accompany every dataset at the point of ingestion. The data model specifies fields, types, formats, and constraints for the storage area where incoming data first lands (the "landing zone"). Equally important is the ingestion metadata model. It prescribes what must be captured at each point of receipt: provenance information (source organization, contact, agreement reference), method details (collection mode, instrument version, sampling parameters), timing information (collection period, delivery and processing timestamps), and quality indicators (completeness rate, delivery timeliness, format conformance). Classification and coding schemes are defined to ensure consistency with national and international standards. Finally, the metadata catalog structure is designed so that datasets are discoverable, linked, and traceable — making active metadata a foundation for downstream automation, as emphasized by the CSDA (Common Statistical Data Architecture) Metadata Management capability.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define target data structure for Raw Data (State #1) — fields, types, formats, constraints | Raw Data Schema Definition | GSBPM 2.1 |
| Define ingestion metadata model: provenance, method, timing, quality indicators | Ingestion Metadata Model | SAF-P09 |
| Define classification and coding schemes | Classification Mapping Rules | SAF-P09 |
| Design metadata catalog structure for dataset registration and discovery | Catalog Registration Template | CSDA Metadata Mgmt |

### Design Validation Rules and Quality Criteria

Before any data enters the system, the acceptance criteria and exception handling rules must be clearly defined. This sub-process establishes completeness thresholds (minimum record counts, required field coverage percentages), SLA parameters (delivery windows, response times, format specifications), and structural validation rules (field types, value ranges, referential integrity, format conformance). Security and integrity check specifications — virus scan requirements, checksum algorithms, and encryption standards — are defined in line with SAF-P10. Quality dimensions to track (completeness, timeliness, conformance, integrity) are agreed upon, and exception handling rules are designed to distinguish between outright rejection, conditional acceptance with quality flags, and routing to manual review. The GAMSO Quality Management capability provides the overarching control framework.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define completeness thresholds and SLA parameters | Quality Criteria Document, SLA Template | GSBPM 2.5 |
| Define structural validation rules: field types, value ranges, referential integrity | Validation Rule Set | GSBPM 2.5 |
| Define security and integrity check specifications | Validation Rule Set | SAF-P10 |
| Define quality dimensions to track | Quality Criteria Document | GAMSO QM |
| Design exception handling rules: rejection vs. conditional acceptance vs. manual review | Exception Handling Policy | GSBPM 2.5 |

### Design Access Control and Privacy Framework

The final design sub-process ensures that security and privacy are embedded from the outset, not bolted on after the fact. Each data source receives a BIV classification (availability, integrity, confidentiality) per SAF-P09. Role-based access controls for the raw data repository are designed in accordance with SAF-P10, specifying who can read, write, and administer. Privacy protection measures follow SAF-P11: pseudonymization timing (when direct identifiers are removed or replaced), purpose limitation (what uses are authorized under each agreement), the GDPR lawful basis (which Article 6 ground applies to each source), and data minimization (whether only necessary data is collected). Audit logging requirements — what access events must be recorded — complete the security design.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define BIV data classification per source | Data Classification Policy | SAF-P09 |
| Design role-based access control for the raw data repository | Access Control Design | SAF-P10 |
| Design privacy protection: pseudonymization timing, purpose limitation, GDPR basis, data minimization | Privacy Impact Assessment Template | SAF-P11 |
| Design audit logging requirements | Audit Logging Specification | SAF-P10 |

```{mermaid}
%%| label: fig-4
%%| fig-cap: "Design Process Decomposition. Statistical needs and data sources feed the five design sub-processes (run in order, left column to right); each produces a design document. Together these documents govern how the pipeline is built, run, and measured. The dashed arrow means the framework standards inform all five."
%%| fig-width: 6
flowchart TB
    subgraph inputs["Inputs"]
        SN["Statistical Needs"]
        FW["Framework Standards<br/><small>GSBPM · GAMSO · CSDA</small>"]
        SRC["Data Sources"]
        LAW["Legal & Privacy"]
    end

    subgraph design["Design Sub-Processes"]
        D1["Data requirements<br/>& source strategy (§3.1)"]
        D2["Collection methodology<br/>& instruments (§3.2)"]
        D3["Data model &<br/>metadata schema (§3.3)"]
        D4["Validation rules &<br/>quality criteria (§3.4)"]
        D5["Access control &<br/>privacy framework (§3.5)"]
    end

    subgraph outputs["Design documents produced"]
        O1["Data requirements spec"]
        O2["Collection & questionnaire"]
        O3["Raw data schema"]
        O4["Validation rule set"]
        O5["Access control &<br/>privacy assessment"]
    end

    SN --> D1
    SRC --> D1
    FW -.->|inform| design
    LAW --> D5

    D1 --> D2 --> D3 --> D4 --> D5

    D1 --> O1
    D2 --> O2
    D3 --> O3
    D4 --> O4
    D5 --> O5

    outputs -->|govern| NEXT["Implementation (§4) · Execution (§5)<br/>measured by Management (§6)"]

    style design fill:#f5f3ff,stroke:#7c3aed
    style outputs fill:#ede9fe,stroke:#7c3aed
```

## Implementation Processes — "provides the execution process"

*Framework alignment: GSBPM Phase 3 (Build) — see [Framework Mappings](#framework-mappings).*

The implementation phase takes the metadata artefacts from Design and **builds, configures, and tests** the production-ready acquisition pipeline. Nothing runs operationally until this phase is complete.

### Build Collection Instruments and Channels

This sub-process transforms the collection methodology design into operational tools and channels. For survey-based collection, this means building or configuring the instruments themselves: a CAWI web portal with the designed question logic, multi-language support, and responsive layout; a CAPI mobile application with offline capability and the designed questionnaire; CATI call center scripts with designed routing logic; and paper forms laid out for automated scanning (OCR) or manual data entry, all following GSBPM 3.1. For secondary and emerging sources, data receipt channels are configured: SFTP endpoints with the designed encryption and authentication, API connections with rate limiting and error handling, and data space connectors per designed specifications. Secure data transfer channels with end-to-end encryption are set up in line with SAF-P10, and a respondent management system handles invitations, reminders, and tracking.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Build/configure survey instruments per mode (CAWI, CAPI, CATI, paper) | Production-ready instruments | GSBPM 3.1 |
| Configure data receipt channels (SFTP, API, data space connectors) | Configured channel endpoints | GSBPM 3.1 |
| Set up secure transfer channels with end-to-end encryption | Secure channel configuration | SAF-P10 |
| Configure respondent management system (invitations, reminders, tracking) | Respondent management system | GSBPM 3.1 |

::: {.callout-tip title="**NSO Example — Household Budget Survey:**"}
 The implementation team builds a CAWI portal with diary entry functionality (daily spending log), configures it for 12 languages, implements the designed sampling filter, and sets up an SFTP fallback channel for large retailers providing scanner data as supplementary price information.
:::

### Configure Data Ingestion Workflows

The designed validation rules and metadata capture requirements are translated into automated workflows in this sub-process. Structural validation — schema conformance, field types, and required fields — is implemented first. Alongside it come integrity checks (checksum verification, virus scanning, digital signature validation), completeness checks (record counts, field coverage thresholds), and SLA checks (delivery timeliness, format conformance), following GSBPM 3.2. Metadata capture at each ingestion point is automated to extract provenance, format, timestamps, and file hashes without manual intervention. The raw-data landing zone (the repository where incoming data first lands) is set up with the designed access controls and storage policies. Event notifications are configured so that downstream consumers (VS-02.0) are alerted when raw data is registered. Exception handling workflows route rejected data to the appropriate queue — provider notification, manual review, or conditional acceptance — per GSBPM 3.4.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Implement validation rules as automated checks (structural, integrity, completeness, SLA) | Automated validation pipeline | GSBPM 3.2 |
| Configure metadata capture at each ingestion point | Automated metadata extraction | SAF-P09 |
| Set up raw data landing zone with access controls and storage policies | Configured repository | GSBPM 3.2 |
| Configure event notifications for downstream consumers | "Raw Data Registered" event publication | GSBPM 3.2 |
| Configure exception handling workflows | Rejection routing and manual review queues | GSBPM 3.4 |

### Build Metadata Registration and Cataloging

This sub-process implements the metadata catalog and the automated registration processes that ensure every dataset is discoverable and traceable. Catalog entries are built based on the designed metadata model (Section 3.3), and automatic metadata propagation is configured from collection instruments (questionnaire metadata: variables, code lists, question wording), transfer channels (source, method, timing), and the validation pipeline (validation results, completeness scores) into the catalog. Metadata quality validation ensures that every registered dataset has all required metadata fields. Search and discovery capabilities are implemented so that downstream consumers can find and access raw data and its associated metadata. As the CSDA emphasizes, active metadata — metadata that can auto-generate collection instruments, validation rules, and processing specifications — is the ultimate goal.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Implement metadata catalog entries based on designed model | Populated metadata catalog | GSBPM 3.3 |
| Configure automatic metadata propagation from instruments, channels, and validation | Automated metadata pipelines | CSDA Metadata Mgmt |
| Set up metadata quality validation | Metadata completeness checks | SAF-P09 |
| Implement metadata search and discovery for downstream consumers | Discovery interface | CSDA Metadata Mgmt |

### Test and Validate the Pipeline

Before the pipeline goes into production, it must be rigorously verified. Technical testing covers all individual components — instruments, channels, validators, and catalog (GSBPM 3.5). Integration testing validates the end-to-end flow from data receipt through validation to catalog registration. A field test or pilot with real or synthetic data (GSBPM 3.6) runs a small-scale test with actual data providers to verify that metadata is correctly captured and propagated, quality criteria are enforced at each checkpoint, and exception handling works as designed. Performance testing confirms the pipeline can handle expected volumes within SLA windows. Security testing — penetration testing of transfer channels and access control verification — ensures the pipeline meets SAF-P10 requirements. The phase concludes with finalization of the production system and documentation of operational procedures (GSBPM 3.7).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Technical testing of all individual components | Unit test reports | GSBPM 3.5 |
| Integration testing: end-to-end flow from receipt to registration | Integration test report | GSBPM 3.5 |
| Field test / pilot with real or synthetic data | Field test report, validated metadata propagation | GSBPM 3.6 |
| Performance testing against expected volumes | Performance test report | GSBPM 3.6 |
| Security testing: penetration testing, access control verification | Security test report | SAF-P10 |
| Finalize production system and document operational procedures | Operational Procedures Manual, Production-Ready Pipeline | GSBPM 3.7 |

```{mermaid}
%%| label: fig-5
%%| fig-cap: "Implementation Pipeline from design artefacts through build/configure/test to production-ready system."
%%| fig-width: 6
flowchart LR
    subgraph design_artefacts["Design Artefacts (from Section 3)"]
        DA1["Data Requirements\n& Source Strategy"]
        DA2["Collection Methodology\n& Instruments"]
        DA3["Data Model &\nMetadata Schema"]
        DA4["Validation Rules &\nQuality Criteria"]
        DA5["Access Control &\nPrivacy Framework"]
    end

    subgraph build["Build & Configure"]
        B1["4.1 Build Collection\nInstruments &\nChannels"]
        B2["4.2 Configure\nIngestion\nWorkflows"]
        B3["4.3 Build Metadata\nRegistration &\nCataloging"]
    end

    subgraph test["Test & Validate"]
        T1["4.4 Technical\nTesting"]
        T2["4.4 Field\nTest / Pilot"]
        T3["4.4 Security\n& Performance"]
    end

    subgraph output["Production-Ready"]
        PR["Operational\nAcquisition\nPipeline"]
        OP["Operational\nProcedures"]
    end

    DA1 & DA2 --> B1
    DA3 & DA4 & DA5 --> B2
    DA3 --> B3

    B1 & B2 & B3 --> T1 --> T2 --> T3
    T3 --> PR & OP

    PR -->|"ready for"| EXEC["Execution\n(Section 5)"]

    style build fill:#eff6ff,stroke:#2563eb
    style test fill:#dbeafe,stroke:#2563eb
```

## Execution Processes — "provides the statistical data"

*Framework alignment: GSBPM Phase 4 (Collect) — see [Framework Mappings](#framework-mappings).*

The execution phase runs the **designed and implemented pipeline** operationally for each production cycle. This corresponds to the five VS-01 value stream stages. In a mature steady state, much of the work has been pre-designed (Section 3) and pre-built (Section 4) — execution focuses on running the cycle, capturing data and metadata, and ensuring quality gates are passed.

### Identify Data Needs and Sources

**Value created:** *Clear understanding of what data is needed and where it can be obtained.*

In a mature steady state, the design phase (Section 3) has already defined the data requirements and source strategy. Per-cycle execution therefore focuses on confirmation rather than re-creation. The team confirms or updates data requirements for the current production cycle, applying GSBPM 1.1 in its recurrent form. They verify that identified data sources remain available and accessible, check that source metadata is current — contact persons, data formats, delivery schedules — and identify any new sources that may have become available since the last cycle. Significant changes to requirements or source availability trigger a return to the design process rather than ad-hoc adaptation during execution.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Confirm or update data requirements for this production cycle | Confirmed requirements for cycle | GSBPM 1.1 |
| Verify data source availability and accessibility | Source availability confirmation | GSBPM 1.5 |
| Check that source metadata is current (contacts, formats, schedules) | Updated source metadata | GSBPM 1.5 |
| Identify new sources available since last cycle | New source assessment (if any) | GSBPM 1.5 |

::: {.callout-tip title="**NSO Example — Annual Census:**"}
At the start of the reference year, the census team confirms that all 393 municipal registers are available for the current reference year, verifies contact persons and API endpoints, and confirms that the supplementary survey sample frame has been updated with the latest population register extract.
:::

### Establish Data Agreement and Access Right

**Value created:** *Legal, ethical, and transparent access to data under controlled conditions.*

Before data flows, legal and operational access must be confirmed for the current production cycle. The team activates or renews data sharing agreements, verifies GDPR compliance for the current data scope — checking that processing records (Article 30) are up to date — and confirms that access credentials and security certificates are valid and not expired. For sources new to this cycle, the full agreement process designed in Section 3.5 is executed. The active agreement status is recorded and linked to the upcoming data deliveries, creating a traceable chain from legal authorization to received data.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Activate or renew data sharing agreements for the current cycle | Active Agreement Record (per source) | GSBPM 4.1 |
| Verify GDPR compliance: processing records (Art. 30) up to date | Compliance Confirmation Log | SAF-P11 |
| Confirm access credentials and security certificates are valid | Current Access Credentials (verified) | SAF-P10 |
| For new sources: execute full agreement process (per Section 3.5) | New source agreement | SAF-P11 |
| Record active agreement status linked to upcoming deliveries | Agreement-delivery linkage | GSBPM 4.1 |

::: {.callout-tip title='**NSO Example — Quarterly Tax Data:**'}
Before the Q3 delivery window opens, the data management team verifies the SLA with the tax authority (delivery within 45 days of quarter end, minimum 98% of expected records), confirms SFTP credentials are valid, and records the active agreement reference number for linking to the incoming dataset.
:::


### Collect, Receive, or Extract Data

**Value created:** *Secure and verifiable transfer of authentic data into the organization.*

This sub-process is the operational heart of the value stream, where data physically enters NSO custody. Primary data collection runs surveys through the designed and built instruments: CAWI portals open, invitation links are sent, and response rates are monitored; CAPI field interviewers are deployed with managed assignments; CATI call schedules are executed with callback management. Secondary data collection receives administrative data via agreed channels — SFTP accepts scheduled file deliveries, APIs pull data on agreed schedules, and data space connectors facilitate federated exchange. Emerging sources — web scraping, sensor data, commercial feeds — are extracted according to designed specifications, all aligned with GSBPM 4.1–4.3.

Equally critical is the metadata captured at the point of receipt. For every dataset received, the ingestion system records the source identifier and organization, timestamp of receipt, transfer method and channel, file hash (SHA-256) and format, volume (record count and file size), agreement reference, and — for surveys — the collection mode and instrument version. This metadata capture obligation, required by SAF-P09, ensures that no data enters the system without the context needed to understand its provenance and quality.

| Ingestion Metadata Field               | Description                                  |
|----------------------------------------|----------------------------------------------|
| Source identifier and organization     | Who provided the data                        |
| Timestamp of receipt                   | When it was received                         |
| Transfer method and channel            | How it was delivered (SFTP, API, CAWI, etc.) |
| File hash (SHA-256) and format         | Integrity verification and format record     |
| Volume (record count, file size)       | Scale of the delivery                        |
| Agreement reference                    | Legal basis for the data                     |
| Collection mode and instrument version | Survey-specific provenance                   |

```{mermaid}
%%| label: fig-6
%%| fig-cap: "Collection Channel Architecture. Whatever the channel — surveys, administrative deliveries, or emerging sources — all data arrives at a single landing point, and each channel records its own metadata on the way in."
%%| fig-width: 6
flowchart LR
    subgraph channels["Collection Channels"]
        direction TB
        S["Survey Collection\n(web / face-to-face / telephone)"]
        A["Administrative Data\n(file transfer / API / data space)"]
        W["Emerging Sources\n(web / sensors / commercial)"]
    end

    subgraph capture["Metadata captured on receipt"]
        M1["Source ID &\norganization"]
        M2["Timestamp &\ntransfer method"]
        M3["File hash &\nformat"]
        M4["Volume &\nagreement ref"]
    end

    subgraph ingestion["Ingestion Point"]
        IP["Raw data storage\n(landing zone)"]
    end

    S -->|"+ survey paradata"| IP
    A -->|"+ transfer metadata"| IP
    W -->|"+ extraction metadata"| IP

    IP --- capture

    IP -->|"to validation\n(§5.4)"| V["Validate & log\nintake (VS-01.4)"]

    style channels fill:#ecfdf5,stroke:#059669
    style capture fill:#f0fdf4,stroke:#059669
```


::: {.callout-tip title='**NSO Example — Multi-Mode Census:**'}
The 2026 census runs with CAWI (70% of households), CAPI (25% for non-respondents and hard-to-reach areas), and paper (5% for elderly and institutionalized populations). Each mode generates channel-specific metadata: CAWI records browser type and completion time; CAPI records interviewer ID, GPS coordinates, and interview duration; paper records scanning batch ID and OCR confidence scores.
:::


### Validate and Log Data Intake

**Value created:** *Confidence that received data is complete, structured, and fully traceable.*

Once data has been received, it must pass through the quality gates before it can be accepted into the system. The validation process checks completeness (expected record counts present, required fields populated, delivery matching SLA), structure and format against the designed schema (Section 3.3), and security and integrity (virus scan, checksum verification via SHA-256, digital signature validation per SAF-P10). A quality assessment is executed against the designed criteria from Section 3.4, producing a completeness rate, timeliness score, and conformance rating. Every validation result, exception, and decision is logged in an audit trail that captures both data metadata (what was validated, what passed, what failed) and process metadata (who validated, when, which rules were applied, which tool version). The outcome is one of two business events: *Data Intake Validated* (proceed to storage and registration) or *Data Intake Rejected* (trigger exception handling per the designed rules — notify provider, queue for manual review, or accept conditionally with quality flag).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Verify completeness: record counts, required fields, SLA conformance | Completeness assessment | GSBPM 4.4 |
| Validate structure and format against designed schema | Structural validation result | GSBPM 4.4 |
| Perform security and integrity checks: virus scan, checksum, signature | Security verification result | SAF-P10 |
| Execute quality assessment against designed criteria | Quality assessment scores | GSBPM 4.4 |
| Create audit trail: log all validation results, exceptions, and decisions | Audit trail record | GAMSO QM |

::: {.callout-important}
**Boundary:** NO content-level editing occurs at this stage. Only technical and structural validation is performed. Content editing (correction, imputation, harmonization) is the responsibility of VS-03.0 Data Editing and Enrichment.
:::

::: {.callout-tip title="**NSO Example — Tax Authority Quarterly File:**"}
Q3 delivery received: 2.3 million records, SHA-256 checksum pass, 47 fields validated against schema (all conform), 0.3% null rate on mandatory fields (within 1% tolerance), delivery received 2 days ahead of SLA deadline. Result: Data Intake Validated. All validation results logged with timestamp, rule version, and operator ID.
:::

### Store and Register Raw Data Artefacts

**Value created:** *Secure, organized, and traceable storage of raw data.*

The final execution sub-process persists validated data and makes it discoverable to the rest of the statistical system. Each dataset version receives a unique persistent identifier (URI/UUID) and is stored in the raw data repository in its original format, in line with SAF-P07's principle of loose coupling from downstream processing. Metadata is registered in the data catalog per SAF-P09: each dataset is linked to its provenance record (source, method, timing), quality assessment results (from Section 5.4), governing data sharing agreement, and classification and coding scheme references. Data lineage is recorded — Source Data (State #0) to Raw Data (State #1) — and access permissions are applied per the designed framework (Section 3.5, SAF-P10, SAF-P11). The sub-process concludes by publishing a "Raw Data Registered" event, notifying downstream VS-02.0 that new raw data is available for standardization.

**Output:** **Raw Data (Steady State #1)** — the official handover artefact to the rest of the statistical value chain.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Assign unique persistent identifier (URI/UUID) to the dataset version | Dataset ID | GSBPM 4.4 |
| Persist data in raw data repository in original format | Stored raw data artefact | SAF-P07 |
| Register metadata in the data catalog (provenance, quality, agreement, classification, lineage) | Catalog registration | SAF-P09 |
| Apply access permissions per designed framework | Access-controlled dataset | SAF-P10, SAF-P11 |
| Publish "Raw Data Registered" event to notify VS-02.0 | Event notification | SAF-P07 |

```{mermaid}
%%| label: fig-7
%%| fig-cap: "Raw Data Artefact Structure. Reading guide: each box is a type of record with its fields; a connecting line means the records are linked one-to-one. Every stored raw dataset carries four linked records: its provenance, its quality assessment, the agreement it was received under, and its access classification."
%%| fig-width: 6
erDiagram
    RAW_DATA_ARTEFACT {
        string dataset_id PK "Unique persistent URI/UUID"
        string dataset_version "Version identifier"
        string original_format "Format as received"
        date reference_period "Statistical reference period"
        datetime registration_timestamp "When registered in catalog"
    }
    PROVENANCE_RECORD {
        string source_organization "Data provider"
        string collection_mode "CAWI/CAPI/SFTP/API/etc"
        string instrument_version "Collection instrument version"
        datetime receipt_timestamp "When data was received"
        string transfer_method "Channel used"
        string file_hash "SHA-256 checksum"
    }
    QUALITY_ASSESSMENT {
        float completeness_rate "Percentage of expected records"
        float field_coverage "Percentage of non-null required fields"
        string timeliness_rating "Ahead/On-time/Late vs SLA"
        string conformance_rating "Pass/Conditional/Fail"
        int validation_errors "Count of validation issues"
    }
    AGREEMENT_REFERENCE {
        string agreement_id "Data sharing agreement ID"
        string legal_basis "GDPR Article 6 ground"
        date valid_from "Agreement start date"
        date valid_until "Agreement end date"
        string purpose_limitation "Authorized uses"
    }
    ACCESS_CONTROL {
        string biv_classification "Availability/Integrity/Confidentiality"
        string access_level "Public/Internal/Restricted/Secret"
        string authorized_roles "Roles with access"
    }

    RAW_DATA_ARTEFACT ||--|| PROVENANCE_RECORD : "has provenance"
    RAW_DATA_ARTEFACT ||--|| QUALITY_ASSESSMENT : "has quality record"
    RAW_DATA_ARTEFACT ||--|| AGREEMENT_REFERENCE : "governed by"
    RAW_DATA_ARTEFACT ||--|| ACCESS_CONTROL : "protected by"
```

## Management Processes — "provides quality reports"

*Framework alignment: GSBPM overarching Quality/Metadata Management — see [Framework Mappings](#framework-mappings).*

The management phase runs **alongside and after** execution. It monitors the acquisition domain's performance, assesses the quality of ingested data, ensures compliance, and feeds improvement recommendations back into the design phase — closing the governance cycle.

### Monitor Process Performance

Operational performance of the acquisition domain must be tracked systematically across production cycles. The process owner and quality manager collect and aggregate key performance indicators, monitor SLA compliance with all data providers, and track paradata — who performed each step, when, how long it took, what tools were used, what errors occurred. This information feeds process performance dashboards that give the process owner a real-time view of domain health, aligned with the GAMSO Quality Management capability for monitoring performance across the production lifecycle.

**Key Performance Indicators (KPIs):** these are collected per production cycle and feed the dashboard the process owner reviews.

| KPI | Description | Measurement |
|---|---|---|
| Response rate | Percentage of sample units that provided data (surveys) | Per survey, per mode, per cycle |
| Delivery timeliness | Whether data providers delivered within SLA windows | Per source, per cycle |
| Rejection rate | Percentage of deliveries that failed validation | Per source, per cycle |
| Processing time | Duration from data receipt to catalog registration | Per dataset, per cycle |
| Metadata completeness | Percentage of required metadata fields populated at registration | Per dataset |
| Exception rate | Frequency of exception handling triggers | Per validation rule |

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Collect and aggregate KPIs per production cycle | Process Performance Dashboard | GAMSO QM |
| Monitor SLA compliance with all data providers | SLA Compliance Report | GAMSO QM |
| Track paradata: operator, timing, tools, errors | Paradata Records | GAMSO QM |
| Generate process performance dashboards | Dashboard for Process Owner | GAMSO QM |

### Assess Data Quality

Beyond process performance, the quality of the ingested data itself must be evaluated against the criteria established in the design phase. Each ingested dataset is assessed across multiple quality dimensions: completeness (record counts versus expected, field coverage), timeliness (delivery date versus SLA deadline), accuracy in a structural sense (format conformance, valid value ranges), consistency (cross-field consistency, temporal consistency with previous deliveries), and conformance to standards (alignment with designed schema and classification schemes). Results are compared against the designed quality criteria from Section 3.4. Quality indicators are produced per dataset, per source, and per production cycle, and quality trends are tracked to detect deteriorating sources or consistently lower-quality modes. This aligns with the CSDA Data Quality capability and SAF Capability 2.1.3 for statistical quality management.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Evaluate quality dimensions per dataset: completeness, timeliness, accuracy, consistency, conformance | Data Quality Report (per cycle) | CSDA Data Quality |
| Compare results against designed quality criteria (Section 3.4) | Quality assessment against baseline | SAF 2.1.3 |
| Produce quality indicators per dataset, per source, per cycle | Quality Scorecards (per source, per mode) | CSDA Data Quality |
| Identify quality trends across sources and modes | Quality Trend Analysis | SAF 2.1.3 |

### Manage Metadata Lifecycle

The metadata ecosystem supporting data acquisition must remain complete, accurate, and current throughout the data lifecycle. This sub-process verifies metadata completeness — checking that every registered dataset has all required metadata fields as an SAF-P09 compliance check — and assesses metadata quality: are provenance records accurate, are classifications correctly applied, are agreement references current? The metadata catalog is actively maintained: outdated entries are retired, schemas are updated for new source formats, and metadata models are versioned. Metadata lineage from source through ingestion to raw data state is tracked, and reconciliation across systems ensures that catalog entries match actual stored artefacts. As the CSDA emphasizes, metadata conveys all context needed to understand and reuse data — without it, data is effectively useless.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Verify metadata completeness for all registered datasets | Metadata Quality Report | SAF-P09 |
| Assess metadata quality: accuracy, currency, correct classification | Metadata Quality Report | CSDA Metadata Mgmt |
| Maintain and update the metadata catalog: retire, update schemas, version models | Catalog Maintenance Log | CSDA Metadata Mgmt |
| Track metadata lineage from source through ingestion to raw data | Metadata Lineage Audit | CSDA Metadata Mgmt |
| Reconcile metadata across systems | Catalog-artefact reconciliation | SAF-P09 |

### Audit and Compliance Reporting

This sub-process produces the evidence that the acquisition domain operates within legal, regulatory, and organizational requirements. Audit trail reports demonstrate full traceability of every dataset from external source to NSO raw data repository. GDPR compliance reporting covers data processing records (Article 30), Data Protection Impact Assessment reviews for high-risk processing, and the ability to demonstrate which data the NSO holds and why. Agreement compliance reporting confirms that all data uses remain within the terms of governing agreements. Security compliance reporting verifies that all designed security measures have been applied and documents any breaches or incidents. These reports satisfy the SAF Capability 4.1.5 (Accountability) obligation and feed into VS-07.5 Audit, Certify, and Report Compliance.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Produce audit trail reports: full traceability from source to raw data | Audit Trail Summary | SAF 4.1.5 |
| Report on GDPR compliance: Art. 30 records, DPIA reviews, data subject rights | GDPR Processing Records | SAF-P11 |
| Report on agreement compliance | Agreement Compliance Report | SAF 4.1.5 |
| Report on security compliance: measures applied, breaches, incidents | Compliance Report (per cycle) | SAF-P10 |

### Continuous Improvement

The final management sub-process closes the governance loop by analyzing performance and quality data to identify and drive improvements. Quality trends across production cycles are examined: are rejection rates decreasing, is metadata completeness improving, are processing times shortening? Improvement opportunities are identified — new data sources that could replace lower-quality existing ones, better collection modes that reduce burden or increase response rates, automation of manual ingestion steps, and simplification of validation rules that generate too many false positives. These improvement recommendations are fed back to the design processes (Section 3), prioritized based on impact and feasibility, and tracked through subsequent design-implement-execute cycles. This is the SAF Capability 4.1.4 (Improve management) in action, and it connects to the GAMSO concept of identifying mature capabilities from innovation that can be transferred to production.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Analyze quality trends across production cycles | Improvement Recommendations Report | SAF 4.1.4 |
| Identify improvement opportunities: new sources, better modes, automation, rule simplification | Updated Design Inputs | SAF 4.1.4 |
| Feed recommendations back to design processes (Section 3) | Design feedback (closing the governance loop) | SAF 4.1.4 |
| Prioritize improvements based on impact and feasibility | Improvement Tracking Log | GAMSO Capability Mgmt |
| Track implementation of accepted improvements | Improvement Tracking Log | GAMSO Capability Mgmt |

```{mermaid}
%%| label: fig-8
%%| fig-cap: "Management Feedback Loop. Execution data flows through monitoring, quality assessment, metadata management, and audit processes. Continuous improvement feeds recommendations back to Design, closing the governance cycle."
%%| fig-width: 6
flowchart TD
    E["Execution\n(Section 5)<br/><em>data + paradata</em>"]

    M1["Monitor process<br/>performance (§6.1)<br/><em>KPIs, SLA compliance</em>"]
    M2["Assess data<br/>quality (§6.2)<br/><em>quality scorecards</em>"]
    M3["Manage metadata<br/>lifecycle (§6.3)<br/><em>catalog maintenance</em>"]
    M4["Audit & compliance<br/>reporting (§6.4)<br/><em>audit trails, GDPR</em>"]
    M5["Continuous<br/>improvement (§6.5)<br/><em>recommendations</em>"]

    D["Design<br/>(Section 3)<br/><em>updated requirements</em>"]

    E --> M1
    E --> M2
    M1 --> M2
    M2 --> M3
    M3 --> M4
    M4 --> M5
    M5 -->|"feedback loop"| D

    M1 -->|"dashboards"| PO["Process Owner"]
    M2 -->|"quality reports"| QM["Quality Manager"]
    M4 -->|"compliance reports"| VS07["VS-07.0\nGovernance"]

    style E fill:#ecfdf5,stroke:#059669
    style D fill:#f5f3ff,stroke:#7c3aed
    style M5 fill:#fef3c7,stroke:#d97706
```

## Business Services and Interfaces

The VS-01.0 business domain exposes the following services:

| Service | Direction | Consumers | Mapped Processes |
|---|---|---|---|
| **Data Collection Service** | External → NSO | Survey respondents, data providers | 5.3 Collect or Receive Data |
| **Data Agreement Management Service** | External ↔ NSO | Data providers, legal authorities | 5.2 Establish Data Agreement |
| **Raw Data Provisioning Service** | Internal (NSO → VS-02.0) | Standardization teams, data analysts | 5.5 Store and Register Raw Data |
| **Ingestion Monitoring Service** | Internal | Process owners, quality managers | 6.1 Monitor Performance, 6.2 Assess Quality |
| **Metadata Catalog Service** | Internal | All data consumers across the NSO | 6.3 Manage Metadata Lifecycle |
| **Design and Methodology Service** | Internal | Methodologists, statistical designers, data engineers | 3.1–3.5 All design processes |

**Interface specifications:**

- **Data Collection Service** interfaces include: web portals (CAWI), mobile apps (CAPI), telephone systems (CATI), SFTP endpoints, REST APIs, data space connectors
- **Raw Data Provisioning Service** interface: event-driven notification ("Raw Data Registered") + catalog query API for downstream consumers to discover and access raw datasets
- **Metadata Catalog Service** interface: search/browse API for metadata discovery, with metadata exchange compliant with SDMX (the international standard for exchanging statistical data and metadata)

### Boundary Interface Specifications

The domain is loosely coupled (SAF-P07) to its neighbors through two boundary interfaces. Specifying each boundary explicitly — the handover artefact, the metadata it must carry, the event that triggers it, and where responsibility transfers — makes the loose-coupling contract concrete and testable.

| Boundary | Handover Artefact | Required Metadata | Trigger Event | Responsibility Transfer |
|---|---|---|---|---|
| **External provider → VS-01.0** (intake) | Source Data (State #0) delivery | Source identifier and organization, transfer method and channel, receipt timestamp, file hash, volume, agreement reference, collection mode and instrument version (surveys) | Delivery received / survey response submitted | The provider is responsible up to the point of receipt; VS-01.0 assumes custody and the metadata-capture obligation (SAF-P09) at the ingestion point |
| **VS-01.0 → VS-02.0** (handover) | Raw Data (State #1) | Provenance, source, collection method, receipt timestamp, file hash, agreement reference, quality assessment (completeness, timeliness, conformance), BIV classification | "Raw Data Registered" event | VS-01.0 retains custody of the raw artefact; VS-02.0 assumes responsibility for standardization on event receipt |

Each interface exchanges a registered, immutable steady-state artefact plus its metadata — never internal working data — so neither side needs knowledge of the other's internal processing.

## Business Objects and Data Flow

```{mermaid}
%%| label: fig-9
%%| fig-cap: "Business Object Lifecycle across all four process types. Design objects govern implementation, which produces the pipeline that processes execution objects, which are assessed by management objects, which feed back to design."
%%| fig-width: 6
flowchart TB
    design["🔷 Design Artefacts<br/><small>Requirements · Methodology · Schema<br/>Metadata Model · Validation Rules · Access Control</small>"]
    implement["🔧 Implementation Assets<br/><small>Instruments · Workflows<br/>Catalog Config · Pipeline</small>"]
    execute["⚡ Execution Objects"]
    manage["📊 Management Reports"]

    design -->|"govern building"| implement
    implement -->|"produces pipeline<br/>that processes"| execute
    execute -->|"assessed by"| manage
    manage -->|"feeds back to"| design

    subgraph execute_detail [" "]
        direction LR
        SD["Source Data<br/>(State #0)"]:::bo -->|"ingested as"| RD["Raw Data<br/>(State #1)"]:::bo
    end

    execute --> execute_detail
    SD -->|generates| logs["Provenance · QA · Audit"]

    classDef bo fill:#fbbf24,stroke:#b45309,color:#000
    style design fill:#f5f3ff,stroke:#7c3aed
    style implement fill:#dbeafe,stroke:#2563eb
    style execute fill:#fef9c3,stroke:#b45309
    style manage fill:#dcfce7,stroke:#16a34a
    style execute_detail fill:none,stroke:none
    style logs fill:#fff,stroke:#888,stroke-dasharray: 5 5
```


## Business Events

```{mermaid}
%%| label: fig-10
%%| fig-cap: "Event-Driven Choreography between Data Provider, NSO teams, showing events across the Design → Implement → Execute → Manage cycle. The management phase closes the loop by feeding improvements back to design."
%%| fig-width: 6

sequenceDiagram
    participant DP as Data Provider
    participant NSO as NSO Teams
    participant PM as Process Mgmt

    rect rgb(245, 243, 255)
    Note over NSO: Design Phase
    NSO->>NSO: Define requirements, methodology,<br/>schema, validation & privacy rules
    NSO-->>NSO: Design Artefacts Published
    end

    rect rgb(239, 246, 255)
    Note over NSO: Implementation Phase
    NSO->>NSO: Build instruments, workflows,<br/>catalog & pipeline
    NSO-->>NSO: Pipeline Production-Ready
    end

    rect rgb(236, 253, 245)
    Note over NSO,DP: Execution Phase (per cycle)
    NSO->>DP: Confirm source & activate agreement
    DP-->>NSO: Agreement Confirmed

    alt Primary Collection
        NSO->>DP: Send survey invitation
        DP-->>NSO: Survey Response
    else Secondary Collection
        DP-->>NSO: Data File (SFTP/API)
    end

    NSO->>NSO: Validate structure & quality

    alt Validation Passed
        NSO->>NSO: Assign ID, store raw data,<br/>register metadata
    else Validation Failed
        NSO->>DP: Request redelivery
    end
    end

    rect rgb(254, 243, 199)
    Note over PM: Management Phase
    PM->>PM: Monitor KPIs, assess quality,<br/>produce compliance reports
    PM-->>NSO: Improvement Recommendations
    end
```

## Framework Mappings

This reference table maps each process group of this document to the international frameworks (GSBPM, GAMSO, CSDA) and the SAF capability model. It is intended for architects and auditors; the narrative sections above do not depend on it.

| Process group | GSBPM | GAMSO | CSDA | SAF Capabilities |
|---|---|---|---|---|
| **Design** | Phase 1 (Specify Needs: 1.1–1.6), Phase 2 (Design: 2.1–2.6) | Production (design activities), Capability Management | Data Governance, Metadata Management | 1.1.1 Needs inventory, 1.1.2 Design statistics product, 2.1.2 Metadata management |
| **Implementation** | Phase 3 (Build: 3.1–3.7) | Capability Management | Data Ingestion (setup), Data Governance (configuration) | 1.1.3 Build statistics product, 3.2.1 Application development, 3.2.2 Functional management |
| **Execution** | Phase 4 (Collect: 4.1–4.4) | Production (execution) | Data Ingestion (execution) | 1.2.1 Primary data collection, 1.2.2 Secondary data collection |
| **Management** | Overarching processes (Quality Management, Metadata Management) | Corporate Support (Quality, Data, Metadata Management), Capability Management (improvement) | Data Quality, Data Governance, Traceability | 2.1.3 Statistical quality management, 4.1.4 Improve management, 4.1.5 Accountability |

## Applying This to Your NSO

### Maturity Assessment Checklist

Use this checklist to assess your NSO's maturity across all four process types — not just execution.

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
- [ ] Do we register every raw dataset in a metadata catalog with provenance links?

**Management Maturity**

- [ ] Do we track KPIs (response rates, rejection rates, timeliness) across cycles?
- [ ] Do we produce data quality reports for each ingested dataset?
- [ ] Do we regularly assess metadata completeness and quality?
- [ ] Do we produce audit and compliance reports?
- [ ] Do we have a formal improvement process that feeds back into design?

### End-to-End Scenarios

Each scenario walks through **all four process types**, demonstrating how the governance pattern works in practice.

#### Scenario A: Household Budget Survey (Primary Collection)

**Design Phase:** Statistical designers define the information need — monthly household expenditure by category, income sources, and household composition. Methodologists design a mixed-mode approach: a CAWI diary for daily entry over two weeks, with CAPI follow-up for non-respondents. Metadata architects define the raw data schema: 156 variables across 12 expenditure categories, with code lists from COICOP (the international classification of household expenditure). Quality criteria are set at a minimum 60% response rate, diary completion rate of at least 80% of days, and delivery to processing within 30 days of collection period end. The privacy framework specifies pseudonymization at point of receipt, with purpose limited to expenditure statistics and CPI input.

**Implementation Phase:** Data engineers build the CAWI diary portal — a responsive web app with daily spending entry and barcode scanning for receipts, configured for 12 languages. System configurators set up the CAPI tablet app with offline capability, GPS logging for urban/rural classification, and interview recording consent. Ingestion workflows are configured so that CAWI responses are aggregated daily, CAPI interviews uploaded at the end of the field period, and paper diaries OCR-scanned in batches. The full pipeline is tested with a 200-household pilot in two municipalities, with metadata propagation verified end-to-end.

**Execution Phase:** For cycle Q3-2026, 8,000 households are sampled from the population register. CAWI invitations go out and a response monitoring dashboard tracks daily completion rates. After week two, CAPI is deployed to 2,400 non-responding households. After week four, 312 paper diaries are received from elderly respondents. Each channel generates ingestion metadata, and all 7,240 completed diaries pass structural validation. Raw data is registered in the catalog with full provenance — per household: mode, completion dates, and diary completeness score.

**Management Phase:** Response rate reaches 90.5% against the 60% target. CAWI diary completeness is 87% of days (target 80%). Quality scoring identifies three municipalities with unusually low CAWI completion, suggesting possible broadband issues. Metadata completeness is 99.8%. Improvement recommendations: add SMS reminders for CAWI to improve daily completion; investigate broadband-gap municipalities for a CAPI-first approach next cycle. Recommendations are fed back to the design team for the Q1-2027 methodology update.

#### Scenario B: Tax Register Administrative Data (Secondary Collection)

**Design Phase:** Statistical designers define the data requirement — quarterly corporate income tax declarations for all legal entities, for use in national accounts and business statistics. The data model maps the tax authority's XML schema to the NSO's raw data structure: 47 fields retained, 12 derived, corporate ID as the linkage key. The SLA is set at delivery within 45 calendar days of quarter end, minimum 98% of expected records, in XML format with XSD validation. Validation rules cover XSD schema validation, corporate ID referential integrity against the business register, and amount fields within historical range (plus or minus three standard deviations). Privacy framework: data is received under the Statistics Act mandate, with pseudonymization deferred to the standardization phase (VS-02.0) per agreement.

**Implementation Phase:** System configurators set up a dedicated SFTP endpoint with mutual TLS authentication and IP whitelist. Data engineers configure automated ingestion: file arrival triggers a validation pipeline (XSD check, checksum, virus scan, completeness, referential integrity, range check). Metadata registration is automated — on successful validation, a provenance record is created and linked to the agreement, and quality scores are calculated and stored. The pipeline is tested with Q1-2026 historical data resubmission; all validation rules are verified and one false-positive range check is identified and the threshold adjusted.

**Execution Phase:** Q3-2026: the tax authority delivers the quarterly file via SFTP on day 38 (within the 45-day SLA). The automated pipeline triggers: XSD valid, SHA-256 checksum matches manifest, virus scan clean, 2,347,891 records (99.2% of expected — above the 98% threshold), 14 corporate IDs not in the business register (flagged but not rejected — known lag in register updates). Raw data is stored in original XML format, assigned dataset ID `RD-TAX-2026Q3-001`. Metadata is registered: provenance, quality assessment (completeness=99.2%, timeliness=OnTime, conformance=Pass with 14 flags), and agreement reference. The "Raw Data Registered" event is published and VS-02.0 is notified.

**Management Phase:** The Q3 quality scorecard shows completeness at 99.2% (stable — consistent with Q1=99.1% and Q2=99.3%) and timeliness on time, seven days ahead of the SLA deadline. The 14 unmatched corporate IDs are all newly registered businesses with a register update lag of two to four weeks, consistent with previous quarters. SLA compliance stands at 100% for 12 consecutive quarters. Metadata completeness is 100%. No improvement recommendations are needed — the process is mature and stable, with an annual agreement renewal review scheduled for Q4.

#### Scenario C: Web-Scraped Price Data (Emerging Source)

**Design Phase:** Statistical designers define the requirement — daily retail prices from major online retailers for CPI basket items covering 500 product categories and 25 retailer websites. The methodology involves no bilateral agreement (public web data), with the legal framework based on the statistics act mandate and a public interest assessment. The data model captures product URL, product name, price, currency, timestamp, retailer, product category (COICOP), and availability status. Validation rules specify that price must be positive, currency must be EUR or local, timestamp must be within 24 hours, the product URL must resolve, and price changes exceeding 50% from the previous day are flagged for review (not rejected). Quality criteria: minimum 85% of target URLs successfully scraped per day, with price change detection within 24 hours. Privacy considerations confirm no personal data is involved, with terms-of-service compliance documented per retailer.

**Implementation Phase:** Data engineers build web scrapers — one module per retailer, headless browser for JavaScript-rendered pages, with proxy rotation to avoid rate limiting. Daily scheduling is configured so that scraping runs at 03:00 local time with results aggregated by 06:00. Volatility handling includes website structure change detection via DOM fingerprinting, with automatic alerts when a scraper breaks. Metadata capture records per-scrape provenance: URL, timestamp, HTTP status, scraper version, and DOM fingerprint. The system is tested with a two-week parallel run comparing scraped prices against manually collected prices for 50 products, achieving 94% agreement (within the acceptance threshold).

**Execution Phase:** Daily operation scrapes 12,500 URLs across 25 retailers. On 2026-03-15, 11,875 URLs are successful (95% — above the 85% threshold), with 625 failures (HTTP 404: product pages removed or restructured). Forty-seven price changes exceeding 50% are flagged for manual review: 41 are confirmed genuine (seasonal sales) and 6 are identified as scraper errors (wrong element selected due to DOM change). Raw data is stored as daily JSON files with full scrape metadata. Metadata is registered: daily provenance, quality scores, scraper version, and DOM fingerprint per retailer.

**Management Phase:** The weekly quality dashboard shows an average daily success rate of 93.2% (above the 85% threshold). Retailer `ElectroShop` shows a declining success rate from 98% to 72% over three weeks — a website redesign detected by DOM fingerprinting. Monthly price comparison against official CPI field collection shows 96.1% agreement for overlapping products (above the 90% acceptance threshold). Improvement recommendations: rebuild the `ElectroShop` scraper for the new DOM structure (implementation action), investigate two new retailers for coverage expansion (design action), and evaluate retailer API access as an alternative to scraping for the top five retailers (design action that may lead to a transition from scraping to API-based secondary collection). Recommendations are fed back to the design team, with the `ElectroShop` scraper rebuild prioritized for the next sprint.

## VS-02.0 Data Standardization and Integration

### Purpose and Scope

This document specifies the complete business layer for the **Standardization without loss of content** business domain, corresponding to the *VS-02.0 Data Standardization and Integration Value Stream*. It also covers 4 governance process types:

- **Design** — how the standardization pipeline is specified and planned (produces metadata)
- **Implementation** — how the pipeline is built, configured, and tested (produces the execution process)
- **Execution** — how raw data is operationally profiled, classified, harmonized, and registered (produces statistical data)
- **Management** — how the domain is monitored, quality-assessed, and improved (produces quality reports)

::: {.callout-warning title="Out of Scope"}
Application and Technology layer specifications are out of scope for this document. Content-level correction, imputation, and enrichment are out of scope — they belong to VS-03.0 Data Editing and Enrichment. Standardization aligns structure, format, classification, and semantics **without altering the informational content** of the data.
:::



::: {.callout-tip title="How to read this document"}
You do not need to read this document cover to cover — go to the section that matches your role:

- **Data collection manager / operations staff** → the **Execution** processes (what happens each production cycle).
- **Quality or compliance manager** → the **Management** processes (monitoring, quality, audit, improvement).
- **Methodologist / statistical designer** → the **Design** processes (requirements, methodology, rules).
- **System builder / IT** → the **Implementation** processes (building and testing the pipeline).
- **Manager wanting the big picture** → read the *Introduction and Strategic Context*, then jump to the *End-to-End Scenarios* at the end.
:::

*A note on numbering:* each `VS-0x.y` below is both a value stream stage (*what value* is added) and a business process (*how* it is done); the numbering maps one-to-one. See the key-concepts box above.



### Position in the Statistical Value Chain

VS-02.0 is the second primary value stream — it receives Raw Data from VS-01.0 and maps and reformats it into a structured, standardized asset that can flow smoothly into editing, analysis, and modeling. It is the "Harmonize & Integrate Information" orchestration stage that makes data from different sources work together — by aligning structure, format, and codes, **not** by changing the data's values.

```{mermaid}
%%| label: fig-1
%%| fig-cap: "Value Stream Context Map. VS-02.0 is highlighted as the standardization stage that bridges acquisition and editing in the primary value chain."
%%| fig-width: 6


flowchart TD
    subgraph primary["Primary Value Streams"]
        direction LR
        VS01["VS-01.0
        Data Acquisition
        & Ingestion"]
        VS02["**VS-02.0**
        Data Standardization
        & Integration"]:::highlight
        VS03["VS-03.0
        Data Editing
        & Enrichment"]
        VS04["VS-04.0
        Estimation, Analysis
        & Modeling"]
        VS05["VS-05.0
        Statistical Product
        Composition"]
        VS06["VS-06.0
        Dissemination
        & Service Delivery"]
        VS01 --> VS02 --> VS03 --> VS04 --> VS05 --> VS06
    end

    subgraph supporting["Supporting Value Streams"]
        VS07["VS-07.0
        Governance &
        Compliance"]
        VS08["VS-08.0
        Innovation &
        Methodology"]
        VS09["VS-09.0
        Infrastructure &
        Platform Enablement"]
        VS10["VS-10.0
        Customer &
        Stakeholder Engagement"]
    end

    supporting -.->|"enables"| primary

    classDef highlight fill:#2563eb,color:#fff,stroke:#1d4ed8,stroke-width:3px
```

### Steady State Transition

VS-02.0 transitions data from **Steady State #1 (Raw Data)** — data under NSO custody in its original form — to **Steady State #2 (Standardized Data)** — data aligned to common structures, formats, classifications, and semantics, with direct identifiers removed, so that it is interoperable and comparable across sources, domains, and time.

```{mermaid}
%%| label: fig-2
%%| fig-cap: "Steady State Transition from Raw Data to Standardized Data through the standardization service at the domain boundary."
%%| fig-width: 6
flowchart LR
    subgraph upstream["Upstream Domain (VS-01.0)"]
        RD["Raw Data
        (State #1)"]
    end

    subgraph boundary["Standardization Boundary"]
        QG["Standardization Service
        (Profiling, Classification/Coding,
        Semantic Alignment, Conformance check)"]
    end

    subgraph internal["Standardized Domain (VS-02.0)"]
        SD["Standardized Data
        (State #2)"]
    end

    RD --> QG --> SD

    style internal fill:#2563eb,color:#fff,stroke:#1d4ed8,stroke-width:3px
    style upstream fill:#7d7d7d,color:#fff,stroke:#1d4ed8,stroke-width:1px
    style boundary fill:#FFF,stroke-dasharray:5,5

```

::: {.callout-tip title='Conformance gate criteria (Examples)*'}
- Source codes mapped 1-to-1 to standard classifications via correspondence/lookup tables (e.g., NACE, ISCO, COICOP — the standard classifications of industries, occupations, and household expenditure), with the original value preserved
- Structure conforms to the target data model (fields, types, formats, cardinalities)
- Descriptive metadata harmonized — coherent definitions, units, reference periods, and quality descriptors recorded **as metadata**
- Structural and semantic validation routines passed
- Direct identifiers removed or pseudonymized per the privacy framework
- No data value has been changed, converted, or derived — only the representation (structure/format) is re-expressed, standard codes are added by 1-to-1 mapping, and metadata is attached
- Standardization metadata captured (source-to-target mappings, classification versions, mapping & format-coercion lineage)
:::

::: {.callout-note title="What 'content' means for the no-loss-of-content invariant"}
The no-loss-of-content invariant covers the **statistical and informational content** of the data — the records, observed values, and key measures, which the content-preservation checks verify are preserved unchanged (record counts and key business measures identical before and after). In VS-02 this is straightforward because the domain **never alters a value**: it only re-expresses the representation (structure/format), adds standard codes by deterministic 1-to-1 mapping, and attaches metadata. Anything that would change a value — unit or currency conversion, reference-period alignment, value reconciliation, derivation, or interpretive coding of free text — is **not** performed here; it belongs to VS-03 (Editing & Enrichment). The invariant does **not** cover direct identifiers, which are personal data rather than statistical content; these are removed or pseudonymized at this transition to satisfy privacy by design (SAF-P11). The distinction matters: **pseudonymization** replaces a direct identifier with a key that preserves the ability to link records, whereas **removal** deletes the identifier and does not preserve linkage. The content-preservation checks operate on statistical content, not on identifiers — so identifier handling never registers as content loss.
:::


### The Four-Process Governance Pattern

The Statistical Architecture Framework defines that each business domain operates through four distinct process types. This is not a linear sequence but a governance cycle where each process type produces a distinct output that feeds the others.


```{mermaid}
%%| label: fig-3
%%| fig-cap: "The Four-Process Governance Pattern. Each process type produces a distinct artefact class. The cycle closes when Management findings feed back into Design improvements."
%%| fig-width: 6
flowchart LR
    D["**Design**
    _provides metadata_

    Target data models, classification
    strategies, mapping rules, conformance criteria"]
    I["**Implement**
    _provides the execution process_

    Configured mapping engines, coding
    services, validation pipelines"]
    E["**Execute**
    _provides the statistical data_
    Standardized datasets, mapping
    lineage, conformance metadata"]
    M["**Manage**
    _provides quality reports_
    Conformance dashboards, classification
    quality scorecards, improvement recommendations"]

    D -->|"design artefacts
    guide building"| I
    I -->|"production-ready
    process"| E
    E -->|"data & process logs
    for assessment"| M
    M -->|"improvement
    feedback"| D

    style D fill:#7c3aed,color:#fff,stroke:#6d28d9
    style I fill:#2563eb,color:#fff,stroke:#1d4ed8
    style E fill:#059669,color:#fff,stroke:#047857
    style M fill:#d97706,color:#fff,stroke:#b45309
```




### Governing Principles

The following principles directly govern the VS-02.0 business domain:

| Principle | Statement | Application to VS-02.0 |
|---|---|---|
| **SAF-P01** | Actively participate in open source to maintain collective control over statistical processes | NSOs should contribute to open source communities for classification, coding, and mapping tooling (e.g., libraries for SDMX, the statistical data-exchange standard, or coding engines), ensuring collective control over critical standardization capabilities rather than vendor dependence. |
| **SAF-P07** | Implement loosely coupled processes and systems | The standardization domain must be independent from upstream acquisition and downstream editing. Standardized Data (State #2) serves as a decoupling interface — downstream consumers access standardized, classified data without knowledge of the original source structure. |
| **SAF-P08** | Data is shared property | Standardized data, once registered, is available to all authorized consumers. Standardization should not be duplicated across statistical products when the same standardized asset can serve multiple purposes. |
| **SAF-P09** | No data without metadata and classification | Standardization is where classification is applied as a first-class activity. Every standardized dataset carries source-to-target mappings, classification scheme versions, harmonized definitions, units, and a BIV classification (availability, integrity, confidentiality). The principle does not require raw inputs to *arrive* already classified — it requires that data **handed over from State #2 onward** carries the required metadata and classification. This domain is the principal fulfillment point of that obligation. |
| **SAF-P10** | Security By Design | Access controls, integrity verification, and audit logging are embedded in the standardization pipeline so that every mapping and format-coercion operation remains traceable and tamper-evident, not added as an afterthought. |
| **SAF-P11** | Privacy By Design | Removal or pseudonymization of direct identifiers is performed during standardization (the State #1 → State #2 transition), applying data minimization and purpose limitation by design rather than retrofitting privacy after data is processed. |

::: {.callout-note title="Cross-cutting principle application"}
Several principles cut across all four process types. SAF-P09 (no data without metadata and classification) is the defining principle of this domain: Design defines the target classifications and mappings, Execute applies and captures them, Manage assesses classification quality and closes remaining gaps. SAF-P11 (Privacy By Design) applies to Design (Section 3.5), Implementation (Section 4.3), and Execution (confirmed at registration, Section 5.5), where direct identifiers are removed or pseudonymized. SAF-P07 (loosely coupled) governs both the State #1 intake interface from VS-01.0 and the State #2 handover interface to VS-03.0.
:::

### Capability Foundations

VS-02.0 draws on the following SAF capabilities:

| Capability Group | Capabilities | Role in VS-02.0 |
|---|---|---|
| **1.1 Statistical design and build** | 1.1.2 Design statistics product, 1.1.3 Build statistics product | Design the target data models, classification strategies, and build the standardization pipeline |
| **2.1 Data management** | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management, 2.1.4 Statistical register management | Manage data and metadata through standardization, harmonize semantics, assess conformance quality, align with reference registers |
| **3.2 Computerization and automation** | 3.2.1 Application development, 3.2.2 Functional management | Build and maintain mapping engines, coding services, and conformance validation pipelines |
| **3.3 Security and Privacy** | 3.3.1 Privacy management, 3.3.2 Security planning | Ensure direct-identifier removal and security by design across standardization processes |
| **4.1 Governance** | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improve management, 4.1.5 Accountability | Govern the domain, steward classification standards, plan improvements, report on compliance |

### Metadata Perspective

It is considered that metadata is an essential product of the Design phase and a critical concern of every other phase. In this domain, metadata — and classification in particular — is not a by-product but the central asset being created. The table below consolidates the metadata produced across all four process types, covering both data metadata (about the datasets) and process metadata or paradata (about how the process runs).

| Process Type | Data Metadata Produced | Process Metadata (Paradata) Produced |
|---|---|---|
| **Design** | Target data models, classification schemes, code lists, source-to-target mapping rules, conformance criteria, harmonized definitions | Design decisions log, classification version policy, review and approval records |
| **Implement** | Mapping configurations, coding-service parameters, validation rule parameters, catalog templates | Build log, test results, configuration change records, deployment approvals |
| **Execute** | Per-dataset source-to-target mappings, applied classification versions, mapping & format-coercion lineage, conformance scores, profiling statistics | Operator identity, timing, volumes, mapping coverage, unmatched-value counts, engine version |
| **Manage** | Conformance scores, classification quality assessments, coverage reports, lineage assessments, trend analyses | Conformance dashboards, classification quality trends, improvement decisions, audit findings |


## Business Roles and Actors



| Role                        | Process Orientation | Description                                                                                       |
|-----------------------------|---------------------|---------------------------------------------------------------------------------------------------|
| **Upstream Data Provider (VS-01.0)** | External (internal NSO) | Supplies Raw Data (State #1) and its provenance metadata to the standardization domain |
| **Standards Body**          | External            | Maintains classification and exchange standards the NSO conforms to (e.g., Eurostat, UNSD for NACE, ISCO, COICOP, SDMX) |
| **Data Architect**          | Design              | Designs the target data models, canonical schemas, and structural conformance rules               |
| **Classification Steward**  | Design              | Owns classification strategy, code lists, and the 1-to-1 correspondence/lookup tables from source codes to standards |
| **Metadata Architect**      | Design              | Designs harmonized definitions, semantic mappings, unit/period metadata, and the standardized metadata schema |
| **Data Engineer**           | Implementation      | Builds and configures profiling, mapping, and format-coercion components and the standardization pipeline |
| **System Configurator**     | Implementation      | Configures classification services, reference-data connections, and access controls               |
| **Test Manager**            | Implementation      | Plans and executes testing of the standardization pipeline (technical, conformance, integration)   |
| **Process Owner**           | Management          | Accountable for the end-to-end performance of the standardization domain                           |
| **Compliance Officer**      | Management          | Ensures privacy (identifier removal) and standards compliance, produces audit reports              |
| **Quality Manager**         | Management          | Monitors conformance KPIs, produces quality reports, and drives continuous improvement             |
| **Methodologist**           | Design              | Designs the mapping methodology and the cross-source harmonization of definitions and metadata     |
| **Data Quality Analyst**    | Execution           | Profiles data, assesses structural and semantic conformance, and logs unmapped values and exceptions |
| **Data Steward**            | Execution           | Registers standardized datasets, manages metadata entries, and applies access controls            |



## Design Processes — "provides metadata"

*Framework alignment: GSBPM Phases 1–2 — see [Framework Mappings](#framework-mappings).*

The design phase produces the **metadata artefacts** that govern all subsequent phases — above all the target data models, classification schemes, and mapping rules. Without well-designed standards, execution produces inconsistent, incomparable data and management has no baseline to measure conformance against.

### Design Target Data Models and Schemas

The starting point of standardization is defining the canonical structure that all data must conform to. This sub-process specifies the target data model for Standardized Data (State #2): entities, fields, data types, formats, units of measure, cardinalities, and referential constraints. It establishes canonical representations for common concepts — dates, geographies, currencies, organizational and personal identifiers — so that data from surveys, registers, and external sources can be expressed consistently. The team also defines the structural conformance contract: what it means for a dataset to be structurally valid against the target model. Where multiple sources describe the same population, the integration model defines how they are aligned to a common key structure (e.g., a business or statistical unit register key), aligned with GSBPM 2.1.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define canonical target data model for Standardized Data (State #2) — entities, fields, types, formats, units | Target Data Model Specification | GSBPM 2.1 |
| Define canonical representations for common concepts (dates, geography, currency, identifiers) | Canonical Concept Catalog | GSBPM 2.1 |
| Define structural conformance contract and referential constraints | Structural Conformance Rules | GSBPM 2.5 |
| Define integration/linkage key structure for multi-source alignment | Integration Key Design | SAF 2.1.4 |

::: {.callout-tip title="**NSO Example — Business Statistics:**"}
A national statistical organization designing its business statistics data model defines the statistical business register identifier as the canonical linkage key, requires that each turnover figure carry its currency and reference-period basis as metadata (values are recorded as received, not converted), and specifies that economic activity is expressed in NACE Rev. 2 via a maintained correspondence table. The design produces the target schema against which survey returns, VAT register data, and structural business statistics are all aligned.
:::


### Design Classification Mapping Strategy

Once the target structure is set, the classification steward designs how **source codes are mapped one-to-one to standard classifications**. This sub-process selects the authoritative classifications and code lists the NSO conforms to — NACE, ISCO, COICOP, NUTS, SDMX code lists, and GSIM-aligned concepts — and defines the version policy (which version applies, how transitions between versions are handled). The mapping is **deterministic**: maintained correspondence/lookup tables translate a value that already carries a source code into the corresponding standard code, with the original value preserved. The design also specifies how **unmapped or uncoded values are handled** — they are flagged and passed to VS-03 (Editing & Enrichment), which performs any interpretive coding of free text. Reference and master data sources are identified so that mapping is anchored to authoritative registers, aligned with GSBPM 2.5 (Design processing and analysis).

::: {.callout-note}
Interpretive coding of free-text values (e.g., coding a written job title to ISCO) is **not** a VS-02 activity — it requires judgement that can change informational content and is therefore performed in VS-03. VS-02 only applies deterministic source-code → standard-code correspondences.
:::

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Select authoritative classifications and code lists (NACE, ISCO, COICOP, NUTS, SDMX, GSIM concepts) | Classification Standards Register | GSBPM 2.5 |
| Define classification version policy and transition handling | Classification Version Policy | SAF-P09 |
| Design deterministic source-code → standard-code correspondence/lookup tables (1-to-1) | Correspondence Table Set | GSBPM 2.5 |
| Define handling of unmapped/uncoded values (flag and route to VS-03) | Unmapped-Value Routing Rules | GSBPM 2.5 |
| Identify reference and master data sources for mapping | Reference Data Catalog | CSDA Reference Data |

::: {.callout-tip title="**NSO Example — Labour Statistics:**"}
The labour statistics team designs deterministic correspondence tables: source education codes from the Labour Force Survey map one-to-one to ISCED-2011, and source region codes map to NUTS-3. Free-text job titles are **not** coded here — they are flagged and handed to VS-03, where occupation is coded to ISCO-08. VS-02 only re-expresses values that already carry a source code.
:::

### Design Metadata and Semantic Harmonization Rules

This sub-process defines how descriptive metadata and semantics are harmonized so that data from different sources can be *understood* consistently — without changing any value. The team designs the harmonized concept and variable definitions, and the **metadata** that records each variable's unit of measure and reference-period basis (the unit/period is recorded, not converted). Semantic mapping rules link source variables to canonical concepts in the concept system, and quality descriptors (completeness, accuracy, confidentiality flags) are standardized. Where sources use differing definitions for the same concept (e.g., when "employee" is defined differently in a survey and an administrative register), the design specifies that the difference is **recorded as metadata and flagged for VS-03** — VS-02 does not adjust values to reconcile them. The metadata catalog structure for standardized artefacts is designed so that lineage from raw to standardized state is fully traceable — making active metadata a foundation for downstream automation, as emphasized by the CSDA Metadata Management capability.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define harmonized concept and variable definitions | Harmonized Concept System | GSBPM 2.2 |
| Define unit-of-measure and reference-period metadata to be recorded per variable (no conversion) | Unit & Reference-Period Metadata Standards | SAF-P09 |
| Design semantic mapping rules from source variables to canonical concepts | Semantic Mapping Rules | CSDA Metadata Mgmt |
| Design rules to record differing cross-source definitions as metadata and flag them for VS-03 | Definition-Difference Policy | SAF 2.1.4 |
| Design metadata catalog structure and lineage model for standardized artefacts | Catalog Registration Template | CSDA Metadata Mgmt |

### Design Conformance Validation Rules

Before any data is standardized, the acceptance criteria for "standardized" must be clearly defined. This sub-process establishes structural validation rules (field types, formats, value ranges, cardinalities, referential integrity against the target model), classification conformance rules (every mapped code belongs to the correct classification version, no orphan codes), and semantic conformance rules (units, definitions, and reference periods are correctly recorded as metadata against the harmonized standards). Coverage thresholds are agreed — maximum acceptable unmapped-value rate — and exception handling rules are designed to distinguish between outright rejection, conditional acceptance with conformance flags, and routing of unmapped values to VS-03. Crucially, validation rules also verify the **no-loss-of-content** invariant: every value is unchanged, and record counts and key business measures are identical before and after. The GAMSO Quality Management capability provides the overarching control framework.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define structural validation rules against the target model | Structural Validation Rule Set | GSBPM 2.5 |
| Define classification conformance rules (valid codes, correct version, no orphans) | Classification Conformance Rules | GSBPM 2.5 |
| Define semantic conformance rules (units, definitions, reference periods) | Semantic Conformance Rules | GSBPM 2.5 |
| Define no-loss-of-content checks (record/measure preservation across standardization) | Content-Preservation Checks | GAMSO QM |
| Design exception handling rules: rejection vs. conditional acceptance vs. manual review | Exception Handling Policy | GSBPM 2.5 |

### Design Standardization Registration and Privacy Framework

The final design sub-process ensures that standardized artefacts are correctly registered, traceable, and privacy-compliant. Each standardized dataset receives a BIV classification (Availability, Integrity, Confidentiality) per SAF-P09, and role-based access controls for the standardized data repository are designed in accordance with SAF-P10. The lineage model is designed so that every standardized field can be traced back to its raw source value and the mapping rule applied. Privacy protection follows SAF-P11: the standardization stage is where direct identifiers are removed or replaced with pseudonymous keys, so the design specifies which identifiers are dropped, which are pseudonymized, the pseudonymization method and key management, and data minimization rules. Audit logging requirements — what mapping & format-coercion events must be recorded — complete the design.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define BIV data classification for standardized datasets | Data Classification Policy | SAF-P09 |
| Design role-based access control for the standardized data repository | Access Control Design | SAF-P10 |
| Design lineage model: standardized field → raw source value → mapping rule | Lineage Model Specification | CSDA Traceability |
| Design identifier removal/pseudonymization: which identifiers, method, key management, minimization | Privacy & Pseudonymization Design | SAF-P11 |
| Design mapping & format-coercion audit logging requirements | Audit Logging Specification | SAF-P10 |

```{mermaid}
%%| label: fig-4
%%| fig-cap: "Design Process Decomposition. Raw data structure, framework and classification standards flow into five design sub-processes, producing metadata artefacts that govern Implementation, Execution, and Management."
%%| fig-width: 6
flowchart TB
    subgraph inputs["Inputs"]
        RM["Raw Data Model<br/><small>(State #1 schema)</small>"]
        FW["Framework Standards<br/><small>GSBPM · GAMSO · CSDA</small>"]
        CL["Classification Standards<br/><small>NACE · ISCO · COICOP · SDMX</small>"]
        LAW["Legal & Privacy"]
    end

    subgraph design["Design Sub-Processes"]
        D1["3.1 Target Data Models<br/>& Schemas"]
        D2["3.2 Classification<br/>Mapping Strategy"]
        D3["3.3 Metadata & Semantic<br/>Harmonization Rules"]
        D4["3.4 Conformance<br/>Validation Rules"]
        D5["3.5 Registration &<br/>Privacy Framework"]
    end

    subgraph outputs["Metadata Artefacts"]
        O1["Target Data Model"]
        O2["Correspondence Tables"]
        O3["Harmonized Concepts"]
        O4["Conformance Rule Set"]
        O5["Lineage & Privacy Design"]
    end

    RM --> D1
    CL --> D2
    FW -.->|inform| design
    LAW --> D5

    D1 --> D2 --> D3 --> D4 --> D5

    D1 --> O1
    D2 --> O2
    D3 --> O3
    D4 --> O4
    D5 --> O5

    outputs -->|govern| NEXT["Implementation (§4) · Execution (§5)<br/>measured by Management (§6)"]

    style design fill:#f5f3ff,stroke:#7c3aed
    style outputs fill:#ede9fe,stroke:#7c3aed
```

## Implementation Processes — "provides the execution process"

*Framework alignment: GSBPM Phase 3 (Build) — see [Framework Mappings](#framework-mappings).*

The implementation phase takes the metadata artefacts from Design and **builds, configures, and tests** the production-ready standardization pipeline. Nothing runs operationally until this phase is complete.

### Build Profiling and Mapping Engines

This sub-process turns the target data model and mapping designs into operational tools. Profiling components are built to analyze incoming raw data structure — inferring types, detecting cardinalities, value distributions, and structural anomalies — so that the pipeline can report how far each source is from the target model. The mapping & format-coercion component is built or configured to apply the designed **value-preserving** operations: renaming, restructuring, type casting, reformatting (e.g., CSV→XML), and key alignment. It does **not** convert units, currencies, or reference periods — those are recorded as metadata and any conversion is performed in VS-03. The component is configured to be declarative and lineage-aware, capturing for each output field which input field and which rule produced it. All mapping logic is version-controlled in line with SAF-P10 so that any standardized record can be reproduced from raw data, following GSBPM 3.1.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Build data profiling components (type inference, cardinality, distributions, anomalies) | Production-ready profiling module | GSBPM 3.1 |
| Build/configure the mapping & format-coercion component (rename, restructure, cast, reformat, align keys) | Configured mapping component | GSBPM 3.1 |
| Configure lineage capture for every mapping/coercion operation | Lineage-aware mapping modules | CSDA Traceability |
| Version-control all mapping & format-coercion logic | Versioned mapping repository | SAF-P10 |

::: {.callout-tip title="**NSO Example — Price Statistics:**"}
The implementation team builds a component that coerces heterogeneous retailer price feeds into the canonical price record structure — reshaping fields and casting types — and records each item's currency, unit (e.g., price-per-kilogram), and scrape timestamp **as metadata**. Prices are stored exactly as received. Converting currencies/units to a common basis and coding each product to its COICOP item require judgement and are performed in VS-03; VS-02 only re-structures and annotates. Lineage is captured so every standardized record links back to the exact raw scrape record.
:::

### Configure Classification Mapping Services

The designed correspondence tables are translated into automated mapping services in this sub-process. Deterministic lookup/correspondence tables are loaded and connected to authoritative reference data, so that a value already carrying a source code is translated one-to-one to the corresponding standard code, following GSBPM 3.2. Classification version control is configured so the correct version is applied and version transitions are managed. Values with no matching correspondence (and any free-text/uncoded values) are routed to VS-03 rather than coded here. Reference and master data connections are configured so mapping stays synchronized with authoritative registers.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Load correspondence/lookup tables for deterministic source-code → standard-code mapping | Configured mapping services | GSBPM 3.2 |
| Configure classification version control and transition handling | Version-controlled classifications | SAF-P09 |
| Configure routing of unmapped/uncoded values to VS-03 | Unmapped-value routing | GSBPM 3.4 |
| Configure reference/master data connections | Synchronized reference data | CSDA Reference Data |

### Build Conformance Validation Pipelines and Metadata Registration

This sub-process implements the conformance validation rules and the registration of standardized artefacts. Structural, classification, semantic, and content-preservation checks (Section 3.4) are implemented as automated validations that run on every standardized dataset. The metadata catalog entries are built from the designed model (Section 3.3), and automatic metadata propagation is configured so that mapping lineage, applied classification versions, harmonized definitions, and conformance scores flow into the catalog. Identifier removal/pseudonymization is implemented per the privacy design (Section 3.5). Event notifications are configured so that downstream consumers (VS-03.0) are alerted when standardized data is registered, and exception workflows route non-conforming data to manual review. As the CSDA emphasizes, active metadata — metadata that can drive standardization rules and downstream processing specifications — is the ultimate goal.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Implement conformance checks as automated validations (structural, classification, semantic, content-preservation) | Automated conformance pipeline | GSBPM 3.2 |
| Implement identifier removal/pseudonymization per privacy design | Pseudonymization component | SAF-P11 |
| Configure automatic metadata & lineage propagation into the catalog | Automated metadata pipelines | CSDA Metadata Mgmt |
| Configure "Standardized Data Registered" event for downstream consumers | Event publication | GSBPM 3.2 |
| Configure exception handling workflows | Non-conformance routing & review queues | GSBPM 3.4 |

### Test and Validate the Pipeline

Before the pipeline goes into production, it must be rigorously verified. Technical testing covers all individual components — profilers, mapping & format-coercion component, mapping services, validators, and catalog (GSBPM 3.5). Integration testing validates the end-to-end flow from raw data intake through mapping, validation, to catalog registration. A pilot run with real or synthetic data (GSBPM 3.6) verifies that source codes are correctly mapped one-to-one, mapping lineage is complete, conformance criteria are enforced, the no-loss-of-content invariant holds (every value unchanged; record counts and key measures preserved), unmapped values are correctly routed to VS-03, and identifier removal works as designed. Performance testing confirms the pipeline can handle expected volumes within processing windows. The phase concludes with finalization of the production system and documentation of operational procedures (GSBPM 3.7).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Technical testing of all individual components | Unit test reports | GSBPM 3.5 |
| Integration testing: end-to-end flow from raw intake to registration | Integration test report | GSBPM 3.5 |
| Pilot with real or synthetic data; verify lineage, no-loss-of-content, and unmapped-value routing | Pilot report, validated lineage | GSBPM 3.6 |
| Verify correspondence-table mappings against the source code lists | Mapping verification report | GSBPM 3.6 |
| Performance testing against expected volumes | Performance test report | GSBPM 3.6 |
| Finalize production system and document operational procedures | Operational Procedures Manual, Production-Ready Pipeline | GSBPM 3.7 |

```{mermaid}
%%| label: fig-5
%%| fig-cap: "Implementation Pipeline from design artefacts through build/configure/test to production-ready system."
%%| fig-width: 6
flowchart LR
    subgraph design_artefacts["Design Artefacts (from Section 3)"]
        DA1["Target Data Model\n& Schemas"]
        DA2["Classification\nMapping Strategy"]
        DA3["Harmonization\nRules"]
        DA4["Conformance\nValidation Rules"]
        DA5["Lineage &\nPrivacy Framework"]
    end

    subgraph build["Build & Configure"]
        B1["4.1 Build Profiling\n& Mapping Engines"]
        B2["4.2 Configure\nClassification\nMapping Services"]
        B3["4.3 Build Conformance\nValidation &\nRegistration"]
    end

    subgraph test["Test & Validate"]
        T1["4.4 Technical\nTesting"]
        T2["4.4 Pilot &\nMapping Verification"]
        T3["4.4 Performance\n& Lineage"]
    end

    subgraph output["Production-Ready"]
        PR["Operational\nStandardization\nPipeline"]
        OP["Operational\nProcedures"]
    end

    DA1 & DA3 --> B1
    DA2 --> B2
    DA4 & DA5 --> B3

    B1 & B2 & B3 --> T1 --> T2 --> T3
    T3 --> PR & OP

    PR -->|"ready for"| EXEC["Execution\n(Section 5)"]

    style build fill:#eff6ff,stroke:#2563eb
    style test fill:#dbeafe,stroke:#2563eb
```

## Execution Processes — "provides the statistical data"

*Framework alignment: the later GSBPM phases for this domain — see [Framework Mappings](#framework-mappings).*

The execution phase runs the **designed and implemented pipeline** operationally for each production cycle. This corresponds to the five VS-02 value stream stages. In a mature steady state, much of the work has been pre-designed (Section 3) and pre-built (Section 4) — execution focuses on running the cycle, applying mappings and classifications, capturing lineage and conformance metadata, and ensuring conformance gates are passed without altering data content.

### Profile and Assess Data Structure

**Value created:** *A clear understanding of how far incoming raw data is from the target standard, so the right mapping and format coercion can be applied.*

When a "Raw Data Registered" event is received from VS-01.0, the standardization domain begins by profiling the incoming dataset. Per-cycle execution applies the profiling components (Section 4.1) to analyze structure, infer types, measure cardinalities and value distributions, and detect inconsistencies, missing fields, and structural anomalies relative to the target data model. The dataset is then compared against the target schema to produce a structure-gap assessment — which fields map directly, which require format coercion, which source codes have a standard correspondence, and which values are uncoded and must be routed to VS-03. Significant or unexpected structural deviations (e.g., a source that has changed its schema) trigger a return to the design process rather than ad-hoc adaptation during execution, applying GSBPM 5.1 in its recurrent form.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Profile incoming raw data: types, cardinalities, distributions, anomalies | Data Profiling Report | GSBPM 5.1 |
| Compare structure against the target data model | Structure-Gap Assessment | GSBPM 5.1 |
| Identify required format coercion and code mappings to apply | Mapping Plan (per dataset) | GSBPM 5.1 |
| Flag unexpected structural deviations for design review | Schema-change exception (if any) | GSBPM 5.1 |

::: {.callout-tip title="**NSO Example — Tax Register Intake:**"}
The quarterly corporate tax file (Raw Data registered by VS-01.0) is profiled on arrival: 47 fields detected, corporate identifier present at 99.8% coverage, economic activity supplied as the tax authority's internal code (which has a maintained correspondence to NACE), and turnover provided in thousands of euro. The structure-gap assessment flags the activity-code correspondence mapping and the format coercion of the XML as the VS-02 work; it records that turnover's unit basis ("thousands of EUR") must travel as metadata and that converting it to a common unit is a VS-03 activity.
:::

### Apply Standard Classifications and Formats

**Value created:** *Source codes re-expressed in shared, authoritative classifications and a common format so data is comparable across sources — with no value changed.*

This is the core standardization sub-process. The mapping & format-coercion component applies the designed **value-preserving** operations — renaming, restructuring, type casting, reformatting (e.g., CSV→XML), and key alignment — to bring the data into the target format. The mapping services then translate values that **already carry a source code** to the corresponding standard classification (NACE, ISCO, COICOP, NUTS, SDMX code lists) via deterministic correspondence/lookup tables, one-to-one, preserving the original value. Values that have no correspondence, or that are free text requiring interpretation, are **not** coded here — they are flagged and routed to VS-03. Throughout, the no-loss-of-content principle is enforced: only the representation changes and standard codes are added; the underlying information is preserved — aligned with GSBPM 5.2. Every applied mapping and classification version is recorded as lineage metadata.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Apply format coercion (rename, restructure, cast, reformat, align keys) | Format-coerced dataset (values unchanged) | GSBPM 5.1 |
| Map source codes to standard classifications via correspondence/lookup (1-to-1) | Standard-coded dataset (original preserved) | GSBPM 5.2 |
| Flag unmapped/uncoded and free-text values and route them to VS-03 | Unmapped-value handover list | GSBPM 5.2 |
| Capture applied mappings and classification versions as lineage | Mapping & classification lineage | SAF-P09 |

```{mermaid}
%%| label: fig-6
%%| fig-cap: "Classification Mapping Architecture. Values that already carry a source code are mapped one-to-one to standard classifications via correspondence/lookup tables, with the original preserved; unmapped and free-text values are routed to VS-03 for interpretive coding. No value is changed in VS-02."
%%| fig-width: 6
flowchart LR
    subgraph sources["Raw Data Inputs"]
        direction TB
        SV["Survey Data\n(source codes + free text)"]
        AD["Administrative Data\n(source codes)"]
        EM["Emerging Sources\n(mixed values)"]
    end

    subgraph mapping["Deterministic Mapping (1-to-1)"]
        L["Correspondence /\nLookup tables"]
    end

    subgraph target["Standard Output"]
        ST["Standard-coded Values\n(original preserved)"]
    end

    V3["VS-03\nEditing & Enrichment\n(interpretive coding)"]

    SV -->|"+ format coercion"| mapping
    AD -->|"+ format coercion"| mapping
    EM -->|"+ format coercion"| mapping

    L -->|"source code has\ncorrespondence"| ST
    L -.->|"unmapped / free text"| V3

    style sources fill:#ecfdf5,stroke:#059669
    style mapping fill:#f0fdf4,stroke:#059669
    style V3 fill:#fee2e2,stroke:#b91c1c
```


::: {.callout-tip title='**NSO Example — Labour Force Survey Standardization:**'}
The LFS returns are standardized in VS-02 by deterministic mapping only: source education codes map one-to-one to ISCED-2011 and source region codes map to NUTS-3 via correspondence tables, and the XML is coerced to the target schema. The 42,000 free-text occupation strings are **not** coded here — they are flagged and handed to VS-03, where occupation is coded to ISCO-08. No response value is altered — values are only re-expressed in standard codes where a deterministic correspondence exists.
:::


### Align Metadata and Semantics

**Value created:** *Coherent, shared meaning across datasets so the same concept means the same thing everywhere.*

Once structure and codes are standardized, the descriptive metadata and semantics are harmonized — at the **metadata level only, without changing any value**. Source variables are linked to canonical concepts in the concept system; each variable's unit of measure and reference-period basis are **recorded as metadata** against the standard conventions (not converted); and where sources use differing definitions for the same concept (e.g., two sources defining "employee" differently), the difference is **recorded as metadata and flagged for VS-03** rather than reconciled by adjusting values. Quality descriptors (completeness, accuracy, confidentiality flags) are standardized and attached. The harmonized metadata is bound to the dataset so that downstream consumers receive both the standardized data and the coherent semantics needed to interpret it, aligned with GSBPM 5.1 and the CSDA Metadata Management capability.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Link source variables to canonical concepts | Concept-aligned variables | GSBPM 5.1 |
| Record unit-of-measure and reference-period basis as metadata (no conversion) | Unit & period metadata | SAF-P09 |
| Record differing cross-source definitions as metadata and flag them for VS-03 | Definition-difference record | SAF 2.1.4 |
| Standardize and attach quality descriptors | Harmonized quality metadata | CSDA Metadata Mgmt |

::: {.callout-tip title="**NSO Example — Multi-Source Business Statistics:**"}
Turnover arrives from the structural business survey, the VAT register, and a commercial dataset. VS-02 links each turnover variable to the canonical concept and **records** each source's currency, unit, and reference-period basis as metadata — noting, for instance, that the VAT register reports on a fiscal-year basis and the survey on a calendar-year basis. VS-02 does **not** adjust the values to a common basis; the period and unit differences are carried as metadata and the alignment/conversion is performed downstream in VS-03, keeping the difference transparent and the original values intact.
:::

### Validate Structural and Semantic Conformance

**Value created:** *Confidence that the standardized data conforms to standards and that no content was lost in standardization.*

Before standardized data can be accepted, it must pass the conformance gates. The validation process runs the automated checks from Section 3.4: structural validation against the target model (types, formats, ranges, cardinalities, referential integrity), classification conformance (every mapped code belongs to the correct classification version, no orphan codes, mapping coverage above the threshold), and semantic conformance (units, definitions, and reference periods are correctly recorded as metadata against the harmonized standards). Critically, content-preservation checks verify the no-loss-of-content invariant — every value is unchanged, and record counts and key business measures are identical before and after. A conformance assessment is produced, with a structural score, mapping coverage rate, and semantic conformance rating. Every result, exception, and decision is logged in a mapping & format-coercion audit trail capturing both data metadata (what was validated, what passed) and process metadata (who validated, when, which rule and engine version). The outcome is one of two business events: *Standardization Conformed* (proceed to registration) or *Standardization Non-Conformant* (trigger exception handling — re-map, route unmapped values to VS-03, or accept conditionally with a conformance flag).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Validate structure against the target model | Structural validation result | GSBPM 5.3 |
| Validate classification conformance (valid codes, correct version, coverage) | Classification conformance result | GSBPM 5.3 |
| Validate semantic conformance (units, definitions, reference periods) | Semantic conformance result | GSBPM 5.3 |
| Run no-loss-of-content checks (record/measure preservation) | Content-preservation result | GAMSO QM |
| Create audit trail: log all conformance results, exceptions, and decisions | Audit trail record | GAMSO QM |

::: {.callout-important}
**Boundary:** NO value is changed at this stage. Standardization re-expresses structure and format, adds standard codes by 1-to-1 mapping, and attaches metadata — nothing more. The following are explicitly the responsibility of **VS-03.0 Data Editing and Enrichment**, not VS-02: content correction, imputation, enrichment, **unit and currency conversion, reference-period alignment, value reconciliation across sources, derivation of new variables, and interpretive coding of free text**.
:::

::: {.callout-tip title="**NSO Example — Price Data Conformance:**"}
The standardized daily price dataset is validated: all 11,875 records conform structurally to the canonical price record, every product whose source code has a COICOP correspondence is mapped (the rest are flagged for VS-03), each price carries its currency and unit as metadata with the value left exactly as received, and the record count and observed price points match the raw scrape exactly (no-loss-of-content confirmed). Result: Standardization Conformed. All results logged with rule version, engine version, and operator ID.
:::

### Register Standardized Artefacts

**Value created:** *Secure, organized, and traceable storage of standardized data, discoverable by downstream consumers.*

The final execution sub-process persists conformant standardized data and makes it discoverable to the rest of the statistical system. Each standardized dataset version receives a unique persistent identifier (URI/UUID) and is stored in the standardized data repository, in line with SAF-P07's principle of loose coupling from downstream processing. Identifier removal/pseudonymization is confirmed applied per the privacy framework (SAF-P11). Metadata is registered in the catalog per SAF-P09: each dataset is linked to its source-to-target mapping lineage, applied classification scheme versions, harmonized concept and quality metadata, and conformance assessment results. Full lineage is recorded — Raw Data (State #1) to Standardized Data (State #2), traceable to the originating source — and access permissions are applied per the designed framework (Section 3.5, SAF-P10). The sub-process concludes by publishing a "Standardized Data Registered" event, notifying downstream VS-03.0 that new standardized data is available for editing and enrichment.

**Output:** **Standardized Data (Steady State #2)** — the official handover artefact to the rest of the statistical value chain.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Assign unique persistent identifier (URI/UUID) to the standardized dataset version | Dataset ID | GSBPM 5.1 |
| Persist data in the standardized data repository | Stored standardized artefact | SAF-P07 |
| Confirm identifier removal/pseudonymization applied | Privacy-compliant dataset | SAF-P11 |
| Register metadata: mapping lineage, classification versions, harmonized concepts, conformance, lineage | Catalog registration | SAF-P09 |
| Apply access permissions per designed framework | Access-controlled dataset | SAF-P10 |
| Publish "Standardized Data Registered" event to notify VS-03.0 | Event notification | SAF-P07 |

```{mermaid}
%%| label: fig-7
%%| fig-cap: "Standardized Data Artefact Structure. Reading guide: each box is a type of record with its fields; a connecting line means the records are linked. Each standardized artefact is linked to its mapping lineage, applied classifications, conformance assessment, and privacy/access classification."
%%| fig-width: 6
erDiagram
    STANDARDIZED_DATA_ARTEFACT {
        string dataset_id PK "Unique persistent URI/UUID"
        string dataset_version "Version identifier"
        string target_model_version "Canonical model version applied"
        string reference_period_basis "Reference-period basis (metadata, not converted)"
        datetime registration_timestamp "When registered in catalog"
    }
    MAPPING_LINEAGE {
        string source_dataset_id "Raw Data (State #1) source ID"
        string mapping_ruleset_version "Mapping & format-coercion ruleset version"
        string engine_version "Standardization engine version"
        string mapping_log_ref "Field-level lineage reference"
    }
    CLASSIFICATION_RECORD {
        string classification_scheme "NACE/ISCO/COICOP/NUTS/etc"
        string scheme_version "Classification version applied"
        float mapping_coverage "Percentage of source codes mapped 1-to-1"
        int unmatched_values "Count routed to VS-03 (unmapped/free text)"
        int orphan_codes "Count of non-conforming codes"
    }
    CONFORMANCE_ASSESSMENT {
        float structural_score "Structural conformance %"
        float mapping_coverage "Mapped-code coverage %"
        string semantic_rating "Pass/Conditional/Fail"
        boolean content_preserved "No-loss-of-content verified (no value changed)"
        int conformance_errors "Count of conformance issues"
    }
    PRIVACY_RECORD {
        string identifiers_removed "Direct identifiers dropped"
        string pseudonymization_method "Method applied"
        string biv_classification "Availability/Integrity/Confidentiality"
        string access_level "Public/Internal/Restricted/Secret"
    }

    STANDARDIZED_DATA_ARTEFACT ||--|| MAPPING_LINEAGE : "derived via"
    STANDARDIZED_DATA_ARTEFACT ||--|| CLASSIFICATION_RECORD : "classified by"
    STANDARDIZED_DATA_ARTEFACT ||--|| CONFORMANCE_ASSESSMENT : "has conformance record"
    STANDARDIZED_DATA_ARTEFACT ||--|| PRIVACY_RECORD : "protected by"
```

## Management Processes — "provides quality reports"

*Framework alignment: GSBPM overarching Quality/Metadata Management — see [Framework Mappings](#framework-mappings).*

The management phase runs **alongside and after** execution. It monitors the standardization domain's performance, assesses the conformance and classification quality of standardized data, ensures compliance, and feeds improvement recommendations back into the design phase — closing the governance cycle.

### Monitor Process Performance

Operational performance of the standardization domain must be tracked systematically across production cycles. The process owner and quality manager collect and aggregate key performance indicators, monitor throughput against processing windows, and track paradata — who performed each step, when, how long it took, what engine and classification versions were used, what exceptions occurred. This information feeds process performance dashboards that give the process owner a real-time view of domain health, aligned with the GAMSO Quality Management capability for monitoring performance across the production lifecycle.

**Key Performance Indicators (KPIs):**

| KPI | Description | Measurement |
|---|---|---|
| Mapping coverage | Percentage of source codes mapped 1-to-1 to a valid standard code | Per dataset, per classification |
| Unmapped-value rate | Percentage of values with no correspondence, routed to VS-03 | Per source, per cycle |
| Conformance pass rate | Percentage of datasets passing conformance on first run | Per source, per cycle |
| Format-conformance rate | Percentage of records conforming to the target structure/format | Per dataset, per cycle |
| Processing time | Duration from raw intake to standardized registration | Per dataset, per cycle |
| Re-mapping rate | Frequency of datasets returned for re-mapping or design change | Per source, per cycle |

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Collect and aggregate KPIs per production cycle | Process Performance Dashboard | GAMSO QM |
| Monitor throughput against processing windows | Throughput Report | GAMSO QM |
| Track paradata: operator, timing, engine/classification versions, exceptions | Paradata Records | GAMSO QM |
| Generate process performance dashboards | Dashboard for Process Owner | GAMSO QM |

### Assess Standardization Quality

Beyond process performance, the quality of the standardized data itself must be evaluated against the criteria established in the design phase. Each standardized dataset is assessed across multiple quality dimensions: mapping completeness (proportion of source codes successfully mapped 1-to-1, unmapped-value rate routed to VS-03), classification conformance (no orphan codes, correct version), structural and format conformance (alignment with the target model), metadata completeness (units, reference-period bases, definitions correctly recorded), and content preservation (confirmation that no value was changed and record counts/key measures are identical). Results are compared against the designed quality criteria from Section 3.4. Quality indicators are produced per dataset, per source, and per production cycle, and quality trends are tracked to detect deteriorating sources, growing unmapped-value rates, or classification version issues. This aligns with the CSDA Data Quality capability and SAF Capability 2.1.3 for statistical quality management.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Assess mapping completeness and unmapped-value rate | Mapping Completeness Report (per cycle) | SAF 2.1.3 |
| Assess classification conformance and orphan-code rate | Conformance & Orphan-Code Report | CSDA Data Quality |
| Assess structural/format conformance, metadata completeness, and content preservation | Conformance Quality Report | SAF 2.1.3 |
| Identify quality trends across sources, classifications, and cycles | Quality Trend Analysis | SAF 2.1.3 |

### Manage Classification and Metadata Lifecycle

The classification standards and metadata ecosystem supporting standardization must remain complete, accurate, and current. This sub-process governs the lifecycle of classification versions — adopting new versions (e.g., a NACE or COICOP revision), managing transition periods, and maintaining the mapping tables and correspondence tables between versions. It verifies metadata completeness — that every standardized dataset carries full mapping lineage, classification versions, and harmonized concepts as an SAF-P09 compliance check — and maintains the concept system, code lists, and reference data so mapping stays anchored to authoritative sources. Metadata lineage from raw through standardization to standardized state is tracked, and reconciliation across systems ensures catalog entries match stored artefacts. As the CSDA emphasizes, active, well-managed metadata is what makes standardized data reusable and downstream automation possible.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Govern classification version lifecycle and correspondence tables | Classification Version & Correspondence Register | SAF-P09 |
| Verify metadata completeness for all standardized datasets | Metadata Quality Report | SAF-P09 |
| Maintain concept system, code lists, and reference data | Reference Data Maintenance Log | CSDA Metadata Mgmt |
| Track metadata lineage from raw through standardization to standardized state | Metadata Lineage Audit | CSDA Traceability |
| Reconcile metadata across systems | Catalog-artefact reconciliation | SAF-P09 |

### Audit and Compliance Reporting

This sub-process produces the evidence that the standardization domain operates within legal, regulatory, and organizational requirements. Audit trail reports demonstrate full traceability of every standardized value from raw source through the mapping rules applied — supporting reproducibility and content-preservation assurance. Privacy compliance reporting covers identifier removal/pseudonymization, confirming that direct identifiers have been dropped or replaced at the State #1 → State #2 transition per SAF-P11, and that data minimization has been applied. Standards compliance reporting confirms conformance to the adopted classifications and exchange standards (e.g., SDMX), and security compliance reporting verifies that designed access controls and audit logging have been applied. These reports satisfy the SAF Capability 4.1.5 (Accountability) obligation and feed into VS-07.0 Governance and Compliance.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Produce audit trail reports: full lineage from raw value to standardized value | Audit Trail Summary | SAF 4.1.5 |
| Report on privacy compliance: identifier removal/pseudonymization, minimization | Privacy Compliance Record | SAF-P11 |
| Report on standards compliance (classifications, SDMX exchange) | Standards Compliance Report | SAF 4.1.5 |
| Report on security compliance: measures applied, breaches, incidents | Compliance Report (per cycle) | SAF-P10 |

### Continuous Improvement

The final management sub-process closes the governance loop by analyzing performance and quality data to identify and drive improvements. Quality trends across production cycles are examined: is mapping coverage improving, is the unmapped-value rate falling, are conformance pass rates rising, is the re-mapping rate decreasing? Improvement opportunities are identified — extending and maintaining correspondence tables to raise coverage, refining mappings that generate orphan codes, adopting new classification versions, and simplifying conformance rules that generate false positives. Where recurring unmapped values point to a source that needs interpretive coding, that need is communicated to VS-03 rather than absorbed into VS-02. These improvement recommendations are fed back to the design processes (Section 3), prioritized based on impact and feasibility, and tracked through subsequent design-implement-execute cycles. This is the SAF Capability 4.1.4 (Improve management) in action, and it connects to the GAMSO concept of transferring mature capabilities from innovation into production.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Analyze quality trends across production cycles | Improvement Recommendations Report | SAF 4.1.4 |
| Identify improvement opportunities: correspondence-table extension, mapping refinement, version adoption | Updated Design Inputs | SAF 4.1.4 |
| Feed recommendations back to design processes (Section 3) | Design feedback (closing the governance loop) | SAF 4.1.4 |
| Prioritize improvements based on impact and feasibility | Improvement Tracking Log | GAMSO Capability Mgmt |
| Track implementation of accepted improvements | Improvement Tracking Log | GAMSO Capability Mgmt |

```{mermaid}
%%| label: fig-8
%%| fig-cap: "Management Feedback Loop. Execution data flows through monitoring, quality assessment, classification/metadata management, and audit processes. Continuous improvement feeds recommendations back to Design, closing the governance cycle."
%%| fig-width: 6
flowchart TD
    E["Execution\n(Section 5)<br/><em>data + paradata</em>"]

    M1["6.1 Monitor<br/>Process Performance<br/><em>KPIs, throughput</em>"]
    M2["6.2 Assess<br/>Standardization Quality<br/><em>mapping coverage</em>"]
    M3["6.3 Manage Classification<br/>& Metadata Lifecycle<br/><em>versions, reference data</em>"]
    M4["6.4 Audit &<br/>Compliance Reporting<br/><em>lineage, privacy</em>"]
    M5["6.5 Continuous<br/>Improvement<br/><em>recommendations</em>"]

    D["Design<br/>(Section 3)<br/><em>updated rules & classifications</em>"]

    E --> M1
    E --> M2
    M1 --> M2
    M2 --> M3
    M3 --> M4
    M4 --> M5
    M5 -->|"feedback loop"| D

    M1 -->|"dashboards"| PO["Process Owner"]
    M2 -->|"quality reports"| QM["Quality Manager"]
    M4 -->|"compliance reports"| VS07["VS-07.0\nGovernance"]

    style E fill:#ecfdf5,stroke:#059669
    style D fill:#f5f3ff,stroke:#7c3aed
    style M5 fill:#fef3c7,stroke:#d97706
```

## Business Services and Interfaces

The VS-02.0 business domain exposes the following services:

| Service | Direction | Consumers | Mapped Processes |
|---|---|---|---|
| **Standardization Service** | Internal (VS-01.0 → NSO) | Raw data consumers, standardization teams | 5.1 Profile, 5.2 Apply Classifications |
| **Classification Mapping Service** | Internal | Standardization teams, methodologists, other domains needing code mapping | 5.2 Apply Standard Classifications |
| **Semantic Harmonization Service** | Internal | Metadata architects, downstream analysts | 5.3 Align Metadata and Semantics |
| **Conformance Validation Service** | Internal | Process owners, quality managers | 5.4 Validate Conformance |
| **Standardized Data Provisioning Service** | Internal (NSO → VS-03.0) | Editing & enrichment teams, data analysts | 5.5 Register Standardized Artefacts |
| **Classification Catalog Service** | Internal | All data consumers across the NSO | 6.3 Manage Classification & Metadata Lifecycle |
| **Design and Methodology Service** | Internal | Methodologists, data architects, classification stewards | 3.1–3.5 All design processes |

**Interface specifications:**

- **Standardized Data Provisioning Service** interface: event-driven notification ("Standardized Data Registered") + catalog query API for downstream consumers to discover and access standardized datasets and their lineage
- **Classification Mapping Service** interface: mapping API (source code → standard code via deterministic correspondence), SDMX-compliant code list exchange, correspondence-table lookup
- **Classification Catalog Service** interface: search/browse API for classifications, code lists, and concept definitions, with SDMX-compliant metadata exchange

### Boundary Interface Specifications

The domain is loosely coupled (SAF-P07) to its neighbors through two steady-state interfaces. Specifying each boundary explicitly — the handover artefact, the metadata it must carry, the event that triggers it, and where responsibility transfers — makes the loose-coupling contract concrete and testable.

| Boundary | Handover Artefact | Required Metadata | Trigger Event | Responsibility Transfer |
|---|---|---|---|---|
| **VS-01.0 → VS-02.0** (intake) | Raw Data (State #1) | Provenance, source, collection method, receipt timestamp, file hash, agreement reference, BIV classification | "Raw Data Registered" event | VS-01.0 retains custody of the raw artefact; VS-02.0 assumes responsibility for standardization on event receipt |
| **VS-02.0 → VS-03.0** (handover) | Standardized Data (State #2) | Source-to-target mapping lineage, applied classification scheme versions, recorded unit/currency/reference-period bases, list of unmapped/uncoded values for VS-03 to code, definition-difference records, conformance assessment, pseudonymization record, BIV classification | "Standardized Data Registered" event | VS-02.0 retains custody of the standardized artefact; VS-03.0 assumes responsibility for editing & enrichment — including any value conversion, interpretive coding, and reconciliation — on event receipt |

Each interface exchanges a registered, immutable steady-state artefact plus its metadata — never internal working data — so neither side needs knowledge of the other's internal processing.

## Business Objects and Data Flow

```{mermaid}
%%| label: fig-9
%%| fig-cap: "Business Object Lifecycle across all four process types. Design objects govern implementation, which produces the pipeline that standardizes execution objects, which are assessed by management objects, which feed back to design."
%%| fig-width: 6
flowchart TB
    design["🔷 Design Artefacts<br/><small>Target Model · Classification Strategy<br/>Harmonization Rules · Conformance Rules · Privacy Design</small>"]
    implement["🔧 Implementation Assets<br/><small>Mapping & Format-Coercion · Mapping Services<br/>Conformance Pipeline · Catalog Config</small>"]
    execute["⚡ Execution Objects"]
    manage["📊 Management Reports"]

    design -->|"govern building"| implement
    implement -->|"produces pipeline<br/>that processes"| execute
    execute -->|"assessed by"| manage
    manage -->|"feeds back to"| design

    subgraph execute_detail [" "]
        direction LR
        RD["Raw Data<br/>(State #1)"]:::bo -->|"standardized as"| SD["Standardized Data<br/>(State #2)"]:::bo
    end

    execute --> execute_detail
    RD -->|generates| logs["Mapping Lineage · Conformance · Audit"]

    classDef bo fill:#fbbf24,stroke:#b45309,color:#000
    style design fill:#f5f3ff,stroke:#7c3aed
    style implement fill:#dbeafe,stroke:#2563eb
    style execute fill:#fef9c3,stroke:#b45309
    style manage fill:#dcfce7,stroke:#16a34a
    style execute_detail fill:none,stroke:none
    style logs fill:#fff,stroke:#888,stroke-dasharray: 5 5
```


## Business Events

```{mermaid}
%%| label: fig-10
%%| fig-cap: "Event-Driven Choreography between the upstream domain (VS-01.0) and NSO teams, showing events across the Design → Implement → Execute → Manage cycle. The management phase closes the loop by feeding improvements back to design."
%%| fig-width: 6

sequenceDiagram
    participant US as Upstream (VS-01.0)
    participant NSO as NSO Teams
    participant PM as Process Mgmt

    rect rgb(245, 243, 255)
    Note over NSO: Design Phase
    NSO->>NSO: Define target model, classification strategy,<br/>harmonization & conformance rules
    NSO-->>NSO: Design Artefacts Published
    end

    rect rgb(239, 246, 255)
    Note over NSO: Implementation Phase
    NSO->>NSO: Build mapping & format-coercion, mapping services,<br/>conformance pipeline & catalog
    NSO-->>NSO: Pipeline Production-Ready
    end

    rect rgb(236, 253, 245)
    Note over NSO,US: Execution Phase (per cycle)
    US-->>NSO: Raw Data Registered event
    NSO->>NSO: Profile & assess structure
    NSO->>NSO: Map codes 1-to-1 & coerce format; record unit/period metadata

    NSO->>NSO: Validate structural & semantic conformance

    alt Conformance Passed
        NSO->>NSO: Assign ID, store standardized data,<br/>register lineage & metadata
        NSO-->>NSO: Standardized Data Registered event
    else Conformance Failed
        NSO->>NSO: Re-map / route unmapped values to VS-03
    end
    end

    rect rgb(254, 243, 199)
    Note over PM: Management Phase
    PM->>PM: Monitor KPIs, assess mapping quality,<br/>produce compliance reports
    PM-->>NSO: Improvement Recommendations
    end
```

## Framework Mappings

This reference table maps each process group of this document to the international frameworks (GSBPM, GAMSO, CSDA) and the SAF capability model. It is intended for architects and auditors; the narrative sections above do not depend on it.

| Process group | GSBPM | GAMSO | CSDA | SAF Capabilities |
|---|---|---|---|---|
| **Design** | Phase 1 (Specify Needs), Phase 2 (Design: 2.1–2.5) | Production (design activities), Capability Management | Data Governance, Metadata Management, Reference & Master Data | 1.1.2 Design statistics product, 2.1.2 Metadata management, 2.1.4 Statistical register management |
| **Implementation** | Phase 3 (Build: 3.1–3.7) | Capability Management | Data Integration (setup), Data Governance (configuration) | 1.1.3 Build statistics product, 3.2.1 Application development, 3.2.2 Functional management |
| **Execution** | Phase 5 (Process: 5.1 Integrate, 5.2 Classify & code, 5.3 Review & validate) | Production (execution) | Data Integration (execution) | 2.1.2 Metadata management, 2.1.4 Statistical register management |
| **Management** | Overarching processes (Quality Management, Metadata Management) | Corporate Support (Quality Management, Data Management, Metadata Management), Capability Management (improvement) | Data Quality, Data Governance, Traceability | 2.1.3 Statistical quality management, 4.1.4 Improve management, 4.1.5 Accountability |

## Applying This to Your NSO

### Maturity Assessment Checklist

Use this checklist to assess your NSO's maturity across all four process types — not just execution.

**Design Maturity**

- [ ] Do we have a documented canonical target data model for standardized data?
- [ ] Do we have a formal classification mapping strategy (deterministic correspondence tables) with an explicit version policy?
- [ ] Do we have harmonized concept and variable definitions, and rules to record cross-source definition differences as metadata (flagged for VS-03)?
- [ ] Do we have explicit structural, classification, and semantic conformance rules documented before standardization begins?
- [ ] Do we have a defined identifier-removal/pseudonymization design for the State #1 → State #2 transition?

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
- [ ] Do we validate structural and semantic conformance before accepting standardized data?
- [ ] Do we register every standardized dataset with full mapping lineage to its raw source?

**Management Maturity**

- [ ] Do we track KPIs (mapping coverage, unmapped-value rate, conformance pass rate) across cycles?
- [ ] Do we assess mapping completeness and orphan-code rate?
- [ ] Do we govern classification version lifecycles and correspondence tables?
- [ ] Do we produce audit, privacy, and standards-compliance reports?
- [ ] Do we have a formal improvement process that feeds back into design (e.g., correspondence-table extension)?

### End-to-End Scenarios

Each scenario walks through **all four process types**, demonstrating how the governance pattern works in practice.

#### Scenario A: Labour Force Survey (Survey, Deterministic Mapping)

**Design Phase:** Data architects define the canonical LFS data model — person and household entities keyed to a pseudonymous personal identifier, with occupation, education, employment status, and region as core variables. Classification stewards adopt ISCED-2011 for education and NUTS-3 for region and build deterministic correspondence tables from the survey's source education and region codes to those standards; they also define the version policy. The design records that the survey's employment-status definition differs from the harmonized ILO definition — this difference is captured as metadata and flagged for VS-03, not reconciled here — and that free-text occupation strings are **not** coded in VS-02 but handed to VS-03 for ISCO-08 coding. The privacy design specifies that the direct personal identifier is replaced with a pseudonymous key at standardization.

**Implementation Phase:** Data engineers build the mapping & format-coercion component that restructures raw survey returns into the canonical model and casts types, and configure the ISCED and NUTS-3 correspondence-table lookups. The conformance pipeline is configured with structural, classification, semantic, and no-loss-of-content checks, and the pseudonymization component is implemented. The pipeline is tested on a 2,000-record synthetic sample; correspondence mappings are verified against the source code lists (100% of source codes resolve), and the routing of free-text occupation to VS-03 is confirmed.

**Execution Phase:** For cycle Q3-2026, a Raw Data Registered event arrives for 42,000 LFS returns. Profiling confirms the expected structure. The component coerces the format and maps source education codes 1-to-1 to ISCED-2011 and source region codes to NUTS-3; the 42,000 free-text occupation strings are flagged and passed to VS-03 for coding. The employment-status definition difference is recorded as metadata, the personal identifier is pseudonymized, and conformance validation passes — including the no-loss-of-content check (42,000 records, no value changed). The standardized dataset is registered with full lineage, and a Standardized Data Registered event notifies VS-03.0.

**Management Phase:** Mapping coverage for education and region is 99.9%, with 4 orphan source codes investigated and corrected in the correspondence table. The unmapped-value rate (free-text occupation routed to VS-03) is as expected. Conformance pass rate is 100% on first run. Improvement recommendations: extend the region correspondence table to cover two newly created NUTS-3 codes; confirm with VS-03 that occupation coding volumes are within capacity. Recommendations are fed back to design for the next cycle.

#### Scenario B: Tax Register to Business Statistics (Multi-Source Integration)

**Design Phase:** Data architects define the canonical business statistics model keyed to the statistical business register (SBR) identifier, with turnover, employment, and economic activity as core measures. Classification stewards adopt NACE Rev. 2 for activity and build a deterministic correspondence table from the tax authority's internal activity codes. The design requires that each turnover figure carry its currency, unit ("thousands of EUR"), and reference-period basis (the VAT register's fiscal year) **as metadata** — values are recorded as received and **not** converted; converting turnover to a common unit and aligning the fiscal year to the calendar year are explicitly VS-03 activities. Conformance rules require SBR-key referential integrity and that every value is preserved unchanged.

**Implementation Phase:** Data engineers build the mapping & format-coercion component: tax internal-code → NACE Rev. 2 via the maintained correspondence table (1-to-1), XML reformatting and type casting, and SBR-key linkage. The unit/currency/period bases are captured as metadata fields. The conformance pipeline checks SBR referential integrity and verifies that every turnover value is byte-for-byte unchanged and record counts match. The pipeline is tested on Q1-2026 historical data; one activity-code correspondence gap is found and the table updated.

**Execution Phase:** Q3-2026: a Raw Data Registered event arrives for 2,347,891 tax records. Profiling flags activity as the tax internal code and turnover in thousands of EUR on a fiscal-year basis. Standardization maps activity to NACE Rev. 2 (99.4% coverage; 0.6% with no correspondence flagged for VS-03), coerces the XML, links the SBR key, and records the turnover unit and fiscal-year basis as metadata — turnover values are left exactly as received. Fourteen records lack an SBR match (newly registered businesses, known register lag) and are flagged but retained. Conformance passes with every value unchanged. The standardized dataset `SD-BUS-2026Q3-001` is registered with lineage to `RD-TAX-2026Q3-001`, and VS-03.0 is notified that unit/period conversion remains to be done.

**Management Phase:** NACE mapping coverage is 99.4% (stable across quarters); the 0.6% unmapped activity codes are passed to VS-03. The 14 unmatched SBR keys match the known register-update lag. No-loss-of-content confirmed: turnover values and record counts identical before and after. SLA on processing time met. Improvement recommendation: extend the NACE correspondence table for the new business-activity codes, and schedule adoption planning for the upcoming NACE revision. Recommendations fed back to design.

#### Scenario C: Web-Scraped Price Data (Emerging Source Standardization)

**Design Phase:** Data architects define the canonical price record — product, retailer, price, currency, unit, reference day, and (where available) a source category code — keyed to a product-offer identifier. The design recognizes that web-scraped data is largely uncoded and heterogeneous, so VS-02's role is deliberately small: coerce the scraped JSON into the canonical record structure and record each item's currency, unit, and scrape timestamp **as metadata**, leaving prices exactly as received. Where a retailer supplies a category code that has a maintained correspondence to COICOP-2018, that code is mapped 1-to-1; products with only a free-text name (no source code) are **not** classified here. Coding products to COICOP, converting currencies to EUR, and normalizing units are all explicitly **VS-03** activities. Conformance rules require structural conformance and preservation of the count of distinct price observations.

**Implementation Phase:** Data engineers build the component that coerces the scraped JSON into the canonical structure and captures currency/unit/timestamp metadata, and configure the correspondence-table lookup for any retailer category codes that map to COICOP. The conformance pipeline checks structural conformance and observation-count preservation. The pipeline is tested on a sample; the structure coercion and metadata capture are verified, and the routing of unclassified products to VS-03 is confirmed.

**Execution Phase:** For 2026-03-15, a Raw Data Registered event arrives for 11,875 scraped price records. Profiling confirms structure. VS-02 coerces the records into the canonical structure, maps the subset of products that carry a correspondence-bearing retailer category code to COICOP-2018, and records each price's currency, unit, and timestamp as metadata — prices are unchanged. The majority of products (free-text only) are flagged for VS-03 classification. Conformance passes, with the distinct-observation count preserved (no value changed). The standardized daily price dataset is registered with lineage to the raw scrape, and VS-03.0 is notified that product classification and currency/unit conversion remain.

**Management Phase:** The weekly dashboard shows structural conformance at 99.6% and a high unmapped-value rate (most products lack a source code and are handed to VS-03) — expected for this source type and a useful signal that the bulk of the work for web data is downstream. Observation-count preservation is 100%. Improvement recommendations: where a retailer begins supplying category codes, add the corresponding correspondence table to raise VS-02 mapping coverage; otherwise no VS-02 change is warranted. Recommendations are fed back to the design team.

## VS-03.0 Data Editing and Enrichment

### Purpose and Scope

This document specifies the complete business layer for the **Editing, derivation, and non-response correction** business domain, corresponding to the *VS-03.0 Data Editing and Enrichment Value Stream*. It also covers 4 governance process types:

- **Design** — how the editing, imputation, and derivation pipeline is specified and planned (produces metadata)
- **Implementation** — how the pipeline is built, configured, and tested (produces the execution process)
- **Execution** — how data is operationally edited, imputed, derived, and versioned (produces statistical data)
- **Management** — how the domain is monitored, quality-assessed, and improved (produces quality reports)

::: {.callout-warning title="Out of Scope"}
Application and Technology layer specifications are out of scope for this document. Estimation, weighting, aggregation, and statistical modeling are out of scope — they belong to VS-04.0 Estimation, Analysis, and Statistical Modeling. VS-03 improves the quality of microdata; it does not produce estimates or aggregates.
:::





*A note on numbering:* each `VS-0x.y` below is both a value stream stage (*what value* is added) and a business process (*how* it is done); the numbering maps one-to-one. See the key-concepts box above.



### Position in the Statistical Value Chain

VS-03.0 is the third primary value stream — it receives Standardized Data from VS-02.0 and improves its quality and completeness so that it becomes trustworthy, analytically sound input for estimation and modeling. It is the "Edit & Enrich Information" orchestration stage where standardized data becomes high-quality statistical input.

```{mermaid}
%%| label: fig-1
%%| fig-cap: "Value Stream Context Map. VS-03.0 is highlighted as the editing-and-enrichment stage that turns standardized data into analytically-ready processed data."
%%| fig-width: 6


flowchart TD
    subgraph primary["Primary Value Streams"]
        direction LR
        VS01["VS-01.0
        Data Acquisition
        & Ingestion"]
        VS02["VS-02.0
        Data Standardization
        & Integration"]
        VS03["**VS-03.0**
        Data Editing
        & Enrichment"]:::highlight
        VS04["VS-04.0
        Estimation, Analysis
        & Modeling"]
        VS05["VS-05.0
        Statistical Product
        Composition"]
        VS06["VS-06.0
        Dissemination
        & Service Delivery"]
        VS01 --> VS02 --> VS03 --> VS04 --> VS05 --> VS06
    end

    subgraph supporting["Supporting Value Streams"]
        VS07["VS-07.0
        Governance &
        Compliance"]
        VS08["VS-08.0
        Innovation &
        Methodology"]
        VS09["VS-09.0
        Infrastructure &
        Platform Enablement"]
        VS10["VS-10.0
        Customer &
        Stakeholder Engagement"]
    end

    supporting -.->|"enables"| primary

    classDef highlight fill:#2563eb,color:#fff,stroke:#1d4ed8,stroke-width:3px
```

### Steady State Transition

VS-03.0 transitions data from **Steady State #2 (Standardized Data)** — structurally aligned and standard-coded data, with values unchanged — to **Steady State #3 (Processed Data)** — data whose content has been validated, corrected, completed, and enriched, integrated with other datasets where applicable, with new derived variables and fully documented lineage.

```{mermaid}
%%| label: fig-2
%%| fig-cap: "Steady State Transition from Standardized Data to Processed Data through the editing and enrichment service at the domain boundary."
%%| fig-width: 6
flowchart LR
    subgraph upstream["Upstream Domain (VS-02.0)"]
        SD["Standardized Data
        (State #2)"]
    end

    subgraph boundary["Editing & Enrichment Boundary"]
        QG["Editing & Enrichment Service
        (Error detection, Correction, Imputation,
        Derivation, Quality versioning)"]
    end

    subgraph internal["Processed Domain (VS-03.0)"]
        PD["Processed Data
        (State #3)"]
    end

    SD --> QG --> PD

    style internal fill:#2563eb,color:#fff,stroke:#1d4ed8,stroke-width:3px
    style upstream fill:#7d7d7d,color:#fff,stroke:#1d4ed8,stroke-width:1px
    style boundary fill:#FFF,stroke-dasharray:5,5

```

::: {.callout-tip title='Quality version criteria (Examples)*'}
- Logical errors, duplicates, outliers, and inconsistencies detected and resolved
- Invalid entries corrected per documented rules; every correction logged with the original value
- Missing and non-response values imputed using approved methods, with imputation flags
- Datasets integrated/linked with other sources where applicable
- New derived variables and indicators calculated and documented
- Inherited operations completed: interpretive coding, unit/currency conversion, reference-period alignment, value reconciliation
- A traceable quality version produced, with full edit lineage from each processed value back to its standardized source value
:::

::: {.callout-important title="The editing discipline — values change, but never silently"}
Unlike VS-02 (which never alters a value), VS-03 **deliberately changes values** to improve quality. The guarantee here is not no-loss-of-content but **full traceability**: every edit, imputation, and derivation is rule-based, documented with a reason, reversible, and recorded so the original value is preserved alongside the processed value. Each change is attributable (who/what rule/when), and a versioned, reproducible Processed Data artefact is produced. The invariant is *no undocumented or irreversible change.*
:::

::: {.callout-note title="Inherited hand-offs from VS-02.0"}
VS-02 deliberately left all value-changing work to this domain. VS-03 receives Standardized Data **plus** the metadata VS-02 attached — recorded unit/currency/reference-period bases, definition-difference records, and the list of unmapped/uncoded values — and performs, here, the operations VS-02 deferred:

- **Interpretive coding** of free-text values (e.g., free-text occupation to ISCO, the international occupation classification) — see §5.2
- **Unit and currency conversion** to a common basis — see §5.4
- **Reference-period alignment** (e.g., fiscal → calendar year) — see §5.4
- **Value reconciliation** across sources with differing definitions — see §5.2
- **Derivation** of new variables and indicators — see §5.4
:::


### The Four-Process Governance Pattern



```{mermaid}
%%| label: fig-3
%%| fig-cap: "The Four-Process Governance Pattern. Each process type produces a distinct artefact class. The cycle closes when Management findings feed back into Design improvements."
%%| fig-width: 6
flowchart LR
    D["**Design**
    _provides metadata_

    Editing & validation rules, imputation
    methodology, derivation specs, versioning policy"]
    I["**Implement**
    _provides the execution process_

    Configured editing/imputation engines,
    derivation pipelines, versioning store"]
    E["**Execute**
    _provides the statistical data_
    Edited & enriched datasets, edit
    lineage, imputation flags, quality versions"]
    M["**Manage**
    _provides quality reports_
    Edit/imputation dashboards, quality
    improvement scorecards, improvement recommendations"]

    D -->|"design artefacts
    guide building"| I
    I -->|"production-ready
    process"| E
    E -->|"data & process logs
    for assessment"| M
    M -->|"improvement
    feedback"| D

    style D fill:#7c3aed,color:#fff,stroke:#6d28d9
    style I fill:#2563eb,color:#fff,stroke:#1d4ed8
    style E fill:#059669,color:#fff,stroke:#047857
    style M fill:#d97706,color:#fff,stroke:#b45309
```




### Governing Principles

The following principles directly govern the VS-03.0 business domain:

| Principle | Statement | Application to VS-03.0 |
|---|---|---|
| **SAF-P01** | Actively participate in open source to maintain collective control over statistical processes | NSOs should contribute to open source communities for editing, imputation, and coding tooling (e.g., selective-editing engines, imputation libraries), ensuring collective control over critical methodological capabilities rather than vendor dependence. |
| **SAF-P07** | Implement loosely coupled processes and systems | The editing domain must be independent from upstream standardization and downstream estimation. Processed Data (State #3) serves as a decoupling interface — downstream consumers access edited, enriched microdata without knowledge of how it was corrected or imputed. |
| **SAF-P08** | Data is shared property | Processed data, once versioned, is available to all authorized consumers. Editing and enrichment should not be duplicated across statistical products when the same processed asset can serve multiple purposes. |
| **SAF-P09** | No data without metadata and classification | Every edit, imputation, and derived variable carries metadata: the rule applied, the original value, the imputation method and flag, the derivation formula, and a classification for derived variables. This is what makes the changes transparent and reproducible. |
| **SAF-P10** | Security By Design | Access controls, integrity verification, and a tamper-evident edit audit trail are embedded in the editing pipeline so that every change to a value remains attributable and traceable, not added as an afterthought. |
| **SAF-P11** | Privacy By Design | The domain works on pseudonymized microdata. Enrichment and integration with external datasets raise re-identification risk, so linkage is assessed for disclosure risk and minimization by design, not retrofitted. |

::: {.callout-note title="Cross-cutting principle application"}
Several principles cut across all four process types. SAF-P09 (no data without metadata and classification) is the backbone of the editing discipline: Design defines the rules and required edit metadata, Execute captures the original value, rule, and reason for every change, and Manage assesses edit quality and closes gaps. SAF-P10 (Security By Design) governs the tamper-evident edit audit trail across Execution (Sections 5.1–5.5). SAF-P11 (Privacy By Design) applies especially to integration/enrichment (Sections 3.4 and 5.4), where linkage can raise re-identification risk. SAF-P07 (loosely coupled) governs both the State #2 intake interface from VS-02.0 and the State #3 handover interface to VS-04.0.
:::

### Capability Foundations

VS-03.0 draws on the following SAF capabilities:

| Capability Group | Capabilities | Role in VS-03.0 |
|---|---|---|
| **1.1 Statistical design and build** | 1.1.2 Design statistics product, 1.1.3 Build statistics product | Design the editing/imputation methodology and derivation specifications, and build the editing pipeline |
| **2.1 Data management** | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management, 2.1.4 Statistical register management | Manage data, edit metadata, and quality versions; assess quality improvement; integrate with statistical registers |
| **3.2 Computerization and automation** | 3.2.1 Application development, 3.2.2 Functional management | Build and maintain editing, imputation, derivation, and integration engines |
| **3.3 Security and Privacy** | 3.3.1 Privacy management, 3.3.2 Security planning | Manage disclosure risk in enrichment/linkage and secure the edit audit trail |
| **4.1 Governance** | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improve management, 4.1.5 Accountability | Govern the domain, steward editing methodology, plan improvements, report on auditability and compliance |

### Metadata Perspective

It is considered that metadata is an essential product of the Design phase and a critical concern of every other phase. In this domain, metadata is what keeps value changes transparent: every edit, imputation, and derivation must be self-describing. The table below consolidates the metadata produced across all four process types, covering both data metadata (about the datasets) and process metadata or paradata (about how the process runs).

| Process Type | Data Metadata Produced | Process Metadata (Paradata) Produced |
|---|---|---|
| **Design** | Editing/validation rule sets, imputation methodology, derivation formulae, integration/linkage rules, quality-version policy | Design decisions log, methodology version, review and approval records |
| **Implement** | Engine configurations, rule parameters, imputation model parameters, derivation definitions, versioning templates | Build log, test results, edit-impact test outcomes, deployment approvals |
| **Execute** | Per-record edit lineage (original value, rule, reason), imputation flags and methods, derived-variable formulae and inputs, quality-version identifiers | Operator identity, timing, volumes, edit/imputation rates, rule/model version, manual-override records |
| **Manage** | Quality-improvement scores vs. baseline, edit/imputation rate reports, lineage assessments, trend analyses | Edit dashboards, quality trends, improvement decisions, audit findings |


## Business Roles and Actors



| Role                        | Process Orientation | Description                                                                                       |
|-----------------------------|---------------------|---------------------------------------------------------------------------------------------------|
| **Upstream Data Provider (VS-02.0)** | External (internal NSO) | Supplies Standardized Data (State #2) and its mapping/metadata to the editing domain |
| **Methodology Authority**   | External            | Sets the editing, imputation, and derivation methods the NSO conforms to (e.g., methodology unit, Eurostat guidance) |
| **Editing Methodologist**   | Design              | Designs error-detection and editing rules, selective-editing strategy, and quality criteria        |
| **Imputation Specialist**   | Design              | Designs imputation methodology, models, donor strategies, and imputation flags                     |
| **Derivation Designer**     | Design              | Specifies derived variables and indicators, formulae, and required inputs                          |
| **Data Engineer**           | Implementation      | Builds and configures editing, imputation, derivation, and integration engines and the pipeline    |
| **System Configurator**     | Implementation      | Configures editing services, reference/donor-data connections, and access controls                |
| **Test Manager**            | Implementation      | Plans and executes testing of the editing pipeline (technical, edit-impact, reproducibility)       |
| **Process Owner**           | Management          | Accountable for the end-to-end performance of the editing and enrichment domain                    |
| **Compliance Officer**      | Management          | Ensures edit auditability and disclosure-risk compliance, produces audit reports                   |
| **Quality Manager**         | Management          | Monitors quality-improvement KPIs, produces quality reports, and drives continuous improvement     |
| **Subject-Matter Analyst**  | Execution           | Reviews flagged records, adjudicates edits, and signs off domain-specific corrections              |
| **Coding Specialist**       | Execution           | Performs interpretive coding of free-text values to standard classifications (handed over from VS-02) |
| **Data Quality Analyst**    | Execution           | Runs error detection, evaluates quality improvement, and logs edit lineage and exceptions          |
| **Data Steward**            | Execution           | Registers processed datasets and quality versions, manages metadata entries, and applies access controls |



## Design Processes — "provides metadata"

*Framework alignment: GSBPM Phases 1–2 — see [Framework Mappings](#framework-mappings).*

The design phase produces the **metadata artefacts** that govern all subsequent phases — the editing and validation rules, imputation methodology, derivation specifications, and the versioning policy. Without well-designed rules and methods, editing becomes ad-hoc and untraceable, and management has no baseline to measure quality improvement against.

### Design Error-Detection and Validation Rules

The starting point of editing is defining what counts as an error. This sub-process establishes the validation and error-detection rules: logical/consistency checks (cross-field, intra-record, and against reference data), range and outlier-detection rules, duplicate-detection rules, and completeness checks. A **selective-editing** strategy is designed so that effort concentrates on errors that materially affect results — score functions and thresholds determine which records are auto-corrected, which are flagged for manual review, and which are left. The team designs the error taxonomy and the disposition options (auto-correct, flag for review, accept), aligned with GSBPM 2.5 (Design processing and analysis).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define logical/consistency, range, and outlier detection rules | Validation Rule Set | GSBPM 2.5 |
| Define duplicate- and completeness-detection rules | Validation Rule Set | GSBPM 2.5 |
| Design selective-editing score functions and review thresholds | Selective-Editing Strategy | GSBPM 2.5 |
| Define error taxonomy and disposition options (auto-correct / review / accept) | Error Taxonomy & Disposition Policy | GSBPM 2.5 |

::: {.callout-tip title="**NSO Example — Structural Business Statistics:**"}
The SBS team designs consistency rules (turnover ≥ 0, employees ≥ 0, turnover-per-employee within a plausible band by NACE class), outlier rules using a Hidiroglou–Berthelot test on year-on-year ratios, and a selective-editing score that flags only units whose potential error would move a published aggregate by more than a set threshold. Everything else is accepted without manual touch.
:::


### Design Imputation Methodology

This sub-process designs how missing and non-response values are completed. The team selects imputation methods per variable and missingness type — deterministic/rule-based imputation, donor methods (hot-deck, nearest-neighbor), model-based methods (regression, ratio), and the use of external/administrative sources — and defines donor pools, matching variables, and acceptance constraints (e.g., edit rules the imputed value must still satisfy). Crucially, the design mandates an **imputation flag** on every imputed value so that imputed and observed values are always distinguishable downstream, aligned with GSBPM 2.5.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Select imputation methods per variable and missingness type | Imputation Methodology Document | GSBPM 2.5 |
| Define donor pools, matching variables, and acceptance constraints | Donor & Matching Specification | GSBPM 2.5 |
| Specify use of external/administrative sources for imputation | External-Source Imputation Rules | GSBPM 2.5 |
| Mandate imputation flags and method codes on every imputed value | Imputation Flagging Standard | SAF-P09 |

::: {.callout-tip title="**NSO Example — Labour Force Survey:**"}
For item non-response on income, the LFS design specifies regression imputation using age, education (ISCED), occupation (ISCO), and region as predictors, with a constraint that imputed income remains within the valid range for the respondent's earnings bracket. Every imputed value receives a flag and a method code so analysts can exclude or down-weight imputed values if needed.
:::

### Design Derivation and Coding Specifications

This sub-process specifies the new variables and indicators to be derived, and the interpretive coding handed over from VS-02. For derivation, each derived variable is defined by a formula, its input variables, units, and the classification it belongs to (per SAF-P09). For interpretive coding, the design specifies the coding scheme (e.g., ISCO for occupation free text, COICOP for product names), the coding approach (manual, computer-assisted, or machine-learning-assisted with confidence thresholds), and the review workflow for low-confidence cases — the work VS-02 deferred because it requires judgement. The team also designs how unit/currency/reference-period conversions are computed from the bases VS-02 recorded as metadata, aligned with GSBPM 2.5.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Specify derived variables and indicators: formulae, inputs, units, classification | Derived-Variable Catalog | GSBPM 2.5 |
| Design interpretive coding approach and review workflow (free-text → standard codes) | Coding Methodology | GSBPM 2.5 |
| Design unit/currency/reference-period conversion rules from VS-02 metadata | Conversion Specification | GSBPM 2.5 |
| Define metadata and classification for every derived variable | Derived-Variable Metadata Standard | SAF-P09 |

### Design Integration and Linkage Rules

Where Processed Data is to be integrated with other datasets, this sub-process designs the linkage. It specifies the linkage keys (e.g., the statistical register identifier aligned in VS-02), deterministic and probabilistic matching rules, conflict-resolution rules where linked sources disagree on a value, and the **value-reconciliation** policy for the definition differences VS-02 recorded as metadata. Because linkage can increase disclosure risk on pseudonymized microdata, a privacy/disclosure-risk assessment is designed per SAF-P11, aligned with GSBPM 5.1 design.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define linkage keys and deterministic/probabilistic matching rules | Linkage Rule Set | GSBPM 2.5 |
| Design conflict-resolution and value-reconciliation rules across sources | Reconciliation Policy | GSBPM 2.5 |
| Design disclosure-risk assessment for integration/enrichment | Disclosure-Risk Assessment Design | SAF-P11 |
| Define lineage requirements for linked/reconciled values | Linkage Lineage Specification | CSDA Traceability |

### Design Quality Evaluation, Versioning, and Audit Framework

The final design sub-process ensures that quality is measured and that every change is traceable. It defines the quality-evaluation criteria (improvement of completeness and accuracy against the State #2 baseline), the **edit audit-trail** requirements (original value, rule applied, reason, actor, timestamp for every change), the quality-versioning policy (how versions are identified, what triggers a new version, immutability and retention), and the role-based access controls for processed microdata in line with SAF-P10. Reproducibility is designed in: a quality version must be regenerable from the standardized input plus the recorded rules.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define quality-evaluation criteria vs. the State #2 baseline | Quality Criteria Document | GAMSO QM |
| Define edit audit-trail requirements (original value, rule, reason, actor, time) | Edit Audit-Trail Specification | SAF-P10 |
| Define quality-versioning policy: identity, triggers, immutability, retention | Versioning Policy | CSDA Traceability |
| Design role-based access control and reproducibility for processed microdata | Access Control & Reproducibility Design | SAF-P10 |

```{mermaid}
%%| label: fig-4
%%| fig-cap: "Design Process Decomposition. The standardized data model, methodology set, and framework standards flow into five design sub-processes, producing metadata artefacts that govern Implementation, Execution, and Management."
%%| fig-width: 6
flowchart TB
    subgraph inputs["Inputs"]
        SM["Standardized Data Model<br/><small>(State #2 schema + metadata)</small>"]
        FW["Framework Standards<br/><small>GSBPM · GAMSO · CSDA</small>"]
        METH["Methodology Set<br/><small>Editing · Imputation · Derivation</small>"]
        LAW["Privacy & Disclosure"]
    end

    subgraph design["Design Sub-Processes"]
        D1["3.1 Error-Detection<br/>& Validation Rules"]
        D2["3.2 Imputation<br/>Methodology"]
        D3["3.3 Derivation &<br/>Coding Specs"]
        D4["3.4 Integration &<br/>Linkage Rules"]
        D5["3.5 Quality, Versioning<br/>& Audit Framework"]
    end

    subgraph outputs["Metadata Artefacts"]
        O1["Validation Rule Set"]
        O2["Imputation Methodology"]
        O3["Derivation & Coding Specs"]
        O4["Linkage & Reconciliation Rules"]
        O5["Versioning & Audit Policy"]
    end

    SM --> D1
    METH -.->|inform| design
    FW -.->|inform| design
    LAW --> D4

    D1 --> D2 --> D3 --> D4 --> D5

    D1 --> O1
    D2 --> O2
    D3 --> O3
    D4 --> O4
    D5 --> O5

    outputs -->|govern| NEXT["Implementation (§4) · Execution (§5)<br/>measured by Management (§6)"]

    style design fill:#f5f3ff,stroke:#7c3aed
    style outputs fill:#ede9fe,stroke:#7c3aed
```

## Implementation Processes — "provides the execution process"

*Framework alignment: GSBPM Phase 3 (Build) — see [Framework Mappings](#framework-mappings).*

The implementation phase takes the metadata artefacts from Design and **builds, configures, and tests** the production-ready editing and enrichment pipeline. Nothing runs operationally until this phase is complete.

### Build Error-Detection and Editing Engines

This sub-process turns the validation and editing rule designs into operational tools. Error-detection components are built to run the designed consistency, range, outlier, duplicate, and completeness checks and to compute the selective-editing scores. The editing engine is built or configured to apply auto-corrections per the designed rules and to route flagged records to the review workflow, capturing for every change the original value, the rule applied, and a reason code. All editing logic is version-controlled in line with SAF-P10 so that any edit is reproducible and attributable, following GSBPM 3.1–3.2.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Build error-detection components (consistency, range, outlier, duplicate, completeness) | Production-ready detection module | GSBPM 3.2 |
| Build/configure the editing engine (auto-correction + review routing) | Configured editing engine | GSBPM 3.2 |
| Configure edit-lineage capture (original value, rule, reason, actor) for every change | Edit audit-trail capture | SAF-P10 |
| Version-control all editing logic | Versioned editing repository | SAF-P10 |

::: {.callout-tip title="**NSO Example — Price Statistics:**"}
The implementation team builds an outlier detector for daily price changes, an editing engine that applies designed corrections (e.g., decimal-point fixes), and a review queue for flagged price jumps. Every correction stores the original scraped price, the rule, and the analyst's adjudication, so the edit can be audited and reversed.
:::

### Configure Imputation and Coding Services

The designed imputation methodology and coding methodology are translated into automated services. Imputation services are configured for each method (deterministic, donor, model-based, external-source), with donor pools and matching variables loaded and acceptance constraints enforced, and every imputed value flagged with its method code, following GSBPM 3.2. The interpretive coding service handed over from VS-02 is configured — computer-assisted and/or ML-assisted coding for free-text values with the designed confidence thresholds, and a manual review workflow for low-confidence cases. Unit/currency/reference-period conversion routines are configured to compute values from the bases VS-02 recorded.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Configure imputation services per method, with donor pools and constraints | Configured imputation services | GSBPM 3.2 |
| Enforce imputation flagging and method codes | Flagged imputation outputs | SAF-P09 |
| Configure interpretive coding service (free-text → standard codes) with review workflow | Coding service + review queue | GSBPM 3.2 |
| Configure unit/currency/reference-period conversion routines | Conversion service | GSBPM 3.4 |

### Build Derivation, Integration, and Versioning Pipelines

This sub-process implements derivation, dataset integration, and quality versioning. Derived-variable calculators are built from the designed formulae, producing each derived variable with its metadata and classification. The integration/linkage component is configured with the designed keys and matching rules, applying the conflict-resolution and value-reconciliation policy and capturing linkage lineage. The quality-versioning store is built so that each accepted Processed Data version is immutable, identified, reproducible from inputs plus rules, and accompanied by its full edit lineage. Event notifications are configured so that downstream consumers (VS-04.0) are alerted when a processed quality version is registered.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Build derived-variable calculators from designed formulae | Derivation pipeline | GSBPM 3.2 |
| Configure integration/linkage with conflict-resolution and reconciliation | Integration component | GSBPM 3.2 |
| Build the quality-versioning store (immutable, identified, reproducible) | Versioning store | CSDA Traceability |
| Configure "Processed Data Registered" event for downstream consumers | Event publication | GSBPM 3.2 |

### Test and Validate the Pipeline

Before the pipeline goes into production, it must be rigorously verified. Technical testing covers all individual components — detectors, editing engine, imputation and coding services, derivation calculators, integration component, and versioning store (GSBPM 3.5). Integration testing validates the end-to-end flow from standardized intake through editing, imputation, derivation, integration, to versioned registration. An **edit-impact test** confirms that edits and imputations move quality indicators in the intended direction without over-editing, and a **reproducibility test** confirms a quality version can be regenerated identically from the standardized input plus the recorded rules. Imputation is evaluated against a holdout/known-value sample. The phase concludes with finalization of the production system and documentation of operational procedures (GSBPM 3.6–3.7).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Technical testing of all individual components | Unit test reports | GSBPM 3.5 |
| Integration testing: end-to-end flow from standardized intake to versioned registration | Integration test report | GSBPM 3.5 |
| Edit-impact test (intended quality change, no over-editing) | Edit-impact report | GSBPM 3.6 |
| Reproducibility test (regenerate a version from inputs + rules) | Reproducibility report | GSBPM 3.6 |
| Evaluate imputation against a holdout/known-value sample | Imputation evaluation report | GSBPM 3.6 |
| Finalize production system and document operational procedures | Operational Procedures Manual, Production-Ready Pipeline | GSBPM 3.7 |

```{mermaid}
%%| label: fig-5
%%| fig-cap: "Implementation Pipeline from design artefacts through build/configure/test to production-ready system."
%%| fig-width: 6
flowchart LR
    subgraph design_artefacts["Design Artefacts (from Section 3)"]
        DA1["Validation\nRule Set"]
        DA2["Imputation\nMethodology"]
        DA3["Derivation &\nCoding Specs"]
        DA4["Linkage &\nReconciliation Rules"]
        DA5["Versioning &\nAudit Policy"]
    end

    subgraph build["Build & Configure"]
        B1["4.1 Build Detection\n& Editing Engines"]
        B2["4.2 Configure Imputation\n& Coding Services"]
        B3["4.3 Build Derivation,\nIntegration & Versioning"]
    end

    subgraph test["Test & Validate"]
        T1["4.4 Technical\nTesting"]
        T2["4.4 Edit-Impact &\nReproducibility"]
        T3["4.4 Imputation\nEvaluation"]
    end

    subgraph output["Production-Ready"]
        PR["Operational\nEditing\nPipeline"]
        OP["Operational\nProcedures"]
    end

    DA1 --> B1
    DA2 & DA3 --> B2
    DA3 & DA4 & DA5 --> B3

    B1 & B2 & B3 --> T1 --> T2 --> T3
    T3 --> PR & OP

    PR -->|"ready for"| EXEC["Execution\n(Section 5)"]

    style build fill:#eff6ff,stroke:#2563eb
    style test fill:#dbeafe,stroke:#2563eb
```

## Execution Processes — "provides the statistical data"

*Framework alignment: the later GSBPM phases for this domain — see [Framework Mappings](#framework-mappings).*

The execution phase runs the **designed and implemented pipeline** operationally for each production cycle. This corresponds to the five VS-03 value stream stages. In a mature steady state, much of the work has been pre-designed (Section 3) and pre-built (Section 4) — execution focuses on running the cycle, applying edits/imputations/derivations, and capturing the full edit lineage so that every value change is documented and reversible.

### Conduct Error Detection and Quality Diagnostics

**Value created:** *A clear, prioritized picture of where the data is wrong, incomplete, or inconsistent.*

When a "Standardized Data Registered" event is received from VS-02.0, the editing domain begins by running the designed detection rules on the incoming dataset. Per-cycle execution applies the consistency, range, outlier, duplicate, and completeness checks, computes the selective-editing scores, and produces a diagnostic report: the location and type of each suspected error, its severity, and its disposition (auto-correct, flag for review, or accept). This corresponds to GSBPM 5.3 (Review and validate). No values are changed yet — this sub-process diagnoses; the correction happens in 5.2.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Run consistency, range, outlier, duplicate, and completeness checks | Error Diagnostic Report | GSBPM 5.3 |
| Compute selective-editing scores and prioritize errors | Prioritized error list | GSBPM 5.3 |
| Assign disposition (auto-correct / flag for review / accept) | Disposition list | GSBPM 5.3 |
| Log all detected issues to the edit audit trail | Audit trail entries | SAF-P10 |

::: {.callout-tip title="**NSO Example — Structural Business Statistics:**"}
The SBS file (Standardized Data registered by VS-02.0) is diagnosed: 312 units fail the turnover-per-employee plausibility band, 47 are duplicates, 1,204 have missing employee counts. Selective-editing scores prioritize 89 units whose potential error would materially affect a published aggregate; the remaining low-impact flags are scheduled for automatic treatment.
:::

### Perform Data Editing and Correction

**Value created:** *Errors corrected and inconsistencies resolved, with every change documented and reversible.*

This sub-process applies corrections to the detected errors, aligned with GSBPM 5.4 (Edit and impute). Auto-correction rules are applied to the records the design earmarked for automatic treatment; flagged records are routed to subject-matter analysts who adjudicate and correct them. For every change, the editing engine records the original value, the rule or analyst decision applied, a reason code, the actor, and a timestamp — so the edit is fully attributable and reversible. This sub-process also performs the **interpretive coding** handed over from VS-02 (coding free-text values such as occupation to ISCO, with low-confidence cases reviewed) and applies the designed **value-reconciliation** rules where integrated sources disagree on a value. No edit may leave a record violating the validation rules.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Apply auto-corrections per designed rules | Corrected records | GSBPM 5.4 |
| Route flagged records to subject-matter review and adjudication | Adjudicated corrections | GSBPM 5.4 |
| Perform interpretive coding of free-text values (e.g., occupation → ISCO) | Coded values + confidence/review records | GSBPM 5.2 |
| Apply value-reconciliation rules across integrated sources | Reconciled values | GSBPM 5.4 |
| Record original value, rule, reason, actor, and time for every change | Edit lineage records | SAF-P10 |

```{mermaid}
%%| label: fig-6
%%| fig-cap: "Editing and Correction Architecture. Auto-correctable, review-flagged, and free-text values are treated through automatic correction, manual adjudication, and interpretive coding respectively; every change writes original value, rule, and reason to the edit audit trail."
%%| fig-width: 6
flowchart LR
    subgraph inputs["Detected Issues (from 5.1)"]
        direction TB
        AC["Auto-correctable\n(low impact)"]
        RV["Flagged for\nreview (high impact)"]
        FT["Free-text values\n(from VS-02 handover)"]
    end

    subgraph editing["Editing & Correction"]
        AE["Auto-correction\n(designed rules)"]
        MR["Manual\nadjudication"]
        IC["Interpretive\ncoding"]
    end

    subgraph output["Corrected Records"]
        OUT["Edited values\n(+ edit lineage)"]
    end

    AC --> AE --> OUT
    RV --> MR --> OUT
    FT --> IC --> OUT

    OUT -.->|"every change logs\noriginal + rule + reason"| AUDIT["Edit Audit Trail"]

    style inputs fill:#ecfdf5,stroke:#059669
    style editing fill:#f0fdf4,stroke:#059669
    style AUDIT fill:#fff,stroke:#888,stroke-dasharray: 5 5
```


::: {.callout-tip title='**NSO Example — Labour Force Survey Coding:**'}
The 42,000 free-text occupation strings handed over from VS-02 are coded to ISCO-08: 88% are auto-coded at or above the 0.85 confidence threshold, 5,040 go to computer-assisted coding, and 1,200 ambiguous cases to expert manual coding. Each coded value records the source text, the assigned code, the method, and the confidence — fully auditable as an editing decision.
:::


### Impute Missing or Non-Response Data

**Value created:** *Complete datasets where gaps are filled with the best available estimate, clearly flagged as imputed.*

This sub-process fills missing and non-response values using the designed imputation methods, aligned with GSBPM 5.4. The appropriate method is applied per variable and missingness pattern — deterministic, donor (hot-deck/nearest-neighbor), model-based, or external-source — subject to the acceptance constraints so that imputed values still satisfy the edit rules. Every imputed value receives an **imputation flag** and a method code so that imputed and observed values are always distinguishable downstream, and the imputation inputs are recorded in the lineage. Imputed values never overwrite observed values; they fill only genuine gaps.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Select and apply the designed imputation method per variable/missingness pattern | Imputed values | GSBPM 5.4 |
| Enforce acceptance constraints (imputed values satisfy edit rules) | Constraint-checked imputations | GSBPM 5.4 |
| Flag every imputed value with method code and record inputs | Imputation flags & lineage | SAF-P09 |
| Log imputation actions to the edit audit trail | Audit trail entries | SAF-P10 |

::: {.callout-tip title="**NSO Example — Labour Force Survey:**"}
Item non-response on income (about 9% of records) is imputed by the designed regression model using age, ISCED, ISCO, and region; each imputed income carries an `imputed=true` flag and method code `REG-01`, and the predictor values used are recorded so the imputation can be reproduced or revised.
:::

### Derive Additional Variables and Indicators

**Value created:** *Enriched datasets carrying the analytical variables downstream production needs.*

This sub-process calculates the derived variables and indicators specified in design, aligned with GSBPM 5.5 (Derive new variables and units). Each derived variable is computed from its documented formula and inputs, given its metadata and classification, and recorded with lineage to the inputs it was derived from. This sub-process also computes the **unit/currency/reference-period conversions** from the bases VS-02 recorded as metadata — for example converting turnover from thousands to units, or aligning a fiscal-year figure to the calendar year — each conversion documented with its rule and rate so the original value remains recoverable. Where datasets are to be combined, the integration/linkage component links records on the designed keys and the lineage records the linkage.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Calculate derived variables and indicators from designed formulae | Derived variables (+ metadata) | GSBPM 5.5 |
| Compute unit/currency/reference-period conversions from VS-02 bases | Converted values (+ conversion lineage) | GSBPM 5.5 |
| Integrate/link datasets on designed keys where applicable | Integrated dataset (+ linkage lineage) | GSBPM 5.1 |
| Record derivation/conversion formulae and inputs as lineage | Derivation lineage | SAF-P09 |

::: {.callout-tip title="**NSO Example — Tax Register to Business Statistics:**"}
Turnover, recorded by VS-02 as "thousands of EUR" on a fiscal-year basis, is converted here to units on a calendar-year basis using the designed conversion and apportionment rules; the conversion factor and the original value are stored in lineage. Turnover-per-employee is then derived as a new indicator with its formula and inputs recorded.
:::

### Perform Quality Evaluation and Versioning

**Value created:** *A trustworthy, traceable Processed Data version with measured quality improvement.*

The final execution sub-process evaluates the result and produces the official quality version, aligned with GSBPM 5.8 (Finalise data files). Quality is evaluated against the State #2 baseline — improvement in completeness and accuracy, edit and imputation rates, and the number of derived variables added — and the edit lineage is verified complete (every change attributable and reversible). A persistent, immutable quality version of the Processed Data is created with a unique identifier, registered in the catalog per SAF-P09 with its full lineage, imputation flags, derived-variable metadata, and quality assessment, and access permissions are applied per SAF-P10. The sub-process concludes by publishing a "Processed Data Registered" event, notifying downstream VS-04.0 that new processed data is available for estimation and analysis.

**Output:** **Processed Data (Steady State #3)** — the official handover artefact to the rest of the statistical value chain.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Evaluate quality improvement vs. the State #2 baseline | Quality Evaluation Report | GSBPM 5.8 |
| Verify edit lineage is complete and reversible | Lineage completeness check | SAF-P10 |
| Create an immutable, identified quality version of Processed Data | Versioned Processed Data | CSDA Traceability |
| Register metadata: edit lineage, imputation flags, derived-variable metadata, quality assessment | Catalog registration | SAF-P09 |
| Publish "Processed Data Registered" event to notify VS-04.0 | Event notification | SAF-P07 |

```{mermaid}
%%| label: fig-7
%%| fig-cap: "Processed Data Artefact Structure. Reading guide: each box is a type of record with its fields; a connecting line means the records are linked. Each processed quality version is linked to its edit lineage, imputation records, derivation records, and quality assessment, all traceable to the standardized source values."
%%| fig-width: 6
erDiagram
    PROCESSED_DATA_ARTEFACT {
        string dataset_id PK "Unique persistent URI/UUID"
        string quality_version "Immutable version identifier"
        date reference_period "Reference period"
        datetime registration_timestamp "When registered in catalog"
        string standardized_source_id "Standardized Data (State #2) source ID"
    }
    EDIT_LINEAGE {
        string variable "Edited variable"
        string original_value "Value as received (State #2)"
        string edited_value "Value after edit"
        string rule_or_decision "Rule applied or analyst decision"
        string reason_code "Why the change was made"
        string actor "Who/what made the change"
    }
    IMPUTATION_RECORD {
        string variable "Imputed variable"
        boolean imputed_flag "True where value was imputed"
        string method_code "Imputation method applied"
        string inputs_ref "Predictors/donors used"
    }
    DERIVATION_RECORD {
        string derived_variable "Derived variable/indicator"
        string formula "Derivation/conversion formula"
        string inputs_ref "Source variables used"
        string classification "Classification of derived variable"
    }
    QUALITY_ASSESSMENT {
        float completeness_improvement "vs State #2 baseline"
        float edit_rate "Percentage of values edited"
        float imputation_rate "Percentage of values imputed"
        boolean lineage_complete "Edit lineage verified complete"
    }

    PROCESSED_DATA_ARTEFACT ||--|{ EDIT_LINEAGE : "documents edits via"
    PROCESSED_DATA_ARTEFACT ||--|{ IMPUTATION_RECORD : "flags imputations via"
    PROCESSED_DATA_ARTEFACT ||--|{ DERIVATION_RECORD : "documents derivations via"
    PROCESSED_DATA_ARTEFACT ||--|| QUALITY_ASSESSMENT : "has quality record"
```

## Management Processes — "provides quality reports"

*Framework alignment: GSBPM overarching Quality/Metadata Management — see [Framework Mappings](#framework-mappings).*

The management phase runs **alongside and after** execution. It monitors the editing domain's performance, assesses the quality improvement achieved, ensures every change is auditable, and feeds improvement recommendations back into the design phase — closing the governance cycle.

### Monitor Process Performance

Operational performance of the editing domain must be tracked systematically across production cycles. The process owner and quality manager collect and aggregate key performance indicators, monitor throughput against processing windows, and track paradata — who edited what, when, with which rule or model version, how many manual interventions occurred. This information feeds process performance dashboards that give the process owner a real-time view of domain health, aligned with the GAMSO Quality Management capability.

**Key Performance Indicators (KPIs):**

| KPI | Description | Measurement |
|---|---|---|
| Edit rate | Percentage of values changed by editing | Per variable, per cycle |
| Imputation rate | Percentage of values imputed | Per variable, per cycle |
| Manual-review rate | Percentage of records routed to manual adjudication | Per source, per cycle |
| Over-editing indicator | Share of edits with negligible impact on results | Per cycle |
| Coding completion rate | Percentage of free-text values successfully coded | Per classification, per cycle |
| Processing time | Duration from standardized intake to versioned registration | Per dataset, per cycle |

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Collect and aggregate KPIs per production cycle | Process Performance Dashboard | GAMSO QM |
| Monitor throughput against processing windows | Throughput Report | GAMSO QM |
| Track paradata: operator, timing, rule/model versions, interventions | Paradata Records | GAMSO QM |
| Generate process performance dashboards | Dashboard for Process Owner | GAMSO QM |

### Assess Data Quality

Beyond process performance, the quality improvement achieved must be evaluated against the criteria established in design. Each processed dataset is assessed across multiple quality dimensions: accuracy improvement (error rates before vs. after editing), completeness improvement (missingness before vs. after imputation), imputation quality (against holdout or known values), consistency (no residual rule violations), and coherence of derived variables. Results are compared against the designed quality criteria from Section 3.5. Quality indicators are produced per dataset, per source, and per cycle, and trends are tracked to detect over-editing, deteriorating sources, or imputation models that need recalibration. This aligns with the CSDA Data Quality capability and SAF Capability 2.1.3.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Evaluate accuracy and completeness improvement vs. baseline | Quality Improvement Report (per cycle) | SAF 2.1.3 |
| Assess imputation quality against holdout/known values | Imputation Quality Report | CSDA Data Quality |
| Check for residual rule violations and over-editing | Consistency & Over-Editing Report | SAF 2.1.3 |
| Identify quality trends across sources, variables, and cycles | Quality Trend Analysis | SAF 2.1.3 |

### Manage Methodology and Version Lifecycle

The editing methodology and the quality versions it produces must remain current, complete, and well-governed. This sub-process governs the lifecycle of editing rules, imputation models, and derivation specifications — versioning them, managing transitions, and retiring obsolete rules. It verifies metadata completeness — that every processed dataset carries full edit lineage, imputation flags, and derived-variable metadata as an SAF-P09 compliance check — and governs the quality-version store: retention, immutability, and reconciliation that catalog entries match stored versions. Metadata lineage from standardized through editing to processed state is tracked. As the CSDA emphasizes, complete, well-managed lineage is what makes edited data trustworthy and reusable.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Govern editing-rule, imputation-model, and derivation lifecycle and versions | Methodology Version Register | SAF-P09 |
| Verify metadata completeness (edit lineage, imputation flags, derived metadata) | Metadata Quality Report | SAF-P09 |
| Govern the quality-version store: retention, immutability, reconciliation | Version Store Audit | CSDA Traceability |
| Track metadata lineage from standardized to processed state | Metadata Lineage Audit | CSDA Traceability |

### Audit and Compliance Reporting

This sub-process produces the evidence that the editing domain operates within methodological, legal, and organizational requirements. Edit-audit reports demonstrate that every value change is attributable and reversible — original value, rule, reason, actor, and time recorded — supporting reproducibility and methodological transparency. Privacy/disclosure-risk reporting covers integration and enrichment, confirming that linkage on pseudonymized microdata stays within the assessed re-identification risk per SAF-P11. Methodology compliance reporting confirms that approved editing and imputation methods were applied, and security compliance reporting verifies that designed access controls and the tamper-evident audit trail have been applied. These reports satisfy the SAF Capability 4.1.5 (Accountability) obligation and feed into VS-07.0 Governance and Compliance.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Produce edit-audit reports: every change attributable and reversible | Edit Audit Summary | SAF 4.1.5 |
| Report on disclosure-risk compliance for integration/enrichment | Disclosure-Risk Report | SAF-P11 |
| Report on methodology compliance (approved editing/imputation methods) | Methodology Compliance Report | SAF 4.1.5 |
| Report on security compliance: access controls, audit-trail integrity | Compliance Report (per cycle) | SAF-P10 |

### Continuous Improvement

The final management sub-process closes the governance loop by analyzing performance and quality data to identify and drive improvements. Quality trends across production cycles are examined: are error rates falling, is over-editing decreasing, is imputation quality improving, are coding completion rates rising? Improvement opportunities are identified — refining edit rules that generate false positives, recalibrating imputation models, automating manual edits that recur, improving the coding service for free text, and tuning selective-editing thresholds to reduce over-editing. These improvement recommendations are fed back to the design processes (Section 3), prioritized based on impact and feasibility, and tracked through subsequent design-implement-execute cycles. This is the SAF Capability 4.1.4 (Improve management) in action, and it connects to the GAMSO concept of transferring mature capabilities from innovation into production.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Analyze quality trends across production cycles | Improvement Recommendations Report | SAF 4.1.4 |
| Identify improvement opportunities: rule refinement, model recalibration, threshold tuning | Updated Design Inputs | SAF 4.1.4 |
| Feed recommendations back to design processes (Section 3) | Design feedback (closing the governance loop) | SAF 4.1.4 |
| Prioritize improvements based on impact and feasibility | Improvement Tracking Log | GAMSO Capability Mgmt |
| Track implementation of accepted improvements | Improvement Tracking Log | GAMSO Capability Mgmt |

```{mermaid}
%%| label: fig-8
%%| fig-cap: "Management Feedback Loop. Execution data flows through monitoring, quality assessment, methodology/version management, and audit processes. Continuous improvement feeds recommendations back to Design, closing the governance cycle."
%%| fig-width: 6
flowchart TD
    E["Execution\n(Section 5)<br/><em>data + paradata</em>"]

    M1["6.1 Monitor<br/>Process Performance<br/><em>edit/imputation rates</em>"]
    M2["6.2 Assess<br/>Data Quality<br/><em>quality improvement</em>"]
    M3["6.3 Manage Methodology<br/>& Version Lifecycle<br/><em>rules, versions</em>"]
    M4["6.4 Audit &<br/>Compliance Reporting<br/><em>edit auditability, privacy</em>"]
    M5["6.5 Continuous<br/>Improvement<br/><em>recommendations</em>"]

    D["Design<br/>(Section 3)<br/><em>updated rules & methods</em>"]

    E --> M1
    E --> M2
    M1 --> M2
    M2 --> M3
    M3 --> M4
    M4 --> M5
    M5 -->|"feedback loop"| D

    M1 -->|"dashboards"| PO["Process Owner"]
    M2 -->|"quality reports"| QM["Quality Manager"]
    M4 -->|"compliance reports"| VS07["VS-07.0\nGovernance"]

    style E fill:#ecfdf5,stroke:#059669
    style D fill:#f5f3ff,stroke:#7c3aed
    style M5 fill:#fef3c7,stroke:#d97706
```

## Business Services and Interfaces

The VS-03.0 business domain exposes the following services:

| Service | Direction | Consumers | Mapped Processes |
|---|---|---|---|
| **Error-Detection Service** | Internal (VS-02.0 → NSO) | Standardized data consumers, editing teams | 5.1 Conduct Error Detection |
| **Editing and Correction Service** | Internal | Editing teams, subject-matter analysts | 5.2 Perform Data Editing and Correction |
| **Imputation Service** | Internal | Editing teams, methodologists | 5.3 Impute Missing or Non-Response Data |
| **Derivation and Integration Service** | Internal | Editing teams, downstream analysts | 5.4 Derive Additional Variables |
| **Processed-Data Provisioning Service** | Internal (NSO → VS-04.0) | Estimation & modeling teams, data analysts | 5.5 Perform Quality Evaluation and Versioning |
| **Quality-Version Catalog Service** | Internal | All data consumers across the NSO | 6.3 Manage Methodology & Version Lifecycle |
| **Design and Methodology Service** | Internal | Methodologists, editing/imputation designers | 3.1–3.5 All design processes |

**Interface specifications:**

- **Processed-Data Provisioning Service** interface: event-driven notification ("Processed Data Registered") + catalog query API for downstream consumers to discover and access processed quality versions and their edit lineage
- **Editing and Correction Service** interface: review/adjudication workbench for analysts + edit-audit query API
- **Quality-Version Catalog Service** interface: search/browse API for quality versions, edit lineage, imputation flags, and derived-variable metadata

### Boundary Interface Specifications

The domain is loosely coupled (SAF-P07) to its neighbors through two steady-state interfaces. Specifying each boundary explicitly — the handover artefact, the metadata it must carry, the event that triggers it, and where responsibility transfers — makes the loose-coupling contract concrete and testable.

| Boundary | Handover Artefact | Required Metadata | Trigger Event | Responsibility Transfer |
|---|---|---|---|---|
| **VS-02.0 → VS-03.0** (intake) | Standardized Data (State #2) | Source-to-target mapping lineage, applied classification versions, recorded unit/currency/reference-period bases, list of unmapped/uncoded values for coding, definition-difference records, BIV classification | "Standardized Data Registered" event | VS-02.0 retains custody of the standardized artefact; VS-03.0 assumes responsibility for editing, imputation, derivation, interpretive coding, and value conversion on event receipt |
| **VS-03.0 → VS-04.0** (handover) | Processed Data (State #3) | Edit lineage (original value, rule, reason), imputation flags and methods, derived-variable formulae and classification, integration/linkage lineage, quality-improvement assessment, quality-version identifier, BIV classification | "Processed Data Registered" event | VS-03.0 retains custody of the processed version; VS-04.0 assumes responsibility for estimation, weighting, and analysis on event receipt |

Each interface exchanges a registered, immutable steady-state artefact plus its metadata — never internal working data — so neither side needs knowledge of the other's internal processing.

## Business Objects and Data Flow

```{mermaid}
%%| label: fig-9
%%| fig-cap: "Business Object Lifecycle across all four process types. Design objects govern implementation, which produces the pipeline that edits and enriches execution objects, which are assessed by management objects, which feed back to design."
%%| fig-width: 6
flowchart TB
    design["🔷 Design Artefacts<br/><small>Validation Rules · Imputation Methodology<br/>Derivation & Coding Specs · Versioning & Audit Policy</small>"]
    implement["🔧 Implementation Assets<br/><small>Editing & Imputation Engines · Derivation Pipeline<br/>Integration Component · Versioning Store</small>"]
    execute["⚡ Execution Objects"]
    manage["📊 Management Reports"]

    design -->|"govern building"| implement
    implement -->|"produces pipeline<br/>that processes"| execute
    execute -->|"assessed by"| manage
    manage -->|"feeds back to"| design

    subgraph execute_detail [" "]
        direction LR
        SD["Standardized Data<br/>(State #2)"]:::bo -->|"edited & enriched as"| PD["Processed Data<br/>(State #3)"]:::bo
    end

    execute --> execute_detail
    SD -->|generates| logs["Edit Lineage · Imputation Flags · Quality Versions"]

    classDef bo fill:#fbbf24,stroke:#b45309,color:#000
    style design fill:#f5f3ff,stroke:#7c3aed
    style implement fill:#dbeafe,stroke:#2563eb
    style execute fill:#fef9c3,stroke:#b45309
    style manage fill:#dcfce7,stroke:#16a34a
    style execute_detail fill:none,stroke:none
    style logs fill:#fff,stroke:#888,stroke-dasharray: 5 5
```


## Business Events

```{mermaid}
%%| label: fig-10
%%| fig-cap: "Event-Driven Choreography between the upstream domain (VS-02.0) and NSO teams, showing events across the Design → Implement → Execute → Manage cycle. The management phase closes the loop by feeding improvements back to design."
%%| fig-width: 6

sequenceDiagram
    participant US as Upstream (VS-02.0)
    participant NSO as NSO Teams
    participant PM as Process Mgmt

    rect rgb(245, 243, 255)
    Note over NSO: Design Phase
    NSO->>NSO: Define editing & validation rules, imputation<br/>methodology, derivation specs & versioning policy
    NSO-->>NSO: Design Artefacts Published
    end

    rect rgb(239, 246, 255)
    Note over NSO: Implementation Phase
    NSO->>NSO: Build editing/imputation engines, derivation<br/>& integration pipelines, versioning store
    NSO-->>NSO: Pipeline Production-Ready
    end

    rect rgb(236, 253, 245)
    Note over NSO,US: Execution Phase (per cycle)
    US-->>NSO: Standardized Data Registered event
    NSO->>NSO: Detect errors & diagnose quality
    NSO->>NSO: Edit, code & reconcile; impute gaps

    NSO->>NSO: Derive variables, convert units, integrate

    alt Quality version accepted
        NSO->>NSO: Evaluate quality, create immutable version,<br/>register lineage & metadata
        NSO-->>NSO: Processed Data Registered event
    else Quality insufficient
        NSO->>NSO: Re-edit / re-impute per review
    end
    end

    rect rgb(254, 243, 199)
    Note over PM: Management Phase
    PM->>PM: Monitor edit/imputation rates, assess quality<br/>improvement, produce audit reports
    PM-->>NSO: Improvement Recommendations
    end
```

## Framework Mappings

This reference table maps each process group of this document to the international frameworks (GSBPM, GAMSO, CSDA) and the SAF capability model. It is intended for architects and auditors; the narrative sections above do not depend on it.

| Process group | GSBPM | GAMSO | CSDA | SAF Capabilities |
|---|---|---|---|---|
| **Design** | Phase 1 (Specify Needs), Phase 2 (Design: 2.1–2.5) | Production (design activities), Capability Management | Data Governance, Metadata Management, Data Quality | 1.1.2 Design statistics product, 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| **Implementation** | Phase 3 (Build: 3.1–3.7) | Capability Management | Data Processing (setup), Data Governance (configuration) | 1.1.3 Build statistics product, 3.2.1 Application development, 3.2.2 Functional management |
| **Execution** | Phase 5 (Process: 5.3 Review & validate, 5.4 Edit & impute, 5.5 Derive new variables, 5.8 Finalise data files; 5.1 Integrate) | Production (execution) | Data Processing (execution) | 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| **Management** | Overarching processes (Quality Management, Metadata Management) | Corporate Support (Quality Management, Data Management, Metadata Management), Capability Management (improvement) | Data Quality, Data Governance, Traceability | 2.1.3 Statistical quality management, 4.1.4 Improve management, 4.1.5 Accountability |

## Applying This to Your NSO

### Maturity Assessment Checklist

Use this checklist to assess your NSO's maturity across all four process types — not just execution.

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
- [ ] Can a quality version be reproduced from the standardized input plus the recorded rules?
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

### End-to-End Scenarios

Each scenario walks through **all four process types**, demonstrating how the governance pattern works in practice.

#### Scenario A: Labour Force Survey (Coding, Editing, and Imputation)

**Design Phase:** Editing methodologists define consistency rules (e.g., age vs. labour-market status, hours vs. employment status) and a selective-editing strategy. Imputation specialists design regression imputation for item non-response on income, with constraints keeping imputed income in the respondent's plausible band. A coding methodology is designed for the free-text occupation strings handed over from VS-02 (ISCO-08, computer-assisted with a 0.85 confidence threshold, expert review below it). The versioning policy and edit audit-trail requirements are set.

**Implementation Phase:** Data engineers build the consistency-check and editing engine, configure the ISCO-08 coding service with its review queue, configure the income imputation model, and stand up the quality-version store. The pipeline is tested on a synthetic sample; the edit-impact test confirms edits move quality in the intended direction, the reproducibility test regenerates an identical version, and imputation is evaluated against a holdout sample (RMSE within target).

**Execution Phase:** For cycle Q3-2026, a Standardized Data Registered event arrives for 42,000 LFS returns. Error detection flags inconsistencies and outliers; auto-corrections are applied and high-impact records adjudicated. The 42,000 free-text occupations are coded to ISCO-08 (88% auto-coded, the rest computer-assisted and manually reviewed). Income non-response (9%) is imputed and flagged. Employment-status is harmonized to the ILO definition per the reconciliation rule. A quality version is created with full edit lineage and registered; VS-04.0 is notified.

**Management Phase:** Edit rate is 6.2%, imputation rate 9%, over-editing indicator low (selective editing working). Coding completion is 99.7%; a holdout re-check shows imputation RMSE stable. Improvement recommendations: refine two consistency rules generating false positives; retrain the occupation coder with this cycle's reviewed cases. Recommendations fed back to design.

#### Scenario B: Tax Register to Business Statistics (Editing, Conversion, Integration, Derivation)

**Design Phase:** The team designs outlier and consistency rules for turnover and employment, a value-reconciliation rule for the definition difference VS-02 recorded between the survey and VAT register, and conversion rules to turn turnover (recorded by VS-02 as "thousands of EUR" on a fiscal-year basis) into units on a calendar-year basis. Derived indicators (turnover-per-employee, productivity index) are specified with formulae and classification, and linkage rules join the tax data to the structural business survey on the SBR key.

**Implementation Phase:** Engineers build the editing engine, the unit/period conversion routines, the integration component (SBR-key linkage with conflict resolution), and the derivation calculators. Edit-impact and reproducibility tests pass; the conversion routine is checked so the original value remains recoverable from lineage.

**Execution Phase:** Q3-2026: a Standardized Data Registered event arrives for 2,347,891 tax records. Outliers and duplicates are detected and corrected with full lineage. Turnover is converted to units on the calendar year (conversion factor and original value stored), the tax and survey sources are integrated on the SBR key with the reconciliation rule applied where they disagree, and turnover-per-employee is derived. A quality version `PD-BUS-2026Q3-001` is created with lineage to `SD-BUS-2026Q3-001`, and VS-04.0 is notified.

**Management Phase:** Edit rate 1.8%, conversion applied to 100% of turnover with original values preserved, reconciliation applied to 12,400 linked units. No-residual-violation check passes. Disclosure-risk report confirms the linkage stays within assessed bounds. Improvement recommendation: tighten the outlier band for one NACE class; document a recurring reconciliation case as a standing rule. Recommendations fed back to design.

#### Scenario C: Web-Scraped Price Data (Coding, Imputation, Derivation)

**Design Phase:** The team designs the product classification (COICOP-2018) handed over from VS-02 for the free-text product names that had no source code, including an ML-assisted classifier with a confidence threshold and a review workflow. Currency-to-EUR and unit-to-standard-quantity conversion rules are designed from the bases VS-02 recorded, an imputation rule fills gaps where a product was not scraped on a given day (carry-forward with a staleness limit), and a daily price-index input is derived.

**Implementation Phase:** Engineers configure the COICOP classifier and review queue, the currency/unit conversion routines, the carry-forward imputation with its staleness flag, and the derivation of the index input. The classifier is evaluated against a manually-classified sample (90% agreement); below-threshold products route to review.

**Execution Phase:** For 2026-03-15, a Standardized Data Registered event arrives for 11,875 records. Products without a source code are classified to COICOP (95% above threshold, 5% reviewed). Prices are converted to EUR and standard units (original values preserved in lineage). Missing daily prices are imputed by carry-forward and flagged with staleness. The daily index input is derived. A quality version is created with full lineage and registered; VS-04.0 is notified.

**Management Phase:** Coding completion 99.2%, imputation rate (carry-forward) 4.8% with staleness within limits, conversion applied to all prices with originals preserved. A holdout check on classification shows 93% accuracy. Improvement recommendations: retrain the classifier for one recurring misclassified category; tighten the carry-forward staleness limit. Recommendations fed back to design.

## VS-04.0 Estimation, Analysis, and Statistical Modeling 

### Purpose and Scope

This document specifies the complete business layer for the **Estimation and closed-loop** business domain, corresponding to the *VS-04.0 Estimation, Analysis, and Statistical Modeling Value Stream*. It also covers 4 governance process types:

- **Design** — how the estimation, weighting, and analytical approach is specified and planned (produces metadata)
- **Implementation** — how the estimation and analysis pipeline is built, configured, and tested (produces the execution process)
- **Execution** — how data is operationally weighted, estimated, modeled, and validated (produces statistical data)
- **Management** — how the domain is monitored, quality-assessed, and improved (produces quality reports)

::: {.callout-warning title="Out of Scope"}
Application and Technology layer specifications are out of scope for this document. Combining multiple analyses into integrated and composite statistical products is out of scope — it belongs to VS-05.0 Statistical Product Composition. Final disclosure control for publication and dissemination belongs to VS-06.0. VS-04 produces validated statistics with initial confidentiality protection; it does not compose products or publish them.
:::





*A note on numbering:* each `VS-0x.y` below is both a value stream stage (*what value* is added) and a business process (*how* it is done); the numbering maps one-to-one. See the key-concepts box above.



### Position in the Statistical Value Chain

VS-04.0 is the fourth primary value stream — it receives Processed Data from VS-03.0 and applies statistical methods, estimation techniques, and analytical models to turn it into representative results that describe real-world phenomena. It is the "Estimate & Analyze Information" orchestration stage where data becomes statistical information.

```{mermaid}
%%| label: fig-1
%%| fig-cap: "Value Stream Context Map. VS-04.0 is highlighted as the estimation-and-analysis stage that turns processed microdata into representative statistics."
%%| fig-width: 6


flowchart TD
    subgraph primary["Primary Value Streams"]
        direction LR
        VS01["VS-01.0
        Data Acquisition
        & Ingestion"]
        VS02["VS-02.0
        Data Standardization
        & Integration"]
        VS03["VS-03.0
        Data Editing
        & Enrichment"]
        VS04["**VS-04.0**
        Estimation, Analysis
        & Modeling"]:::highlight
        VS05["VS-05.0
        Statistical Product
        Composition"]
        VS06["VS-06.0
        Dissemination
        & Service Delivery"]
        VS01 --> VS02 --> VS03 --> VS04 --> VS05 --> VS06
    end

    subgraph supporting["Supporting Value Streams"]
        VS07["VS-07.0
        Governance &
        Compliance"]
        VS08["VS-08.0
        Innovation &
        Methodology"]
        VS09["VS-09.0
        Infrastructure &
        Platform Enablement"]
        VS10["VS-10.0
        Customer &
        Stakeholder Engagement"]
    end

    supporting -.->|"enables"| primary

    classDef highlight fill:#2563eb,color:#fff,stroke:#1d4ed8,stroke-width:3px
```

### Steady State Transition

VS-04.0 transitions data from **Steady State #3 (Processed Data)** — edited, complete, enriched microdata — to **Steady State #4 (Output Data / Statistics)** — aggregated and analyzed statistics with estimates calculated, accuracy and quality indicators produced, lineage documented, internal review completed, and initial confidentiality measures applied so the output can potentially be released.

```{mermaid}
%%| label: fig-2
%%| fig-cap: "Steady State Transition from Processed Data to Output Data through the estimation and analysis service at the domain boundary. State #4 is shared with VS-05.0 Statistical Product Composition."
%%| fig-width: 6
flowchart LR
    subgraph upstream["Upstream Domain (VS-03.0)"]
        PD["Processed Data
        (State #3)"]
    end

    subgraph boundary["Estimation & Analysis Boundary"]
        QG["Estimation & Analysis Service
        (Weighting, Estimation, Aggregation,
        Modeling, Validation, Disclosure control)"]
    end

    subgraph internal["Output Domain (VS-04.0)"]
        OD["Output Data / Statistics
        (State #4)"]
    end

    PD --> QG --> OD

    style internal fill:#2563eb,color:#fff,stroke:#1d4ed8,stroke-width:3px
    style upstream fill:#7d7d7d,color:#fff,stroke:#1d4ed8,stroke-width:1px
    style boundary fill:#FFF,stroke-dasharray:5,5

```

::: {.callout-tip title='Output quality criteria (Examples)*'}
- Estimation/analytical approach selected and justified for the analytical objective
- Weighting and calibration applied to correct for sample bias, non-response, and coverage
- Estimates and aggregates calculated with accuracy measures (sampling error, confidence intervals)
- Model-based analyses conducted where applicable, with diagnostics documented
- Results validated for statistical soundness and coherence; methodology documented
- Initial statistical disclosure control applied so the output can potentially be released
- Full lineage from each statistic back to the processed source data and the method applied
:::

::: {.callout-important title="The methodological discipline — insight, transparently produced"}
VS-04 does not change microdata values; it **computes statistics from them**. The output is a new kind of object — estimates, weights, aggregates, model results. The guarantee here is **methodological transparency, reproducibility, and statistical soundness**: every estimate carries the methodology and parameters that produced it, an accuracy measure (sampling error, confidence interval, or model diagnostic), and lineage to its inputs, so that any published figure can be regenerated and defended. Fitness for purpose and coherence with related statistics are explicit acceptance criteria.
:::

::: {.callout-note title="Inherited from VS-03.0"}
VS-04 receives Processed Data **plus** the metadata VS-03 attached — edit lineage, derived-variable definitions, and **imputation flags**. The imputation flags matter here: estimation must reflect the additional uncertainty that imputed values introduce (e.g., via variance estimation that accounts for imputation), and the edit/derivation lineage is carried through so every estimate remains traceable to its original observed and imputed inputs.
:::


### The Four-Process Governance Pattern



```{mermaid}
%%| label: fig-3
%%| fig-cap: "The Four-Process Governance Pattern. Each process type produces a distinct artefact class. The cycle closes when Management findings feed back into Design improvements."
%%| fig-width: 6
flowchart LR
    D["**Design**
    _provides metadata_

    Estimation & weighting methodology,
    model specs, validation &\ndisclosure-control policy"]
    I["**Implement**
    _provides the execution process_

    Configured weighting/estimation engines,
    modeling environment, variance & SDC tools"]
    E["**Execute**
    _provides the statistical data_
    Weighted, estimated & modeled outputs,
    accuracy measures, methodology lineage"]
    M["**Manage**
    _provides quality reports_
    Accuracy & coherence dashboards, revision
    analyses, improvement recommendations"]

    D -->|"design artefacts
    guide building"| I
    I -->|"production-ready
    process"| E
    E -->|"data & process logs
    for assessment"| M
    M -->|"improvement
    feedback"| D

    style D fill:#7c3aed,color:#fff,stroke:#6d28d9
    style I fill:#2563eb,color:#fff,stroke:#1d4ed8
    style E fill:#059669,color:#fff,stroke:#047857
    style M fill:#d97706,color:#fff,stroke:#b45309
```




### Governing Principles

The following principles directly govern the VS-04.0 business domain:

| Principle | Statement | Application to VS-04.0 |
|---|---|---|
| **SAF-P01** | Actively participate in open source to maintain collective control over statistical processes | NSOs should contribute to open source communities for estimation, weighting, and modeling tooling (e.g., calibration and variance-estimation libraries), ensuring collective control over critical methodological capabilities rather than vendor dependence. |
| **SAF-P07** | Implement loosely coupled processes and systems | The estimation domain must be independent from upstream editing and downstream composition. Output Data (State #4) serves as a decoupling interface — downstream consumers access validated statistics without knowledge of the estimation internals. |
| **SAF-P08** | Data is shared property | Output statistics and output microdata, once validated, are available to all authorized consumers. Estimation should not be duplicated across products when the same validated output can serve multiple purposes. |
| **SAF-P09** | No data without metadata and classification | Every estimate carries metadata: the methodology and parameters applied, the weights used, accuracy measures (sampling error, confidence interval), the reference population, and a classification for derived statistics. This is what makes results transparent and reproducible. |
| **SAF-P10** | Security By Design | Access controls, integrity verification, and a tamper-evident record of methods and parameters are embedded in the estimation pipeline so that every published figure is attributable and reproducible, not added as an afterthought. |
| **SAF-P11** | Privacy By Design | Initial statistical disclosure control is applied to outputs at this stage, and the disclosure risk of estimates and any output microdata is assessed by design, so the result can potentially be released. |

::: {.callout-note title="Cross-cutting principle application"}
Several principles cut across all four process types. SAF-P09 (no data without metadata and classification) is the backbone of methodological transparency: Design defines the methodology and required output metadata, Execute captures the method, parameters, weights, and accuracy measures for every estimate, and Manage assesses output quality and coherence. SAF-P10 (Security By Design) governs the tamper-evident record of methods and the reproducibility of outputs across Execution (Sections 5.1–5.5). SAF-P11 (Privacy By Design) applies especially to validation and disclosure control (Section 5.5), where the output's disclosure risk is assessed before handover. SAF-P07 (loosely coupled) governs both the State #3 intake interface from VS-03.0 and the State #4 handover interface to VS-05.0.
:::

### Capability Foundations

VS-04.0 draws on the following SAF capabilities:

| Capability Group | Capabilities | Role in VS-04.0 |
|---|---|---|
| **1.1 Statistical design and build** | 1.1.2 Design statistics product, 1.1.3 Build statistics product | Design the estimation/weighting methodology and analytical models, and build the estimation pipeline |
| **2.1 Data management** | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management, 2.1.4 Statistical register management | Manage data, methodology metadata, and quality; assess accuracy and coherence; use registers for calibration totals |
| **3.2 Computerization and automation** | 3.2.1 Application development, 3.2.2 Functional management | Build and maintain weighting, estimation, aggregation, and modeling engines |
| **3.3 Security and Privacy** | 3.3.1 Privacy management, 3.3.2 Security planning | Apply statistical disclosure control and assess output disclosure risk |
| **4.1 Governance** | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improve management, 4.1.5 Accountability | Govern the domain, steward estimation methodology, plan improvements, report on reproducibility and compliance |

### Metadata Perspective

It is considered that metadata is an essential product of the Design phase and a critical concern of every other phase. In this domain, metadata is what makes a published figure defensible: every estimate must carry the method, parameters, weights, and accuracy that produced it. The table below consolidates the metadata produced across all four process types, covering both data metadata (about the outputs) and process metadata or paradata (about how the process runs).

| Process Type | Data Metadata Produced | Process Metadata (Paradata) Produced |
|---|---|---|
| **Design** | Estimation/weighting methodology, calibration totals & sources, aggregation specs, model specifications, validation & SDC policy | Design decisions log, methodology version, review and approval records |
| **Implement** | Engine configurations, weighting/estimation parameters, model parameters, variance-estimation settings, SDC parameters | Build log, test results, reproducibility-test outcomes, deployment approvals |
| **Execute** | Per-estimate methodology, weights, accuracy measures (sampling error, CI), model diagnostics, reference population, applied-SDC record | Operator identity, timing, software/version, parameter values, run identifiers |
| **Manage** | Accuracy & coherence assessments, revision analyses, lineage assessments, trend analyses | Accuracy dashboards, coherence reports, improvement decisions, audit findings |


## Business Roles and Actors



| Role                        | Process Orientation | Description                                                                                       |
|-----------------------------|---------------------|---------------------------------------------------------------------------------------------------|
| **Upstream Data Provider (VS-03.0)** | External (internal NSO) | Supplies Processed Data (State #3) with edit/imputation lineage to the estimation domain |
| **Methodology Authority**   | External            | Sets the estimation, weighting, and analytical methods the NSO conforms to (e.g., methodology unit, Eurostat guidance) |
| **Estimation Methodologist**| Design              | Designs the estimation strategy, weighting/calibration methodology, and accuracy-measurement approach |
| **Model Designer**          | Design              | Specifies analytical and forecasting models, their inputs, assumptions, and diagnostics            |
| **Disclosure-Control Designer** | Design          | Designs the statistical disclosure control rules and disclosure-risk criteria for outputs           |
| **Data Engineer**           | Implementation      | Builds and configures weighting, estimation, aggregation, and modeling engines and the pipeline    |
| **System Configurator**     | Implementation      | Configures estimation services, calibration-total sources, and access controls                    |
| **Test Manager**            | Implementation      | Plans and executes testing of the estimation pipeline (technical, reproducibility, benchmark)      |
| **Process Owner**           | Management          | Accountable for the end-to-end performance of the estimation and analysis domain                   |
| **Compliance Officer**      | Management          | Ensures reproducibility and disclosure-risk compliance, produces audit reports                     |
| **Quality Manager**         | Management          | Monitors accuracy/coherence KPIs, produces quality reports, and drives continuous improvement      |
| **Survey Statistician**     | Execution           | Applies the designed weighting/calibration and computes estimates with accuracy measures           |
| **Analyst / Modeler**       | Execution           | Conducts model-based analysis, regression, and forecasting, and documents diagnostics              |
| **Subject-Matter Reviewer** | Execution           | Reviews results for plausibility, coherence, and fitness for purpose, and signs off                |
| **Data Steward**            | Execution           | Registers output datasets and versions, manages metadata entries, and applies access controls      |



## Design Processes — "provides metadata"

*Framework alignment: GSBPM Phases 1–2 — see [Framework Mappings](#framework-mappings).*

The design phase produces the **metadata artefacts** that govern all subsequent phases — the estimation strategy, weighting/calibration methodology, aggregation and model specifications, and the validation and disclosure-control policy. Without well-designed methods, estimation becomes ad-hoc and indefensible, and management has no baseline to measure accuracy and coherence against.

### Design Estimation Strategy and Accuracy Approach

The starting point is choosing how the statistics will be estimated. This sub-process selects the estimation strategy appropriate to the source and analytical objective — design-based estimation for sample surveys, register-based aggregation, or model-assisted/model-based estimation for small domains — and defines the **accuracy-measurement** approach: how sampling error and confidence intervals are computed, including how the uncertainty introduced by VS-03 imputation is reflected in variance estimation. The team defines the target parameters, reference populations, and domains of estimation, aligned with GSBPM 2.5 (Design processing and analysis).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Select estimation strategy per source and objective (design-based / register-based / model-based) | Estimation Strategy Document | GSBPM 2.5 |
| Define target parameters, reference populations, and domains of estimation | Estimation Specification | GSBPM 2.5 |
| Define accuracy-measurement approach (sampling error, CI), reflecting imputation uncertainty | Accuracy Measurement Plan | GSBPM 2.5 |
| Define coherence criteria with related and prior statistics | Coherence Criteria | GAMSO QM |

::: {.callout-tip title="**NSO Example — Labour Force Survey:**"}
The LFS team designs a design-based estimation strategy for the employment rate, with calibration to population totals by age, sex, and region, and a variance estimator (e.g., a linearization or replication method) that accounts for the survey design and for income/non-response imputation flagged in VS-03. Target parameters and the domains of estimation (national and NUTS-2) are specified.
:::


### Design Weighting and Calibration Methodology

This sub-process designs how sample bias, non-response, and coverage errors are corrected through weighting. The team specifies the design weights, the non-response adjustment model, and the calibration method (e.g., calibration to known population totals from registers), including the auxiliary variables and calibration totals to be used and their authoritative sources. Bounds and acceptance constraints on weights are defined to prevent extreme weights, aligned with GSBPM 2.5.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Specify design weights and non-response adjustment | Weighting Specification | GSBPM 2.5 |
| Specify calibration method, auxiliary variables, and calibration totals (with sources) | Calibration Specification | GSBPM 2.5 |
| Define weight bounds and acceptance constraints | Weight Constraint Policy | GSBPM 2.5 |
| Define the authoritative source and version for calibration totals | Calibration-Total Source Register | CSDA Reference Data |

::: {.callout-tip title="**NSO Example — Household Survey:**"}
The household survey calibration is designed to population totals by age × sex × region drawn from the population register, with a generalized regression (GREG) calibration and weight bounds to cap the calibration factor, so that weighted demographic margins reproduce the register while extreme weights are avoided.
:::

### Design Aggregation and Model Specifications

This sub-process specifies what is computed. For aggregation, each output statistic is defined by its formula, the domains/breakdowns, and rounding/units conventions. For analysis, model-based methods (regression, time-series/forecasting, small-area models) are specified with their inputs, assumptions, and the diagnostics that must be produced and checked. Each output statistic is given its metadata and classification per SAF-P09, aligned with GSBPM 2.5.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Specify output aggregates: formulae, domains/breakdowns, units, rounding | Aggregation Specification | GSBPM 2.5 |
| Specify analytical/forecasting models: inputs, assumptions, diagnostics | Model Specification | GSBPM 2.5 |
| Define metadata and classification for every output statistic | Output-Statistic Metadata Standard | SAF-P09 |
| Define seasonal adjustment / time-series treatment where applicable | Time-Series Treatment Spec | GSBPM 2.5 |

### Design Validation and Disclosure-Control Policy

This sub-process designs how results are validated and protected before handover. Validation criteria cover statistical soundness (plausibility, consistency, model diagnostics within bounds), coherence with related and prior statistics, and the revision policy. The **statistical disclosure control (SDC)** policy is designed — disclosure-risk criteria for tables and any output microdata, and the protection methods (suppression, rounding, perturbation) — so the output reaches a state where it can potentially be released, aligned with GSBPM 6 design and SAF-P11. Reproducibility is designed in: an output must be regenerable from the processed input plus the recorded methodology and parameters.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define validation criteria: soundness, coherence, model diagnostics, revision policy | Validation Policy | GAMSO QM |
| Define disclosure-risk criteria and SDC protection methods | Disclosure-Control Policy | SAF-P11 |
| Define output metadata and methodology-documentation requirements | Output Documentation Standard | SAF-P09 |
| Design reproducibility: regenerate outputs from inputs + methodology + parameters | Reproducibility Design | SAF-P10 |

### Design Quality-Measurement and Versioning Framework

The final design sub-process ensures accuracy is measured and outputs are traceable. It defines the quality indicators to be produced (sampling error, coefficient of variation, response/coverage rates, model fit), the **output-versioning** policy (how versions are identified, what triggers a revision, immutability and retention), the lineage requirements from each statistic back to its processed inputs and the method applied, and the role-based access controls for outputs in line with SAF-P10.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define quality indicators (sampling error, CV, response/coverage, model fit) | Quality Indicator Set | GAMSO QM |
| Define output-versioning and revision policy | Versioning Policy | CSDA Traceability |
| Define lineage from each statistic to processed inputs and method | Lineage Specification | CSDA Traceability |
| Design role-based access control for outputs | Access Control Design | SAF-P10 |

```{mermaid}
%%| label: fig-4
%%| fig-cap: "Design Process Decomposition. The processed data model, methodology set, calibration totals, and framework standards flow into five design sub-processes, producing metadata artefacts that govern Implementation, Execution, and Management."
%%| fig-width: 6
flowchart TB
    subgraph inputs["Inputs"]
        PM["Processed Data Model<br/><small>(State #3 + imputation flags)</small>"]
        FW["Framework Standards<br/><small>GSBPM · GAMSO · CSDA</small>"]
        METH["Methodology Set<br/><small>Estimation · Weighting · Models</small>"]
        REG["Calibration Totals<br/><small>Registers / reference data</small>"]
    end

    subgraph design["Design Sub-Processes"]
        D1["3.1 Estimation Strategy<br/>& Accuracy Approach"]
        D2["3.2 Weighting &<br/>Calibration Methodology"]
        D3["3.3 Aggregation &<br/>Model Specs"]
        D4["3.4 Validation &<br/>Disclosure-Control Policy"]
        D5["3.5 Quality-Measurement<br/>& Versioning Framework"]
    end

    subgraph outputs["Metadata Artefacts"]
        O1["Estimation Strategy"]
        O2["Weighting & Calibration Spec"]
        O3["Aggregation & Model Specs"]
        O4["Validation & SDC Policy"]
        O5["Quality & Versioning Policy"]
    end

    PM --> D1
    METH -.->|inform| design
    FW -.->|inform| design
    REG --> D2

    D1 --> D2 --> D3 --> D4 --> D5

    D1 --> O1
    D2 --> O2
    D3 --> O3
    D4 --> O4
    D5 --> O5

    outputs -->|govern| NEXT["Implementation (§4) · Execution (§5)<br/>measured by Management (§6)"]

    style design fill:#f5f3ff,stroke:#7c3aed
    style outputs fill:#ede9fe,stroke:#7c3aed
```

## Implementation Processes — "provides the execution process"

*Framework alignment: GSBPM Phase 3 (Build) — see [Framework Mappings](#framework-mappings).*

The implementation phase takes the metadata artefacts from Design and **builds, configures, and tests** the production-ready estimation and analysis pipeline. Nothing runs operationally until this phase is complete.

### Build Weighting and Calibration Engines

This sub-process turns the weighting and calibration designs into operational tools. The weighting engine is built or configured to compute design weights and non-response adjustments, and the calibration engine to calibrate to the designed totals using the specified auxiliary variables, enforcing the weight bounds. The calibration-total connections are configured to the authoritative register/reference sources with version pinning, so the totals used are recorded and reproducible. All weighting logic is version-controlled in line with SAF-P10, following GSBPM 3.1–3.2.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Build/configure the weighting engine (design weights, non-response adjustment) | Configured weighting engine | GSBPM 3.2 |
| Build/configure the calibration engine with auxiliary variables and bounds | Configured calibration engine | GSBPM 3.2 |
| Configure calibration-total connections (versioned register sources) | Calibration-total integration | CSDA Reference Data |
| Version-control all weighting/calibration logic | Versioned methodology repository | SAF-P10 |

::: {.callout-tip title="**NSO Example — Household Survey:**"}
The team configures a GREG calibration engine that pulls age × sex × region totals from a pinned version of the population register, applies weight bounds, and records the calibration totals and convergence diagnostics with every run so the weighting is reproducible.
:::

### Build Estimation and Aggregation Pipelines

The designed estimation and aggregation specifications are implemented as automated services. The estimation engine computes the target parameters with the designed accuracy measures, and the **variance-estimation** component computes sampling errors and confidence intervals — accounting for the survey design and for imputation uncertainty using the VS-03 imputation flags. The aggregation pipeline computes the specified output aggregates across the designed domains with the rounding/units conventions. Every output is produced with its methodology, parameters, weights, and accuracy measure attached, following GSBPM 3.2.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Build the estimation engine for the designed target parameters | Estimation pipeline | GSBPM 3.2 |
| Build the variance-estimation component (design + imputation uncertainty) | Variance/accuracy component | GSBPM 3.2 |
| Build the aggregation pipeline (domains, units, rounding) | Aggregation pipeline | GSBPM 3.2 |
| Attach methodology, weights, and accuracy measure to every output | Output metadata binding | SAF-P09 |

### Build Modeling Environment, Validation, and SDC Tooling

This sub-process implements model-based analysis, validation, and disclosure control. The modeling environment is built/configured to run the specified analytical, forecasting, and small-area models with their diagnostics, and (where applicable) seasonal adjustment. Validation tooling implements the designed soundness and coherence checks, including comparison against prior periods and related statistics. The **SDC tooling** implements the designed disclosure-risk checks and protection methods (suppression, rounding, perturbation). The output-versioning store is built so each accepted output version is immutable, identified, reproducible from inputs plus methodology, and accompanied by its lineage. Event notifications are configured to alert downstream consumers (VS-05.0) when an output version is registered.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Build/configure the modeling environment (models, diagnostics, seasonal adjustment) | Modeling environment | GSBPM 3.2 |
| Implement validation tooling (soundness, coherence, prior-period comparison) | Validation tooling | GSBPM 3.2 |
| Implement SDC tooling (disclosure-risk checks, suppression/rounding/perturbation) | SDC tooling | SAF-P11 |
| Build the output-versioning store (immutable, identified, reproducible) | Versioning store | CSDA Traceability |
| Configure "Output Data Registered" event for downstream consumers | Event publication | GSBPM 3.2 |

### Test and Validate the Pipeline

Before the pipeline goes into production, it must be rigorously verified. Technical testing covers all individual components — weighting, calibration, estimation, variance, aggregation, modeling, validation, SDC, and versioning store (GSBPM 3.5). Integration testing validates the end-to-end flow from processed intake through weighting, estimation, modeling, validation, SDC, to versioned registration. A **reproducibility test** confirms an output can be regenerated identically from the processed input plus the recorded methodology and parameters; a **benchmark/back-series test** compares results against a known or prior-period benchmark; and accuracy measures are checked against expectations. The phase concludes with finalization of the production system and documentation of operational procedures (GSBPM 3.6–3.7).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Technical testing of all individual components | Unit test reports | GSBPM 3.5 |
| Integration testing: end-to-end flow from processed intake to versioned registration | Integration test report | GSBPM 3.5 |
| Reproducibility test (regenerate an output from inputs + methodology) | Reproducibility report | GSBPM 3.6 |
| Benchmark / back-series test against known or prior results | Benchmark test report | GSBPM 3.6 |
| Check accuracy measures and model diagnostics against expectations | Accuracy verification report | GSBPM 3.6 |
| Finalize production system and document operational procedures | Operational Procedures Manual, Production-Ready Pipeline | GSBPM 3.7 |

```{mermaid}
%%| label: fig-5
%%| fig-cap: "Implementation Pipeline from design artefacts through build/configure/test to production-ready system."
%%| fig-width: 6
flowchart LR
    subgraph design_artefacts["Design Artefacts (from Section 3)"]
        DA1["Estimation\nStrategy"]
        DA2["Weighting &\nCalibration Spec"]
        DA3["Aggregation &\nModel Specs"]
        DA4["Validation &\nSDC Policy"]
        DA5["Quality &\nVersioning Policy"]
    end

    subgraph build["Build & Configure"]
        B1["4.1 Build Weighting\n& Calibration Engines"]
        B2["4.2 Build Estimation\n& Aggregation Pipelines"]
        B3["4.3 Build Modeling,\nValidation & SDC"]
    end

    subgraph test["Test & Validate"]
        T1["4.4 Technical\nTesting"]
        T2["4.4 Reproducibility\n& Benchmark"]
        T3["4.4 Accuracy\nVerification"]
    end

    subgraph output["Production-Ready"]
        PR["Operational\nEstimation\nPipeline"]
        OP["Operational\nProcedures"]
    end

    DA1 & DA2 --> B1
    DA1 & DA3 --> B2
    DA3 & DA4 & DA5 --> B3

    B1 & B2 & B3 --> T1 --> T2 --> T3
    T3 --> PR & OP

    PR -->|"ready for"| EXEC["Execution\n(Section 5)"]

    style build fill:#eff6ff,stroke:#2563eb
    style test fill:#dbeafe,stroke:#2563eb
```

## Execution Processes — "provides the statistical data"

*Framework alignment: the later GSBPM phases for this domain — see [Framework Mappings](#framework-mappings).*

The execution phase runs the **designed and implemented pipeline** operationally for each production cycle. This corresponds to the five VS-04 value stream stages. In a mature steady state, much of the work has been pre-designed (Section 3) and pre-built (Section 4) — execution focuses on running the cycle, computing weights/estimates/models, and capturing the methodology, parameters, and accuracy measures so that every output is reproducible and defensible.

### Confirm Estimation and Analytical Approach

**Value created:** *The right, pre-approved method selected for this cycle's data and objective.*

When a "Processed Data Registered" event is received from VS-03.0, execution begins by confirming the estimation and analytical approach for the cycle. In a mature steady state the methodology has been designed (Section 3), so per-cycle execution confirms or selects the pre-approved approach for the data at hand, verifies that the calibration totals and reference sources are current, and confirms that the target parameters and domains apply. Significant changes (a new domain, a methodology revision) trigger a return to the design process rather than ad-hoc adaptation. This applies GSBPM 2.5/5.6 in their recurrent form.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Confirm or select the pre-approved estimation/analytical approach for the cycle | Confirmed approach for cycle | GSBPM 2.5 |
| Verify calibration totals and reference sources are current | Reference-source confirmation | CSDA Reference Data |
| Confirm target parameters and domains of estimation | Confirmed estimation scope | GSBPM 5.6 |
| Flag methodology changes for design review | Methodology-change exception (if any) | GAMSO QM |

::: {.callout-tip title="**NSO Example — Labour Force Survey:**"}
For cycle Q3-2026 the LFS team confirms the design-based estimation strategy and the calibration totals (latest population-register extract by age × sex × region), and confirms the domains (national and NUTS-2). No methodology change is needed, so the cycle proceeds without a return to design.
:::

### Apply Weighting and Calibration

**Value created:** *Bias from sampling, non-response, and coverage corrected so results represent the population.*

This sub-process computes the weights, aligned with GSBPM 5.6 (Calculate weights). The weighting engine applies the design weights and non-response adjustment, and the calibration engine calibrates to the confirmed population totals using the designed auxiliary variables, enforcing the weight bounds. Calibration convergence and the resulting weight distribution are checked against the designed constraints, and the calibration totals, auxiliary variables, and convergence diagnostics are recorded so the weighting is reproducible.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Compute design weights and non-response adjustment | Adjusted weights | GSBPM 5.6 |
| Calibrate to confirmed population totals with designed auxiliary variables | Calibrated weights | GSBPM 5.6 |
| Check convergence and weight distribution against bounds | Weight diagnostics | GSBPM 5.6 |
| Record calibration totals, auxiliaries, and diagnostics as lineage | Weighting lineage | SAF-P09 |

::: {.callout-tip title="**NSO Example — Household Survey:**"}
The GREG calibration converges in 6 iterations; weighted margins reproduce the register totals by age × sex × region, the calibration factor stays within the designed bounds, and the totals and diagnostics are stored with the run.
:::

### Estimate and Aggregate Data

**Value created:** *Representative statistics and aggregates, each carrying its accuracy.*

This sub-process computes the target estimates and aggregates, aligned with GSBPM 5.7 (Calculate aggregates) and 6.1 (Prepare draft outputs). The estimation engine computes the target parameters using the calibrated weights, and the aggregation pipeline computes the specified aggregates across the designed domains with the units/rounding conventions. The variance-estimation component computes sampling errors and confidence intervals, reflecting both the survey design and the imputation uncertainty signaled by the VS-03 imputation flags. Every estimate is produced with its methodology, weights, and accuracy measure attached.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Compute target estimates using calibrated weights | Point estimates | GSBPM 5.7 |
| Compute aggregates across designed domains (units, rounding) | Output aggregates | GSBPM 5.7 |
| Compute sampling errors and CIs (design + imputation uncertainty) | Accuracy measures | GSBPM 6.1 |
| Attach methodology, weights, and accuracy to every estimate | Estimate metadata | SAF-P09 |

```{mermaid}
%%| label: fig-6
%%| fig-cap: "Estimation and Aggregation Architecture. Calibrated weights and imputation-flagged microdata feed point estimation and aggregation; variance estimation reflects both the survey design and the imputation uncertainty, and every output carries its accuracy and methodology."
%%| fig-width: 6
flowchart LR
    subgraph inputs["Processed microdata (State #3)"]
        direction TB
        MD["Microdata\n(observed + imputed,\nimputation-flagged)"]
        WT["Calibrated weights\n(from 5.2)"]
    end

    subgraph estimation["Estimation & Aggregation"]
        EST["Point\nestimates"]
        AGG["Aggregates\n(by domain)"]
        VAR["Variance / CI\n(design + imputation)"]
    end

    subgraph output["Output statistics"]
        OUT["Estimates + aggregates\n(+ accuracy + methodology)"]
    end

    MD --> EST
    WT --> EST
    EST --> AGG
    EST --> VAR
    AGG --> OUT
    VAR --> OUT

    MD -.->|"imputation flags\nraise uncertainty"| VAR

    style inputs fill:#ecfdf5,stroke:#059669
    style estimation fill:#f0fdf4,stroke:#059669
```


::: {.callout-tip title='**NSO Example — Labour Force Survey:**'}
The Q3-2026 employment rate is estimated at 71.4% with a 95% CI of ±0.5pp at national level and wider intervals at NUTS-2; the variance estimate is inflated appropriately for the income/non-response imputation flagged in VS-03. Each published cell carries its estimate, CV, and the method that produced it.
:::


### Perform Model-Based Analysis

**Value created:** *Deeper insight — relationships, trends, and small-domain estimates the direct counts cannot give.*

This sub-process conducts the designed model-based analyses, aligned with GSBPM 6.1/6.3. Analytical, regression, time-series/forecasting, and small-area models specified in design are run on the data, their diagnostics computed and checked against the designed bounds, and seasonal adjustment applied where applicable. Results are interpreted in context, with assumptions and limitations documented. As with direct estimates, every model output carries its specification, parameters, diagnostics, and uncertainty so it is reproducible and defensible.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Run the designed analytical/forecasting/small-area models | Model outputs | GSBPM 6.1 |
| Compute and check model diagnostics against designed bounds | Model diagnostics | GSBPM 6.2 |
| Apply seasonal adjustment / time-series treatment where applicable | Adjusted series | GSBPM 6.1 |
| Interpret results; document assumptions and limitations | Analytical commentary | GSBPM 6.3 |

::: {.callout-tip title="**NSO Example — Tax Register to Business Statistics:**"}
For small NACE × region domains where the direct register aggregate is unstable, a small-area model borrows strength across domains to produce more reliable estimates; model diagnostics (fit, prediction intervals) are recorded, and the model-based cells are flagged distinctly from direct aggregates.
:::

### Validate and Document Results

**Value created:** *Statistically sound, coherent, documented, and disclosure-safe statistics ready for handover.*

The final execution sub-process validates the results and produces the official output version, aligned with GSBPM 6.2 (Validate outputs), 6.4 (Apply disclosure control), and 6.5 (Finalise outputs). Results are checked for statistical soundness and consistency, and for coherence with prior periods and related statistics; significant movements are explained, and revisions handled per policy. **Initial statistical disclosure control** is applied per the designed policy — disclosure risk assessed and protection methods (suppression, rounding, perturbation) applied — so the output can potentially be released. The methodology and quality indicators are documented, a persistent immutable output version is created with a unique identifier and full lineage, registered per SAF-P09, and access permissions applied per SAF-P10. The sub-process concludes by publishing an "Output Data Registered" event, notifying downstream VS-05.0 that new validated statistics are available for composition.

**Output:** **Output Data / Statistics (Steady State #4)** — the official handover artefact to the rest of the statistical value chain.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Validate soundness and coherence; explain movements; handle revisions | Validation Report | GSBPM 6.2 |
| Apply initial statistical disclosure control per designed policy | Disclosure-controlled outputs | GSBPM 6.4 |
| Document methodology and quality indicators | Methodology & Quality Documentation | SAF-P09 |
| Create an immutable, identified output version with full lineage | Versioned Output Data | CSDA Traceability |
| Register metadata and publish "Output Data Registered" event to notify VS-05.0 | Catalog registration, event | SAF-P07 |

```{mermaid}
%%| label: fig-7
%%| fig-cap: "Output Data Artefact Structure. Reading guide: each box is a type of record with its fields; a connecting line means the records are linked. Each output version contains estimates with accuracy measures, is linked to the methodology that produced it and the applied disclosure control, and is traceable to the processed source data."
%%| fig-width: 6
erDiagram
    OUTPUT_DATA_ARTEFACT {
        string dataset_id PK "Unique persistent URI/UUID"
        string output_version "Immutable version identifier"
        date reference_period "Reference period"
        datetime registration_timestamp "When registered in catalog"
        string processed_source_id "Processed Data (State #3) source ID"
    }
    ESTIMATE_RECORD {
        string statistic "Estimate / aggregate"
        string domain "Domain / breakdown"
        float point_estimate "Estimated value"
        string method "Estimation method applied"
    }
    ACCURACY_MEASURE {
        float sampling_error "Standard error"
        float cv "Coefficient of variation"
        string confidence_interval "CI at stated level"
        boolean imputation_reflected "Imputation uncertainty included"
    }
    METHODOLOGY_RECORD {
        string weighting_method "Design + calibration method"
        string calibration_totals_ref "Register source + version"
        string model_spec "Model specification (if any)"
        string software_version "Engine/software version"
    }
    DISCLOSURE_CONTROL {
        string sdc_method "Suppression/rounding/perturbation"
        string risk_assessment "Disclosure-risk outcome"
        boolean release_safe "Cleared for potential release"
    }

    OUTPUT_DATA_ARTEFACT ||--|{ ESTIMATE_RECORD : "contains"
    ESTIMATE_RECORD ||--|| ACCURACY_MEASURE : "has accuracy"
    OUTPUT_DATA_ARTEFACT ||--|| METHODOLOGY_RECORD : "produced by"
    OUTPUT_DATA_ARTEFACT ||--|| DISCLOSURE_CONTROL : "protected by"
```

## Management Processes — "provides quality reports"

*Framework alignment: GSBPM overarching Quality/Metadata Management — see [Framework Mappings](#framework-mappings).*

The management phase runs **alongside and after** execution. It monitors the estimation domain's performance, assesses the accuracy and coherence of outputs, ensures every result is reproducible and disclosure-safe, and feeds improvement recommendations back into the design phase — closing the governance cycle.

### Monitor Process Performance

Operational performance of the estimation domain must be tracked systematically across production cycles. The process owner and quality manager collect and aggregate key performance indicators, monitor throughput against the release calendar, and track paradata — which methods and parameter/software versions were run, when, by whom, and how many manual interventions occurred. This information feeds process performance dashboards that give the process owner a real-time view of domain health, aligned with the GAMSO Quality Management capability.

**Key Performance Indicators (KPIs):**

| KPI | Description | Measurement |
|---|---|---|
| On-time output rate | Outputs produced within the release-calendar window | Per output, per cycle |
| Average sampling error / CV | Typical accuracy of key estimates | Per statistic, per cycle |
| Coherence-check pass rate | Outputs passing coherence checks on first run | Per cycle |
| Revision magnitude | Size of revisions vs. previously published figures | Per statistic, per cycle |
| Reproducibility rate | Outputs regenerable identically from inputs + methodology | Per cycle |
| Processing time | Duration from processed intake to versioned registration | Per output, per cycle |

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Collect and aggregate KPIs per production cycle | Process Performance Dashboard | GAMSO QM |
| Monitor throughput against the release calendar | Throughput Report | GAMSO QM |
| Track paradata: methods, parameter/software versions, interventions | Paradata Records | GAMSO QM |
| Generate process performance dashboards | Dashboard for Process Owner | GAMSO QM |

### Assess Output Quality

Beyond process performance, the quality of the outputs themselves must be evaluated against the criteria established in design. Each output is assessed across multiple quality dimensions: accuracy (sampling error, CV, model fit), coherence (consistency with related and prior statistics), timeliness (against the release calendar), and reliability (revision analysis comparing preliminary and final figures). Results are compared against the designed quality criteria from Section 3.5. Quality indicators are produced per statistic, per output, and per cycle, and trends are tracked to detect deteriorating accuracy, growing revisions, or models that need recalibration. This aligns with the CSDA Data Quality capability and SAF Capability 2.1.3.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Evaluate accuracy (sampling error, CV, model fit) | Accuracy Report (per cycle) | SAF 2.1.3 |
| Assess coherence with related and prior statistics | Coherence Report | CSDA Data Quality |
| Conduct revision analysis (preliminary vs. final) | Revision Analysis | SAF 2.1.3 |
| Identify quality trends across statistics and cycles | Quality Trend Analysis | SAF 2.1.3 |

### Manage Methodology and Output-Version Lifecycle

The estimation methodology and the output versions it produces must remain current, complete, and well-governed. This sub-process governs the lifecycle of estimation methods, weighting/calibration specifications, and models — versioning them, managing transitions (e.g., a methodology change with back-series implications), and retiring obsolete methods. It verifies metadata completeness — that every output carries full methodology, weights, accuracy measures, and lineage as an SAF-P09 compliance check — and governs the output-version store: retention, immutability, and reconciliation that catalog entries match stored versions. Metadata lineage from processed through estimation to output state is tracked.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Govern estimation-method, weighting, and model lifecycle and versions | Methodology Version Register | SAF-P09 |
| Verify metadata completeness (methodology, weights, accuracy, lineage) | Metadata Quality Report | SAF-P09 |
| Govern the output-version store: retention, immutability, reconciliation | Version Store Audit | CSDA Traceability |
| Track metadata lineage from processed to output state | Metadata Lineage Audit | CSDA Traceability |

### Audit and Compliance Reporting

This sub-process produces the evidence that the estimation domain operates within methodological, legal, and organizational requirements. Reproducibility-audit reports demonstrate that every published figure can be regenerated from the processed input plus the recorded methodology and parameters — supporting methodological transparency and accountability. Disclosure-control reporting confirms that SDC was applied and that outputs meet the disclosure-risk criteria per SAF-P11. Methodology compliance reporting confirms that approved estimation and analytical methods were applied, and security compliance reporting verifies that designed access controls and the tamper-evident methodology record have been applied. These reports satisfy the SAF Capability 4.1.5 (Accountability) obligation and feed into VS-07.0 Governance and Compliance.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Produce reproducibility-audit reports: every figure regenerable | Reproducibility Audit Summary | SAF 4.1.5 |
| Report on disclosure control applied and disclosure-risk outcomes | Disclosure-Control Report | SAF-P11 |
| Report on methodology compliance (approved methods applied) | Methodology Compliance Report | SAF 4.1.5 |
| Report on security compliance: access controls, methodology-record integrity | Compliance Report (per cycle) | SAF-P10 |

### Continuous Improvement

The final management sub-process closes the governance loop by analyzing performance and quality data to identify and drive improvements. Quality trends across production cycles are examined: are sampling errors falling, are revisions shrinking, is coherence improving, are models holding up? Improvement opportunities are identified — refining the calibration specification to reduce variance, recalibrating or replacing models, improving non-response adjustment, adopting better variance estimators, and tuning the release process to improve timeliness. These improvement recommendations are fed back to the design processes (Section 3), prioritized based on impact and feasibility, and tracked through subsequent design-implement-execute cycles. This is the SAF Capability 4.1.4 (Improve management) in action, and it connects to the GAMSO concept of transferring mature capabilities from innovation into production.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Analyze quality trends across production cycles | Improvement Recommendations Report | SAF 4.1.4 |
| Identify improvement opportunities: calibration, models, variance estimators, timeliness | Updated Design Inputs | SAF 4.1.4 |
| Feed recommendations back to design processes (Section 3) | Design feedback (closing the governance loop) | SAF 4.1.4 |
| Prioritize improvements based on impact and feasibility | Improvement Tracking Log | GAMSO Capability Mgmt |
| Track implementation of accepted improvements | Improvement Tracking Log | GAMSO Capability Mgmt |

```{mermaid}
%%| label: fig-8
%%| fig-cap: "Management Feedback Loop. Execution data flows through monitoring, quality assessment, methodology/version management, and audit processes. Continuous improvement feeds recommendations back to Design, closing the governance cycle."
%%| fig-width: 6
flowchart TD
    E["Execution\n(Section 5)<br/><em>data + paradata</em>"]

    M1["6.1 Monitor<br/>Process Performance<br/><em>accuracy, timeliness</em>"]
    M2["6.2 Assess<br/>Output Quality<br/><em>accuracy, coherence, revisions</em>"]
    M3["6.3 Manage Methodology<br/>& Version Lifecycle<br/><em>methods, versions</em>"]
    M4["6.4 Audit &<br/>Compliance Reporting<br/><em>reproducibility, disclosure</em>"]
    M5["6.5 Continuous<br/>Improvement<br/><em>recommendations</em>"]

    D["Design<br/>(Section 3)<br/><em>updated methods & models</em>"]

    E --> M1
    E --> M2
    M1 --> M2
    M2 --> M3
    M3 --> M4
    M4 --> M5
    M5 -->|"feedback loop"| D

    M1 -->|"dashboards"| PO["Process Owner"]
    M2 -->|"quality reports"| QM["Quality Manager"]
    M4 -->|"compliance reports"| VS07["VS-07.0\nGovernance"]

    style E fill:#ecfdf5,stroke:#059669
    style D fill:#f5f3ff,stroke:#7c3aed
    style M5 fill:#fef3c7,stroke:#d97706
```

## Business Services and Interfaces

The VS-04.0 business domain exposes the following services:

| Service | Direction | Consumers | Mapped Processes |
|---|---|---|---|
| **Weighting and Calibration Service** | Internal (VS-03.0 → NSO) | Processed data consumers, estimation teams | 5.2 Apply Weighting and Calibration |
| **Estimation and Aggregation Service** | Internal | Estimation teams, analysts | 5.3 Estimate and Aggregate Data |
| **Modeling and Analysis Service** | Internal | Analysts, methodologists | 5.4 Perform Model-Based Analysis |
| **Validation and Disclosure-Control Service** | Internal | Quality managers, disclosure-control officers | 5.5 Validate and Document Results |
| **Output-Data Provisioning Service** | Internal (NSO → VS-05.0) | Product composition teams, data analysts | 5.5 Validate and Document Results |
| **Output-Version Catalog Service** | Internal | All data consumers across the NSO | 6.3 Manage Methodology & Version Lifecycle |
| **Design and Methodology Service** | Internal | Methodologists, estimation/model designers | 3.1–3.5 All design processes |

**Interface specifications:**

- **Output-Data Provisioning Service** interface: event-driven notification ("Output Data Registered") + catalog query API for downstream consumers to discover and access output versions, their accuracy measures, and methodology
- **Estimation and Aggregation Service** interface: estimation API returning estimates with accuracy measures, and a methodology/parameters query API
- **Output-Version Catalog Service** interface: search/browse API for output versions, accuracy measures, methodology documentation, and lineage

### Boundary Interface Specifications

The domain is loosely coupled (SAF-P07) to its neighbors through two steady-state interfaces. Specifying each boundary explicitly — the handover artefact, the metadata it must carry, the event that triggers it, and where responsibility transfers — makes the loose-coupling contract concrete and testable.

| Boundary | Handover Artefact | Required Metadata | Trigger Event | Responsibility Transfer |
|---|---|---|---|---|
| **VS-03.0 → VS-04.0** (intake) | Processed Data (State #3) | Edit lineage, derived-variable definitions, **imputation flags and methods**, quality-improvement assessment, quality-version identifier, BIV classification | "Processed Data Registered" event | VS-03.0 retains custody of the processed version; VS-04.0 assumes responsibility for weighting, estimation, modeling, and validation on event receipt |
| **VS-04.0 → VS-05.0** (handover) | Output Data / Statistics (State #4) | Methodology and parameters, weights, accuracy measures (sampling error, CI), model diagnostics, applied-SDC record, quality indicators, output-version identifier, lineage to processed source, BIV classification | "Output Data Registered" event | VS-04.0 retains custody of the output version; VS-05.0 assumes responsibility for composing integrated and composite products on event receipt |

Each interface exchanges a registered, immutable steady-state artefact plus its metadata — never internal working data — so neither side needs knowledge of the other's internal processing.

## Business Objects and Data Flow

```{mermaid}
%%| label: fig-9
%%| fig-cap: "Business Object Lifecycle across all four process types. Design objects govern implementation, which produces the pipeline that estimates and analyses execution objects, which are assessed by management objects, which feed back to design."
%%| fig-width: 6
flowchart TB
    design["🔷 Design Artefacts<br/><small>Estimation Strategy · Weighting & Calibration Spec<br/>Aggregation & Model Specs · Validation & SDC Policy</small>"]
    implement["🔧 Implementation Assets<br/><small>Weighting & Estimation Engines · Modeling Environment<br/>Variance & SDC Tooling · Versioning Store</small>"]
    execute["⚡ Execution Objects"]
    manage["📊 Management Reports"]

    design -->|"govern building"| implement
    implement -->|"produces pipeline<br/>that processes"| execute
    execute -->|"assessed by"| manage
    manage -->|"feeds back to"| design

    subgraph execute_detail [" "]
        direction LR
        PD["Processed Data<br/>(State #3)"]:::bo -->|"estimated & analyzed as"| OD["Output Data<br/>(State #4)"]:::bo
    end

    execute --> execute_detail
    PD -->|generates| logs["Methodology · Weights · Accuracy · Output Versions"]

    classDef bo fill:#fbbf24,stroke:#b45309,color:#000
    style design fill:#f5f3ff,stroke:#7c3aed
    style implement fill:#dbeafe,stroke:#2563eb
    style execute fill:#fef9c3,stroke:#b45309
    style manage fill:#dcfce7,stroke:#16a34a
    style execute_detail fill:none,stroke:none
    style logs fill:#fff,stroke:#888,stroke-dasharray: 5 5
```


## Business Events

```{mermaid}
%%| label: fig-10
%%| fig-cap: "Event-Driven Choreography between the upstream domain (VS-03.0) and NSO teams, showing events across the Design → Implement → Execute → Manage cycle. The management phase closes the loop by feeding improvements back to design."
%%| fig-width: 6

sequenceDiagram
    participant US as Upstream (VS-03.0)
    participant NSO as NSO Teams
    participant PM as Process Mgmt

    rect rgb(245, 243, 255)
    Note over NSO: Design Phase
    NSO->>NSO: Define estimation & weighting methodology,<br/>model specs, validation & SDC policy
    NSO-->>NSO: Design Artefacts Published
    end

    rect rgb(239, 246, 255)
    Note over NSO: Implementation Phase
    NSO->>NSO: Build weighting/estimation engines, modeling<br/>environment, variance & SDC tooling
    NSO-->>NSO: Pipeline Production-Ready
    end

    rect rgb(236, 253, 245)
    Note over NSO,US: Execution Phase (per cycle)
    US-->>NSO: Processed Data Registered event
    NSO->>NSO: Confirm approach; apply weighting & calibration
    NSO->>NSO: Estimate & aggregate; run model-based analysis

    NSO->>NSO: Validate soundness & coherence; apply disclosure control

    alt Output version accepted
        NSO->>NSO: Document methodology, create immutable version,<br/>register accuracy & lineage
        NSO-->>NSO: Output Data Registered event
    else Validation failed
        NSO->>NSO: Re-estimate / revise per review
    end
    end

    rect rgb(254, 243, 199)
    Note over PM: Management Phase
    PM->>PM: Monitor accuracy & timeliness, assess coherence<br/>& revisions, produce audit reports
    PM-->>NSO: Improvement Recommendations
    end
```

## Framework Mappings

This reference table maps each process group of this document to the international frameworks (GSBPM, GAMSO, CSDA) and the SAF capability model. It is intended for architects and auditors; the narrative sections above do not depend on it.

| Process group | GSBPM | GAMSO | CSDA | SAF Capabilities |
|---|---|---|---|---|
| **Design** | Phase 1 (Specify Needs), Phase 2 (Design: 2.1–2.5) | Production (design activities), Capability Management | Data Governance, Metadata Management, Data Quality | 1.1.2 Design statistics product, 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| **Implementation** | Phase 3 (Build: 3.1–3.7) | Capability Management | Data Processing / Analysis (setup), Data Governance (configuration) | 1.1.3 Build statistics product, 3.2.1 Application development, 3.2.2 Functional management |
| **Execution** | Phase 5 (Process: 5.6 Calculate weights, 5.7 Calculate aggregates) + Phase 6 (Analyze: 6.1 Prepare draft outputs, 6.2 Validate outputs, 6.3 Interpret & explain, 6.4 Apply disclosure control, 6.5 Finalise outputs) | Production (execution) | Data Analysis (execution) | 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| **Management** | Overarching processes (Quality Management, Metadata Management) | Corporate Support (Quality Management, Data Management, Metadata Management), Capability Management (improvement) | Data Quality, Data Governance, Traceability | 2.1.3 Statistical quality management, 4.1.4 Improve management, 4.1.5 Accountability |

## Applying This to Your NSO

### Maturity Assessment Checklist

Use this checklist to assess your NSO's maturity across all four process types — not just execution.

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

### End-to-End Scenarios

Each scenario walks through **all four process types**, demonstrating how the governance pattern works in practice.

#### Scenario A: Labour Force Survey (Design-Based Estimation)

**Design Phase:** Estimation methodologists design a design-based strategy for the employment rate, calibrated to population totals by age × sex × region, with a variance estimator that accounts for the survey design and for the income/non-response imputation flagged in VS-03. Target parameters, domains (national and NUTS-2), coherence criteria with prior quarters, and the disclosure-control policy for small cells are specified.

**Implementation Phase:** Engineers configure the GREG calibration engine (pinned register totals), the estimation engine, and a replication-based variance component that inflates variance for imputed values; they implement coherence checks against prior quarters and small-cell suppression. Reproducibility and back-series tests pass; accuracy measures match expectations on test data.

**Execution Phase:** For Q3-2026, a Processed Data Registered event arrives. The approach and calibration totals are confirmed; calibration converges and weighted margins reproduce the register. The employment rate is estimated at 71.4% (95% CI ±0.5pp national, wider at NUTS-2), with variance inflated for imputation. Coherence checks against Q2 pass; small NUTS-2 cells are suppressed by SDC. An output version is created with methodology, weights, and accuracy, and registered; VS-05.0 is notified.

**Management Phase:** Average CV for key estimates is stable, the coherence-check pass rate is 100%, and the preliminary-vs-final revision is within tolerance. Reproducibility audit confirms the figures regenerate from inputs + methodology. Improvement recommendations: add an auxiliary variable to the calibration to reduce variance for youth-employment estimates. Recommendations fed back to design.

#### Scenario B: Tax Register to Business Statistics (Register-Based + Small-Area Estimation)

**Design Phase:** The team designs register-based aggregation of turnover and employment by NACE × region, and a small-area model for domains where direct aggregates are unstable. Accuracy measures, coherence criteria with national accounts inputs, and disclosure control for dominant-unit cells are specified.

**Implementation Phase:** Engineers build the aggregation pipeline (designed domains, units, rounding), the small-area model with its diagnostics, and dominance-rule suppression for confidentiality. Reproducibility and benchmark tests against the prior year pass; the small-area model's prediction intervals are verified.

**Execution Phase:** Q3-2026: a Processed Data Registered event arrives for the integrated business dataset. Aggregates are computed by NACE × region; unstable small domains are estimated with the small-area model and flagged distinctly from direct aggregates. Dominant-unit cells are suppressed by SDC. Coherence with national-accounts inputs is checked. `OD-BUS-2026Q3-001` is created with methodology and accuracy, linked to `PD-BUS-2026Q3-001`, and VS-05.0 is notified.

**Management Phase:** Coherence with national accounts is within tolerance; revision analysis shows stable estimates; the small-area model fit is monitored across cycles. Disclosure-control report confirms no dominant-unit disclosure. Improvement recommendation: recalibrate the small-area model after two more cycles of data. Recommendations fed back to design.

#### Scenario C: Web-Scraped Price Data (Index Estimation)

**Design Phase:** The team designs the price-index estimation (e.g., a GEKS or Törnqvist multilateral index) over the COICOP items coded in VS-03, with quality-adjustment treatment, an approach for new/disappearing products, and coherence criteria against the official CPI. The disclosure policy is light (aggregated indices), and the accuracy approach for the index is specified.

**Implementation Phase:** Engineers build the index estimator, the new/disappearing-product handling, and seasonal/quality adjustment, plus coherence checks against the official CPI. Reproducibility and back-series tests pass; the index is benchmarked against the official series on historical data.

**Execution Phase:** For the monthly run, a Processed Data Registered event arrives. The multilateral index is computed over COICOP items using the carry-forward-imputed daily prices flagged in VS-03 (their uncertainty noted), new products are chained in, and the index is validated for coherence against the official CPI movement. An output version with methodology and accuracy is created and registered; VS-05.0 is notified.

**Management Phase:** The scraped index tracks the official CPI within the agreed tolerance; revision magnitude is small. Reproducibility audit passes. Improvement recommendations: refine the new-product chaining rule for one volatile category, and evaluate a longer multilateral window. Recommendations fed back to design.

## VS-05.0 Statistical Product Composition

### Purpose and Scope

This document specifies the complete business layer for the **Statistically composed and composite statistical products** business domain, corresponding to the *VS-05.0 Statistical Product Composition Value Stream*. It also covers 4 governance process types:

- **Design** — how composite products, indicators, and coherence checks are specified and planned (produces metadata)
- **Implementation** — how the composition pipeline is built, configured, and tested (produces the execution process)
- **Execution** — how outputs are operationally integrated, composed, checked, and registered (produces statistical data)
- **Management** — how the domain is monitored, quality-assessed, and improved (produces quality reports)

::: {.callout-warning title="Out of Scope"}
Application and Technology layer specifications are out of scope for this document. Re-estimation, weighting, and model-based analysis are out of scope — they belong to VS-04.0 Estimation, Analysis, and Statistical Modeling; VS-05 composes existing validated outputs, it does not re-estimate them. Publishing, distribution, and user services are out of scope — they belong to VS-06.0 Dissemination and Service Delivery.
:::





*A note on numbering:* each `VS-0x.y` below is both a value stream stage (*what value* is added) and a business process (*how* it is done); the numbering maps one-to-one. See the key-concepts box above.



### Position in the Statistical Value Chain

VS-05.0 is the fifth primary value stream — it receives Output Data (validated statistics) from VS-04.0 and brings multiple analytical results together into coherent, high-value statistical products ready for dissemination. It is the "Compose & Approve Products" orchestration stage where separate analyses become finished statistical products.

```{mermaid}
%%| label: fig-1
%%| fig-cap: "Value Stream Context Map. VS-05.0 is highlighted as the composition stage that turns validated analytical outputs into approved statistical products."
%%| fig-width: 6


flowchart TD
    subgraph primary["Primary Value Streams"]
        direction LR
        VS01["VS-01.0
        Data Acquisition
        & Ingestion"]
        VS02["VS-02.0
        Data Standardization
        & Integration"]
        VS03["VS-03.0
        Data Editing
        & Enrichment"]
        VS04["VS-04.0
        Estimation, Analysis
        & Modeling"]
        VS05["**VS-05.0**
        Statistical Product
        Composition"]:::highlight
        VS06["VS-06.0
        Dissemination
        & Service Delivery"]
        VS01 --> VS02 --> VS03 --> VS04 --> VS05 --> VS06
    end

    subgraph supporting["Supporting Value Streams"]
        VS07["VS-07.0
        Governance &
        Compliance"]
        VS08["VS-08.0
        Innovation &
        Methodology"]
        VS09["VS-09.0
        Infrastructure &
        Platform Enablement"]
        VS10["VS-10.0
        Customer &
        Stakeholder Engagement"]
    end

    supporting -.->|"enables"| primary

    classDef highlight fill:#2563eb,color:#fff,stroke:#1d4ed8,stroke-width:3px
```

### Steady State Transition

VS-05.0 operates **within Steady State #4 (Output Data / Statistics)**. It receives individual validated analytical outputs (the estimation form of State #4 produced by VS-04.0) and produces **approved, registered composite statistical products** (the final-product form of State #4) — coherent across sources and time, validated against dissemination and confidentiality standards, and ready to hand to dissemination. State #4 is shared between the estimation domain (VS-04) and this composition domain (VS-05).

```{mermaid}
%%| label: fig-2
%%| fig-cap: "Steady State Transition within State #4: from individual analytical outputs to approved, registered composite statistical products."
%%| fig-width: 6
flowchart LR
    subgraph upstream["Upstream Domain (VS-04.0)"]
        OD["Output Data / Statistics
        (State #4 — analytical outputs)"]
    end

    subgraph boundary["Composition Boundary"]
        QG["Composition Service
        (Integrate outputs, Construct composites,
        Coherence checks, Interpret, Approve & register)"]
    end

    subgraph internal["Product Domain (VS-05.0)"]
        SP["Statistical Products
        (State #4 — approved & registered)"]
    end

    OD --> QG --> SP

    style internal fill:#2563eb,color:#fff,stroke:#1d4ed8,stroke-width:3px
    style upstream fill:#7d7d7d,color:#fff,stroke:#1d4ed8,stroke-width:1px
    style boundary fill:#FFF,stroke-dasharray:5,5

```

::: {.callout-tip title='Product approval criteria (Examples)*'}
- Source outputs selected and integrated with their accuracy/methodology metadata preserved
- Composite indicators, indices, and time series constructed per documented specifications
- Internal consistency and coherence with related and prior products verified
- Analytical and interpretive content (commentary, visualizations) produced and reviewed
- Product validated against dissemination and confidentiality standards
- Approved by the designated authority and registered with a unique product identifier
- Full lineage from the product back to its component State #4 outputs and the composition method
:::

::: {.callout-important title="The composition discipline — coherence and interpretability"}
VS-05 does not re-estimate; it **composes** validated outputs into products. The guarantee here is **coherence and interpretability**: composite products are internally consistent, methodologically sound, coherent with related and prior statistics, and accompanied by the metadata and interpretation users need. Every product carries lineage to its component outputs and the composition method, and is **approved against dissemination and confidentiality standards** before it is registered.
:::

::: {.callout-note title="Inherited from VS-04.0"}
VS-05 receives Output Data **plus** the metadata VS-04 attached — methodology, weights, accuracy measures (sampling error, confidence intervals), and the record of the disclosure control already applied. VS-05 **propagates** this accuracy and quality metadata into the composite product (it does not discard or recompute it), uses it to weight or caveat composed figures, and runs coherence checks across the combined outputs. Composition never silently changes a component estimate; any adjustment for coherence is documented and traceable.
:::


### The Four-Process Governance Pattern



```{mermaid}
%%| label: fig-3
%%| fig-cap: "The Four-Process Governance Pattern. Each process type produces a distinct artefact class. The cycle closes when Management findings feed back into Design improvements."
%%| fig-width: 6
flowchart LR
    D["**Design**
    _provides metadata_

    Product specs, composite-indicator
    definitions, coherence & approval policy"]
    I["**Implement**
    _provides the execution process_

    Configured integration & composition
    pipelines, coherence-check & approval tooling"]
    E["**Execute**
    _provides the statistical data_
    Composed products, coherence results,
    interpretive content, approval records"]
    M["**Manage**
    _provides quality reports_
    Coherence & interpretability dashboards,
    product-quality scorecards, improvement recommendations"]

    D -->|"design artefacts
    guide building"| I
    I -->|"production-ready
    process"| E
    E -->|"data & process logs
    for assessment"| M
    M -->|"improvement
    feedback"| D

    style D fill:#7c3aed,color:#fff,stroke:#6d28d9
    style I fill:#2563eb,color:#fff,stroke:#1d4ed8
    style E fill:#059669,color:#fff,stroke:#047857
    style M fill:#d97706,color:#fff,stroke:#b45309
```




### Governing Principles

The following principles directly govern the VS-05.0 business domain:

| Principle | Statement | Application to VS-05.0 |
|---|---|---|
| **SAF-P01** | Actively participate in open source to maintain collective control over statistical processes | NSOs should contribute to open source communities for composition, indicator-construction, and reporting/visualization tooling, ensuring collective control over critical product capabilities rather than vendor dependence. |
| **SAF-P07** | Implement loosely coupled processes and systems | The composition domain must be independent from upstream estimation and downstream dissemination. The approved statistical product serves as a decoupling interface — dissemination accesses it without knowledge of how it was composed. |
| **SAF-P08** | Data is shared property | Approved statistical products and their components, once registered, are available to all authorized consumers. Composition should reuse existing validated outputs rather than duplicate analysis. |
| **SAF-P09** | No data without metadata and classification | Every composite product carries metadata: its component outputs and their accuracy, the composition/indicator methodology, coherence-check results, classification, and the approval record. This is what makes products interpretable and trustworthy. |
| **SAF-P10** | Security By Design | Access controls, integrity verification, and a tamper-evident composition and approval record are embedded in the pipeline so that every product is attributable and reproducible, not added as an afterthought. |
| **SAF-P11** | Privacy By Design | Composition is validated against confidentiality standards, and the disclosure risk of composite products (including the risk of combining outputs) is assessed by design, before registration. |

::: {.callout-note title="Cross-cutting principle application"}
Several principles cut across all four process types. SAF-P09 (no data without metadata and classification) underpins interpretability: Design defines the product and required metadata, Execute captures component lineage, composition method, and coherence results, and Manage assesses product quality. SAF-P10 (Security By Design) governs the tamper-evident approval/composition record across Execution (Sections 5.1–5.5). SAF-P11 (Privacy By Design) applies especially to approval (Section 5.5), where the composite product's confidentiality and disclosure risk are confirmed before registration. SAF-P07 (loosely coupled) governs both the State #4 intake interface from VS-04.0 and the handover interface to VS-06.0.
:::

### Capability Foundations

VS-05.0 draws on the following SAF capabilities:

| Capability Group | Capabilities | Role in VS-05.0 |
|---|---|---|
| **1.1 Statistical design and build** | 1.1.2 Design statistics product, 1.1.3 Build statistics product | Design the statistical products and composite indicators, and build the composition pipeline |
| **2.1 Data management** | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management, 2.1.4 Statistical register management | Manage products, metadata, and quality; assess coherence; integrate across registers and time |
| **3.2 Computerization and automation** | 3.2.1 Application development, 3.2.2 Functional management | Build and maintain integration, indicator-construction, and reporting/visualization engines |
| **3.3 Security and Privacy** | 3.3.1 Privacy management, 3.3.2 Security planning | Validate products against confidentiality standards and assess composite disclosure risk |
| **4.1 Governance** | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improve management, 4.1.5 Accountability | Govern the domain, steward product approval, plan improvements, report on compliance |

### Metadata Perspective

It is considered that metadata is an essential product of the Design phase and a critical concern of every other phase. In this domain, metadata is what makes a composite product interpretable: each product must carry its components, methodology, coherence results, and approval. The table below consolidates the metadata produced across all four process types, covering both data metadata (about the products) and process metadata or paradata (about how the process runs).

| Process Type | Data Metadata Produced | Process Metadata (Paradata) Produced |
|---|---|---|
| **Design** | Product specifications, composite-indicator definitions, coherence criteria, approval & confidentiality policy | Design decisions log, methodology version, review and approval records |
| **Implement** | Integration configurations, indicator-construction parameters, coherence-check parameters, product templates | Build log, test results, coherence-test outcomes, deployment approvals |
| **Execute** | Per-product component lineage, composition/indicator method, coherence-check results, interpretive content, approval record | Operator identity, timing, software/version, approval workflow trail |
| **Manage** | Coherence & interpretability assessments, product-quality scores, lineage assessments, trend analyses | Coherence dashboards, product-quality trends, improvement decisions, audit findings |


## Business Roles and Actors



| Role                        | Process Orientation | Description                                                                                       |
|-----------------------------|---------------------|---------------------------------------------------------------------------------------------------|
| **Upstream Data Provider (VS-04.0)** | External (internal NSO) | Supplies Output Data (State #4) with methodology/accuracy metadata to the composition domain |
| **Standards Body**          | External            | Maintains product, indicator, and exchange standards the NSO conforms to (e.g., SDMX, index manuals) |
| **Product Manager**         | Design              | Designs the statistical product portfolio, product specifications, and release content             |
| **Indicator/Index Methodologist** | Design        | Specifies composite indicators, indices, and time-series construction methods                       |
| **Coherence Designer**      | Design              | Designs the consistency and coherence checks across sources and time                               |
| **Data Engineer**           | Implementation      | Builds and configures integration, indicator-construction, and reporting engines and the pipeline  |
| **System Configurator**     | Implementation      | Configures composition services, output-source connections, and access controls                   |
| **Test Manager**            | Implementation      | Plans and executes testing of the composition pipeline (technical, coherence, reproducibility)     |
| **Process Owner**           | Management          | Accountable for the end-to-end performance of the composition domain                               |
| **Compliance Officer**      | Management          | Ensures confidentiality and standards compliance of products, produces audit reports               |
| **Quality Manager**         | Management          | Monitors coherence/interpretability KPIs, produces quality reports, and drives continuous improvement |
| **Integration Specialist**  | Execution           | Selects and integrates the component outputs into the product structure                            |
| **Subject-Matter Author**   | Execution           | Produces analytical and interpretive content, commentary, and visualizations                       |
| **Approval Authority**      | Execution           | Validates products against standards and approves them for registration and release                |
| **Data Steward**            | Execution           | Registers approved products and versions, manages metadata entries, and applies access controls    |



## Design Processes — "provides metadata"

*Framework alignment: GSBPM Phases 1–2 — see [Framework Mappings](#framework-mappings).*

The design phase produces the **metadata artefacts** that govern all subsequent phases — the product specifications, composite-indicator definitions, coherence checks, and the approval and confidentiality policy. Without well-designed product specs, composition becomes ad-hoc and incoherent, and management has no baseline to measure coherence and interpretability against.

### Design the Statistical Product Portfolio

The starting point is defining what products will be produced. This sub-process specifies each statistical product — its purpose, target users, content, structure, breakdowns, release frequency, and the set of component State #4 outputs it draws on. The team designs how component outputs are selected and integrated (which estimates, which domains, which time periods) and how their accuracy metadata is carried into the product, aligned with GSBPM 2.5 (Design processing and analysis).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Specify each product: purpose, users, content, structure, breakdowns, frequency | Product Specification | GSBPM 2.1 |
| Define the component outputs each product draws on and selection rules | Component-Selection Specification | GSBPM 2.5 |
| Define how component accuracy/quality metadata is carried into the product | Metadata-Propagation Rules | SAF-P09 |
| Define product classification and versioning identity | Product Metadata Standard | SAF-P09 |

::: {.callout-tip title="**NSO Example — Labour Market Publication:**"}
The labour-market quarterly publication is specified to combine the LFS employment-rate estimates (national and NUTS-2), the unemployment series, and administrative job-vacancy figures into a single coherent release, carrying each component's confidence intervals into the published tables.
:::


### Design Composite Indicators and Indices

This sub-process specifies the derived measures the products present — composite indicators, indices, ratios, and time-series aggregates. Each is defined by its formula, component inputs, weighting/aggregation method, base period, and chaining/linking rules for time series, together with the metadata and classification it carries. Where a composite combines outputs of differing accuracy, the design specifies how uncertainty is represented, aligned with GSBPM 2.5.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Specify composite indicators/indices: formula, inputs, weighting, base period | Composite-Indicator Specification | GSBPM 2.5 |
| Specify time-series construction: chaining, linking, benchmarking | Time-Series Specification | GSBPM 2.5 |
| Define how component uncertainty is represented in composites | Uncertainty-Representation Rules | SAF-P09 |
| Define metadata and classification for each composite | Composite Metadata Standard | SAF-P09 |

### Design Consistency and Coherence Checks

This sub-process designs the checks that ensure integrated products are sound. It specifies internal-consistency checks (totals reconcile to components, breakdowns sum to totals), coherence checks against related statistics (e.g., national accounts, prior products) and across time, and the tolerance thresholds and disposition rules (accept, flag, return for review). The revision policy for products is also designed here, aligned with GSBPM 2.5 and GAMSO Quality Management.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define internal-consistency checks (totals, breakdowns reconcile) | Consistency Check Set | GSBPM 2.5 |
| Define coherence checks vs. related statistics and across time | Coherence Check Set | GAMSO QM |
| Define tolerance thresholds and disposition rules | Coherence Tolerance Policy | GSBPM 2.5 |
| Define product revision policy | Revision Policy | GAMSO QM |

### Design Analytical and Interpretive Content

This sub-process designs the human-facing content that makes products interpretable. It specifies the analytical narrative and commentary structure, the visualizations and tables, the key messages and their evidence, and the editorial/quality-review workflow for interpretive content. Accessibility and plain-language standards are designed in, aligned with GSBPM 2.5.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Specify analytical narrative and commentary structure | Content Template | GSBPM 2.5 |
| Specify visualizations and tables | Visualization Specification | GSBPM 2.5 |
| Define key messages and evidence requirements | Key-Message Guidelines | GSBPM 2.5 |
| Define editorial and quality-review workflow for content | Editorial Review Policy | GAMSO QM |

### Design Approval, Confidentiality, and Versioning Framework

The final design sub-process ensures products are properly approved, protected, and traceable. It defines the approval workflow and authority, the confidentiality/disclosure standards a product must meet before registration (including the risk of combining outputs), the product-versioning policy (identity, revision triggers, immutability, retention), the lineage requirements from each product to its component outputs, and the role-based access controls in line with SAF-P10.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define approval workflow and authority | Approval Policy | SAF 4.1.5 |
| Define confidentiality/disclosure standards for products (incl. combination risk) | Confidentiality Standard | SAF-P11 |
| Define product-versioning and lineage requirements | Versioning & Lineage Policy | CSDA Traceability |
| Design role-based access control for products | Access Control Design | SAF-P10 |

```{mermaid}
%%| label: fig-4
%%| fig-cap: "Design Process Decomposition. Output data with accuracy, user needs, and product standards flow into five design sub-processes, producing metadata artefacts that govern Implementation, Execution, and Management."
%%| fig-width: 6
flowchart TB
    subgraph inputs["Inputs"]
        OM["Output Data + accuracy<br/><small>(State #4 from VS-04)</small>"]
        FW["Framework Standards<br/><small>GSBPM · GAMSO · CSDA</small>"]
        STD["Product & Index Standards<br/><small>SDMX · index manuals</small>"]
        USR["User Needs"]
    end

    subgraph design["Design Sub-Processes"]
        D1["3.1 Product<br/>Portfolio"]
        D2["3.2 Composite<br/>Indicators & Indices"]
        D3["3.3 Consistency &<br/>Coherence Checks"]
        D4["3.4 Analytical &<br/>Interpretive Content"]
        D5["3.5 Approval, Confidentiality<br/>& Versioning"]
    end

    subgraph outputs["Metadata Artefacts"]
        O1["Product Specifications"]
        O2["Composite-Indicator Specs"]
        O3["Coherence Check Set"]
        O4["Content Templates"]
        O5["Approval & Versioning Policy"]
    end

    OM --> D1
    USR --> D1
    FW -.->|inform| design
    STD --> D2

    D1 --> D2 --> D3 --> D4 --> D5

    D1 --> O1
    D2 --> O2
    D3 --> O3
    D4 --> O4
    D5 --> O5

    outputs -->|govern| NEXT["Implementation (§4) · Execution (§5)<br/>measured by Management (§6)"]

    style design fill:#f5f3ff,stroke:#7c3aed
    style outputs fill:#ede9fe,stroke:#7c3aed
```

## Implementation Processes — "provides the execution process"

*Framework alignment: GSBPM Phase 3 (Build) — see [Framework Mappings](#framework-mappings).*

The implementation phase takes the metadata artefacts from Design and **builds, configures, and tests** the production-ready composition pipeline. Nothing runs operationally until this phase is complete.

### Build Integration and Composition Engines

This sub-process turns the product and integration designs into operational tools. The integration engine is built or configured to select and combine the designed component outputs into the product structure, carrying their accuracy/quality metadata. The composition engine is built to assemble products from their components per the specifications. Output-source connections are configured to the State #4 catalog with version pinning so the exact component versions used are recorded. All composition logic is version-controlled in line with SAF-P10, following GSBPM 3.1–3.2.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Build/configure the integration engine (select and combine component outputs) | Configured integration engine | GSBPM 3.2 |
| Build/configure the composition engine (assemble products from components) | Configured composition engine | GSBPM 3.2 |
| Configure pinned connections to the State #4 output catalog | Output-source integration | CSDA Metadata Mgmt |
| Version-control all composition logic | Versioned composition repository | SAF-P10 |

::: {.callout-tip title="**NSO Example — Business Statistics Product:**"}
The SBS composite product engine is configured to integrate the register-based aggregates and the survey-based estimates for the same NACE × region domains, pinning the exact `OD-BUS` output versions and carrying their accuracy metadata into the combined tables.
:::

### Build Indicator-Construction and Time-Series Engines

The designed composite-indicator and time-series specifications are implemented. Indicator/index calculators are built from the designed formulae and weighting, time-series engines are configured for chaining, linking, and benchmarking, and uncertainty representation is implemented so composites carry an appropriate measure of accuracy. Every composite output is produced with its method and inputs attached, following GSBPM 3.2.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Build indicator/index calculators from designed formulae | Indicator-construction engine | GSBPM 3.2 |
| Configure time-series chaining, linking, and benchmarking | Time-series engine | GSBPM 3.2 |
| Implement uncertainty representation for composites | Composite-accuracy component | SAF-P09 |
| Attach method and inputs to every composite | Composite metadata binding | SAF-P09 |

### Build Coherence-Check, Content, and Approval Tooling

This sub-process implements the consistency/coherence checks, the content-production tooling, and the approval/versioning store. Coherence tooling implements the designed internal-consistency and cross-source/time checks with their tolerances. Content tooling supports the analytical narrative, tables, and visualizations per the templates, with the editorial review workflow. The approval-and-versioning store is built so each approved product version is immutable, identified, reproducible from its components plus method, and accompanied by its lineage and approval record. Event notifications are configured to alert downstream consumers (VS-06.0) when a product is approved and registered.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Implement coherence/consistency checks with tolerances | Coherence tooling | GSBPM 3.2 |
| Build content/visualization tooling with editorial workflow | Content tooling | GSBPM 3.2 |
| Build the approval-and-versioning store (immutable, identified, reproducible) | Approval & versioning store | CSDA Traceability |
| Configure "Statistical Product Registered" event for downstream consumers | Event publication | GSBPM 3.2 |

### Test and Validate the Pipeline

Before the pipeline goes into production, it must be rigorously verified. Technical testing covers all components — integration, composition, indicator/time-series engines, coherence checks, content tooling, and the approval store (GSBPM 3.5). Integration testing validates the end-to-end flow from output intake through composition, coherence checks, content, approval, to registration. A **coherence test** confirms composites reconcile to components and cohere with prior products; a **reproducibility test** confirms a product regenerates identically from its component versions plus the composition method. The phase concludes with finalization of the production system and documentation of operational procedures (GSBPM 3.6–3.7).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Technical testing of all individual components | Unit test reports | GSBPM 3.5 |
| Integration testing: end-to-end flow from output intake to registration | Integration test report | GSBPM 3.5 |
| Coherence test (composites reconcile to components and prior products) | Coherence test report | GSBPM 3.6 |
| Reproducibility test (regenerate a product from components + method) | Reproducibility report | GSBPM 3.6 |
| Finalize production system and document operational procedures | Operational Procedures Manual, Production-Ready Pipeline | GSBPM 3.7 |

```{mermaid}
%%| label: fig-5
%%| fig-cap: "Implementation Pipeline from design artefacts through build/configure/test to production-ready system."
%%| fig-width: 6
flowchart LR
    subgraph design_artefacts["Design Artefacts (from Section 3)"]
        DA1["Product\nSpecifications"]
        DA2["Composite-Indicator\nSpecs"]
        DA3["Coherence\nCheck Set"]
        DA4["Content\nTemplates"]
        DA5["Approval &\nVersioning Policy"]
    end

    subgraph build["Build & Configure"]
        B1["4.1 Build Integration\n& Composition Engines"]
        B2["4.2 Build Indicator\n& Time-Series Engines"]
        B3["4.3 Build Coherence,\nContent & Approval"]
    end

    subgraph test["Test & Validate"]
        T1["4.4 Technical\nTesting"]
        T2["4.4 Coherence\nTest"]
        T3["4.4 Reproducibility\nTest"]
    end

    subgraph output["Production-Ready"]
        PR["Operational\nComposition\nPipeline"]
        OP["Operational\nProcedures"]
    end

    DA1 --> B1
    DA2 --> B2
    DA3 & DA4 & DA5 --> B3

    B1 & B2 & B3 --> T1 --> T2 --> T3
    T3 --> PR & OP

    PR -->|"ready for"| EXEC["Execution\n(Section 5)"]

    style build fill:#eff6ff,stroke:#2563eb
    style test fill:#dbeafe,stroke:#2563eb
```

## Execution Processes — "provides the statistical data"

*Framework alignment: the later GSBPM phases for this domain — see [Framework Mappings](#framework-mappings).*

The execution phase runs the **designed and implemented pipeline** operationally for each production cycle. This corresponds to the five VS-05 value stream stages. In a mature steady state, much of the work has been pre-designed (Section 3) and pre-built (Section 4) — execution focuses on running the cycle, composing products, checking coherence, and capturing component lineage and approval so that every product is coherent, interpretable, and reproducible.

### Select and Integrate Source Datasets

**Value created:** *The right validated outputs brought together as the basis for a coherent product.*

When an "Output Data Registered" event is received from VS-04.0, execution begins by selecting and integrating the component outputs for the product. Per-cycle execution applies the designed selection rules to pick the correct State #4 output versions (by domain, period, and accuracy), integrates them into the product structure, and carries their accuracy/methodology metadata forward. Components from multiple domains, surveys, or time periods are combined per the specification, aligned with GSBPM 7.1/7.2.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Select the correct component output versions per the specification | Selected components | GSBPM 7.1 |
| Integrate components into the product structure | Integrated product base | GSBPM 7.2 |
| Carry component accuracy/methodology metadata into the product | Propagated metadata | SAF-P09 |
| Record component lineage (which output versions were used) | Component lineage | CSDA Traceability |

::: {.callout-tip title="**NSO Example — Labour Market Publication:**"}
For Q3-2026 the team selects the validated `OD-LFS-2026Q3` employment and unemployment outputs (national and NUTS-2) and the latest administrative vacancy output, pinning their exact versions and carrying their confidence intervals into the integrated product base.
:::

### Construct Composite Indicators or Indices

**Value created:** *Derived measures — indices, ratios, time series — that summarize and add meaning.*

This sub-process computes the designed composite indicators, indices, and time-series aggregates from the integrated components, aligned with GSBPM 7.2. Indicators and indices are calculated per the designed formulae and weighting; time series are chained, linked, and benchmarked per the specification; and each composite carries an appropriate uncertainty measure derived from its components. No component estimate is re-estimated — composites are built from the validated outputs as received.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Calculate composite indicators/indices per designed formulae | Composite indicators | GSBPM 7.2 |
| Construct time series (chain, link, benchmark) | Composite time series | GSBPM 7.2 |
| Derive composite uncertainty from component accuracy | Composite accuracy measures | SAF-P09 |
| Record composition method and inputs as lineage | Composite lineage | SAF-P09 |

::: {.callout-tip title="**NSO Example — CPI Headline Index:**"}
The headline CPI is composed from the validated item indices using the designed weighting and chaining; the all-items index and its main divisions are constructed, with each carrying its method and the period weights used.
:::

### Perform Consistency and Coherence Checks

**Value created:** *Confidence that the product is internally consistent and coheres with the wider statistical picture.*

This sub-process runs the designed checks, aligned with GSBPM 6.2 (Validate outputs). Internal-consistency checks confirm totals reconcile to components and breakdowns sum to totals; coherence checks compare the product against related statistics and prior releases within the designed tolerances. Discrepancies are dispositioned per policy — accepted, flagged, or returned for review — and explained where significant. No silent adjustment is made: any reconciliation is documented and traceable.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Run internal-consistency checks (totals, breakdowns reconcile) | Consistency results | GSBPM 6.2 |
| Run coherence checks vs. related and prior statistics | Coherence results | GSBPM 6.2 |
| Disposition discrepancies (accept / flag / return) and explain | Discrepancy dispositions | GSBPM 6.2 |
| Log all check results to the product audit trail | Audit trail entries | SAF-P10 |

```{mermaid}
%%| label: fig-6
%%| fig-cap: "Composition and Coherence Architecture. Component outputs are integrated and composed into indicators, then checked for internal consistency and coherence against prior products before becoming a coherent product carrying its lineage and accuracy."
%%| fig-width: 6
flowchart LR
    subgraph components["Component outputs (State #4)"]
        direction TB
        C1["Domain A\nestimates"]
        C2["Domain B\nestimates"]
        C3["Prior-period\nproducts"]
    end

    subgraph compose["Compose & Check"]
        INT["Integrate"]
        IDX["Construct\ncomposites"]
        COH["Coherence &\nconsistency checks"]
    end

    subgraph product["Statistical Product"]
        P["Coherent product\n(+ lineage + accuracy)"]
    end

    C1 --> INT
    C2 --> INT
    INT --> IDX --> COH --> P
    C3 -.->|"coherence\ncomparison"| COH

    style components fill:#ecfdf5,stroke:#059669
    style compose fill:#f0fdf4,stroke:#059669
```


::: {.callout-tip title='**NSO Example — Business Statistics Product:**'}
The composite SBS product is checked: NACE-class turnover sums to the published total, the survey- and register-based components agree within tolerance for overlapping domains, and the series is coherent with the prior year; one domain exceeds tolerance and is returned to VS-04 for review rather than silently adjusted.
:::


### Generate Analytical and Interpretive Outputs

**Value created:** *Products users can understand — narrative, key messages, and visualizations grounded in the data.*

This sub-process produces the human-facing content, aligned with GSBPM 6.3 (Interpret and explain outputs). The analytical narrative and commentary are written per the templates, key messages are stated with their supporting evidence, and tables and visualizations are produced. Content passes the editorial and quality-review workflow to ensure it is accurate, plain-language, accessible, and consistent with the data and its caveats (including the accuracy carried from VS-04).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Write analytical narrative and commentary per templates | Product narrative | GSBPM 6.3 |
| State key messages with supporting evidence | Key messages | GSBPM 6.3 |
| Produce tables and visualizations | Visualizations & tables | GSBPM 6.3 |
| Run editorial and quality review of content | Reviewed content | GAMSO QM |

::: {.callout-tip title="**NSO Example — Labour Market Publication:**"}
The quarterly commentary explains the 0.3pp rise in the employment rate, notes it is within the confidence interval, and presents a regional map and a time-series chart; the editorial review confirms the wording does not overstate a movement that is not statistically significant.
:::

### Approve and Register Statistical Products

**Value created:** *A validated, approved, registered product ready for dissemination.*

The final execution sub-process validates, approves, and registers the product, aligned with GSBPM 6.5 (Finalise outputs) and 7.1. The product is validated against the dissemination and confidentiality standards (including the disclosure risk arising from combining outputs), submitted to the designated approval authority, and — on approval — a persistent immutable product version is created with a unique identifier and full lineage (components, method, coherence results, approval record), registered per SAF-P09, with access permissions applied per SAF-P10. The sub-process concludes by publishing a "Statistical Product Registered" event, notifying downstream VS-06.0 that an approved product is available for dissemination.

**Output:** **Approved Statistical Product (Steady State #4)** — the official handover artefact to the dissemination domain.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Validate the product against dissemination and confidentiality standards | Validation result | GSBPM 6.5 |
| Submit to and obtain sign-off from the approval authority | Approval record | SAF 4.1.5 |
| Create an immutable, identified product version with full lineage | Versioned product | CSDA Traceability |
| Register metadata and publish "Statistical Product Registered" event to notify VS-06.0 | Catalog registration, event | SAF-P07 |

```{mermaid}
%%| label: fig-7
%%| fig-cap: "Statistical Product Artefact Structure. Reading guide: each box is a type of record with its fields; a connecting line means the records are linked. Each product version is linked to its component lineage, coherence results, interpretive content, and approval record, all traceable to the State #4 outputs it was composed from."
%%| fig-width: 6
erDiagram
    STATISTICAL_PRODUCT {
        string product_id PK "Unique persistent URI/UUID"
        string product_version "Immutable version identifier"
        string product_type "Publication / index / time series / dataset"
        date reference_period "Reference period"
        datetime registration_timestamp "When registered in catalog"
    }
    COMPONENT_LINEAGE {
        string component_output_id "State #4 output version used"
        string domain "Domain / source of the component"
        string composition_method "How it was combined"
        string accuracy_carried "Accuracy metadata propagated"
    }
    COHERENCE_RESULT {
        boolean internally_consistent "Totals/breakdowns reconcile"
        boolean coherent_with_related "Coherent with related statistics"
        boolean coherent_over_time "Coherent with prior products"
        int discrepancies "Count of flagged discrepancies"
    }
    INTERPRETIVE_CONTENT {
        string narrative_ref "Commentary / analytical narrative"
        string key_messages "Key messages with evidence"
        string visualizations "Tables and charts"
        boolean editorial_passed "Editorial review completed"
    }
    APPROVAL_RECORD {
        string approver "Approval authority"
        boolean confidentiality_cleared "Meets confidentiality standard"
        datetime approved_at "Approval timestamp"
        boolean release_ready "Cleared for dissemination"
    }

    STATISTICAL_PRODUCT ||--|{ COMPONENT_LINEAGE : "composed from"
    STATISTICAL_PRODUCT ||--|| COHERENCE_RESULT : "validated by"
    STATISTICAL_PRODUCT ||--|| INTERPRETIVE_CONTENT : "explained by"
    STATISTICAL_PRODUCT ||--|| APPROVAL_RECORD : "approved by"
```

## Management Processes — "provides quality reports"

*Framework alignment: GSBPM overarching Quality/Metadata Management — see [Framework Mappings](#framework-mappings).*

The management phase runs **alongside and after** execution. It monitors the composition domain's performance, assesses the coherence and interpretability of products, ensures every product is approved and reproducible, and feeds improvement recommendations back into the design phase — closing the governance cycle.

### Monitor Process Performance

Operational performance of the composition domain must be tracked systematically across production cycles. The process owner and quality manager collect and aggregate key performance indicators, monitor throughput against the release calendar, and track paradata — which component versions and methods were used, when, by whom, and how many approval iterations occurred. This information feeds process performance dashboards that give the process owner a real-time view of domain health, aligned with the GAMSO Quality Management capability.

**Key Performance Indicators (KPIs):**

| KPI | Description | Measurement |
|---|---|---|
| On-time product rate | Products composed within the release-calendar window | Per product, per cycle |
| Coherence-check pass rate | Products passing coherence checks on first run | Per product, per cycle |
| Approval-iteration count | Number of approval cycles before sign-off | Per product, per cycle |
| Component reuse rate | Share of products reusing existing validated outputs | Per cycle |
| Reproducibility rate | Products regenerable from components + method | Per cycle |
| Processing time | Duration from output intake to product registration | Per product, per cycle |

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Collect and aggregate KPIs per production cycle | Process Performance Dashboard | GAMSO QM |
| Monitor throughput against the release calendar | Throughput Report | GAMSO QM |
| Track paradata: component versions, methods, approval iterations | Paradata Records | GAMSO QM |
| Generate process performance dashboards | Dashboard for Process Owner | GAMSO QM |

### Assess Product Quality

Beyond process performance, the quality of the products themselves must be evaluated against the criteria established in design. Each product is assessed across multiple quality dimensions: coherence (internal consistency and consistency with related and prior statistics), interpretability (clarity and accuracy of narrative and visualizations), completeness (all designed content present), and accuracy propagation (component accuracy correctly carried). Results are compared against the designed quality criteria from Section 3.5. Quality indicators are produced per product and per cycle, and trends are tracked to detect recurring coherence issues or interpretive weaknesses. This aligns with the CSDA Data Quality capability and SAF Capability 2.1.3.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Evaluate coherence (internal and with related/prior statistics) | Coherence Report (per cycle) | SAF 2.1.3 |
| Assess interpretability of narrative and visualizations | Interpretability Review | CSDA Data Quality |
| Check completeness and correct accuracy propagation | Product Completeness Report | SAF 2.1.3 |
| Identify quality trends across products and cycles | Quality Trend Analysis | SAF 2.1.3 |

### Manage Product and Version Lifecycle

The product portfolio and the versions it produces must remain current, complete, and well-governed. This sub-process governs the lifecycle of product specifications, composite-indicator definitions, and content templates — versioning them, managing transitions (e.g., an index rebasing), and retiring obsolete products. It verifies metadata completeness — that every product carries full component lineage, composition method, coherence results, and approval as an SAF-P09 compliance check — and governs the product-version store: retention, immutability, and reconciliation that catalog entries match stored versions. Metadata lineage from outputs through composition to products is tracked.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Govern product, indicator, and template lifecycle and versions | Product Version Register | SAF-P09 |
| Verify metadata completeness (component lineage, method, coherence, approval) | Metadata Quality Report | SAF-P09 |
| Govern the product-version store: retention, immutability, reconciliation | Version Store Audit | CSDA Traceability |
| Track metadata lineage from outputs to products | Metadata Lineage Audit | CSDA Traceability |

### Audit and Compliance Reporting

This sub-process produces the evidence that the composition domain operates within methodological, legal, and organizational requirements. Reproducibility-audit reports demonstrate that every product can be regenerated from its component versions plus the composition method — supporting transparency and accountability. Approval-and-confidentiality reporting confirms that every registered product was approved by the designated authority and meets the confidentiality standard, including the disclosure risk of combining outputs per SAF-P11. Standards compliance reporting confirms conformance to product and exchange standards (e.g., SDMX), and security compliance reporting verifies access controls and the integrity of the approval record. These reports satisfy the SAF Capability 4.1.5 (Accountability) obligation and feed into VS-07.0 Governance and Compliance.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Produce reproducibility-audit reports: every product regenerable | Reproducibility Audit Summary | SAF 4.1.5 |
| Report on approval and confidentiality compliance of products | Approval & Confidentiality Report | SAF-P11 |
| Report on standards compliance (products, SDMX exchange) | Standards Compliance Report | SAF 4.1.5 |
| Report on security compliance: access controls, approval-record integrity | Compliance Report (per cycle) | SAF-P10 |

### Continuous Improvement

The final management sub-process closes the governance loop by analyzing performance and quality data to identify and drive improvements. Quality trends across production cycles are examined: are coherence issues falling, are approval iterations shrinking, is component reuse rising, is interpretability improving? Improvement opportunities are identified — refining composite-indicator methods, improving coherence checks that generate false positives, streamlining the approval workflow, enhancing visualizations, and increasing reuse of validated outputs. These improvement recommendations are fed back to the design processes (Section 3), prioritized based on impact and feasibility, and tracked through subsequent design-implement-execute cycles. This is the SAF Capability 4.1.4 (Improve management) in action, and it connects to the GAMSO concept of transferring mature capabilities from innovation into production.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Analyze quality trends across production cycles | Improvement Recommendations Report | SAF 4.1.4 |
| Identify improvement opportunities: indicator methods, coherence checks, approval, visualization, reuse | Updated Design Inputs | SAF 4.1.4 |
| Feed recommendations back to design processes (Section 3) | Design feedback (closing the governance loop) | SAF 4.1.4 |
| Prioritize improvements based on impact and feasibility | Improvement Tracking Log | GAMSO Capability Mgmt |
| Track implementation of accepted improvements | Improvement Tracking Log | GAMSO Capability Mgmt |

```{mermaid}
%%| label: fig-8
%%| fig-cap: "Management Feedback Loop. Execution data flows through monitoring, quality assessment, product/version management, and audit processes. Continuous improvement feeds recommendations back to Design, closing the governance cycle."
%%| fig-width: 6
flowchart TD
    E["Execution\n(Section 5)<br/><em>data + paradata</em>"]

    M1["6.1 Monitor<br/>Process Performance<br/><em>coherence pass, timeliness</em>"]
    M2["6.2 Assess<br/>Product Quality<br/><em>coherence, interpretability</em>"]
    M3["6.3 Manage Product<br/>& Version Lifecycle<br/><em>products, versions</em>"]
    M4["6.4 Audit &<br/>Compliance Reporting<br/><em>reproducibility, approval</em>"]
    M5["6.5 Continuous<br/>Improvement<br/><em>recommendations</em>"]

    D["Design<br/>(Section 3)<br/><em>updated product specs</em>"]

    E --> M1
    E --> M2
    M1 --> M2
    M2 --> M3
    M3 --> M4
    M4 --> M5
    M5 -->|"feedback loop"| D

    M1 -->|"dashboards"| PO["Process Owner"]
    M2 -->|"quality reports"| QM["Quality Manager"]
    M4 -->|"compliance reports"| VS07["VS-07.0\nGovernance"]

    style E fill:#ecfdf5,stroke:#059669
    style D fill:#f5f3ff,stroke:#7c3aed
    style M5 fill:#fef3c7,stroke:#d97706
```

## Business Services and Interfaces

The VS-05.0 business domain exposes the following services:

| Service | Direction | Consumers | Mapped Processes |
|---|---|---|---|
| **Integration and Composition Service** | Internal (VS-04.0 → NSO) | Output data consumers, composition teams | 5.1 Select and Integrate Source Datasets |
| **Indicator and Index Service** | Internal | Composition teams, methodologists | 5.2 Construct Composite Indicators or Indices |
| **Coherence Validation Service** | Internal | Quality managers, subject-matter authors | 5.3 Perform Consistency and Coherence Checks |
| **Analytical Content Service** | Internal | Authors, editors, downstream dissemination | 5.4 Generate Analytical and Interpretive Outputs |
| **Product Provisioning Service** | Internal (NSO → VS-06.0) | Dissemination teams | 5.5 Approve and Register Statistical Products |
| **Product Catalog Service** | Internal | All data consumers across the NSO | 6.3 Manage Product & Version Lifecycle |
| **Design and Methodology Service** | Internal | Product managers, indicator methodologists | 3.1–3.5 All design processes |

**Interface specifications:**

- **Product Provisioning Service** interface: event-driven notification ("Statistical Product Registered") + catalog query API for downstream consumers to discover and access approved products, their lineage, and accuracy
- **Indicator and Index Service** interface: composite-construction API and a methodology/parameters query API
- **Product Catalog Service** interface: search/browse API for products, component lineage, coherence results, and approval records

### Boundary Interface Specifications

The domain is loosely coupled (SAF-P07) to its neighbors through two steady-state interfaces. Specifying each boundary explicitly — the handover artefact, the metadata it must carry, the event that triggers it, and where responsibility transfers — makes the loose-coupling contract concrete and testable.

| Boundary | Handover Artefact | Required Metadata | Trigger Event | Responsibility Transfer |
|---|---|---|---|---|
| **VS-04.0 → VS-05.0** (intake) | Output Data / Statistics (State #4) | Methodology and parameters, weights, accuracy measures, model diagnostics, applied-SDC record, output-version identifier, lineage to processed source, BIV classification | "Output Data Registered" event | VS-04.0 retains custody of the output version; VS-05.0 assumes responsibility for composing products on event receipt |
| **VS-05.0 → VS-06.0** (handover) | Approved Statistical Product (State #4) | Component lineage, composition/indicator method, propagated accuracy, coherence results, interpretive content, approval record, confidentiality status, product-version identifier, BIV classification | "Statistical Product Registered" event | VS-05.0 retains custody of the product version; VS-06.0 assumes responsibility for dissemination and service delivery on event receipt |

Each interface exchanges a registered, immutable steady-state artefact plus its metadata — never internal working data — so neither side needs knowledge of the other's internal processing.

## Business Objects and Data Flow

```{mermaid}
%%| label: fig-9
%%| fig-cap: "Business Object Lifecycle across all four process types. Design objects govern implementation, which produces the pipeline that composes execution objects into products, which are assessed by management objects, which feed back to design."
%%| fig-width: 6
flowchart TB
    design["🔷 Design Artefacts<br/><small>Product Specs · Composite-Indicator Specs<br/>Coherence Checks · Approval & Versioning Policy</small>"]
    implement["🔧 Implementation Assets<br/><small>Integration & Composition Engines · Indicator Engines<br/>Coherence & Content Tooling · Approval Store</small>"]
    execute["⚡ Execution Objects"]
    manage["📊 Management Reports"]

    design -->|"govern building"| implement
    implement -->|"produces pipeline<br/>that processes"| execute
    execute -->|"assessed by"| manage
    manage -->|"feeds back to"| design

    subgraph execute_detail [" "]
        direction LR
        OD["Output Data<br/>(State #4)"]:::bo -->|"composed & approved as"| SP["Statistical Product<br/>(State #4)"]:::bo
    end

    execute --> execute_detail
    OD -->|generates| logs["Component Lineage · Coherence Results · Approval Records"]

    classDef bo fill:#fbbf24,stroke:#b45309,color:#000
    style design fill:#f5f3ff,stroke:#7c3aed
    style implement fill:#dbeafe,stroke:#2563eb
    style execute fill:#fef9c3,stroke:#b45309
    style manage fill:#dcfce7,stroke:#16a34a
    style execute_detail fill:none,stroke:none
    style logs fill:#fff,stroke:#888,stroke-dasharray: 5 5
```


## Business Events

```{mermaid}
%%| label: fig-10
%%| fig-cap: "Event-Driven Choreography between the upstream domain (VS-04.0) and NSO teams, showing events across the Design → Implement → Execute → Manage cycle. The management phase closes the loop by feeding improvements back to design."
%%| fig-width: 6

sequenceDiagram
    participant US as Upstream (VS-04.0)
    participant NSO as NSO Teams
    participant PM as Process Mgmt

    rect rgb(245, 243, 255)
    Note over NSO: Design Phase
    NSO->>NSO: Define product specs, composite indicators,<br/>coherence checks & approval policy
    NSO-->>NSO: Design Artefacts Published
    end

    rect rgb(239, 246, 255)
    Note over NSO: Implementation Phase
    NSO->>NSO: Build integration/composition engines,<br/>coherence, content & approval tooling
    NSO-->>NSO: Pipeline Production-Ready
    end

    rect rgb(236, 253, 245)
    Note over NSO,US: Execution Phase (per cycle)
    US-->>NSO: Output Data Registered event
    NSO->>NSO: Select & integrate components; construct composites
    NSO->>NSO: Run coherence checks; produce interpretive content

    NSO->>NSO: Validate against standards; submit for approval

    alt Approved
        NSO->>NSO: Create immutable product version,<br/>register lineage & metadata
        NSO-->>NSO: Statistical Product Registered event
    else Not approved
        NSO->>NSO: Revise / return component to VS-04
    end
    end

    rect rgb(254, 243, 199)
    Note over PM: Management Phase
    PM->>PM: Monitor coherence & timeliness, assess product<br/>quality, produce audit reports
    PM-->>NSO: Improvement Recommendations
    end
```

## Framework Mappings

This reference table maps each process group of this document to the international frameworks (GSBPM, GAMSO, CSDA) and the SAF capability model. It is intended for architects and auditors; the narrative sections above do not depend on it.

| Process group | GSBPM | GAMSO | CSDA | SAF Capabilities |
|---|---|---|---|---|
| **Design** | Phase 1 (Specify Needs), Phase 2 (Design: 2.1–2.5) | Production (design activities), Capability Management | Data Governance, Metadata Management, Data Quality | 1.1.2 Design statistics product, 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| **Implementation** | Phase 3 (Build: 3.1–3.7) | Capability Management | Data Processing / Dissemination preparation (setup), Data Governance (configuration) | 1.1.3 Build statistics product, 3.2.1 Application development, 3.2.2 Functional management |
| **Execution** | Phase 6 (Analyze: 6.2 Validate outputs, 6.3 Interpret & explain, 6.5 Finalise outputs) + Phase 7 (7.1 Update output systems, 7.2 Produce dissemination products) | Production (execution) | Data Analysis / Dissemination preparation (execution) | 2.1.2 Metadata management, 2.1.3 Statistical quality management |
| **Management** | Overarching processes (Quality Management, Metadata Management) | Corporate Support (Quality Management, Data Management, Metadata Management), Capability Management (improvement) | Data Quality, Data Governance, Traceability | 2.1.3 Statistical quality management, 4.1.4 Improve management, 4.1.5 Accountability |

## Applying This to Your NSO

### Maturity Assessment Checklist

Use this checklist to assess your NSO's maturity across all four process types — not just execution.

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

### End-to-End Scenarios

Each scenario walks through **all four process types**, demonstrating how the governance pattern works in practice.

#### Scenario A: Labour Market Quarterly Publication

**Design Phase:** Product managers specify the quarterly labour-market publication: employment and unemployment rates (national and NUTS-2), a vacancy indicator, narrative, and a regional visualization, drawing on the validated LFS and administrative outputs. Coherence checks against prior quarters and the approval workflow are designed.

**Implementation Phase:** Engineers configure the integration engine (pinned LFS/administrative outputs), the time-series engine for the headline series, coherence checks vs. prior quarters, and the content/approval tooling. Coherence and reproducibility tests pass on historical data.

**Execution Phase:** For Q3-2026, an Output Data Registered event arrives. The team integrates the pinned `OD-LFS-2026Q3` outputs (carrying their CIs), constructs the seasonally-relevant series, and runs coherence checks (all reconcile; coherent with Q2). The commentary explains the 0.3pp employment-rate rise and notes its significance; visualizations are produced and editorially reviewed. The product is approved and registered as an immutable version with full lineage; VS-06.0 is notified.

**Management Phase:** Coherence-check pass rate is 100%, approval completed in one iteration, all component CIs correctly propagated. Improvement recommendation: add an automated check comparing the vacancy indicator to a related administrative series. Recommendations fed back to design.

#### Scenario B: Structural Business Statistics Composite Product

**Design Phase:** The composite SBS product is specified to integrate the register-based and survey-based turnover/employment estimates for the same NACE × region domains, with internal-consistency checks (domains sum to totals) and coherence vs. national-accounts inputs.

**Implementation Phase:** Engineers configure integration of the pinned `OD-BUS` outputs, the consistency checks, and dominance-aware confidentiality validation for the composite. Coherence and reproducibility tests pass.

**Execution Phase:** Q3-2026: an Output Data Registered event arrives. The register- and survey-based components are integrated for overlapping domains; NACE-class turnover sums to the published total; the components agree within tolerance except one domain, which is returned to VS-04 for review rather than adjusted. Once resolved, the product is approved and registered (`SP-BUS-2026Q3-001`) with lineage to its components; VS-06.0 is notified.

**Management Phase:** One coherence discrepancy this cycle (resolved upstream); component reuse rate high; reproducibility audit passes. Improvement recommendation: tighten the tolerance for the recurring domain and document the reconciliation. Recommendations fed back to design.

#### Scenario C: Consumer Price Index Product

**Design Phase:** The CPI product is specified to compose the headline all-items index and main divisions from the validated item indices, with chaining/rebasing rules, coherence checks against the prior month and year, and analytical commentary.

**Implementation Phase:** Engineers configure the index-composition engine (designed weights and chaining), coherence checks, and the commentary/approval tooling. Coherence and reproducibility tests pass; the composed headline matches the expected value on test data.

**Execution Phase:** For the monthly run, an Output Data Registered event arrives with the validated item indices. The headline and division indices are composed with the period weights, coherence checks confirm consistency with the prior month and year, and the commentary explains the main contributors to the monthly change. The product is approved and registered with full lineage; VS-06.0 is notified.

**Management Phase:** Coherence pass rate 100%, headline reproducible from item indices + weights, approval in one iteration. Improvement recommendation: enhance the contributions visualization for the commentary. Recommendations fed back to design.

## VS-06.0 Dissemination and Service Delivery

### Purpose and Scope

This document specifies the complete business layer for the **Dissemination** business domain, corresponding to the *VS-06.0 Dissemination and Service Delivery Value Stream*. It also covers 4 governance process types:

- **Design** — how the dissemination strategy, channels, and release processes are specified and planned (produces metadata)
- **Implementation** — how the dissemination platforms and release pipeline are built, configured, and tested (produces the execution process)
- **Execution** — how products are operationally prepared, released, supported, and monitored (produces statistical data)
- **Management** — how the domain is monitored, quality-assessed, and improved (produces quality reports)

::: {.callout-warning title="Out of Scope"}
Application and Technology layer specifications are out of scope for this document (the technical platforms themselves are provided by VS-09.0 Infrastructure and Platform Enablement). Composing and approving statistical products is out of scope — it belongs to VS-05.0; VS-06 disseminates products that have already been approved and registered.
:::





*A note on numbering:* each `VS-0x.y` below is both a value stream stage (*what value* is added) and a business process (*how* it is done); the numbering maps one-to-one. See the key-concepts box above.



### Position in the Statistical Value Chain

VS-06.0 is the sixth and final primary value stream — it receives approved statistical products from VS-05.0 and publishes, distributes, and makes them accessible to users through trusted, secure channels. It is the "Release & Serve" orchestration stage where statistical products become societal value.

```{mermaid}
%%| label: fig-1
%%| fig-cap: "Value Stream Context Map. VS-06.0 is highlighted as the dissemination stage — the exit point of the value chain, releasing statistics to users and society."
%%| fig-width: 6


flowchart TD
    subgraph primary["Primary Value Streams"]
        direction LR
        VS01["VS-01.0
        Data Acquisition
        & Ingestion"]
        VS02["VS-02.0
        Data Standardization
        & Integration"]
        VS03["VS-03.0
        Data Editing
        & Enrichment"]
        VS04["VS-04.0
        Estimation, Analysis
        & Modeling"]
        VS05["VS-05.0
        Statistical Product
        Composition"]
        VS06["**VS-06.0**
        Dissemination
        & Service Delivery"]:::highlight
        VS01 --> VS02 --> VS03 --> VS04 --> VS05 --> VS06
    end

    subgraph supporting["Supporting Value Streams"]
        VS07["VS-07.0
        Governance &
        Compliance"]
        VS08["VS-08.0
        Innovation &
        Methodology"]
        VS09["VS-09.0
        Infrastructure &
        Platform Enablement"]
        VS10["VS-10.0
        Customer &
        Stakeholder Engagement"]
    end

    VS06 ==>|"released to"| USERS["Users & Society
    (State #6 — Consumed)"]
    supporting -.->|"enables"| primary

    classDef highlight fill:#2563eb,color:#fff,stroke:#1d4ed8,stroke-width:3px
    style USERS fill:#0f766e,color:#fff,stroke:#0f766e
```

### Steady State Transition

VS-06.0 transitions data from **Steady State #4 (approved statistical products)** to **Steady State #5 (Released Data)** — products that have undergone final disclosure control (additional confidentiality protection beyond State #4), are documented for correct interpretation, and are published or delivered to external parties via trusted channels. Once released, data is used externally as **Steady State #6 (Consumed Data)**, outside the NSO's direct control.

```{mermaid}
%%| label: fig-2
%%| fig-cap: "Steady State Transition from approved products (State #4) to Released Data (State #5), consumed externally as State #6."
%%| fig-width: 6
flowchart LR
    subgraph upstream["Upstream Domain (VS-05.0)"]
        SP["Approved Statistical
        Products (State #4)"]
    end

    subgraph boundary["Dissemination Boundary"]
        QG["Dissemination Service
        (Prepare & disclosure-control, Publish,
        Provide access, Support users, Monitor)"]
    end

    subgraph internal["Released Domain (VS-06.0)"]
        RD["Released Data
        (State #5)"]
    end

    subgraph external["External"]
        CD["Consumed Data
        (State #6)"]
    end

    SP --> QG --> RD --> CD

    style internal fill:#2563eb,color:#fff,stroke:#1d4ed8,stroke-width:3px
    style upstream fill:#7d7d7d,color:#fff,stroke:#1d4ed8,stroke-width:1px
    style boundary fill:#FFF,stroke-dasharray:5,5
    style external fill:#0f766e,color:#fff,stroke:#0f766e
```

::: {.callout-tip title='Release readiness criteria (Examples)*'}
- Dissemination channels and formats selected for the target users (open data, API, publication, secure research access)
- Final statistical disclosure control applied; output further protected vs State #4 where required
- Released microdata de-identified to the agreed standard
- Documentation, metadata, and methodology notes prepared for correct interpretation
- Release timing managed per the release calendar and equal-access/embargo policy
- Accessibility standards met (formats, languages, machine-readability)
- Usage monitoring and feedback channels in place
:::

::: {.callout-important title="The dissemination discipline — accessibility, trust, and responsible use"}
VS-06 is the chain's exit point: it converts statistical output into societal value. The guarantee here is **accessibility and trust** — accurate, timely, understandable delivery through trusted, secure channels — gated by **final statistical disclosure control** (no release without confidentiality clearance) and supported by documentation and user services that enable **responsible use**. Equal access to released statistics (managed release timing, embargo discipline) and accessibility (formats, languages, machine-readability) are explicit obligations.
:::

::: {.callout-note title="Inherited from VS-05.0"}
VS-06 receives approved, registered statistical products **plus** the metadata VS-05 attached — component lineage, composition method, propagated accuracy, coherence results, the approval record, and the product's confidentiality status. VS-06 applies the **final disclosure control for release** (beyond the initial disclosure control of VS-04 and the standards check of VS-05), formats the product for each channel, and publishes — it does not alter the statistics, only protects, formats, and delivers them.
:::

::: {.callout-note title="Reliance on supporting value streams"}
Dissemination is a strategic, user-centered activity that depends on the supporting value streams: **VS-07.0 Governance and Compliance** ensures all dissemination complies with data-protection and confidentiality law; **VS-09.0 Infrastructure and Platform Enablement** provides the portals, APIs, and secure research environments; and **VS-10.0 Customer and Stakeholder Engagement** ensures dissemination services meet real user needs. The usage and feedback gathered here (Section 5.5) flow back to VS-10 and across the chain.
:::


### The Four-Process Governance Pattern



```{mermaid}
%%| label: fig-3
%%| fig-cap: "The Four-Process Governance Pattern. Each process type produces a distinct artefact class. The cycle closes when Management findings feed back into Design improvements."
%%| fig-width: 6
flowchart LR
    D["**Design**
    _provides metadata_

    Dissemination & access strategy, release
    & disclosure policy, support model"]
    I["**Implement**
    _provides the execution process_

    Configured publication & access channels,
    disclosure-control & release tooling"]
    E["**Execute**
    _provides the statistical data_
    Released products, access services,
    user support, usage data"]
    M["**Manage**
    _provides quality reports_
    Usage & accessibility dashboards, release
    quality scorecards, improvement recommendations"]

    D -->|"design artefacts
    guide building"| I
    I -->|"production-ready
    process"| E
    E -->|"data & process logs
    for assessment"| M
    M -->|"improvement
    feedback"| D

    style D fill:#7c3aed,color:#fff,stroke:#6d28d9
    style I fill:#2563eb,color:#fff,stroke:#1d4ed8
    style E fill:#059669,color:#fff,stroke:#047857
    style M fill:#d97706,color:#fff,stroke:#b45309
```




### Governing Principles

The following principles directly govern the VS-06.0 business domain:

| Principle | Statement | Application to VS-06.0 |
|---|---|---|
| **SAF-P01** | Actively participate in open source to maintain collective control over statistical processes | NSOs should contribute to open source communities for dissemination platforms, APIs, and visualization tooling, ensuring collective control over critical delivery capabilities rather than vendor dependence. |
| **SAF-P07** | Implement loosely coupled processes and systems | The dissemination domain consumes approved products through the State #4 interface without knowledge of how they were composed, and exposes released data through stable, versioned access services. |
| **SAF-P08** | Data is shared property | Released data is made broadly and equally available to all authorized users through open and standard channels, maximising reuse while respecting confidentiality. |
| **SAF-P09** | No data without metadata and classification | Every released product carries the metadata, methodology notes, and documentation users need to interpret it correctly; released datasets are accompanied by structural and reference metadata (e.g., SDMX). |
| **SAF-P10** | Security By Design | Access controls, secure channels, and integrity protection are embedded in publication and access services — including secure research environments for sensitive microdata — not added as an afterthought. |
| **SAF-P11** | Privacy By Design | Final statistical disclosure control and de-identification are applied before release, and the disclosure risk of every released product and microdata file is assessed and cleared by design. |

::: {.callout-note title="Cross-cutting principle application"}
Several principles cut across all four process types. SAF-P11 (Privacy By Design) is the release gate: disclosure control is designed (Section 3.2/3.4), implemented (Section 4.2), and applied at execution (Section 5.2) before anything is published. SAF-P08 (data is shared property) and SAF-P09 (metadata) drive open, well-documented, equal-access release. SAF-P10 (Security By Design) governs access services and secure research environments across Execution (Sections 5.3–5.4). SAF-P07 (loosely coupled) governs the State #4 intake interface from VS-05.0 and the released-data access interface to external users.
:::

### Capability Foundations

VS-06.0 draws on the following SAF capabilities:

| Capability Group | Capabilities | Role in VS-06.0 |
|---|---|---|
| **1.1 Statistical design and build** | 1.1.2 Design statistics product, 1.1.3 Build statistics product | Design dissemination products/services and build the release and access pipeline |
| **2.1 Data management** | 2.1.1 Data lifecycle management, 2.1.2 Metadata management, 2.1.3 Statistical quality management | Manage released data and its metadata, and the quality of release and access |
| **3.2 Computerization and automation** | 3.2.1 Application development, 3.2.2 Functional management | Build and maintain publication channels, APIs, dashboards (with VS-09 platforms) |
| **3.3 Security and Privacy** | 3.3.1 Privacy management, 3.3.2 Security planning | Apply final disclosure control and secure access to released and microdata products |
| **4.1 Governance** | 4.1.1 Strategy and governance, 4.1.2 Policy and planning, 4.1.4 Improve management, 4.1.5 Accountability | Govern release, manage equal-access policy, plan improvements, report on compliance |

### Metadata Perspective

It is considered that metadata is an essential product of the Design phase and a critical concern of every other phase. In this domain, metadata is what enables responsible use: every released product must carry the documentation, methodology, and reference metadata users need. The table below consolidates the metadata produced across all four process types, covering both data metadata (about the released products) and process metadata or paradata (about how the process runs).

| Process Type | Data Metadata Produced | Process Metadata (Paradata) Produced |
|---|---|---|
| **Design** | Dissemination & access strategy, channel/format specs, release & disclosure policy, documentation standards | Design decisions log, policy version, review and approval records |
| **Implement** | Channel configurations, API/dataset templates, disclosure-control parameters, documentation templates | Build log, test results, accessibility-test outcomes, deployment approvals |
| **Execute** | Per-release documentation, applied-SDC record, channel/format published, release timestamp, access-service metadata | Operator identity, release-calendar adherence, embargo handling, publication run identifiers |
| **Manage** | Usage statistics, accessibility assessments, user-satisfaction metrics, release-quality reports | Usage dashboards, feedback logs, improvement decisions, audit findings |


## Business Roles and Actors



| Role                        | Process Orientation | Description                                                                                       |
|-----------------------------|---------------------|---------------------------------------------------------------------------------------------------|
| **Upstream Data Provider (VS-05.0)** | External (internal NSO) | Supplies approved statistical products (State #4) with their metadata and approval record |
| **Data User**               | External            | Consumes released data — policymakers, researchers, journalists, businesses, the public            |
| **Dissemination Manager**   | Design              | Designs the dissemination and access strategy, product/service portfolio, and release calendar     |
| **Disclosure-Control Designer** | Design          | Designs the final disclosure-control rules and de-identification standards for release              |
| **Channel/Service Designer**| Design              | Designs the access channels, formats, APIs, dashboards, and secure research access                 |
| **Data Engineer**           | Implementation      | Builds and configures publication channels, APIs, and access services (on VS-09 platforms)         |
| **System Configurator**     | Implementation      | Configures release tooling, access controls, and disclosure-control tooling                       |
| **Test Manager**            | Implementation      | Plans and executes testing of the release pipeline (technical, accessibility, security)            |
| **Process Owner**           | Management          | Accountable for the end-to-end performance of the dissemination domain                             |
| **Compliance Officer**      | Management          | Ensures data-protection, confidentiality, and equal-access compliance (with VS-07), produces audits |
| **Quality Manager**         | Management          | Monitors usage/accessibility KPIs, produces quality reports, and drives continuous improvement     |
| **Release Manager**         | Execution           | Manages the release event: timing, embargo, equal access, and publication                          |
| **Open-Data / API Product Owner** | Execution     | Operates the open-data, API, and dashboard services for released data                              |
| **User-Support Lead**       | Execution           | Provides documentation, helpdesk support, and training for correct interpretation and use          |
| **Engagement / Communications Officer** | Execution | Promotes releases and gathers user feedback (with VS-10)                                            |



## Design Processes — "provides metadata"

*Framework alignment: GSBPM Phases 1–2 — see [Framework Mappings](#framework-mappings).*

The design phase produces the **metadata artefacts** that govern all subsequent phases — the dissemination and access strategy, the disclosure-control and release policy, the channel/format specifications, and the user-support and documentation model. Without well-designed strategy and policy, release becomes ad-hoc and risks confidentiality breaches or inequitable access, and management has no baseline to measure accessibility and impact against.

### Design the Dissemination and Access Strategy

The starting point is deciding who the products are for and how they will be reached. This sub-process defines the target user groups and their needs (with VS-10), the access channels and release formats (open data, API, research access, publications, dashboards), the release calendar, and the equal-access/embargo policy. It maps each product to its appropriate channels and formats, aligned with GSBPM 2.5 and Phase 7 design.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define target user groups and their needs (with VS-10) | User Segmentation | GSBPM 2.1 |
| Define access channels and release formats (open data, API, research access, publications) | Channel & Format Strategy | GSBPM 2.5 |
| Define the release calendar and equal-access/embargo policy | Release Calendar & Access Policy | SAF 4.1.5 |
| Map each product to its channels and formats | Product-Channel Map | GSBPM 2.5 |

::: {.callout-tip title="**NSO Example — Labour Market Statistics:**"}
The labour-market dissemination strategy targets policymakers (press release + commentary on the release date), researchers (API + downloadable series), and the public (interactive dashboard). The release calendar is published in advance and an embargo gives accredited media pre-access under agreement, ensuring equal access at the release moment.
:::


### Design Disclosure-Control and De-identification for Release

This sub-process designs the final confidentiality protection applied before release. It specifies the disclosure-control rules for tables and dashboards (suppression, rounding, perturbation) over and above the protection already applied upstream, the de-identification standard for any released microdata, and the disclosure-risk criteria a release must meet. Differential treatment by channel is designed — for example, more detailed microdata only via a secure research environment — aligned with SAF-P11 and GSBPM 6.4.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define final disclosure-control rules for tables/dashboards | Release SDC Rules | SAF-P11 |
| Define de-identification standard for released microdata | De-identification Standard | SAF-P11 |
| Define disclosure-risk criteria a release must meet | Disclosure-Risk Criteria | SAF-P11 |
| Design differential treatment by channel (open vs. secure research access) | Channel Protection Design | SAF-P10 |

### Design Channels, Formats, and Documentation

This sub-process designs the delivery mechanics. It specifies the publication formats and accessibility standards (machine-readable formats, languages, web-accessibility), the API and dataset structures (e.g., SDMX), the dashboard and visualization designs, the secure research environment access model, and the documentation standard (methodology notes, metadata, user guides) that must accompany every release. It draws on the platforms provided by VS-09, aligned with GSBPM 2.5/3 design.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Specify publication formats and accessibility standards | Format & Accessibility Standard | GSBPM 2.5 |
| Specify API/dataset structures (e.g., SDMX) | API & Dataset Specification | CSDA Dissemination |
| Specify dashboards, visualizations, and research-access model | Service Design | GSBPM 2.5 |
| Define the documentation standard accompanying every release | Documentation Standard | SAF-P09 |

### Design User Support, Promotion, and Feedback Model

This sub-process designs how users are supported and heard. It specifies the user-support model (documentation, helpdesk, training), the promotion/communication approach for releases (with VS-10), and the usage-monitoring and feedback model — what is measured (usage, satisfaction), how feedback is collected, and how it routes back into improvement. The equal-access and correction/erratum policy round out the design, aligned with GSBPM 7 design and Phase 8.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define the user-support model (documentation, helpdesk, training) | User-Support Model | GSBPM 2.5 |
| Define promotion/communication approach for releases (with VS-10) | Communication Plan | GSBPM 2.5 |
| Define usage-monitoring and feedback model | Usage & Feedback Model | GSBPM 2.5 |
| Define correction/erratum and re-release policy | Correction Policy | SAF 4.1.5 |

### Design Release Governance and Audit Framework

The final design sub-process ensures releases are governed, equitable, and auditable. It defines the release approval/sign-off workflow, the equal-access controls (no privileged early access outside policy), the release-versioning policy (identity, revisions/corrections, retention), the lineage requirements from each release back to its approved product, and the role-based access controls for access services in line with SAF-P10.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Define release approval/sign-off workflow | Release Approval Policy | SAF 4.1.5 |
| Define equal-access controls and embargo governance | Equal-Access Controls | SAF 4.1.5 |
| Define release-versioning and lineage requirements | Versioning & Lineage Policy | CSDA Traceability |
| Design role-based access control for access services | Access Control Design | SAF-P10 |

```{mermaid}
%%| label: fig-4
%%| fig-cap: "Design Process Decomposition. Approved products, user needs, and confidentiality/access law flow into five design sub-processes, producing metadata artefacts that govern Implementation, Execution, and Management."
%%| fig-width: 6
flowchart TB
    subgraph inputs["Inputs"]
        SP["Approved Products<br/><small>(State #4 from VS-05)</small>"]
        FW["Framework Standards<br/><small>GSBPM · GAMSO · CSDA</small>"]
        USR["User Needs<br/><small>(via VS-10)</small>"]
        LAW["Confidentiality & Access Law<br/><small>(via VS-07)</small>"]
    end

    subgraph design["Design Sub-Processes"]
        D1["3.1 Dissemination<br/>& Access Strategy"]
        D2["3.2 Disclosure-Control<br/>& De-identification"]
        D3["3.3 Channels, Formats<br/>& Documentation"]
        D4["3.4 User Support,<br/>Promotion & Feedback"]
        D5["3.5 Release Governance<br/>& Audit Framework"]
    end

    subgraph outputs["Metadata Artefacts"]
        O1["Channel & Format Strategy"]
        O2["Release SDC Rules"]
        O3["Service & Documentation Specs"]
        O4["Support & Feedback Model"]
        O5["Release Governance Policy"]
    end

    SP --> D1
    USR --> D1
    FW -.->|inform| design
    LAW --> D2

    D1 --> D2 --> D3 --> D4 --> D5

    D1 --> O1
    D2 --> O2
    D3 --> O3
    D4 --> O4
    D5 --> O5

    outputs -->|govern| NEXT["Implementation (§4) · Execution (§5)<br/>measured by Management (§6)"]

    style design fill:#f5f3ff,stroke:#7c3aed
    style outputs fill:#ede9fe,stroke:#7c3aed
```

## Implementation Processes — "provides the execution process"

*Framework alignment: GSBPM Phase 3 (Build) — see [Framework Mappings](#framework-mappings).*

The implementation phase takes the metadata artefacts from Design and **builds, configures, and tests** the production-ready dissemination and access pipeline — on the platforms provided by VS-09.0. Nothing is published operationally until this phase is complete.

### Build Publication and Access Channels

This sub-process turns the channel and format designs into operational services. Publication channels (website/publication system), the API and open-data services, dashboards, and the secure research environment access are built or configured on the VS-09 platforms per the designed formats and accessibility standards. SDMX-compliant dataset and metadata exchange is configured, and access controls are applied per the designed model, following GSBPM 3.1–3.3.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Build/configure publication channels and the open-data/API services | Configured publication & API services | GSBPM 3.3 |
| Build/configure dashboards and visualization services | Configured dashboards | GSBPM 3.3 |
| Configure secure research environment access | Research-access service | SAF-P10 |
| Configure SDMX-compliant dataset and metadata exchange | Standard exchange interfaces | CSDA Dissemination |

::: {.callout-tip title="**NSO Example — Open Data and API:**"}
The team configures an SDMX-based API and a bulk open-data download for the labour-market series on the NSO's VS-09 platform, with rate-limiting and machine-readable metadata, plus a public dashboard fed from the same released datasets.
:::

### Configure Disclosure-Control and Release Tooling

The designed final disclosure-control rules and release policy are implemented. SDC tooling is configured to apply the designed suppression/rounding/perturbation to tables and dashboards and to de-identify released microdata, with disclosure-risk checks enforced before publication. Release tooling is configured for managed-timing release, embargo handling, and equal-access enforcement, following GSBPM 6.4/7.3.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Configure final SDC tooling (suppression/rounding/perturbation) | Configured SDC tooling | SAF-P11 |
| Configure microdata de-identification to the designed standard | De-identification component | SAF-P11 |
| Enforce disclosure-risk checks before publication | Release disclosure gate | SAF-P11 |
| Configure managed-timing release, embargo, and equal-access enforcement | Release-management tooling | SAF 4.1.5 |

### Build Documentation, Support, and Usage-Monitoring Services

This sub-process implements the user-facing support and the feedback loop. Documentation/metadata services are built so every release is accompanied by methodology notes, reference metadata, and user guides. Helpdesk and training support is set up per the support model. Usage-monitoring and feedback collection are implemented to capture usage statistics, satisfaction, and feedback, and to route them into the improvement loop (and to VS-10). The release-versioning store is built so each release is identified, immutable, and traceable to its approved product, and event notifications are configured to signal a release.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Build documentation/metadata services for every release | Documentation services | SAF-P09 |
| Set up helpdesk and training support | User-support services | GSBPM 3.3 |
| Implement usage-monitoring and feedback collection | Usage & feedback tooling | GSBPM 3.3 |
| Build the release-versioning store and configure the "Statistics Released" event | Versioning store, event publication | CSDA Traceability |

### Test and Validate the Pipeline

Before the pipeline goes into production, it must be rigorously verified. Technical testing covers all components — publication channels, API, dashboards, research access, SDC tooling, release tooling, and documentation/support services (GSBPM 3.5). Integration testing validates the end-to-end flow from product intake through preparation, disclosure control, release, to access and support. An **accessibility test** confirms formats meet the accessibility standard; a **security/disclosure test** confirms access controls and that no output breaches the disclosure-risk criteria; and a **release-rehearsal** confirms managed timing and embargo work. The phase concludes with finalization of the production system and documentation of operational procedures (GSBPM 3.6–3.7).

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Technical testing of all individual components | Unit test reports | GSBPM 3.5 |
| Integration testing: end-to-end flow from intake to access & support | Integration test report | GSBPM 3.5 |
| Accessibility test (formats, languages, machine-readability) | Accessibility test report | GSBPM 3.6 |
| Security/disclosure test (access controls, disclosure-risk criteria) | Security & disclosure test report | SAF-P10, SAF-P11 |
| Release rehearsal (managed timing, embargo, equal access) | Release-rehearsal report | GSBPM 3.6 |
| Finalize production system and document operational procedures | Operational Procedures Manual, Production-Ready Pipeline | GSBPM 3.7 |

```{mermaid}
%%| label: fig-5
%%| fig-cap: "Implementation Pipeline from design artefacts through build/configure/test to production-ready system."
%%| fig-width: 6
flowchart LR
    subgraph design_artefacts["Design Artefacts (from Section 3)"]
        DA1["Channel & Format\nStrategy"]
        DA2["Release SDC\nRules"]
        DA3["Service &\nDocumentation Specs"]
        DA4["Support &\nFeedback Model"]
        DA5["Release Governance\nPolicy"]
    end

    subgraph build["Build & Configure"]
        B1["4.1 Build Publication\n& Access Channels"]
        B2["4.2 Configure SDC\n& Release Tooling"]
        B3["4.3 Build Docs,\nSupport & Monitoring"]
    end

    subgraph test["Test & Validate"]
        T1["4.4 Technical\nTesting"]
        T2["4.4 Accessibility &\nDisclosure Tests"]
        T3["4.4 Release\nRehearsal"]
    end

    subgraph output["Production-Ready"]
        PR["Operational\nDissemination\nPipeline"]
        OP["Operational\nProcedures"]
    end

    DA1 & DA3 --> B1
    DA2 & DA5 --> B2
    DA3 & DA4 --> B3

    B1 & B2 & B3 --> T1 --> T2 --> T3
    T3 --> PR & OP

    PR -->|"ready for"| EXEC["Execution\n(Section 5)"]

    style build fill:#eff6ff,stroke:#2563eb
    style test fill:#dbeafe,stroke:#2563eb
```

## Execution Processes — "provides the statistical data"

*Framework alignment: the later GSBPM phases for this domain — see [Framework Mappings](#framework-mappings).*

The execution phase runs the **designed and implemented pipeline** operationally for each release cycle. This corresponds to the five VS-06 value stream stages. In a mature steady state, much of the work has been pre-designed (Section 3) and pre-built (Section 4) — execution focuses on running the release, serving users, and monitoring usage, with final disclosure control as the gate that must pass before anything is published.

### Confirm Dissemination and Access Plan

**Value created:** *The right channels, formats, and timing confirmed for this release.*

When a "Statistical Product Registered" event is received from VS-05.0, execution begins by confirming the dissemination plan for the release. In a mature steady state the strategy has been designed (Section 3), so per-cycle execution confirms the channels, formats, and release-calendar slot for the product, verifies the embargo/equal-access arrangements, and confirms the target user groups. Significant changes (a new channel, a policy change) trigger a return to the design process rather than ad-hoc adaptation.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Confirm channels, formats, and release-calendar slot for the product | Confirmed release plan | GSBPM 7.1 |
| Verify embargo and equal-access arrangements | Access arrangements confirmed | SAF 4.1.5 |
| Confirm target user groups and communication plan | Confirmed audience & comms | GSBPM 7.4 |
| Flag plan changes for design review | Plan-change exception (if any) | GAMSO QM |

::: {.callout-tip title="**NSO Example — Labour Market Release:**"}
For the Q3-2026 labour-market release the team confirms the release date and slot, the press embargo for accredited media, and the channels (press release, API, dashboard), with no change to the strategy this cycle.
:::

### Prepare Data for Dissemination

**Value created:** *Products made disclosure-safe and formatted for each channel.*

This sub-process prepares the product for release, aligned with GSBPM 6.4 (Apply disclosure control) and 7.2. The final disclosure control is applied — suppression, rounding, or perturbation for tables and dashboards beyond the upstream protection, and de-identification for any released microdata — and the release is checked against the disclosure-risk criteria; **nothing proceeds if the criteria are not met**. The product is then formatted for each channel (publication, API/dataset, dashboard) and the accompanying documentation, metadata, and methodology notes are assembled per the documentation standard.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Apply final disclosure control to tables/dashboards | Disclosure-controlled outputs | GSBPM 6.4 |
| De-identify any released microdata to the designed standard | De-identified microdata | SAF-P11 |
| Check the release against disclosure-risk criteria (gate) | Disclosure clearance | SAF-P11 |
| Format for each channel and assemble documentation/metadata | Channel-ready products + docs | GSBPM 7.2 |

::: {.callout-important}
**Release gate:** No product is published until it passes the disclosure-risk criteria. If a release fails the gate, it is returned for additional protection — confidentiality is non-negotiable at the boundary to State #5.
:::

### Publish and Provide Access Services

**Value created:** *Statistics released to users through trusted, secure channels — equally and on time.*

This sub-process executes the release, aligned with GSBPM 7.3 (Manage release). The product and its metadata are published via the confirmed channels — portal/publication, API/open data, dashboards — and made available through secure research environments where microdata access is mediated. Release timing is managed per the calendar with embargo and equal-access enforced (no privileged early access outside policy), and the release is promoted per the communication plan (with VS-10). A persistent, identified released version is recorded with lineage to the approved product, and a "Statistics Released" event is published.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Publish products and metadata via confirmed channels (portal, API, dashboards) | Published release | GSBPM 7.3 |
| Provide mediated access via secure research environment where applicable | Research-access provision | SAF-P10 |
| Manage release timing, embargo, and equal access | Managed release | SAF 4.1.5 |
| Promote the release per the communication plan (with VS-10) | Promotion executed | GSBPM 7.4 |

```{mermaid}
%%| label: fig-6
%%| fig-cap: "Release Architecture. The approved product is disclosure-controlled and formatted, must pass the disclosure-risk gate, and is then released through publication, API, dashboard, and secure research channels to users (State #6)."
%%| fig-width: 6
flowchart LR
    subgraph product["Approved product (State #4)"]
        SP["Approved product\n(+ metadata, accuracy)"]
    end

    subgraph prepare["Prepare & Gate"]
        SDC["Final disclosure\ncontrol"]
        FMT["Format per channel\n+ documentation"]
        GATE{"Disclosure-risk\ncriteria met?"}
    end

    subgraph release["Release (State #5)"]
        PUB["Portal / Publication"]
        API["API / Open data"]
        DASH["Dashboards"]
        SRE["Secure research\nenvironment"]
    end

    USERS["Users & Society\n(State #6)"]

    SP --> SDC --> FMT --> GATE
    GATE -->|"yes"| PUB & API & DASH & SRE
    GATE -->|"no"| RET["Return for\nmore protection"]
    PUB & API & DASH & SRE --> USERS

    style product fill:#ecfdf5,stroke:#059669
    style prepare fill:#f0fdf4,stroke:#059669
    style release fill:#eff6ff,stroke:#2563eb
    style USERS fill:#0f766e,color:#fff,stroke:#0f766e
```


::: {.callout-tip title='**NSO Example — Multi-Channel Release:**'}
At 09:00 on the release date the Q3-2026 labour-market figures go live simultaneously on the website, the API, and the dashboard; accredited media that received the embargoed copy may publish at the same moment. Equal access is enforced — no figure is available before the release time.
:::


### Support and Engage Users

**Value created:** *Users helped to find, understand, and correctly use the statistics.*

This sub-process supports users, aligned with GSBPM 7.5 (Manage user support). Documentation, metadata, and user guides are made available with the release; the helpdesk answers queries; and training or guidance is provided for correct interpretation and use. Engagement activities (with VS-10) gather questions and needs, and any errata or clarifications are issued per the correction policy. The aim is responsible use — helping users avoid misinterpretation of estimates and their uncertainty.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Provide documentation, metadata, and user guides with the release | Published documentation | SAF-P09 |
| Operate the helpdesk and respond to user queries | Query responses | GSBPM 7.5 |
| Provide training/guidance for correct interpretation | User guidance | GSBPM 7.5 |
| Issue errata/clarifications per the correction policy | Corrections (if any) | SAF 4.1.5 |

::: {.callout-tip title="**NSO Example — Research Microdata:**"}
Researchers accessing de-identified business microdata via the secure research environment receive the data dictionary, methodology notes, and an onboarding session; the helpdesk handles output-checking requests so that researchers' exported results also meet disclosure rules.
:::

### Monitor Usage and Feedback

**Value created:** *Insight into how statistics are used and valued, feeding continuous improvement.*

The final execution sub-process closes the loop with users, aligned with GSBPM 7.4 and Phase 8 (Evaluate). Usage is tracked across channels (downloads, API calls, dashboard views, publication reads), user satisfaction and feedback are collected, and the insights are analyzed to understand reach, value, and unmet needs. These insights are routed back to the design process (Section 3), to VS-10 Customer and Stakeholder Engagement, and across the value chain — for example, signalling demand for a new breakdown that would originate in earlier streams.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Track usage across channels (downloads, API calls, views) | Usage Statistics | GSBPM 7.4 |
| Collect user satisfaction and feedback | Feedback Log | GSBPM 8 |
| Analyze reach, value, and unmet needs | Usage Insight Report | GSBPM 8 |
| Route insights to design, VS-10, and the wider chain | Improvement & engagement inputs | SAF 4.1.4 |

```{mermaid}
%%| label: fig-7
%%| fig-cap: "Released Data Artefact Structure. Reading guide: each box is a type of record with its fields; a connecting line means the records are linked. Each released version is linked to its disclosure-control record, the channels it was released via, its documentation, and its usage — all traceable to the approved product it came from."
%%| fig-width: 6
erDiagram
    RELEASED_DATA_ARTEFACT {
        string release_id PK "Unique persistent URI/UUID"
        string release_version "Immutable release identifier"
        string product_source_id "Approved product (State #4) ID"
        date reference_period "Reference period"
        datetime release_timestamp "When released"
    }
    DISCLOSURE_RECORD {
        string final_sdc_method "Suppression/rounding/perturbation applied"
        string deidentification "Microdata de-identification standard"
        boolean risk_criteria_met "Passed disclosure-risk gate"
        string approver "Release sign-off authority"
    }
    CHANNEL_RECORD {
        string channel "Portal / API / dashboard / research env"
        string format "Format (e.g., SDMX, CSV, HTML)"
        string accessibility "Accessibility standard met"
        boolean equal_access "Equal-access/embargo enforced"
    }
    DOCUMENTATION_RECORD {
        string methodology_notes "Methodology documentation"
        string metadata_ref "Reference & structural metadata"
        string user_guide "User guidance"
        string corrections "Errata issued (if any)"
    }
    USAGE_RECORD {
        int downloads "Downloads / API calls"
        int dashboard_views "Dashboard views"
        float satisfaction "User-satisfaction measure"
        string feedback_ref "Collected feedback"
    }

    RELEASED_DATA_ARTEFACT ||--|| DISCLOSURE_RECORD : "protected by"
    RELEASED_DATA_ARTEFACT ||--|{ CHANNEL_RECORD : "released via"
    RELEASED_DATA_ARTEFACT ||--|| DOCUMENTATION_RECORD : "documented by"
    RELEASED_DATA_ARTEFACT ||--|| USAGE_RECORD : "monitored by"
```

## Management Processes — "provides quality reports"

*Framework alignment: GSBPM overarching Quality/Metadata Management — see [Framework Mappings](#framework-mappings).*

The management phase runs **alongside and after** execution. It monitors the dissemination domain's performance, assesses the accessibility and impact of releases, ensures every release is compliant and equitable, and feeds improvement recommendations back into the design phase and to VS-10 — closing the governance cycle.

### Monitor Process Performance

Operational performance of the dissemination domain must be tracked systematically across release cycles. The process owner and quality manager collect and aggregate key performance indicators, monitor adherence to the release calendar, and track paradata — which channels were used, when each release went live, how embargoes were handled, and how many support queries arose. This information feeds process performance dashboards that give the process owner a real-time view of domain health, aligned with the GAMSO Quality Management capability.

**Key Performance Indicators (KPIs):**

| KPI | Description | Measurement |
|---|---|---|
| On-time release rate | Releases published exactly on the calendar slot | Per release, per cycle |
| Disclosure-gate pass rate | Releases passing the disclosure-risk gate on first run | Per release, per cycle |
| Channel availability | Uptime/availability of API and access services | Per channel |
| Usage / reach | Downloads, API calls, dashboard views per release | Per release, per channel |
| User satisfaction | Satisfaction measure from feedback | Per cycle |
| Support response time | Time to resolve user queries | Per cycle |

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Collect and aggregate KPIs per release cycle | Process Performance Dashboard | GAMSO QM |
| Monitor adherence to the release calendar | Release-Calendar Adherence Report | GAMSO QM |
| Track paradata: channels, timing, embargo handling, queries | Paradata Records | GAMSO QM |
| Generate process performance dashboards | Dashboard for Process Owner | GAMSO QM |

### Assess Dissemination Quality

Beyond process performance, the quality of dissemination itself must be evaluated against the criteria established in design. Each release and the service overall are assessed across multiple quality dimensions: accessibility (formats, languages, machine-readability, web-accessibility compliance), timeliness and punctuality (against the release calendar), reach and relevance (usage vs. expectations, coverage of user groups), and clarity (do users interpret correctly, judged from queries and feedback). Results are compared against the designed criteria from Section 3. Quality indicators are produced per release and per cycle, and trends are tracked. This aligns with the CSDA Data Quality capability and SAF Capability 2.1.3.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Assess accessibility compliance of releases | Accessibility Report (per cycle) | SAF 2.1.3 |
| Assess timeliness and punctuality vs. the release calendar | Punctuality Report | CSDA Data Quality |
| Assess reach, relevance, and clarity from usage and feedback | Reach & Clarity Report | SAF 2.1.3 |
| Identify quality trends across releases and cycles | Quality Trend Analysis | SAF 2.1.3 |

### Manage Release and Channel Lifecycle

The dissemination products, channels, and the releases they produce must remain current, complete, and well-governed. This sub-process governs the lifecycle of channels, formats, and documentation standards — versioning them, managing transitions (e.g., an API version upgrade), and retiring obsolete channels. It verifies metadata completeness — that every release carries full documentation, disclosure record, and lineage as an SAF-P09 compliance check — and governs the release-version store: retention, immutability, corrections handling, and reconciliation that catalog entries match what is published. Metadata lineage from approved product to released data is tracked.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Govern channel, format, and documentation lifecycle and versions | Channel Version Register | SAF-P09 |
| Verify metadata completeness (documentation, disclosure record, lineage) | Metadata Quality Report | SAF-P09 |
| Govern the release-version store: retention, immutability, corrections | Release Store Audit | CSDA Traceability |
| Track metadata lineage from approved product to released data | Metadata Lineage Audit | CSDA Traceability |

### Audit and Compliance Reporting

This sub-process produces the evidence that the dissemination domain operates within legal, regulatory, and organizational requirements. Disclosure-compliance reports confirm that every release passed the disclosure-risk gate and that released microdata meets the de-identification standard per SAF-P11. Equal-access compliance reports confirm that release timing and embargo policy were respected (no privileged early access). Accessibility-compliance reports confirm formats met the accessibility standard, and security-compliance reports verify access controls and secure-research-environment integrity. These reports — produced with VS-07.0 Governance and Compliance — satisfy the SAF Capability 4.1.5 (Accountability) obligation.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Produce disclosure-compliance reports: every release passed the gate | Disclosure Compliance Summary | SAF-P11 |
| Report on equal-access compliance (timing, embargo) | Equal-Access Compliance Report | SAF 4.1.5 |
| Report on accessibility compliance | Accessibility Compliance Report | SAF 4.1.5 |
| Report on security compliance: access controls, research-environment integrity | Compliance Report (per cycle) | SAF-P10 |

### Continuous Improvement

The final management sub-process closes the governance loop by analyzing performance, usage, and feedback data to identify and drive improvements. Trends across release cycles are examined: is punctuality holding, is reach growing, is satisfaction improving, are support queries falling? Improvement opportunities are identified — adding or improving channels and formats, enhancing documentation that users find unclear, streamlining the release process, improving accessibility, and signalling demand for new statistics or breakdowns. These recommendations are fed back to the design processes (Section 3), to VS-10 Customer and Stakeholder Engagement, and — where the need originates earlier — across the value chain, prioritized and tracked through subsequent cycles. This is the SAF Capability 4.1.4 (Improve management) in action, and it connects to the GAMSO concept of transferring mature capabilities from innovation into production.

| Activity | Key Outputs | Framework Ref |
|---|---|---|
| Analyze usage, satisfaction, and quality trends across cycles | Improvement Recommendations Report | SAF 4.1.4 |
| Identify improvement opportunities: channels, documentation, accessibility, release process | Updated Design Inputs | SAF 4.1.4 |
| Feed recommendations back to design, VS-10, and the wider chain | Design & engagement feedback (closing the loop) | SAF 4.1.4 |
| Prioritize improvements based on impact and feasibility | Improvement Tracking Log | GAMSO Capability Mgmt |
| Track implementation of accepted improvements | Improvement Tracking Log | GAMSO Capability Mgmt |

```{mermaid}
%%| label: fig-8
%%| fig-cap: "Management Feedback Loop. Execution releases and usage data flow through monitoring, quality assessment, release/channel management, and audit processes. Continuous improvement feeds recommendations back to Design and to VS-10, closing the governance cycle."
%%| fig-width: 6
flowchart TD
    E["Execution\n(Section 5)<br/><em>releases + usage data</em>"]

    M1["6.1 Monitor<br/>Process Performance<br/><em>punctuality, reach</em>"]
    M2["6.2 Assess<br/>Dissemination Quality<br/><em>accessibility, clarity</em>"]
    M3["6.3 Manage Release<br/>& Channel Lifecycle<br/><em>channels, versions</em>"]
    M4["6.4 Audit &<br/>Compliance Reporting<br/><em>disclosure, equal access</em>"]
    M5["6.5 Continuous<br/>Improvement<br/><em>recommendations</em>"]

    D["Design<br/>(Section 3)<br/><em>updated strategy & channels</em>"]
    V10["VS-10.0\nEngagement"]

    E --> M1
    E --> M2
    M1 --> M2
    M2 --> M3
    M3 --> M4
    M4 --> M5
    M5 -->|"feedback loop"| D
    M5 -->|"user insight"| V10

    M1 -->|"dashboards"| PO["Process Owner"]
    M2 -->|"quality reports"| QM["Quality Manager"]
    M4 -->|"compliance reports"| VS07["VS-07.0\nGovernance"]

    style E fill:#ecfdf5,stroke:#059669
    style D fill:#f5f3ff,stroke:#7c3aed
    style M5 fill:#fef3c7,stroke:#d97706
```

## Business Services and Interfaces

The VS-06.0 business domain exposes the following services:

| Service | Direction | Consumers | Mapped Processes |
|---|---|---|---|
| **Dissemination Preparation Service** | Internal (VS-05.0 → NSO) | Approved-product consumers, release teams | 5.2 Prepare Data for Dissemination |
| **Publication and Open-Data Service** | NSO → External | Data users, the public, businesses | 5.3 Publish and Provide Access Services |
| **API and Dashboard Service** | NSO → External | Researchers, developers, analysts | 5.3 Publish and Provide Access Services |
| **Secure Research Access Service** | NSO → External (mediated) | Accredited researchers | 5.3 Publish and Provide Access Services |
| **User Support Service** | NSO → External | All data users | 5.4 Support and Engage Users |
| **Usage and Feedback Service** | Internal ↔ External | Process owners, VS-10, the wider chain | 5.5 Monitor Usage and Feedback |
| **Design and Strategy Service** | Internal | Dissemination managers, channel designers | 3.1–3.5 All design processes |

**Interface specifications:**

- **Publication and Open-Data Service** interface: web publication + bulk open-data download with machine-readable metadata; equal-access release timing enforced
- **API and Dashboard Service** interface: SDMX-compliant API (query released series/datasets + metadata) and interactive dashboards fed from the released datasets
- **Secure Research Access Service** interface: mediated access to de-identified microdata in a controlled environment with output checking

### Boundary Interface Specifications

The domain is loosely coupled (SAF-P07) to its neighbor upstream and to external users. Specifying each boundary explicitly — the handover artefact, the metadata it must carry, the event that triggers it, and where responsibility transfers — makes the loose-coupling contract concrete and testable. As the final primary value stream, VS-06 has **no downstream primary value stream**: its handover is to external users (State #5 → State #6), and its feedback path runs to VS-10.

| Boundary | Handover Artefact | Required Metadata | Trigger Event | Responsibility Transfer |
|---|---|---|---|---|
| **VS-05.0 → VS-06.0** (intake) | Approved Statistical Product (State #4) | Component lineage, composition method, propagated accuracy, coherence results, approval record, confidentiality status, product-version identifier, BIV classification | "Statistical Product Registered" event | VS-05.0 retains custody of the product version; VS-06.0 assumes responsibility for preparation, release, and service delivery on event receipt |
| **VS-06.0 → Users/Society** (release) | Released Data (State #5): published statistics + de-identified microdata + access services | Final disclosure-control record, documentation/methodology notes, reference & structural metadata, channel/format, release timestamp, release-version identifier, lineage to approved product | "Statistics Released" event | NSO publishes/serves; external users consume the data as **State #6 (Consumed)**, outside NSO control. Usage and feedback flow back to VS-06.5 and VS-10. |

Each interface exchanges a registered, immutable steady-state artefact plus its metadata — never internal working data — so neither side needs knowledge of the other's internal processing.

## Business Objects and Data Flow

```{mermaid}
%%| label: fig-9
%%| fig-cap: "Business Object Lifecycle across all four process types. Design objects govern implementation, which produces the pipeline that releases execution objects; the approved product becomes released data and then consumed data, assessed by management objects that feed back to design."
%%| fig-width: 6
flowchart TB
    design["🔷 Design Artefacts<br/><small>Access Strategy · Release SDC Rules<br/>Service & Documentation Specs · Governance Policy</small>"]
    implement["🔧 Implementation Assets<br/><small>Publication & Access Channels · SDC & Release Tooling<br/>Documentation, Support & Monitoring</small>"]
    execute["⚡ Execution Objects"]
    manage["📊 Management Reports"]

    design -->|"govern building"| implement
    implement -->|"produces pipeline<br/>that processes"| execute
    execute -->|"assessed by"| manage
    manage -->|"feeds back to"| design

    subgraph execute_detail [" "]
        direction LR
        SP["Approved Product<br/>(State #4)"]:::bo -->|"released as"| RD["Released Data<br/>(State #5)"]:::bo -->|"consumed as"| CD["Consumed Data<br/>(State #6)"]:::ext
    end

    execute --> execute_detail
    RD -->|generates| logs["Disclosure Record · Documentation · Usage Data"]

    classDef bo fill:#fbbf24,stroke:#b45309,color:#000
    classDef ext fill:#0f766e,stroke:#0f766e,color:#fff
    style design fill:#f5f3ff,stroke:#7c3aed
    style implement fill:#dbeafe,stroke:#2563eb
    style execute fill:#fef9c3,stroke:#b45309
    style manage fill:#dcfce7,stroke:#16a34a
    style execute_detail fill:none,stroke:none
    style logs fill:#fff,stroke:#888,stroke-dasharray: 5 5
```


## Business Events

```{mermaid}
%%| label: fig-10
%%| fig-cap: "Event-Driven Choreography between the upstream domain (VS-05.0), NSO teams, and users, showing events across the Design → Implement → Execute → Manage cycle. The management phase closes the loop by feeding improvements back to design and to VS-10."
%%| fig-width: 6

sequenceDiagram
    participant US as Upstream (VS-05.0)
    participant NSO as NSO Teams
    participant USR as Users
    participant PM as Process Mgmt

    rect rgb(245, 243, 255)
    Note over NSO: Design Phase
    NSO->>NSO: Define access strategy, release & disclosure<br/>policy, channels & support model
    NSO-->>NSO: Design Artefacts Published
    end

    rect rgb(239, 246, 255)
    Note over NSO: Implementation Phase
    NSO->>NSO: Build publication/API channels, SDC &<br/>release tooling, support & monitoring
    NSO-->>NSO: Pipeline Production-Ready
    end

    rect rgb(236, 253, 245)
    Note over NSO,USR: Execution Phase (per release)
    US-->>NSO: Statistical Product Registered event
    NSO->>NSO: Confirm plan; apply final disclosure control

    alt Disclosure gate passed
        NSO->>USR: Publish via channels (managed timing, equal access)
        NSO-->>NSO: Statistics Released event
        USR-->>NSO: Usage & feedback
    else Disclosure gate failed
        NSO->>NSO: Return for additional protection
    end

    NSO->>USR: Provide documentation & support
    end

    rect rgb(254, 243, 199)
    Note over PM: Management Phase
    PM->>PM: Monitor usage & punctuality, assess accessibility,<br/>produce compliance reports
    PM-->>NSO: Improvement Recommendations (to design & VS-10)
    end
```

## Framework Mappings

This reference table maps each process group of this document to the international frameworks (GSBPM, GAMSO, CSDA) and the SAF capability model. It is intended for architects and auditors; the narrative sections above do not depend on it.

| Process group | GSBPM | GAMSO | CSDA | SAF Capabilities |
|---|---|---|---|---|
| **Design** | Phase 1 (Specify Needs), Phase 2 (Design: 2.1–2.5) | Production (design activities), Capability Management | Data Governance, Metadata Management, Dissemination | 1.1.2 Design statistics product, 2.1.2 Metadata management, 3.3.1 Privacy management |
| **Implementation** | Phase 3 (Build: 3.1–3.7) | Capability Management | Dissemination (setup), Data Governance (configuration) | 1.1.3 Build statistics product, 3.2.1 Application development, 3.2.2 Functional management |
| **Execution** | Phase 6 (6.4 Apply disclosure control) + Phase 7 (7.2 Produce dissemination products, 7.3 Manage release, 7.4 Promote, 7.5 Manage user support) + Phase 8 (Evaluate) for usage monitoring | Production (execution), Corporate Support (communication) | Dissemination (execution) | 2.1.2 Metadata management, 3.3.1 Privacy management |
| **Management** | Phase 8 (Evaluate) + Overarching processes (Quality Management, Metadata Management) | Corporate Support (Quality Management, Communication), Capability Management (improvement) | Data Quality, Data Governance, Traceability | 2.1.3 Statistical quality management, 4.1.4 Improve management, 4.1.5 Accountability |

## Applying This to Your NSO

### Maturity Assessment Checklist

Use this checklist to assess your NSO's maturity across all four process types — not just execution.

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

### End-to-End Scenarios

Each scenario walks through **all four process types**, demonstrating how the governance pattern works in practice.

#### Scenario A: Labour Market Quarterly Release

**Design Phase:** The dissemination strategy targets policymakers (press release), researchers (API + series download), and the public (dashboard), with a pre-announced release calendar and a media embargo policy. Final disclosure-control rules for small NUTS-2 cells, accessibility standards, and the documentation standard are designed.

**Implementation Phase:** Engineers configure the publication page, the SDMX API, and the dashboard on the VS-09 platform, the SDC tooling for small-cell suppression, and embargo/equal-access release tooling. Accessibility, disclosure, and release-rehearsal tests pass.

**Execution Phase:** A Statistical Product Registered event arrives for the Q3-2026 labour-market product. The team confirms the plan, applies final SDC (suppressing two small NUTS-2 cells), and clears the disclosure-risk gate. At 09:00 the figures publish simultaneously on the website, API, and dashboard; embargoed media publish at the same moment. Documentation and methodology notes accompany the release; the helpdesk handles queries. Usage and feedback are collected. A Statistics Released event is published.

**Management Phase:** On-time release rate 100%, disclosure-gate passed first time, API availability 99.95%, usage up 12% on the prior quarter. Improvement recommendation: add a plain-language summary after feedback showed confusion about the confidence interval. Recommendations fed back to design and VS-10.

#### Scenario B: Business Statistics — Microdata via Secure Research Environment

**Design Phase:** The strategy provides aggregate tables openly and de-identified business microdata through a secure research environment (SRE) for accredited researchers. The de-identification standard, output-checking rules, and SRE access model are designed with VS-07.

**Implementation Phase:** Engineers configure the open tables on the portal and the SRE access service with output checking on the VS-09 platform; the de-identification component and disclosure gate are configured. Security/disclosure and accessibility tests pass.

**Execution Phase:** A Statistical Product Registered event arrives for the SBS product. Aggregate tables are disclosure-controlled and published openly; the microdata is de-identified to the standard and made available in the SRE. Accredited researchers are onboarded with the data dictionary and methodology; the helpdesk handles output-checking so researchers' exported results also meet disclosure rules. Usage in the SRE is logged. A Statistics Released event is published.

**Management Phase:** Disclosure-gate pass rate 100%, no disclosure incidents, SRE onboarding time within target. Improvement recommendation: add a self-service output-checking pre-screen to reduce helpdesk load. Recommendations fed back to design and VS-10.

#### Scenario C: Consumer Price Index — Headline Release and Dashboard

**Design Phase:** The CPI dissemination strategy provides a headline press release, an API for the series, and an interactive dashboard, on a fixed pre-announced calendar with a tight embargo (price indices are market-sensitive). Accessibility and documentation standards are designed.

**Implementation Phase:** Engineers configure the release page, the API, and the dashboard, plus strict embargo/equal-access release tooling (CPI is market-sensitive). Disclosure (light, aggregated indices), accessibility, and release-rehearsal tests pass.

**Execution Phase:** A Statistical Product Registered event arrives for the monthly CPI product. The plan is confirmed, the light disclosure check passes, and at the scheduled minute the headline, API series, and dashboard go live simultaneously with strict equal access. Documentation explains the monthly movement and contributions; the helpdesk handles media queries. Usage spikes are monitored. A Statistics Released event is published.

**Management Phase:** Punctuality 100% (critical for a market-sensitive release), no embargo breaches, dashboard views at record highs on release day. Improvement recommendation: add a contributions-to-change visual to the dashboard after user feedback. Recommendations fed back to design and VS-10.

## VS-07.0 Governance and Compliance

### Purpose and Scope

VS-07.0 makes sure that every process, dataset, and product in the organization operates under clear rules, standards, and accountability. It builds trust — inside and outside the NSO — by ensuring all data activities are ethical, transparent, and compliant with legal, methodological, and quality requirements, aligned with standards such as the **European Statistics Code of Practice, GDPR, GSBPM, GAMSO, and ISO** data-quality principles. The value it creates is **integrity and accountability**.

This document covers the business layer only: the governance capabilities, how they are established and operated, and how they interact with the rest of the value chain. The specific application and technology controls that implement them are out of scope (provided with VS-09).



*A note on numbering:* each `VS-0x.y` below is both a value stream stage (*what value* is added) and a business process (*how* it is done); the numbering maps one-to-one. See the key-concepts box above.

### Position — a supporting stream that works across the whole chain

VS-07 is not a stage in the production line. It runs **horizontally** across all six primary streams, setting the rules they must follow and collecting the evidence that they do.

```{mermaid}
%%| label: fig-1
%%| fig-cap: "VS-07 governs the whole primary value chain horizontally; it is not a step within it."
%%| fig-width: 6
flowchart TD
    subgraph primary["Primary Value Streams"]
        direction LR
        VS01["VS-01"] --> VS02["VS-02"] --> VS03["VS-03"] --> VS04["VS-04"] --> VS05["VS-05"] --> VS06["VS-06"]
    end

    VS07["**VS-07.0 Governance & Compliance**"]:::hi
    VS07 -->|"sets rules & controls,<br/>collects compliance evidence"| primary

    classDef hi fill:#7c3aed,color:#fff,stroke:#6d28d9,stroke-width:2px
```

::: {.callout-important title="How a supporting value stream differs from a primary one"}
- **No steady-state data transition.** VS-07 does not take data from one steady state to the next; it does not appear in the #1→#6 chain. It oversees the streams that do.
- **It runs continuously**, not per production cycle — there is no "Data Registered" event that triggers it.
- **Its output is an enabling capability, not a data artefact:** governance frameworks, compliance mechanisms, assurance, and audit results.
- **It aligns to GAMSO** (the over-arching activity model) rather than to GSBPM production phases.
:::

### How It Interacts with the Production Chain

VS-07 interacts with every other stream in two directions: **downward** it imposes governance frameworks, policies, and controls; **upward** it receives compliance evidence, quality indicators, and audit findings. The primary streams' own audit-and-compliance reporting (their §6.4) feeds directly into VS-07.

```{mermaid}
%%| label: fig-2
%%| fig-cap: "Interaction with the chain: VS-07 sets controls and consumes evidence across the chain, and provides external assurance."
%%| fig-width: 6
flowchart LR
    VS07["VS-07<br/>Governance &<br/>Compliance"]:::hi

    subgraph chain["All value streams (VS-01…VS-10)"]
        P["Processes, datasets,<br/>products & platforms"]
    end

    VS07 -->|"frameworks, policies,<br/>roles, controls"| P
    P -->|"compliance evidence,<br/>quality indicators, audit findings"| VS07
    VS07 -->|"certification &<br/>assurance"| EXT["Regulators, the public,<br/>international peers"]

    classDef hi fill:#7c3aed,color:#fff,stroke:#6d28d9
    style EXT fill:#0f766e,color:#fff,stroke:#0f766e
```

### Framework Alignment (GAMSO)

Where the primary streams map to **GSBPM** production phases, VS-07 maps to the **GAMSO** over-arching activities and the **Governance** capability domain of the SAF:

| GAMSO area | Relevance to VS-07 |
|---|---|
| **Strategy and Leadership** | Set governance strategy, charters, and accountability; manage organizational and ethical frameworks |
| **Corporate Support** | Manage the legal framework, quality management, and information security governance |
| **Capability Management** | Govern the lifecycle of standards, methods, and data assets |
| **SAF capability domain: Governance (4.x)** | Strategy & governance, policy & planning, improvement management, accountability |

### Principles Emphasised

VS-07 is the stream that **enforces the data principles across the whole chain** and embodies several of the broader architecture principles:

| Principle | Statement | How VS-07 applies / enforces it |
|---|---|---|
| **SAF-P09** | No data without metadata and classification | Governs metadata and classification obligations and audits them across every stream |
| **SAF-P10** | Security By Design | Sets and assures the information-security and access-control framework |
| **SAF-P11** | Privacy By Design | Sets the privacy, confidentiality, and disclosure-control policy and verifies compliance |
| **SAF-P03** | Active Life Cycle management | Governs the lifecycle of policies, standards, classifications, and data assets |
| **SAF-P04** | Maximize the benefits for the organization | Aligns controls to organizational value and accountability, avoiding governance for its own sake |
| **SAF-P07** | Implement loosely coupled processes and systems | Defines the steady-state interface and event conventions the streams are governed by |

## Roles and Actors



| Role | Description |
|---|---|
| **Chief Data / Governance Officer** | Accountable for the governance framework and organizational data policy |
| **Compliance Officer** | Ensures legal and regulatory compliance (Code of Practice, GDPR, statistics law) |
| **Data Owner / Steward / Custodian** | The data-governance roles VS-07 defines and assigns across domains |
| **Quality Manager** | Defines quality indicators and monitors quality and compliance status |
| **Internal / External Auditor** | Conducts audits and certifications of adherence to the frameworks |
| **Legal Counsel** | Interprets regulation and frames compliance procedures |
| **Process Owners (VS-01…VS-10)** | Accountable, in their own streams, for operating within VS-07's controls and supplying evidence |

## The Value-Stream Flow

VS-07's six business processes form a continuous governance loop — **plan → build → operate → improve** — that never stops running.

```{mermaid}
%%| label: fig-3
%%| fig-cap: "The six business processes as a continuous governance loop."
%%| fig-width: 6
flowchart LR
    A["07.1 Define<br/>Frameworks & Policies"] --> B["07.2 Establish Legal &<br/>Regulatory Compliance"]
    B --> C["07.3 Implement Data &<br/>Metadata Governance"]
    C --> D["07.4 Monitor Quality &<br/>Compliance Indicators"]
    D --> E["07.5 Audit, Certify<br/>& Report"]
    E --> F["07.6 Update & Improve<br/>Governance"]
    F -.->|"continuous loop"| A

    style A fill:#f5f3ff,stroke:#7c3aed
    style B fill:#f5f3ff,stroke:#7c3aed
    style C fill:#eff6ff,stroke:#2563eb
    style D fill:#ecfdf5,stroke:#059669
    style E fill:#ecfdf5,stroke:#059669
    style F fill:#fef3c7,stroke:#d97706
```

::: {.callout-note title="Model note"}
The strategy model labels two steps `VS-07.5`. They are distinct activities; this document treats them as **VS-07.5 Audit, Certify, and Report Compliance** and **VS-07.6 Update and Improve Governance Mechanisms**.
:::

**Plan — establish the rules.** The loop begins by **defining governance frameworks and policies** (07.1): the overarching charters and principles covering data, metadata, ethics, confidentiality, and statistical quality — the rule-book the whole organization works under. In parallel it **establishes legal and regulatory compliance mechanisms** (07.2): identifying the applicable regulations (GDPR, official-statistics legislation, data-sharing agreements) and defining the procedures that keep every process within the law.

**Build — embed the controls.** The frameworks are made operational by **implementing data and metadata governance** (07.3): assigning the data-governance roles (owner, steward, custodian) and the processes for metadata creation, maintenance, and lineage tracking, so governance is wired into how the streams actually work rather than living only on paper.

**Operate — assure continuously.** With controls in place, VS-07 **monitors quality and compliance indicators** (07.4) — measuring process and output quality (accuracy, timeliness, comparability) and tracking compliance status on formal scorecards and dashboards — and periodically **audits, certifies, and reports compliance** (07.5): conducting internal and external audits, performing quality reviews, and documenting adherence, which produces the assurance that statistics can be trusted.

**Improve — close the loop.** Finally it **updates and improves the governance mechanisms** (07.6): incorporating feedback, regulatory changes, and lessons learned back into the policies and control frameworks — so governance evolves with the organization rather than ossifying.

| Business process | What it produces |
|---|---|
| VS-07.1 Define Governance Frameworks and Policies | Governance charters and policies (data, metadata, ethics, confidentiality, quality) |
| VS-07.2 Establish Legal and Regulatory Compliance Mechanisms | Compliance procedures mapped to applicable regulation |
| VS-07.3 Implement Data and Metadata Governance | Assigned governance roles + metadata/lineage processes |
| VS-07.4 Monitor Quality and Compliance Indicators | Quality & compliance dashboards/scorecards |
| VS-07.5 Audit, Certify, and Report Compliance | Audit reports, certifications, assurance statements |
| VS-07.6 Update and Improve Governance Mechanisms | Revised policies and controls reflecting change |

## Capability Governance

VS-07 is itself a capability that must be **designed** (its frameworks and operating model), **built** (roles, tooling, dashboards — with VS-09), **operated** (continuous monitoring and periodic audit), and **improved** (07.6). Unlike a primary stream it runs **continuously and organization-wide**, not as a per-cycle production run, and it produces assurance rather than statistical data.

### Key Performance Indicators

VS-07 monitors itself with the same discipline it imposes on the chain:

| KPI | Description | Measurement |
|---|---|---|
| Policy coverage | Share of streams and data domains operating under current, approved policies | Per policy domain, annually |
| Audit findings closed on time | Percentage of audit findings remediated within their agreed deadline | Per audit cycle |
| Compliance incidents | Number of confidentiality, security, or legal incidents | Per quarter (target: zero) |
| Certification status | Certifications and peer-review assessments held and current (e.g. Code of Practice) | Annually |
| Metadata-governance compliance | Share of registered datasets meeting the SAF-P09 obligations | Per cycle, from the streams' compliance evidence (their §6.4) |
| Regulatory response time | Time from detection of a regulatory change to an updated policy being issued | Per change |

## Interactions, Services and Events

VS-07 offers governance and assurance as a service to every other stream.

| Counterpart | VS-07 provides | VS-07 receives | Interaction / event |
|---|---|---|---|
| **All primary streams (VS-01…06)** | Frameworks, policies, data-governance roles, controls | Compliance evidence, quality indicators, audit findings (their §6.4) | "Compliance review", "Audit", "Policy update issued" |
| **VS-08 Innovation** | Compliance criteria a new method must meet | Requests to assess/approve new methods before production | "Method compliance assessment" |
| **VS-09 Infrastructure** | Security & continuity policy to enforce | Security posture and incident evidence | "Security/continuity review" |
| **VS-10 Engagement** | Transparency & accountability commitments | Stakeholder trust signals and complaints | "Transparency report" |
| **External (regulators, public, peers)** | Certification, assurance, transparency reports | Regulatory requirements and changes | "Certification", "Regulatory change" |

## Business Objects / Artefacts

VS-07 manages enabling artefacts, not data states: the **governance framework & policy set**, the **regulatory compliance register**, the **data-governance role assignments and metadata/lineage rules**, the **quality & compliance dashboards**, and the **audit/certification reports**. These are referenced by every stream. Each artefact has a designated owner and is version-managed across its lifecycle (SAF-P03): changes are tracked, prior versions remain identifiable, and obsolete policies and controls are formally retired.

## Applying This to Your NSO

### Maturity Assessment Checklist

- [ ] Do we have documented governance frameworks and policies covering data, metadata, ethics, confidentiality, and quality?
- [ ] Have we mapped applicable regulation (GDPR, statistics law) to concrete compliance procedures?
- [ ] Are data-governance roles (owner, steward, custodian) assigned and metadata/lineage processes in place?
- [ ] Do we monitor quality and compliance on dashboards, and audit/certify periodically?
- [ ] Is there a closed loop that feeds audit findings and regulatory change back into the frameworks?

### Scenarios

**Scenario A — A new regulation lands.** A change to data-protection law is detected (07.2/07.6). VS-07 assesses the impact, updates the privacy and confidentiality policy, issues a "Policy update" to all streams, and verifies adoption at the next audit — the chain stays compliant without each stream interpreting the law independently.

**Scenario B — Pre-production method approval.** VS-08 proposes a new machine-learning coding method. VS-07 assesses it against the compliance criteria (privacy, transparency, quality) before VS-08's 08.5 transfer to production, certifies it, and records the decision — so only sound, compliant methods reach the production streams.

**Scenario C — Preparing a Code of Practice peer review.** Ahead of the periodic European Statistics Code of Practice peer review, VS-07 assembles the evidence base from its dashboards and the streams' compliance reporting (07.4/07.5): policy register, audit trail summaries, quality indicators, and incident records. Gaps surfaced by the self-assessment — say, an outdated revision policy — are remediated through 07.6 before the review. The peer-review outcome and its recommendations enter the governance backlog, and the resulting certification is published as external assurance.


## VS-08.0 Innovation and Methodological Development

### Purpose and Scope

VS-08.0 makes sure the statistical organization does not stand still. Its purpose is to discover, test, and introduce new ways of working — new data sources, methods, tools, and technologies — and to move the organization from "we have always done it this way" to "we can do this better, faster, and smarter." It connects research, methodology, IT, and business users, and it keeps innovation **controlled**, so that only methods that are sound, documented, and compliant end up in production. The value it creates is **continuous improvement** — keeping the SAF future-proof for new data (IoT, administrative, data spaces) and new techniques (ML, small-area estimation).



*A note on numbering:* each `VS-0x.y` below is both a value stream stage (*what value* is added) and a business process (*how* it is done); the numbering maps one-to-one. See the key-concepts box above.

### Position — a supporting stream that works across the whole chain

VS-08 is not a stage in the production line. It runs alongside it as a pipeline that **feeds improvements into** every primary stream and draws its agenda from their needs.

```{mermaid}
%%| label: fig-1
%%| fig-cap: "VS-08 draws needs from the chain and delivers validated methods back into it."
%%| fig-width: 6
flowchart TD
    subgraph primary["Primary Value Streams"]
        direction LR
        VS01["VS-01"] --> VS02["VS-02"] --> VS03["VS-03"] --> VS04["VS-04"] --> VS05["VS-05"] --> VS06["VS-06"]
    end

    VS08["**VS-08.0 Innovation &<br/>Methodological Development**"]:::hi
    primary -->|"improvement needs"| VS08
    VS08 -->|"validated methods & tools<br/>transferred to production"| primary

    classDef hi fill:#7c3aed,color:#fff,stroke:#6d28d9,stroke-width:2px
```

::: {.callout-important title="How a supporting value stream differs from a primary one"}
- **No steady-state data transition.** VS-08 does not move data from one state to the next; it improves the *methods and tools* the production streams use.
- **It runs continuously**, as a research-and-development pipeline, not per production cycle.
- **Its output is an enabling capability, not a data artefact:** validated methods, documented tools, reference implementations, and trained staff.
- **It aligns to GAMSO Capability Management**, not to GSBPM production phases.
:::

### How It Interacts with the Production Chain

VS-08 has a distinctive two-way relationship with the chain. The improvement recommendations every primary stream produces (their §6.5 continuous-improvement loops), together with user needs surfaced by VS-10, form VS-08's **innovation backlog**. After research and evaluation, the famous **transfer gate (08.5)** moves a validated method or tool **into** the relevant production stream — gated by VS-07 compliance approval and enabled by VS-09 platforms.

```{mermaid}
%%| label: fig-2
%%| fig-cap: "Interaction with the chain: needs in, validated methods out (through a governed transfer gate)."
%%| fig-width: 6
flowchart LR
    SRC["Improvement needs<br/>(VS-01…06 §6.5)<br/>+ user needs (VS-10)<br/>+ external tech scan"] --> VS08["VS-08<br/>Innovation"]:::hi
    VS08 -->|"08.5 transfer<br/>(validated method/tool)"| PROD["Target production<br/>stream (e.g. VS-03/04)"]
    VS07["VS-07 Governance"] -.->|"compliance approval"| VS08
    VS09["VS-09 Infrastructure"] -.->|"sandbox & production platforms"| VS08

    classDef hi fill:#7c3aed,color:#fff,stroke:#6d28d9
```

### Framework Alignment (GAMSO)

Where the primary streams map to **GSBPM** production phases, VS-08 maps to **GAMSO Capability Management** and the SAF's research/capability foundations:

| GAMSO area | Relevance to VS-08 |
|---|---|
| **Capability Management** | Manage research & innovation, develop methodology, manage change, build staff capability |
| **Strategy and Leadership** | Set the innovation agenda aligned to organizational strategy |
| **SAF capabilities** | Statistical design & build (methodology), research; supports all primary capabilities |

### Principles Emphasised

| Principle | Statement | How VS-08 applies it |
|---|---|---|
| **SAF-P01** | Actively participate in open source to maintain collective control over statistical processes | Innovate on and contribute to shared, open methods and tools rather than vendor black boxes |
| **SAF-P05** | IT and technology is everyone's business | Connect research, methodology, IT, and business users; build broad capability to adopt new methods |
| **SAF-P03** | Active Life Cycle management | Manage methods and tools across their lifecycle, from PoC to production to retirement |
| **SAF-P04** | Maximize the benefits for the organization | Prioritize innovations by organization-wide value and scalability, not novelty |
| **SAF-P07** | Implement loosely coupled processes and systems | Transfer methods that fit the steady-state interfaces, so production streams stay decoupled |

## Roles and Actors



| Role | Description |
|---|---|
| **Head of Methodology / Innovation** | Owns the innovation agenda and the methodological standards |
| **Researcher / Data Scientist** | Conducts research and proofs-of-concept |
| **Methodologist** | Evaluates soundness and feasibility; formalizes validated methods |
| **Tool / Platform Engineer** | Builds reference implementations and prepares them for production (with VS-09) |
| **Subject-Matter Expert (from production streams)** | Brings the real problem and validates fitness for purpose |
| **Compliance Officer (VS-07)** | Approves a method against compliance criteria before transfer |
| **Trainer / Knowledge Manager** | Disseminates results and builds staff competency |

## The Value-Stream Flow

VS-08's six business processes form a continuous innovation pipeline — **identify → research → evaluate → develop → integrate → share**.

```{mermaid}
%%| label: fig-3
%%| fig-cap: "The six business processes as a continuous innovation pipeline."
%%| fig-width: 6
flowchart LR
    A["08.1 Identify<br/>Needs & Opportunities"] --> B["08.2 Research<br/>& Proof-of-Concept"]
    B --> C["08.3 Evaluate<br/>Soundness & Feasibility"]
    C --> D["08.4 Develop &<br/>Document Methods/Tools"]
    D --> E["08.5 Integrate into<br/>Production"]
    E --> F["08.6 Promote<br/>Knowledge Sharing"]
    F -.->|"feeds the next agenda"| A

    style A fill:#f5f3ff,stroke:#7c3aed
    style B fill:#f5f3ff,stroke:#7c3aed
    style C fill:#eff6ff,stroke:#2563eb
    style D fill:#eff6ff,stroke:#2563eb
    style E fill:#ecfdf5,stroke:#059669
    style F fill:#fef3c7,stroke:#d97706
```

**Plan — find what is worth doing.** The pipeline begins by **identifying innovation needs and opportunities** (08.1): scanning technological, methodological, and policy developments (AI, ML, new data sources, cloud) and the chain's own improvement backlog for things worth pursuing. Candidates then enter **research and proofs-of-concept** (08.2): controlled experiments and pilots that test a new method or technology in limited scope before any commitment.

**Build — make it sound and real.** Promising results are put through **evaluation of methodological soundness and feasibility** (08.3): assessing accuracy, scalability, and alignment with quality and ethical frameworks — the gate that stops attractive-but-unsound ideas. What passes is **developed and documented** (08.4) into standardized procedures, algorithms, or reference implementations, so it is reproducible and ready to hand over rather than living in a researcher's notebook.

**Operate — put it to work.** The defining step is **integrating innovation into production environments** (08.5): transitioning a validated method or tool from pilot to production in the relevant primary stream, ensuring interoperability and — crucially — passing VS-07 governance approval and running on VS-09 platforms. This is the transfer gate where innovation becomes part of business as usual.

**Improve — spread it.** Finally VS-08 **promotes knowledge sharing and capability building** (08.6): disseminating results, best practices, and guidelines, and growing staff competency so the organization can actually adopt and sustain the new way of working — which in turn surfaces the next round of needs.

| Business process | What it produces |
|---|---|
| VS-08.1 Identify Innovation Needs and Opportunities | Prioritized innovation backlog |
| VS-08.2 Conduct Research and Proof-of-Concepts | Experiment/pilot results |
| VS-08.3 Evaluate Methodological Soundness and Feasibility | Soundness & feasibility assessment |
| VS-08.4 Develop / Document New Methodologies or Tools | Standardized method + reference implementation + documentation |
| VS-08.5 Integrate Innovation into Production Environments | Method/tool live in a production stream (governed transfer) |
| VS-08.6 Promote Knowledge Sharing and Capability Building | Disseminated guidance + trained staff |

## Capability Governance

VS-08 is itself a capability that is **designed** (innovation strategy, evaluation criteria), **built** (research/sandbox environments — with VS-09), **operated** (the pipeline runs continuously), and **improved** (08.6 and retrospectives). Unlike a primary stream it produces **methods and capability**, not statistical data, and its cadence is project/pipeline-based, not per production cycle. The GAMSO notion of transferring mature capabilities from innovation into production is exactly step 08.5.

### Key Performance Indicators

| KPI | Description | Measurement |
|---|---|---|
| Idea-to-production lead time | Median time from a backlog item (08.1) to a completed transfer (08.5) | Per transferred innovation |
| Transfer rate and durability | Methods/tools transferred to production per year, and the share still in use after 12 months | Annually |
| Gate effectiveness | Share of PoCs stopped at the 08.3 gate with a documented rationale (a healthy gate stops some) | Per evaluation |
| Backlog responsiveness | Share of prioritized backlog items reaching a PoC within the agreed time | Per planning period |
| Capability building | Staff trained on new methods, and adoption rate in the target streams | Per year, per transfer |

## Interactions, Services and Events

| Counterpart | VS-08 provides | VS-08 receives | Interaction / event |
|---|---|---|---|
| **All primary streams (VS-01…06)** | Validated methods/tools transferred to production | Improvement recommendations (their §6.5); fitness-for-purpose validation | "Innovation need raised", "Method transferred to production" |
| **VS-10 Engagement** | New service/product possibilities | User needs that imply new methods | "User-driven innovation need" |
| **VS-07 Governance** | Methods for pre-production approval | Compliance criteria & approval | "Method compliance assessment" |
| **VS-09 Infrastructure** | Requirements for sandbox/production platforms | Research environments and production runtime | "Platform request", "Production onboarding" |

## Business Objects / Artefacts

VS-08 manages enabling artefacts: the **innovation backlog**, **research findings and PoC results**, **soundness/feasibility assessments**, **validated methods, algorithms, and reference implementations**, and **knowledge assets** (guidelines, training). These are version-managed across their lifecycle (SAF-P03) and, once transferred, become part of a production stream's design metadata. Each artefact has a designated owner; changes are tracked, prior versions remain identifiable, and superseded methods are formally retired.

## Applying This to Your NSO

### Maturity Assessment Checklist

- [ ] Do we maintain a prioritized innovation backlog drawn from both technology scanning and the production streams' improvement needs?
- [ ] Do we test new methods in controlled PoCs before committing?
- [ ] Do we evaluate soundness, scalability, and ethics before development?
- [ ] Is there a governed transfer gate (with VS-07 approval) for moving methods into production?
- [ ] Do we disseminate results and build staff capability so innovations are sustained?

### Scenarios

**Scenario A — ML-assisted coding.** A production stream (VS-03) repeatedly flags free-text occupation coding as costly. VS-08 picks this up (08.1), pilots an ML coder (08.2), evaluates accuracy and bias (08.3), builds a documented reference implementation (08.4), and — after VS-07 approval and on a VS-09 platform — transfers it into VS-03 (08.5), then trains the coding team (08.6).

**Scenario B — New data source (web-scraped prices).** VS-10 reports demand for more timely price statistics. VS-08 researches web-scraping and multilateral index methods, evaluates feasibility and quality against the official CPI, documents the method, and transfers it into VS-01/VS-04, sharing the methodology across the price-statistics team.

**Scenario C — The gate says no.** A vendor demo convinces a statistical domain that a generative-AI assistant could draft analytical commentary (VS-05). VS-08 takes it through the pipeline: the PoC (08.2) shows impressive fluency, but the evaluation (08.3) finds unexplainable variation between runs and no way to meet the methodological-transparency requirement, and VS-07's compliance pre-assessment concurs. The idea is stopped at the gate, the rationale is documented and shared (08.6), and a narrower, compliant alternative — template-based drafting with human sign-off — is added to the backlog. A healthy 08.3 gate is one that sometimes says no.

## VS-09.0 Infrastructure and Platform Enablement

### Purpose and Scope

VS-09.0 provides the technical and digital foundation that supports every part of the statistical organization. Where the other streams focus on data, methods, or governance, this one ensures all of those activities can actually **run** — safely, efficiently, and at scale. It delivers the IT environments, data platforms, tools, and integration services that make statistical production possible from collection to dissemination, keeping systems secure, resilient, and compliant while remaining flexible enough to adopt new technologies. The value it creates is **reliable enablement** — turning infrastructure from a background function into an active enabler of the statistical mission.

This document is the **business-layer** view of that enablement (the capability of providing platforms and services). The detailed application and technology architecture is the subject of the SAF's application and technology layers.



*A note on numbering:* each `VS-0x.y` below is both a value stream stage (*what value* is added) and a business process (*how* it is done); the numbering maps one-to-one. See the key-concepts box above.

### Position — a supporting stream that works across the whole chain

VS-09 is not a stage in the production line. It is the **foundation underneath** all of it: every primary and supporting stream runs on the platforms it provides.

```{mermaid}
%%| label: fig-1
%%| fig-cap: "VS-09 is the technical foundation every other stream runs on."
%%| fig-width: 6
flowchart TD
    subgraph primary["Primary Value Streams"]
        direction LR
        VS01["VS-01"] --> VS02["VS-02"] --> VS03["VS-03"] --> VS04["VS-04"] --> VS05["VS-05"] --> VS06["VS-06"]
    end
    other["Supporting streams<br/>VS-07 · VS-08 · VS-10"]

    VS09["**VS-09.0 Infrastructure &<br/>Platform Enablement**"]:::hi
    VS09 -->|"platforms, environments,<br/>integration & continuity"| primary
    VS09 -->|"runtime & tooling"| other

    classDef hi fill:#7c3aed,color:#fff,stroke:#6d28d9,stroke-width:2px
```

::: {.callout-important title="How a supporting value stream differs from a primary one"}
- **No steady-state data transition.** VS-09 does not move data along the chain; it provides the environments in which the chain runs.
- **It runs continuously** as an always-on service, not per production cycle.
- **Its output is an enabling capability, not a data artefact:** platforms, environments, integration services, and assured availability.
- **It aligns to GAMSO Capability Management and Corporate Support**, not to GSBPM production phases.
:::

### How It Interacts with the Production Chain

VS-09 receives requirements (from business capabilities, data volumes, and the other streams — notably VS-08 for new technology and VS-06 for dissemination platforms) and provides the platforms, integration services, and operational assurance the whole organization depends on. Its security and continuity posture is governed by VS-07.

```{mermaid}
%%| label: fig-2
%%| fig-cap: "Interaction with the chain: requirements in; platforms, integration, and assured availability out."
%%| fig-width: 6
flowchart LR
    REQ["Requirements<br/>(business capabilities,<br/>data volumes, VS-08 tech,<br/>VS-06 channels)"] --> VS09["VS-09<br/>Infrastructure &<br/>Platform Enablement"]:::hi
    VS09 -->|"environments, platforms,<br/>integration, availability"| ALL["All value streams<br/>(VS-01…VS-10)"]
    VS07["VS-07 Governance"] -.->|"security & continuity policy"| VS09
    ALL -.->|"incidents, capacity demand"| VS09

    classDef hi fill:#7c3aed,color:#fff,stroke:#6d28d9
```

### Framework Alignment (GAMSO)

Where the primary streams map to **GSBPM** production phases, VS-09 maps to **GAMSO** capability and support activities and the SAF **supporting-business** capability domain (IT):

| GAMSO area | Relevance to VS-09 |
|---|---|
| **Capability Management** | Manage IT capability; introduce and modernize technology |
| **Corporate Support** | Manage IT services and operations, security, and business continuity |
| **SAF capability domain: Supporting business (3.x)** | Computerization & automation (application development, functional management); security & privacy (technical) |

### Principles Emphasised

| Principle | Statement | How VS-09 applies it |
|---|---|---|
| **SAF-P10** | Security By Design | Builds security and access control into every platform and environment from the start |
| **SAF-P06** | Business Continuity | Guarantees availability, resilience, and disaster recovery for the whole chain |
| **SAF-P02** | Active support | Runs platforms as actively-supported, monitored services, not one-off builds |
| **SAF-P05** | IT and technology is everyone's business | Provides self-service, well-documented platforms so technology serves all teams |
| **SAF-P01** | Actively participate in open source to maintain collective control over statistical processes | Favours open, shared platform components to retain collective control |

## Roles and Actors



| Role | Description |
|---|---|
| **Chief Technology / Infrastructure Officer** | Accountable for the technical foundation and its strategy |
| **Platform / Cloud Architect** | Designs the platform and infrastructure architecture |
| **DevOps / Platform Engineer** | Provisions, configures, and operates environments |
| **Integration Engineer** | Builds APIs, workflow engines, and orchestration |
| **Security & Continuity Officer** | Implements security controls, monitoring, and disaster recovery (with VS-07) |
| **Service Desk / Operations** | Runs incident management and keeps services available |
| **Consuming teams (VS-01…VS-10)** | Define requirements and run their processes on the platforms |

## The Value-Stream Flow

VS-09's six business processes form a continuous enablement lifecycle — **define → design → provision → integrate → assure → evolve**.

```{mermaid}
%%| label: fig-3
%%| fig-cap: "The six business processes as a continuous enablement lifecycle."
%%| fig-width: 6
flowchart LR
    A["09.1 Define Digital &<br/>Technical Requirements"] --> B["09.2 Design Platform &<br/>Infrastructure Architecture"]
    B --> C["09.3 Provision &<br/>Configure Platforms"]
    C --> D["09.4 Enable Integration<br/>& Orchestration"]
    D --> E["09.5 Ensure Performance,<br/>Security & Continuity"]
    E --> F["09.6 Evolve &<br/>Modernize"]
    F -.->|"continuous lifecycle"| A

    style A fill:#f5f3ff,stroke:#7c3aed
    style B fill:#f5f3ff,stroke:#7c3aed
    style C fill:#eff6ff,stroke:#2563eb
    style D fill:#eff6ff,stroke:#2563eb
    style E fill:#ecfdf5,stroke:#059669
    style F fill:#fef3c7,stroke:#d97706
```

**Plan — understand what is needed.** The lifecycle begins by **defining digital and technical requirements** (09.1): identifying the infrastructure needs arising from business capabilities, data volumes, and analytical complexity across the streams. These feed the **design of the platform and infrastructure architecture** (09.2): blueprints for data storage, processing, integration, and secure access (data fabric, data market, compute platforms).

**Build — stand it up.** The architecture is realized by **provisioning and configuring platforms** (09.3): deploying environments (on-premise, hybrid, or cloud) with the necessary governance, monitoring, and security controls, and by **enabling integration and orchestration services** (09.4): the APIs, workflow engines, and automation that connect the business services and processes — including the steady-state event interfaces the primary streams rely on.

**Operate — keep it running and safe.** Day to day, VS-09 **ensures performance, security, and continuity** (09.5): monitoring platform performance, implementing data protection, managing incidents, and guaranteeing availability and disaster recovery — the assurance that the whole chain can run reliably.

**Improve — modernize.** Finally it **evolves and modernizes the technical ecosystem** (09.6): introducing new technologies (often transferred from VS-08), retiring obsolete components, and keeping the foundation flexible for new data sources and operating models.

| Business process | What it produces |
|---|---|
| VS-09.1 Define Digital and Technical Requirements | Infrastructure requirements derived from business needs |
| VS-09.2 Design Platform and Infrastructure Architecture | Architecture blueprints (storage, processing, integration, access) |
| VS-09.3 Provision and Configure Platforms | Deployed, controlled environments |
| VS-09.4 Enable Integration and Orchestration Services | APIs, workflow/automation, event interfaces |
| VS-09.5 Ensure Performance, Security, and Continuity | Monitoring, security, availability, disaster recovery |
| VS-09.6 Evolve and Modernize the Technical Ecosystem | Modernization roadmap and adopted technologies |

## Capability Governance

VS-09 is itself a capability that is **designed** (architecture and operating model), **built** (provisioning and integration), **operated** (continuous monitoring, security, and incident management), and **improved** (09.6). Unlike a primary stream it produces **platforms and assured availability**, not statistical data, and runs as an **always-on service** rather than a per-cycle production run. Its security and continuity are governed by VS-07.

### Key Performance Indicators

| KPI | Description | Measurement |
|---|---|---|
| Platform availability | Measured availability against the agreed service level, per platform | Monthly |
| Incident response | Mean time to restore service after an incident, per severity class | Per incident, trended quarterly |
| Event-interface reliability | Delivery rate of the steady-state handover events the chain depends on | Per interface, monthly |
| Capacity headroom | Share of platforms operating within their planned capacity envelope | Monthly, ahead of known peaks |
| Security posture | Open critical vulnerabilities and patch latency (assessed with VS-07) | Continuous, reported quarterly |
| Modernization progress | Components retired or replaced according to the roadmap | Annually |

## Interactions, Services and Events

| Counterpart | VS-09 provides | VS-09 receives | Interaction / event |
|---|---|---|---|
| **All streams (VS-01…VS-10)** | Environments, platforms, integration, availability | Requirements, capacity demand, incidents | "Platform/service request", "Incident", "Capacity change" |
| **VS-06 Dissemination** | Portals, APIs, dashboards, secure research environments | Channel/scaling requirements | "Dissemination platform request" |
| **VS-08 Innovation** | Sandbox and production runtime for new tech | New-technology adoption requests | "Technology onboarding" |
| **VS-07 Governance** | Security posture and continuity evidence | Security & continuity policy | "Security/continuity review" |

## Business Objects / Artefacts

VS-09 manages enabling artefacts: **technical requirements**, **architecture blueprints**, **provisioned environments and platforms**, **integration/orchestration services and event interfaces**, **monitoring/security/continuity controls**, and the **modernization roadmap**. These underpin every stream and are managed across their lifecycle (SAF-P03), with security and continuity (SAF-P10/P06) built in. Each artefact has a designated owner; changes are tracked, prior versions remain identifiable, and obsolete components are formally retired.

## Applying This to Your NSO

### Maturity Assessment Checklist

- [ ] Do we derive infrastructure requirements from business capabilities and data volumes (not ad-hoc)?
- [ ] Do we have architecture blueprints for storage, processing, integration, and secure access?
- [ ] Are environments provisioned with governance, monitoring, and security controls built in?
- [ ] Do we provide integration/orchestration and the event interfaces the streams rely on?
- [ ] Do we monitor performance, manage incidents, and guarantee availability and disaster recovery?
- [ ] Is there a modernization path that adopts new technology (often from VS-08) and retires the obsolete?

### Scenarios

**Scenario A — Onboarding a secure research environment.** VS-06 needs to release de-identified microdata to accredited researchers. VS-09 captures the requirement (09.1), designs the SRE architecture (09.2), provisions it with access controls and output checking (09.3/09.4), and assures its security and availability (09.5) under VS-07's policy — so VS-06 can deliver controlled microdata access reliably.

**Scenario B — Adopting a cloud processing platform.** VS-08 validates a scalable processing technology. VS-09 designs and provisions the platform (09.2/09.3), enables integration with the existing pipelines (09.4), assures performance and continuity (09.5), and folds it into the modernization roadmap (09.6), so the production streams gain capacity without disruption.

**Scenario C — Scaling for the census peak.** The census (VS-01) will multiply ingestion and processing volumes for three months. VS-09 derives the peak requirements with the census team (09.1), updates the capacity plan and architecture (09.2), provisions elastic compute and storage ahead of the field period (09.3), and load-tests the ingestion event interfaces end to end (09.4). During the peak it monitors throughput and availability against the agreed service levels (09.5); afterwards the surge capacity is released and the lessons feed the modernization roadmap (09.6). The chain experiences the census as business as usual.

## VS-10.0 Customer and Stakeholder Engagement

### Purpose and Scope

VS-10.0 ensures the statistical organization remains connected, relevant, and responsive to the needs of those it serves. It builds and maintains mutual understanding and trust between the NSO and its users, data providers, partners, and policy stakeholders. Because official statistics exist to create **public value**, the organization must understand what stakeholders need, communicate transparently, and keep products, services, and policies aligned with real-world demand. It is **not a one-way process** — it is a continuous dialogue that turns stakeholder insight into better products, improved services, and stronger relationships. The value it creates is **relevance and public value**.



*A note on numbering:* each `VS-0x.y` below is both a value stream stage (*what value* is added) and a business process (*how* it is done); the numbering maps one-to-one. See the key-concepts box above.

### Position — a supporting stream that works across the whole chain

VS-10 is not a stage in the production line. It sits at the **edges** of the chain — facing both the data providers who feed VS-01 and the users who consume VS-06 — and channels what it learns inward to shape the whole chain.

```{mermaid}
%%| label: fig-1
%%| fig-cap: "VS-10 engages providers and users two-way and channels their needs into the chain."
%%| fig-width: 6
flowchart TD
    PROV["Data providers"] --> VS01["VS-01"]
    subgraph primary["Primary Value Streams"]
        direction LR
        VS01 --> VS02["VS-02"] --> VS03["VS-03"] --> VS04["VS-04"] --> VS05["VS-05"] --> VS06["VS-06"]
    end
    VS06 --> USERS["Users & Society"]

    VS10["**VS-10.0 Customer &<br/>Stakeholder Engagement**"]:::hi
    VS10 <-->|"needs & relationships"| PROV
    VS10 <-->|"needs, feedback,<br/>satisfaction"| USERS
    VS10 -->|"needs routed into<br/>design & innovation"| primary

    classDef hi fill:#7c3aed,color:#fff,stroke:#6d28d9,stroke-width:2px
    style PROV fill:#0f766e,color:#fff,stroke:#0f766e
    style USERS fill:#0f766e,color:#fff,stroke:#0f766e
```

::: {.callout-important title="How a supporting value stream differs from a primary one"}
- **No steady-state data transition.** VS-10 does not move data along the chain; it moves **understanding** — needs in, communication and services out.
- **It runs continuously** as an ongoing dialogue, not per production cycle.
- **Its output is an enabling capability, not a data artefact:** understood needs, a managed service portfolio, relationships, and impact insight.
- **It aligns to GAMSO Strategy & Leadership and Corporate Support**, not to GSBPM production phases.
:::

### How It Interacts with the Production Chain

VS-10 is the chain's two-way interface with the outside world. It is tightly coupled with **VS-01** (the data providers it engages) and **VS-06** (the users whose feedback it gathers, receiving VS-06.5's usage and satisfaction data). It translates what it hears into requirements that flow into design across the primary streams and into the **VS-08** innovation backlog.

```{mermaid}
%%| label: fig-2
%%| fig-cap: "Interaction with the chain: needs and feedback in; communication, services, and requirements out."
%%| fig-width: 6
flowchart LR
    EXT["Users, providers,<br/>partners, policymakers"] <-->|"dialogue"| VS10["VS-10<br/>Engagement"]:::hi
    VS06["VS-06 Dissemination"] -->|"usage & feedback (§6.5)"| VS10
    VS10 -->|"user needs & service requirements"| DES["Design across VS-01…06"]
    VS10 -->|"user-driven innovation needs"| VS08["VS-08 Innovation"]

    classDef hi fill:#7c3aed,color:#fff,stroke:#6d28d9
    style EXT fill:#0f766e,color:#fff,stroke:#0f766e
```

### Framework Alignment (GAMSO)

Where the primary streams map to **GSBPM** production phases, VS-10 maps to **GAMSO** leadership and support activities:

| GAMSO area | Relevance to VS-10 |
|---|---|
| **Strategy and Leadership** | Manage stakeholder and customer relationships; align the portfolio to strategy |
| **Corporate Support** | Manage communications, marketing, user support, and service management |
| **SAF capabilities** | Needs inventory (supports statistical design & build); customer/stakeholder management |

### Principles Emphasised

| Principle | Statement | How VS-10 applies it |
|---|---|---|
| **SAF-P04** | Maximize the benefits for the organization | Keeps the whole chain aligned to real stakeholder value and public benefit |
| **SAF-P08** | Data is shared property | Promotes broad, equitable access and reuse of statistics and services |
| **SAF-P02** | Active support | Runs user support and service management as actively-managed services |
| **SAF-P11** | Privacy By Design | Engages data providers and users with transparency about how their data is used and protected |

## Roles and Actors

::: {.callout-note title="Indicative, not prescriptive"}
The roles below are indicative, not a mandated organizational structure. The SAF deliberately leaves organization design to each NSO — assign these responsibilities to fit your own size, culture, and operating model.
:::


| Role | Description |
|---|---|
| **Head of Communication / Engagement** | Owns the stakeholder strategy and the external relationship |
| **User Researcher** | Collects and analyzes user needs and satisfaction |
| **Service / Product Portfolio Manager** | Defines and manages the catalog of services and data products |
| **Account / Relationship Manager** | Manages relationships with key providers, partners, and policy users |
| **Service Desk / User Support** | Operates day-to-day user support |
| **Communications / Outreach Officer** | Runs outreach, workshops, and knowledge-sharing events |
| **Impact Analyst** | Measures use, societal impact, and satisfaction |

## The Value-Stream Flow

VS-10's six business processes form a continuous engagement cycle — **understand → offer → deliver → measure** — that feeds back on itself.

```{mermaid}
%%| label: fig-3
%%| fig-cap: "The six business processes as a continuous engagement cycle."
%%| fig-width: 6
flowchart LR
    A["10.1 Identify &<br/>Segment Stakeholders"] --> B["10.2 Collect &<br/>Analyze User Needs"]
    B --> C["10.3 Define & Manage<br/>Service Portfolios"]
    C --> D["10.4 Deliver Services &<br/>Manage Relationships"]
    D --> E["10.5 Engage &<br/>Communicate"]
    E --> F["10.6 Monitor Impact<br/>& Satisfaction"]
    F -.->|"insight feeds the next cycle"| A

    style A fill:#f5f3ff,stroke:#7c3aed
    style B fill:#f5f3ff,stroke:#7c3aed
    style C fill:#eff6ff,stroke:#2563eb
    style D fill:#ecfdf5,stroke:#059669
    style E fill:#ecfdf5,stroke:#059669
    style F fill:#fef3c7,stroke:#d97706
```

**Understand — know who and what.** The cycle begins by **identifying and segmenting stakeholders** (10.1): mapping the ecosystem of users, data providers, partners, and policymakers and understanding their roles and expectations. It then **collects and analyzes user needs** (10.2): gathering feedback, running consultations, and translating stakeholder needs into concrete data or service requirements.

**Offer — shape the response.** Those needs shape the **definition and management of service portfolios** (10.3): catalogs of business services and data products that address stakeholder needs and align with strategic goals — the bridge between what users want and what the chain produces.

**Deliver — serve and communicate.** Services are put into the hands of users by **delivering services and managing relationships** (10.4): operating customer support, service desks, and account management, and monitoring satisfaction and service performance. Alongside delivery, VS-10 **engages and communicates with stakeholders** (10.5): outreach, workshops, and knowledge-sharing that promote awareness and correct understanding of statistical outputs.

**Measure — learn and feed back.** Finally it **monitors impact and satisfaction** (10.6): measuring how data and services are used, assessing societal impact, and feeding insight back into planning and innovation — closing the loop so the next cycle of needs is better understood.

| Business process | What it produces |
|---|---|
| VS-10.1 Identify and Segment Stakeholders | Stakeholder map and segments |
| VS-10.2 Collect and Analyze User Needs | Needs register / service requirements |
| VS-10.3 Define and Manage Service Portfolios | Service & product portfolio |
| VS-10.4 Deliver Services and Manage Relationships | Operating support & managed relationships |
| VS-10.5 Engage and Communicate with Stakeholders | Outreach, communication, awareness |
| VS-10.6 Monitor Impact and Satisfaction | Impact & satisfaction insight (fed back to the chain) |

## Capability Governance

VS-10 is itself a capability that is **designed** (engagement strategy, portfolio model), **built** (support and feedback channels — with VS-09), **operated** (continuous dialogue, support, communication), and **improved** (10.6 insight). Unlike a primary stream it produces **relevance, relationships, and insight**, not statistical data, and runs as a **continuous dialogue** rather than a per-cycle production run.

### Key Performance Indicators

| KPI | Description | Measurement |
|---|---|---|
| User satisfaction | Satisfaction score across user segments and services | Per survey wave, per segment |
| Needs conversion | Share of captured needs converted into requirements routed to design or innovation | Per planning period |
| Service performance | Support response and resolution times against the service standard | Monthly |
| Reach and engagement | Participation in consultations and outreach; channel reach across segments | Per campaign, annually |
| Impact evidence | Documented uses of official statistics in policy, research, and media | Annually |

## Interactions, Services and Events

| Counterpart | VS-10 provides | VS-10 receives | Interaction / event |
|---|---|---|---|
| **Users & society** | Services, support, communication, the service portfolio | Needs, feedback, satisfaction | "User need captured", "Consultation", "Service request" |
| **Data providers (via VS-01)** | Relationship management, transparency | Willingness to provide data, provider needs | "Provider engagement" |
| **VS-06 Dissemination** | Service requirements & user expectations | Usage and satisfaction data (its §6.5) | "Feedback received" |
| **VS-08 Innovation & design across VS-01…06** | User-driven needs and service requirements | New/improved products and services | "Need routed to design/innovation" |

## Business Objects / Artefacts

VS-10 manages enabling artefacts: the **stakeholder map and segments**, the **user-needs register**, the **service and product portfolio**, **relationship and support records**, and **impact and satisfaction metrics**. These carry user insight into the rest of the chain and are maintained continuously rather than versioned per production cycle. Each artefact nevertheless has a designated owner and a managed lifecycle (SAF-P03): changes are tracked and outdated entries are retired.

## Applying This to Your NSO

### Maturity Assessment Checklist

- [ ] Have we mapped and segmented our stakeholders (users, providers, partners, policymakers)?
- [ ] Do we systematically collect and analyze user needs and translate them into requirements?
- [ ] Do we manage a service/product portfolio aligned to those needs and to strategy?
- [ ] Do we operate user support and manage key relationships, monitoring satisfaction?
- [ ] Do we measure impact and feed insight back into design and innovation (VS-08)?

### Scenarios

**Scenario A — A new user need becomes a product.** Through consultation (10.2) VS-10 learns that regional policymakers need more granular labour-market data. It logs the requirement, adds a candidate product to the portfolio (10.3), routes the need to design (VS-04/VS-05) and, where new methods are required, to VS-08. Once released by VS-06, VS-10 monitors uptake and satisfaction (10.6) and refines the offering.

**Scenario B — Closing the feedback loop.** VS-06.5 reports confusion about confidence intervals in a release. VS-10 analyzes the feedback (10.2/10.6), provides targeted user guidance and a plain-language explainer (10.5), and feeds a documentation improvement back to VS-05/VS-06 design — turning a usability problem into a concrete improvement.

**Scenario C — A new audience emerges.** Monitoring shows journalists increasingly republishing statistics from third-party aggregators, sometimes incorrectly. VS-10 identifies data journalists as a distinct segment (10.1), consults them on their needs — machine-readable releases, embeddable visuals, plain-language methodology notes (10.2) — and adds a media-service offer to the portfolio (10.3). The channel requirements are routed to VS-06 and VS-09, an embargoed media briefing service is set up under VS-07's equal-access policy (10.4/10.5), and citation accuracy in the press is tracked as an impact measure (10.6).
