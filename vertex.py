"""
Vertex used in graphs.
"""
class Vertex:
    """
    Create a vertex with the given id and data.
    :param id: (int) the identifier of the vertex. Should be unique.
    """
    def __init__(self, id: int):
        self._id = id

    """
    Gives the id of this vertex.
    :return: (int) the identifier of the vertex.
    """
    def get_id(self):
        return self._id

    """
    Two vertex are equals if they have the same identifier.
    """
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Vertex):
            return False
        return self.get_id() == o.get_id()