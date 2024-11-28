import pandas as pd
from collections import Counter
import math
from pprint import pprint

# Entropy calculation function
def entropy(probs):
    return sum(-prob * math.log(prob, 2) for prob in probs if prob > 0)

# Calculate entropy of a list
def entropy_of_list(a_list):
    cnt = Counter(a_list)
    num_instances = len(a_list)
    probs = [x / num_instances for x in cnt.values()]
    return entropy(probs)

# Information gain function
def information_gain(df, split_attribute_name, target_attribute_name):
    df_split = df.groupby(split_attribute_name)
    nobs = len(df.index) * 1.0
    
    df_agg_ent = df_split[target_attribute_name].agg(
        [entropy_of_list, lambda x: len(x) / nobs]
    )
   
    avg_info = sum(df_agg_ent['entropy_of_list'] * df_agg_ent['<lambda_0>'])
    old_entropy = entropy_of_list(df[target_attribute_name])
    return old_entropy - avg_info

# ID3 Decision Tree algorithm
def id3DT(df, target_attribute_name, attribute_names, default_class=None):
    cnt = Counter(df[target_attribute_name])
    if len(cnt) == 1:
        return next(iter(cnt))
    elif df.empty or not attribute_names:
        return default_class
    else:
        default_class = max(cnt, key=cnt.get)
        gainz = [information_gain(df, attr, target_attribute_name) for attr in attribute_names]
        
        index_of_max = gainz.index(max(gainz))
        best_attr = attribute_names[index_of_max]
        tree = {best_attr: {}}
        remaining_attributes = [i for i in attribute_names if i != best_attr]
        for attr_val, data_subset in df.groupby(best_attr):
            subtree = id3DT(data_subset, target_attribute_name, remaining_attributes, default_class)
            tree[best_attr][attr_val] = subtree
            
        return tree

# Classification function
def classify(instance, tree, default=None):
    attribute = next(iter(tree)) 
    if instance[attribute] in tree[attribute]:
        result = tree[attribute][instance[attribute]]
        if isinstance(result, dict):
            return classify(instance, result)
        else:
            return result
    else:
        return default

# Simulate the dataset from the image provided earlier
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Define attribute names and target column name
attribute_names = list(df.columns)
attribute_names.remove('PlayTennis')

# Build the decision tree
tree = id3DT(df, 'PlayTennis', attribute_names)
print("The Resultant Decision Tree is:")
pprint(tree)

# New data to classify
new_data = {
    'Outlook': ['Rain', 'Sunny'],
    'Temperature': ['Mild', 'Hot'],
    'Humidity': ['Normal', 'High'],
    'Wind': ['Weak', 'Strong']
}

# Convert new data into DataFrame
df2 = pd.DataFrame(new_data)

# Apply the classifier to the new instances
df2['Predicted'] = df2.apply(classify, axis=1, args=(tree, 'No'))

# Display the classified results
print(df2[['Outlook', 'Temperature', 'Humidity', 'Wind', 'Predicted']])
