import unittest

from pipeline import GeneratorPipeline

@GeneratorPipeline
def nums(gen, max):
    yield from range(1, max+1)

@GeneratorPipeline
def times(gen, constant, *args):
    yield from (n * constant for n in gen)

@GeneratorPipeline
def minus(gen, constant):
    yield from (n-constant for n in gen)

class TestStringMethods(unittest.TestCase):

    def test_source_generator(self):
        """Verify execution of the decorated source generator with a pipeline"""
        pipeline = nums(5)
        self.assertEqual([1, 2, 3, 4, 5], list(pipeline))

    def test_source_generator_reuse(self):
        self.assertEqual([1, 2, 3, 4, 5], list(nums(5)))
        self.assertEqual([1, 2, 3, 4], list(nums(4)))

    def test_pipeline_2_terms(self):
        pipeline = nums(5) | times(2)
        self.assertEqual([2, 4, 6, 8, 10], list(pipeline))

    def test_pipeline_3_terms(self):
        pipeline = nums(5) | times(2) | minus(1)
        self.assertEqual([1, 3, 5, 7, 9], list(pipeline))

    def test_pipeline_3_terms_dups(self):
        pipeline = nums(5) | times(2) | minus(5) | times(3)
        self.assertEqual([-9, -3, 3, 9, 15], list(pipeline))

if __name__ == '__main__':
    unittest.main()


