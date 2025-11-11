# --- STEP 1: Import libraries ---
import pandas as pd

# --- STEP 2: Load your CSV ---
file_path = "/Users/anamontanez/Documents/Anana2314.github.io/LAB10"
df = pd.read_csv('/Users/anamontanez/Documents/Anana2314.github.io/LAB10')

# --- STEP 3: Basic overview ---
print("Shape of the dataset:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

# --- STEP 4: Preview first rows ---
df.head()

# --- STEP 5: Info on datatypes and nulls ---
df.info()

# --- STEP 6: Summary statistics ---
df.describe(include='all')

# --- STEP 7: Check missing values ---
df.isna().sum().sort_values(ascending=False)

# --- STEP 8: Check for duplicates ---
df.duplicated().sum()

# --- STEP 9: Get value counts for categorical columns (optional) ---
for col in df.select_dtypes(include='object').columns:
    print(f"\nTop values in '{col}':")
    print(df[col].value_counts().head(5))
