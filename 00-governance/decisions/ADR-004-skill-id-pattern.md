# ADR-004: Skill ID Pattern

**Status:** Accepted
**Date:** 2026-03-13
**Context:** Stage A Repository Framework Design

## Decision

Adopt the Hybrid pattern `SK-D{nn}-{nnn}` as the canonical Skill ID pattern.

## Alternatives Considered

### Option A — Flat Sequential
- Format: `SK-0001`, `SK-0002`, ...
- Pros: Simple, no hierarchy baked in
- Cons: No information carried in the ID; requires lookup for every operation. Poor for human scanning.

### Option B — Hierarchical Dotted (Phase 1 style)
- Format: `D01.2.003` (Domain.Subdomain.Sequence)
- Pros: Instantly readable hierarchy; matches existing Phase 1 IDs
- Cons: Refactoring a domain or subdomain forces mass ID changes. Tight coupling between taxonomy and identity.

### Option C — Hybrid (Selected)
- Format: `SK-D01-003`
- `SK` = Skill (entity type prefix)
- `D01` = Domain code (stable, rarely changes)
- `003` = Sequential number within that domain (zero-padded, 3 digits)

## Rationale

1. Domain prefix provides instant human readability without full lookup
2. Sequential number is stable under subdomain reorganization — if D01.2 merges into D01.1, skills keep their IDs
3. The SC → SK promotion path gives a clear lifecycle signal
4. The `.a` / `.b` sub-skill notation avoids deep nesting while allowing decomposition
5. Zero-padded 3-digit sequence supports up to 999 skills per domain (sufficient for 14 domains × ~15 skills each)

## Conventions

- Skill Candidate (pre-validation): `SC-D{nn}-{nnn}`
- Validated Skill: `SK-D{nn}-{nnn}`
- Sub-skill: `SK-D{nn}-{nnn}.{a}`
- Composition Pattern: `CP-{nnn}`

## Consequences

- All skill candidates use SC- prefix until promoted to SK- after Phase 3 validation
- IDs are stable under subdomain reorganization
- Maximum 999 skills per domain (expandable if needed)
