import ast
from pathlib import Path
SOURCE=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text();TREE=ast.parse(SOURCE)
def load(name):
 node=next(x for x in TREE.body if isinstance(x,ast.FunctionDef) and x.name==name);scope={};exec(compile(ast.Module(body=[node],type_ignores=[]),'<contract>','exec'),scope);return scope[name]
def test_contradiction_and_unknown_propagate():
 fn=load('propagate');assert fn(3,[[0,1],[1,2]],[],[0],[1,2])==['CONTRADICTED','INVALIDATED','INVALIDATED'];assert fn(3,[[0,1],[1,2]],[],[],[0,1,2])==['UNKNOWN','AT_RISK','AT_RISK']
def test_supported_graph_stays_verified():
 assert load('propagate')(3,[[0,1],[1,2]],[0,1,2],[],[])==['SUPPORTED','SUPPORTED','SUPPORTED']
def test_surface_and_attribution():
 for name in ('open_circuit','audit','get_circuit'):assert f'def {name}' in SOURCE
 assert 'one citation list per premise required' in SOURCE and 'two evidence origins required' in SOURCE and 'prompt_comparative' in SOURCE

