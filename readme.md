# Pet Food Label Decoder

Simple tool to categorize pet food ingredients into understandable groups.

## What It Does

Categorizes ingredients as: **Proteins**, **Fillers**, **Additives**, or **Unclear**

## Usage

```bash
python main.py
```

Input: `chicken meal, corn, wheat, artificial flavor`

Output:
```
--- Pet Food Decoder ---

Protein Sources:
  - chicken meal
These provide amino acids for muscles and tissues.

Fillers:
  - corn
  - wheat
These are carbs for energy and binding the food together.

Additives:
  - artificial flavor
These are added for flavor, color, or preservation.

Note: Common in adult dog food.
Disclaimer: Educational purposes only, not veterinary advice.
```

---

## Workflow

![Workflow](flow.svg)

1. **Input Processing** - Clean text, lowercase, split by commas
2. **Classification** - Match against predefined lists (Protein → Filler → Additive → Unclear)
3. **Output** - Display results with mock LLM explanations

---

## Classification Logic

**Predefined Lists:**
- Proteins (11): chicken, beef, lamb, fish, turkey, salmon, duck, pork, chicken meal, beef meal, fish meal
- Fillers (9): corn, wheat, soy, rice, barley, oats, rice flour, corn meal, wheat flour
- Additives (7): artificial flavor, artificial color, preservative, bha, bht, food coloring

**Mock LLM:** Pre-written explanations for each category ensure safe, controlled outputs.

---

## Limitations

1. Only ~27 ingredients recognized
2. Exact matching only (no variations)
3. No nutritional quality analysis
4. No medical advice capability
5. Requires comma-separated format
6. Static knowledge (manual updates)
7. No species/age/size context

---

## Safety Features

 No health claims  
 Educational disclaimer  
 Transparent logic  
 Controlled outputs

---

**Requirements:** Python 3.x (no external libraries)

**Files:** `main.py`, `flow.svg`, `README.md`