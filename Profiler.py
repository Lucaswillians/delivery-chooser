import time
import re
import matplotlib.pyplot as plt

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

def extract_profit_from_log():
    profit = 0
    with open("delivery_optimizer.log", "r") as log_file:
        for line in log_file:
            match = re.search(r"Total profit: (\d+)", line)
            if match:
                profit = int(match.group(1))
    return profit

def main():
    executions = 100
    withoutAITimes = []
    withAITimes = []
    withoutAIProfits = []
    withAIProfits = []

    for _ in range(executions):
        # Run without AI
        withoutAITimes.append(runWithoutAI())
        withoutAIProfits.append(extract_profit_from_log())

        # Run with AI
        withAITimes.append(runWithAI())
        withAIProfits.append(extract_profit_from_log())

    # Calculate statistics for time
    max_withoutAI = max(withoutAITimes)
    min_withoutAI = min(withoutAITimes)
    avg_withoutAI = sum(withoutAITimes) / len(withoutAITimes)

    max_withAI = max(withAITimes)
    min_withAI = min(withAITimes)
    avg_withAI = sum(withAITimes) / len(withAITimes)

    print(f"Without AI - (Max: {max_withoutAI}, Min: {min_withoutAI}, Average: {avg_withoutAI}) seconds")
    print(f"With AI - (Max: {max_withAI}, Min: {min_withAI}, Average: {avg_withAI}) seconds")

    # Calculate statistics for profit
    avg_profit_withoutAI = sum(withoutAIProfits) / len(withoutAIProfits)
    avg_profit_withAI = sum(withAIProfits) / len(withAIProfits)

    print(f"Without AI - Average Profit: {avg_profit_withoutAI}")
    print(f"With AI - Average Profit: {avg_profit_withAI}")

    # Plot results
    plot_results(withoutAITimes, withAITimes, withoutAIProfits, withAIProfits)

def plot_results(withoutAITimes, withAITimes, withoutAIProfits, withAIProfits):
    plt.figure(figsize=(12, 6))

    # Plot execution times
    plt.subplot(1, 2, 1)
    plt.plot(withoutAITimes, label='Without AI')
    plt.plot(withAITimes, label='With AI')
    plt.xlabel('Executions')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time Comparison')
    plt.legend()

    # Plot profits
    plt.subplot(1, 2, 2)
    plt.plot(withoutAIProfits, label='Without AI')
    plt.plot(withAIProfits, label='With AI')
    plt.xlabel('Executions')
    plt.ylabel('Profit')
    plt.title('Profit Comparison')
    plt.legend()

    # Save the figure
    plt.tight_layout()
    plt.savefig('comparison_graphs.png')
    plt.show()

if __name__ == '__main__':
    main()
