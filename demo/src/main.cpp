#include "demo.hpp"

namespace demo { 

    std::string hello_echo(
        const std::string& echo
    ) {
        return std::string("Hello~") + echo;
    }

    std::string hello_echo_only_in_cplusplus(
        const std::string& echo
    ) {
        return std::string("C++ Hello~") + echo;
    }

}