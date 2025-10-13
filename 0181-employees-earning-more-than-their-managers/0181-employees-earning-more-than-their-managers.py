import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(employee)
    df.rename(columns={'name': 'Employee'}, inplace=True)
    result = pd.merge(df, df, left_on='managerId', right_on='id', suffixes=('', '_manager'))
    result = result[result['salary'] > result['salary_manager']]
    result = result[['Employee']]
    return result
