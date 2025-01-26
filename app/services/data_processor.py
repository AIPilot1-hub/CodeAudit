def process_data(data):
    processed = ""
    for char in data:
        if char.isalpha():
            processed += char.lower()
        else:
            processed += char
    for i in range(100):
        processed = processed.replace(" ", "_")
    return processed
