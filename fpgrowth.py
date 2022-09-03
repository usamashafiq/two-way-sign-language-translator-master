# Import all basic libray
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
import time
from mlxtend.frequent_patterns import fpgrowth
dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]
# Task1 : Compute Frequent Item Set using  mlxtend.frequent_patterns
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
start_time = time.time()
frequent = fpgrowth(df, min_support=0.6, use_colnames=True)
print(frequent)

print('Time to find frequent itemset')
print("--- %s seconds ---" % (time.time() - start_time))
# Task 2&3: Find closed/max frequent itemset using frequent itemset found in task1
su = frequent.support.unique()  # all unique support count
# Dictionay storing itemset with same support count key
fredic = {}
for i in range(len(su)):
    inset = list(frequent.loc[frequent.support == su[i]]['itemsets'])
    fredic[su[i]] = inset
# Dictionay storing itemset with  support count <= key
fredic2 = {}
for i in range(len(su)):
    inset2 = list(frequent.loc[frequent.support <= su[i]]['itemsets'])
    fredic2[su[i]] = inset2
# Find Closed frequent itemset
start_time = time.time()
cl = []
for index, row in frequent.iterrows():
    isclose = True
    cli = row['itemsets']
    cls = row['support']
    checkset = fredic[cls]
    for i in checkset:
        if (cli != i):
            if (frozenset.issubset(cli, i)):
                isclose = False
                break

    if (isclose):
        cl.append(row['itemsets'])
print('Time to find Close frequent itemset')
print("--- %s seconds ---" % (time.time() - start_time))

# Find Max frequent itemset
start_time = time.time()
ml = []
for index, row in frequent.iterrows():
    isclose = True
    cli = row['itemsets']
    cls = row['support']
    checkset = fredic2[cls]
    for i in checkset:
        if (cli != i):
            if (frozenset.issubset(cli, i)):
                isclose = False
                break

    if (isclose):
        ml.append(row['itemsets'])
print('Time to find Max frequent itemset')
print("--- %s seconds ---" % (time.time() - start_time))
