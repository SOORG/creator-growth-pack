# Creator Growth Pack

Four reusable **instruction-only AI skills** for creator acquisition, digital-product listings, storefront profiles and content planning. Version **1.2.0**.

## Copyright and resale license

**Copyright © 2026 Sorin Olariu, individual.** The official distribution account is **[SOORG on GitHub](https://github.com/SOORG/creator-growth-pack)**. The distributor account is not a separate legal entity. **Licensing contact: info@hostallin.com.**

**Current edition: SOORG License v1.0 — Commercial Use and Unmodified Resale.** See [LICENSE](LICENSE), [NOTICE](NOTICE.md), and [Reseller Guide](docs/RESELLER-GUIDE.md). You may use the Product personally/commercially and resell an **identical, complete original release**. You may not edit, translate, rebrand or redistribute only selected Product files without separate written permission. Every reseller must preserve the licensing files and state that the Product is licensed under **SOORG License v1.0**, credited to Sorin Olariu and originally published via SOORG.

**Historical exception:** v1.1.0 was released under MIT. Those earlier recipients retain rights validly granted by that license; changing the default-branch LICENSE does not cancel their permissions. See [Licensing History](docs/LICENSING-HISTORY.md). This is a proprietary/source-available license, **not an OSI-approved open-source license**. Some platforms may require different license terms.

This repository includes a Claude Code plugin manifest and portable Agent Skills. It is **not a WordPress plugin**, storefront service, email sender or automatic publishing tool. It cannot independently verify facts or execute actions; review every generated output before use.

| Skill | Output |
| --- | --- |
| `creator-outreach` | Permission-aware 3-message recruitment sequence and follow-up plan |
| `product-listing-copy` | Fact-checked listing draft, SEO tags and conditional price rationale |
| `creator-profile-setup` | Profile copy, design briefs and readiness checklist |
| `social-content-engine` | Capacity-aware 30-day calendar and draft captions |

## Install

### Claude Code — plugin

Add this Git repository using the supported Claude Code plugin installation process. The `.claude-plugin/plugin.json` manifest identifies the plugin; all four skills are inside `skills/`. Platform acceptance of custom no-modification license terms should be confirmed separately.

### Claude Code — individual skills

Copy the named directories inside `skills/` into `~/.claude/skills/` (personal) or `.claude/skills/` (project) for permitted installation and use; for example `~/.claude/skills/creator-outreach/SKILL.md`. This installation process **does not authorize resale of extracted or modified individual skills**. See the complete-package resale rule in LICENSE.

### Codex / ChatGPT Skills

Use the supported Skills import flow. Standalone skills are not equivalent to a ChatGPT Plugin. Compatibility should not be represented as verified unless tested.

### Claude.ai

Generate individual installation ZIPs with `python3 scripts/package_skills.py` and install where supported. **These ZIPs are installation artifacts, not standalone resellable Product packages.** Resellers must supply the unchanged official complete release with its LICENSE and NOTICE, not ZIPs containing extracted skills.

## Example prompts

- “Use creator-outreach to draft a respectful creator partnership sequence; here are the verified offer terms and creator's public post.”
- “Use product-listing-copy for these exact files, formats, usage rights and buyer personas.”
- “Use creator-profile-setup to improve my bio without inventing testimonials.”
- “Use social-content-engine for a month with three posts per week.”

## Accuracy and operator controls

- Any fee, payout schedule, refund period, offer, discount, price or license promise must come from **current, verified operator terms**.
- Do not invent creator observations, proof, results, file inventories, product benefits or legal compliance.
- Generate **drafts only**. Never send messages, publish listings, access accounts or authorize payments without explicit user approval and appropriate integrations.
- Follow applicable privacy, direct-marketing and platform rules. Respect opt-outs.
- If evidence is missing, use `[VERIFY]` and show the missing inputs rather than describing a draft as ready to publish.

## Tests and package checks

Run `python3 -m unittest discover -s tests -v` and `python3 scripts/package_skills.py --check`. Standard-library Python is the only build/test dependency.

See [Audit](docs/AUDIT.md), [Roadmap](docs/ROADMAP.md), [Changelog](CHANGELOG.md), [Licensing History](docs/LICENSING-HISTORY.md), [LICENSE](LICENSE), and [NOTICE](NOTICE.md).

## Contact

**Sorin Olariu — SOORG** · info@hostallin.com
