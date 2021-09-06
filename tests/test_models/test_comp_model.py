from hypothesis import given, settings, assume, strategies as st
from hypothesis import reproduce_failure, note
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from core.nodes.nodes import Component
from models.comp_model import CompModel

# settings(max_examples = 20)

test_comp_model = CompModel()

root = Component(name='root', desc='no description')
first = Component(name='Project', desc='Top level node, describe the project here!')
root.add_child(first)

root_name == getattr(root, "name")
root_desc == getattr(root, "desc")
first_name == getattr(first, "name")
first_desc == getattr(first, "desc")

root_index_name = test_comp_model.createIndex(0, 0, None)
first_index_name = test_comp_model.createIndex(0, 0, root_index_name)
root_index_desc = test_comp_model.createIndex(0, 1, None)
first_index_desc = test_comp_model.createIndex(0, 1, root_index_name)

def test_comp_model_creation():

    assert test_comp_model.root == root

def test_comp_model_data():

    assert test_comp_model.data(root_index_name, qtc.Qt.DisplayRole) == root_name
    assert test_comp_model.data(root_index_desc, qtc.Qt.DisplayRole) == root_desc
    assert test_comp_model.data(first_index_name, qtc.Qt.DisplayRole) == first_name
    assert test_comp_model.data(first_index_desc, qtc.Qt.DisplayRole) == first_desc

# def test_comp_model_index():

#     assert root_index ==