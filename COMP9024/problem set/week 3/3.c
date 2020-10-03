/* Makes an array of 10 integers and returns a pointer to it */

int *makeArrayOfInts() {
   int *arr = malloc(sizeof(int) * 10);
   assert(arr != NULL);  // always check that memory allocation was successful
   int i;
   for (i=0; i<10; i++) {
      arr[i] = i;
   }
   return arr;           // this is fine because the array itself will live on
}
