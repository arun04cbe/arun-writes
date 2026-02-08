---
sidebar_position: 3
sidebar_label: Practical Guide 3
sidebar_class_name: green
sidebar_key: unique-sidebar-item-key
---

# Multi-Agent AI System

:::info[Task]

**Design AI System which will be able intake requirements for features and then split tasks for the corresponding features.**

:::

## Considerations

1. Similar to how we do `Design` (HLD or LLD), for any software feature, it is always good to design the AI workflow along with the whole system.
2. The way in which we provide UI/UX to the users also has an effect in which we design the AI system.
3. If the entire flow has a many AI Agents plugged together to accomplish a task, `Human In Loop (HIL)` checkpoints at necessary places will make the system with better performance.
4. `S` in `SOLID Principles` talks about Single Responsibility, it is always good to have an AI Agent which is good at preforming one task.
5. Other Considerations
   1. How much autonomy is needed?
   2. Accuracy Vs Latency
   3. Fallback scenarios
   4. Memory Scope (Short-Term or Long-Term)

From the above consideration, we may still have multiple ways in which we design the entire AI System for the above task. Let's consider a couple of approaches and implement the system.

## Approach 1

- User need not select if the input is a feature requirement of planning of tasks. Agent can identify based on input and do either requirement gathering or planning tasks.

A simple solution is provided below,

![Multi Agent Workflow 1](../../../src/images/multi_agent_workflow_1.png)
