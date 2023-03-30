import sys
import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('./data.csv')
    fns = [one, two, three, four, five, six, seven]

    idx = validate_params()
    # execute function
    fns[idx - 1](df)


def validate_params() -> int:
    if len(sys.argv) != 2:
        print('Usage: main.py (task number)')
        exit(1)
    
    idx = int(sys.argv[1])
    assert idx in list(range(1, 8)), 'Task number must be in the closed interval [1, 7]'

    return idx


def one(
    df: pd.DataFrame
) -> None:
    # where all professions are N/A
    no_profession = df[df['Profession'].isna()]
    new_df = pd.DataFrame({
        "Gender": no_profession['Gender'],
        "Age": no_profession["Age"],
        "Spending Score": no_profession["Spending Score (1-100)"]
    }).reset_index()  # use the default index

    print(new_df)
    print(f'\nNumber of unemployed people: {len(new_df)}')


def two(
    df: pd.DataFrame
) -> None:
    new_df = pd.DataFrame({
        "Age": df["Age"],
        "Spending Score": df["Spending Score (1-100)"]
    }).reset_index()
    new_df.plot.scatter('Age', 'Spending Score')
    plt.show()


def three(
    df: pd.DataFrame
) -> None:
    new_df = df.reset_index(drop=True).groupby(['Profession', 'Gender'])
    counts = new_df.size().unstack()
    counts.plot.bar()
    plt.show()


def four(
    df: pd.DataFrame
) -> None:
    new_df = df.fillna('****')
    print(new_df)


def five(
    df: pd.DataFrame
) -> None:
    gender = df['Gender'].value_counts()
    gender.plot.pie()
    plt.show()


def six(
    df: pd.DataFrame
) -> None:
    df['Annual Income ($)'].apply(
        lambda income: 'greater' if income >= 50_000 else 'less'
    ).value_counts().plot.pie()
    plt.show()



def seven(
    df: pd.DataFrame
) -> None:
    new_df = df[df['Profession'].isin(['Artist', 'Engineer'])]
    grouped = new_df.groupby(['Profession'])['Spending Score (1-100)'].mean()
    grouped.plot.bar()
    plt.show()


if __name__ == '__main__':
    main()
