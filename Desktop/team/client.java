package soket;

import java.net.*;
import java.util.Scanner;
import java.io.*;

public class client {

	public static void main(String[] args) throws IOException {
		
		
		Socket client=new Socket("localhost",1618);
		
		InputStreamReader edn=new InputStreamReader(client.getInputStream());
		BufferedReader bf=new BufferedReader(edn);
		
		PrintWriter print=new PrintWriter(client.getOutputStream());
		
		Scanner input=new Scanner(System.in);
		System.out.println("Send message:");
		
		print.println(input.nextLine());
		print.flush();
		client.close();
		bf.close();
		input.close();
		
		
		
		
		
		

	}

}
