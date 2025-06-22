import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # Race count
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentage with Bachelors degrees
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # Higher and lower education
    higher_education = df[df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])]

    # Percent with >50K
    higher_education_rich = round(
        (higher_education['salary'] == '>50K').sum() / len(higher_education) * 100, 1)
    lower_education_rich = round(
        (lower_education['salary'] == '>50K').sum() / len(lower_education) * 100, 1)

    # Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # Rich percentage among those working min hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['salary'] == '>50K').sum() / len(min_workers) * 100, 1)

    # Country with highest % >50K
    country_percent = df[df['salary'] == '>50K']['native-country'].value_counts() / \
        df['native-country'].value_counts() * 100
    highest_earning_country = country_percent.idxmax()
    highest_earning_country_percentage = round(country_percent.max(), 1)

    # Top occupation in India for >50K
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

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
