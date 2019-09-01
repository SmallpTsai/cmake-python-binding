# source
file(GLOB MY_INCS *.hpp)

# install header
INSTALL(FILES ${MY_INCS}
        DESTINATION "include/${CMAKE_PROJECT_NAME}"
        )
