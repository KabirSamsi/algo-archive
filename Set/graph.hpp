#include <iostream>
#include <vector>
#include <utility>
#include "card.hpp"

using namespace std;

enum edge {
    sameColor, sameNumber, sameSize, sameShape, 
    diffColor, diffNumber, diffSize, diffShape
};

struct node {
    card value;
    vector<pair<edge, card*>> edges;
};