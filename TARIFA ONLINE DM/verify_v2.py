import json

with open('product_data_v2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for type in ['flexibles', 'rigidos']:
    print(f'=== {type.upper()} ===')
    for cat in data[type][:3]:
        print(f"Category: {cat['name']}")
        for sub in cat.get('subcategories', [])[:3]:
            print(f"  Subcategory: {sub['name']}")
            for p in sub.get('products', [])[:2]:
                print(f"    Product: {p}")
