
import pandas as pd

data_path = "https://aisgaiap.blob.core.windows.net/aiap-assignments-data/titanic.csv"


def transform(data_path):
    """Ingest data, process it and return it as a feature-engineered dataframe.

    Parameters:
        data_path (string): Path to raw csv file

    Returns:
        titanic_clean: Clean data for model
    """
    titanic_raw = open(data_path)

    # Choose only columns with high feature importance and the label
    impt_columns = ['Pclass', 'Sex', 'Age',
                    'SibSp', 'Parch', 'Fare', 'Survived']
    df_ = titanic_raw[impt_columns]

    # Fill empty columns
    titanic_filled = fill_age(df_)

    # Encode columns
    categoricals = ['Pclass', 'Sex']
    titanic_enc = encode(titanic_filled, categoricals)

    return titanic_enc


def open(data_path):
    df = pd.read_csv(data_path, encoding='ISO-8859-1')
    return df


def fill_age(df):
    """Fill missing values in Age with the medians of Sex & Pclass groups"""
    df['Age'] = df.groupby(['Sex', 'Pclass'])['Age'].apply(
        lambda x: x.fillna(x.median()))
    return df


def encode(df, col):
    df_ohe = pd.get_dummies(df, columns=col, dummy_na=False)
    return df_ohe
