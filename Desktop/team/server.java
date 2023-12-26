package soket;

import java.net.*;
import java.util.Scanner;
import java.io.*;


public class server {

	public static void main(String[] args)throws IOException {
		
		ServerSocket server=new ServerSocket(1618);
		Socket client = server.accept();
		
		InputStreamReader in=new InputStreamReader(client.getInputStream());
		BufferedReader br=new BufferedReader(in);
		
		PrintWriter print=new PrintWriter(client.getOutputStream());
		
		String veri=br.readLine();
        System.out.println("Gelen veri:"+veri);
        
        Scanner scan=new Scanner(System.in);
        
        String message=scan.nextLine();
        System.out.println("Send message:");
        
        print.println(message);
        print.flush();
        scan.close();
        server.close();
		
		

	}

}
