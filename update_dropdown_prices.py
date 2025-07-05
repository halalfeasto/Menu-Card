#!/usr/bin/env python3
import re

# Read the HTML file
with open('/home/rahman/resturant-project/Menu/Resturant-Pamplet-Project/index.html', 'r') as file:
    content = file.read()

# Find all dropdown items and their corresponding combo prices
# Pattern to match dropdown headers with regular prices
dropdown_pattern = r'<span class="item-price">\$([0-9.]+)</span>'

# Find all regular prices in dropdown headers
regular_prices = re.findall(dropdown_pattern, content)

# Find all combo prices in dropdown content
combo_pattern = r'<span class="text-gray-500">Combo: \$([0-9.]+)</span>'
combo_prices = re.findall(combo_pattern, content)

print(f"Found {len(regular_prices)} regular prices and {len(combo_prices)} combo prices")

# Update the dropdown headers to include both prices
# We need to match each regular price with its corresponding combo price
updates = []

# Create a list of price pairs (regular, combo)
if len(regular_prices) >= len(combo_prices):
    price_pairs = []
    combo_idx = 0
    
    for i, reg_price in enumerate(regular_prices):
        if reg_price == "9.54" and combo_idx < len(combo_prices):
            continue  # Skip the already updated Cheeseburger
        
        if combo_idx < len(combo_prices):
            combo_price = combo_prices[combo_idx]
            price_pairs.append((reg_price, combo_price))
            combo_idx += 1

    # Update the content with new price format
    for reg_price, combo_price in price_pairs:
        old_pattern = f'<span class="item-price">${reg_price}</span>'
        new_pattern = f'<span class="item-price">Only ${reg_price} | Combo ${combo_price}</span>'
        content = content.replace(old_pattern, new_pattern, 1)

# Write back to file
with open('/home/rahman/resturant-project/Menu/Resturant-Pamplet-Project/index.html', 'w') as file:
    file.write(content)

print("Dropdown prices updated successfully!")