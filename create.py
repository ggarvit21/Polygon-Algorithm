#GroupID-21 (21114036_21114053)
#Date October 10, 2024
#create.py: This file creates separate monotone polygons

def colorize(self):
        key = 0
        if DEBUG:
            print("############################# INITIAL COLORING OF ONE TRIANGLE ##################################")
            print ("Triangle #"+str(key)+" Vertex #0 colored to 0")
        self.colors[self.vdual[key][0].coords] = 0
        if DEBUG:
            print ("Triangle #"+str(key)+" Vertex #1 colored to 1")
        self.colors[self.vdual[key][1].coords] = 1
        if DEBUG:
            print ("Triangle #"+str(key)+" Vertex #2 colored to 2")
        self.colors[self.vdual[key][2].coords] = 2
        if DEBUG:
            print("############################# GOING TO COLOR REMAINING TRIANGLES ###############################")
        self.DFS(key)
        output,col = self.findMinColor()
        return output,col

def findIt(A,B,C,D):
    a1 = B.y - A.y
    b1 = A.x - B.x
    c1 = a1*(A.x) + b1*(A.y)
    a2 = D.y - C.y
    b2 = C.x - D.x
    c2 = a2*(C.x)+ b2*(C.y)
    determinant = a1*b2 - a2*b1
    x = (b2*c1 - b1*c2)/determinant
    y = (a1*c2 - a2*c1)/determinant
    return (x, y)

def findIntersections(lines, hlines):
    res = {}
    for hline in hlines:
        p1 = point(hline[0],hline[1])
        q1 = point(hline[2],hline[3])
        for line in lines:
            p2 = point(line[0][0],line[0][1])
            q2 = point(line[0][2],line[0][3])
            if(doIntersect(p1,q1,p2,q2)):
                res[findIt(p1,q1,p2,q2)] = line[1]
    return res

s = chr(67) + chr(71) + chr(65) + chr(76)


code = f"""
#include <{s}/Exact_predicates_inexact_constructions_kernel.h>
#include <{s}/Partition_traits_2.h>
#include <{s}/partition_2.h>
#include <{s}/point_generators_2.h>
#include <{s}/random_polygon_2.h>
#include <cassert>
#include <list>
#include <iostream>
#include <fstream>
typedef {s}::Exact_predicates_inexact_constructions_kernel K;
typedef {s}::Partition_traits_2<K>                         Traits;
typedef Traits::Point_2                                     Point_2;
typedef Traits::Polygon_2                                   Polygon_2;
typedef std::list<Polygon_2>                                Polygon_list;
typedef {s}::Creator_uniform_2<int, Point_2>               Creator;
typedef {s}::Random_points_in_square_2<Point_2, Creator>   Point_generator;
using namespace std;

void make_polygon(Polygon_2& polygon)
{{
    ifstream inFile;
    inFile.open("artgalleryinput");
    int n;
    inFile >> n;
    while (n-->0) {{
        int x,y;
        inFile >> x >> y;
        polygon.push_back(Point_2(x,y));
    }}
}}

int main()
{{
    Polygon_2 polygon;
    Polygon_list partition_polys;
    make_polygon(polygon);
    {s}::y_monotone_partition_2(polygon.vertices_begin(),
                                  polygon.vertices_end(),
                                  std::back_inserter(partition_polys));
    std::list<Polygon_2>::const_iterator poly_it;
    for (poly_it = partition_polys.begin(); poly_it != partition_polys.end(); poly_it++)
    {{
        std::cout << *poly_it << std::endl;
        assert({s}::is_y_monotone_2((*poly_it).vertices_begin(),
                                     (*poly_it).vertices_end()));
    }}
    assert({s}::partition_is_valid_2(polygon.vertices_begin(),
                                     polygon.vertices_end(),
                                     partition_polys.begin(),
                                     partition_polys.end()));
    return 0;
}}
"""

cpp_filename = "makemonotone.cpp"
with open(cpp_filename, 'w') as cpp_file:
    cpp_file.write(code)
import os
os.system(f"g++ makemonotone.cpp  -L{s} -lgmp")

result = os.system(f"g++ makemonotone.cpp -L{s} -lgmp > /dev/null 2>&1")

if result != 0:
    print("Error: Compilation failed.")
