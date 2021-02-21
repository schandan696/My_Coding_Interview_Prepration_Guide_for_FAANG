// You have been given an integer array/list(ARR) of size N which contains numbers
// from 0 to (N - 2). Each number is present at least once. That is, if N = 5,
// the array/list constitutes values ranging from 0 to 3, and among these, there
// is a single integer value that is present twice. You need to find and return
// that duplicate number present in the array.
// Note :
// Duplicate number is always present in the given array/list.



public class DuplicateInArray{	

	public static int duplicate(int[] arr){  
      	int n = arr.length-2;
      	int sum1 = n*(n+1)/2;
      	int sum=0;
      	for(int i = 0; i < arr.length; i++){
          	sum=sum+arr[i];
        }
      
	return sum-sum1;
	}
}