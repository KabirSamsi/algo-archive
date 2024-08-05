#include <iostream>

enum color {red, green, purple};
enum pattern {empty, striped, full};
enum shape {diamond, squiggle, oval};

struct card {
    int count;
    color cl;
    pattern pat;
    shape sp;
};