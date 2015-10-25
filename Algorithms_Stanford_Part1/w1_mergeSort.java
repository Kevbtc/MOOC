/*
	mergeSort.
	10/15/2015. No idea how to implement it...
	10/24/2015.
*/

// Array 初始化用大括号
// int[] src = {1, 3, 2, 4, 7, 5, 6, 8};

import java.util.Arrays;

public class mergeSort{

	public static int[] mergeSort(int[] src){

		if (src.length <= 1)
			return src;

		int arrayLength = src.length;
		int[] a = new int[arrayLength/2];
		int[] b = new int[arrayLength - arrayLength/2];
		for (int i = 0; i < arrayLength; i++){
			if(i<arrayLength/2)
				a[i] = src[i];
			else
				b[i - arrayLength/2] = src[i];
		}
		
		int[] n = mergeSort(a);
		int[] m = mergeSort(b);
		return merge(n, m);
	}

	private static int[] merge(int[] a, int[] b){ // Done.
		int aLength = a.length;
		int bLength = b.length;
		int k = a.length + b.length;
		int[] dest = new int[k];
		int m = 0; int n = 0;
		for (int i = 0; i < k; i++){
			if (m >= aLength)
				dest[i] = b[n++];
			else if (n >= bLength)
				dest[i] = a[m++];
			else if (a[m] < b[n])
				dest[i] = a[m++];
			else
				dest[i] = b[n++];
		}
		return dest;
	}


	public static void main(String[] args){
		/* test merge
		int[] src = {1, 3, 6, 8, 10, 10, 20};
		int[] src2 = {2, 3, 8, 10};
		
		int[] merged = merge(src, src2);

		for (int i=0; i<merged.length; i++){
			System.out.print(merged[i]+" ");
		}
		System.out.print("\n");
		*/

		int[] src = {1100, 2134, 2, 3, 54, 0, -10, -2, 90, 23, 1, 2, 6};
		int[] result = mergeSort(src);

		System.out.println(Arrays.toString(result));

	}
}