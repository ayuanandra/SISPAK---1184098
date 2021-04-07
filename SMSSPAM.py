import pandas as pd

df = pd.read_table('SMSSpamCollection',
                   sep='\t', 
                   header=None, 
                   names=['label', 'sms_message'])

print("Dataframe head before modifications\n", df.head(), "\n")

df['label'] = df.label.map({'ham': 0, 'spam': 1})
print("The size of the array: ", df.shape)
print("Dataframe head after modifications\n", df.head(), "\n")

# 1. Convert all strings to their lower case form
documents = ["Hello, how are you!",
			"Win money win from home.",
			"Call me now.",
			"Hello, Call hello you tomorrow?"]

lower_case_documents = []
for i in documents:
	lower_case_documents.append(i.lower())
# print("Printing lower case documents: \n", lower_case_documents)

# 2. Removing all punctuations
sans_punctation_documents = []
import string

for i in lower_case_documents:
	sans_punctation_documents.append(i.translate(str.maketrans('', '', string.punctuation)))

# print("Printing sans punctation documents: \n", sans_punctation_documents)

# 3. Tokenization
preprocessed_documents = []
for i in sans_punctation_documents:
	preprocessed_documents.append(i.split(' '))

# print("Printing preprocessed documents: \n", preprocessed_documents)

# 4. Count frequencies

frequency_list = []
import pprint
from collections import Counter
for i in preprocessed_documents:
	frequency_counts = Counter(i)
	frequency_list.append(frequency_counts)
#pprint.pprint(frequency_list)

'''
	Implementing Bag of Words in scikit-learn
'''
from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer()
count_vector.fit(documents)
print(count_vector.get_feature_names())



doc_array = count_vector.transform(documents).toarray()
print("Doc array: \n", doc_array)



frequency_matrix = pd.DataFrame(doc_array, columns = count_vector.get_feature_names())

print("\nFrequency matrix: \n", frequency_matrix)


# Split into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df['sms_message'], df['label'], random_state=1)

print('Number of rows in the total set: {}'.format(df.shape[0]))
print('Number of rows in the training set: {}'.format(X_train.shape[0]))
print('Number of rows in the test set: {}'.format(X_test.shape[0]))
print(df.head())

df['label'] = df.label.map({'ham':0, 'spam':1})
print(df.shape)
print(df.head());
