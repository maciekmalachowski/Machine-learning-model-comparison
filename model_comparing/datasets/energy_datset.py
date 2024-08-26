import pandas as pd
from sklearn.model_selection import train_test_split

def get_data():
    name = "energy"
    dataset_type = "reg"
    df = pd.read_csv(r"C:/Users/Maciek/W_my_notebooks/energy/energydata_complete.csv")
    # create X columns list and set y column
    x_cols = ["date", "lights", "T1", "RH_1", "T2", "RH_2", "T3", "RH_3", "T4", "RH_4", "T5", "RH_5", "T6", "RH_6", "T7", "RH_7", "T8", "RH_8", "T9", "RH_9", "T_out", "Press_mm_hg", "RH_out", "Windspeed", "Visibility", "Tdewpoint", "rv1", "rv2"]
    y_col = "Appliances"
    # set input matrix
    X = df[x_cols]
    # set target vector
    y = df[y_col]

    # split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.95, shuffle=True, random_state=42)

    return name, X_train, X_test, y_train, y_test, dataset_type
