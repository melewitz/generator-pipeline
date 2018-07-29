# GeneratorPipeline
An intuitive and efficient way to pipe data from one python generator to another.

GeneratorPipeline is modeled after pipes from the Unix command line.  No
temporary variables are required and the sequence is easy to visualize.

## Usage
Below is a trivial example that demonstrates the power of GeneratorPipeline.
Each pipeline component must accept a generator as the first parameter.
```python
>>> from pipeline import GeneratorPipeline
>>>
>>> @GeneratorPipeline
... def nums(gen, max):
...     yield from range(1, max+1)
...
>>> @GeneratorPipeline
... def times(gen, constant, *args):
...     yield from (n * constant for n in gen)
...
>>> @GeneratorPipeline
... def minus(gen, constant):
...     yield from (n-constant for n in gen)
...
>>>
>>> gen = nums(5) | times(2)
>>> list(gen)
[2, 4, 6, 8, 10]
>>>
>>> gen = nums(5) | times(2) | minus(5) | times(3)
>>> list(gen)
[-9, -3, 3, 9, 15]

```

## TODO

1. Add is_datasource parameter so source only generators do not require an input generator parameter.  Something like:
```python
>>> @GeneratorPipeline(is_datasource)
... def nums(max):  # Note the parameter 'gen' is no longer required
...     yield from range(1, max+1)
```
2. Investigate support for generator classes and class method generators.
