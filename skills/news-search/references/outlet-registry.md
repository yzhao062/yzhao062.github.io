# Outlet Registry

Classification of outlets by tier, with `site:` domains for Dimension 3 sweep queries.

**Normalization rule:** Each row must have exactly one search-ready domain (suitable for `site:{domain}` queries). No comma-separated domains, no URL paths. If an outlet has multiple domains, split into separate rows.

---

## Tier 1 Outlets (mainstream tech/business press)

If a result appears in these outlets, it is Tier 1 coverage.

### Tech Press

| Outlet | Domain | Focus |
|--------|--------|-------|
| TechCrunch | techcrunch.com | Startups, tech news |
| VentureBeat | venturebeat.com | Enterprise AI, transformative tech |
| Wired | wired.com | Tech, culture, science |
| The Verge | theverge.com | Tech, science, culture |
| Ars Technica | arstechnica.com | Tech deep dives |
| MIT Technology Review | technologyreview.com | Tech and science |
| IEEE Spectrum | spectrum.ieee.org | Engineering, computing |
| TechRadar | techradar.com | Consumer tech, cybersecurity |
| Tom's Hardware | tomshardware.com | Hardware, AI |
| TechSpot | techspot.com | Tech news |
| InfoQ | infoq.com | Software engineering |
| The New Stack | thenewstack.io | Developer infrastructure |

### Security Press

| Outlet | Domain | Focus |
|--------|--------|-------|
| Dark Reading | darkreading.com | Enterprise cybersecurity |
| The Hacker News | thehackernews.com | Security news |
| SecurityWeek | securityweek.com | Cybersecurity |
| SC Magazine | scmagazine.com | Security professionals |
| Bleeping Computer | bleepingcomputer.com | Security, tech support |
| Krebs on Security | krebsonsecurity.com | Investigative security |
| The Record | therecord.media | Cybersecurity journalism |
| CyberNews | cybernews.com | Cyber threat news |
| CSO Online | csoonline.com | Security leadership |

### Business Press

| Outlet | Domain | Focus |
|--------|--------|-------|
| Forbes | forbes.com | Business, tech |
| Fortune | fortune.com | Business |
| Bloomberg | bloomberg.com | Finance, tech |
| Wall Street Journal | wsj.com | Finance, business |
| Reuters | reuters.com | Wire service |
| Financial Times | ft.com | Global business |

### Science Press

| Outlet | Domain | Focus |
|--------|--------|-------|
| Nature News | nature.com | Science journalism |
| Science Magazine | science.org | Science journalism |
| Scientific American | scientificamerican.com | Popular science |
| New Scientist | newscientist.com | Science news |
| Phys.org | phys.org | Science news syndication |

---

## Tier 1.5 Outlets (policy, trade press, VC)

### Government Trade Press

Outlets that report on government rather than publish government documents. The U.S. government-publishing domains (congress.gov, senate.gov, house.gov, gao.gov, whitehouse.gov, federalregister.gov, nist.gov, nsf.gov, energy.gov, etc.) live in their Tier 0 home under "Government Document Sources" below; do not duplicate them here.

| Outlet | Domain | Focus |
|--------|--------|-------|
| FedScoop | fedscoop.com | Federal IT policy news |
| MeriTalk | meritalk.com | Government IT news |
| NextGov/FCW | nextgov.com | Federal technology news |

### Policy, Think Tanks & Research Institutes

| Outlet | Domain | Focus |
|--------|--------|-------|
| Future of Life Institute | futureoflife.org | AI safety policy, Safety Index |
| Brookings Institution | brookings.edu | AI policy research |
| RAND Corporation | rand.org | Defense and policy research |
| AI Now Institute | ainowinstitute.org | AI policy and rights |
| Center for AI Safety (CAIS) | safe.ai | AI safety research, benchmarks |
| Center for Security and Emerging Technology (CSET) | cset.georgetown.edu | Georgetown, AI/national security |
| Stanford HAI | hai.stanford.edu | Stanford Human-Centered AI |
| MIT CSAIL | csail.mit.edu | MIT AI research news |
| Berkeley AI Research (BAIR) | bair.berkeley.edu | Berkeley AI blog |
| Partnership on AI | partnershiponai.org | Multi-stakeholder AI policy |
| Alan Turing Institute | turing.ac.uk | UK national AI institute |
| World Economic Forum | weforum.org | Global AI governance reports |
| OECD AI Policy Observatory | oecd.ai | International AI policy tracker |
| International AI Safety Report | internationalaisafetyreport.org | Multi-government AI safety assessment (Bengio-led, 30+ countries) |
| Privacy International | privacyinternational.org | Digital rights, surveillance, AI privacy policy |
| IEEE Standards Association | standards.ieee.org | AI/ML technical standards |
| ISO | iso.org | International standards |

### Consulting & Industry Reports

| Outlet | Domain | Focus |
|--------|--------|-------|
| McKinsey | mckinsey.com | Strategy, AI reports |
| Deloitte | deloitte.com | Tech trends, audit, AI |
| PwC | pwc.com | Risk, AI governance |
| Accenture | accenture.com | Technology, security |
| EY (Ernst & Young) | ey.com | AI governance, audit |
| KPMG | kpmg.com | AI trust, governance |
| Bain & Company | bain.com | Tech strategy |
| BCG (Boston Consulting Group) | bcg.com | AI and digital reports |
| IBM Research | research.ibm.com | AI research blog |
| Google DeepMind Blog | deepmind.google | AI research blog |
| Microsoft Research Blog | microsoft.com/en-us/research/blog | AI research highlights |
| Cisco Research | blogs.cisco.com | Security, networking AI |

### Standards Bodies & Frameworks

| Outlet | Domain | Focus |
|--------|--------|-------|
| OWASP | owasp.org | Application security standards |
| OWASP GenAI | genai.owasp.org | AI-specific security standards |
| NIST AI | airc.nist.gov | AI Risk Management Framework |
| MITRE ATLAS | atlas.mitre.org | Adversarial ML threat matrix |
| Cloud Security Alliance | cloudsecurityalliance.org | AI security guidance |
| MLCommons | mlcommons.org | ML benchmarks and standards |

### VC & Investment

| Outlet | Domain | Focus |
|--------|--------|-------|
| Bessemer Venture Partners | bvp.com | VC landscape reports |
| Andreessen Horowitz (a16z) | a16z.com | VC tech analysis |
| Sequoia | sequoiacap.com | VC insights |

---

## Books & Reference (Tier 4 if cited by name)

| Source | Domain | Focus |
|--------|--------|-------|
| Google Books | books.google.com | Textbooks, monographs citing your work |
| O'Reilly | oreilly.com | Technical books and learning platforms |
| Manning | manning.com | Technical books, liveProjects |
| Springer | link.springer.com | Academic book chapters |
| Wiley | wiley.com | Academic and professional books |

---

## Government Document Sources (Tier 0 if names your work)

These are high-value for tenure cases. Search for your tool/paper names within these. Phase A should tag candidates from these domains with `outlet_class: gov-pdf` per `references/domain-registry.md`. This section is the single home for U.S. government-publishing domains; do not duplicate them in Tier 1.5.

| Source | Domain | How to search |
|--------|--------|---------------|
| Congress.gov full text | congress.gov | Search bills, reports, hearings for tool names |
| Senate Reports | senate.gov | Senate committee reports, hearing testimony PDFs |
| House Reports | house.gov | House committee reports, hearing testimony PDFs |
| CRS Reports | crsreports.congress.gov | Congressional Research Service analyses |
| GAO Reports | gao.gov | Government accountability studies |
| White House / Executive | whitehouse.gov | Executive orders, OMB memos, OSTP reports |
| Federal Register | federalregister.gov | RFIs, rules, notices mentioning AI tools |
| NIST (main) | nist.gov | NIST announcements, RFIs, blog (publication PDFs at nvlpubs.nist.gov) |
| NIST Publications | nvlpubs.nist.gov | Standards documents, special publications |
| NSF | nsf.gov | NSF announcements, dear colleague letters, program solicitations; awards mentioning your work via the /awardsearch path |
| DOE | energy.gov | Department of Energy publications |
| DOE Technical Reports | osti.gov | National lab reports |

## Patent Sources (Tier 3 ecosystem evidence if names your work)

Patents are a separate source class from government documents. Phase A should tag candidates from these domains with `outlet_class: patent`. See `references/domain-registry.md` § Patents for the seeded domain list. Patent hits belong in the Ecosystem adoption ledger; only elevate to a higher tier if a separate government or policy report independently cites the same work.

| Source | Domain | How to search |
|--------|--------|---------------|
| Google Patents | patents.google.com | Full-text search and citation links |
| WIPO PatentScope | patentscope.wipo.int | Global patent database |
| USPTO | uspto.gov | USPTO patent search and PAIR |

---

## Tier 2 Outlets (industry press, institutional PR)

| Outlet | Domain | Focus |
|--------|--------|-------|
| KDnuggets | kdnuggets.com | Data science |
| Analytics Vidhya | analyticsvidhya.com | Data science education |
| Towards Data Science (Medium) | towardsdatascience.com | Data science blog |
| MarkTechPost | marktechpost.com | AI research news |
| AI:PRODUCTIVITY | aiproductivity.ai | AI tools news |
| DEV Community | dev.to | Developer community |
| Hacker News | news.ycombinator.com | Tech community |
| Reddit r/MachineLearning | reddit.com/r/MachineLearning | ML community |
| USC Viterbi News | viterbischool.usc.edu | University PR |
| Harvard Medical School News | hms.harvard.edu | University PR |
| Amazon Science | amazon.science | Industry research |
| Google AI Blog | blog.google | Industry research |
| LLNL Computing | computing.llnl.gov | National lab |
| AI Accelerator Institute | aiacceleratorinstitute.com | AI industry |
| CCC Blog | cccblog.org | Computing research community |
| Grokipedia | grokipedia.com | AI encyclopedia |

---

## Tier 2.5 Outlets (AI newsletters, vendor research blogs)

| Outlet | Domain | Focus |
|--------|--------|-------|
| The Batch (deeplearning.ai) | deeplearning.ai | Andrew Ng's newsletter |
| Import AI | importai.net | Jack Clark's policy newsletter |
| The Gradient | thegradient.pub | AI research magazine |
| Synced Review | syncedreview.com | AI research news |
| AI News | artificialintelligence-news.com | AI industry news |
| Palo Alto Networks Blog | paloaltonetworks.com | Enterprise security research |
| Cisco Blog | blogs.cisco.com | Enterprise networking/security research |

---

## Industry Analysts (Tier 1.5 if mentioned)

| Firm | Domain |
|------|--------|
| Gartner | gartner.com |
| Forrester | forrester.com |
| IDC | idc.com |
| McKinsey | mckinsey.com |
| Deloitte | deloitte.com |
| PwC | pwc.com |
| Accenture | accenture.com |
| OWASP | owasp.org |
| OWASP GenAI | genai.owasp.org |
