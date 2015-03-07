from providedcode.dependencygraph import DependencyGraph
from providedcode.transitionparser import TransitionParser
import sys
if __name__ == '__main__':
	sentence = []
	for line in sys.stdin:
		dg = DependencyGraph.from_sentence(line)
		sentence.append(dg)
	 
	tp = TransitionParser.load(sys.argv[1])
	parsed = tp.parse(sentence)
	for i in parsed:
		print i.to_conll(10).encode('utf-8'), '\n'
