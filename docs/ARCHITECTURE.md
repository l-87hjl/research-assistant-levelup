# Architecture Overview

This project implements an **agentic research assistant** with a hard separation between **Research (Role A)** and **Synthesis (Role B)**.

## Core Principles
- Research is read-only and source-forward
- Synthesis is original, blank-slate construction
- Provenance is always preserved
- No silent transitions between roles

## High-Level Components
- agents/
  - research_agent.py (Role A)
  - synthesis_agent.py (Role B)
- modes/
  - mode_contracts.md
- ethics/
  - usage_and_ethics.md
- logs/
  - changes/ (why + what changed)
  - runtime/ (execution logs)

## Non-Goals (for now)
- Governor / deployment-level enforcement
- Auto-merging code into downstream repos

These will be addressed in later phases.