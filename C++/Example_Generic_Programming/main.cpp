#include <iostream>


template <typename TypeParameter>
struct LinkedList {
    TypeParameter head;
    LinkedList<TypeParameter> * tail;
};


struct IntOps {
    static int initial() { return 0;}
    static int bin(int a, int b) { return a+b;}
};

template <typename TypeParameter, typename Ops>
TypeParameter fold(LinkedList<TypeParameter> *ll)
{
    TypeParameter acc = Ops::initial();
    LinkedList<TypeParameter> * m = ll;
    while(m)
    {
        acc = Ops::bin(acc, m->head);
        m = m->tail;
    }
    return acc;
}

int main() {
    LinkedList<int> x {3, nullptr};
    LinkedList<int> y {2, &x};

    auto sum = fold<int, IntOps>;


    std::cout << sum(&y) << std::endl;
    return 0;
}