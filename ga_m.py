import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from nen import QP, ProblemResult, MethodResult, Problem
from nen.Solver import SAQPSolver, JarSolver

# names_FSP = ['E-Shop', 'eCos', 'uClinux', 'Amazon'] # iterations=30，maxEvaluations=50000
# names_FSP = ['E-Shop', 'ERS', 'WebPortal', 'Drupal']
names_FSP = ['E-Shop', 'ERS', 'WebPortal', 'Drupal']
order_FSP = ['COST', 'USED_BEFORE', 'DEFECTS', 'DESELECTED']
weight_FSP = {'COST': 1 / 4, 'USED_BEFORE': 1 / 4, 'DEFECTS': 1 / 4, 'DESELECTED': 1 / 4}

# names_NRP = ['classic-1', 'rp', 'ms', 'Baan']
names_NRP = ['Baan']
order_NRP = ['cost', 'revenue']
weight_NRP = {'cost': 1 / 2, 'revenue': 1 / 2}

result_folder = 'ga_'

for name in names_NRP:
    problem = Problem(name)
    problem.vectorize(order_NRP)

    # prepare the problem result folder before solving
    problem_result = ProblemResult(name, problem, result_folder)

    # solve with NSGA-II
    JarSolver.solve(
        solver_name='GASingle', config_name='tmp_config',
        problem=name, objectiveOrder=order_NRP, iterations=30,
        populationSize=100, maxEvaluations=2000, weights=weight_NRP,
        crossoverProbability=0.8, mutationProbability=(1 / problem.variables_num),
        resultFolder=result_folder, methodName='ga', exec_time=-1
    )
    # load results
    ea_result = MethodResult('ga', problem_result.path, problem)
    ea_result.load(evaluate=True, single_flag=True)
    ea_result.make_method_result(single_flag=True)
    problem_result.add(ea_result)
    problem_result.dump()

# for name in names_FSP:
#     # result_folder = 'nsgaii-{}'.format(name)
#     problem = Problem(name)
#     problem.vectorize(order_FSP)

#     # prepare the problem result folder before solving
#     problem_result = ProblemResult(name, problem, result_folder)

#     # solve with NSGA-II
#     JarSolver.solve(
#         solver_name='GASingle', config_name='tmp_config',
#         problem=name, objectiveOrder=order_FSP, iterations=30,
#         populationSize=100, maxEvaluations=20000, weights=weight_FSP,
#         crossoverProbability=0.8, mutationProbability=(1 / problem.variables_num),
#         resultFolder=result_folder, methodName='ga', exec_time=-1
#     )

#     # load results
#     ea_result = MethodResult('ga', problem_result.path, problem)
#     ea_result.load(evaluate=True, single_flag=True)
#     ea_result.make_method_result(single_flag=True)
#     problem_result.add(ea_result)
#     problem_result.dump()