# Author: Clinton Sheppard <fluentcoder@gmail.com>
# Copyright (c) 2016 Clinton Sheppard
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0

import unittest
import datetime
import genetic


def get_fitness(genes):
    return genes.count(1)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}...{1}\t{2:3.2f}\t{3}".format(
        ''.join(map(str, candidate.Genes[:15])),
        ''.join(map(str, candidate.Genes[-15:])),
        candidate.Fitness,
        str(timeDiff)))


class OneMaxTests(unittest.TestCase):
    def test(self, length=100):
        geneset = [0, 1]
        startTime = datetime.datetime.now()

        def fnDisplay(candidate):
            display(candidate, startTime)

        def fnGetFitness(genes):
            return get_fitness(genes)

        optimalFitness = length
        best = genetic.get_best(fnGetFitness, length, optimalFitness,
                                geneset, fnDisplay)
        self.assertEqual(best.Fitness, optimalFitness)
