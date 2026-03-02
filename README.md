Here is a clean and professional README content without emojis or decorative elements:

---

# Secure Multi-App Tool Architecture

Role-Based Sales & Finance Analytics Platform

## Overview

This project is a secure, modular analytics dashboard built using Streamlit. It implements Role-Based Access Control (RBAC), dynamic query routing, audit logging, and interactive data visualizations.

The platform simulates an enterprise analytics system where different departments can access only the insights relevant to their assigned roles. User authentication, permission validation, query routing, and logging are handled through a clean modular architecture.

---

## Features

* Secure authentication system
* Role-Based Access Control (Admin, Sales, Finance, Operations)
* Intelligent query-to-tool routing
* Interactive Plotly visualizations
* Audit logging for user activity tracking
* Dark-themed enterprise dashboard interface
* Modular and scalable project structure

---

## Role Permissions

Admin

* Full access to all tools
* Access to audit logs

Sales

* Sales summary
* Region analysis
* Model comparison

Finance

* Profit trend
* Expense breakdown

Operations

* Units sold trend

---

## Project Structure

app.py – Main Streamlit application
auth.py – Authentication logic
access_control.py – Role permission rules
query_router.py – Query routing logic
tools.py – Analytics tool registry
logger.py – Audit logging system
schema.json – Schema configuration
dataset.csv – Sample dataset
audit_log.txt – System activity logs

---

## Tech Stack

Python
Streamlit
Plotly
Pandas
JSON Configuration

---

## How to Run

pip install -r requirements.txt
streamlit run app.py

---

## Purpose

This project demonstrates secure system design, clean modular architecture, RBAC implementation, and integration between backend logic and frontend visualization. It is suitable for showcasing skills in data engineering, backend development, analytics engineering, and business intelligence.
