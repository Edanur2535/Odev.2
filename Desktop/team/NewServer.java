package multipleC;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class NewServer {

	public static void main(String[] args)throws IOException {
		
		ServerSocket serverSocket=new ServerSocket(2345);
		System.out.println("Server socket:"+serverSocket);
		Socket srr=null;
		try {
			while(true) {
			srr=serverSocket.accept();
			System.out.println("A new client connected:"+srr);
			DataInputStream dis=new DataInputStream(srr.getInputStream());
			DataOutputStream dos=new DataOutputStream(srr.getOutputStream());
			System.out.println("new thread for this client");
			
			Thread t=new MultiClientHandler(srr,dis,dos);
			t.start();
			}
			
		}
		catch(Exception e) {
			srr.close();
			System.out.println(e);
		}

	}

}
class MultiClientHandler extends Thread{
	final DataInputStream dis;
	final DataOutputStream dos;
	final Socket srr;
	
	public MultiClientHandler (Socket s,DataInputStream dis,DataOutputStream dos) {
		this.srr=s;
		this.dis=dis;
		this.dos=dos;
}
	public void run() {
		String received;
		while(true) {
			try {
				dos.writeUTF("Send message to server");
				received=dis.readUTF();
				
				if(received.equals("Exit")) {
					System.out.println("Client"+this.srr+"send exit...");
					System.out.println("Closing the connection");
					this.srr.close();
					System.out.println("Connection closed");
					break;
				}
				dos.writeUTF(received);
				System.out.println("Response of client"+received);
			}
			catch (Exception e) {
				System.out.println(e);
				}
		}
	
	try {
		this.dis.close();
		this.dos.close();
	}catch (Exception e) {
		System.out.println("Error:"+e);
	}
}
}
