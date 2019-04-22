#include <fstream>
#include <iostream>
using namespace std;

void euler(double x_0, double y_0, double x_f, double h, string filename);
void implicit(double x_0, double y_0, double x_f, double h, string filename);

int main () {
  string filename;
  filename = "euler_001.dat";
  double x_0 = 0.0;
  double y_0 = 1.0;
  double x_f = 4.0;
  double h = 0.01;
  euler(x_0,y_0,x_f,h,filename);
  filename = "euler_01.dat";
  h = 0.1;
  euler(x_0,y_0,x_f,h,filename);
  filename = "euler_1.dat";
  h = 1.0;
  euler(x_0,y_0,x_f,h,filename);
    
  filename = "implicit_001.dat";
  h = 0.01;
  implicit(x_0,y_0,x_f,h,filename);
  filename = "implicit_01.dat";
  h = 0.1;
  implicit(x_0,y_0,x_f,h,filename);
  filename = "implicit_1.dat";
  h = 1.0;
  implicit(x_0,y_0,x_f,h,filename);
  return 0;
}
void euler(double x_0, double y_0, double x_f, double h, string filename){
  ofstream outfile;
  outfile.open(filename);

  cout << "Escribiendo euler en " << filename << endl; 
  
    double x=x_0;
    double y=y_0;
    int n=(x_f-x_0)/h;    
    int i;
    for(i=0;i<(n+1);i++){
        x=x_0+(i*h);
        outfile << x <<' '<< y << endl;
        y=y-(h*y);
    }
    outfile.close();
    cout << "Terminamos en " << filename << endl; 
}
void implicit(double x_0, double y_0, double x_f, double h, string filename){
  ofstream outfile;
  outfile.open(filename);

  cout << "Escribiendo implicit en " << filename << endl; 
  
    double x=x_0;
    double y=y_0;
    int n=(x_f-x_0)/h;    
    int i;
    for(i=0;i<(n+1);i++){
        x=x_0+(i*h);
        outfile << x <<' '<< y << endl;
        y=y/(1+h);
    }
    outfile.close();
    cout << "Terminamos en " << filename << endl; 
}