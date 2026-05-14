#  Referral-sense-ai

### *Predictive Physician Targeting for Rare Disease Diagnostics*

**Referral-sense-ai** uses NPI-level claims patterns to identify "Hidden Specialists"—physicians who are likely managing undiagnosed or mismanaged rare disease patients but haven't yet referred them to a specialized Treatment Center.


##  The Strategic Problem: The Diagnostic Odyssey

As shown in the initial project scope (**{12755DFA-EA0D-4610-A00A-A019382796F4}.png**), rare disease patients often wait **5-7 years** to receive an accurate diagnosis. This delay is a massive barrier to therapy adoption.

This tool shifts the commercial strategy from **Reactive** (waiting for referrals) to **Predictive** (finding doctors before they even know they have a rare patient).


##  Core Engine Features

### 1. Proxy Signal Detection

The engine looks beyond primary diagnosis codes using feature engineering to identify:

* **Symptom-Management Clusters:** Chronic usage of low-efficacy treatments suggesting a mismanaged condition.
* **Diagnostic Lab Patterns:** High frequencies of metabolic or genetic screening orders without a definitive outcome.
* **Specialty Proximity:** Identifying "High-Suspect" NPIs in non-obvious specialties (e.g., Rheumatology for Mitochondrial disorders).

### 2. Geographic Access & Proximity Analysis

Finding a patient is only half the battle. Our engine calculates the **Travel Burden** to the nearest Center of Excellence (CoE):

* **Haversine Distance Mapping:** Real-time calculation of physician-to-CoE mileage.
* **Access Desert Identification:** Highlighting high-potential physicians in areas where travel support is a mandatory clinical requirement.


##  Business & Field Impact

* **MSL Efficiency:** Field teams spend 80% less time on "cold" calls and focus on high-propensity NPIs.
* **Site Optimization:** Informs Clinical Operations where to open new treatment sites based on identified patient clusters.
* **Earlier Intervention:** Reduces the "Diagnostic Odyssey" by identifying candidate patients significantly earlier in their journey.

---

##  Installation & Usage

```bash
# Clone the repository
git clone https://github.com/your-username/referral-sense-ai.git
cd referral-sense-ai

# Install dependencies
pip install -r requirements.txt

# Run the targeting engine
python main.py

```

---

## Part of the Life Sciences Executive Suite

This repository is a core pillar of a comprehensive Biotech Commercial Stack:

1. **[Net-Guard-GTN-Optimizer](https://www.google.com/search?q=link):** Revenue integrity and rebate optimization.
2. **Referral-Sense-AI:** (This Repo) Physician targeting and referral mapping.
3. **[Patient-Voice-NLP](https://www.google.com/search?q=link):** Patient unmet need and sentiment extraction.


`![Access Map](./docs/access_map.png)`

