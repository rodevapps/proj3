import java.util.Arrays;

class Simple{
 public static int findLowestInt(int[] A) {
  if(A.length == 0)
   return 1;
  else if(A.length == 1 && A[0] != 1)
   return 1;
  else if(A.length == 1 && A[0] == 1)
   return 2;

  Arrays.sort(A);

  if(A[0] > 1 || A[A.length - 1] < 1)
   return 1;

  if (A[A.length - 1] == 1)
   return 2;

  for(int i = 1; i < A.length; i++) {
   if (A[i] - A[i - 1] > 1) {
    if (A[i - 1] + 1 > 0)
     return A[i - 1] + 1;
    else if (A[i] > 1)
     return 1;
   }
  }

  return A[A.length - 1] + 1;
 }

 public static void main(String args[]){
  int[] arr = {-1,1,2,3,40};

  System.out.println(findLowestInt(arr));
 }
}
