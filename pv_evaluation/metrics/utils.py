import pandas as pd
import editdistance



def validate_membership(membership_vect):
    """Validate membership vector
    
    Membership vector should be a pandas Series with no NA values and no duplicated index values.
    """
    assert isinstance(membership_vect, pd.Series), "Membership vector should be a pandas Series."
    assert membership_vect.hasnans == False, "Membership vector should not contain NA values."
    assert membership_vect.index.hasnans == False, "Membership vetor index should not contain NA values."
    assert (
        membership_vect.index.has_duplicates == False
    ), "Membership vector index (mention ids) should not contain duplicate values."
