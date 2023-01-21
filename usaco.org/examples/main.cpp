#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <vector>
#include <algorithm>

/* 
   instructions to compile and run code:
   
   ssh to dev2 (PuTTY)

   ls
   cd usaco
   cd examples
   c++ --std=c++17 main.cpp to compile file
   output stored in a.out

   ./a.out to print the output

*/

void sort_descending(std::vector<int>& vec)
{
   sort(vec.begin(), vec.end(), std::greater<int>());
}


 
int main(int argc, char *argv[])
{
   std::vector<int> a;

   for (auto i=0; i<10; ++i)
      a.emplace_back(i);

   for (auto it : a) {
    	std::cout << it << '\n';
   }


   sort_descending(a);


   std::cout << " --------------------------" << std::endl;
   for (auto it : a) {
    	std::cout << it << '\n';
   }


   // sort reverse
   
   return 0;
 
}
