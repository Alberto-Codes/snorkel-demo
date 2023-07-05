from snorkel.labeling import PandasLFApplier

from snrkl_label_funcs import lf_amount_based, lf_keyword_based


def create_label_matrix(df, lfs):
    # Create a PandasLFApplier object
    applier = PandasLFApplier(lfs)

    # Apply the labeling functions to the DataFrame
    L_train = applier.apply(df)

    return L_train
