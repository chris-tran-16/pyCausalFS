
__author__ = """N. Cullen <ncullen.th@dartmouth.edu>"""

from pyCausalFS.pyBN.classes import Factorization

from copy import copy
import numpy as np


def marginal_ve_e(bn, target, evidence={}):
	"""
	Perform Sum-Product Variable Elimination on
	a Discrete Bayesian Network.

	Arguments
	---------
	*bn* : a BayesNet object

	*target* : a list of target RVs

	*evidence* : a dictionary, where
		key = rv and value = rv value

	Returns
	-------
	*marginal_dict* : a dictionary, where
		key = an rv in target and value =
		a numpy array containing the key's
		marginal conditional probability distribution.

	Notes
	-----
	- Mutliple pieces of evidence often returns "nan"...numbers too small?
		- dividing by zero -> perturb values in Factor class
	"""
	_phi = Factorization(bn)

	order = copy(list(bn.nodes()))
	order.remove(target)

	#### EVIDENCE PROCESSING ####
	for E, e in evidence.items():
		_phi -= (E,e)
		order.remove(E)

	#### SUM-PRODUCT ELIMINATE VAR ####
	for var in order:
		_phi /= var

	# multiply phi's together if there is evidence
	final_phi = _phi.consolidate()

	return np.round(final_phi.cpt,4)