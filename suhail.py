import csv

print("\n" + "="*70)
print(" "*15 + "🏠 SIMPLE LINEAR REGRESSION - HOUSE PRICE PREDICTION 🏠")
print("="*70)

csv_file_path = "data.csv"

try:
    # CSV file ko manually read karein
    print("\n✓ Reading CSV file...")
    data = []
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    
    print(f"✓ {len(data)} records loaded successfully!")
    
    # Data ko convert karein
    areas = []
    prices = []
    
    print("\n" + "-"*70)
    print("📊 DATASET PREVIEW (First 5 rows):")
    print("-"*70)
    print(f"{'Area':<10} {'Bedrooms':<12} {'Bathrooms':<12} {'Age':<8} {'Price':<15}")
    print("-"*70)
    
    for i, row in enumerate(data):
        area = float(row['Area'])
        price = float(row['Price'])
        
        areas.append(area)
        prices.append(price)
        
        if i < 5:  # First 5 rows display karein
            print(f"{area:<10.0f} {row['Bedrooms']:<12} {row['Bathrooms']:<12} {row['Age']:<8} ${price:>12,.0f}")
    
    # ===== SIMPLE LINEAR REGRESSION (Area vs Price) =====
    print("\n" + "-"*70)
    print("🔧 REGRESSION ANALYSIS (Area as predictor):")
    print("-"*70)
    
    n = len(areas)
    sum_x = sum(areas)
    sum_y = sum(prices)
    sum_xy = sum(a * p for a, p in zip(areas, prices))
    sum_x2 = sum(a ** 2 for a in areas)
    
    # Linear regression formula: y = mx + b
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - m * sum_x) / n
    
    print(f"Linear Regression Equation: Price = {m:.2f} × Area + {b:,.2f}")
    print(f"\nSlope (m):      ${m:,.2f} per sq.ft")
    print(f"Intercept (b):  ${b:,.2f}")
    
    # Calculate R² (Coefficient of Determination)
    y_mean = sum_y / n
    ss_tot = sum((p - y_mean) ** 2 for p in prices)
    ss_res = sum((p - (m * a + b)) ** 2 for a, p in zip(areas, prices))
    r_squared = 1 - (ss_res / ss_tot)
    
    # RMSE
    rmse = (ss_res / n) ** 0.5
    
    print(f"\nModel Performance:")
    print(f"  • R² Score:  {r_squared:.4f} (Model fitness)")
    print(f"  • RMSE:      ${rmse:,.2f}")
    
    # ===== PREDICTIONS =====
    print("\n" + "-"*70)
    print("🔮 PRICE PREDICTIONS FOR DIFFERENT AREAS:")
    print("-"*70)
    
    test_areas = [1000, 1500, 2000, 2500, 3000]
    print(f"{'Area (sq.ft)':<18} {'Predicted Price':<20}")
    print("-"*40)
    
    for area in test_areas:
        predicted_price = m * area + b
        print(f"{area:<18} ${predicted_price:>18,.2f}")
    
    # Actual vs Predicted comparison
    print("\n" + "-"*70)
    print("✓ ACTUAL VS PREDICTED (First 8 records):")
    print("-"*70)
    print(f"{'Actual Price':<20} {'Predicted Price':<20} {'Difference':<15}")
    print("-"*55)
    
    for i in range(min(8, len(areas))):
        actual = prices[i]
        predicted = m * areas[i] + b
        diff = actual - predicted
        print(f"${actual:>18,.0f} ${predicted:>18,.0f} ${diff:>13,.0f}")
    
    print("\n" + "="*70)
    print("✅ REGRESSION ANALYSIS COMPLETE!")
    print("="*70 + "\n")

except FileNotFoundError:
    print(f"\n❌ Error: '{csv_file_path}' file nahi mila!")
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()


