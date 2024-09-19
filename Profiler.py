import time

from Extractor import Extractor
from DeliveryOptimizer import DeliveryOptimizer
from DeliveryOptimizerAI import DeliveryOptimizerAI

def runWithoutAI():
    start_time = time.time()

    optimizer = DeliveryOptimizer()
    optimizer.calculate_deliveries()

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time

def runWithAI():
    start_time = time.time()

    optimizer = DeliveryOptimizerAI(
        Extractor.get_connections(),
        Extractor.get_deliveries()
    )
    optimizer.a_star_search()

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time

def main():
    executions = [1 for _ in range(1000)]
    withoutAITimes = []
    withAITimes = []

    for execution in executions:
        withoutAITimes.append(runWithoutAI())
        withAITimes.append(runWithAI())

    max_withoutAI = max(withoutAITimes)
    min_withoutAI = min(withoutAITimes)
    avg_withoutAI = sum(withoutAITimes) / len(withoutAITimes)

    print(f"Without AI - (Max: {max_withoutAI}, Min: {min_withoutAI}, Average: {avg_withoutAI}) seconds")

    max_withAI = max(withAITimes)
    min_withAI = min(withAITimes)
    avg_withAI = sum(withAITimes) / len(withAITimes)

    print(f"With AI - (Max: {max_withAI}, Min: {min_withAI}, Average: {avg_withAI}) seconds")

if __name__ == '__main__':
    main()
