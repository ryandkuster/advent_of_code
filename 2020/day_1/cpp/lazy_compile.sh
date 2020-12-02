#compile and run stdin from command line providing file ending in .cpp
cpp_file=$1

echo 'compiling' $cpp_file

/usr/bin/g++ $cpp_file -o ${cpp_file%%.cpp} && ./${cpp_file%%.cpp}
