# Load the project path
# from project_path import PROJECT_PATH
# import sys
# sys.path.append(PROJECT_PATH)

from nen import QP, ProblemResult, MethodResult, Quadratic
from nen.Solver import QAWSOSolver, SolverUtil, EmbeddingSampler

names_FSP = ['ERS', 'WebPortal', 'Amazon']
order_FSP = ['COST', 'USED_BEFORE', 'DEFECTS', 'DESELECTED']
weight_FSP = {'COST': 1 / 4, 'USED_BEFORE': 1 / 4, 'DEFECTS': 1 / 4, 'DESELECTED': 1 / 4}

names_NRP = ['rp', 'ms', 'Baan']
order_NRP = ['cost', 'revenue']
weight_NRP = {'cost': 1 / 2, 'revenue': 1 / 2}


for name in names_FSP:
    result_folder = 'soqa-{}'.format(name)
    problem = QP(name, order_FSP)
    problem_result = ProblemResult(name, problem, result_folder)
    moqa_method_result = MethodResult('soqa', problem_result.path, problem)
    wso = Quadratic(linear=SolverUtil.weighted_sum_objective(problem.objectives, weight_FSP))
    penalty = EmbeddingSampler.calculate_penalty(wso, problem.constraint_sum)
    for _ in range(3):
        result = QAWSOSolver.solve(problem=problem, num_reads=1000, penalty=penalty, weights=weight_FSP)
        moqa_method_result.add(result)

    # add result to method result, problem result
    problem_result.add(moqa_method_result)

    # dump result to result/given_path folder
    problem_result.dump()

for name in names_NRP:
    result_folder = 'soqa-{}'.format(name)
    problem = QP(name, order_NRP)
    problem_result = ProblemResult(name, problem, result_folder)
    moqa_method_result = MethodResult('soqa', problem_result.path, problem)
    wso = Quadratic(linear=SolverUtil.weighted_sum_objective(problem.objectives, weight_NRP))
    penalty = EmbeddingSampler.calculate_penalty(wso, problem.constraint_sum)
    for _ in range(3):
        result = QAWSOSolver.solve(problem=problem, num_reads=1000, penalty=penalty, weights=weight_NRP)
        moqa_method_result.add(result)

    # add result to method result, problem result
    problem_result.add(moqa_method_result)

    # dump result to result/given_path folder
    problem_result.dump()