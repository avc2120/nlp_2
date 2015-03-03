class Transition(object):
    """
    This class defines a set of transitions which are applied to a
    configuration to get the next configuration.
    """
    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'

    def __init__(self):
        raise ValueError('Do not construct this object!')

    @staticmethod
    def left_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
	hasHead = False
	s = conf.stack[-1]
	for tuple in conf.arcs:
		if tuple[2] == s:
			hasHead = True
	if(s != 0 and hasHead == False):
		s = conf.stack.pop(-1)
		b = conf.buffer[0]
		conf.arcs.append((b,relation,s))
	else:
		return -1
    @staticmethod
    def right_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer or not conf.stack:
            return -1

        # You get this one for free! Use it as an example.

        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer.pop(0)

        conf.stack.append(idx_wj)
        conf.arcs.append((idx_wi, relation, idx_wj))

    @staticmethod
    def reduce(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
	hasHead = False
	i = conf.stack[-1]
	for tuple in conf.arcs:
		if tuple[2] == i:
			hasHead = True
	if(hasHead):
		conf.stack.pop(-1)
	else:
		return -1

    @staticmethod
    def shift(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
	if not conf.stack:
		conf.stack = []

	s = conf.buffer.pop(0)
	conf.stack.append(s)
