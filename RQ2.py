import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from nen import Problem, ProblemResult, MethodResult, Visualizer

names_FSP = ['WebPortal', 'Drupal', 'E-Shop', 'ERS']
# names_FSP = ['ERS']
order_FSP = ['COST', 'USED_BEFORE', 'DEFECTS', 'DESELECTED']
weight_FSP = {'COST': 1 / 4, 'USED_BEFORE': 1 / 4, 'DEFECTS': 1 / 4, 'DESELECTED': 1 / 4}

# names_NRP = ['ms', 'Baan', 'classic-1', 'rp']
names_NRP = ['rp', 'ms']
order_NRP = ['cost', 'revenue']
weight_NRP = {'cost': 1 / 2, 'revenue': 1 / 2}

nsgaii_result_folder = 'nsgaii_'
moqa_result_folder = 'moqa_'

# compare MOQA with NSGA-II
# for name in names_FSP:
#     problem = Problem(name)
#     problem.vectorize(order_FSP)

#     # prepare the problem result folder before solving
#     nsgaii_problem_result = ProblemResult(name, problem, nsgaii_result_folder)
#     moqa_problem_result = ProblemResult(name, problem, moqa_result_folder)

#     ga_result = MethodResult('nsgaii', nsgaii_problem_result.path, problem)
#     ga_result.load(evaluate=True, total_num_anneals=100)
#     qa_result = MethodResult('moqa', moqa_problem_result.path, problem)
#     qa_result.load(evaluate=True, total_num_anneals=3000)

#     moqa_problem_result.add(ga_result)
#     moqa_problem_result.add(qa_result)

#     # compare
#     scores_ga = moqa_problem_result.average_compare(union_method='moqa', average_method='nsgaii')
#     table_ga = Visualizer.tabulate_single_problem(
#         name, ['moqa', 'nsgaii'], ['elapsed time', 'found', 'front', 'igd', 'hv', 'spacing'],
#         scores_ga, {'elapsed time': 4, 'found': 2, 'front': 2, 'igd': 2, 'hv': 2, 'spacing': 2}
#     )
#     Visualizer.tabluate(table_ga, 'moqa-nsgaii-compare-{}.csv'.format(name))


for name in names_NRP:
    problem = Problem(name)
    problem.vectorize(order_NRP)
    # prepare the problem result folder before solving
    # prepare the problem result folder before solving
    nsgaii_problem_result = ProblemResult(name, problem, nsgaii_result_folder)
    moqa_problem_result = ProblemResult(name, problem, moqa_result_folder)

    ga_result = MethodResult('nsgaii', nsgaii_problem_result.path, problem)
    ga_result.load(evaluate=True, total_num_anneals=100)
    qa_result = MethodResult('moqa', moqa_problem_result.path, problem)
    qa_result.load(evaluate=True, total_num_anneals=3000)

    moqa_problem_result.add(ga_result)
    moqa_problem_result.add(qa_result)

    # compare
    scores_ga = moqa_problem_result.average_compare(union_method='moqa', average_method='nsgaii')
    table_ga = Visualizer.tabulate_single_problem(
        name, ['moqa', 'nsgaii'], ['elapsed time', 'found', 'front', 'igd', 'hv', 'spacing'],
        scores_ga, {'elapsed time': 4, 'found': 2, 'front': 2, 'igd': 2, 'hv': 2, 'spacing': 2}
    )
    Visualizer.tabluate(table_ga, 'moqa-nsgaii-compare-{}.csv'.format(name))