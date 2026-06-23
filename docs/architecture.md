# Irecco Lab — Architecture

## Purpose
Irecco Lab is the umbrella platform and studio layer for multiple distinct software products built by one independent developer.
The architecture must support shipping one product at a time without losing the ability to reuse common modules later.

## Strategic Principle
The platform is not the first product.
The platform is a reusable foundation that grows only when it directly helps a real product ship faster, operate better, or earn sooner.

## Architectural Style
Start with a modular monolith in Python.
Do not start with microservices.
Design module boundaries now so selected modules can be extracted later if operational pressure justifies it.

## Top-Level Layers

### 1. Irecco Lab Core
Shared modules that can support multiple products:
- identity and roles
- product registry
- documentation system
- beta access and invitations
- support and feedback intake
- notifications
- admin tools

### 2. Product Shell
A repeatable product layer used by each product:
- product landing page
- docs entrypoint
- beta/waitlist flow
- support entrypoint
- release notes/changelog
- account access rules

### 3. Product Domains
Each product owns its own domain logic, terminology, workflows, and UI.
Shared core must not absorb product-specific concepts too early.

## First Product
MillWork is the first anchor product and should be the main pressure test for the platform.
Anything built in core should be justified by a real MillWork use case or a near-term second-product use case.

## Future Evolution
Potential extraction candidates in the future:
- notifications
- auth/identity
- billing/licensing
- docs publishing
- community/support

Extraction should happen only after clear pain appears:
- different scaling needs
- different deployment cycles
- strong module boundaries already proven
- operational value from separation
