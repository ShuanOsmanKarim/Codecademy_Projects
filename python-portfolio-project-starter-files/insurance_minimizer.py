# This file analyses each person's profile and gives a recomendaiton as to how to cut insurance costs.

import csv

test_data = {'age': '61', 'sex': 'female', 'bmi': '29.07', 'children': '0', 'smoker': 'yes', 'region': 'northwest', 'charges': '29141.3603'}

def estimate_insurance_cost(age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500 - 8364.539700000001
    return estimated_cost

def make_suggestion(dic):
    # charges
    charges = float(dic['charges'])
    # charge = float('inf')
    # new_charge = float('inf')
    possible_bmi = [i/100 for i in range(1850, 3000)]
    # age is an immutable characteristic
    age = int(dic['age'])
    # sex is an immutable characteristic
    sex = 0
    if dic['sex'] == 'male':
        sex = 1
    # bmi
    bmi = float(dic['bmi'])
    possible_bmi = [i/100 for i in range(1850, 3000)]
    bmi_goal = float('inf')
    bmi_charges_update = charges
    # children can increase
    children = int(dic['children'])
    possible_children = [i for i in range(children, 10)]
    child_goal = children
    child_charges_update = charges
    # smoker
    smoker = 0
    if dic['smoker'] == 'yes':
        smoker = 1
    if smoker == 1:
        smoker_charges_update = estimate_insurance_cost(age, sex, bmi, children, 0)
    else:
        smoker_charges_update = charges
    # region does not contribute
    region = dic['region']
    # bmi reduction calc
    for b in possible_bmi:
        c = estimate_insurance_cost(age, sex, b, children, smoker)
        # print(charges)
        if c < bmi_charges_update:
            bmi_goal = b
            bmi_charges_update = c
    for b in possible_children:
        c = estimate_insurance_cost(age, sex, bmi, b, smoker)
        if c < child_charges_update:
            child_goal = b
            child_charges_update = c
    best_charges = estimate_insurance_cost(age, sex, bmi_goal, child_goal, 0)
    # print statments
    if bmi_charges_update != charges:
        print("You can save {} by changing you bmi from {} to {}.".format((charges-bmi_charges_update), bmi, bmi_goal))
    if child_charges_update != charges:
        print("You can save {} by having {} more children.".format((charges-child_charges_update), (child_goal-children)))
    if smoker_charges_update != charges:
        print("You can save {} quitting smoking.".format((charges-smoker_charges_update)))
    print("the best thing for you to do is have a bmi of {}, {} more children, and not be a smoker. Then you would save {} on you insurance with a payment of only {}.".format(bmi_goal, child_goal, (charges-best_charges), best_charges))




with open('insurance.csv') as insurance_file:
        insurance_records = list(csv.DictReader(insurance_file))

# print(29141.3603 - estimate_insurance_cost(61 ,0 , 29.07, 0, 1))


for r in insurance_records:
    make_suggestion(r)





