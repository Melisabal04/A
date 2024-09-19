import math
points = [(2, 3), (4, 5), (7, 8), (0, 0)]
def euclideanDistance(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1]**2))

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)

print("Tüm mesafeler:", distances)
print("Minimum mesafe:", min_distance)
