# Multi-Agent Customer Assistant

## Description

This project implements a multi-agent system using the Google Agent Development Kit (ADK). The system is designed to assist Spanish-speaking users with inquiries related to billing and identity/access management (IAM). It features a `root_agent` that intelligently routes user requests to specialized sub-agents: `billing_agent` and `iam_agent`.

All agent responses are configured to be provided in Spanish.

## Features

*   **Spanish Language Support:** Designed primarily for Spanish language interactions.
*   **Specialized Sub-Agents:**
    *   `billing_agent`: Handles invoice analysis and billing-related questions.
    *   `iam_agent`: Manages password resets and Multi-Factor Authentication (MFA) setup.
*   **Hierarchical Orchestration:** A `root_agent` receives user queries, requires a User ID for context, and delegates tasks to the appropriate sub-agent.
*   **Tool Integration:** Agents leverage predefined Python functions as tools to perform specific actions.

## Components

The system consists of the following key agents and tools:

*   **Agents (from `google.adk.agents`):**
    *   `root_agent`: The main entry point for user interactions. It delegates tasks to `iam_agent` or `billing_agent` based on the query. It's instructed to always request a User ID if not provided.
    *   `iam_agent`: Specializes in Identity and Access Management tasks. It uses the `reset_password` and `setup_mfa` tools.
    *   `billing_agent`: Specializes in billing and invoice inquiries. It uses the `analyze_billing` tool.

*   **Tools (Python Functions):**
    *   `analyze_billing(user_id: str)`: Simulates analyzing a user's invoice and returns a summary.
    *   `reset_password(userid: str)`: Simulates sending a password reset link to the user's registered email.
    *   `setup_mfa(userid: str, phone: str)`: Simulates setting up MFA for a user's account using their phone number.
    *   `search_web(query: str)`: Simulates performing a web search. (Note: This tool is defined but not currently assigned to any agent in the provided configuration).

## Prerequisites

*   Python 3.7+
*   Google Agent Development Kit (ADK) library (`google.adk`) and its dependencies.

## Installation

Ensure the ADK library and its dependencies are available in your Python environment. For Google internal usage, this typically involves including the necessary dependencies in your `BUILD` file.


##  Usage

To use the system, interact with the root_agent instance using the methods provided by the ADK framework. The root_agent will handle the query and orchestrate with the sub-agents as needed.

## Example Scenarios:

A user sends a query like "¿Cuánto es mi factura este mes?" (How much is my bill this month?). The root_agent, ensuring it has the User ID, would delegate this to the billing_agent. The billing_agent would invoke the analyze_billing tool.
A user sends a query like "Olvidé mi contraseña, ¿qué hago?" (I forgot my password, what do I do?). The root_agent would delegate this to the iam_agent. The iam_agent would invoke the reset_password tool.
All responses from the agents will be in Spanish, as per their configuration.
