# test
import py2php
import compiler

#unindented_source = py2php.get_source(compiler.parseFile('source.py'))

unindented_source = py2php.get_source(compiler.parse('var = 8'))

print py2php.indent_source(py2php.add_semicolons(unindented_source))