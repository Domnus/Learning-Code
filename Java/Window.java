import javax.swing.JFrame;
import javax.swing.JLabel;

public class Window{
	public static void main(String args[]){
		JFrame window = new JFrame();

		window.setTitle("My Window");
		window.setSize(800, 600);
		window.setVisible(true);

		JLabel label = new JLabel();
		label.setText("My Label");
		
		window.add(label);	
	}
}
