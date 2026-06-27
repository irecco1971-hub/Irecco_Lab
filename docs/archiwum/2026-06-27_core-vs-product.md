# Irecco Lab — Core vs Product Boundary

## Goal
Prevent the shared platform from becoming bloated.
Anything placed in core should have strong reuse potential or immediate operational value.

## Belongs to Core
- users
- roles and permissions
- product registry
- docs framework
- beta invitations and access states
- generic feedback intake
- notifications infrastructure
- admin dashboard foundation
- audit/logging foundation

## Belongs to Product
- product terminology
- product-specific data models
- product-specific onboarding
- product-specific feature logic
- product-specific UI flows
- product-specific support categories
- product-specific release notes content

## Belongs to Backlog
- universal billing before billing exists
- shared marketplace before multiple products need it
- multi-brand complexity before product count justifies it
- advanced analytics before real traffic exists
- microservices before boundaries are proven

## Decision Filter
Before adding something to core, ask:
1. Does MillWork need this now?
2. Is reuse by another product realistic, not hypothetical?
3. Will building this now reduce future delivery cost?

If the answer is no to two or more, keep it out of core.
