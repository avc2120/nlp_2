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
    def num_children(idx, arcs):
	num = 0
	for (wi, r, wj) in arcs:
		if wi== idx:
			num = num + 1
	return num
    
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
            printed = True
	
        # an example set of features:
        if stack:
           	stack_idx0 = stack[-1]

            	token = tokens[stack_idx0]
            	#STK[0] FORM
		def stack_0_form():
			if FeatureExtractor._check_informative(token['word'], True):
            			result.append('STK_0_FORM_' + token['word'])
	    	#STK[0] FEAT
            	def stack_0_feat():
			if 'feats' in token and FeatureExtractor._check_informative(token['feats']):
                		feats = token['feats'].split("|")
                		for feat in feats:
                    			result.append('STK_0_FEATS_' + feat)
		#STK[0] TAG
		def stack_0_tag():	
			if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
				tags = token['tag'].split("|")
				for tag in tags:
					result.append('STK_0_POSTAG_' + tag)
        	def stack_0_ctag():
			if 'ctag' in token and FeatureExtractor._check_informative(token['ctag']):
				tags = token['ctag'].split("|")
				for tag in tags:
					result.append('STK_0_CTAG_' + tag)
        	
		# Left most, right most dependency of stack[0]
       		dep_left_most, dep_right_most = FeatureExtractor.find_left_right_dependencies(stack_idx0, arcs)
	
		#STK[0] LDEP
            	def stack_0_ldep():
			if FeatureExtractor._check_informative(dep_left_most):
                		result.append('STK_0_LDEP_' + dep_left_most)
        	#STK[0] RDEP	
		def stack_0_rdep():
			if FeatureExtractor._check_informative(dep_right_most):
                		result.append('STK_0_RDEP_' + dep_right_most)
		num = FeatureExtractor.num_children(stack_idx0, arcs)
		
		def stack_0_child():
			result.append('STK_0_CHILD_' + str(num))
		#STK 0 STUFF------------------
		stack_0_form()
		stack_0_feat()
		stack_0_tag()
		#stack_0_ctag()
		stack_0_ldep()
		stack_0_rdep()
		stack_0_child()
		#-----------------------------
		if(len(stack)>=2):
			stack_idx1 = stack[-2]
			token = tokens[stack_idx1]
     		
			#STK[1] LEMMA		
			def stack_1_lemma():
				if 'lemma' in token and FeatureExtractor._check_informative(token['lemma']):
					lemmas = token['lemma'].split("|")
					for lemma in lemmas:
						result.append('STK_1_LEMMA_' + lemma)
	    	
			#STK[1] TAG
			def stack_1_tag():
			 	if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
			 		tags = token['tag'].split("|")
			 		for tag in tags:
			 			result.append('STK_1_POSTAG_' + tag)
        		def stack_1_form():
				if FeatureExtractor._check_informative(token['word'], True):
            				result.append('STK_1_FORM_' + token['word'])
	    		#STK[0] FEAT
            		def stack_1_feat():
				if 'feats' in token and FeatureExtractor._check_informative(token['feats']):
                			feats = token['feats'].split("|")
                			for feat in feats:
                    				result.append('STK_1_FEATS_' + feat)
			#STK[0] TAG
        		def stack_1_ctag():
				if 'ctag' in token and FeatureExtractor._check_informative(token['ctag']):
					tags = token['ctag'].split("|")
					for tag in tags:
						result.append('STK_1_CTAG_' + tag)
        	
		#STK 1 STUFF-----------------
			stack_1_tag()
			stack_1_form()
			#stack_1_ctag()
			stack_1_feat()
		#form tag feats
		#---------------------------
		if buffer:
			def distance():
				noun_count = 0
				verb_count = 0	
				buf_idx0 = buffer[0]
				small = stack_idx0 if stack_idx0 < buf_idx0 else buf_idx0
				big = stack_idx0 if stack_idx0 > buf_idx0 else buf_idx0
				for index in range(small, big+1):
					token = tokens[index]
					if 'ctag' in token and FeatureExtractor._check_informative(token['ctag']):
						tags = token['ctag'].split("|")
						for tag in tags:
							if tag == 'NN' or  tag == 'NOUN':
								noun_count = noun_count + 1
							if tag == 'VV' or tag == 'VERB':
								verb_count = verb_count + 1
				result.append('NOUN_COUNT_' + str(noun_count))
				result.append('VERB_COUNT_' + str(verb_count))

			distance()
			
		
        if buffer:
            	buffer_idx0 = buffer[0]
            	token = tokens[buffer_idx0]
        	#BUF[0] FORM 
		def buf_0_form():  
	 		if FeatureExtractor._check_informative(token['word'], True):
                		result.append('BUF_0_FORM_' + token['word'])
		#BUF[0] FEATS
		def buf_0_feats():
	        	if 'feats' in token and FeatureExtractor._check_informative(token['feats']):
            			feats = token['feats'].split("|")
            			for feat in feats:
                			result.append('BUF_0_FEATS_' + feat)
        	#BUF[0] TAG    	
		def buf_0_tag():
			if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
				tags = token['tag'].split("|")
				for tag in tags:
					result.append('BUF_0_POSTAG_' + tag)
    		#BUF[0] CTAG
		def buf_0_ctag():
			if 'ctag' in token and FeatureExtractor._check_informative(token['ctag']):
				tags = token['ctag'].split("|")
				for tag in tags:
					result.append('BUF_0_CTAG_' + tag)
        	
		#BUF[0] LEMMA	
		def buf_0_lemma():	
			if 'lemma' in token and FeatureExtractor._check_informative(token['lemma']):
				lemmas = token['lemma'].split("|")
				for lemma in lemmas:
					result.apprent('BUF_0_LEMMA_' + lemma)
        	
        	dep_left_most, dep_right_most = FeatureExtractor.find_left_right_dependencies(buffer_idx0, arcs)
		#BUF[0] LDEP
		def buf_0_ldep():
        		if FeatureExtractor._check_informative(dep_left_most):
            			result.append('BUF_0_LDEP_' + dep_left_most)
        	#BUF[0] RDEP
		def buf_0_rdep():	
			if FeatureExtractor._check_informative(dep_right_most):
            			result.append('BUF_0_RDEP_' + dep_right_most)
		num = FeatureExtractor.num_children(buffer_idx0, arcs)
		def buf_0_child():
			result.append('BUF_0_CHILD_' + str(num))
		#BUF 0 STUFF ----------------
		buf_0_form()
		buf_0_feats()
		buf_0_tag()
		#buf_0_ctag()
		buf_0_ldep()
		buf_0_rdep()
		buf_0_child()
		#---------------------------
	
		if len(buffer) >= 2:
			buffer_idx1 = buffer[1]
	    		token = tokens[buffer_idx1]
			#BUF[1] FORM
			def buf_1_form():    		
				if FeatureExtractor._check_informative(token['word'], True):
					result.append('BUF_1_FORM_' + token['word'])
	    	#BUF[0] FEAT
            		def buf_1_feat():
				if 'feats' in token and FeatureExtractor._check_informative(token['feats']):
                			feats = token['feats'].split("|")
                			for feat in feats:
                    				result.append('BUF_1_FEATS_' + feat)
			# #BUF[0] TAG
         		def buf_1_ctag():
				if 'ctag' in token and FeatureExtractor._check_informative(token['ctag']):
			 		tags = token['ctag'].split("|")
			 		for tag in tags:
		 				result.append('BUF_1_CTAG_' + tag)
        		
		#BUF 2 STUFF--------------
			buf_1_form()
			buf_1_feat()
			buf_1_ctag()
			#tag feats rdep ldep
		#-------------------------	
		#BUF[2] TAG
		if len(buffer) >= 3:
			buffer_idx2 = buffer[2]
			token = tokens[buffer_idx2]
			def buf_2_tag():
				if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
					tags = token['tag'].split("|")
					for tag in tags:
						result.append('BUF_2_POSTAG_' + tag)
        	#BUF 2 TAG--------------
			#buf_2_tag()
		#-----------------------
		#BUF[3] TAG
	   
		if len(buffer) >= 4:
			buffer_idx3 = buffer[3]
			token = tokens[buffer_idx3]
			def buf_3_tag():
				if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
					tags = token['tag'].split("|")
					for tag in tags:
						result.append('BUF_3_POSTAG_' + tag)
   
		#BUF 3 STUFF------------
			#buf_3_tag() #increases
		#-----------------------
	return result
