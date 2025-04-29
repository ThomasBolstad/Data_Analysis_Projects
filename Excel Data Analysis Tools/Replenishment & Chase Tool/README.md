# Replenishment Report – Licensed Sports Product Chase Tool

This Excel-based replenishment tool identifies top-selling licensed sports products that require backfill, driving smarter inventory chases by team, gender, store tier, and subclass. It was used in-season to dynamically allocate inventory to high-demand store-team combinations with high sell-through rates.

---

## 📁 Tabs & Functional Overview

- **Instructions**: Guide for using the report — steps for updating inputs and reviewing chase recommendations.
- **Replen Template Dump**: Raw store-level sell-through data (daily or weekly) used to drive replenishment logic.
- **Buyplan Dump**: Cross-references planned buys with actual sales to monitor fulfillment gaps.
- **Team Rollup / Team Gender Rollup / Team Gender Store Rollup**: Aggregates sales and inventory by key dimensions to highlight over/under-performing combinations.
- **Subclass Store Rollup**: Identifies sales trends by subclass and store tier to prioritize replenishment focus.
- **Top Styles To Replen**: Final prioritized output for chasing — includes sell-through, on-hand, velocity, and suggested units to order.
- **Team / Tiers**: Metadata tabs with store-team relationships and tier assignments.
- **Coding**: Logic to categorize styles and flag valid replen candidates.

---

## 🔹 Key Features

- **Velocity-Based Replenishment**: Identifies fast-selling styles based on current sell-through rates and remaining on-hand.
- **Team + Gender + Tier Rollups**: Ensures targeted replenishment by matching demand signals to regional and format-based strategies.
- **Buyplan Gap Comparison**: Highlights which buys have under-executed and need backfill.
- **Top Styles Prioritization**: Outputs a sorted list of styles with the most urgent chase opportunity, ranked by margin, turn, and stockout risk.

---

## 🛠️ Technologies Used

- Microsoft Excel (no macros required)
- Pivot Tables
- INDEX-MATCH
- Conditional Formatting
- Data Validation

---

## 📈 Use Case

This tool drove ~$1.3M in incremental licensed product revenue between Fall 2024 and Spring 2025 by enabling responsive, data-driven replenishment. Its logic was used in weekly chase calls and vendor conversations, supporting 96% sell-through rates on chased styles.

---

## 🚀 How to Use

1. Paste current sales + inventory export into **Replen Template Dump**
2. Update **Buyplan Dump** if buy gaps are needed
3. Review **Top Styles To Replen** and apply filters by subclass, team, tier, etc.
4. Use outputs to place manual POs or update automated replenishment flows

---

## 📄 License

This tool was developed for internal use and is shared for educational and demonstration purposes only.

---

> *"Built to chase smart, not react late — replenish based on what’s actually selling."*
