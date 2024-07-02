from topologicpy.Wire import Wire
from topologicpy.Vertex import Vertex
from topologicpy.Face import Face
from topologicpy.Edge import Edge
from topologicpy.Graph import Graph
from topologicpy.Cell import Cell
from topologicpy.Shell import Shell
from topologicpy.CellComplex import CellComplex
from topologicpy.Cluster import Cluster
from topologicpy.Topology import Topology


def twist_animation(t):
    angle = t * 360
    c = Cell.Prism(height=2, uSides=5, vSides=5, wSides=5)
    c = Topology.Twist(
        c, origin=Vertex.Origin(), angleRange=[0, angle], triangulate=True
    )
    return c, Cell.Prism(width=2, length=2, height=3)


def hyperboloid_animation(t):
    angle = t * 360

    c = Cell.Hyperboloid(
        origin=Vertex.Origin(),
        baseRadius=3,
        topRadius=3,
        height=5,
        sides=60,
        twist=angle,
        placement="lowerleft",
    )
    return c, Cell.Prism(width=2, length=2, height=3)


def cone_animation(t):
    x = t * 4 + 1
    c = Cell.Cone(
        origin=Vertex.Origin(),
        baseRadius=2,
        topRadius=x * -1,
        height=x,
        uSides=20,
        vSides=10,
        direction=[0, 0, 1],
        placement="top",
    )
    return c, Cell.Prism(width=2, length=2, height=15)


def rotated_cell_complex_animation(t):
    angle = t * 360
    c = CellComplex.Prism(height=2, uSides=5, vSides=5, wSides=5)
    bb_centroid = Topology.Centroid(Cell.Prism(width=2, length=2, height=3))
    axis = [0, 0, 1]
    c = Topology.Rotate(
        c,
        origin=bb_centroid,
        axis=axis,
        angle=angle,
        angTolerance=0.001,
        tolerance=0.0001,
    )
    return c, Cell.Prism(width=2, length=2, height=3)


def translated_cell_complex_animation(t):
    distance = t * 0.5
    c = CellComplex.Prism(height=2, uSides=5, vSides=5, wSides=5)
    c = Topology.Translate(c, x=distance, y=0, z=0)
    return c, Cell.Prism(width=2, length=2, height=3)


def taper_animation(t):
    ratio = t * 1.0
    c = Cell.Prism(height=2, uSides=5, vSides=5, wSides=5)
    c = Topology.Taper(
        c, origin=Vertex.Origin(), ratioRange=[0, ratio], triangulate=False
    )
    return c, Cell.Prism(width=2, length=2, height=3)


def scale_animation(t):
    scale_factor = t * 0.9 + 0.1
    c = CellComplex.Prism(uSides=2, vSides=2, wSides=2)
    c = Topology.Scale(c, x=scale_factor, y=scale_factor, z=scale_factor)
    return c, Cell.Prism(width=2, length=2, height=3)


def hyperbolic_paraboloid_animation(t):
    a = t * 0.5
    b = -t * 0.5
    hyp_par = Shell.HyperbolicParaboloidCircularDomain(
        origin=Vertex.Origin(),
        radius=1.5,
        sides=36,
        rings=10,
        A=a,
        B=b,
        direction=[0, 0, 1],
        placement="bottom",
        tolerance=0.0001,
    )
    return hyp_par, Cell.Prism(width=2, length=2, height=3)


def cell_complex_animation(t):
    sides = int(t * 4) + 1
    c = CellComplex.Prism(
        origin=None,
        width=3,
        length=3,
        height=3,
        uSides=sides,
        vSides=sides,
        wSides=sides,
        direction=[0, 0, 1],
        placement="center",
        tolerance=0.0001,
    )
    return c, Cell.Prism(width=2, length=2, height=3)


def explode_animation(t):
    c = CellComplex.Prism(
        origin=Vertex.Origin(),
        width=1,
        length=1,
        height=1,
        uSides=3,
        vSides=3,
        wSides=3,
        direction=[0, 0, 1],
        placement="center",
        tolerance=0.0001,
    )
    explode = Topology.Explode(
        c,
        origin=Vertex.Origin(),
        scale=0.5 + t,
        typeFilter=None,
        axes="xyz",
        tolerance=0.0001,
    )
    return explode, Cell.Prism(width=3, length=3, height=3)


def torus_animation(t):
    u_sides = int(t * 18) + 2
    torus = Cell.Torus(
        origin=Vertex.Origin(),
        majorRadius=0.5,
        minorRadius=0.125,
        uSides=u_sides,
        vSides=16,
        direction=[0, 0, 1],
        placement="bottom",
    )
    return torus, Cell.Prism(width=2, length=2, height=3)


def union_animation(t):
    v1 = Vertex.ByCoordinates(1, 0, 1)
    v2 = Vertex.ByCoordinates(1, 1, 1)

    c1 = CellComplex.Prism(
        origin=v1,
        length=2,
        width=2,
        height=3,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )
    c2 = CellComplex.Prism(
        origin=v2,
        length=2,
        width=2,
        height=2,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )

    cluster_C1_C2 = Cluster.ByTopologies(c1, c2)
    union_C1_C2 = Topology.Boolean(c1, c2, operation="union")

    if t < 0.5:
        return cluster_C1_C2, Cell.Prism(width=4, length=4, height=4)
    else:
        return union_C1_C2, Cell.Prism(width=4, length=4, height=4)


def intersect_animation(t):
    v1 = Vertex.ByCoordinates(1, 0, 1)
    v2 = Vertex.ByCoordinates(1, 1, 1)

    c1 = CellComplex.Prism(
        origin=v1,
        length=2,
        width=2,
        height=3,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )
    c2 = CellComplex.Prism(
        origin=v2,
        length=2,
        width=2,
        height=2,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )

    cluster_C1_C2 = Cluster.ByTopologies(c1, c2)
    intersect_C1_C2 = Topology.Boolean(c1, c2, operation="intersect")

    if t < 0.5:
        return cluster_C1_C2, Cell.Prism(width=4, length=4, height=4)
    else:
        return intersect_C1_C2, Cell.Prism(width=4, length=4, height=4)


def difference_animation(t):
    v1 = Vertex.ByCoordinates(1, 0, 1)
    v2 = Vertex.ByCoordinates(1, 1, 1)

    c1 = CellComplex.Prism(
        origin=v1,
        length=2,
        width=2,
        height=3,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )
    c2 = CellComplex.Prism(
        origin=v2,
        length=2,
        width=2,
        height=2,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )

    cluster_C1_C2 = Cluster.ByTopologies(c1, c2)
    difference_C1_C2 = Topology.Boolean(c1, c2, operation="difference")

    if t < 0.5:
        return cluster_C1_C2, Cell.Prism(width=4, length=4, height=4)
    else:
        return difference_C1_C2, Cell.Prism(width=4, length=4, height=4)


def symdif_animation(t):
    v1 = Vertex.ByCoordinates(1, 0, 1)
    v2 = Vertex.ByCoordinates(1, 1, 1)

    c1 = CellComplex.Prism(
        origin=v1,
        length=2,
        width=2,
        height=3,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )
    c2 = CellComplex.Prism(
        origin=v2,
        length=2,
        width=2,
        height=2,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )

    cluster_C1_C2 = Cluster.ByTopologies(c1, c2)
    symdif_C1_C2 = Topology.Boolean(c1, c2, operation="symdif")

    if t < 0.5:
        return cluster_C1_C2, Cell.Prism(width=4, length=4, height=4)
    else:
        return symdif_C1_C2, Cell.Prism(width=4, length=4, height=4)


def merge_animation(t):
    v1 = Vertex.ByCoordinates(1, 0, 1)
    v2 = Vertex.ByCoordinates(1, 1, 1)

    c1 = CellComplex.Prism(
        origin=v1,
        length=2,
        width=2,
        height=3,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )
    c2 = CellComplex.Prism(
        origin=v2,
        length=2,
        width=2,
        height=2,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )

    cluster_C1_C2 = Cluster.ByTopologies(c1, c2)
    merge_C1_C2 = Topology.Boolean(c1, c2, operation="merge")

    if t < 0.5:
        return cluster_C1_C2, Cell.Prism(width=4, length=4, height=4)
    else:
        return merge_C1_C2, Cell.Prism(width=4, length=4, height=4)


def slice_animation(t):
    v1 = Vertex.ByCoordinates(1, 0, 1)
    v2 = Vertex.ByCoordinates(1, 1, 1)

    c1 = CellComplex.Prism(
        origin=v1,
        length=2,
        width=2,
        height=3,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )
    c2 = CellComplex.Prism(
        origin=v2,
        length=2,
        width=2,
        height=2,
        vSides=4,
        uSides=4,
        wSides=4,
        placement="center",
    )

    cluster_C1_C2 = Cluster.ByTopologies(c1, c2)
    slice_C1_C2 = Topology.Boolean(c1, c2, operation="slice")

    if t < 0.5:
        return cluster_C1_C2, Cell.Prism(width=4, length=4, height=4)
    else:
        return slice_C1_C2, Cell.Prism(width=4, length=4, height=4)


def impose_animation(t):
    v1 = Vertex.ByCoordinates(1, 0, 1)
    v2 = Vertex.ByCoordinates(1, 1, 1)

    c1 = CellComplex.Prism(
        origin=v1,
        length=2,
        width=2,
        height=3,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )
    c2 = CellComplex.Prism(
        origin=v2,
        length=2,
        width=2,
        height=2,
        vSides=4,
        uSides=4,
        wSides=4,
        placement="center",
    )

    cluster_C1_C2 = Cluster.ByTopologies(c1, c2)
    impose_C1_C2 = Topology.Boolean(c1, c2, operation="impose")

    if t < 0.5:
        return cluster_C1_C2, Cell.Prism(width=4, length=4, height=4)
    else:
        return impose_C1_C2, Cell.Prism(width=4, length=4, height=4)


def imprint_animation(t):
    v1 = Vertex.ByCoordinates(1, 0, 1)
    v2 = Vertex.ByCoordinates(1, 1, 1)

    c1 = CellComplex.Prism(
        origin=v1,
        length=2,
        width=2,
        height=3,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )
    c2 = CellComplex.Prism(
        origin=v2,
        length=2,
        width=2,
        height=2,
        vSides=4,
        uSides=4,
        wSides=4,
        placement="center",
    )

    cluster_C1_C2 = Cluster.ByTopologies(c1, c2)
    imprint_C1_C2 = Topology.Boolean(c1, c2, operation="imprint")

    if t < 0.5:
        return cluster_C1_C2, Cell.Prism(width=4, length=4, height=4)
    else:
        return imprint_C1_C2, Cell.Prism(width=4, length=4, height=4)


def spiral_animation(t):
    turns = int(t * 9) + 1
    spiral = Wire.Spiral(
        origin=Vertex.Origin(),
        radiusA=0.1,
        radiusB=0.75,
        height=4,
        turns=turns,
        sides=36,
        clockwise=False,
        reverse=False,
        direction=[0, 0, 1],
        placement="center",
    )
    return spiral, Cell.Prism(width=4, length=4, height=4)


def ellipse_animation(t):
    width = t * 4 + 1
    ellipse = Wire.Ellipse(
        origin=Vertex.Origin(),
        inputMode=1,
        width=width,
        length=1,
        focalLength=0.866025,
        eccentricity=0.866025,
        majorAxisLength=1.0,
        minorAxisLength=0.5,
        sides=32,
        fromAngle=0.0,
        toAngle=360.0,
        close=True,
        direction=[0, 0, 1],
        placement="center",
        tolerance=0.0001,
    )
    return ellipse, Cell.Prism(width=4, length=4, height=4)


def capsule_animation(t):
    u_sides = int(t * 17) + 3
    capsule = Cell.Capsule(
        origin=Vertex.Origin(),
        radius=1,
        height=4,
        uSides=u_sides,
        vSidesEnds=8,
        vSidesMiddle=1,
        direction=[0, 0, 1],
        placement="center",
        tolerance=0.0001,
    )
    return capsule, Cell.Prism(width=4, length=4, height=4)


def graph_animation(t):
    sides = int(t * 4) + 1
    c = CellComplex.Prism(
        width=2, length=2, height=2, uSides=sides, vSides=sides, wSides=sides
    )
    graph = Graph.ByTopology(c)
    graph_top = Cluster.SelfMerge(Graph.Topology(graph))
    return c, Cell.Prism(width=4, length=4, height=4)


def triangulate_animation(t):
    sides = int(t * 4) + 1
    c = CellComplex.Prism(
        width=2, length=2, height=2, uSides=sides, vSides=sides, wSides=sides
    )
    triangulate_c = Topology.Triangulate(c, tolerance=0.0002)
    return triangulate_c, Cell.Prism(width=4, length=4, height=4)


def bounding_box_animation(t):
    v1 = Vertex.Origin()
    v2 = Vertex.ByCoordinates(0.5, 0.5, 0.5)
    c1 = CellComplex.Prism(
        origin=v1,
        length=1,
        width=1,
        height=1,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )
    c2 = CellComplex.Prism(
        origin=v2,
        length=1,
        width=1,
        height=1,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )
    cluster = Cluster.ByTopologies(c1, c2)

    angle = t * 180
    rotated_c = Topology.Rotate(cluster, origin=Vertex.Origin(), z=1, degree=angle)
    boundingBox = Topology.BoundingBox(rotated_c)

    return (rotated_c, boundingBox), Cell.Prism(width=4, length=4, height=4)


def bounding_box_of_rotated_cell_complexes(t):
    v1 = Vertex.Origin()
    v2 = Vertex.ByCoordinates(0.5, 0.5, 0.5)
    c1 = CellComplex.Prism(
        origin=v1,
        length=1,
        width=1,
        height=1,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )
    c2 = CellComplex.Prism(
        origin=v2,
        length=1,
        width=1,
        height=1,
        vSides=2,
        uSides=2,
        wSides=2,
        placement="center",
    )
    cluster = Cluster.ByTopologies(c1, c2)

    angle = t * 180
    rotated_c = Topology.Rotate(
        cluster,
        origin=Vertex.Origin(),
        axis=[0, 0, 1],
        angle=angle,
        angTolerance=0.1,
        tolerance=0.001,
    )
    boundingBox = Topology.BoundingBox(rotated_c)

    return boundingBox, Cell.Prism(width=4, length=4, height=4)


def star_animation(t):
    rays = int(t * 17) + 3
    star = Wire.Star(
        origin=Vertex.Origin(),
        radiusA=2,
        radiusB=0.5,
        rays=rays,
        direction=[0, 0, 1],
        placement="center",
        tolerance=0.0001,
    )
    return star, Cell.Prism(width=4, length=4, height=4)


def interpolate_animation(t):
    v1 = Vertex.Origin()
    v2 = Vertex.ByCoordinates(3, 0, 0)
    v3 = Vertex.ByCoordinates(0, 3, 0)
    v4 = Vertex.ByCoordinates(3, 3, 0)
    wire1 = Wire.ByVertices([v1, v2])
    wire2 = Wire.ByVertices([v3, v4])

    n = int(t * 10)
    interpolate = Wire.Interpolate(
        [wire1, wire2], n=n, outputType="default", mapping="default", tolerance=0.0001
    )

    return interpolate, Cell.Prism(width=4, length=4, height=4)


def pie_animation(t):
    sides = int(t * 27) + 3
    pie = Shell.Pie(
        origin=Vertex.Origin(),
        radiusA=2,
        radiusB=0.0,
        sides=sides,
        rings=1,
        fromAngle=0.0,
        toAngle=360.0,
        direction=[0, 0, 1],
        placement="center",
        tolerance=0.0001,
    )
    return pie, Cell.Prism(width=4, length=4, height=4)


def bisect_animation(t):
    v1 = Vertex.Origin()
    v2 = Vertex.ByCoordinates(4, 0, 0)
    v3 = Vertex.ByCoordinates(4, t * 4, 0)
    edge1 = Edge.ByVertices([v1, v2])
    edge2 = Edge.ByVertices([v1, v3])
    bisect = Edge.Bisect(edge1, edge2, length=3.0, placement=0, tolerance=0.0001)
    cluster = Cluster.ByTopologies([edge1, edge2, bisect])
    return cluster, Cell.Prism(width=8, length=8, height=8)


def bounding_box_for_a_rotated_triangle_animation(t):
    v1 = Vertex.Origin()
    v2 = Vertex.ByCoordinates(1, 3, 0)
    v3 = Vertex.ByCoordinates(2, 3, 0)
    face = Face.ByVertices([v1, v2, v3])

    angle = t * 90
    rotate_face = Topology.Rotate(
        face, origin=Vertex.Origin(), angle=angle, angTolerance=0.1, tolerance=0.001
    )
    boundingRectangle = Face.BoundingRectangle(
        rotate_face, optimize=0, tolerance=0.0001
    )

    return boundingRectangle, Cell.Prism(width=6, length=6, height=6)


def roof_animation(t):
    v1 = Vertex.Origin()
    v2 = Vertex.ByCoordinates(3, 0, 0)
    v3 = Vertex.ByCoordinates(0, 3, 0)
    face = Face.ByVertices([v1, v2, v3])

    angle = t * 40 + 5
    roof = Cell.Roof(face, angle=angle, epsilon=0.01, tolerance=0.001)

    return roof, Cell.Prism(width=6, length=6, height=6)


animation_functions = {
    "Twist": twist_animation,
    "Hyperboloid": hyperboloid_animation,
    "Cone": cone_animation,
    "Rotated-Cell-Complex": rotated_cell_complex_animation,
    "Translated-Cell-Complex": translated_cell_complex_animation,
    "Taper": taper_animation,
    "Scale": scale_animation,
    "Hyperbolic-Paraboloid": hyperbolic_paraboloid_animation,
    "Cell-Complex": cell_complex_animation,
    "Explode": explode_animation,
    "Torus": torus_animation,
    "Union": union_animation,
    "Intersect": intersect_animation,
    "Difference": difference_animation,
    "Symdif": symdif_animation,
    "Merge": merge_animation,
    "Slice": slice_animation,
    "Impose": impose_animation,
    "Imprint": imprint_animation,
    "Spiral": spiral_animation,
    "Ellipse": ellipse_animation,
    "Capsule": capsule_animation,
    "Graph": graph_animation,
    "Triangulate": triangulate_animation,
    "Bounding-Box-Of-Rotated-Cell-Complexes": bounding_box_of_rotated_cell_complexes,
    "Star": star_animation,
    "Interpolate": interpolate_animation,
    "Pie": pie_animation,
    "Bisect": bisect_animation,
    "Bounding-Box-For-A-Rotated-Triangle": bounding_box_for_a_rotated_triangle_animation,
    "Roof": roof_animation,
}
