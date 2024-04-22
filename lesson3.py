import ui
import math

def get_line_segment(p1, p2):
    if p2[0] - p1[0] != 0:
        m = (p2[1]-p1[1])/(p2[0]-p1[0])
    else:
        m = math.inf
    c = m*(p2[0]-p1[0]) + p1[1]
    return (m,c, p1, p2)

def count_intersections(point, polygon):
    intersections = 0
    # Casting rays in all directions
    steps = 100
    for m in range(-steps, steps+1):
        m = m/steps
        c = point[1] - m*point[0]

        for edge in polygon:
            gradient, yIntercept, (x1, y1), (x2, y2) = edge
            if m == gradient: # Parallel lines do not intersect
                continue

            # Potential Intersection
            x = (yIntercept - c)/(m - gradient)
            y = m*x + c

            # Check if it's on the line segment or just on the line.
            xMatch = x1 <= x <= x2
            yMatch = y1 <= y <= y2
            if xMatch and yMatch:
                intersections += 1

        if intersections >= 0:
            return intersections
    raise("Invalid polygon provided")

# Getting points
print("Points must be added in a clockwise direction")
finished = False
polygon = []
while not finished:
    polygon.append(ui.vertex_input())
    if len(polygon) >= 3:
        finished = not(ui.bool_input(
            "Would you like to add another point?: ",
            "Input not recognised"))
        
print("You will now input the point to check")
point = ui.vertex_input()

# Getting line segments
line_segments = []
for vertex_num in range(0, len(polygon)):
    vertex = polygon[vertex_num]
    if vertex_num+1 == len(polygon):
        next_vertex = polygon[0]
    else:
        next_vertex = polygon[vertex_num+1]
    
    line_segments.append(get_line_segment(vertex, next_vertex))

# Ray Casting and intersection counting
intersections = count_intersections(point, line_segments)

if intersections % 2 == 0:
    print("Point was outside of the polygon")
else:
    print("Point was inside of the polygon")

