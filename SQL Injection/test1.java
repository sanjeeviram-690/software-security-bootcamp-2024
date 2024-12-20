import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class test1 {
    public static void main(String[] args) {
        String userId = "someUserInput";  // Assume this is user input
        String query = "SELECT * FROM Users WHERE UserId = '" + userId + "'";

        try {
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "root", "password");
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                System.out.println("User ID: " + rs.getString("UserId"));
                System.out.println("User Name: " + rs.getString("UserName"));
            }

            rs.close();
            stmt.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
