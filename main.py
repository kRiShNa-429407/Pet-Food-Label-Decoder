# Pet Food Label Decoder
# Helps understand pet food ingredients

# Lists of ingredients we know about(predefined)
proteins = ["chicken", "beef", "lamb", "fish", "turkey", "salmon", "chicken meal", "beef meal", "fish meal", "duck", "pork"]

fillers = ["corn", "wheat", "soy", "rice", "rice flour", "corn meal", "wheat flour", "barley", "oats"]

additives = ["artificial flavor", "artificial colour", "artificial color", "preservative", "bha", "bht", "food coloring"]


# Main function
def decode_label(text):
    # Clean up the text
    text = text.lower()
    text = text.replace("ingredients:", "")
    
    # Split by comma
    parts = text.split(",")
    
    # Remove spaces
    ingredients = []
    for part in parts:
        part = part.strip()
        if part != "":
            ingredients.append(part)
    
    # Empty lists to store results
    protein_list = []
    filler_list = []
    additive_list = []
    unclear_list = []
    
    # Go through each ingredient
    for ingredient in ingredients:
        # Check what type it is
        found = False
        
        # Is it a protein?
        for p in proteins:
            if ingredient == p:
                protein_list.append(ingredient)
                found = True
                break
        
        if found:
            continue
        
        # Is it a filler?
        for f in fillers:
            if ingredient == f:
                filler_list.append(ingredient)
                found = True
                break
        
        if found:
            continue
        
        # Is it an additive?
        for a in additives:
            if ingredient == a:
                additive_list.append(ingredient)
                found = True
                break
        
        if found:
            continue
        
        # If we get here, it's unclear
        unclear_list.append(ingredient)
    
    # Count how many known ingredients we found
    known_count = len(protein_list) + len(filler_list) + len(additive_list)
    
    # If nothing , just stop
    if known_count == 0 and len(unclear_list) == 0:
        return
    
    # Rrinting results
    print("\n--- Pet Food Decoder ---\n")
    
    # Mock LLM function to generate explanations
    def mock_llm_explanation(category):
        explanations = {
            "protein": "These provide amino acids for muscles and tissues.",
            "filler": "These are carbs for energy and binding the food together.",
            "additive": "These are added for flavor, color, or preservation.",
            "unclear": "Not enough info available about these."
        }
        return explanations[category]
    
    # Print proteins if we found any
    if len(protein_list) > 0:
        print("Protein Sources:")
        for item in protein_list:
            print("  - " + item)
        print(mock_llm_explanation("protein"))
        print()
    
    # Print fillers if we found any
    if len(filler_list) > 0:
        print("Fillers:")
        for item in filler_list:
            print("  - " + item)
        print(mock_llm_explanation("filler"))
        print()
    
    # Print additives if we found any
    if len(additive_list) > 0:
        print("Additives:")
        for item in additive_list:
            print("  - " + item)
        print(mock_llm_explanation("additive"))
        print()
    
    # Print unclear ingredients if we found any
    if len(unclear_list) > 0:
        print("Unclear:")
        for item in unclear_list:
            print("  - " + item)
        print(mock_llm_explanation("unclear"))
        print()
    
    # Only print note and disclaimer if we found known ingredients
    if known_count > 0:
        print("Note: Common in adult dog food.\n")
        print("Disclaimer: Educational purposes only, not veterinary advice.")


# Run the program
user_input = input("Enter ingredients: ")
decode_label(user_input)