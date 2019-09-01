#pragma once

#include <string>

namespace demo { 

    std::string hello_echo(
        const std::string& echo
    );

#ifndef SWIG    /* following is hidden from python binding */

    /* only in c++ library */
    std::string hello_echo_only_in_cplusplus(
        const std::string& echo
    );

#endif
}

