// TSP_cities map
#include <iostream>
#include <cstdlib>
#include<string>
using namespace std;
int main(void)
{
	int min = 10;
	int max = 90;
	int route_Cities[8][8];
	int x = rand() % (max - min + 1) + min;
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			if(i<j)
				route_Cities[i][j] = rand() % (max - min + 1) + min;
			if (i == j)
				route_Cities[i][j] = 0;
			route_Cities[j][i] = route_Cities[i][j];
			cout << route_Cities[i][j] << " ";
			
		}
		cout << endl;
	}

	cout << endl;

	system("pause");
	return 0;
}
