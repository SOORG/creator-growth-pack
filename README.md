# Creator Growth Pack

Four reusable, **instruction-only AI skills** for creator acquisition, digital-product listings, storefront profiles and content planning. Version **1.1.0**.

This repository includes a Claude Code plugin manifest and portable Agent Skills. It is **not a WordPress plugin**, storefront service, email sender or automatic publishing tool. It cannot independently verify facts or execute actions; review every generated output before use.

| Skill | Output |
| --- | --- |
| `creator-outreach` | Permission-aware 3-message recruitment sequence and follow-up plan |
| `product-listing-copy` | Fact-checked listing draft, SEO tags and conditional price rationale |
| `creator-profile-setup` | Profile copy, design briefs, readiness checklist |
| `social-content-engine` | Capacity-aware 30-day calendar and draft captions |

## Install

### Claude Code — plugin

Use Claude Code's plugin installation flow to add this Git repository as a plugin source, or install skill folders directly as below. The `.claude-plugin/plugin.json` manifest identifies the plugin; all four skills live in `skills/`.

### Claude Code — individual skills

Clone the repository and copy the contents of `skills/` (each **named skill folder**, not the outer pack folder) into either `~/.claude/skills/` for personal use or `.claude/skills/` in a project. A valid location is `~/.claude/skills/creator-outreach/SKILL.md`.

### Codex / ChatGPT Skills

Import the individual `skills/<skill-name>/` directories using your product's supported Skills installation flow. Standalone skills are not equivalent to a ChatGPT Plugin; a different publishing process may be required. Avoid copying raw `SKILL.md` text into `.cursor/rules/` as though it were a native Cursor rule.

### Claude.ai

Create an individual ZIP for each skill with `python3 scripts/package_skills.py`, then upload a skill ZIP through Claude's custom-skill interface where available. The packaging script puts `SKILL.md` at each archive root.

## Example prompts

- “Use creator-outreach to draft a respectful creator partnership sequence; here are the verified offer terms and creator's public post.”
- “Use product-listing-copy for these exact files, formats, usage rights and buyer personas.”
- “Use creator-profile-setup to improve my bio without inventing testimonials.”
- “Use social-content-engine for a month with three posts per week.”

## Accuracy and operator controls

- Any fee, payout schedule, refund period, offer, discount, price or license promise must come from **current, user-provided terms**, not from examples in this pack.
- Do not invent creator observations, proof, results, file inventories, product benefits, availability or legal compliance.
- Generate **drafts only**. Never send messages, publish listings, access personal accounts or authorize payments without explicit user approval and an appropriate integration.
- Follow applicable privacy, direct-marketing and platform rules; honor opt-outs. This pack does not provide legal advice.
- If evidence is missing, use `[VERIFY]` and show the missing inputs; do not describe a draft as ready to publish.

## Quality checks

Run `python3 -m unittest discover -s tests -v` and `python3 scripts/package_skills.py --check` before releasing. Python standard library is the only build/test dependency; skill execution needs no scripts.

See [AUDIT](docs/AUDIT.md), [ROADMAP](docs/ROADMAP.md), [CHANGELOG](CHANGELOG.md), [example operator terms](examples/platform-terms.example.md), [LICENSE](LICENSE) and [NOTICE](NOTICE.md). The selling notes are draft templates, not guarantees.

## Maintainer

Copyright notice: Host All in (as stated in the supplied source). Verify the legal rights holder and commercial publication permissions before selling branded releases. Support contact in supplied source: `support@hostallin.com` (not operationally verified).
