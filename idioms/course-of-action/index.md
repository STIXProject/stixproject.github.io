---
layout: idiom
title: Course of Action Idioms
---

<img src="/images/Course of Action.png" class="component-img" alt="Course of Action Icon" />

A STIX [Course of Action](/documentation/coa/CourseOfActionType) component is used to convey information about courses of action that may be taken either in response to an attack or as a preventative measure prior to an attack. They are used to express both courses of action that might be taken (are possible options are are suggested) in the course of an incident, to mitigate the impact of an indicator, or to mitigate the effect of an exploit target (vulnerability or misconfiguration).

The course of action component itself contains information about the efficacy of the action, the likely impact, cost, and even a structured course of action meant to be implemented automatically in a tool

Course of action idioms primarily deal with expressing different types of courses of action: remedial courses of action like patching a vulnerability or operational courses of action like blocking network traffic.

<hr class="separator" />

### Blocking Network Traffic

One response malware activity on a network is to block that traffic's command and control servers at an external firewall. This idiom describes a course of action to implement such a block.

[View this idiom »](block-network-traffic)