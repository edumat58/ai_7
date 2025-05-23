def model_summary():
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LinearRegression

    # Sample data
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])

    model = LinearRegression()
    model.fit(X, y)

    df = pd.DataFrame({
        "X": X.flatten(),
        "y": y,
        "prediction": model.predict(X)
    })

    return df

if __name__ == "__main__":
    print(model_summary())
