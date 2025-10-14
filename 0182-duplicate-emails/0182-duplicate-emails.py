import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:

    return (person[person.duplicated('email') == True]
                  [['email']].drop_duplicates())