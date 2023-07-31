﻿import pprint
from abc import ABC
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, Union

from gempy_engine.core.data.legacy_solutions import LegacySolution
from gempy_engine.core.data.stack_relation_type import StackRelationType
from gempy.core.data.structural_element import StructuralElement


class FaultsRelationSpecialCase(Enum):
    OFFSET_NONE = auto()
    OFFSET_ALL = auto()
    
    
@dataclass
class StructuralGroup(ABC):
    name: str
    elements: list[StructuralElement] = field(repr=False)
    structural_relation: StackRelationType
    
    fault_relations: Optional[Union[list["StructuralGroup"], FaultsRelationSpecialCase]] = field(default=None, repr=False)
    solution: Optional[LegacySolution] = field(init=False, default=None, repr=False)
    
    def __repr__(self):
        elements_repr = ',\n'.join([repr(e) for e in self.elements])
        return f"StructuralGroup(\n" \
               f"\tname={self.name},\n" \
               f"\tstructural_relation={self.structural_relation},\n" \
               f"\telements=[\n{elements_repr}\n]\n)"

    def _repr_html_(self):
        elements_html = '<br>'.join([e._repr_html_() for e in self.elements])
        html = f"""
    <table style="border-left:1.2px solid black;>
      <tr><th colspan="2"><b>StructuralGroup:</b></th></tr>
      <tr><td>Name:</td><td>{self.name}</td></tr>
      <tr><td>Structural Relation:</td><td>{self.structural_relation}</td></tr>
      <tr><td>Elements:</td><td>{elements_html}</td></tr>
    </table>
        """
        return html

    def _repr_html_2(self):
        elements_html = ''.join([e._repr_html_() for e in self.elements])
        html = f"""<pre>
    <b>StructuralGroup:</b>
      Name: {self.name}
      Structural Relation: {self.structural_relation}
      Elements:
    {elements_html}
      Solution: {self.solution}
    </pre>"""
        return html

    @property
    def id(self):
        raise NotImplementedError
    
    @property
    def number_of_points(self) -> int:
        return sum([element.number_of_points for element in self.elements])
    
    @property
    def number_of_orientations(self) -> int:
        return sum([element.number_of_orientations for element in self.elements])
    
    @property
    def number_of_elements(self) -> int:
        return len(self.elements)



# ? I think these two subclasses are not necessary
@dataclass
class Stack(StructuralGroup): 
    def __int__(self, name: str, elements: list[StructuralElement]):
        super().__init__(name, elements)
        
    def __repr__(self):
        return pprint.pformat(self.__dict__)


@dataclass
class Fault(StructuralGroup): 
    pass
