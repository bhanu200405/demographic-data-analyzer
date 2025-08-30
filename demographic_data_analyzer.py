import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read the data
    df = pd.read_csv('adult.data.csv')

    # 1. How many of each race are represented in this dataset? 
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. What percentage of people with advanced education make >50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )
    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 5. What is the minimum number of hours a person works per week?
    min_work_hours = int(df['hours-per-week'].min())

    # 6. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K']
    rich_percentage = round((len(rich_min_workers) / len(num_min_workers)) * 100, 1)

    # 7. What country has the highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country_percentage = round(
        (rich_country_counts / country_counts * 100).max(), 1
    )
    highest_earning_country = (rich_country_counts / country_counts * 100).idxmax()

    # 8. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    if print_data:
        print("Race count:\n", race_count, "\n")
        print("Average age of men:", average_age_men, "\n")
        print("Percentage with Bachelor's degrees:", percentage_bachelors, "\n")
        print("Percentage with higher education earning >50K:", higher_education_rich, "\n")
        print("Percentage without higher education earning >50K:", lower_education_rich, "\n")
        print("Minimum work hours per week:", min_work_hours, "\n")
        print("Percentage of rich among those who work minimum hours:", rich_percentage, "\n")
        print("Country with highest % earning >50K:", highest_earning_country, "\n")
        print("Highest percentage:", highest_earning_country_percentage, "\n")
        print("Top occupation in India for >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
