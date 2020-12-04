#include <algorithm>
#include <iostream>
#include <list>
int main() {
	std::list<int> my_list = { 12, 5, 10, 9 };

	for (int x : my_list) {
		std::cout << x << '\n';
	}
}
