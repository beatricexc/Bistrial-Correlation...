# get data
data = pd.read_csv('D:\quiz-Alg2U0Quiz-standard20180510.csv')

# get continuous and dichotomous data
grades = data['Percent Correct']
question_1 = data['Q1']

# pbc of first question
pbc = pointbiserialr(question_1, grades)
print(pbc)

def pbc_scratch(binary_data, continuous_data, data):
    """
    Function that computes the point biserial correlation of two pandas data frame columns
    :param binary_data: name of dichotomous data column
    :param continuous_data: name of dichotomous data column
    :param data: dataframe where above columns come from
    :returns: Point Biserial Correlation
    """

    bd_unique = data[binary_data].unique()
    
    g0 = data[data[binary_data] == bd_unique[0]][continuous_data]
    g1 = data[data[binary_data] == bd_unique[1]][continuous_data]
    
    s_y = np.std(data[continuous_data])
    n = len(data[binary_data])
    n0 = len(g0)
    n1 = len(g1)
    m0 = g0.mean()
    m1 = g1.mean()
    
    return (m0-m1)*sqrt((n0*n1)/n**2)/s_y
