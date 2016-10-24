#include <cmath> // for sqrt()
#include <iostream>
#include <iomanip>

using namespace std;

//part a
const int tmax = 1000; // number of time steps
const double dt = 0.1; // time step to make x range from 0 to 10
const double e_tol = 1.0e-03;

const double r_T = 0.05;
const double r = 0.007;
const double c = 0.52;
const double g = 9.81;
const double y_low = 0.025;
const double y_high = 0.1;
const double q_in = 5.0e-05;




double f_x(long double x, long double y, double s) {
   double ans;
   if (y<0) {
      ans = q_in/(M_PI*pow(r_T,2));
   }
   else {
	  ans = (q_in-(s*M_PI*pow(r,2)*c*sqrt(2.0*g*y)))/(M_PI*pow(r_T,2));
   }
   return ans;
};   
  
double RK45(double h, long double x, long double y, long double &y_ans, long double &z_ans, long double &rel_e, double s) {
   //y = y0;
   double k1,k2,k3,k4,k5,k6; 
   k1 = h*f_x(x,y,s);
   k2 = h*f_x((x+h/4.0),(y+k1/4.0),s);
   k3 = h*f_x((x + 3.0*h/4.0),(y+ 3*k1/32.0 + 9*k2/32.0),s);
   k4 = h*f_x((x + 12.0*h/13.0),(y+ 1932.0*k1/2197.0 + 7200.0*k2/2197.0 + 7296.0*k3/2197.0),s);
   k5 = h*f_x((x+h),(y+ 439.0*k1/216.0 - 8.0*k2 - 3680.0*k3/513.0 - 845.0*k4/4104.0 ),s);
   k6 = h*f_x((x+h/2.0),(y - 8.0*k1/27.0 + 2.0*k2 - 3544.0*k3/2565.0 - 1859.0*k4/4104.0 - 11.0*k5/40.0),s);
   
   y_ans = y + 25.0*k1/216.0 + 1408.0*k3/2565.0 + 2197.0*k4/4104.0 - k5/5.0;
   z_ans = y + 16.0*k1/135.0 + 6656.0*k3/12825.0 + 28561.0*k4/56430.0 - 9.0*k5/50.0 + 2.0*k6/55.0;
   
   rel_e  = abs(z_ans-y_ans)/z_ans;
};    
int main(void)
{
   long double xRK45[tmax+1], yRK45[tmax+1], yRK4[tmax+1], yRK5[tmax+1], q_record[tmax+1];
   //initial condition 
  
   //part a 
   xRK45[0] = 0.0;
   yRK45[0] = 0.0;
   //part b
   yRK4[0] = 0.0;
   yRK5[0] = 0.0;
   int i;
   long double y_i, z_i, e_rel;
   long double q = 1.0;
   
   for (i=1; i<=tmax; i++) {
	   xRK45[i] = xRK45[i-1] + dt;
   };
   double s_use = 0.0;
   cout << "x" << " " << "y" << " " << "yRK4" << " " << "yRK5" << " " << "h" << endl;
   for (i=0;i<=tmax;i++) {
      RK45(q*dt,xRK45[i], yRK45[i],y_i, z_i, e_rel, s_use);
	  //cout << "e_rel" << " " << e_rel << endl;
      q = pow(e_tol*dt/(2.0*abs(z_i-y_i)), (1.0/4.0));
	 
	  //cout << "q" << " " << q << " " << "h" << " " << q*dt << endl;
	  
	  //part b
      yRK4[i+1] = y_i;
	  yRK5[i+1] = z_i;
     
      while (e_rel > e_tol ) { 
	     
         RK45(q*dt,xRK45[i], yRK45[i],y_i, z_i, e_rel,s_use);
		 q = pow(e_tol*q*dt/(2.0*abs(z_i-y_i)), 0.25);

	  }	 
	  cout << "q" << " " << q << endl;
      if (q>2) {
         q=2.0;
	  }
	  yRK45[i+1] = y_i; 
	  if ((y_i < y_high or y_i < y_low) and yRK45[i+1] > yRK45[i]) {
         s_use=0.0;
	  }
      else {
         s_use=1.0;
      }		
	  //part c
      q_record[i] = q*dt;
	     
   }; 
   
   for (i=0; i<=tmax;i++) {
       cout << xRK45[i] << " " << yRK45[i] << " " << yRK4[i] << " " << yRK5[i] << " " << dt*q_record[i] <<endl; 
   };  

   
      
   return 0;
};  
