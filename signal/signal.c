/*
* File: signal.c
* Author: Ruby Abrams
* Purpose: Going to try generate a continuous signal
*				and then do some processing on it.
*/

#include <stdio.h>
#include <math.h>
#include <gsl/gsl_sf_trig.h>
#define PI 3.141592653589793238462643383279

unsigned long factorial(unsigned long f)
{
    if ( f == 0 )
        return 1;
    return(f * factorial(f - 1));
}

// a continuous function
// to be defined: approximate sin(x)
double sine(double t){
		float a, k; //, sine;
		k = 3;
		a = 2*PI*k*t;
		// sine = a - pow(a,3)/factorial(3) + pow(a,5)/factorial(5) - pow(a,7)/factorial(7);

		return gsl_sf_sin(a);
}

int main()
{
	int n;
	float t, tot_time;
		n = 0;
		tot_time = 10000;
		while(n < tot_time){
			t = ((float)n)/tot_time;
			printf("%.5f,%.5f\n", t, sine(t));
			n++;
		}
		return 0;
}
