import random
from providedcode import dataset
from providedcode.transitionparser import TransitionParser
from providedcode.evaluate import DependencyEvaluator
from featureextractor import FeatureExtractor
from transition import Transition

if __name__ == '__main__':
    data = dataset.get_danish_train_corpus().parsed_sents()
    random.seed(1234)
    subdata = random.sample(data, 200)
  
    data1 = dataset.get_english_train_corpus().parsed_sents()
    random.seed(1234)
    subdata1 = random.sample(data1, 200)
    
    data2 = dataset.get_korean_train_corpus().parsed_sents()
    random.seed(1234)
    subdata2 = random.sample(data2, 200)
    
    data3 = dataset.get_swedish_train_corpus().parsed_sents()
    random.seed(1234)
    subdata3 = random.sample(data3, 200)




    try:
        tp = TransitionParser(Transition, FeatureExtractor)
        tp.train(subdata)
        tp.save('danish.model')

        tp1 = TransitionParser(Transition, FeatureExtractor)
        tp1.train(subdata1)
        tp1.save('english.model')

        tp2 = TransitionParser(Transition, FeatureExtractor)
        tp2.train(subdata2)
        tp2.save('korean.model')

        tp3 = TransitionParser(Transition, FeatureExtractor)
        tp3.train(subdata3)
        tp3.save('swedish.model')


        testdata = dataset.get_danish_test_corpus().parsed_sents()
        tp = TransitionParser.load('danish.model')
	parsed = tp.parse(testdata)
	with open('test.conll', 'w') as f:
            for p in parsed:
                f.write(p.to_conll(10).encode('utf-8'))
                f.write('\n')

        ev = DependencyEvaluator(testdata, parsed)
        print "UAS: {} \nLAS: {}".format(*ev.eval())


	testdata1 = dataset.get_english_dev_corpus().parsed_sents()
        tp1 = TransitionParser.load('english.model')
	parsed1 = tp1.parse(testdata1)
	
	with open('test.conll', 'w') as f:
            for p in parsed1:
                f.write(p.to_conll(10).encode('utf-8'))
                f.write('\n')

        ev1 = DependencyEvaluator(testdata1, parsed1)
        print "UAS: {} \nLAS: {}".format(*ev1.eval())


	testdata2 = dataset.get_korean_test_corpus().parsed_sents()
        tp2 = TransitionParser.load('korean.model')
	parsed2 = tp2.parse(testdata2)

	with open('test.conll', 'w') as f:
            for p in parsed2:
                f.write(p.to_conll(10).encode('utf-8'))
                f.write('\n')

        ev2 = DependencyEvaluator(testdata2, parsed2)
        print "UAS: {} \nLAS: {}".format(*ev2.eval())


	testdata3 = dataset.get_swedish_test_corpus().parsed_sents()
        tp3 = TransitionParser.load('swedish.model')
	parsed3 = tp3.parse(testdata3)

	with open('test.conll', 'w') as f:
            for p in parsed3:
                f.write(p.to_conll(10).encode('utf-8'))
                f.write('\n')

        ev3 = DependencyEvaluator(testdata3, parsed3)
        print "UAS: {} \nLAS: {}".format(*ev3.eval())

        #parsing arbitrary sentences (english):
        #sentence = DependencyGraph.from_sentence('Hi, this is a test')

       	#tp = TransitionParser.load('swedish.model')
        #parsed = tp.parse([sentence])
        #print parsed[0].to_conll(10).encode('utf-8')
    except NotImplementedError:
        print """
        This file is currently broken! We removed the implementation of Transition
        (in transition.py), which tells the transitionparser how to go from one
        Configuration to another Configuration. This is an essential part of the
        arc-eager dependency parsing algorithm, so you should probably fix that :)

        The algorithm is described in great detail here:
            http://aclweb.org/anthology//C/C12/C12-1059.pdf

        We also haven't actually implemented most of the features for for the
        support vector machine (in featureextractor.py), so as you might expect the
        evaluator is going to give you somewhat bad results...

        Your output should look something like this:

            UAS: 0.23023302131
            LAS: 0.125273849831

        Not this:

            Traceback (most recent call last):
                File "test.py", line 41, in <module>
                    ...
        NotImplementedError: Please implement shift! """
