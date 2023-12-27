package multipleC;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.InetAddress;
import java.net.Socket;
import java.util.Scanner;

public class MultiClient {

	public static void main(String[] args) {
		try {
			Scanner sc=new Scanner(System.in);
			InetAddress ip=InetAddress.getByName("localhost");
			Socket s=new Socket(ip,2345);
			
			DataInputStream dis=new DataInputStream(s.getInputStream());
			DataOutputStream dos=new DataOutputStream(s.getOutputStream());
			
			while(true) {
				System.out.println(dis.readUTF());
				String tosand=sc.nextLine();
				dos.writeUTF(tosand);
				
				if(tosand.equals("Exit")) {
					s.close();
					System.out.println("Connection closed");
					break;
				}
				String received=dis.readUTF();
				System.out.println("Server says:"+received);
			 }
			 sc.close();
			 dis.close();
			 dos.close();
			 
		}catch(Exception e) {
			System.out.println("Client error:"+e);
		}

	}

}
