import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('./data.csv')
    one(df)


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
    raise NotImplementedError()


def three(
    df: pd.DataFrame
) -> None:
    raise NotImplementedError()


def four(
    df: pd.DataFrame
) -> None:
    raise NotImplementedError()


def five(
    df: pd.DataFrame
) -> None:
    raise NotImplementedError()


def six(
    df: pd.DataFrame
) -> None:
    raise NotImplementedError()


def seven(
    df: pd.DataFrame
) -> None:

    raise NotImplementedError()


if __name__ == '__main__':
    main()
