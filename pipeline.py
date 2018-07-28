

class GeneratorPipeline:
    """
    Function decorator that allows data to be piped from one generator
    to another.
    """
    def __init__(self, function):
        """Invoked when the decorator is used on a function"""
        self.function = function

    def __call__(self, *args, **kwargs):
        """
        Invoked when a decorated function is called.  Returns a unique instance
        configured with the parameters passed to the decorated function.
        """
        return self.PipelineTerm(self.function, *args, **kwargs)

    class PipelineTerm:
        """
        Represents a unique instance of the decorated function and
        implements the chaining of data between pipeline terms.
        """
        def __init__(self, function, *args, **kwargs):
            """Invoked when when a decorated function is used."""
            self.function = function
            self.args = args
            self.kwargs = kwargs
            self.source_generator = None

        def set_source_generator(self, source_generator):
            """
            Assigned the input pipe for a pipeline term which occurs after
            instantiation of the term and its source.
            """
            if self.source_generator is None:
                self.source_generator = source_generator

        def __call__(self, *args, **kwargs):
            return self

        def __or__(self, rhs):
            lhs = self.__call__(*self.args, **self.kwargs)
            rhs.set_source_generator(lhs)
            return rhs(lhs, *self.args, **self.kwargs)

        def __iter__(self):
            return self.function(self.source_generator, *self.args, **self.kwargs)

        def __next__(self):
            yield from self

