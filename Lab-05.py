import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

data = {
    'Outlook':     ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast',
                     'Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool',
                     'Mild','Cool','Mild','Mild','Mild','Hot','Mild'],
    'Humidity':    ['High','High','High','High','Normal','Normal','Normal',
                     'High','Normal','Normal','Normal','High','Normal','High'],
    'Wind':        ['Weak','Strong','Weak','Weak','Weak','Strong','Strong',
                     'Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
    'PlayTennis':  ['No','No','Yes','Yes','Yes','No','Yes',
                     'No','Yes','Yes','Yes','Yes','Yes','No']
}
df = pd.DataFrame(data)

# Encode categorical columns to numbers (sklearn needs numeric input)
encoders = {}
df_enc = df.copy()
for col in df.columns:
    le = LabelEncoder()
    df_enc[col] = le.fit_transform(df[col])
    encoders[col] = le

X = df_enc.drop('PlayTennis', axis=1)
y = df_enc['PlayTennis']

# criterion='entropy' + no max_depth limit mimics ID3
clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
clf.fit(X, y)

plt.figure(figsize=(14, 8))
plot_tree(clf, feature_names=X.columns, class_names=encoders['PlayTennis'].classes_,
          filled=True, rounded=True, fontsize=10)
plt.savefig('tree.png', dpi=150, bbox_inches='tight')
plt.show()