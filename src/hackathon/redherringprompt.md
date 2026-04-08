# CONTEXT
I am generating a "Stress-Test" dataset for a DSPy prompt optimization hackathon. The goal is to defeat simple Zero-Shot classifiers by providing clinical narratives where the primary diagnosis is buried under secondary symptoms and "red herring" data.

# OBJECTIVE
Generate {count} highly complex, non-duplicate clinical vignettes for the category: {category}.

# STYLE & TONE
Write as an Overworked Triage Resident. Use dense, shorthand medical jargon (e.g., "s/p," "r/o," "h/o," "c/w"). The notes should feel disjointed, including irrelevant social history (e.g., "patient recently traveled," "stress at work") to act as "semantic noise".

# DIFFICULTY REQUIREMENTS (THE "HARD" GATE)
1. **THE RED HERRING (50% of cases):** Start the note with 2-3 sentences describing symptoms that point strongly to a DIFFERENT category (e.g., start a Diabetes case with chest pain and sweating). 
2. **THE LATENT SIGNAL:** The evidence for {category} must only appear in the final sentence, often as a subtle lab value or a specific physical exam finding (e.g., "HgbA1c: 7.2" or "reduced FEV1/FVC").
3. **COMORBIDITIES:** Give every patient at least two other chronic conditions that are NOT in the {category} group to confuse the labeler.
4. **NO TRIGGER WORDS:** Forbidden to use the category name (e.g., if {category} is Diabetes, do not use the word "Sugar" or "Insulin").

# RESPONSE STRUCTURE
Output exactly {count} rows in JSON format.

{{
  "patient_notes": "A dense, noisy narrative including the Red Herring and the Latent Signal.",
  "reasoning": "A deep clinical derivation explaining why the Latent Signal overrides the Red Herring.",
  "label": "{category}"
}}