#include <cmath> 
#include <iostream>

using namespace std;

//left image
//const double alpha = 0.2;
//const double beta = 0.9991;

//right image
const double alpha = 0.2;
const double beta = 0.9991;

//number of points
const int N = 100000;


int main(void) {
	
   int i;	
   double x_vals[N+1];
   double y_vals[N+1];
   
   x_vals[0] = 0.0;
   y_vals[0] = -3.0;
   
   //cout << x_vals[0] << " " << y_vals[0] << endl;
   
   for (i=0;i<N;i++) {
	   //cout << x_vals[i] << " " << y_vals[i] << endl;
	   x_vals[i+1] = 1.0-alpha*x_vals[i]*x_vals[i] + y_vals[i];
	   y_vals[i+1] = beta*x_vals[i];
   };

   cout << "x" << " " << "y" << endl; 
   
   for (i=0; i<=N; i++) {
      cout << x_vals[i] << " " << y_vals[i] << endl;
   };

   return 0;
   
};
   
   