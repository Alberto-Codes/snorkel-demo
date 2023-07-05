from snorkel.labeling import labeling_function

# Define the label constants
NO_REIMBURSEMENT = 0
REIMBURSEMENT = 1
ABSTAIN = -1


@labeling_function()
def lf_keyword_based(x):
    keywords = ["refund", "reimbursement", "credit"]
    if any(keyword in x.Description.lower() for keyword in keywords):
        return REIMBURSEMENT
    else:
        return ABSTAIN


@labeling_function()
def lf_amount_based(x):
    if x.Amount in [45, 50]:
        return REIMBURSEMENT
    else:
        return ABSTAIN
