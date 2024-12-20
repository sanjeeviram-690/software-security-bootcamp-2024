import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.List;

public class SqlInjectionExample {

    public static void main(String[] args) {
        String userIds = "1,2,3"; // Example of dynamic list construction
        String statusCondition = "active";
        getUserData(userIds, statusCondition);
    }

    public static void getUserData(String userIds, String statusCondition) {
        Connection connection = null;
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;

        try {
            
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "user", "password");

            String query = "SELECT * FROM users WHERE user_id IN (" + userIds + ") " +
                           "AND status = '" + statusCondition + "'";
            
            preparedStatement = connection.prepareStatement(query);
            resultSet = preparedStatement.executeQuery();

            
            while (resultSet.next()) {
                System.out.println("User ID: " + resultSet.getInt("user_id"));
                System.out.println("Status: " + resultSet.getString("status"));
            }

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            
            try {
                if (resultSet != null) resultSet.close();
                if (preparedStatement != null) preparedStatement.close();
                if (connection != null) connection.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
