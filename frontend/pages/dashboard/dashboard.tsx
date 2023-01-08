import get_cookies from "../../utils/cookies/get_cookies";

const username = get_cookies("username");
const Dashboard = () => {
  return (
    <>
      <title>Dashboard</title>
      <h1>Welcome {username}</h1>
    </>
  );
};

export default Dashboard;
