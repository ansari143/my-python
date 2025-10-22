'''2. Implement __add__ in a Vector class so that adding two Vector objects
returns a new Vector with summed components.
'''

from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class Vector:
    components: Tuple[float, ...]
    
    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension")
        return Vector(tuple(a + b for a, b in zip(self.components, other.components)))

    def __repr__(self) -> str:
        return f"Vector({self.components})"

# Example
v1 = Vector((1, 2, 3))
v2 = Vector((4, 5, 6))
print(v1 + v2)  # Vector((5, 7, 9))
