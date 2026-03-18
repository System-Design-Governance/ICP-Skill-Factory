# ADR-007: YAML Metadata vs Prose Section Separation

**Status:** Accepted
**Date:** 2026-03-18

## Context

During Phase 3 batch authoring, the original 27-field flat schema (SCHEMA.md v1.0) was implemented with an implicit structural split: 13 fields became YAML key-value pairs inside a fenced code block under `## Metadata`, while 14 fields became independent `## ` prose sections with narrative content (multi-paragraph descriptions, bulleted lists, tables).

This split was never formally documented, causing SCHEMA.md to describe all 27 fields as if they were YAML metadata. The full-forensic-review (2026-03-18) identified this as a Critical gap (G-003).

Additionally, the schema was sometimes cited as containing "Workflow/Process" and "Pitfalls/Anti-patterns" sections. Forensic grep across all 171 SK files confirmed 0/171 contain these sections. SK definitions are knowledge specifications, not operational procedures.

## Decision

1. SCHEMA.md v1.2 explicitly separates Part A (13 YAML metadata fields) from Part B (14 prose sections)
2. The absence of Workflow and Pitfalls sections in SK definitions is documented as intentional: these are constructed in SKILL.md (Phase 5) from SK content + domain knowledge
3. `composition_patterns` is marked as Optional/Deferred since Phase 4 (Dependency Mapping) was not executed

## Consequences

- New SK authors have clear structural guidance
- SKILL.md developers understand that Workflow and Pitfalls must be self-constructed, not extracted from SK
- No retroactive changes to existing 171 SK files required
