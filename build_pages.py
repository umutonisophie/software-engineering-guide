#!/usr/bin/env python3
"""Build the ten specialisation pages of the Software Engineering course site.

imparable.html shipped with a sidebar linking to imparable1.html through
imparable10.html, but all ten were zero bytes, so every sidebar link landed on a
blank page. This script writes them, reusing the exact structure and CSS class
names from imparable.html so the pages inherit the existing stylesheet with no
changes to it.

Content is written here rather than duplicated as ten hand-edited files so the
shared shell - header, sidebar, footer - stays consistent across the set.

Run:  python3 build_pages.py
"""

from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent

# The sidebar order and labels, taken from imparable.html.
SPECIALISATIONS = [
    ("imparable1", "Data & Machine Learning",
     "Teaching a computer to find patterns in data and make predictions from them."),
    ("imparable2", "Python",
     "A language readable enough to be a beginner's first and capable enough to run production systems."),
    ("imparable3", "Frontend Web",
     "The part of the application the user actually touches."),
    ("imparable4", "Frontend Mobile",
     "The same interface discipline, constrained by a phone's battery and screen."),
    ("imparable5", "Cybersecurity",
     "Finding the weaknesses before someone who is not paid to finds them."),
    ("imparable6", "Internet of Things",
     "Software for devices that report on the physical world."),
    ("imparable7", "UX Research",
     "Finding out what people actually need rather than what they say they want."),
    ("imparable8", "Product Design",
     "Turning a requirement into something coherent and usable."),
    ("imparable9", "Product Management",
     "Deciding what to build, and being able to justify why."),
    ("imparable10", "Quality Assurance",
     "The discipline that makes a claim of correctness testable."),
]

# Per-page body content. Each entry is (intro, [(heading, paragraph), ...]).
CONTENT = {
    "imparable1": (
        "Data and machine learning is the practice of building systems that improve "
        "from examples rather than from hand-written rules. It sits at the overlap of "
        "statistics, linear algebra and software engineering, and the engineering half "
        "is what separates it from a research exercise.",
        [
            ("What the work involves",
             "Exploratory analysis to understand a dataset before trusting it, then "
             "choosing a model that suits the question. Classical methods - regression, "
             "decision trees, gradient boosting - are often the right answer, because "
             "they train in seconds and their behaviour is explainable."),
            ("Why the model is only half the job",
             "A model that scores well on a test split and behaves badly in production "
             "is a common and expensive outcome. Data leakage, distribution shift between "
             "training and production, and imbalanced classes cause most of it, and none "
             "are visible from the accuracy number alone."),
            ("Where the field is heading",
             "The bottleneck has moved from model architecture to data quality and "
             "evaluation. Teams capable of measuring honestly are more valuable than teams "
             "with access to a larger model."),
        ]),
    "imparable2": (
        "Python is the default first language for new programmers and a standard tool for "
        "experienced ones. Its appeal is that it reads close to English while still "
        "supporting the concurrency and typing needed for serious work.",
        [
            ("Why it is taught first",
             "It has no compilation step, so a beginner can write a function and run it "
             "immediately. The feedback loop is the whole point: the language gets out of "
             "the way of learning to program."),
            ("What a working programmer needs beyond the basics",
             "Modules and packages, virtual environments, and a real grasp of exceptions "
             "and iterables. The standard library covers more - csv, json, sqlite3, "
             "unittest - than most curricula admit, and reaching for a dependency first is "
             "usually a mistake."),
            ("Where it is genuinely strong",
             "Data work, scientific computing, web backends and scripting. It is a poor "
             "choice for anything where predictable latency matters, and being honest "
             "about that is part of knowing the language."),
        ]),
    "imparable3": (
        "Frontend web development builds the interface a user interacts with, and owns "
        "three problems at once: structure, behaviour, and a rendering model the browser "
        "controls.",
        [
            ("The three layers",
             "HTML carries meaning, CSS carries presentation, JavaScript carries behaviour. "
             "Keeping those concerns separate is what makes a frontend maintainable - the "
             "moment presentation logic leaks into scripts, every change risks breaking layout."),
            ("Responsive design",
             "A layout has to survive viewports from a 320px phone to an ultrawide monitor. "
             "Flexible units, media queries and CSS Grid handle most cases; the discipline is "
             "testing at the extremes rather than at one comfortable width."),
            ("Accessibility is not optional",
             "Semantic elements give screen reader users structure for free, visible focus "
             "states help keyboard users, and colour contrast is a legal requirement in many "
             "jurisdictions. All three are cheap when designed in and expensive to retrofit."),
        ]),
    "imparable4": (
        "Mobile frontend work applies the same interface discipline to a device with a "
        "battery, a thermal limit, a touch screen and an operating system that can kill your "
        "process without warning.",
        [
            ("The constraints are the design",
             "Mobile users are often on a metered connection, so payload size is a user-facing "
             "decision. A slow app on a cheap Android device is a real failure, not an edge case."),
            ("Platform specifics",
             "iOS and Android differ in navigation conventions, permission dialogs and review "
             "requirements. Flutter and React Native share code across both; a native build in "
             "Swift or Kotlin still wins where platform integration is the product."),
            ("State that survives",
             "A mobile app is routinely killed in the background, so state has to be persisted "
             "and restored deliberately rather than held in memory and trusted."),
        ]),
    "imparable5": (
        "Cybersecurity is the discipline of finding, understanding and fixing weaknesses in "
        "software, and of assuming an attacker is already probing for them.",
        [
            ("How vulnerabilities are found",
             "Reading code for logic errors, fuzzing inputs, and threat-modelling a design "
             "before it is built. Most serious breaches come from a simple mistake in one of "
             "these, not from an exotic technique."),
            ("Classes of weakness worth knowing",
             "Injection flaws when untrusted input reaches a query, broken access control when "
             "the server trusts the client, and insecure deserialisation. Broken access control "
             "is consistently the most common and most severe, because it needs no special skill "
             "to exploit."),
            ("Defence in depth",
             "No single control holds. Parameterised queries, least-privilege access, hashed "
             "passwords, and keeping dependencies patched each catch what the others miss."),
        ]),
    "imparable6": (
        "Internet of Things work is software for devices that sense and act on the physical "
        "world, which introduces failure modes a web application never has.",
        [
            ("What changes with physical devices",
             "Sensors report wrong values, networks drop, and devices lose power mid-write. "
             "Software has to treat bad input as the normal case rather than the exception."),
            ("Security is harder by default",
             "A device may have no screen, may ship with a shared default password, and is often "
             "on a home network with no oversight. Devices that are reachable for a decade after "
             "purchase make update mechanisms a design requirement, not an afterthought."),
            ("Common architecture",
             "A constrained microcontroller reading a sensor, a gateway translating protocols, "
             "and a backend that stores and aggregates. The interesting engineering is usually "
             "at the boundaries."),
        ]),
    "imparable7": (
        "UX research studies how people actually use a product, so that design decisions rest "
        "on evidence rather than on the loudest opinion in the room.",
        [
            ("What the method actually is",
             "Interviews, observation, and usability testing, analysed for patterns. The output "
             "is not a set of preferences but a set of findings about behaviour, which is a much "
             "narrower and more useful claim."),
            ("Finding versus fixing",
             "A study that produces a list of complaints has not done its job. The work is "
             "identifying the underlying problem - a user who cannot find the button may be "
             "blocked by terminology, not layout."),
            ("Honesty about evidence",
             "A small usability test can tell you that people cannot complete a task. It cannot "
             "tell you the market will buy the product. Overstating a method's reach is the most "
             "common way research gets misused."),
        ]),
    "imparable8": (
        "Product design turns a requirement into something coherent, usable and buildable, and "
        "is accountable for how it feels as well as how it works.",
        [
            ("Designing the thing, not the screen",
             "A design covers states that are easy to omit: empty, loading, error, offline, and "
             "the case where a user has done something unexpected. Interfaces are mostly these "
             "edge states, not the happy path."),
            ("Working in systems",
             "Components, tokens and consistent patterns mean a new feature inherits existing "
             "behaviour instead of reinventing it. Consistency is what makes an interface feel "
             "predictable."),
            ("Design and engineering are one conversation",
             "A design that cannot be built within its constraints is a wish. The strongest work "
             "happens when the designer and the engineer argue it out before implementation starts."),
        ]),
    "imparable9": (
        "Product management decides what gets built and, more importantly, can explain why. It "
        "is the discipline of choosing between options when every one of them has a constituency.",
        [
            ("Prioritising is the actual job",
             "Requests arrive from sales, support, engineering and users, each with a legitimate "
             "claim. Choosing means weighing reach, effort, risk and strategic fit, and being "
             "able to defend the decision afterwards."),
            ("Writing the specification",
             "A good PRD states the problem, the users, the success measure and what is explicitly "
             "out of scope. Most of its value is in agreeing what will not be built, because that "
             "is the part every stakeholder otherwise assumes is still coming."),
            ("Measuring afterwards",
             "Shipping without a defined success metric means the outcome can only be argued "
             "about. Deciding what counts as a win has to happen before the work, not after."),
        ]),
    "imparable10": (
        "Quality assurance is the discipline that makes a claim of correctness testable. Its "
        "purpose is not to catch every possible bug but to make the risk of an undetected one "
        "visible and low.",
        [
            ("Testing pyramid, and why the shape",
             "Many fast unit tests, fewer integration tests, fewest end-to-end tests. Unit tests "
             "are cheap and pinpoint failures; end-to-end tests catch real integration problems "
             "but are slow and flaky, so a large suite of them costs more than it returns."),
            ("What a good test asserts",
             "Behaviour the code actually has, including failure paths. A test asserting that "
             "multiply(5, 4) returns 10 proves very little; asserting that it rejects a "
             "non-numeric input proves something real."),
            ("Automation and its limit",
             "Automating a manual test that is never run adds nothing. A broken test that the "
             "team learns to ignore is worse than no test at all, because it reports safety while "
             "providing none."),
        ]),
}

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Software Engineering Master - {title}</title>
    <link rel="stylesheet" href="imparable.css">
</head>
<body>

    <header>
        <nav class="top-nav">
            <a href="imparable.html">Home</a>
            <a href="#contents">Contents</a>
        </nav>
    </header>

    <div class="main-wrapper">

        <nav class="sidebar-links">
{sidebar}
        </nav>

        <main class="content-area">
            <article class="card inline-contents">
                <h3>Contents</h3>
{contents}
            </article>

            <article class="card explanation-section">
                <h1>{title}</h1>
                <p>{intro}</p>
{sections}
            </article>
        </main>

    </div>

    <footer class="conclusion-footer">
        <p>Conclusion &copy; 2026 Software Engineering Master</p>
    </footer>

</body>
</html>
"""


def build_sidebar(current_slug: str) -> str:
    lines = []
    for slug, label, _ in SPECIALISATIONS:
        if slug == current_slug:
            lines.append(f'            <a href="{slug}.html">{label}</a>')
        else:
            lines.append(f'            <a href="{slug}.html">{label}</a>')
    return "\n".join(lines)


def main() -> None:
    for slug, title, _ in SPECIALISATIONS:
        intro, sections = CONTENT[slug]

        contents = "\n".join(
            f"                <p>{heading}</p>" for heading, _ in sections
        )

        body = []
        for heading, paragraph in sections:
            body.append(f"                <h2>{heading}</h2>")
            body.append(f"                <p>{paragraph}</p>")
        sections_html = "\n".join(body)

        html = PAGE_TEMPLATE.format(
            title=title,
            sidebar=build_sidebar(slug),
            contents=contents,
            intro=intro,
            sections=sections_html,
        )
        (OUT_DIR / f"{slug}.html").write_text(html, encoding="utf-8")
        print(f"wrote {slug}.html  ({len(html):,} bytes)  {title}")


if __name__ == "__main__":
    main()
