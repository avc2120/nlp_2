from providedcode.dependencygraph import DependencyGraph
from providedcode.transitionparser import TransitionParser
import sys
for line in sys.stdin:
	sentence = DependencyGraph.from_sentence(line) 
	tp = TransitionParser.load(sys.argv[1])
	parsed = tp.parse([sentence])
	print parsed[0].to_conll(10).encode('utf-8')
