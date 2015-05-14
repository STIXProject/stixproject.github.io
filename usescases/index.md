---
layout: flat
title: Use Cases
---

The STIX Language is targeted to support a range of core use cases involved in cyber threat management, including [analyzing cyber threats](http://stixproject.github.io/usecases/#analyzing-cyber-threats), [specifying indicator patterns](http://stixproject.github.io/usecases/#specifying-indicator-patterns), [managing response activities](http://stixproject.github.io/usecases/#managing-response-activities), and [sharing cyber threat information](http://stixproject.github.io/usecases/#sharing-threat-information).

##Analyzing Cyber Threats
A cyber threat analyst reviews structured and unstructured information regarding cyber threat activity from a variety of manual or automated input sources. The analyst seeks to understand the nature of relevant threats, identify them, and fully characterize them such that all of the relevant knowledge of the threat can be fully expressed and evolved over time. This relevant knowledge includes threat-related actions, behaviors, capabilities, intents, attributed actors, etc. From this understanding and characterization the analyst may then specify relevant threat indicator patterns, suggest courses of action for threat response activities, and/or share the information with other trusted parties.

*Example:* In the case of a potential phishing attack, a cyber threat analyst may analyze and evaluate a suspected phishing email, analyze any email attachments and links to determine if they are malicious, determine if the email was sent to others, assess commonality of who/what is being targeted in the phishing attack, determine whether malicious attachments were opened or links followed, and keep a record of all analysis performed.

##Specifying Indicator Patterns for Cyber Threats
A cyber threat analyst specifies measurable patterns representing the observable characteristics of specific cyber threats along with their threat context and relevant metadata for interpreting, handling, and applying the pattern and its matching results. This may be done manually or with the assistance of automated tooling and structured instantial threat information. 

*Example:* In the case of a confirmed phishing attack, a cyber threat analyst may harvest the relevant set of observables (e.g., to or from addresses, actual source, subject, embedded URLs, type of attachments, specific attachment, etc.) from the performed analysis of the phishing email, identify the relevant TTPs exhibited in the phishing attack, perform kill chain correlation of the attack, assign appropriate confidence for the indicator, determine appropriate handling guidance, generate any relevant automated rule patterns for the indicator (e.g., Snort, YARA, OVAL, etc.), assign any suggested courses of action, and package it all up as a coherent record for sharing (i.e., [Sharing Cyber Threat Information](http://stixproject.github.io/usecases/#sharing-threat-information)) and future reference.

##Managing Cyber Threat Response Activities
Cyber decision makers and cyber operations personnel work together to prevent or detect cyber threat activity and to investigate and respond to any detected incidences of such activity. Preventative courses of action may be remedial in nature to mitigate vulnerabilities, weaknesses, or misconfigurations that may be targets of exploit. After detection and investigation of specific incidents, reactive courses of action may be pursued. 

*Example:* In the case of a confirmed phishing attack with defined indicators, cyber decision makers and cyber operations personnel work together to fully understand the effects of the phishing attack within the environment including malware installed or malware executed, to assess the cost and efficacy of potential courses of action, and to implement appropriate preventative or detective courses of action.

**Cyber Threat Prevention**

Cyber decision makers evaluate potential preventative courses of action for identified relevant threats and select appropriate actions for implementation. Cyber operations personnel implement selected courses of action in order to prevent the occurrence of specific cyber threats whether through general prophylactic application of mitigations or through specific targeted mitigations initiated by predictive interpretation of leading indicators.

*Example:* In the case of a confirmed phishing attack with defined indicators, a cyber decision maker may evaluate a suggested preventative course of action (e.g., implementing a blocking rule at the email gateway) defined within an indicator for the phishing attack, determine its relevant cost and risk, and decide whether or not to implement it. If it is decided to implement the suggested course of action, cyber operations personnel carry out the implementation.

**Cyber Threat Detection**

Cyber operations personnel apply mechanisms (both automated and manual) to monitor and assess cyber operations in order to detect the occurrence of specific cyber threats whether in the past through historical evidence, currently ongoing through dynamic situational awareness, or apriori through predictive interpretation of leading indicators. This detection is typically via cyber threat indicator patterns. 

*Example:* In the case of a confirmed phishing attack with defined indicators, cyber operations personnel may harvest any specified observable patterns from defined indicators of the attack and apply them appropriately within the operational environment to detect any evidence of the phishing attack occurring.

**Incident Response**

Cyber operations personnel respond to detections of potential cyber threats, investigate what has occurred or is occurring, attempt to identify and characterize the nature of the actual threat, and potentially carry out specific mitigating or corrective courses of action.

*Example:* In the case of a confirmed phishing attack, cyber operations personnel may conduct investigative activities to determine whether the phishing attack was successful in carrying out negative effects within the target environment (e.g., was malware installed or run) and if so, attempt to characterize in detail those effects (e.g., which systems were affected by malware, what data was exfiltrated, etc.). Once the effects are understood, cyber operations personnel would implement appropriate mitigating or corrective courses of action (e.g., wipe and restore systems, block exfil channels, etc.).

##Sharing Cyber Threat Information
Cyber decision makers establish policy for what sorts of cyber threat information will be shared with which other parties and how it should be handled based on agreed to frameworks of trust in such a way as to maintain appropriate levels of consistency, context and control. This policy is then implemented to share the appropriate cyber threat indicators and other cyber threat information.

*Example:* In the case of a confirmed phishing attack with defined indicators, the policies predefined by cyber decision makers could enable the relevant indicators to be automatically or manually shared with trusted partners or communities such that they could take advantage of the knowledge gained by the sharing organization.

Send feedback about this page to stix@mitre.org.
