# HTML to PDF Converter

**A lightweight helper tool for developers**

A small, focused utility for converting HTML content into high-quality PDF documents. Designed as a convenience tool for developers who need quick, reliable HTML → PDF output without setting up a full PDF pipeline.

> ⚠️ **Not a commercial product** — This is a personal utility built to solve a common developer pain point. No subscriptions, no paywalls, no upsells. Just a tool that does one thing well.

---

## 🛠️ Built With

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Azure_Functions-0062AD?style=for-the-badge&logo=azure-functions&logoColor=white" alt="Azure Functions"/>
  <img src="https://img.shields.io/badge/Azure_Static_Web_Apps-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white" alt="Azure Static Web Apps"/>
  <img src="https://img.shields.io/badge/WeasyPrint-2C3E50?style=for-the-badge&logo=python&logoColor=white" alt="WeasyPrint"/>
  <img src="https://img.shields.io/badge/Milligram-9B59B6?style=for-the-badge&logo=css3&logoColor=white" alt="Milligram CSS"/>
</p>

<p>
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
</p>

---

## Why This Exists

Generating PDFs from HTML is a common need during development — exporting reports, generating invoices, validating print layouts, testing CSS `@page` rules, or producing shareable documents from web content.

This tool removes friction by providing a simple interface and a single-purpose API that does one thing well.

**This is not a startup. This is not a SaaS.** It's a developer helping other developers skip the boilerplate.

---

## What It's Good At

- Turning HTML + CSS into print-ready PDFs
- Preserving layout, typography, and page rules
- Handling real-world HTML (not just toy examples)
- Staying out of your way

It's meant to be **used**, not configured.

---

## Intended Audience

This tool is for:

- Web developers
- Backend developers
- Full-stack engineers
- Anyone who already understands HTML/CSS and just wants a PDF

It is **not** intended as a learning resource, a tutorial on PDF generation, or a framework.

---

## How It's Typically Used

1. Paste or send HTML you already have
2. Quickly validate PDF output
3. Download the generated PDF
4. Move on with your work

No assumptions about frameworks, languages, or workflows.

---

## Output Quality

The PDF rendering supports:

- CSS layouts (flexbox, grid, tables)
- Fonts and typography
- Page size and margins
- Print-specific rules (`@page`, page breaks, etc.)

The goal is **predictable, production-grade output** — not screenshots or browser print hacks.

---

## Quick Tech Overview

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Frontend** | HTML5, Vanilla JS, Milligram CSS | Clean, minimal UI |
| **Backend** | Python 3.10, Azure Functions | Serverless API |
| **PDF Engine** | WeasyPrint | HTML/CSS → PDF rendering |
| **Hosting** | Azure Static Web Apps | Fast, free-tier friendly |
| **CI/CD** | GitHub Actions | Automated deployments |

---

## Design Philosophy

- Minimal UI
- No unnecessary options
- Fast feedback
- Sensible defaults
- Developer-first ergonomics

---

## Stability Note

This is a helper tool, not a public platform. Interfaces and internals may evolve to better serve developer workflows. Use it, fork it, adapt it.

---

## License

**MIT** — Free to use, modify, and distribute.

---

<p align="center">
  <i>Built with Python, Azure, and a focus on simplicity.</i><br/>
  <i>Made by a developer, for developers.</i>
</p>