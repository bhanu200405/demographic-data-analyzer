import pandas as pd

# Load the dataset directly from the UCI repository
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
df = pd.read_csv(url, header=None, names=[
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
], na_values=" ?", skipinitialspace=True)

# 1. Count of people by race
race_count = df['race'].value_counts()

# 2. Average age of men
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

# 3. Percentage with Bachelor's degree
percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

# 4. Percentage with advanced education earning >50K
advanced_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
higher_education_rich = round((df[advanced_edu]['salary'] == '>50K').mean() * 100, 1)

# 5. Percentage without advanced education earning >50K
lower_edu = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
lower_education_rich = round((df[lower_edu]['salary'] == '>50K').mean() * 100, 1)

# 6. Minimum work hours per week
min_work_hours = df['hours-per-week'].min()

# 7. Percentage of min-hour workers earning >50K
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

# 8. Country with highest % earning >50K
country_counts = df.groupby('native-country')
rich_country_percentage = (country_counts['salary']
                           .apply(lambda x: (x == '>50K').mean() * 100))
highest_earning_country = rich_country_percentage.idxmax()
highest_earning_country_percentage = round(rich_country_percentage.max(), 1)

# 9. Most popular occupation for >50K in India
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]
