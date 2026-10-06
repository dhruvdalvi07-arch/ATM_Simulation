# ATM Card Mechanism Simulation (Python)

A console-based ATM simulation developed in Python that models authentication, card validation, account operations, and multi-session state handling using in-memory data structures.

---

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Programming Concepts Used](#programming-concepts-used)
- [Application Flow & Logic](#application-flow--logic)
- [Pre-configured Accounts](#pre-configured-accounts)
- [Setup and Execution](#setup-and-execution)
- [Usage Guide](#usage-guide)
- [File Structure](#file-structure)

---

## Overview

This project simulates the core operational pipeline of an Automated Teller Machine (ATM). It manages authentication, verifies user credentials, provides a menu-driven interface for banking actions (checking balances, cash withdrawals, deposits, and updating PINs), and supports repeated operations across multiple accounts without resetting state mid-execution.

---

## Key Features

1. **Card Validation & PIN Authentication**
   - Verifies card presence in the internal database before granting access.
   - Restricts operations until a valid matching PIN is supplied.

2. **Per-Transaction Security**
   - Requires PIN confirmation on every individual operation (Balance Inquiry, Cash Withdrawal, Cash Deposit) to ensure heightened security per action.

3. **In-Memory Session Persistence**
   - Modifications (such as balance deductions/additions or PIN updates) stay active and accessible across multiple sessions within the same runtime.
   - Allows changing a PIN, ending the card session, and logging back in with the newly updated PIN immediately.

4. **Two-Tier Exit Control**
   - **Account-Level Exit (Option 5):** Concludes the active card session, prints a card-retrieval message, and loops back to the main card prompt while preserving state.
   - **System-Level Shutdown:** Entering `exit` or `quit` at the primary card prompt terminates the script completely.

5. **Input Sanitation & Error Handling**
   - Blocks negative amounts, non-numeric values, or zero-value transactions.
   - Enforces balance limits to prevent overdrafting during cash withdrawals.
   - Requires matching PIN confirmation before saving updates.

---

## Programming Concepts Used

- **Variables & Basic Data Types:** Strings, floats, booleans, and integers.
- **Data Structures:** Nested Python dictionaries mapping unique card numbers to account attributes (`name`, `pin`, `balance`).
- **Control Flow:** `if`, `elif`, and `else` conditional branching for validation and menu routing.
- **Nested Loops:** Outer loop controlling system uptime and inner loop managing the active customer session.
- **Basic Arithmetic Operations:** Real-time updates to financial balances.
- **String Manipulation:** Input trimming (`.strip()`), normalization (`.lower()`), and formatted currency output (`:,.2f`).

---

## Application Flow & Logic

```text
[START]
   │
   ▼
[Enter Card Number] ──(Type 'exit' / 'quit')──► [SHUTDOWN SYSTEM]
   │
   ├─► Not Found ──► "Invalid card number" ──► (Loop back)
   │
   ▼ (Valid Card)
[Enter Initial PIN]
   │
   ├─► Mismatch ──► "Incorrect PIN" ──► (Loop back)
   │
   ▼ (Authenticated)
[Display ATM Menu (Options 1–5)]
   │
   ├── 1. Check Balance ──► Verify PIN ──► Show Current Balance
   ├── 2. Withdraw Money ──► Verify PIN ──► Validate Bounds & Balance ──► Deduct
   ├── 3. Deposit Money  ──► Verify PIN ──► Validate Amount > 0 ──► Add
   ├── 4. Change PIN     ──► Verify Current PIN ──► Match New PINs ──► Update Key
   └── 5. Exit Session   ──► Eject Card ──► [Return to Enter Card Number]
