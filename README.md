# AutoTriage: Intelligent Customer Success Pipeline

## Overview
AutoTriage is an end-to-end automated workflow designed to handle incoming customer inquiries. It acts as a digital mailroom that ingests emails, uses an AI Agent to categorize and assess urgency, routes the tasks to a project management workspace, and stores the data for long-term statistical analysis.

## The Business Problem
Manual triage of customer support emails leads to delayed response times and lost data. This project solves that by automating the ingestion, decision-making, and routing processes, leaving human workers to handle only the final resolution.

## Tech Stack & Architecture
* **Data Ingestion:** Google Apps Script (GAS)
* **Orchestration & Backend:** Python (FastAPI)
* **AI Processing:** [LLM - Gemini API]
* **Workflow Management:** Airtable (REST API, Automations, Formulas)
* **Persistent Storage:** SQL (PostgreSQL)
* **Advanced Analytics:** R (Data Wrangling & Automated Reporting)

## System Flow
1. **Listen:** GAS monitors a specific inbox for incoming emails and extracts the payload.
2. **Analyze:** Python receives the payload and passes it to an AI agent to extract sentiment, category, and urgency.
3. **Route:** Python makes a REST API call to Airtable to create an actionable ticket. Native Airtable automations alert the team based on urgency.
4. **Archive:** Python simultaneously logs the raw payload and AI insights into a relational SQL database.
5. **Analyze:** An R script periodically queries the SQL database to generate statistical trend reports.

## Phases of development
* System Architecture & Database Schema Design
* Phase 1: Data Ingestion (GAS to Python)
* Phase 2: AI Orchestration
* Phase 3: Airtable Routing
* Phase 4: SQL Archiving
* Phase 5: R Analytics
