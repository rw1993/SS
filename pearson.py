# -*- coding:utf-8 -*-
from scipy.stats.stats import pearsonr


def load_numbers(string):
    with open(string, "r") as f:
        lines = [line[:-1] for line in f.readlines()]
        numbers = map(float, lines)
        return numbers


def normalize(rates):
    max_rate = max(rates)
    min_rate = min(rates)
    divider = max_rate - min_rate
    return map(lambda x:x / divider, rates)


if __name__ == "__main__":
    ai_rates = load_numbers("similarities.txt")
    man_rates = load_numbers("gs.txt")
    man_rates = normalize(man_rates)
    print pearsonr(ai_rates, man_rates)
