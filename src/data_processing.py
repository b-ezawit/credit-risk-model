import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
from sklearn.impute import SimpleImputer


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # datetime features
    df["TransactionStartTime"] = pd.to_datetime(df["TransactionStartTime"])

    df["transaction_hour"] = df["TransactionStartTime"].dt.hour
    df["transaction_day"] = df["TransactionStartTime"].dt.day
    df["transaction_month"] = df["TransactionStartTime"].dt.month
    df["transaction_year"] = df["TransactionStartTime"].dt.year

    # aggregation features
    agg = df.groupby("CustomerId").agg({
        "Amount": ["sum", "mean", "std"],
        "TransactionId": "count"
    })

    agg.columns = [
        "total_amount",
        "avg_amount",
        "std_amount",
        "transaction_count"
    ]

    agg = agg.reset_index()

    # fix missing std values
    agg = agg.fillna(0)

    df = df.merge(agg, on="CustomerId", how="left")

    return df


# feature columns
numeric_features = [
    "Amount",
    "Value",
    "total_amount",
    "avg_amount",
    "std_amount",
    "transaction_count",
    "transaction_hour",
    "transaction_day",
    "transaction_month",
    "transaction_year"
]

categorical_features = [
    "CurrencyCode",
    "CountryCode",
    "ProviderId",
    "ProductId",
    "ProductCategory",
    "ChannelId",
    "PricingStrategy"
]


# numeric pipeline
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# categorical pipeline
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])


preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

def build_pipeline():
    numeric_features = [
        "Amount",
        "Value",
        "total_amount",
        "avg_amount",
        "std_amount",
        "transaction_count",
        "transaction_hour",
        "transaction_day",
        "transaction_month",
        "transaction_year"
    ]

    categorical_features = [
        "CurrencyCode",
        "CountryCode",
        "ProviderId",
        "ProductId",
        "ProductCategory",
        "ChannelId",
        "PricingStrategy"
    ]

    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )

    return Pipeline(steps=[
        ("preprocessor", preprocessor)
    ])