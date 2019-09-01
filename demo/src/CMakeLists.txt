# source

file(GLOB MY_SRCS *.c *.cpp *.hpp)

message(STATUS ${MY_SRCS})

include_directories(${PUBLIC_INCLUDE_DIR})

# demo - target

add_library(${CMAKE_PROJECT_NAME} SHARED ${MY_SRCS})
set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES OUTPUT_NAME ${CMAKE_PROJECT_NAME})
set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES LINKER_LANGUAGE CXX)
# target_link_libraries(${CMAKE_PROJECT_NAME} ${OPENSSL_LIBRARIES})

# demo - install

INSTALL(TARGETS ${CMAKE_PROJECT_NAME} DESTINATION lib/)

