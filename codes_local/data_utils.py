def gen_rand_split(df_sel, val_p, test_p, SEED_val, SEED_test):
    '''generates random split given the percentages for the validation and test groups'''

    from sklearn.model_selection import train_test_split

    #df_raw = pd.read_csv('150k.csv')

    X = df_sel.drop('z', axis=1)
    y = df_sel['z']

    # 3.1. Train-Test Split (e.g., 85% Train/Val, 15% Test)
    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_p, random_state=SEED_test
    )

    # 3.2. Train-Validation Split
    X_train, X_val, y_train, y_val = train_test_split(
        #X_train_val, y_train_val, test_size=val_p/(1-test_p), random_state=SEED_val
        X_train_val, y_train_val, test_size=val_p/(1-test_p), random_state=SEED_val   
    )

    return X_train, X_val, X_test, y_train, y_val, y_test


'''
def select_variables(df_raw, selected_vars):
    #Seleccionar variables de entrada a la red (i.e., features)

    df_selected = df_raw[selected_vars]

    return df_selected
'''    