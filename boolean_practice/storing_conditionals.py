# Calculate risk of heart disease based on age and body mass
# index (BMI).


def heart_risk(age, bmi):

    young = age <= 45
    slim = bmi < 22.0
    if young and slim:
        risk = 'low'
    elif young and not slim:
        risk = 'medium'
    elif not young and slim:
        risk = 'medium'
    elif not young and not slim:
        risk = 'high'
    return risk
heart_risk(45, 15)
heart_risk(42, 20)
heart_risk(18, 23)


#
def risk(age, bmi):

    table = [['medium', 'high'],
             ['low', 'medium']]
    young = age <= 45
    heavy = bmi >= 22.0
    risk = table[young][heavy]
    return risk
risk(23, 32)
