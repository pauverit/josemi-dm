import json

try:
    with open('product_data_v5.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print('=== FLEXIBLES CATEGORIES ===')
    for cat in data['flexibles']:
        print(f"Cat: {cat['name']} ({len(cat['subcategories'])} subcats)")
        for sc in cat['subcategories'][:2]:
            print(f"  - {sc['name']} ({len(sc['products'])} prods)")

    print('\n=== RIGIDOS CATEGORIES ===')
    for cat in data['rigidos'][:5]:
        print(f"Cat: {cat['name']} ({len(cat['subcategories'])} subcats)")
except Exception as e:
    print(f'Error: {e}')
