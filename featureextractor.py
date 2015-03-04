from nltk.compat import python_2_unicode_compatible

printed = False

@python_2_unicode_compatible
class FeatureExtractor(object):
    @staticmethod
    def _check_informative(feat, underscore_is_informative=False):
        """
        Check whether a feature is informative
        """

        if feat is None:
            return False

        if feat == '':
            return False

        if not underscore_is_informative and feat == '_':
            return False

        return True

    @staticmethod
    def find_left_right_dependencies(idx, arcs):
        left_most = 1000000
        right_most = -1
        dep_left_most = ''
        dep_right_most = ''
        for (wi, r, wj) in arcs:
            if wi == idx:
                if (wj > wi) and (wj > right_most):
                    right_most = wj
                    dep_right_most = r
                if (wj < wi) and (wj < left_most):
                    left_most = wj
                    dep_left_most = r
        return dep_left_most, dep_right_most

    @staticmethod
    def extract_features(tokens, buffer, stack, arcs):
        """
        This function returns a list of string features for the classifier

        :param tokens: nodes in the dependency graph
        :param stack: partially processed words
        :param buffer: remaining input words
        :param arcs: partially built dependency tree

        :return: list(str)
        """

        """
        Think of some of your own features here! Some standard features are
        described in Table 3.2 on page 31 of Dependency Parsing by Kubler,
        McDonald, and Nivre

        [http://books.google.com/books/about/Dependency_Parsing.html?id=k3iiup7HB9UC]
        """
        result = []


        global printed
        if not printed:
            print("This is not a very good feature extractor!")
            printed = True

        # an example set of features:
        if stack:
           	stack_idx0 = stack[-1]
            	token = tokens[stack_idx0]
            #STK[0] FORM
		if FeatureExtractor._check_informative(token['word'], True):
            		result.append('STK_0_FORM_' + token['word'])
	    #STK[0] FEAT

            	if 'feats' in token and FeatureExtractor._check_informative(token['feats']):
                	feats = token['feats'].split("|")
                	for feat in feats:
                    		result.append('STK_0_FEATS_' + feat)
	    #STK[0] TAG
		if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
			tags = token['tag'].split("|")
			for tag in tags:
				result.append('STK_0_POSTAG_' + tag)
            	# Left most, right most dependency of stack[0]
            	dep_left_most, dep_right_most = FeatureExtractor.find_left_right_dependencies(stack_idx0, arcs)
	    #STK[0] LDEP
            	if FeatureExtractor._check_informative(dep_left_most):
                	result.append('STK_0_LDEP_' + dep_left_most)
            #STK[0] RDEP	
		if FeatureExtractor._check_informative(dep_right_most):
                	result.append('STK_0_RDEP_' + dep_right_most)
	   	if(len(stack)>=2):
			stack_idx1 = stack[-2]
			token = tokens[stack_idx1]
	    #STK[1] LEMMA		
			if 'lemma' in token and FeatureExtractor._check_informative(token['lemma']):
				lemmas = token['lemma'].split("|")
				for lemma in lemmas:
					result.append('STK_1_LEMMA_' + lemma)
	    #STK[1] TAG
			if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
				tags = token['tag'].split("|")
				for tag in tags:
					result.append('STK_1_POSTAG_' + tag)
            	
		
        if buffer:
            	buffer_idx0 = buffer[0]
            	token = tokens[buffer_idx0]
        #BUF[0] FORM   
	 	if FeatureExtractor._check_informative(token['word'], True):
                	result.append('BUF_0_FORM_' + token['word'])
	#BUF[0] FEATS
	        if 'feats' in token and FeatureExtractor._check_informative(token['feats']):
            		feats = token['feats'].split("|")
            		for feat in feats:
                		result.append('BUF_0_FEATS_' + feat)
        #BUF[0] TAG    	
		if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
			tags = token['tag'].split("|")
			for tag in tags:
				result.append('BUF_0_POSTAG_' + tag)
    	#BUF[0] LEMMA	
		if 'lemma' in token and FeatureExtractor._check_informative(token['lemma']):
			lemmas = token['lemma'].split("|")
			for lemma in lemmas:
				result.apprent('BUF_0_LEMMA_' + lemma)
        	
        	dep_left_most, dep_right_most = FeatureExtractor.find_left_right_dependencies(buffer_idx0, arcs)
	#BUF[0] LDEP
        	if FeatureExtractor._check_informative(dep_left_most):
            		result.append('BUF_0_LDEP_' + dep_left_most)
        #BUF[0] RDEP	
		if FeatureExtractor._check_informative(dep_right_most):
            		result.append('BUF_0_RDEP_' + dep_right_most)
		if len(buffer) >= 2:
			buffer_idx1 = buffer[1]
	    		token = tokens[buffer_idx1]
	#BUF[1] FORM    		
			if FeatureExtractor._check_informative(token['word'], True):
				result.append('BUF_1_FORM_' + token['word'])
	#BUF[1] LEMMA
			if 'lemma' in token and FeatureExtractor._check_informative(token['lemma']):
		    		lemmas = token['lemma'].split("|")
				for lemma in lemmas:
					result.append('BUF_1_LEMMA_' + lemma)
	#BUF[2] TAG
		if len(buffer) >= 3:
			if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
				tags = token['tag'].split("|")
				for tag in tags:
					result.append('BUF_2_POSTAG_' + tag)
        #BUF[3] TAG
	    	if len(buffer) >= 4:
			if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
				tags = token['tag'].split("|")
				for tag in tags:
					result.append('BUF_3_POSTAG_' + tag)
   
	
	return result
