1b. Dependency Graphs are projective if there are no crossing links. In other words, the dependency graphs do not intersect. Non-projective dependencies arise with scrambling of words, extraposition(the TA is coming who is wearing a hat), and topicalization (Cheese, I thought he likes). Thus, non-projective dependency graphs cannot be represented by Context Free Grammar. For any k between points a and b there cannot exist a parent or child of k outside of a and b.

1c. Projective: I went to the beach today.
Non-projective: I pet a cat with whiskers yesterday which was black.

UAS: 0.229038040231
LAS: 0.125473013344

2b.
The unlabeled attachment score of is 0.229038040231 and the labeled attachment score is 0.125473013344. This means that for UAS only 22.9% of the worsd parsed were tagged with the correct heads and only 12.5% of the LAS tokens were tagged with the correct heads and labels. Thus, badfeatures.model is not a good model and requires feature extraction to generate a better model.

Danish
UAS: 0.799001996008 
LAS: 0.710778443114

English
UAS: 0.755555555556 
LAS: 0.725925925926

Korean
UAS: 0.747392815759 
LAS: 0.623020471224

Swedish
UAS: 0.795459071898 
LAS: 0.687910774746


Lemma  Stack[0]
Implementation: takes the index of the first item popped out from teh stack and token is set to the list of features in the tokens dictionary.The program then checks if form is in token and FeatureExtractor._check_informative checks that the lemma is not a None or empty string. Lastly a feature vector is generated containing 'STACK_0_LEMMA_'
Complexity: O(n) because iterates through the words in the sentence and because accessing the lemma through a dictionary is O(1), the total complexity is O(n).
Performance:
UAS: 0.313580246914 
LAS: 0.212345679012
Lemma represents the linguistic property of a word represented by the dictionary form of a word (example: lemma of markets is market). By extracting the lemma of the word allows the dependency parser to recognize different forms of a word and allows the dependency parser to more accurately parse lemmas of a word.

Children Stack[0]
Implementation: I implemented the feature which counted the number of children that the first item popped from the stack has. It checks for the number of children by iterating through arcs and when stk_idx0 match with the first item in teh arc tuple, num would be incremented.
Complexity:O(n^2) because iterates through all the arcs for n times each time checking to see if the parent matches the current word and then increments 1 when a match is found. 
Performance: 
UAS: 0.145679012346 
LAS: 0.0765432098765
The children counting feature extraction allowed all the languages except for english to go up. The displayed example above is the English example and is thus lower than the result from part 2. Implementing number of children on english may not be effective as english has so many dependencies resulting in overfitting.

Postag Stack[0]
Implementation: Takes the index of the first item popped from the stack and token set to the list of features in the tokens ictionary. Then checks if tag is in token and in FeatureExtractor._check_informative, it checks to see if the tag is a None type or empty string. Lastly each of the tags in the sentence  are tagged with "STACK_0_POSTAG_"
Complexity: Similar to Lemma Stack[0], it takes O(n) total because O(1) to access dictionary and when iterating through n words in a sentence, takes up to O(n).
Performance:
UAS: 0.40987654321 
LAS: 0.345679012346
Parts of speech increases the performance by the most as it extracts the most important feature in dependency parsing. Training the data on the parts of speech allows for more words parsed to be tagged with the correct heads. 

Tradeoffs for arc-eager parsing is that arc-eager parser uses a bottom up parsing method generating subtrees and combining them recursively to generate the tree. However, the assumption is that the sentences are projective as it would then take O(n) time. However, if the sentence is not projective, it would lead to inaccurate tags since the model was trained on projective sentences.

