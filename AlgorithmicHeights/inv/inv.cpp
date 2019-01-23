//
//  inv.cpp
//
//  Created by Mateusz Stompór on 22/01/2019.
//  Copyright © 2019 Mateusz Stompór. All rights reserved.
//

// Compilation
// $ g++ -o inv.x inv.cpp -std=c++14

// Running
// $ ./inv.x path_to_dataset

#include <iostream>
#include <memory>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>

auto bubble_sort(std::vector<int> & sequence) -> unsigned long long {
    unsigned long long swaps_amount = 0;
    for(std::size_t i{0}; i<sequence.size(); ++i) {
        std::cout<<i+1<<"/"<<sequence.size()<<'\n';
        for(std::size_t j{1}; j<sequence.size(); ++j) {
            if(sequence[j] < sequence[j-1]) {
                std::iter_swap(sequence.begin() + j, sequence.begin() + j - 1);
                ++swaps_amount;
            }
        }
    }
    return swaps_amount;
}

auto parse(std::ifstream & input) -> std::tuple<int, std::vector<int>> {
    std::string count_literal;
    std::string sequence_literal;
    std::getline(input, count_literal);
    std::getline(input, sequence_literal);
    auto count = std::stoi(count_literal);
    std::vector<int> numbers;
    std::istringstream stream(sequence_literal);
    int number;
    while(stream >> number) {
        numbers.push_back(number);
    }
    return std::make_tuple(count, numbers);
}
        
auto main(int argc, char ** argv) -> int {
    if(argc != 2) {
        std::cerr<<"Wrong invocation!"<<'\n';
        std::cerr<<"Pass a path to the dataset as an argument"<<'\n';
    }
    std::ifstream input;
    input.open(argv[1]);
    auto data = parse(input);
    input.close();
    auto size = std::get<0>(data);
    auto numbers = std::get<1>(data);
    numbers.resize(size);
    std::cout<<bubble_sort(numbers)<<'\n';
}
