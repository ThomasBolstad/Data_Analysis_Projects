# Buying Office Buyplan Automation Template

This macro-enabled Excel tool automates seasonal merchandise purchasing for licensed team sports across hundreds of stores and teams. It combines sales forecasting, team performance, and tiered store segmentation to produce a data-driven buy plan optimized for replenishment and allocation.

---

## 📁 Tabs & Functional Overview

- **Buy Sheet Original / Final**: Main working tabs where raw product-level buy data is stored and reviewed. Final version reflects the refined purchases used for execution.
- **Allocation Tab Final / Original**: Breaks down buy quantities by store tier and team affiliation using matrix logic.
- **Team Sales Rank**: Ranks teams based on recent sales performance to dynamically influence buy volume.
- **Store-Tier Data**: Provides metadata on store segmentation by tier (A/B/C), region, and format.
- **Test Matrix**: A staging tab to test new team/store allocation combinations before applying them to the buy.
- **Pivot / Pivot Data**: Summary visualizations to review buy totals by vendor, category, team, and channel.
- **UPCS&KLINK / KLINK**: SKU lookups and style-color metadata used for mapping products.
- **dropdown.dates**: Controls the date pickers and versioning logic used in drop-down menus.
- **Order Maintenance**: Allows for last-minute adjustments and edits to orders before submission.

---

## 🔹 Key Features

- **Automated Allocation Logic**: Dynamically distributes product buys by team, store tier, and sales velocity.
- **Sales Rank Integration**: Prioritizes product flow to top-selling teams across different store types.
- **Pivot-Driven Validation**: Validates buys by category, vendor, and delivery window with summary views.
- **SKU Metadata & UPC Matching**: Ensures clean and accurate product mapping for downstream ordering systems.
- **Customizable for Season & Category**: Built to be easily duplicated and edited for each new season or licensed category (e.g., MLB, NFL, NCAA).

---

## 🛠️ Technologies Used

- Microsoft Excel (macro-enabled `.xlsm`)
- VBA Macros
- INDEX-MATCH, VLOOKUP, CEILING/FLOOR logic
- Pivot Tables
- Conditional Formatting
- Data Validation and Drop-Downs

---

## 📈 Sample Use Case

This file was used to plan $150M+ in licensed product buys across 4,500+ team-store combinations, saving hours of manual entry and producing accurate, tiered purchase volumes tailored to store and team-level performance. The logic contributed to a $1M+ revenue lift during peak seasons.

---

## 🚀 How to Use

1. Duplicate this file for each season or league.
2. Update raw sales data in **Team Sales Rank** and **Store-Tier Data**.
3. Populate **Buy Sheet Original** with product plans.
4. Review and finalize buys in **Buy Sheet Final**.
5. Review allocations in **Allocation Tab Final**.
6. Use **Order Maintenance** for last-minute edits before submission.

---

## 📄 License

This tool is proprietary and was originally developed for internal use at Kohl’s. Public reuse should be limited to showcasing analytical or Excel-based skills unless otherwise approved.

---

> *“Built to turn raw sales chaos into clear, confident buying strategies — team by team, store by store.”*
