import pandas as pd

def calculate_demographic_data(print_data=False):
    # Column names for the dataset
    column_names = [
        "age", "workclass", "fnlwgt", "education", "education-num", 
        "marital-status", "occupation", "relationship", "race", 
        "sex", "capital-gain", "capital-loss", "hours-per-week", 
        "native-country", "salary"
    ]
    
    # Read the CSV
    df = pd.read_csv('adult.data.csv', names=column_names, skipinitialspace=True)
    
    # 1. How many of each race?
    race_count = df['race'].value_counts()
    
    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # 3. Percentage with Bachelor's degrees
    total_people = df.shape[0]
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)
    
    # 4. Percentage with advanced education earning >50K
    higher_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu_df = df[df['education'].isin(higher_education)]
    higher_edu_rich = higher_edu_df[higher_edu_df['salary'] == '>50K']
    percentage_higher_education_rich = round((higher_edu_rich.shape[0] / higher_edu_df.shape[0]) * 100, 1)
    
    # 5. Percentage without advanced education earning >50K
    lower_edu_df = df[~df['education'].isin(higher_education)]
    lower_edu_rich = lower_edu_df[lower_edu_df['salary'] == '>50K']
    percentage_lower_education_rich = round((lower_edu_rich.shape[0] / lower_edu_df.shape[0]) * 100, 1)
    
    # 6. Minimum hours per week
    min_work_hours = int(df['hours-per-week'].min())
    
    # 7. Percentage of rich among those who work minimum hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage_min_workers = round((rich_min_workers.shape[0] / min_workers.shape[0]) * 100, 1)
    
    # 8. Country with highest % earning >50K
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_rich_percentage = (rich_country_counts / country_counts * 100).fillna(0)
    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)
    
    # 9. Most popular occupation for those who earn >50K in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].mode()[0] if not india_rich.empty else None
    
    if print_data:
        print("Race count:\n", race_count)
        print("\nAverage age of men:", average_age_men)
        print("\nPercentage with Bachelor's degrees:", percentage_bachelors)
        print("\nPercentage with higher education earning >50K:", percentage_higher_education_rich)
        print("\nPercentage without higher education earning >50K:", percentage_lower_education_rich)
        print("\nMinimum work hours per week:", min_work_hours)
        print("\nPercentage of rich among those who work minimum hours:", rich_percentage_min_workers)
        print("\nCountry with highest % earning >50K:", highest_earning_country)
        print("Highest percentage:", highest_earning_country_percentage)
        print("\nTop occupation in India for >50K:", top_IN_occupation)
    
    # Return all values
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_higher_education_rich': percentage_higher_education_rich,
        'percentage_lower_education_rich': percentage_lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
