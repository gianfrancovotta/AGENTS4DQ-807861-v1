# AGENTS FOR DATA QUALITY
REPLY × LUISS Machine Learning Project | A.A. 2025/26

**Team members:**
- Maria Dichio (822231)
- Gianfranco Votta (807861)
- Armando Fornario (813811)

**Captain:**
- Gianfranco Votta (807861)

## Section 1 — Introduction

NoiPA is the digital platform of the *Ministero dell'Economia e delle Finanze* that manages salaries, timesheets, and tax/social security obligations for employees of the Italian Public Administration. It periodically receives datasets from heterogeneous sources containing demographic, economic, or health records. Validation is currently manual or entirely absent.

This project builds a **multi-agent system** that automatically processes a raw NoiPA dataset and:
- Detects and classifies data quality issues across five dimensions
- Applies automated corrections where confidence is high
- Produces a structured **quality report** with anomalies, correction suggestions, and an overall **Reliability Score** (0–100)
