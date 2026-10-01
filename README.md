# Software Engineering Guide

A static site introducing software engineering and the ten specialisations that
make up the field. Plain HTML and CSS, no framework and no build step — open
`index.html` in a browser.

## What it covers

`index.html` is the landing page: what software engineering is and how to
choose a direction. From there, ten pages each cover one specialisation — what
the work involves, what makes it difficult, and where it leads.

| Page | Specialisation |
|---|---|
| `imparable1.html` | Data & Machine Learning |
| `imparable2.html` | Python |
| `imparable3.html` | Frontend Web |
| `imparable4.html` | Frontend Mobile |
| `imparable5.html` | Cybersecurity |
| `imparable6.html` | Internet of Things |
| `imparable7.html` | UX Research |
| `imparable8.html` | Product Design |
| `imparable9.html` | Product Management |
| `imparable10.html` | Quality Assurance |

Every page carries the same sidebar, so any specialisation is one click from any
other.

## What was fixed

The site shipped with **all ten specialisation pages at zero bytes**, so every
sidebar link landed on a blank page, and `index.html` was empty as well. The
pages are now written and the links resolve — 132 internal links, none broken.

Three other issues came out of the same pass:

- **A dead banner image.** `imparable.html` loaded its banner from
  `https://pinimg.com`, a URL that does not resolve, so the header rendered as a
  broken-image icon stretched over a 220px box. Replaced with a CSS gradient
  banner, which also removes an external request.
- **Two dead links in the header.** The top nav pointed at `register` and
  `login`, neither of which exists anywhere in the site. Replaced with anchors
  that resolve.
- **Anchors with no target.** Pages linked to `#contents`, but no element
  carried that `id`, so the link did nothing. The `id` is now on the contents
  card in all 11 pages that link to it.

## The generator

`build_pages.py` writes the ten specialisation pages from a single content
table. The shared shell — header, sidebar, footer, CSS classes — is defined once
rather than pasted into ten files, so a change to the navigation or the
structure applies everywhere.

```bash
python3 build_pages.py
```

The generated pages are committed, so running it is only necessary after editing
the content table. The script changes no existing CSS: the pages reuse the class
names `imparable.css` already defined.

## Why the filenames are unchanged

The pages are still called `imparable1.html` through `imparable10.html`. The
original name came from an assignment, and the sidebar, the filename pattern and
the cross-links are all consistent with it. Renaming would have meant rewriting
132 links for no gain; the repository name is descriptive instead.

## Project layout

```
index.html        landing page: what software engineering is
imparable.html    the introduction, and the sidebar root
imparable1-10     the ten specialisation pages
imparable.css     the stylesheet, with numbered sections
build_pages.py    regenerates the ten specialisation pages
```

## Accessibility

Semantic elements throughout, a `role="img"` with `aria-label` on the CSS
banner, and a visible skip-free but logical heading order (`h1` per page, `h2`
per section). Contrast on the gradient banner meets WCAG AA for its large text.
