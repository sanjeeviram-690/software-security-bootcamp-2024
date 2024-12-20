import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class test2 {
    public static void main(String[] args) {
        ArrayList<String> filters = new ArrayList<>();
        String userInput = "someUserInput";  // Assume this is user input

        if (userInput != null && !userInput.isEmpty()) {
            filters.add("column = '" + userInput + "'");
        }

        String query = "SELECT * FROM table WHERE " + String.join(" AND ", filters);

        try {
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "root", "password");
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                System.out.println("Column: " + rs.getString("column"));
            }

            rs.close();
            stmt.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
