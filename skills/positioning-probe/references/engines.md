# Scraping search engines

## Read this before the table

Treat the table below as a dated sample rather than a lookup. Two runs on the same machine
three hours apart disagreed about which engines worked, and the disagreement was total. The
engine the earlier run called the only working one came back degraded. One it had called
blocked came back at rank 1.

The runs differed after the client configuration changed: a different user agent, a
different curl binary, different accept-encoding. Engine-side state was not held constant,
so the cause is unresolved. Either way the lesson holds, because neither side is stable
enough to trust a stored verdict.

**So the artifact worth keeping is the control-query method, not the verdict table.** Run
the control every time. Never carry a verdict forward from a previous run, including this one.

## The control query

Pick a query whose correct top result is already known, and require that exact result before
calling an engine usable.

The run recorded here used `PyOD anomaly detection library author` and required
`github.com/yzhao062/pyod` in a parsed organic result. Any well-known repository, paper, or
homepage works. What matters is that you know the answer before you look.

Four verdicts, and the boundary between the first two is where runs go wrong:

| Verdict | Meaning |
|---|---|
| WORKING | The expected result appeared in organic results |
| DEGRADED | A response came back, possibly HTTP 200 with a full page of real results, but the expected result was absent |
| BLOCKED | An explicit throttle, CAPTCHA, or verification interstitial |
| ERROR | Route, transport, or engine identity failed |

**HTTP 200 with a real-looking result page is DEGRADED, not WORKING.** Bing returned 200
with date-calculator results for a query about an anomaly-detection library. An earlier run
recorded a page of generic AI destinations for a query about audit researchers. Both parse
cleanly, and neither is usable. Rank position is part of the check too. An engine can be
WORKING at rank 2 while another is WORKING at rank 1. That gap matters when the real query
has no known answer.

## Sample run, 2026-08-25, Windows

Verdicts from one machine on one date. Reproduce before relying on any row.

| Engine | Control | Verdict |
|---|---|---|
| DuckDuckGo HTML | rank 1 | WORKING |
| Yahoo | rank 1 | WORKING, one transient 500 first |
| Ecosia | rank 2 | WORKING |
| Yandex | rank 2 | WORKING, roughly 274 KB of HTML |
| Bing | absent | DEGRADED, unrelated results at 200 |
| Google | absent | DEGRADED, interstitial at 200 |
| Swisscows | absent | DEGRADED, shell with no organic links |
| Qwant | absent | DEGRADED, navigation only |
| Yep | absent | DEGRADED, application shell |
| Marginalia | absent | DEGRADED, 20 real results without the target |
| Brave | unverified | BLOCKED, 429 on first call |
| Mojeek | unverified | BLOCKED, CAPTCHA at 200 |
| Startpage | unverified | BLOCKED, Anubis verification page |
| Stract | unverified | ERROR, 404 |
| Mwmbl | unverified | ERROR, 303 then timeout |

Ordering that run suggested: DuckDuckGo HTML first, for the smallest response and rank 1,
then Ecosia. Yahoo comes next, with one retry on a 5xx. Put Yandex last, since its HTML is
heavy.

## Windows client note

The Git for Windows curl on `PATH` crashed with exit `-1073741819`, an access violation, on
three Startpage attempts in one run. Running the same request through the system binary at
`C:\Windows\System32\curl.exe` succeeded. When a client crashes rather than returning a status, try another
binary before concluding anything about the engine.

A request shape that worked:

```powershell
& 'C:\Windows\System32\curl.exe' -L --compressed -sS `
  -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' `
  --connect-timeout 10 --max-time 30 `
  'https://html.duckduckgo.com/html/?q=<urlencoded query>'
```

Retry one transient 5xx before moving on. Yahoo returned an empty 500 on the first call and
valid results on the next two.

## Reporting rule

When no engine passes the control, the run is unmeasurable and the correct output is a
refusal to report numbers. A unit that says "no engine passed, this is unmeasurable" is
worth more than one that says zero. Zeros from a degraded engine cannot be told apart from
real ones, and they get read as findings.
