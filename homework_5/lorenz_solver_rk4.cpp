// Integrating equation of motion with 1st and 2nd order schemes

#include <cmath> // for sqrt()
#include <iostream>
#include <iomanip>

using namespace std;

//original parameters given by Lorenz to generate chaos
const double sigma = 10.0;
const double beta = 8.0/3.0;
const double rho = 28.0;

//rk45 use
const int tmax = 45000; // number of time steps
const double dt = 0.001; // time step to make x range from 0 to 4 seconds


// Take one time step using the Euler method
void computeF(double x, double y, double z, double &dx, double &dy,double &dz)
{
   dx = sigma*(y-x);
   dy = x*(rho-z)-y;
   dz = x*y-beta*z;

};

int main(void)
{
   double xRK4[tmax + 1], yRK4[tmax + 1], zRK4[tmax+1];
   double dx, dy, dz, xtmp, ytmp, ztmp;
   double dx1, dy1, dz1, dx2, dy2, dz2, dx3, dy3, dz3, dx4, dy4, dz4;
   int t;

// initial condition   
   xRK4[0] = 1.000;
   yRK4[0] = 1.000;
   zRK4[0] = 1.000;

   cout << "x" << " " << "y" << " " << "z" << endl;
   cout << xRK4[0] << " " << yRK4[0] << " " << zRK4[0] << endl;
// integrate in time
   for(t = 1; t <= tmax+1; t++) {
    
     // RK4
     computeF(xRK4[t-1], yRK4[t-1], zRK4[t-1], dx1, dy1, dz1);
     xtmp  = xRK4[t-1]  + 0.5*dt*dx1;
     ytmp  = yRK4[t-1]  + 0.5*dt*dy1;
     ztmp = zRK4[t-1] + 0.5*dt*dz1;
	 
     computeF(xtmp, ytmp, ztmp, dx2, dy2, dz2); // f2
     xtmp  = xRK4[t-1]  + 0.5*dt*dx2;
     ytmp  = yRK4[t-1]  + 0.5*dt*dy2;
     ztmp = zRK4[t-1] + 0.5*dt*dz2;
	 
     computeF(xtmp, ytmp, ztmp, dx3, dy3, dz3); // f3
     xtmp  = xRK4[t-1]  + dt*dx3;
     ytmp  = yRK4[t-1]  + dt*dy3;
     ztmp = zRK4[t-1] + dt*dz3;
	 
     computeF(xtmp, ytmp, ztmp, dx4, dy4, dz4); //f 4
     xRK4[t]  = xRK4[t-1]  + dt/6.0*(dx1 + 2.0*dx2 + 2.0*dx3 + dx4);
     yRK4[t]  = yRK4[t-1]  + dt/6.0*(dy1 + 2.0*dy2 + 2.0*dy3 + dy4);
     zRK4[t]  = zRK4[t-1]  + dt/6.0*(dz1 + 2.0*dz2 + 2.0*dz3 + dz4);
	 
	 //print state coordinates
	 cout << xRK4[t] << " " << yRK4[t] << " " << zRK4[t] << endl;
     
   };
   return 0;
};
