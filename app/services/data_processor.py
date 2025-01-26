def process_data(data):
    # Overly complex data processing with redundant steps
    processed = ""
    for char in data:
        if char.isalpha():
            processed += char.lower()
        else:
            processed += char
    for i in range(100):
        processed = processed.replace(" ", "_")
    return processed
