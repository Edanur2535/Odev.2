package algorithm;
import java.util.Scanner;

public class array {

	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int[] nums= {1,4,8,10,14,19};
		int target;
		System.out.println("enter a target:");
		target=scan.nextInt();
		for(int i=0;i<nums.length;i++) {
			if(nums[i]>target){
				System.out.println("Index:"+i);
				break;
			}
			else if(nums[i]==target) {
				System.out.println("Index:"+(i+1));
				break;
			}
		}
        	     
		while(nums[nums.length-1]<target) {
			System.out.println("Index:"+nums.length);
			break;
		}
		

	}

}
