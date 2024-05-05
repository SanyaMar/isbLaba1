#include <iostream>
#include <random>

void generate_cpp(size_t bits) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(0, 1);

    for (size_t i = 0; i < bits; ++i) {
        std::cout << dis(gen);
    }

    std::cout << std::endl;
}

int main() {
    int BITS=128;
    generate_cpp(BITS);

    return 0;
}
