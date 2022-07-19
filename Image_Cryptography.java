/ Image Cryptography
// MINI PROJECT

import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class Image_Cryptography {

    public static void operate(int key) {
        JFileChooser fileChooser = new JFileChooser();
        fileChooser.showOpenDialog(null);
        File file = fileChooser.getSelectedFile();

        // fileInputStream reader
        try {
            FileInputStream fis = new FileInputStream(file);

            byte[] data = new byte[fis.available()];
            fis.read(data);
            int i = 0;
            for (byte b : data) {
                System.out.println(b);
                data[i] = (byte) (b ^ key);
                i++;
            }

            FileOutputStream fos = new FileOutputStream(file);
            fos.write(data);
            fos.close();
            fis.close();
            JOptionPane.showMessageDialog(null, "Done");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }


    public static void main(String[] args) {

        // CREATING GUI

        JFrame f = new JFrame();                                    // JFrame is a top-level container that provides a window on the screen. (comes in lib : javax.swing.*)
        f.setTitle("Image Encryption");                            // f.setTitle() helps us to name the frame
        f.setSize(500, 500);                       // f.setSize()  helps us to size(lXb)  the opening window
        f.setLocationRelativeTo(null);                            //f.setLocationRelativeTo(null);  this is basically helping us to set the gui  at the center
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);         //.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)  : It causes the application to exit when the application receives a close
                                                                 // window event from the operating system

        // font set
        Font font = new Font("Roboto", Font.BOLD, 25);  // coming from java.awt

        //creating text field
        JTextField textField = new JTextField(10);
        textField.setFont(font);

        f.add(new JLabel("Enter the encryption key:"));

        // creating button
        JButton button = new JButton();
        button.setText("Encrypt");
        button.setFont(font);
        JButton button1 = new JButton();
        button1.setText("Decrypt");
        button1.setFont(font);

        // creating the function of the button
        button.addActionListener(e -> {
            System.out.println("button clicks");
            try {
                String text = textField.getText();
                int temp = Integer.parseInt(text);
                operate(temp);
            } catch (Exception ex) {
                System.out.println("Please Enter a Number !!");
            }
        });

        button1.addActionListener(e -> {
            System.out.println("button clicks");
            try {
                String text = textField.getText();
                int temp = Integer.parseInt(text);
                operate(temp);
            } catch (Exception ex) {
                System.out.println("Please Enter a Number !!");
            }


        });

        //setting layout
        f.setLayout(new FlowLayout());                      // coming from java.awt  : The Java FlowLayout class is used to arrange the
                                                           // components in a line, one after another (in a flow). It is the default layout of the applet or panel.

        // adding button and text field to the gui
        f.add(textField);
        f.add(button);
        f.add(button1);


        f.setVisible(true);       // makes the gui visible
    }
}
