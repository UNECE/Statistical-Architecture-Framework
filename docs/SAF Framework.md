SAF Architecture Framework
============================

Created on: 07-07-2025
Workgroup SAF: Trygve Falch (Statistics Norway), Jakob Engdahl (Statistics Sweden), Stephane Crete (Statistics Canada), Cedric Couralet (Insee), Daan Swinkels (CBS), Pascal Fransen (CBS)
Version 0.3

| Version | Date | Contributor/Secretary |
|---|---|---|
|0.1|2025-07-07|Initial version|
|0.2|2026-06-01|Review processed|
|0.3|2026-07-31|Merge Business Architecture|

## Content
[Preface](#preface)

Acknowledgements [TODO]

[Introduction](#introduction)

Activity Proposal [TODO]

[Purpose](#purpose)

[Definition of Scope](#definition-of-scope)

[Target Audience](#target-audience)

Constraints & Assumptions [TODO]

[Motivation](#motivation)
-    [Drivers](#drivers)
-    [Goals](#goals)
-    [Meaning](#meaning)

[Outcome](#outcome)

[Architecture Principles](#architecture-principles)

[Stakeholders, Roles and Collaborations](#stakeholders-roles-and-collaborations)

[Capability Model](#capability-model)

[Valuestreams](#value-streams)

[Business Architecture](#business-architecture)


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

TODO : formatting

Definition: Architecture drivers in many ocassions  are the same forces that make change necessary. They capture the pressures, trends, and constraints that statistical offices face and which the SAF is designed to address. Drivers can be external, such as technological advancements or new regulations, or internal, such as the need to replace legacy systems or respond to stakeholder demands. By documenting these drivers, SAF ensures that its architecture is not an abstract ideal but a practical response to real-world challenges.

For statistical organizations, these drivers are particularly intense. Rapid technological change requires continuous adaptation, while political and societal pressures demand timely, relevant, and transparent data. At the same time, many organizations face limited budgets and must balance modernization with cost control. 

Recognizing these drivers helps statistical offices prioritize investments and avoid the pitfalls of reactive decision-making, where short-term fixes can lead to long-term inefficiencies.

Including architecture drivers in the framework also strengthens communication with stakeholders. By clearly articulating the external and internal factors shaping architecture, CIOs, CTOs, and enterprise architects can build a stronger case for change, justify strategic initiatives, and ensure that all parties understand the urgency of modernization. In this way, SAF creates a shared understanding of why action is necessary and what risks are avoided by adopting a structured framework.
 
#### SAF-D1 Evolving Data Ecosystems and Partnerships

The environment for producing official statistics is shifting from one of isolated data collection toward a complex and interdependent data ecosystem. Traditional surveys, once the cornerstone of statistical production, now coexist with administrative, commercial, platform, and community-driven data sources. This evolution expands opportunities for collaboration but also introduces dependencies on actors, technologies, and infrastructures outside the direct control of statistical organizations.

Open-source development has become a key element of this ecosystem. It provides a shared foundation for innovation, transparency, and cost efficiency, while fostering cooperation across institutional and national boundaries. As part of a wider collaboration model, open source allows NSIs to co-develop tools and methods with peers, academia, and private partners, ensuring that advances in technology benefit the entire statistical community. SAF addresses this driver by promoting architectures that support secure data sharing, standardized interfaces, and transparent governance models. It enables NSIs to participate confidently in broader ecosystems, from national data platforms to European data spaces, where production may take place across multiple environments and jurisdictions. By combining openness with strong governance and clear accountability, SAF ensures that collaboration and shared development strengthen rather than compromise the integrity of official statistics.
 
#### SAF-D2 Artificial Intelligence and Technological Acceleration

Artificial intelligence, automation, and rapid technological progress are transforming how data is created, processed, and consumed. For statistical organizations, these developments bring both opportunities and dependencies. Emerging tools can automate repetitive tasks, enhance analytical capabilities, and strengthen quality assurance. At the same time, they redefine what it means for official statistics to remain relevant and trusted in an environment increasingly shaped by intelligent systems.

The accelerating pace of innovation requires statistical offices to be both adopters and enablers of AI. Internally, this means developing architectures and competencies that support automation, machine learning, and advanced analytics within secure and transparent frameworks. Externally, it requires ensuring that official statistics are AI-ready - that is, machine-readable, machine-understandable, and interoperable with the digital platforms and applications used by policymakers, researchers, and citizens.

SAF addresses this driver by enabling NSIs to adopt a risk-based approach to modernization. It supports architectures where critical processes that demand methodological rigor, transparency, and control can be tightly governed, while areas that are less sensitive can be automated to a higher degree. This balance ensures that innovation strengthens quality and efficiency without compromising security, privacy, or trust.

Through modular and standards-based design, SAF provides the flexibility needed to integrate emerging technologies at an appropriate pace. It allows NSIs to benefit from automation and AI-driven tools while maintaining full accountability for statistical quality, data protection, and institutional independence.
 
#### SAF-D3 Trust, Scientific Rigor, and Data Protection

Trust is the foundation of official statistics. In an environment increasingly challenged by misinformation, privacy concerns, and competition from unregulated data providers, maintaining public confidence requires more than compliance. It depends on scientific rigor, transparency, and clear accountability for how data is handled and communicated.

SAF addresses this driver by embedding trust and protection directly into architectural design. It promotes governance and technical controls that safeguard confidentiality, ensure methodological integrity, and make processes traceable and transparent. Through a risk-based approach, SAF allows NSIs to apply strict oversight where sensitivity and quality demands are high, while enabling greater automation and shared solutions where risks are lower. This balance ensures that modernization strengthens trust rather than compromising it.
 
#### SAF-D4 Uncertain and Polarized Global Environment

Statistical organizations operate in an increasingly complex and uncertain world. Global tensions, political polarization, and shifting power dynamics influence both the demand for and the perception of official statistics. At the same time, digital interdependence and cross-border data flows require statistical systems to remain open and interoperable while safeguarding national and institutional integrity.

SAF addresses this driver by providing a stable and transparent foundation for cooperation and resilience. It promotes interoperable architectures based on shared standards, enabling NSIs to exchange data and methods securely even in times of uncertainty. By embedding governance and design principles that protect independence and transparency, SAF helps organizations maintain credibility, comparability, and trust in environments where facts themselves are often contested.
 
#### SAF-D5 Resource Constraints and Organizational Agility

Many statistical organizations face increasing expectations with limited budgets, aging systems, and challenges in recruiting and retaining specialized skills. At the same time, the demand for more timely, detailed, and multidomain outputs continues to grow. Meeting these needs requires not only efficiency, but the ability to adapt rapidly to changing priorities and technologies.

SAF addresses this driver by promoting architectures that make flexibility and reuse a core principle. It supports modular designs, shared services, and scalable solutions that reduce duplication and enable more effective use of existing resources. By fostering an agile organizational mindset and clear governance around priorities, SAF allows NSIs to reallocate capacity, modernize incrementally, and continue to deliver high-quality outputs even under financial and staffing constraints.


## Goals

Definition: Architecture goals represent the outcomes an organization aims to achieve by adopting and implementing aframework. They define what success looks like and serve as the link between strategy and action. In the case of the SAF, these goals are not just about modernizing IT systems, but about ensuring that national statistical institutes can continue to provide trustworthy, relevant, and high-quality statistics in a rapidly changing environment.

The goals of SAF address both operational and strategic needs. On one hand, they focus on efficiency, modernization, and compliance, which are essential for ensuring sustainability. On the other hand, they support innovation, adaptability, and collaboration, enabling statistical offices to embrace new opportunities such as integrating alternative data sources or experimenting with advanced analytics. Together, these goals ensure that modernization efforts do not compromise the fundamental values of official statistics, neutrality, accuracy, and reliability.

By defining goals explicitly, SAF provides a roadmap that can be adapted by each statistical organization according to its maturity and context. This ensures that while each office may have unique challenges and resources, they are all working toward a shared vision that promotes harmonization, comparability, and global collaboration in official statistics.
 
#### SAF-G1 Cost Efficiency and Resource Sharing
With limited budgets and growing demands, statistical organizations must operate as efficiently as possible. SAF promotes cost optimization and improved effectiveness through shared services, reuse of solutions, and stronger interoperability. By pooling resources and adopting common components, NSIs can access capabilities that would be difficult to develop individually while avoiding duplication of effort.
SAF also encourages the use of open-source components and community-driven platforms where this strengthens transparency, collaboration, and cost efficiency. Through modular architectures and clear governance, organizations can adapt to changing needs, reallocate capacity, and modernize incrementally without large-scale reinvestments. This approach ensures that efficiency is achieved in ways that reinforce both quality and long-term sustainability.
 
#### SAF-G2 Harmonized Reference Framework

Without a shared architectural reference, statistical organizations risk developing isolated solutions that reduce comparability and increase long-term costs. SAF provides a harmonized foundation of standards, patterns, and best practices that can be adapted to local contexts while supporting interoperability across borders and domains. As collaboration increasingly takes place across shared infrastructures such as national data platforms and international data spaces, harmonization also becomes a prerequisite for participation. By promoting transparency and consistent design principles, SAF helps NSIs protect the integrity of official statistics and ensure that shared and open solutions can be reused safely and effectively. A common reference framework enables collaboration, strengthens trust, and supports coherence even as the data landscape evolves.
 
#### SAF-G3 Modernization of Statistical Systems

Many statistical organizations continue to rely on fragmented and legacy IT environments that limit innovation and responsiveness. SAF provides guidance for transitioning toward modern, modular, and service-based architectures that are secure, scalable, and easier to maintain. Modernization reduces technical debt, improves reliability, and allows faster delivery of new and higher-quality statistical outputs.
Modernization increasingly takes place in environments where multiple actors operate, from national infrastructures to cross-border data spaces. SAF ensures that such settings can be used safely by defining principles for access control, data protection, and accountability. It also supports a risk-based approach to automation and integration of emerging technologies. Critical processes can remain tightly governed to preserve methodological rigor, while less sensitive stages can be automated or shared.
 
#### SAF-G4 Support for Data Innovation

Innovation in data and methods is central to the future of official statistics. SAF promotes an environment where experimentation, collaboration, and reuse are encouraged within secure and well-governed boundaries. By providing a clear architectural foundation, SAF enables NSIs to incorporate new data sources, tools, and analytical methods without undermining consistency or quality.

Innovation is not only about creating new solutions but also about making change possible within production. Many statistical organizations find it difficult to introduce new data sources or develop new statistical products because their production systems are optimized for predictability and stability. While these are necessary principles, they can limit agility. SAF addresses this by supporting architectures that balance robustness with flexibility, allowing new components, data, or workflows to be integrated more rapidly while maintaining full control over quality and compliance.

To make this possible, the framework emphasizes mechanisms and guardrails that enable controlled integration of innovative methods into production chains. This includes versioning, validation, and automated testing approaches that preserve reliability even as systems evolve. SAF also seeks to narrow the gap between innovation and production by promoting shared platforms and processes that allow prototypes to transition smoothly into operational environments.

Open source plays a key role in this innovation process. It allows organizations to build on each other’s work, increase transparency, and strengthen the collective capacity of the statistical community. SAF supports this through architectural patterns that enable safe reuse of open components and integration with shared platforms. In doing so, it helps turn innovation into a structured, sustainable part of statistical production.
 
#### SAF-G5 Sustainable Compliance

Compliance with regulations, standards, and ethical principles is fundamental to maintaining the trust and legitimacy of official statistics. SAF ensures that modernization aligns with legal, security, and quality frameworks while promoting transparency and accountability. Within the statistical domain, well-established standards such as GSBPM, GSIM, and SDMX continue to provide a foundation for consistent processes, metadata management, and data exchange. These remain essential for ensuring methodological rigor and comparability across the statistical system.

However, as the production of statistics becomes increasingly integrated into the broader data and technology ecosystem, compliance must also extend beyond traditional statistical standards. SAF encourages active engagement with and adoption of relevant standards from adjacent fields such as data management, artificial intelligence, and cloud computing. This outward-looking approach ensures that NSIs remain interoperable with modern data platforms and can benefit from technological progress developed outside the statistical community.

Through consistent governance and the use of open, verifiable technologies, SAF supports compliance as an enabler rather than a constraint. It provides the structures necessary to ensure that innovation, data sharing, and open collaboration occur within controlled and auditable environments. This approach reinforces public trust by embedding transparency, scientific rigor, and privacy-by-design across all processes.

## Meaning
Architecture meaning provides the “why” behind the framework. While goals and outcomes describe what SAF achieves, meaning explains why it matters. For statistical organizations, architecture is not just a technical exercise but a way of ensuring their continued relevance in a digital society. SAF’s meaning lies in its role as the foundation for modernization, trust, and international collaboration.

- One dimension of this meaning is its role as a bridge between strategy and technology. Without such a framework, investments in IT risk being disconnected from the mission of providing high-quality statistics. SAF ensures that every technological decision, from adopting a new platform to restructuring business processes, can be traced back to strategic objectives, creating a coherent organizational narrative. 
- Another dimension is collaboration. The meaning of SAF extends beyond individual organizations: it is a unifying language for the UNECE statistical community. By providing shared models, practices, and principles, SAF fosters international collaboration, reduces duplication, and amplifies collective impact. In this sense, SAF is not just meaningful to IT professionals but to the broader community of statisticians, policymakers, and citizens who depend on trustworthy statistics.
 
#### SAF-M1 Bridge Between Strategy and Technology
SAF connects high-level strategic objectives, such as improving statistical relevance and efficiency, with concrete technology choices. It ensures that IT investments are always justified by their contribution to the organization’s mission.
 
#### SAF-M2 Catalyst for Collaboration
SAF is a unifying framework for the statistical community. It enables organizations to work together on shared goals, whether through joint platforms, interoperable systems, or harmonized standards, thereby amplifying the collective capacity of UNECE members.
 
#### SAF-M3 Foundation for Digital Transformation
SAF is not just a set of technical models; it is the foundation for digital transformation in official statistics. It enables NSIs to embrace innovation without sacrificing methodological rigor or institutional trust.

#### SAF-M4 Unifying Language and Notation
By adopting TOGAF and ArchiMate, SAF ensures that diverse stakeholders can communicate using a consistent language and notation. This reduces misunderstandings, enables shared modelling practices, and promotes architectural maturity across the community.


# Outcome

Architecture outcomes describe the tangible benefits that organizations can expect when adopting SAF. They translate principles, goals, and drivers into measurable impacts such as improved interoperability, reduced costs, and enhanced data quality. Outcomes are critical for demonstrating the value of architecture to stakeholders, as they provide a clear “return on investment” for adopting the framework. In the SAF, outcomes are both technical and societal.

On the technical side, NSIs benefit from streamlined processes, better metadata management, and more efficient system development. On the societal side, SAF supports trust, transparency, and comparability of statistics, which are essential for informed policy-making and democratic accountability. This dual perspective ensures that SAF delivers benefits beyond IT, directly supporting the mission of statistical organizations.

By emphasizing outcomes, SAF also reinforces a culture of continuous improvement. Outcomes are not static; rather they evolve as organizations mature and as new challenges emerge. Making outcomes explicit allows NSIs to assess progress, measure success, and adjust their modernization strategies in line with both internal priorities and external demands.
 
#### SAF-O1 Accelerated Modernization
Embedding governance, metadata, and lineage into architecture ensures that statistical outputs maintain the highest standards of quality and trustworthiness. SAF makes quality an architectural outcome rather than an afterthought.
 
#### SAF-O2 Enhanced Data Quality
Embedding governance, metadata, and lineage into architecture ensures that statistical outputs maintain the highest standards of quality and trustworthiness. SAF makes quality an architectural outcome rather than an afterthought.
 
#### SAF-O3 Improved Interoperability
By adopting SAF, NSIs will achieve higher levels of interoperability across systems, domains, and borders. This facilitates cross-country collaborations, enhances comparability of statistics, and simplifies the integration of external data sources into official workflows.
 
#### SAF-O4 Improved Trust and Transparency
By embedding principles such as openness, security, and transparency, SAF helps to build and maintain public trust in statistics. This outcome strengthens the reputation of NSIs and the legitimacy of their outputs.
 
#### SAF-O5 Increased Efficiency
SAF reduces duplication of effort by promoting reuse, harmonization, and standardization. This outcome means lower IT costs, faster system development cycles, and more efficient data processing pipelines across the statistical system.
 
#### SAF-O6 Shared Knowledge Base
SAF fosters a community of practice across UNECE members. Through shared architectural frameworks, NSIs can exchange lessons learned, reusable components, and knowledge, leading to continuous improvement at lower cost.

# Architecture Principles
Architecture principles are the basis for any enterprise architecture framework. They provide the guiding rules and fundamental truths that define the way organizations design, implement, and manage their IT landscapes. In the context of official statistics, principles are particularly important because they ensure consistency across an interconnected environment.

For the SAF, architecture principles act as a compass for decision-making. They ensure that whenever there is a choice to be made between technologies, processes, or solutions, decisions are not taken in isolation but in accordance with the overarching vision of the statistical community. They also prevent short-term convenience from undermining long-term sustainability, a challenge that statistical offices often face given their reliance on legacy systems and resource constraints.

These principles also provide an element of accountability. When stakeholders understand the principles behind architectural decisions, it becomes easier to justify investments, explain trade-offs, and demonstrate that architecture is not a purely technical exercise but a strategic enabler of the organization’s mission. In this way, principles make architecture transparent, predictable, and anchored in trust.

#### SAF-P01 Reuse before open source, open source, before buying, buying before making it yourself
In case of equal suitability (Business Case), reuse of (parts of) applications takes precedence. The use of open source software takes precedence over purchasing. Purchasing is then preferred over making it yourself. Non-statistical processes only use standard applications.

Reuse of an application or parts of that application is sustainable and cost-efficient, and also leads to standardization in service provision and information provision. If reuse is not possible, investigate whether an Open Source solution is available before considering a Closed Source (Commercial) solution.
 
#### SAF-P02 Active support
Systems (hardware and software) have an active user community and/or vendor support. The rule of thumb is that we use the latest or the second-to-last major version. Among other things, for business continuity it is necessary to be able to get quick and good support in resolving a disruption in the event of a disruption. It is also important from a security perspective that identified security risks are resolved in a timely manner.
 
#### SAF-P03 Active Life Cycle management
With active Life Cycle management we prevent overdue maintenance in the IV landscape so that continuity & security risks are mitigated, among other things. Without Life Cycle management, systems or parts thereof can become outdated and thus become vulnerable in terms of security. Without active Life Cycle management, a  technological debt is also built up that, when it eventually has to be repaid, will require disproportionate effort or introduce continuity risks. Keeping systems and components up-to-date in accordance with established LCM policy mitigates these risks.
 
#### SAF-P04 Maximize the benefits for the organization
IT decisions are made to maximize the benefits of the organization as a whole. This principle embodies 'service above self'. Decisions made from an organization-wide perspective have greater long-term value than decisions made from a departmental perspective. To maximize the return on the investment, IV decisions must align with the organization-wide mission and priorities.
 
#### SAF-P05 IT and technology is everyone's business
All departments in the organization participate in IV decisions that are necessary to achieve organizational goals. IT and technology users are the key stakeholders in the application of technology to meet an organization's needs. To ensure that IT and technology are aligned with business operations, all departments in the organization must be involved in all aspects of the IT and technology landscape. Business experts from across the organization and the technical staff responsible for developing and maintaining the IT and technology capabilities must work together as a team to jointly define the goals and objectives.
 
#### SAF-P06 Business Continuity
Organizational activities are maintained despite system or employee outages. As systems and processes become increasingly important to operations, we become more dependent on them; therefore, we must consider the reliability of such systems and processes in their design and operation. Departments throughout the organization must have the ability to continue their activities, regardless of external events, within agreed lead times. Hardware failures, natural disasters, and data corruption must not disrupt or stop operations. The enterprise must be able to operate on the basis of alternative IV systems/processes.
 
#### SAF-P07 Implement loosely coupled processes and systems
Processes and systems should be built as independently as possible. This means that processes and systems are designed in such a way that they are not intertwined and dependent on each other. Functionality and logic should be shared with the rest of the organization via standard interfaces. Loosely coupling processes and systems offers more flexibility to adapt or replace individual processes and systems in the future. In addition, there are advantages in terms of scalability and robustness. Differences in security and privacy requirements can also be better enforced.
 
#### SAF-P08 Data is shared property
Statistical data that has been determined to add value for use by internal or external users is shared. This implies re-use of data, both in observation to reduce the burden and in further processing to prevent duplication of work in improving and analyzing data.
 
#### SAF-P09 No data without metadata and classification
All data that needs to be shared, needs to be provided with metadata information that describes the content and meaning of the data as well as possible. In addition, the data also needs to be classified. Metadata makes it possible to make data FAIR and the BIV classification (Availability, Integrity and Confidentiality) provides direction for the necessary technical and organizational measures. This is to comply with various laws, requirements and security standards.
 
#### SAF-P10 Security By Design
Security should not be an afterthought in IV solutions, but should be part of those solutions. Coherent security mechanisms should span all layers of the architecture and be scalable from small objects to large objects. Security should be designed as an integrated part of the system architecture.
 
#### SAF-P11 Privacy By Design
Privacy by design should be designed as an integrated part of the system architecture and business processes. Privacy should not be an afterthought in IV solutions, but should be part of those solutions. The result is that privacy becomes an essential part of the core functionality that is delivered. Privacy is an integral part of the system without compromising functionality.


### Value
The value of architecture lies in the benefits it creates for stakeholders. While outcomes describe specific impacts, value captures the broader, long-term importance of SAF to statistical organizations and society. It is about demonstrating that investing in architecture is not merely a technical necessity but a strategic decision that creates trust, efficiency, and sustainability.
For NSIs, the value of SAF includes reduced risks, greater agility, and improved alignment between IT and business objectives. For international organizations, it provides harmonization and comparability, enabling more effective collaboration across borders. For citizens and policymakers, the value lies in the trustworthiness of the statistics produced, ensuring that public policy and democratic processes are grounded in reliable data.
Value is also about sustainability. Without a framework, modernization efforts can be fragmented, costly, and short-lived. SAF provides a stable foundation that reduces technical debt, improves governance, and ensures that investments yield long-term benefits. In doing so, it secures the role of statistical organizations as trusted institutions in the digital age.
 
#### SAF-V1 Cross-Border Comparability
Statistics gain value when they are comparable across borders. SAF enables this by promoting common standards, models, and processes, ensuring that statistics from different countries can be meaningfully compared.

#### SAF-V2 Innovation Enablement
SAF is designed to support the integration of advanced technologies such as AI/ML, real-time analytics, and big data. By lowering the barriers to innovation, it enables NSIs to experiment safely while maintaining methodological soundness.


#### SAF-V3 Risk Reduction
By embedding compliance, security, and governance into the architecture, SAF reduces risks associated with system failures, data breaches, or regulatory non-compliance. This value is particularly critical in maintaining the trust of citizens and stakeholders.
 
#### SAF-V4 Strategic Alignment
SAF ensures that all IT initiatives within NSIs directly contribute to their mission of producing official statistics. This alignment improves governance, prioritization, and the impact of IT investments.
 
#### SAF-V5 Sustainability
SAF promotes efficiency and modernization while reducing technical debt. By providing clear pathways for evolution, it ensures that NSIs can sustain their IT landscapes without repeated costly overhauls.
 
#### SAF-V6 Trust & Legitimacy
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

# Capability Model

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

# Value Streams

## Primary Value Streams

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

The execution processes between the business domains are loosely coupled. Each has its own design and implementation. For the mutual exchange of data, they are loosely linked via steady state interfaces. To this end, five steady state phases are recognized that exist between the business domains: [1] raw data, [2] standardized data without loss of content, [3] processed data, [4] statistics, and [5] released data. An steady state phase is therefore an environment where high-quality versions of data are brought together for exchange, but it also represents a value in the value chain of this data.

Each of the mentioned business domain can be linked to a GSBPM phase.


## Steady States of Data and Their Business Process Links


The business architecture leverages a data value chain approach where data progresses through predefined steady states, each representing a stage where data meets specific quality criteria and is ready for exchange between business domains. These steady states serve as handover points in the statistical production process, ensuring consistency, reusability, and quality control as well as interoperability across other ONS.

### State #1: Raw Data

**Business Domain Link:*- Observation/Collection

**Description:*- Raw data represents the initial entry point where data has been received from external data holders and checked for basic safety and validation. At this stage, data has entered the NSO system in its original form as received from the data provider.

**Quality Requirements:**
- File integrity checks completed
- Virus and security scans performed
- SLA requirements verified with the data provider (e.g., completeness, delivery time)
- Data stored in its original format or equivalent

**ONS Use:*- Raw data for the raw source data in its original form as received from the data holder. The ONS does not have access to the data at the source; this is the first point of possession.

**Key Characteristics:**
- Data has not been further validated for content
- Sender verification completed
- Technical checks and transformations on the technical level only (not content level)
- Forms the baseline for all subsequent processing

### State #2: Standardized Data

**Business Domain Links:*- Standardization without loss of content

**Description:*- Standardized data has been transformed, formatted, and structured according to defined standards. This is the first point at which interoperability between domains is enabled through common classifications and standardized formats.

**Quality Requirements:**
- Format and structure standardized (e.g., converted from CSV to XML)
- Common classifications and code lists applied (e.g., geocoding, economic activity classifications)
- Variables mapped to enterprise standards
- Reference periods harmonized
- Confidentiality measures applied (e.g., pseudonymisation, data minimization)
- Data must not contain personally identifiable information

**ONS Use:*- Standardized data based on the received raw data, enabling data integration and interoperability across the organization.

**Key Processing Activities:**
- Application of reference data and master data
- Restructuring and reformatting to NSO's standard storage format
- Recoding of variables to align with enterprise standards
- Pseudonymisation and encryption where required
- Value sets adapted to organizational standards

**Interoperability Benefit:*- This state enables data from different sources to be combined and used across multiple statistical products, reducing duplication and increasing efficiency.

### State #3: Processed Data

**Business domain Links:*- Editing, derivation, and non-response correction

**Description:*- Processed data has undergone content-related validation, editing, and enrichment. Data accuracy has been improved through validation checks and corrective measures. This data is ready to be integrated with other datasets.

**Quality Requirements:**
- Completeness and accuracy improved through validation and editing
- Data integrity checks completed
- Filtering, editing, or imputation applied as needed
- Data lineage documented
- Integration with other datasets completed where applicable
- New derived variables calculated

**ONS Use:*- Processed data for the processed statistical microdata, ready for statistical analysis and production.

**Key Processing Activities:**
- Data cleansing and editing (content-related standardization)
- Integration with other datasets
- Validity checking and error correction
- Imputation of missing values
- Creation of new variables through calculation or derivation
- Flagging of problematic values

**Domain Responsibility:*- While this processing is primarily driven by individual statistical domains, depending on the data type, it may be performed by a central unit for efficiency and consistency.

**Reusability Focus:*- Processed data aims to be as reusable as possible for other processes or units, reducing duplication of data and processing effort while increasing transparency.

### State #4: Output Data (Statistics)

**Business Domain Links:*- Estimation and closed-loop + Statistically composed and composite statistical products

**Description:*- Output data represents statistics that have been aggregated and analyzed, or microdata that has been prepared for specific purposes. Confidentiality measures have been applied to allow potential release.

**Quality Requirements:**
- Data lineage fully documented
- Aggregation and analysis completed
- Confidentiality measures applied
- Statistical estimates calculated
- Quality indicators produced
- Internal review completed

**ONS Use:*- Statistics for basic statistics and integrated macrostatistics. These may be used internally by other statistical processes or prepared for dissemination.

**Key Characteristics:**
- Statistics will usually be aggregated data or estimated sizes
- May contain confidential and detailed data not yet suitable for publication
- Can be shared internally for use as input data in other statistical processes, especially macro statistics
- Estimated statistical target quantities produced
- Different confidentiality thresholds may apply depending on intended use

**Domain-Driven Production:*- The type of outputs and specific processing methods vary significantly by statistical domain and product requirements.

### State #5: Published Output Data (Released Data)

**Business Process Links:*- Disseminate

**Description:*- Published output data has been fully vetted, confidentiality requirements have been satisfied, and the data has been released or published for external use.

**Quality Requirements:**
- Higher confidentiality criteria applied
- Stronger documentation requirements met
- Data lineage fully traceable
- Quality reports completed
- Release authorization obtained
- Metadata and documentation suitable for external users

**ONS Use:*- Released data for all data to be disseminated publicly or delivered to authorized external parties.

**Key Characteristics:**
- All requirements for confidentiality taken care of
- May be further processed compared to State #4 for additional confidentiality protection
- Published by the NSO or delivered to external parties
- Includes both published statistical values and delivered microdata (de-identified)
- Strict documentation requirements to support user understanding and data reuse

**External Consumption:*- This is the final state in the value chain where statistical information fulfills the core mission of the NSO—delivering trusted statistics to society.

### State #6: Consumed Data

**Description:*- Data that has been used by external parties for their own purposes. This represents data outside the direct control of the ONS.

**ONS Use:*- None - Consumed data is data used by external data consumers for their analyses and decision-making.

**Key Characteristic:*- This state recognizes that once data is published, it enters the public domain and is used in ways that may be beyond the NSO's direct oversight, though the quality and documentation provided in State #5 support appropriate use.
