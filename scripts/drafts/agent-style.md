🚀 agent-style: 21 drop-in writing rules that shape how AI coding agents write like a tech pro.

Works with any AGENTS.md-compliant tool: Claude Code, Codex, Copilot, Cursor, Aider, and more. 12 rules from canonical writing authorities (Strunk & White, Orwell, Pinker, Gopen & Swan), 9 from field observation of LLM output.

v0.3.0 sanity bench, AI-tell violations on 10 fixed prose tasks:
• Claude Opus 4.7: 105 → 58 (-45%)
• GPT-5.4 via Codex: 51 → 28 (-45%)
• Gemini 3 Flash: 79 → 14 (-82%)

How it works:
• Injected into the agent's system prompt, so the first draft already reads clean
• Deterministic audit layer catches em-dashes, transition openers, cliché verbs, contractions, same-starts
• One `pip install agent-style` or a drop-in AGENTS.md block

213+ GitHub stars in 3 days.

Install: pip install agent-style
Repo: https://github.com/yzhao062/agent-style
Docs: https://viterbi-web.usc.edu/~yzhao010/agent-style.html

#AIAgents #LLMs #OpenSource #Python #PromptEngineering
