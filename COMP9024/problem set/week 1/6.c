int max(int a, int b, int c) {
   int d = a * (a >= b) + b * (a < b);   // d is max of a and b
   return  c * (c >= d) + d * (c < d);   // return max of c and d
}
