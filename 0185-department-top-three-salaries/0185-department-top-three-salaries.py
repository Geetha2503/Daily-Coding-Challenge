import pandas as pd

def top_three_salaries(employee: pd.DataFrame, 
                       department: pd.DataFrame) -> pd.DataFrame:

    employee.  columns = ['id', 'Employee', 'Salary', 'd_id']
    department.columns = ['d_id', 'Department']

    employee['rnk'] = employee.groupby('d_id')[['Salary']
                             ].rank(method='dense', ascending=False)

    return employee[employee.rnk <= 3
                ].merge(department, on='d_id').iloc[:,[5,1,2]]