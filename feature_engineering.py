import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class ChurnFeatureEngineer(BaseEstimator, TransformerMixin):

    def __init__(self):
        self.service_columns = [
            "PhoneService",
            "MultipleLines",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies"
        ]

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        # Average monthly spend
        X["AverageMonthlySpend"] = np.where(
            X["tenure"] > 0,
            X["TotalCharges"] / X["tenure"],
            X["MonthlyCharges"]
        )

        # Total number of active services
        X["TotalServices"] = (
            X[self.service_columns]
            .eq("Yes")
            .sum(axis=1)
        )

        # Customer tenure group
        X["TenureGroup"] = X["tenure"].apply(
            self.create_tenure_group
        )

        return X

    @staticmethod
    def create_tenure_group(tenure):

        if tenure <= 12:
            return "New"

        elif tenure <= 24:
            return "Developing"

        elif tenure <= 48:
            return "Established"

        else:
            return "Loyal"
