
set(PYTARGET_NAME "lib${CMAKE_PROJECT_NAME}")

# source

include_directories(${PUBLIC_INCLUDE_DIR})

# python binding

find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})
find_package(PythonLibs 3)
include_directories(${PYTHON_INCLUDE_PATH})

set(CMAKE_SWIG_FLAGS -threads -c++ -O -I${PUBLIC_INCLUDE_DIR})
if(CMAKE_BUILD_TYPE EQUAL "Debug") 
    set(CMAKE_SWIG_FLAGS "${CMAKE_SWIG_FLAGS} -DDEBUG")
endif()

set(CMAKE_SWIG_OUTDIR ${PYSRC_DIR}/${CMAKE_PROJECT_NAME})
set_property(SOURCE swig.i 
    PROPERTY CPLUSPLUS ON
)
set_source_files_properties( ${swig_generated_file_fullname} 
    PROPERTIES COMPILE_FLAGS "-fPIC"
)
swig_add_library(${PYTARGET_NAME} 
    LANGUAGE python 
    SOURCES swig.i
)
set_target_properties(${SWIG_MODULE_${PYTARGET_NAME}_REAL_NAME} PROPERTIES 
    LIBRARY_OUTPUT_DIRECTORY ${PYSRC_DIR}/${CMAKE_PROJECT_NAME}  # generate .so to pysrc/${CMAKE_PROJECT_NAME}
)
swig_link_libraries(${PYTARGET_NAME} ${CMAKE_PROJECT_NAME} ${PYTHON_LIBRARIES})

# install

INSTALL(CODE
    "execute_process(
        COMMAND pip3 install .
        WORKING_DIRECTORY ${PYSRC_DIR}
    )"
)